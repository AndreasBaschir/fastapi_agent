from pydantic import BaseModel, Field
from typing import Literal, Optional

class RequestModel(BaseModel):
    text: str = Field(
        ..., 
        description="The block of text you want to summarize.",
        min_length=50
    )
    length: Literal["short", "medium", "long"] = Field(
        ..., 
        description="The desired length of the summary."
    )
    style: Literal["bullet", "paragraph", "numbered"] = Field(
        ..., 
        description="The desired output format for the summary."
    )
    focus: Optional[str] = Field(
        None, 
        description="An optional topic or keyword to emphasize in the summary."
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "text": "The cost of AI computing is falling. A technique called distillation is making it cheaper to build decent LLMs. This shift excites some and alarms others in the AI ecosystem. Distillation is, at its core, using one model to improve another.",
                    "length": "short",
                    "style": "bullet",
                    "focus": "distillation"
                }
            ]
        }
    }

class ResponseModel(BaseModel):
    summary: str = Field(description="The generated summary of the text.")
    meta: dict = Field(description="Metadata about the request, including model, length, style, and focus.")
