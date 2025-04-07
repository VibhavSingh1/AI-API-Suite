from fastapi import FastAPI
from app.routes import summarizer

app = FastAPI(
    title="AI API Suite",
    description="A collection of AI-powered APIs like summarization, sentiment analysis, etc.",
    version="1.0.0"
)

# Register routers
app.include_router(summarizer.router, prefix="/summarizer", tags=["Summarizer"])
