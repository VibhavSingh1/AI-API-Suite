"""
Configuration module for the AI API Suite.

This module defines the `Settings` class using Pydantic's `BaseSettings` from the 
`pydantic-settings` package. It reads configuration values from environment variables 
and optionally from a `.env` file.
"""


from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "AI API Suite"
    debug: bool = True               # fallback default
    environment: str = "development" # fallback default
    description: str = "A collection of AI-powered APIs like summarization, sentiment analysis, etc."
    version: str = "1.0.0"

    class Config:
        env_file = ".env"


settings = Settings()

print("APP:", settings.app_name)
print("VERSION:", settings.version)
print("DEBUG:", settings.debug)
print("ENVIRONMENT:", settings.environment)
