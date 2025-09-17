# FastAPI Summarization Agent

A FastAPI-based microservice that provides intelligent text summarization using Google Gemini 2.5 Flash with customizable length, style, and focus parameters. Designed to be callable as a tool by LangChain.

You can find the app at [this link](https://fastapi-agent-1vpx.onrender.com). The containerized app is hosted using [render.com](render.com).

Press `Try it out` and by using the RequestBody schema, send a request.

## Table of Contents

- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [LangChain Integration](#langchain-integration)
- [Usage Examples](#usage-examples)
- [Docker Deployment](#docker-deployment)
- [Testing](#testing)
- [Logging](#logging)
- [Prompt Design](#prompt-design)

## Features

- **Customizable Summarization**: Support for different lengths (short, medium, long), styles (bullet, paragraph, numbered), and focus topics
- **Real LLM Integration**: Uses Google Gemini 2.5 Flash for high-quality summaries
- **Rate Limiting**: Built-in middleware to prevent API abuse (10 requests/minute per IP)
- **Centralized Logging**: Comprehensive logging system with timestamped logs organized by component
- **LangChain Compatible**: Designed to work seamlessly with LangChain RequestsPostTool
- **Interactive Documentation**: Auto-generated OpenAPI docs with examples
- **Containerized**: Docker support for easy deployment
- **Comprehensive Testing**: Unit tests with real markdown examples

## Setup Instructions

### Prerequisites

- Python 3.12+
- Google Gemini API key
- Git

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd fastapi_agent
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5. Run the Application locally

```bash
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000` with interactive documentation at `http://localhost:8000/`.

## Project Structure

```
fastapi_agent/
├── src/
│   ├── main.py                    # FastAPI application with logging
│   ├── config/
│   │   └── prompts.py            # LLM prompt templates
│   ├── schemas/
│   │   └── http_schemas.py       # Pydantic models
│   ├── throttling/
│   │   └── rate_limiter.py       # Rate limiting middleware
│   └── tests/
│       └── test_endpoint.py      # Unit tests with logging
├── utils/
│   └── logging_config.py         # Centralized logging utility
├── tools/
│   └── langchain_integration.py  # LangChain tool definition
├── examples/
│   └── langchain_agent_demo.py   # Agent demonstration with logging
├── scripts/
│   └── clean_markdown.py         # Utility script for cleaning markdown
├── docs/
│   └── examples/                 # Test markdown files
├── logs/                         # Generated log files (organized by component)
│   ├── api/                      # FastAPI logs
│   ├── examples/                 # Agent demo logs
│   └── tests/                    # Test execution logs
├── Dockerfile                    # Container configuration
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```


## API Documentation

### Endpoint: `POST /summarize`

Summarizes text with customizable parameters using Google Gemini 2.5 Flash.

#### Request Schema

```json
{
  "text": "Your text to summarize here...",
  "length": "short|medium|long",
  "style": "bullet|paragraph|numbered",
  "focus": "optional topic to emphasize"
}
```

#### Response Schema

```json
{
  "summary": "Generated summary text...",
  "meta": {
    "model": "gemini-2.5-flash",
    "length": "short",
    "style": "bullet",
    "focus": "costs"
  }
}
```

#### Parameters

- **text** (string, required): The text to summarize
- **length** (string, required): Summary length
  - `short`: 2-4 sentences or bullet points
  - `medium`: 1-2 paragraphs or 5-8 bullet points
  - `long`: 2-3 paragraphs or 8-12 bullet points
- **style** (string, required): Output format
  - `bullet`: Bullet point format
  - `paragraph`: Paragraph format
  - `numbered`: Numbered list format
- **focus** (string, optional): Topic or keyword to emphasize

#### Example Request

```bash
curl -X POST "http://localhost:8000/summarize" \
     -H "Content-Type: application/json" \
     -d '{
       "text": "The cost of AI computing is falling. A technique called distillation is making it cheaper to build decent LLMs. This shift excites some and alarms others in the AI ecosystem.",
       "length": "short",
       "style": "bullet",
       "focus": "distillation"
     }'
```

## LangChain Integration

In `/examples/langchain_agent_demo.py`

### Architecture Overview

The service is designed to work seamlessly with LangChain agents:

```
User Request
    ↓
LangChain Agent (ChatGoogleGenerativeAI)
    ↓ (decides to use summarization tool)
HTTP Request to FastAPI Service
    ↓
FastAPI app (genai.Client)
    ↓
Gemini API
    ↓
Summary returned via HTTP
    ↓
Agent formats final response
```

### Using RequestsPostTool

```python
from langchain_community.tools import RequestsPostTool
from langchain_community.utilities import RequestsWrapper
from src.schemas import RequestModel

# Create a requests wrapper
requests_wrapper = RequestsWrapper()

# Define the LangChain tool
summarization_tool = RequestsPostTool(
    name="text_summarizer",
    description="Summarizes text with customizable length, style, and focus.",
    url="http://127.0.0.1:8000/summarize",
    headers={"Content-Type": "application/json"},
    schema=RequestModel,
    requests_wrapper=requests_wrapper,
    allow_dangerous_requests=True,
)
```

### Agent Integration Example

```python
from langchain.agents import initialize_agent, AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from tools.langchain_integration import summarization_tool
from utils.logging_config import setup_logging, get_logger

# Set up logging
log_file = setup_logging("agent_demo", "examples")
logger = get_logger(__name__)

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    temperature=0,
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# Create agent
agent = initialize_agent(
    tools=[summarization_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Use the agent
response = agent.invoke("""
Please summarize the following text in bullet points,
focusing on costs: [your text here]
""")
```

### Running the Demo

1. Start the FastAPI server:
   ```bash
   uvicorn src.main:app --reload
   ```

2. Run the LangChain agent demo:
   ```bash
   python3 -m examples.langchain_agent_demo
   ```

The demo processes the provided example text and logs results to `logs/examples/agent_demo_YYYYMMDD_HHMMSS.log`.

## Usage Examples

### Testing the Public Hosted API

The FastAPI application is deployed and publicly accessible at: **https://fastapi-agent-1vpx.onrender.com**

#### Quick Test with cURL

```bash
curl -X POST "https://fastapi-agent-1vpx.onrender.com/summarize" \
     -H "Content-Type: application/json" \
     -d '{
       "text": "The cost of AI computing is falling. A technique called distillation is making it cheaper to build decent LLMs. This shift excites some and alarms others in the AI ecosystem.",
       "length": "short",
       "style": "bullet",
       "focus": "distillation"
     }'
```

#### Interactive Documentation

Visit **https://fastapi-agent-1vpx.onrender.com/** for the live interactive API documentation where you can:
- View detailed parameter descriptions
- Test the API directly in your browser
- See example requests and responses
- Download the OpenAPI specification

#### Using the Markdown Cleaning Script for Public API Testing

For testing with the provided example files, use the markdown cleaning script to prepare text:

```bash
# On Linux/Mac
python scripts/clean_markdown.py docs/examples/example_LLM_costs_overview.md | xclip -selection clipboard

# On Windows/WSL
python scripts/clean_markdown.py docs/examples/example_LLM_costs_overview.md | clip.exe
```

This script can be used on any .md file:

```bash
# On Linux/Mac
python scripts/clean_markdown.py your_file_path.md | xclip -selection clipboard

# On Windows/WSL
python scripts/clean_markdown.py your_file_path.md | clip.exe
```

After running the script, the cleaned text will be in your clipboard. Navigate to the **live API docs** at https://fastapi-agent-1vpx.onrender.com/, press `Try it out`, and paste the text into the RequestBody JSON field.

#### Testing with Different Parameters

Try these parameter combinations with the public API:

1. **Short Bullet Summary with Focus**:
   ```json
   {
     "text": "[your cleaned text here]",
     "length": "short",
     "style": "bullet",
     "focus": "costs"
   }
   ```

2. **Medium Paragraph Summary**:
   ```json
   {
     "text": "[your cleaned text here]",
     "length": "medium",
     "style": "paragraph",
     "focus": "pricing"
   }
   ```

3. **Long Numbered List**:
   ```json
   {
     "text": "[your cleaned text here]",
     "length": "long",
     "style": "numbered",
     "focus": "competition"
   }
   ```

### Local Development Testing

#### Running Locally

For local development and testing:

```bash
# Start the local server
uvicorn src.main:app --reload
```

The local API will be available at `http://localhost:8000` with interactive documentation at `http://localhost:8000/`.

#### Local cURL Testing

```bash
curl -X POST "http://localhost:8000/summarize" \
     -H "Content-Type: application/json" \
     -d '{
       "text": "Your test text here...",
       "length": "short",
       "style": "bullet",
       "focus": "distillation"
     }'
```

## Docker Deployment

### Build and Run

```bash
# Build the Docker image
docker build -t fastapi-summarization .

# Run the container
docker run -d -p 8000:8000 --env-file .env fastapi-summarization
```

## Testing

### Run Unit Tests

```bash
pytest src/tests/ -v
```

The tests automatically use all markdown files in `docs/examples/` to validate the API endpoint and generate detailed logs in `logs/tests/`.

### Test the hosted Docker app

### Testing the Public API

The hosted application at **https://fastapi-agent-1vpx.onrender.com** can be tested directly without any setup:

1. **Browser Testing**: Visit https://fastapi-agent-1vpx.onrender.com/ and use the interactive docs
2. **cURL Testing**: Use the cURL examples above with the public URL
3. **Postman/Insomnia**: Import the OpenAPI spec from the public docs
4. **LangChain Integration**: Point your tools to the public URL

### Local Unit Tests

For local development, run the comprehensive test suite:

```bash
pytest src/tests/ -v
```

The tests automatically use all markdown files in `docs/examples/` to validate the API endpoint and generate detailed logs in `logs/tests/`.

### Test Coverage

Tests cover:
- API endpoint functionality with real markdown content
- Response structure validation
- Error handling for various edge cases
- Integration testing with multiple file types
- Logging functionality verification
- Rate limiting behavior

**Note**: The unit tests are designed for local development. The public API includes rate limiting (10 requests/minute), so extensive automated testing should be done against a local instance.

## Logging

### Centralized Logging System

The application uses a centralized logging utility (`utils/logging_config.py`) that provides:

- **Timestamped log files**: Each component run creates a unique log file
- **Organized structure**: Logs are organized by component in subdirectories
- **Dual output**: Logs to both console and file simultaneously
- **Consistent formatting**: Standardized log format across all components

### Log Organization

```
logs/
├── api/                    # FastAPI application logs
│   └── fastapi_app_YYYYMMDD_HHMMSS.log
├── examples/               # LangChain agent demo logs
│   └── agent_demo_YYYYMMDD_HHMMSS.log
└── tests/                  # Test execution logs
    └── test_endpoint_YYYYMMDD_HHMMSS.log
```

### Using the Logging System

```python
from utils.logging_config import setup_logging, get_logger

# Set up logging for your component
log_file = setup_logging("component_name", "subdirectory")
logger = get_logger(__name__)

# Use the logger
logger.info("Your log message here")
```

### Log Content

Logs include:
- **API requests/responses** with timing information
- **LLM API calls** with performance metrics
- **Error handling** with full stack traces
- **Business logic** events and data processing
- **Startup/shutdown** events

## Prompt Design

### System Instruction

The system prompt establishes the AI's role as a summarization assistant with clear guidelines for different lengths and styles.

### User Prompt Construction

The `build_user_prompt()` function dynamically constructs prompts based on:
- User-specified length, style, and focus parameters
- Clear task instructions
- Conditional focus emphasis

### Design Rationale

1. **Modular Approach**: Separates system instructions from user prompts for maintainability
2. **Parameter Reflection**: Ensures all user preferences are incorporated into the LLM prompt
3. **Clear Guidelines**: Provides specific length targets to ensure consistent output
4. **Focus Integration**: Incorporates optional focus topics when provided

## Rate Limiting

The API includes built-in rate limiting:
- **Limit**: 10 requests per minute per IP address
- **Headers**: Includes `Retry-After` and rate limit information
- **Response**: Returns 429 status code when exceeded
- **Logging**: Rate limit violations are logged for monitoring

## Error Handling

The API provides clear error responses for:
- Invalid input parameters
- Empty or too-short text
- LLM API failures
- Rate limit violations

All errors are comprehensively logged with stack traces for debugging.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Use the centralized logging system for any new components
6. Submit a pull request
