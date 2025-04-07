from fastapi import HTTPException, APIRouter
from app.models.summarizer import SummarizationRequest, SummarizationResponse

router = APIRouter()


@router.post('/summarize', response_model=SummarizationResponse)
def summarize(request: SummarizationRequest):
    # summarizer = get_summarizer()

    return SummarizationResponse(summary="Endpoint is Active!")