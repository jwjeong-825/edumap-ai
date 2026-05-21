import pandas as pd


def load_major_data():
    raw = pd.read_excel(
        "app/data/majors.xlsx",
        header=None
    )

    df = raw.iloc[7:].copy()

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

    # 학교명, 학과명 없는 데이터 제거
    df = df.dropna(subset=["학교명", "학과명"])

    # 폐지 학과 제거
    df = df[df["학과상태"] != "폐지"]

    # 대학원 관련 데이터 제거
    df = df[
        ~df["학과특성"].astype(str).str.contains("대학원", na=False)
    ]

    df = df[
        ~df["학교명"].astype(str).str.contains("대학원", na=False)
    ]

    # 사내대학 제거
    df = df[
        ~df["학교명"].astype(str).str.contains("사내", na=False)
    ]

    # 사이버대학 제거
    df = df[
        ~df["학교명"].astype(str).str.contains("사이버", na=False)
    ]

    # 방송통신대학 제거
    df = df[
        ~df["학교명"].astype(str).str.contains("방송통신", na=False)
    ]

    # 기능대학 제거
    df = df[
        ~df["학교명"].astype(str).str.contains("기능", na=False)
    ]

    # 중복 제거
    df = df.drop_duplicates(
        subset=["학교명", "학과명", "학과소재지"]
    )

    return df


MAJOR_DF = load_major_data()


def search_majors(keyword: str):
    result = MAJOR_DF[
        MAJOR_DF["학과명"]
        .astype(str)
        .str.contains(keyword, case=False, na=False)
    ]

    result = result.head(50)

    return result.to_dict(orient="records")


def search_by_university(university: str):
    result = MAJOR_DF[
        MAJOR_DF["학교명"]
        .astype(str)
        .str.contains(university, case=False, na=False)
    ]

    result = result.head(50)

    return result.to_dict(orient="records")


def search_by_region(region: str):
    result = MAJOR_DF[
        MAJOR_DF["대학소재지"]
        .astype(str)
        .str.contains(region, case=False, na=False)
    ]

    result = result.head(50)

    return result.to_dict(orient="records")
