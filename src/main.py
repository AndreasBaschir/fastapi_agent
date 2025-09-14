from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal, Optional
from middleware import RateLimiterMiddleware
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
    pass
