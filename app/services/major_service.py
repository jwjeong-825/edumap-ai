import pandas as pd


def load_major_data():
    raw = pd.read_excel("app/data/majors.xlsx", header=None)

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

    df = df.dropna(subset=["학교명", "학과명"])
    df = df[df["학과상태"] != "폐지"]

    df = df[
        ~df["학과특성"].astype(str).str.contains("대학원", na=False)
    ]

    df = df[
        ~df["학교명"].astype(str).str.contains("대학원", na=False)
    ]

    df = df[
        ~df["학교명"].astype(str).str.contains("사내", na=False)
    ]

    df = df[
        ~df["학교명"].astype(str).str.contains("사이버", na=False)
    ]

    df = df[
        ~df["학교명"].astype(str).str.contains("방송통신", na=False)
    ]

    df = df[
        ~df["학교명"].astype(str).str.contains("기능", na=False)
    ]

    df = df.drop_duplicates(
        subset=["학교명", "학과명", "학과소재지"]
    )

    return df


MAJOR_DF = load_major_data()


def paginate_results(results, limit: int, offset: int):
    total_count = len(results)
    paginated = results[offset:offset + limit]

    return {
        "total_count": total_count,
        "count": len(paginated),
        "limit": limit,
        "offset": offset,
        "has_more": offset + limit < total_count,
        "results": paginated
    }


def search_majors(keyword: str, limit: int = 50, offset: int = 0):
    keyword = keyword.strip()

    results = []

    for _, row in MAJOR_DF.iterrows():
        score = 0

        major_name = str(row["학과명"])
        university_name = str(row["학교명"])
        middle_category = str(row["표준중계열"])
        small_category = str(row["표준소계열"])

        if keyword in major_name:
            score += 3

        if keyword in middle_category:
            score += 2

        if keyword in small_category:
            score += 1

        if keyword in university_name:
            score += 1

        if score > 0:
            row_data = row.to_dict()
            row_data["score"] = score
            results.append(row_data)

    results = sorted(
        results,
        key=lambda item: item["score"],
        reverse=True
    )

    return paginate_results(results, limit, offset)


def search_by_university(university: str, limit: int = 50, offset: int = 0):
    result = MAJOR_DF[
        MAJOR_DF["학교명"]
        .astype(str)
        .str.contains(university, case=False, na=False)
    ]

    results = result.to_dict(orient="records")

    return paginate_results(results, limit, offset)


def search_by_region(region: str, limit: int = 50, offset: int = 0):
    result = MAJOR_DF[
        MAJOR_DF["대학소재지"]
        .astype(str)
        .str.contains(region, case=False, na=False)
    ]

    results = result.to_dict(orient="records")

    return paginate_results(results, limit, offset)
