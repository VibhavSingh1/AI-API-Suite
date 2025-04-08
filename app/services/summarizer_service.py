"""
Module to store methods and services related to the summarizer service
"""

from transformers import pipeline, Pipeline
from typing import Optional
import logging

logger = logging.getLogger(__name__)

# Singleton-like global variable for the summarizer model
_summarizer: Optional[Pipeline] = None

def get_summarizer() -> Optional[Pipeline]:
    """
    Loads and returns the summarization pipeline.
    Ensures the model is only loaded once using a global instance.

    Returns:
        Optional[Pipeline]: Hugging Face summarization pipeline if loaded successfully.
    """
    global _summarizer
    if _summarizer is None:
        try:
            logger.info("Loading summarization model...")
            _summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
            logger.info("Summarizer model loaded successfully.")
        except Exception as e:
            logger.error(f"Error loading summarization model: {e}")
            _summarizer = None
    else:
        logger.info("Existing summarization model found!")
    return _summarizer


def summarize_text(
    model: Pipeline, text: str, max_length: int, min_length: int, do_sample: bool
) -> str:
    """
    Summarizes the input text using the provided model.

    Args:
        model (Pipeline): Hugging Face summarization pipeline.
        text (str): The text to be summarized.
        max_length (int): Maximum length of the summary.
        min_length (int): Minimum length of the summary.
        do_sample (bool): Whether or not to use sampling.

    Returns:
        str: The summarized text.
    """
    logger.debug("Performing text summarization.")
    summary = model(
        text,
        max_length=max_length,
        min_length=min_length,
        do_sample=do_sample
    )[0]["summary_text"]
    return summary