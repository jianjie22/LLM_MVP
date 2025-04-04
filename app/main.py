# app/main.py

from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes import router
from app.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await init_db()
    yield
    # Shutdown
    # You could clean up resources here if needed

app = FastAPI(title="LLM_MVP", lifespan=lifespan)

app.include_router(router)
