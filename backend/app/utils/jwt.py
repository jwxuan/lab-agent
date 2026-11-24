from datetime import datetime, timedelta

import jwt

from app.config import get_settings


def create_access_token(user_id: int) -> str:
    """创建JWT token"""
    expire = datetime.now() + timedelta(hours=get_settings().JWT_EXPIRE_HOURS)

    payload = {"user_id": user_id, "exp": expire}  # exp是固定key，不能写成别的

    return jwt.encode(
        payload, get_settings().JWT_SECRET_KEY, algorithm=get_settings().JWT_ALGORITHM
    )


def decode_access_token(token: str) -> dict:
    """解析JWT token"""
    try:
        payload = jwt.decode(
            token,
            get_settings().JWT_SECRET_KEY,
            algorithms=[get_settings().JWT_ALGORITHM],
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")
