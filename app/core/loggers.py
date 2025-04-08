"""
Logging Configuration Module.

This module sets up the application's logging system, ensuring that logs are saved
to a dedicated `logs/` directory with filenames based on the current date.

Usage:
Import and use the `logger` object from this module across your application for consistent logging.

Example:
    from app.core.logger import logger
    logger.info("Application started.")
"""


import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
import sys
from datetime import datetime
from app.core.settings import settings

# Directory to store logs
LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Logger name to be used globally
LOGGER_NAME = "app_logger"

# Get logger instance
logger = logging.getLogger(LOGGER_NAME) # Object to be imported
LOG_LEVEL = getattr(logging, settings.log_level.upper(), logging.INFO)
logger.setLevel(LOG_LEVEL)

# Prevent duplicate handlers on reloads
if not logger.hasHandlers():
    # Console handler (prints to terminal)
    console_handler = logging.StreamHandler(sys.stdout)
    console_formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # File handler (rotates daily)
    file_handler = TimedRotatingFileHandler(
        filename=LOG_DIR / f"{datetime.now().strftime('%Y%m%d')}.txt",
        when="midnight",
        interval=1,
        backupCount=7,  # Keep 7 days of logs
        encoding="utf-8",
        utc=True  # Use UTC or remove it for local timezone
    )
    file_formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
