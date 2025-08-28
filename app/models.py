# /app/models.py

from sqlalchemy import Column, Integer, String, DateTime
from .database import Base
from datetime import datetime, timezone

class Article(Base):
    __tablename__ = "articles"  # 테이블 이름

    # 테이블 컬럼 정의
    article_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    original_url = Column(String, unique=True, index=True)
    source_name = Column(String)
    summary = Column(String)
    published_at = Column(DateTime)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))