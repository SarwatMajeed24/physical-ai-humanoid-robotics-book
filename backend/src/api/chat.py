from fastapi import APIRouter, HTTPException
from typing import Dict, Any
import uuid
from datetime import datetime
import logging

from ..models.chat import ChatRequest, ChatResponse
from ..services.rag_chain import RAGChain
from ..services.cohere_agent import CohereAgentService

router = APIRouter()
logger = logging.getLogger(__name__)

# In-memory session storage (in production, use a proper database)
sessions: Dict[str, Any] = {}

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(chat_request: ChatRequest):
    """Process user query and return RAG-generated response"""
    try:
        # Generate or use provided session ID
        session_id = chat_request.session_id or str(uuid.uuid4())

        # Initialize session if it doesn't exist
        if session_id not in sessions:
            sessions[session_id] = {
                "session_id": session_id,
                "created_at": datetime.now(),
                "messages": []
            }

        # Add user message to session
        user_message = {
            "message_id": str(uuid.uuid4()),
            "role": "user",
            "content": chat_request.query,
            "timestamp": datetime.now(),
            "selected_text": chat_request.selected_text
        }
        sessions[session_id]["messages"].append(user_message)

        # Create RAG chain and process the query
        rag_chain = RAGChain()
        response = await rag_chain.retrieve_and_generate(
            query=chat_request.query,
            selected_text=chat_request.selected_text
        )

        # Update the response with the actual session ID
        response.session_id = session_id

        # Add assistant response to session
        assistant_message = {
            "message_id": str(uuid.uuid4()),
            "role": "assistant",
            "content": response.response,
            "timestamp": datetime.now(),
            "sources": response.sources
        }
        sessions[session_id]["messages"].append(assistant_message)

        logger.info(f"Processed chat request for session {session_id}")
        return response

    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        # Return a user-friendly error response instead of raising HTTPException
        error_response = ChatResponse(
            response="Book content is being indexed. Please try again in a moment!",
            session_id=chat_request.session_id or str(uuid.uuid4()),
            sources=[],
            timestamp=datetime.now()
        )
        return error_response

@router.post("/agent/chat", response_model=ChatResponse)
async def agent_chat_endpoint(chat_request: ChatRequest):
    """Process user query using Cohere agent with tool use"""
    try:
        # Generate or use provided session ID
        session_id = chat_request.session_id or str(uuid.uuid4())

        # Initialize session if it doesn't exist
        if session_id not in sessions:
            sessions[session_id] = {
                "session_id": session_id,
                "created_at": datetime.now(),
                "messages": []
            }

        # Add user message to session
        user_message = {
            "message_id": str(uuid.uuid4()),
            "role": "user",
            "content": chat_request.query,
            "timestamp": datetime.now(),
            "selected_text": chat_request.selected_text
        }
        sessions[session_id]["messages"].append(user_message)

        # Create Cohere agent and process the query with context
        agent_service = CohereAgentService()
        response_text = await agent_service.get_agent_response_with_context(
            query=chat_request.query,
            selected_text=chat_request.selected_text
        )

        # Create a ChatResponse with sources (sources will be empty since agent handles tool use internally)
        response = ChatResponse(
            response=response_text,
            session_id=session_id,
            sources=[],  # Agent handles sources internally through tool use
            timestamp=datetime.now()
        )

        # Add assistant response to session
        assistant_message = {
            "message_id": str(uuid.uuid4()),
            "role": "assistant",
            "content": response.response,
            "timestamp": datetime.now(),
            "sources": response.sources
        }
        sessions[session_id]["messages"].append(assistant_message)

        logger.info(f"Processed agent chat request for session {session_id}")
        return response

    except Exception as e:
        logger.error(f"Error in agent chat endpoint: {str(e)}")
        # Return a user-friendly error response instead of raising HTTPException
        error_response = ChatResponse(
            response="Book content is being indexed. Please try again in a moment!",
            session_id=chat_request.session_id or str(uuid.uuid4()),
            sources=[],
            timestamp=datetime.now()
        )
        return error_response

@router.get("/sessions/{session_id}")
async def get_session(session_id: str):
    """Get a specific session's information"""
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")

    return sessions[session_id]

@router.delete("/sessions/{session_id}")
async def delete_session(session_id: str):
    """Delete a specific session"""
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")

    del sessions[session_id]
    return {"message": "Session deleted successfully"}