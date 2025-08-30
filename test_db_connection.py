# test_db_connection.py

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from app.config import settings # 기존 app/config.py의 settings를 그대로 사용

def test_connection():
    print("--- 데이터베이스 연결 테스트 시작 ---")
    print(f"연결 시도 URL: {settings.DATABASE_URL}")

    try:
        # 데이터베이스에 연결 시도
        engine = create_engine(settings.DATABASE_URL)
        connection = engine.connect()
        
        print("✅ 연결 성공! 데이터베이스와 정상적으로 통신했습니다.")
        connection.close()
        
    except OperationalError as e:
        print("❌ 연결 실패! 데이터베이스에 접속할 수 없습니다.")
        print("--- SQLAlchemy가 알려준 오류 메시지 ---")
        print(e)
        print("------------------------------------")
        print("해결 힌트: .env 파일의 사용자 이름, 비밀번호, 데이터베이스 이름이 정확한지 다시 확인해주세요.")
        
    except Exception as e:
        print(f"❌ 예상치 못한 다른 오류 발생: {e}")

if __name__ == "__main__":
    test_connection()