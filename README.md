# 🎓 EduMap AI

키워드 기반 탐색을 통해 전국 대학의 관련 학과 정보를 빠르게 확인할 수 있는 교육 데이터 검색 서비스입니다.

---

## 🚀 Project Overview

EduMap AI는 교육 공공데이터를 기반으로 사용자가 관심 키워드, 지역, 학교명을 입력하면 관련 학과 정보를 탐색할 수 있도록 만든 웹 서비스입니다.

단순 검색뿐 아니라 학과 계열 분석, 최근 검색어, 즐겨찾기 기능 등을 제공하여 실제 서비스 형태를 목표로 개발했습니다.

---

## ✨ Main Features

### 🔎 학과 키워드 검색
- 관심 키워드 기반 학과 탐색
- 검색 정확도 개선 로직 적용
- 관련 계열 우선 정렬

### 🏫 학교명 검색
- 특정 대학의 학과 조회 가능

### 📍 지역 검색
- 지역 기반 대학/학과 탐색

### 🤖 AI 추천 분석
- 입력 키워드 기반 연관 계열 추천
- 향후 GPT API 기반 AI 추천 기능 확장 예정

### ⭐ 사용자 편의 기능
- 최근 검색어 저장
- 즐겨찾기 기능
- 반응형 UI 지원

---

## 🛠 Tech Stack

### Backend
- Python
- FastAPI
- Pandas

### Frontend
- HTML
- CSS
- JavaScript

### Data
- 교육 공공데이터
- Excel 기반 학과 데이터 처리

### DevOps / Environment
- Git
- GitHub
- Linux (Ubuntu)

---

## 📂 Project Structure

```bash
edumap-ai/
│
├── app/
│   ├── data/
│   ├── routers/
│   ├── services/
│   └── main.py
│
├── static/
├── index.html
├── requirements.txt
└── README.md
```

---

## ⚙️ Run Project

### 1. 가상환경 생성

```bash
python3 -m venv venv
```

### 2. 가상환경 실행

```bash
source venv/bin/activate
```

### 3. 패키지 설치

```bash
pip install -r requirements.txt
```

### 4. 서버 실행

```bash
python3 -m uvicorn app.main:app --reload
```

---

## 📸 Preview

### 메인 화면
- 키워드 기반 학과 탐색 UI
- AI 추천 분석 영역
- 최근 검색어 / 즐겨찾기 기능

---

## 🎯 Future Plans

- GPT API 기반 AI 추천 시스템
- 학과 상세 페이지
- 대학 입시 정보 연동
- Docker 기반 배포
- AWS 클라우드 배포
- RAG 기반 학과 추천 시스템 확장

---

## 👨‍💻 Developer

- 정주원
- Chosun University
- AI·SW Engineering
