from typing import Dict, Any, List
from app.ml_bridge.inference import inference_engine
from app.core.logging import get_logger

logger = get_logger(__name__)


class PredictionService:
    """Service layer for prediction operations."""
    
    def __init__(self):
        self.inference = inference_engine
    
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
            
            # Run prediction
            prediction, confidence = self.inference.predict(text)
            
            # Extract top features
            top_features = self.inference.extract_top_features(text)
            
            result = {
                "prediction": prediction,
                "confidence": confidence,
                "top_features": top_features
            }
            
            logger.info(f"Prediction completed: {prediction} with confidence {confidence:.4f}")
            return result
            
        except Exception as e:
            logger.error(f"Prediction service error: {e}")
            raise


# Global prediction service instance
prediction_service = PredictionService()
