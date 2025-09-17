from pathlib import Path
from langchain_community.tools import RequestsPostTool
from langchain_community.utilities import RequestsWrapper

from src.schemas import RequestModel

# Create a requests wrapper
requests_wrapper = RequestsWrapper()

# Define the LangChain tool for text summarization
summarization_tool = RequestsPostTool(
    name="text_summarizer",
    description="Summarizes text with customizable length, style, and focus. Use this when you need to create summaries of long text content.",
    url="http://127.0.0.1:8000/summarize",
    headers={"Content-Type": "application/json"},
    schema=RequestModel,
    requests_wrapper=requests_wrapper,
    allow_dangerous_requests=True,
)

