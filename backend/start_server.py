#!/usr/bin/env python3
"""
Simple startup script for the RAG Chatbot API server
"""
import os
import sys
from dotenv import load_dotenv
from uvicorn import run
from main import app

# Load environment variables from .env file
load_dotenv()

def main():
    """Start the FastAPI server"""
    print("Starting RAG Chatbot API server...")
    print("Loading configuration...")

    # Check for required environment variables
    required_vars = ['COHERE_API_KEY', 'QDRANT_URL']
    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        print(f"Warning: Missing required environment variables: {', '.join(missing_vars)}")
        print("The server will start but some functionality may not work without these variables.")

    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', '8001'))

    print(f"Starting server on {host}:{port}")
    print("Press Ctrl+C to stop the server")

    try:
        run(app, host=host, port=port)
    except KeyboardInterrupt:
        print("\nShutting down server...")
        return 0
    except Exception as e:
        print(f"Error starting server: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())