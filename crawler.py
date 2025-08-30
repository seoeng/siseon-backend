# crawler.py

import requests
from bs4 import BeautifulSoup
from app.database import SessionLocal
from app.models import Article

# 데이터베이스 세션 준비
db = SessionLocal()

# 크롤링할 RSS 피드 주소 (ex: 연합뉴스TV 속보)
RSS_URL = "https://www.yonhapnewstv.co.kr/browse/feed/"

try:
    # requests로 웹사이트 내용 가져오기
    response = requests.get(RSS_URL)
    response.raise_for_status() # 오류가 있으면 예외 발생

    # BeautifulSoup으로 내용 분석
    soup = BeautifulSoup(response.content, 'lxml')

    # 'item' 태그를 모두 찾아서 각 기사 정보 추출
    items = soup.find_all('item')
    print(f"총 {len(items)}개의 기사를 찾았습니다. 데이터베이스에 저장합니다...")

    for item in items:
        content_encoded = item.find('content:encoded')
        title_tag = content_encoded.find('span', class_='yna_title') if content_encoded else None
        
        if not title_tag:
            print("제목을 찾을 수 없어 건너뜀")
            continue

        title_text = title_tag.text.strip()

        link_tag = item.find('link')
        link_text = link_tag.next_sibling.strip() if link_tag else "링크 없음"
        

        # 데이터로 Article 객체 만들기
        new_article = Article(
            title=title_text,
            content=link_text # 일단 content에 link 넣어놓음!
        )
        db.add(new_article)

    # 모든 새로운 기사 한번에 데이터베이스에 저장
    db.commit()
    print("데이터베이스 저장을 시도했습니다.")


except requests.exceptions.RequestException as e:
    print(f"URL에 접속하는 중 오류 발생: {e}")
    db.rollback() # 오류 발생 시 변경사항 되돌림
except Exception as e:
    print(f"오류 발생: {e}")
    db.rollback()
finally:
    # 작업 끝나면 세션 닫아줌
    db.close()