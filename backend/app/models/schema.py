from pydantic import BaseModel, Field, field_validator
from typing import Optional, List, Dict, Any
from app.core.config import settings


class PredictRequest(BaseModel):
    """Request schema for prediction endpoint."""
    
    text: str = Field(
        ...,
        min_length=settings.MIN_TEXT_LENGTH,
        max_length=settings.MAX_TEXT_LENGTH,
        description="Text input for prediction"
    )
    
    @field_validator('text')
    @classmethod
    def clean_text(cls, v: str) -> str:
        """Clean and validate input text."""
        if not v or not v.strip():
            raise ValueError("Text cannot be empty or whitespace only")
        return v.strip()


class PredictResponse(BaseModel):
    """Response schema for prediction endpoint."""
    
    prediction: str = Field(..., description="Predicted class label")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Prediction confidence score")
    top_features: List[Dict[str, Any]] = Field(default_factory=list, description="Top contributing features")


class ExplainRequest(BaseModel):
    """Request schema for explanation endpoint."""
    
    text: str = Field(
        ...,
        min_length=settings.MIN_TEXT_LENGTH,
        max_length=settings.MAX_TEXT_LENGTH,
        description="Text input for explanation"
    )
    method: str = Field(default="shap", description="Explanation method: shap, lime, or rule")
    
    @field_validator('method')
    @classmethod
    def validate_method(cls, v: str) -> str:
        """Validate explanation method."""
        valid_methods = ["shap", "lime", "rule"]
        if v.lower() not in valid_methods:
            raise ValueError(f"Method must be one of: {', '.join(valid_methods)}")
        return v.lower()
    
    @field_validator('text')
    @classmethod
    def clean_text(cls, v: str) -> str:
        """Clean and validate input text."""
        if not v or not v.strip():
            raise ValueError("Text cannot be empty or whitespace only")
        return v.strip()


class ExplainResponse(BaseModel):
    """Response schema for explanation endpoint."""
    
    explanation: List[Dict[str, Any]] = Field(..., description="Detailed explanation data")
    summary: str = Field(..., description="Human-readable explanation summary")


class HealthResponse(BaseModel):
    """Response schema for health check endpoint."""
    
    status: str = Field(..., description="Service health status")


class ErrorResponse(BaseModel):
    """Standard error response schema."""
    
    error: str = Field(..., description="Error message")
    detail: Optional[str] = Field(None, description="Additional error details")
