from app.services.ai_service import (
    generate_ai_recommendation,
    extract_search_keywords
)
from app.services.ai_service import generate_ai_recommendation
from fastapi import APIRouter
from app.services.major_service import (
    search_majors,
    search_by_university,
    search_by_region
)

router = APIRouter()


@router.get("/recommend")
def recommend(keyword: str, limit: int = 50, offset: int = 0):

    keywords = extract_search_keywords(keyword)

    all_results = []

    for k in keywords:
        data = search_majors(k, limit=9999, offset=0)
        all_results.extend(data["results"])

    unique_results = []

    seen = set()

    for item in all_results:

        key = (
            item["학교명"],
            item["학과명"]
        )

        if key not in seen:
            seen.add(key)
            unique_results.append(item)

    total_count = len(unique_results)

    paginated = unique_results[
        offset:offset + limit
    ]

    return {
        "type": "ai_major_search",
        "keyword": keyword,
        "ai_keywords": keywords,
        "total_count": total_count,
        "count": len(paginated),
        "limit": limit,
        "offset": offset,
        "has_more": offset + limit < total_count,
        "results": paginated
    }


@router.get("/search/university")
def search_university(university: str, limit: int = 50, offset: int = 0):
    data = search_by_university(university, limit, offset)

    return {
        "type": "university",
        "university": university,
        **data
    }


@router.get("/search/region")
def search_region(region: str, limit: int = 50, offset: int = 0):
    data = search_by_region(region, limit, offset)

    return {
        "type": "region",
        "region": region,
        **data
    }
@router.get("/ai/recommend")
def ai_recommend(keyword: str):

    result = generate_ai_recommendation(keyword)

    return {
        "keyword": keyword,
        "recommendation": result
    }
