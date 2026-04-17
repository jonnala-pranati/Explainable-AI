from typing import Dict, Any, List
from services.ml_service import ml_service
from app.core.logging import get_logger

logger = get_logger(__name__)


class PredictionService:
    """Service layer for prediction operations."""
    
    def __init__(self):
        self.ml = ml_service
    
    def predict(self, text: str) -> Dict[str, Any]:
        """
        Generate prediction for input text.
        
        Args:
            text: Input text for prediction
            
        Returns:
            Dictionary containing prediction, confidence, and top features
        """
        try:
            logger.info(f"Processing prediction request for text length: {len(text)}")
            
            # Run prediction using ML service
            result = self.ml.predict(text)
            
            logger.info(f"Prediction completed: {result['prediction']} with confidence {result['confidence']:.4f}")
            return result
            
        except Exception as e:
            logger.error(f"Prediction service error: {e}")
            raise


# Global prediction service instance
prediction_service = PredictionService()
