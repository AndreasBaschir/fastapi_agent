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
