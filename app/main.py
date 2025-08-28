# /app/main.py

from fastapi import FastAPI
from . import models # models.py 가져오기
from .database import engine # database.py에서 engine 가져오기

# models.py 에서 정의한 모든 테이블을 데이터베이스에 생성
# PostgreSQL의 siseon_db안에 articles 테이블이 생성
models.Base.metadata.create_all(bind=engine)

# FastAPI 앱 인스턴스 생성
app = FastAPI()

# '/api/v1/articles'라는 주소(URL)로 GET 요청이 오면 return
@app.get("/")
def read_root():
    return {"Hello": "Database Setup Coomplete!"}