from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class BookContentChunk(BaseModel):
    """
    Represents a chunk of book content that has been processed and embedded for RAG retrieval
    """
    id: str
    url: str
    title: str
    content: str
    embedding: List[float]  # Vector embedding of the content (1024 dimensions for Cohere)
    section: str  # Book section identifier (e.g., "Chapter 1", "Module 3")
    created_at: datetime
    updated_at: datetime

class EmbeddingRequest(BaseModel):
    """
    Request model for embedding generation
    """
    content: str

class EmbeddingResponse(BaseModel):
    """
    Response model for embedding generation
    """
    id: str
    embedding: List[float]