# Quickstart: Local Frontend-Backend Integration for RAG Chatbot

## Development Setup

### Prerequisites
- Python 3.11+ (for backend)
- Node.js 18+ (for Docusaurus frontend)
- Access to Qdrant Cloud (for RAG functionality)
- Google Gemini API key (for free tier usage)

### Environment Setup

1. Create a `.env` file in the backend directory:
```bash
GEMINI_API_KEY=your_gemini_api_key_here
QDRANT_URL=your_qdrant_cloud_url
QDRANT_API_KEY=your_qdrant_api_key
QDRANT_COLLECTION_NAME=physical_ai_book_2025
```

2. Install backend dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Install frontend dependencies:
```bash
cd frontend  # or wherever your Docusaurus project is
npm install
```

## Running the Integrated System

### Backend (FastAPI)
```bash
cd backend
uvicorn src.main:app --reload --port 8000
```

The backend API will be available at `http://localhost:8000`.

### Frontend (Docusaurus)
```bash
cd frontend  # or your Docusaurus project directory
npm run start
```

The frontend will be available at `http://localhost:3000`.

## API Endpoints

### POST /api/v1/chat
Send a message to the RAG chatbot:
```json
{
  "query": "Your question about the book content",
  "selected_text": "Optional text selected by user",
  "session_id": "Optional session ID (auto-generated if not provided)"
}
```

Response:
```json
{
  "response": "Generated response from the RAG system",
  "session_id": "Current session ID",
  "sources": [
    {
      "url": "Source document URL",
      "title": "Source document title",
      "snippet": "Relevant content snippet"
    }
  ],
  "timestamp": "ISO timestamp"
}
```

## Integration Testing

### Basic Communication Test
1. Start both backend (port 8000) and frontend (port 3000)
2. Open browser to http://localhost:3000
3. Open browser dev tools Network tab
4. Use the chat widget to send a message
5. Verify request goes to http://localhost:8000/api/v1/chat
6. Verify response comes back and displays in the chat widget

### Selected Text Functionality Test
1. Select text on the page
2. Type a question in the chat widget
3. Send the message
4. Verify that selected_text appears in the request payload
5. Confirm that the response takes the selected text into account

### CORS Verification
1. Check that no CORS errors appear in browser console
2. Verify that requests from localhost:3000 can reach localhost:8000
3. Confirm that browser security doesn't block the API calls

## Troubleshooting

### Common Issues
- **CORS errors**: Ensure CORS middleware is properly configured in FastAPI
- **Connection refused**: Verify both services are running on correct ports
- **Network timeouts**: Check firewall settings or proxy configurations
- **SSL certificate errors**: For local development, ensure using HTTP not HTTPS

### Debugging Tips
- Check backend logs for incoming requests
- Monitor frontend network tab for request/response details
- Verify environment variables are correctly set
- Confirm that Qdrant Cloud is accessible and properly configured