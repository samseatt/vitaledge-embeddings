# File: vitaledge-embeddings/app/main.py
from fastapi import FastAPI, HTTPException
from app.api.routes.embeddings import router as embeddings_router
from app.core.config import settings
from app.utils.logging import setup_logging

# Set up logging for the application
setup_logging(log_level="DEBUG", log_file="logs/vitaledge_embeddings.log")

app = FastAPI(title="VitalEdge Embeddings")

# Include Routers
app.include_router(embeddings_router, prefix="/embeddings", tags=["Embeddings"])

@app.on_event("startup")
async def startup_event():
    print(f"Starting application with backend: {settings.backend}")

@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down application.")
