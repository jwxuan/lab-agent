from sqlalchemy.orm import Session

from app.common.exceptions import BusinessException
from app.models.user import User
from app.schemas.auth import LoginRequest, LoginResponse
from app.schemas.user import UserResponse
from app.utils.jwt import create_access_token
from app.utils.password import verify_password


def login(db: Session, data: LoginRequest):
    user = db.query(User).filter(User.username == data.username).first()

    # 判断账号和密码是否正确
    if not user or not verify_password(data.password, user.password):
        raise BusinessException(code=10101, message="账号或密码错误")
    # 验证账号的状态
    if user.status != 1:
        raise BusinessException(code=10102, message="账号或密码错误")
    # 创建token
    token = create_access_token(user.id)
    return LoginResponse(token=token, user=UserResponse.model_validate(user))
