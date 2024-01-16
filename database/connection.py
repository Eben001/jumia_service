import os

import motor.motor_asyncio
from beanie import init_beanie
from dotenv import load_dotenv

from models.product import *

load_dotenv('.env')


async def init_db():
    mongodb_url = os.getenv("MONGODB_URL")  # Retrieve MongoDB URL from environment variable

    if not mongodb_url:
        raise ValueError("MongoDB URL not found in environment variables")
    # Specify your document models in the list
    document_models = [MensFashion, WomenClothing, WomenJewelry, HealthBeauty, Fragrance]

    client = motor.motor_asyncio.AsyncIOMotorClient(mongodb_url)
    await init_beanie(database=client.Product, document_models=document_models)
