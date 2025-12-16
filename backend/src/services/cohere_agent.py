from typing import List, Dict, Any, Optional
import cohere
from langchain_cohere import ChatCohere
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from langchain import hub
from ..services.qdrant_retrieval_tool import qdrant_retrieval_tool
from ..config.settings import settings
import logging

logger = logging.getLogger(__name__)

class CohereAgentService:
    def __init__(self, model_name: str = "command-r-08-2024"):
        if not settings.COHERE_API_KEY:
            raise ValueError("COHERE_API_KEY environment variable is not set")

        self.model_name = model_name
        self.client = cohere.Client(settings.COHERE_API_KEY)

        # Initialize the LLM for the agent
        self.llm = ChatCohere(
            model=model_name,
            cohere_api_key=settings.COHERE_API_KEY,
            temperature=0.7
        )

        # Initialize tools for the agent
        self.tools = [qdrant_retrieval_tool]

        # Create the react agent with the new pattern using proper prompt structure
        # Use the official react agent prompt template which has the required variables
        try:
            # Try to get the official react prompt from langchain hub
            prompt = hub.pull("hwchase17/react")
        except:
            # If hub is not available, create the proper prompt manually
            template = """Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:
Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Important:
1. For simple greetings like "hi", "hello", "hey", etc., respond directly with a friendly greeting without using tools.
2. If you have enough information from tool results, ALWAYS give Final Answer immediately. Do not call tools unnecessarily.
3. If no relevant context is found after using tools, provide a direct final answer without additional tool calls.
4. Stop using tools when you have sufficient information to answer the question.
5. Always provide a complete, helpful response to the user.
6. LIMIT tool usage to maximum 2-3 calls unless absolutely necessary. If you've used tools 2-3 times and have relevant information, provide the Final Answer.
7. After retrieving information, synthesize it into a comprehensive response and stop using tools.

Begin!

Question: {input}
{agent_scratchpad}"""
            prompt = PromptTemplate.from_template(template)

        self.agent = create_react_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=prompt
        )

        # Initialize the agent executor with the new agent
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=4,
            max_execution_time=60,
            early_stopping_method="generate",
            return_intermediate_steps=False
        )

    async def run_agent(self, query: str) -> str:
        """Run the Cohere agent with tools to answer the query"""
        # Check if the query is a simple greeting
        clean_query = query.strip().lower()
        if clean_query in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening", "greetings"]:
            return "Hi! I'm your Physical AI Book Assistant. Ask me anything about ROS 2, Gazebo, NVIDIA Isaac, or humanoid robotics!"

        try:
            # Run the agent with the query using async invocation
            response = await self.agent_executor.ainvoke({"input": query})
            return response.get("output", response) if isinstance(response, dict) else str(response)
        except Exception as e:
            error_msg = str(e)
            logger.error(f"Error running Cohere agent: {error_msg}", exc_info=True)

            # Check if it's an iteration/time limit error and provide more helpful message
            if "iteration limit" in error_msg.lower() or "time limit" in error_msg.lower() or "stopped due to" in error_msg.lower():
                return "I'm still learning about this topic. Could you try rephrasing your question or ask something more specific about the Physical AI & Humanoid Robotics book?"
            else:
                return f"I'm having trouble processing your request with the agent. The system encountered an error: {error_msg}"

    async def get_agent_response_with_context(self, query: str, selected_text: Optional[str] = None) -> str:
        """Get agent response with potential selected text context"""
        # Check if the query is a simple greeting
        clean_query = query.strip().lower()
        if clean_query in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening", "greetings"]:
            return "Hi! I'm your Physical AI Book Assistant. Ask me anything about ROS 2, Gazebo, NVIDIA Isaac, or humanoid robotics!"

        try:
            # If selected text is provided, create a more specific query
            if selected_text:
                full_query = f"The user has selected this text: '{selected_text[:500]}...'. Now, {query}. Use the Qdrant tool to find additional relevant information from the book."
            else:
                full_query = f"{query}. Use the Qdrant tool to find relevant information from the book."

            response = await self.agent_executor.ainvoke({"input": full_query})
            return response.get("output", response) if isinstance(response, dict) else str(response)
        except Exception as e:
            error_msg = str(e)
            logger.error(f"Error getting agent response with context: {error_msg}", exc_info=True)

            # Check if it's an iteration/time limit error and provide more helpful message
            if "iteration limit" in error_msg.lower() or "time limit" in error_msg.lower() or "stopped due to" in error_msg.lower():
                return "I'm still learning about this topic. Could you try rephrasing your question or ask something more specific about the Physical AI & Humanoid Robotics book?"
            else:
                return f"I'm having trouble processing your request with the agent. The system encountered an error: {error_msg}"