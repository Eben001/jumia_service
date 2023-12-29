from beanie import Document


class Product(Document):
    product_link: str
    product_name: str
    image_url: str
    original_price: str
    discount_price: str
    discount_percentage: str

    class Config:
        schema_extra = {
            "example": {
                "product_name": "",
                "product_link": "",
                "image_url": "",
                "original_price": "₦51,949",
                "discount_price": "₦25,975",
                "discount_percentage": "-50%",
            }
        }

    class Settings:
        name = "automobile"
