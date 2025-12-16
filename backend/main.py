import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from src.api import health, chat

# Load .env file (Vercel pe bhi kaam karega)
load_dotenv()

app = FastAPI(
    title="RAG Chatbot API",
    description="API for RAG Chatbot for Physical AI & Humanoid Robotics Book",
    version="1.0.0"
)

# CORS middleware – production ke liye specific origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://physical-ai-humanoid-robotics-book-lovat.vercel.app",
        "https://physical-ai-humanoid-robotics-book-5b9e-26ejgwi0o.vercel.app",
        "http://localhost:3000"  # local development ke liye
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(health.router, prefix="/api/v1", tags=["health"])
app.include_router(chat.router, prefix="/api/v1", tags=["chat"])

@app.get("/")
async def root():
    return {"message": "RAG Chatbot API is running!"}