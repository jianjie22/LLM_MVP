# app/database.py

from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models import Conversation  # We'll create this model soon
import asyncio
import os


MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongodb:27017")
DB_NAME = "llm_db"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]


# This should be called during FastAPI startup
async def init_db():
    await init_beanie(database=db, document_models=[Conversation])
