from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application configuration settings."""
    
    # API Configuration
    API_TITLE: str = "Explainable AI Lite API"
    API_VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"
    
    # CORS Configuration
    CORS_ORIGINS: Union[list[str], str] = ["http://localhost:3000", "http://localhost:5173", "https://explainable-ai-lite.vercel.app", "http://localhost:8080"]
    
    @field_validator('CORS_ORIGINS', mode='before')
    @classmethod
    def parse_cors_origins(cls, v):
        if isinstance(v, str):
            if v.startswith('['):
                # JSON-like format
                import json
                try:
                    return json.loads(v)
                except json.JSONDecodeError:
                    # Fallback to comma-separated
                    return [origin.strip() for origin in v.split(',')]
            else:
                # Comma-separated format
                return [origin.strip() for origin in v.split(',')]
        return v
    
    # Model Configuration
    MODEL_PATH: str = "model/model.pkl"
    VECTORIZER_PATH: str = "model/vectorizer.pkl"
    
    # Validation Configuration
    MAX_TEXT_LENGTH: int = 10000
    MIN_TEXT_LENGTH: int = 1
    
    # Logging Configuration
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
