import os
import time
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from google import genai
from google.genai import types

from .config.prompts import SYSTEM_INSTRUCTION, build_user_prompt
from .schemas import RequestModel, ResponseModel
from .throttling import RateLimiterMiddleware
from utils.logging_config import setup_logging, get_logger

# Set up logging for the FastAPI app
app_log_file = setup_logging("fastapi_app", "api")
logger = get_logger(__name__)

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    logger.error("❌ GEMINI_API_KEY not found in environment variables")
    raise ValueError("GEMINI_API_KEY is required")

client = genai.Client(api_key=api_key)
logger.info("✅ Gemini client initialized successfully")

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle application startup and shutdown"""
    # Startup
    logger.info(f"🚀 FastAPI application starting up")
    logger.info(f"📁 API logs saved to: {app_log_file}")
    logger.info(f"🔧 Rate limiting: 10 requests per minute per IP")
    
    yield
    
    # Shutdown
    logger.info("🛑 FastAPI application shutting down")

tags_metadata = [
    {
        "name": "summarize",
        "description": "Text summarization using Google Gemini 2.5 Flash.",
        "externalDocs": {
            "description": "Gemini 2.5 Flash Model Docs",
            "url": "https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash",
        },
    }
]

app = FastAPI(
    lifespan=lifespan,
    openapi_tags=tags_metadata,
    title="FastAPI summarization Agent",
    description="An API that summarizes text using Google Gemini 2.5 Flash with user-defined preferences.",
    version="1.0.0",
    contact={
        "name": "Andreas Baschir",
        "url": "https://www.linkedin.com/in/andreas-baschir-21b963236/",
        "email": "andreas.baschir@stud.etti.upb.ro",
    },
    docs_url="/",
    redoc_url=None,
)

# Apply rate limiting middleware: max 10 requests per minute per IP
app.add_middleware(RateLimiterMiddleware, max_requests=10, window_seconds=60)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log all HTTP requests and responses with timing"""
    start_time = time.time()
    
    # Log incoming request
    logger.info(f"🔵 {request.method} {request.url.path} - Client: {request.client.host}")
    
    # Process request
    response = await call_next(request)
    
    # Calculate processing time
    process_time = time.time() - start_time
    
    # Log response with timing
    status_emoji = "🟢" if response.status_code < 400 else "🔴"
    logger.info(f"{status_emoji} {request.method} {request.url.path} - Status: {response.status_code} - Time: {process_time:.3f}s")
    
    return response

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Log all unhandled exceptions"""
    logger.error(f"🔴 Unhandled exception on {request.method} {request.url.path}: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )

@app.post("/summarize", tags=["summarize"], response_model=ResponseModel)
async def summarize(request: RequestModel):
    """
    Summarizes a given block of text using the Gemini 2.5 Flash model.

    This endpoint takes a piece of text and user preferences for summarization
    and returns a generated summary along with metadata about the request.

    ### Request Body
    - **text** (str): The block of text to summarize.
    - **length** (str): The desired length of the summary.
      - Accepted values: `short`, `medium`, `long`.
    - **style** (str): The desired output format for the summary.
      - Accepted values: `bullet`, `paragraph`, `numbered`.
    - **focus** (Optional[str]): An optional topic or keyword to emphasize in the summary.

    ### Response Body
    - **summary** (str): The generated summary of the text.
    - **meta** (dict): Metadata about the request, including the model used,
      length, style, and focus.
    """

    # Log incoming summarization request
    logger.info(f"📝 Summarization request - Text: {len(request.text)} chars, Length: {request.length}, Style: {request.style}, Focus: {request.focus}")

    # Validate and clean the input text
    if not request.text.strip():
        logger.warning("⚠️ Empty text submitted for summarization")
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    original_length = len(request.text)
    request.text = request.text.replace("\r", "").replace("\n", " ").replace("\t", " ")
    cleaned_length = len(request.text)
    
    if original_length != cleaned_length:
        logger.info(f"🧹 Text cleaned - Original: {original_length} chars, Cleaned: {cleaned_length} chars")

    # Build the user prompt using the separated function
    user_prompt = build_user_prompt(
        text=request.text,
        length=request.length,
        style=request.style,
        focus=request.focus
    )
    
    logger.info(f"🔧 Built user prompt - Length: {len(user_prompt)} chars")

    try:
        # Log API call attempt
        logger.info("🤖 Calling Gemini 2.5 Flash API...")
        
        # Call the external API
        api_start_time = time.time()
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION
            ),
            contents=user_prompt
        )
        api_time = time.time() - api_start_time
        
        logger.info(f"✅ Gemini API call successful - Time: {api_time:.3f}s")
        
    except Exception as e:
        logger.error(f"❌ Gemini API call failed: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error generating summary: {str(e)}")

    # Extract and return the response
    summary = response.text.strip()
    summary_length = len(summary)
    
    logger.info(f"📄 Summary generated - Output: {summary_length} chars")
   
    meta = {
        "model": "gemini-2.5-flash",
        "length": request.length,
        "style": request.style,
        "focus": request.focus
    }
    
    logger.info("✅ Summarization completed successfully")
    return ResponseModel(summary=summary, meta=meta)
