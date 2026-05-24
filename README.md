# 🤖 EduMap AI

공공데이터와 GPT API를 활용한 **AI 기반 진로·학과 탐색 서비스**입니다.

사용자가 자연어로 관심 분야와 진로 방향을 입력하면, AI가 이를 분석하고 관련 학과 키워드를 추출하여 전국 대학 학과 정보를 탐색·추천합니다.

---

## 🚀 Project Overview

EduMap AI는 전국 대학 학과 공공데이터와 GPT API를 결합해 사용자의 관심사와 진로 방향에 맞는 학과를 탐색할 수 있도록 만든 AI 서비스입니다.

기존의 단순 키워드 검색 방식에서 벗어나, 자연어 입력을 AI가 이해하고 실제 공공데이터 검색과 연결하는 구조를 목표로 개발했습니다.

예시:

- "게임 개발자가 되고 싶어요"
- "AI랑 반도체 둘 다 관심 있어요"
- "병원에서 일하고 싶어요"

---

## ✨ Main Features

### 🤖 AI 기반 학과 탐색
- GPT API 기반 자연어 분석
- 학과 검색 키워드 자동 추출
- AI 추천 설명 생성

### 🔎 공공데이터 기반 검색
- 전국 대학 학과 데이터 활용
- 학과 / 대학 / 계열 탐색
- 중복 제거 및 결과 정렬

### 📊 검색 결과 UX
- 전체 검색 결과 개수 표시
- 50개 단위 더보기 기능
- 학과 카드 UI 제공

### ⭐ 사용자 편의 기능
- 최근 검색어 저장
- 즐겨찾기 저장 / 삭제
- 학과 정보 검색 버튼

### 🎨 Modern UI
- 자연어 기반 단일 검색창
- AI 추천 분석 박스
- 계열별 아이콘
- 반응형 UI

---

## 🛠 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

---

## 🏗 Architecture

```text
사용자 자연어 입력
        ↓
GPT API 키워드 추출
        ↓
FastAPI Backend
        ↓
교육 공공데이터 검색
        ↓
학과 추천 + AI 설명 제공
```

---

## 📂 Project Structure

```bash
edumap-ai/
│
├── app/
│   ├── data/
│   │   └── majors.xlsx
│   │
│   ├── routers/
│   │   └── major.py
│   │
│   ├── services/
│   │   ├── major_service.py
│   │   └── ai_service.py
│   │
│   └── main.py
│
├── index.html
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Run Project

```bash
cd ~/edumap-ai
source venv/bin/activate
python3 -m uvicorn app.main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

---

## 📸 Preview

(프로젝트 UI 캡처 예정)

---

## 🎯 Future Plans

- 입시 데이터 연동
- AI 추천 정확도 향상
- RAG 기반 추천 확장
- Docker 환경 구성
- AWS 배포
- Demo / 발표 영상 제작

---

## 👨‍💻 Developer

정주원  
Chosun University  
AI·SW Engineering
