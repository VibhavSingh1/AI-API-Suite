from pydantic import ConfigDict, BaseModel
from typing import Optional


class SummarizationRequest(BaseModel):
    text: str
    max_length: Optional[int] = 130
    min_length: Optional[int] = 30
    do_sample: Optional[bool] = False

    model_config = ConfigDict(
        extra="forbid"
    )


class SummarizationResponse(BaseModel):
    summary: str