#!/usr/bin/env python3
"""
Test script to verify the backend is working correctly
"""
import asyncio
import requests
import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_server_running():
    """Test if the server is running and accessible"""
    port = int(os.getenv('PORT', '8001'))
    url = f"http://localhost:{port}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "message" in data and "RAG Chatbot API is running!" in data["message"]:
                print("✅ Server is running and accessible!")
                return True
        print(f"❌ Server returned unexpected response: {response.status_code} - {response.text}")
        return False
    except requests.exceptions.ConnectionError:
        print(f"❌ Server is not running on port {port}")
        return False
    except Exception as e:
        print(f"❌ Error testing server: {str(e)}")
        return False

def test_health_endpoint():
    """Test the health endpoint"""
    port = int(os.getenv('PORT', '8001'))
    url = f"http://localhost:{port}/api/v1/health"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("✅ Health endpoint is working!")
            return True
        else:
            print(f"❌ Health endpoint returned status {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error testing health endpoint: {str(e)}")
        return False

def main():
    """Run all backend tests"""
    print("Testing RAG Chatbot Backend...")
    print("=" * 50)

    # Test basic imports
    try:
        from src.api import health, chat
        from src.services.crawler import SitemapCrawler
        from src.services.cohere_embedding import CohereEmbeddingService
        from src.services.vector_store import QdrantVectorStore
        from src.services.rag_chain import RAGChain
        print("✅ All imports work correctly!")
    except ImportError as e:
        print(f"❌ Import error: {str(e)}")
        return False

    # Test if server is running
    server_running = test_server_running()

    if server_running:
        test_health_endpoint()

    print("=" * 50)
    print("Backend test completed!")

    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)