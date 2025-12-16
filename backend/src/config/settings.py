import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    # Cohere settings
    COHERE_API_KEY: str = os.getenv("COHERE_API_KEY", "bFODOX6iFSFWb71tJehNzb6EwMMERxw3h2cWIBkW")

    # Qdrant settings
    QDRANT_URL: str = os.getenv("QDRANT_URL", "")
    QDRANT_API_KEY: str = os.getenv("QDRANT_API_KEY", "")

    # Book settings
    BOOK_SITEMAP_URL: str = os.getenv("BOOK_SITEMAP_URL", "https://physical-ai-humanoid-robotics-book-lovat.vercel.app/sitemap.xml")

    # Application settings
    APP_NAME: str = "Free LLM RAG Agent API"
    API_V1_STR: str = "/api/v1"

    # Qdrant collection name
    QDRANT_COLLECTION_NAME: str = os.getenv("QDRANT_COLLECTION_NAME", "physical_ai_book_2025")

settings = Settings()