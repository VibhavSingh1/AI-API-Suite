"""
This module defines Pydantic models for the AI Summarization API.

These models are used for validating incoming API payloads and formatting outgoing responses.
"""

from typing import Optional

from pydantic import BaseModel, ConfigDict


class SummarizationRequest(BaseModel):
    """
    Request body model for text summarization.
    """

    text: str
    max_length: Optional[int] = 130
    min_length: Optional[int] = 30
    do_sample: Optional[bool] = False

    model_config = ConfigDict(extra="forbid")


class SummarizationResponse(BaseModel):
    """
    Response model containing the summarized text.
    """

    summary: str
    char_count: int
    word_count: int
