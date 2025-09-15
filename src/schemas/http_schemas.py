from pydantic import BaseModel, Field
from typing import Literal, Optional


class RequestModel(BaseModel):
    text: str = Field(..., description="The text to summarize")
    length: Literal["short", "medium", "long"] = Field(..., description="The desired summary length")
    style: Literal["bullet", "paragraph", "numbered"] = Field(..., description="The desired summary style")
    focus: Optional[str] = Field(None, description="Optional topic to emphasize in the summary")

class ResponseModel(BaseModel):
    summary: str
    meta: dict
