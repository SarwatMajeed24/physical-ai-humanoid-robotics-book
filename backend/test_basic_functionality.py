"""
Basic functionality test for the RAG Chatbot API
"""
import pytest
import asyncio
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_endpoint():
    """Test that the root endpoint is accessible"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "RAG Chatbot API is running!" in response.json()["message"]

def test_health_endpoint():
    """Test the health endpoint"""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert "status" in response.json()
    assert "timestamp" in response.json()
    assert "dependencies" in response.json()

def test_status_endpoint():
    """Test the status endpoint"""
    response = client.get("/api/v1/status")
    assert response.status_code == 200
    assert "status" in response.json()
    assert "indexed_content_count" in response.json()

def test_chat_endpoint_structure():
    """Test that chat endpoint accepts the correct structure"""
    # Test with minimal valid request
    response = client.post(
        "/api/v1/chat",
        json={
            "query": "Hello",
            "session_id": "test_session_123"
        }
    )
    # Should return 200 OK or 500 if external services are not configured
    assert response.status_code in [200, 500]

if __name__ == "__main__":
    pytest.main([__file__])