# File: vitaledge-embeddings/app/services/openai_service.py
from openai import OpenAI
import os
from app.core.config import settings
import logging

# Logger for this file
logger = logging.getLogger(__name__)

class OpenAIEmbeddingService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)
    
    async def generate_embeddings(self, texts):
        response = self.client.embeddings.create(
            input=texts,
            model="text-embedding-ada-002"
        )
        return [embedding.embedding for embedding in response.data]
