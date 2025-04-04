# app/main.py

from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes import router
from app.database import init_db
from dotenv import load_dotenv
import os

load_dotenv()

# You can now get it with:
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print(OPENAI_API_KEY)  # For debugging purposes, remove in production
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await init_db()
    yield
    # Shutdown
    # You could clean up resources here if needed

app = FastAPI(title="LLM_MVP", lifespan=lifespan)

app.include_router(router)
