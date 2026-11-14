"""Pydantic schemas for Research Analyst API request and response models."""

from typing import List, Optional
from pydantic import BaseModel, Field, field_validator


class ResearchQuestionRequest(BaseModel):
    """Schema for incoming research questions."""
    question: str = Field(
        ...,
        min_length=5,
        max_length=2000,
        description="The research or market analysis query to investigate.",
        examples=["What is the forecasted CAGR and capital expenditure impact of generative AI on semiconductor infrastructure through 2028?"]
    )

    @field_validator("question")
    @classmethod
    def validate_question_content(cls, value: str) -> str:
        trimmed = value.strip()
        if len(trimmed) < 5:
            raise ValueError("Question must contain at least 5 non-whitespace characters.")
        return trimmed


class ResearchAnalystResponse(BaseModel):
    """Schema for multi-agent research analysis response."""
    status: str = Field(default="success", description="Status of the research analysis.")
    question: str = Field(..., description="The original question submitted.")
    answer: str = Field(..., description="Synthesized, peer-reviewed research answer.")
    sources: List[str] = Field(default_factory=list, description="Research papers, reports, or library sources consulted.")
    disclaimer: str = Field(..., description="Mandatory educational research disclaimer.")


class HealthResponse(BaseModel):
    """Schema for system health check endpoint."""
    status: str = Field(default="healthy")
    app_name: str
    groq_configured: bool
    model: str
    agents: List[str]
