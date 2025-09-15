import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from google import genai
from google.genai import types
from .throttling import RateLimiterMiddleware
from .schemas import RequestModel, ResponseModel

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
app = FastAPI()

# Apply rate limiting middleware: max 5 requests per minute per IP
app.add_middleware(RateLimiterMiddleware, max_requests=5, window_seconds=60)


@app.post("/summarize", response_model=ResponseModel)
async def summarize(request: RequestModel):
    """
    Summarizes the provided text based on user preferences for length, style, and focus.
    - request: RequestModel containing text, length, style, and optional focus.
    - returns: ResponseModel with the summary and metadata.
    """

    # Validate and clean the input text
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    request.text = request.text.replace("\r", "").replace("\n", " ").replace("\t", " ")

    # Construct the user prompt
    user_prompt = f"Summarize the following text in a {request.length} {request.style} format:\n\n{request.text}"
    if request.focus:
        user_prompt += f" Emphasize the topic: {request.focus}."

    try:
        # Call the external API
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction="You are a helpful assistant that summarizes text based on user preferences."
            ),
            contents=user_prompt
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating summary: {str(e)}")

    # Extract and return the response
    summary = response.text.strip()
    meta = {
        "model": "gemini-2.5-flash",
        "length": request.length,
        "style": request.style,
        "focus": request.focus
    }
    return ResponseModel(summary=summary, meta=meta)


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Agent! Use the /summarize endpoint to get started."}
