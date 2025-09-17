# FastAPI Summarization Agent

A FastAPI-based microservice that provides intelligent text summarization using Google Gemini 2.5 Flash with customizable length, style, and focus parameters. Designed to be callable as a tool by LangChain or LlamaIndex agents.

## Table of Contents

- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [API Documentation](#api-documentation)
- [LangChain Integration](#langchain-integration)
- [Usage Examples](#usage-examples)
- [Docker Deployment](#docker-deployment)
- [Testing](#testing)
- [Prompt Design](#prompt-design)
- [Project Structure](#project-structure)

## Features

- **Customizable Summarization**: Support for different lengths (short, medium, long), styles (bullet, paragraph, numbered), and focus topics
- **Real LLM Integration**: Uses Google Gemini 2.5 Flash for high-quality summaries
- **Rate Limiting**: Built-in middleware to prevent API abuse (10 requests/minute per IP)
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

### 5. Run the Application

```bash
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000` with interactive documentation at `http://localhost:8000/`.

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

- **text** (string, required): The text to summarize (minimum 50 characters)
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

The demo processes the provided example text and logs results to `examples/agent_demo.log`.

## Usage Examples

### Helper Script for Markdown Processing

For testing with the provided example files, use the markdown cleaning script:

```bash
# On Linux/Mac
python scripts/clean_markdown.py docs/examples/example_LLM_costs_overview.md | xclip -selection clipboard

# On Windows/WSL
python scripts/clean_markdown.py docs/examples/example_LLM_costs_overview.md | clip.exe
```

This removes markdown formatting and makes the text suitable for API testing using the interactive FastAPI docs.

### Interactive Documentation

Visit `http://localhost:8000/` for the interactive API documentation where you can:
- View detailed parameter descriptions
- Test the API directly in your browser
- See example requests and responses
- Download the OpenAPI specification

## Docker Deployment

### Build and Run

```bash
# Build the Docker image
docker build -t fastapi-summarization .

# Run the container
docker run -d -p 8000:8000 --env-file .env fastapi-summarization
```

### Docker Compose (Optional)

```yaml
version: '3.8'
services:
  summarization-api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
```

## Testing

### Run Unit Tests

```bash
pytest src/tests/ -v
```

The tests automatically use all markdown files in `docs/examples/` to validate the API endpoint.

### Test Coverage

Tests cover:
- API endpoint functionality
- Response structure validation
- Error handling
- Integration with real markdown content

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
4. **Focus Integration**: Seamlessly incorporates optional focus topics when provided

### Adapting the Prompt

To modify summarization behavior:

1. **Edit System Instruction** (`src/config/prompts.py`):
   - Adjust length guidelines
   - Add new style formats
   - Modify tone or approach

2. **Extend User Prompt Builder**:
   - Add new parameters
   - Include additional context
   - Implement custom formatting rules

## Project Structure

```
fastapi_agent/
├── src/
│   ├── main.py                 # FastAPI application
│   ├── config/
│   │   └── prompts.py         # LLM prompt templates
│   ├── schemas/
│   │   └── http_schemas.py    # Pydantic models
│   ├── throttling/
│   │   └── rate_limiter.py    # Rate limiting middleware
│   └── tests/
│       └── test_endpoint.py   # Unit tests
├── tools/
│   └── langchain_integration.py  # LangChain tool definition
├── examples/
│   └── langchain_agent_demo.py   # Agent demonstration
├── scripts/
│   └── clean_markdown.py     # Utility script for cleaning markdown
├── docs/
│   └── examples/              # Test markdown files
├── Dockerfile                 # Container configuration
├── requirements.txt           # Python dependencies
└── README.md                 # This file
```

## Rate Limiting

The API includes built-in rate limiting:
- **Limit**: 10 requests per minute per IP address
- **Headers**: Includes `Retry-After` and rate limit information
- **Response**: Returns 429 status code when exceeded

## Error Handling

The API provides clear error responses for:
- Invalid input parameters
- Empty or too-short text
- LLM API failures
- Rate limit violations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

This project is developed as a demonstration of FastAPI and LLM integration capabilities.
