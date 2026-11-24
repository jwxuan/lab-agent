from fastapi import FastAPI

from app.api import api
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

# 路由挂载
app.include_router(api)


@app.get("/")
def root():
    return {"message": "Hello FastAPI"}
