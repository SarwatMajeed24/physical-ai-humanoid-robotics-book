from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Optional
import time
from datetime import datetime
import requests

from ..config.settings import settings
from ..services.cohere_embedding import CohereEmbeddingService
from ..services.vector_store import QdrantVectorStore

router = APIRouter()

class HealthResponse(BaseModel):
    status: str
    timestamp: str
    dependencies: Dict[str, str]

class StatusResponse(BaseModel):
    status: str
    indexed_content_count: int
    last_crawl_time: Optional[str]
    qdrant_collection_status: str

@router.get("/health")
async def health_check():
    """Check the health status of the RAG service"""
    dependencies = {}

    # Check Cohere API
    try:
        if settings.COHERE_API_KEY:
            cohere_service = CohereEmbeddingService()
            # Test with a simple embedding to verify API access
            test_embedding = cohere_service.generate_embedding("health check")
            dependencies["cohere"] = "ok" if test_embedding is not None else "error"
        else:
            dependencies["cohere"] = "not configured"
    except Exception as e:
        dependencies["cohere"] = f"error: {str(e)}"

    # Check Qdrant connection
    try:
        vector_store = QdrantVectorStore()
        count = await vector_store.get_all_chunks_count()
        dependencies["qdrant"] = "ok"
    except Exception as e:
        dependencies["qdrant"] = f"error: {str(e)}"

    # Check general database connection by attempting to initialize
    try:
        vector_store = QdrantVectorStore()
        await vector_store.initialize_collection()
        dependencies["database"] = "ok"
    except Exception as e:
        dependencies["database"] = f"error: {str(e)}"

    overall_status = "ok" if all("ok" in status for status in dependencies.values()) else "error"

    return HealthResponse(
        status=overall_status,
        timestamp=datetime.now().isoformat(),
        dependencies=dependencies
    )

@router.get("/status")
async def service_status():
    """Get the indexing and service status"""
    try:
        vector_store = QdrantVectorStore()
        await vector_store.initialize_collection()

        indexed_count = await vector_store.get_all_chunks_count()

        return StatusResponse(
            status="ok",
            indexed_content_count=indexed_count,
            last_crawl_time=None,  # Will be updated when crawling happens
            qdrant_collection_status="ready"
        )
    except Exception as e:
        return StatusResponse(
            status="error",
            indexed_content_count=0,
            last_crawl_time=None,
            qdrant_collection_status=f"error: {str(e)}"
        )