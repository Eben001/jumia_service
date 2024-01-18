from typing import Optional

from beanie import Document


class BaseModel(Document):
    name: str
    price: Optional[int]
    original_price: Optional[int]
    discount_percentage: Optional[int]
    seller_score: Optional[int]
    product_rating: Optional[float]
    product_link: str
    image_url: str

    class Config:
        schema_extra = {
            "example": {
                "name": "",
                "price": 100,
                "original_price": 949,
                "discount_percentage": 10,
                "seller_score": 12,
                "product_rating": 5.0,
                "product_link": "",
                "image_url": "",
            }
        }

class MensFashion(BaseModel):
    class Settings:
        name = "mens_fashion"


class WomenClothing(BaseModel):
    class Settings:
        name = "women_clothing"


class WomenJewelry(BaseModel):
    class Settings:
        name = "women_jewelry"


class HealthBeauty(BaseModel):
    class Settings:
        name = "health_beauty"


class Fragrance(BaseModel):
    class Settings:
        name = "fragrance"
