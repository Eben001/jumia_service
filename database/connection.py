import os

from beanie import init_beanie
import motor.motor_asyncio

from models.product import Product
from dotenv import load_dotenv
load_dotenv('.env')


async def init_db():
    mongodb_url = os.getenv("MONGODB_URL")  # Retrieve MongoDB URL from environment variable

    if not mongodb_url:
        raise ValueError("MongoDB URL not found in environment variables")

    client = motor.motor_asyncio.AsyncIOMotorClient(mongodb_url)
    await init_beanie(database=client.Product, document_models=[Product])
