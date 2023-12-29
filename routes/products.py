from typing import List

from fastapi import APIRouter

from models.product import Product

product_router = APIRouter(
    tags=["Products"]
)


@product_router.get("/automobile", response_model=List[Product])
async def get_automobile_category() -> List[Product]:
    products = await Product.find_all().to_list()
    return products


@product_router.post("/add_new_product")
async def create_product(product: Product) -> dict:
    await product.create()
    return {
        "message": "Product created successfully"
    }
