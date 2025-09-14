from fastapi import FastAPI, HTTPException
from google import genai
from google.genai import types
from middleware import RateLimiterMiddleware
from pydantic import BaseModel, Field
from typing import Literal, Optional

client = genai.Client()

app = FastAPI()
app.add_middleware(RateLimiterMiddleware, max_requests=5, window_seconds=60)

class RequestModel(BaseModel):
    text: str = Field(..., description="The text to summarize")
    length: Literal["short", "medium", "long"] = Field(..., description="The desired summary length")
    style: Literal["bullet", "paragraph", "numbered"] = Field(..., description="The desired summary style")
    focus: Optional[str] = Field(None, description="Optional topic to emphasize in the summary")

class ResponseModel(BaseModel):
    summary: str
    meta: dict

@app.post("/summarize", response_model=ResponseModel)
async def summarize(request: RequestModel):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    user_prompt = f"Summarize the following text in a {request.length} {request.style} format:\n\n {request.text}"
    if request.focus:
        user_prompt += f" Emphasize the topic: {request.focus}."
    
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        config=types.GenerateContentConfig(
            system_instruction="You are a helpful assistant that summarizes text based on user preferences."),
        contents=f"{user_prompt}"
    )

    summary = response.text.strip()
    meta = {"model": "gemini-2.5-flash", "length": request.length, "style": request.style, "focus": request.focus}
    return ResponseModel(summary=summary, meta=meta)
