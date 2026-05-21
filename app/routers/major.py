from fastapi import APIRouter
from app.services.major_service import (
    search_majors,
    search_by_university,
    search_by_region
)

router = APIRouter()


@router.get("/recommend")
def recommend(keyword: str):
    results = search_majors(keyword)

    return {
        "type": "major_keyword",
        "keyword": keyword,
        "count": len(results),
        "results": results
    }


@router.get("/search/university")
def search_university(university: str):
    results = search_by_university(university)

    return {
        "type": "university",
        "university": university,
        "count": len(results),
        "results": results
    }


@router.get("/search/region")
def search_region(region: str):
    results = search_by_region(region)

    return {
        "type": "region",
        "region": region,
        "count": len(results),
        "results": results
    }
