# File: vitaledge-embeddings/app/services/local_service.py
from sentence_transformers import SentenceTransformer
import logging

# Logger for this file
logger = logging.getLogger(__name__)

class LocalEmbeddingService:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")  # Replace with a suitable HuggingFace model
    
    def generate_embeddings(self, texts):
        logger.debug(f"service/generate_embeddings called with texts {texts}")
        return self.model.encode(texts).tolist()
