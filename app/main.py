"""
Main application entry point for the AI API Suite using FastAPI.

This module initializes the FastAPI app with metadata (title, description, version) 
loaded from the settings and registers API routers.

"""

from fastapi import FastAPI
from app.routes import summarizer
from app.core.settings import settings
from app.core.loggers import logger

logger.info(f"Starting {settings.app_name} v{settings.version} in {settings.environment} mode.")

app = FastAPI(
    title=settings.app_name,
    description=settings.description,
    version=settings.version
)

# Register routers
app.include_router(summarizer.router, prefix="/summarizer", tags=["Summarizer"])
logger.info("Router registered: /summarizer")
