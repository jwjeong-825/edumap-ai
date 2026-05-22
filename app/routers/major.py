from fastapi import APIRouter
from app.services.major_service import (
    search_majors,
    search_by_university,
    search_by_region
)

router = APIRouter()


@router.get("/recommend")
def recommend(keyword: str, limit: int = 50, offset: int = 0):
    data = search_majors(keyword, limit, offset)

    return {
        "type": "major_keyword",
        "keyword": keyword,
        **data
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
