import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_ai_recommendation(user_input: str):

    prompt = f"""
사용자의 관심 분야를 분석하고
관련 학과를 추천해주세요.

사용자 입력:
{user_input}

다음 형식으로 자연스럽게 설명해주세요:
- 어떤 계열과 관련 있는지
- 추천 학과
- 왜 추천되는지

너무 길지 않게 4~5줄 정도로 작성해주세요.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",

        messages=[
            {
                "role": "system",
                "content": "당신은 진로 및 학과 추천 AI입니다."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.7,
        max_tokens=300
    )

    return response.choices[0].message.content

def extract_search_keywords(user_input: str):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",

        messages=[
            {
                "role": "system",
                "content":
                """
당신은 대학 학과 검색 키워드 추출 AI입니다.

사용자 입력을 보고
실제 대학 학과명 또는 학문 분야 키워드
최대 3개만 추출하세요.

규칙:

1.
직업, 꿈, 감정, 일반 단어 금지

2.
반드시 대학 학과 검색 가능한
학문/전공 키워드만 출력

3.
설명 금지

4.
쉼표로만 반환

예시:

입력:
게임 개발자가 되고 싶어요
출력:
게임,소프트웨어,컴퓨터

입력:
AI랑 반도체 둘 다 관심 있어요
출력:
인공지능,반도체,전자

입력:
병원에서 일하고 싶어요
출력:
간호,보건,의학
"""
            },
            {
                "role": "user",
                "content": user_input
            }
        ],

        temperature=0.1,
        max_tokens=40
    )

    result = response.choices[0].message.content.strip()

    keywords = [
        keyword.strip()
        for keyword in result.split(",")
    ]

    return keywords
