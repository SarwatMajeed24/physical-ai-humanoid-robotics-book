from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.chat import router as chat_router
from .config.settings import settings
import uvicorn
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Free LLM RAG Agent API",
    description="API for RAG agent using Cohere free tier",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(chat_router, prefix="/api/v1", tags=["chat"])

@app.get("/")
def read_root():
    return {"message": "Free LLM RAG Agent API is running!"}

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up Free LLM RAG Agent API")
    # Initialize any required services here

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down Free LLM RAG Agent API")

if __name__ == "__main__":
    logger.info("Starting server on http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)