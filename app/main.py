# /app/main.py

from fastapi import FastAPI
from contextlib import asynccontextmanager
from . import models
from .database import engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("서버 시작: 데이터베이스 테이블 생성을 시도합니다.")
    # 이 코드가 models.py의 모든 테이블을 생성합니다.
    models.Base.metadata.create_all(bind=engine)
    yield
    print("서버 종료.")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"message": "Siseon backend is running!"}