from typing import List, Optional
import cohere
from ..config.settings import settings
import logging

logger = logging.getLogger(__name__)

class CohereLLMService:
    def __init__(self, model_name: str = "command-r-08-2024"):
        if not settings.COHERE_API_KEY:
            raise ValueError("COHERE_API_KEY environment variable is not set")

        self.client = cohere.Client(settings.COHERE_API_KEY)
        self.model_name = model_name

    async def generate_response(self, prompt: str) -> str:
        """Generate a response using the Cohere model"""
        try:
            response = self.client.chat(
                message=prompt,
                model=self.model_name,
                temperature=0.7
            )

            response_text = response.text if response.text else ""

            if not response_text:
                return "I couldn't generate a meaningful response for your query. Please try rephrasing your question."

            return response_text
        except Exception as e:
            logger.error(f"Error generating response with Cohere: {str(e)}")
            return "I'm having trouble processing your request right now. Please try asking in a different way."

    async def chat_with_context(self, query: str, context: str) -> str:
        """Generate a response based on query and context"""
        prompt = f"""
        You are an assistant for the Physical AI & Humanoid Robotics book.
        Use the following context to answer the user's question.
        If the context contains relevant information, use it to provide an accurate answer.
        If the context contains partial information, use what's available and supplement with general knowledge about humanoid robotics.
        If no relevant context is available, provide a helpful response based on general knowledge about humanoid robotics and suggest rephrasing the question.
        Keep your answers informative and relevant to robotics topics.

        Context: {context}

        Question: {query}

        Answer:
        """
        return await self.generate_response(prompt)