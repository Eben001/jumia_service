from typing import List

from fastapi import APIRouter

from models.product import *

product_router = APIRouter(tags=["Products"])

async def get_special_products(model, discount_percentage=80, seller_score=80, product_rating=4.0, price_limit=10000):
    products = await model.find(
        model.discount_percentage >= discount_percentage,
        model.seller_score >= seller_score,
        model.product_rating >= product_rating,
        model.price < price_limit
    ).to_list()
    return products


@product_router.get("/women_clothing_specials", response_model=List[WomenClothing])
async def get_women_clothing_specials() -> List[WomenClothing]:
    return await get_special_products(WomenClothing)


@product_router.get("/women_jewelry_specials", response_model=List[WomenJewelry])
async def get_women_jewelry_specials() -> List[WomenJewelry]:
    return await get_special_products(WomenJewelry)


@product_router.get("/mens_fashion_specials", response_model=List[MensFashion])
async def get_mens_fashion_specials() -> List[MensFashion]:
    return await get_special_products(MensFashion)


@product_router.get("/health_beauty_specials", response_model=List[HealthBeauty])
async def get_health_beauty_specials() -> List[HealthBeauty]:
    return await get_special_products(HealthBeauty)


@product_router.get("/fragrance_specials", response_model=List[Fragrance])
async def get_fragrance_specials() -> List[Fragrance]:
    return await get_special_products(Fragrance)
