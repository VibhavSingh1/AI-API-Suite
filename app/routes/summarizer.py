"""
Summarizer API routes.

Provides a POST endpoint to summarize input text using a transformer model.

Endpoints:
    - POST /summarizer/summarize: Returns a summarized version of the given text.
"""

from fastapi import HTTPException, APIRouter
from app.models.summarizer import SummarizationRequest, SummarizationResponse
from fastapi.responses import JSONResponse
from app.services.summarizer_service import get_summarizer, summarize_text

router = APIRouter()


@router.post('/summarize', response_model=SummarizationResponse)
def summarize(request: SummarizationRequest):
    """
    Summarizes the given text input using a preloaded transformer model.

    Args:
        request (SummarizationRequest): The input data containing the text and optional config.

    Returns:
        SummarizationResponse: The summarized version of the input text.
    """

    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Input text cannot be empty")

    # Get the summarizer model
    summarizer = get_summarizer()
    if summarizer is None:
        raise HTTPException(status_code=500, detail="Summarization model unvailable")

    try:
        summary = summarize_text(
            model=summarizer,
            text=request.text,
            max_length=request.max_length,
            min_length=request.min_length,
            do_sample=request.do_sample
        )

        if not summary or not isinstance(summary, str):
            raise HTTPException(status_code=500, detail="Generated summary is invalid or empty.")

        return JSONResponse(
            status_code=200,
            content=SummarizationResponse(
                summary=summary,
                char_count=len(summary),
                word_count=len(summary.split())
                ).model_dump()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Summarization failed: {str(e)}")