# File: vitaledge-embeddings/app/api/routes/embeddings.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.services.local_service import LocalEmbeddingService
from app.services.openai_service import OpenAIEmbeddingService
from app.core.config import settings
import logging

# Logger for this file
logger = logging.getLogger(__name__)

router = APIRouter()

# Initialize embedding services
local_service = LocalEmbeddingService()
openai_service = OpenAIEmbeddingService()

backend = settings.backend

class EmbeddingsRequest(BaseModel):
    texts: List[str]

@router.post("/generate")
async def generate_embeddings(request: EmbeddingsRequest):
    logger.debug(f"generate_embeddings called with backend {backend} and text {request.texts}")
    if backend == "local":
        embeddings = local_service.generate_embeddings(request.texts)
    elif backend == "openai":
        embeddings = await openai_service.generate_embeddings(request.texts)
    else:
        raise HTTPException(status_code=400, detail="Unsupported backend.")
    return {"embeddings": embeddings}

@router.post("/admin/set_backend")
async def set_backend(backend: str):
    if backend not in ["local", "openai"]:
        raise HTTPException(status_code=400, detail="Invalid backend choice.")
    settings.backend = backend
    return {"message": f"Backend switched to {backend}"}
