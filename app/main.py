"""
Main application entry point for the AI API Suite using FastAPI.

This module initializes the FastAPI app with metadata (title, description, version) 
loaded from the settings and registers API routers.

"""

from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes import summarizer
from app.core.settings import settings
from app.core.loggers import logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Starting app {settings.app_name} v{settings.version} in {settings.environment} mode.")
    yield
    logger.info(f"🛑 Shutting app {settings.app_name} v{settings.version} in {settings.environment} mode.")  

app = FastAPI(
    title=settings.app_name,
    description=settings.description,
    version=settings.version,
    lifespan=lifespan
)

# Register routers
app.include_router(summarizer.router, prefix="/summarizer", tags=["Summarizer"])