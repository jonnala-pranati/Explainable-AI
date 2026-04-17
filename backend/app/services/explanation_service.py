from typing import Dict, Any, List
from services.ml_service import ml_service
from app.core.logging import get_logger

logger = get_logger(__name__)


class ExplanationService:
    """Service layer for explanation operations."""
    
    def __init__(self):
        self.ml = ml_service
    
    def explain(self, text: str, method: str = "shap") -> Dict[str, Any]:
        """
        Generate explanation for prediction using specified method.
        
        Args:
            text: Input text for explanation
            method: Explanation method (shap, lime, or rule)
            
        Returns:
            Dictionary containing explanation data and summary
        """
        try:
            logger.info(f"Processing explanation request with method: {method}")
            
            # Route to appropriate explanation method
            if method == "shap":
                result = self.ml.explain_shap(text)
            elif method == "lime":
                result = self.ml.explain_lime(text)
            elif method == "rule":
                result = self.ml.explain_rule(text)
            else:
                raise ValueError(f"Unknown explanation method: {method}")
            
            logger.info(f"Explanation completed using method: {method}")
            return result
            
        except Exception as e:
            logger.error(f"Explanation service error: {e}")
            raise


# Global explanation service instance
explanation_service = ExplanationService()
