# 👁️세상을 바라보는 새로운 *'SISEON'* 👁️
> 뉴스와 시사에 관심은 많지만 어렵고 재미없어 꾸준히 읽지 못하는 20대 청년들을 위한 앱입니다.  

이 레포지토리는 Flutter로 만들어진 [시선 레포지토리](https://github.com/seoeng/siseon-frontend)와 통신합니다.


## 🚀 개발기간
- 2025.08.27(수)~


## 🌟 주요기능
* **AI 요약:** 바쁜 당신을 위해 AI가 매일 새로운 뉴스를 세 문장으로 요약해줘요.
* **오늘의 퀴즈:** 요약된 뉴스를 바탕으로 생성된 퀴즈를 풀며 핵심 내용을 완벽하게 익힐 수 있어요.
* **성장 트래킹:** 퀴즈를 풀며 얻은 포인트와 연속 학습 기록(스트릭)으로 나의 성장을 한눈에 확인하세요.
* **관심사 필터:** 내가 원하는 분야의 뉴스만 골라볼 수 있어요. (개발 예정)
  

## 🛠️ 기술 스택

| 구분 | 기술명 |
|---|---|
| **프론트엔드** | ![Flutter](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white) ![Dart](https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white) |
| **백엔드** | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white) |
| **데이터베이스**| ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white) |
| **AI** | ![OpenAI](https://img.shields.io/badge/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white) |
| **배포** | ![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white) |

## ⚙️ 설치 및 실행 방법

이 프로젝트를 로컬 환경에서 실행하기 위한 단계별 가이드입니다.

### 1. 사전 요구사항

* [Python 3.9+](https://www.python.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [Git](https://git-scm.com/)

### 2. 프로젝트 클론 및 설정

```bash
# 1. GitHub에서 프로젝트를 클론합니다.
git clone [https://github.com/당신의_깃허브_ID/umteu-server.git](https://github.com/당신의_깃허브_ID/umteu-server.git)
cd umteu-server

# 2. Python 가상환경을 생성하고 활성화합니다.
# (Windows)
python -m venv .venv
.venv\Scripts\activate
# (macOS/Linux)
python -m venv .venv
source .venv/bin/activate

# 3. 필요한 라이브러리를 설치합니다.
pip install -r requirements.txt
