# /app/config.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # .env 파일에서 읽어올 환경 변수들을 여기에 변수로 정의
    DATAbase_URL : str
    OPENAI_API_KEY : str
    JWT_SECRET_KEY : str

    class Config:
        # .env 파일을 읽어오도록 설정
        env_file = ".env"

# 다른 파일에서 이 settings 객체를 import 해서 사용할 수 있도록 인스턴스 생성
settings = Settings()