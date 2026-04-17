from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application configuration settings."""
    
    # API Configuration
    API_TITLE: str = "Explainable AI Lite API"
    API_VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"
    
    # CORS Configuration
    CORS_ORIGINS: list[str] = ["http://localhost:3000", "http://localhost:5173"]
    
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
