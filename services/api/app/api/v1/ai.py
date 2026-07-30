from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ai_commerce import AICommerceService

router = APIRouter(prefix="/ai", tags=["ai"])

service = AICommerceService()


class SeoRequest(BaseModel):
    title: str
    keywords: list[str] = []


@router.post("/seo")
def seo(payload: SeoRequest) -> dict[str, str]:
    return service.generate_seo(payload.title, payload.keywords)


@router.get("/opportunity-score")
def opportunity_score(
    margin: float,
    demand: float,
    competition: float
) -> dict[str, float]:
    return {
        "score": service.score_product(
            margin,
            demand,
            competition
        )
    }
