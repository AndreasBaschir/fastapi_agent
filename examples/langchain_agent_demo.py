import os
import logging

from langchain.agents import initialize_agent, AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from tools.langchain_integration import summarization_tool

# Set up logging to current directory
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='examples/agent_demo.log',
    filemode='w'
)

logger = logging.getLogger(__name__)

# Initialize Gemini LLM for the agent
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    temperature=0,
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# Create the agent using the summarization tool in tools/langchain_integration.py
agent = initialize_agent(
    tools=[summarization_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Example usage
if __name__ == "__main__":
    # Read one of the example files
    with open("docs/examples/example_LLM_costs_overview.md", "r") as f:
        text_content = f.read()
    
    logger.info("Starting summarization request")
    
    response = agent.invoke(f"""
    Please summarize the following text in a short manner (less than 200 words) 
    in bullet points, specifically focusing on the costs for using LLMs:

    {text_content}
    """)
    
    logger.info(f"Response: {response}")
    print("Response logged to agent_demo.log")