from pydantic import BaseModel


class ProductRead(BaseModel):
    id: str
    slug: str
    title: str
    price: float
    rating: float = 4.8
    image: str
    badge: str = "AI Pick"
    delivery: str = "5-8 days"
