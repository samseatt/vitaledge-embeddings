# app/api/routes/__init__.py

from fastapi import APIRouter
from app.api.routes import embeddings

router = APIRouter()

router.include_router(embeddings.router, prefix="/embeddings", tags=["Embeddings"])
