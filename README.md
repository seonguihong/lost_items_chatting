# Lost Items Chatting

분실물 관리를 위한 Django 기반 AI 챗봇 웹 애플리케이션

---

## 📝 프로젝트 소개

**Lost Items Chatting**은 분실물 정보를 체계적으로 관리하고,  
사용자가 챗봇 인터페이스를 통해 자연어로 손쉽게 분실물을 조회할 수 있도록 만든 Django 기반 웹 서비스입니다.  
챗봇 UI, 이미지/날짜 기반 탐색, 자연어 명사 추출 등 다양한 기능을 제공합니다.

---

## 💡 주요 기능

- **대화형 챗봇 UI**  
  자연어 입력을 통해 분실물 종류, 색상, 날짜 등 조건으로 분실물 조회  
  (예: "빨간색 우산을 잃어버렸어요" → "잃어버린 날짜는 언제인가요?" → 검색 결과 안내)
- **분실물 DB 관리**  
  - 이름, 카테고리, 색상, 날짜, 습득 위치, 이미지 등 다양한 정보 등록/조회
  - 관리자 페이지에서 데이터 직접 관리 가능
- **이미지 기반 분실물 정보 제공**
- **사용자/관리자 로그인 및 권한 분리**
- **반응형·직관적 웹 UI (템플릿 & Static 활용)**
- **다중 앱 구조 (chatbot, login, main)로 유지보수 편리**

---

## 🔍 자연어 기반 분실물 검색

- **한국어 형태소 분석:**  
  KoNLPy의 Hannanum을 활용하여 사용자 질의에서 명사를 추출,  
  이를 표준 색상·카테고리로 정규화해 검색 정확도와 편의성 향상

- **정밀한 다중 조건 검색:**  
  - 입력 질의에서 색상, 태그(카테고리) 자동 인식  
  - 분실 날짜 이후 필터링 등 다양한 조건 조합 가능

- **실시간 챗봇 연동:**  
  - AJAX를 통한 실시간 대화 및 결과 표시  
  - 결과는 JSON으로 받아 2개씩 페이지네이션 UI 제공

---

## 🛠️ 기술 스택

- Python
- Django (MTV 아키텍처, 다중 앱 구조)
- KoNLPy(Hannanum 형태소 분석기)
- HTML/CSS/JavaScript (jQuery)
- AJAX (실시간 챗봇 연동)
- Django Templates & Static/Media 파일 관리
- **Database:** Django 기본 SQLite3


## ⚡️ 설치 및 실행 방법

1. **프로젝트 클론**
    ```bash
    git clone https://github.com/seonguihong/lost_items_chatting.git
    cd lost_items_chatting
    ```

2. **필수 패키지 설치**
    ```bash
    pip install -r requirements.txt
    # (또는: pip install django konlpy 등)
    ```

3. **마이그레이션 및 서버 실행**
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

4. **웹 서비스 접속**
    - 챗봇: `http://127.0.0.1:8000/chatbot/`
    - 관리자: `http://127.0.0.1:8000/admin/`

---

## 📌 주요 코드/작동 방식 예시

- **한국어 명사 추출 및 정규화**
    - KoNLPy(Hannanum)로 명사 추출 → 색상/카테고리 표준화 → DB검색 정밀도 향상
- **실시간 챗봇-서버 연동**
    - AJAX POST로 `/chatbot/search_lost_item/`에 질의 전송, 결과를 JSON으로 받아 UI에 반영
- **2개씩 결과 페이지네이션**
    - 검색 결과가 2개씩 챗봇 UI에 보여지며, 이전/다음 버튼으로 페이지 이동

---
