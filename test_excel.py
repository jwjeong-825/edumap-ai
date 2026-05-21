import pandas as pd

# 엑셀 전체를 헤더 없이 읽기
raw = pd.read_excel("app/data/majors.xlsx", header=None)

# 8번째 줄부터 실제 데이터
df = raw.iloc[7:].copy()

# 우리가 필요한 컬럼만 직접 이름 붙이기
df = df[[2, 8, 12, 14, 15, 16, 17, 18, 22, 23]]

df.columns = [
    "학교명",
    "대학소재지",
    "학과명",
    "학과특성",
    "학과상태",
    "표준대계열",
    "표준중계열",
    "표준소계열",
    "학과소재지",
    "학과상세소재지"
]

print(df.head())
print(df.columns)
