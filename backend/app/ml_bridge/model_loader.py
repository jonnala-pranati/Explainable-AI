import joblib
from typing import Optional, Any
from app.core.logging import get_logger
from app.core.config import settings

logger = get_logger(__name__)


class ModelLoader:
    """Singleton class for loading ML models at startup."""
    
    _instance: Optional['ModelLoader'] = None
    _model: Optional[Any] = None
    _vectorizer: Optional[Any] = None
    
    def __new__(cls) -> 'ModelLoader':
        """Implement singleton pattern."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def load_models(self) -> None:
        """Load model and vectorizer from disk (called once at startup)."""
        if self._model is not None and self._vectorizer is not None:
            logger.info("Models already loaded, skipping reload")
            return
        
        try:
            logger.info(f"Loading model from {settings.MODEL_PATH}")
            self._model = joblib.load(settings.MODEL_PATH)
            logger.info("Model loaded successfully")
            
            logger.info(f"Loading vectorizer from {settings.VECTORIZER_PATH}")
            self._vectorizer = joblib.load(settings.VECTORIZER_PATH)
            logger.info("Vectorizer loaded successfully")
            
        except FileNotFoundError as e:
            logger.error(f"Model files not found: {e}")
            raise
        except Exception as e:
            logger.error(f"Error loading models: {e}")
            raise
    
    def get_model(self) -> Any:
        """Get the loaded model instance."""
        if self._model is None:
            raise RuntimeError("Model not loaded. Call load_models() first.")
        return self._model
    
    def get_vectorizer(self) -> Any:
        """Get the loaded vectorizer instance."""
        if self._vectorizer is None:
            raise RuntimeError("Vectorizer not loaded. Call load_models() first.")
        return self._vectorizer
    
    def is_loaded(self) -> bool:
        """Check if models are loaded."""
        return self._model is not None and self._vectorizer is not None


# Global singleton instance
model_loader = ModelLoader()
