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
