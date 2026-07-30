from fastapi import APIRouter

from app.schemas.catalog import ProductRead

router = APIRouter(prefix="/catalog", tags=["catalog"])


@router.get("/featured", response_model=list[ProductRead])
def featured_products():
    return [
        ProductRead(
            id="1",
            slug="smart-travel-pack",
            title="Smart Travel Pack",
            price=79,
            image="https://images.unsplash.com/photo-1553062407-98eeb64c6a62",
            badge="AI Trending"
        ),
        ProductRead(
            id="2",
            slug="ergonomic-led-desk",
            title="Ergonomic LED Desk",
            price=129,
            image="https://images.unsplash.com/photo-1518455027359-f3f8164ba6bd",
            badge="High margin"
        ),
        ProductRead(
            id="3",
            slug="minimal-sneakers",
            title="Minimal Performance Sneakers",
            price=64,
            image="https://images.unsplash.com/photo-1542291026-7eec264c27ff",
            badge="Fast ship"
        ),
    ]
