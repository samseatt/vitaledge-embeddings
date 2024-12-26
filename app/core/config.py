# File: vitaledge-embeddings/app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    backend: str = "local"  # Default backend
    openai_api_key: str = None

    class Config:
        env_file = ".env"

settings = Settings()
