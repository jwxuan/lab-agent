from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.database import Base, engine
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI()

# 路由挂载
app.include_router(auth_router)


@app.get("/")
def root():
    return {"message": "Hello FastAPI"}
