import asyncio
from typing import List, Optional, Dict, Any
from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import Distance, VectorParams, PointStruct
from ..models.embedding import BookContentChunk
from ..config.settings import settings
import logging

logger = logging.getLogger(__name__)

class QdrantVectorStore:
    def __init__(self):
        # Initialize Qdrant client with settings
        if settings.QDRANT_URL.startswith('https://') or settings.QDRANT_URL.startswith('http://'):
            # Use HTTP/HTTPS URL
            self.client = QdrantClient(
                url=settings.QDRANT_URL,
                api_key=settings.QDRANT_API_KEY,
                timeout=10
            )
        else:
            # Assume it's a local instance or use grpc
            self.client = QdrantClient(
                host=settings.QDRANT_URL,
                api_key=settings.QDRANT_API_KEY,
                timeout=10
            )

        self.collection_name = settings.QDRANT_COLLECTION_NAME

    async def initialize_collection(self):
        """Initialize the Qdrant collection if it doesn't exist"""
        try:
            # Check if collection exists
            collections = self.client.get_collections()
            collection_names = [col.name for col in collections.collections]

            if self.collection_name not in collection_names:
                # Create collection with 1024 dimensions (for Cohere embeddings)
                self.client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=VectorParams(size=1024, distance=Distance.COSINE),
                )
                logger.info(f"Created Qdrant collection: {self.collection_name}")
            else:
                logger.info(f"Qdrant collection {self.collection_name} already exists")
        except Exception as e:
            logger.error(f"Error initializing Qdrant collection: {str(e)}")
            raise

    async def store_chunk(self, chunk: BookContentChunk) -> bool:
        """Store a single content chunk in the vector database"""
        try:
            if not chunk.embedding or len(chunk.embedding) == 0:
                logger.warning(f"Chunk {chunk.id} has no embedding, skipping storage")
                return False

            point = PointStruct(
                id=chunk.id,
                vector=chunk.embedding,
                payload={
                    "url": chunk.url,
                    "title": chunk.title,
                    "content": chunk.content,
                    "section": chunk.section,
                    "created_at": chunk.created_at.isoformat(),
                    "updated_at": chunk.updated_at.isoformat()
                }
            )

            self.client.upsert(
                collection_name=self.collection_name,
                points=[point]
            )
            return True
        except Exception as e:
            logger.error(f"Error storing chunk {chunk.id}: {str(e)}")
            return False

    async def store_chunks(self, chunks: List[BookContentChunk]) -> bool:
        """Store multiple content chunks in the vector database"""
        try:
            points = []
            for chunk in chunks:
                point = PointStruct(
                    id=chunk.id,
                    vector=chunk.embedding,
                    payload={
                        "url": chunk.url,
                        "title": chunk.title,
                        "content": chunk.content,
                        "section": chunk.section,
                        "created_at": chunk.created_at.isoformat(),
                        "updated_at": chunk.updated_at.isoformat()
                    }
                )
                points.append(point)

            self.client.upsert(
                collection_name=self.collection_name,
                points=points
            )
            return True
        except Exception as e:
            logger.error(f"Error storing chunks: {str(e)}")
            return False

    async def retrieve_similar(self, query_embedding: List[float], limit: int = 5) -> List[Dict[str, Any]]:
        """Retrieve similar content chunks based on query embedding"""
        try:
            # First check if collection exists
            try:
                collection_info = self.client.get_collection(self.collection_name)
            except Exception as collection_error:
                logger.error(f"Collection {self.collection_name} does not exist or is not accessible: {str(collection_error)}")
                return []

            results = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_embedding,
                limit=limit,
                with_payload=True
            )

            retrieved_chunks = []
            for result in results:
                retrieved_chunks.append({
                    "id": result.id,
                    "score": result.score,
                    "url": result.payload.get("url"),
                    "title": result.payload.get("title"),
                    "content": result.payload.get("content"),
                    "section": result.payload.get("section")
                })

            return retrieved_chunks
        except Exception as e:
            logger.error(f"Error retrieving similar chunks: {str(e)}")
            return []

    async def get_chunk_by_id(self, chunk_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific chunk by ID"""
        try:
            records = self.client.retrieve(
                collection_name=self.collection_name,
                ids=[chunk_id],
                with_payload=True
            )

            if records:
                record = records[0]
                return {
                    "id": record.id,
                    "url": record.payload.get("url"),
                    "title": record.payload.get("title"),
                    "content": record.payload.get("content"),
                    "section": record.payload.get("section")
                }
            return None
        except Exception as e:
            logger.error(f"Error retrieving chunk {chunk_id}: {str(e)}")
            return None

    async def get_all_chunks_count(self) -> int:
        """Get the total count of stored chunks"""
        try:
            count = self.client.count(
                collection_name=self.collection_name
            )
            return count.count
        except Exception as e:
            logger.error(f"Error getting chunks count: {str(e)}")
            return 0

    async def create_collection_and_store_chunks(self, chunks: List[BookContentChunk]) -> bool:
        """Create Qdrant collection and store embedded chunks (for T017)"""
        try:
            # Initialize the collection
            await self.initialize_collection()

            # Store all chunks
            success = await self.store_chunks(chunks)
            return success
        except Exception as e:
            logger.error(f"Error creating collection and storing chunks: {str(e)}")
            return False