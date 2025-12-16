from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from uuid import UUID

class SourceReference(BaseModel):
    """
    Model for source reference in chat response
    """
    url: str
    title: str
    snippet: str

class ChatRequest(BaseModel):
    """
    Request model for chat endpoint
    """
    query: str
    selected_text: Optional[str] = None
    session_id: Optional[str] = None

class ChatResponse(BaseModel):
    """
    Response model for chat endpoint
    """
    response: str
    session_id: str
    sources: List[SourceReference]
    timestamp: datetime

class Message(BaseModel):
    """
    Represents a single message in a chat session
    """
    message_id: str
    role: str  # "user" or "assistant"
    content: str
    timestamp: datetime
    selected_text: Optional[str] = None
    sources: Optional[List[SourceReference]] = None

class ChatSession(BaseModel):
    """
    Represents a user's chat session with the Cohere RAG agent
    """
    session_id: str
    created_at: datetime
    messages: List[Message]