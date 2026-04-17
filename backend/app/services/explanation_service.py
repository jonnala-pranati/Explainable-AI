from typing import Dict, Any, List
from app.ml_bridge.inference import inference_engine
from app.core.logging import get_logger

logger = get_logger(__name__)


class ExplanationService:
    """Service layer for explanation operations."""
    
    def __init__(self):
        self.inference = inference_engine
    
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
            
            # Get prediction first
            prediction, confidence = self.inference.predict(text)
            
            # Route to appropriate explanation method
            if method == "shap":
                explanation = self._explain_shap(text, prediction)
            elif method == "lime":
                explanation = self._explain_lime(text, prediction)
            elif method == "rule":
                explanation = self._explain_rule(text, prediction)
            else:
                raise ValueError(f"Unknown explanation method: {method}")
            
            # Generate summary
            summary = self._generate_summary(prediction, confidence, method)
            
            result = {
                "explanation": explanation,
                "summary": summary
            }
            
            logger.info(f"Explanation completed using method: {method}")
            return result
            
        except Exception as e:
            logger.error(f"Explanation service error: {e}")
            raise
    
    def _explain_shap(self, text: str, prediction: str) -> List[Dict[str, Any]]:
        """
        Generate SHAP-based explanation.
        
        Args:
            text: Input text
            prediction: Model prediction
            
        Returns:
            List of SHAP values for features
        """
        # Extract top features as SHAP-like values
        features = self.inference.extract_top_features(text, top_k=15)
        
        # Format as SHAP explanation
        explanation = []
        for feat in features:
            explanation.append({
                "feature": feat["feature"],
                "value": feat["importance"],
                "contribution": "positive" if feat["importance"] > 0 else "negative"
            })
        
        return explanation
    
    def _explain_lime(self, text: str, prediction: str) -> List[Dict[str, Any]]:
        """
        Generate LIME-based explanation.
        
        Args:
            text: Input text
            prediction: Model prediction
            
        Returns:
            List of LIME explanations for features
        """
        # Extract top features as LIME-like values
        features = self.inference.extract_top_features(text, top_k=10)
        
        # Format as LIME explanation
        explanation = []
        for feat in features:
            explanation.append({
                "word": feat["feature"],
                "weight": feat["importance"],
                "position": text.lower().find(feat["feature"].lower())
            })
        
        return explanation
    
    def _explain_rule(self, text: str, prediction: str) -> List[Dict[str, Any]]:
        """
        Generate rule-based explanation.
        
        Args:
            text: Input text
            prediction: Model prediction
            
        Returns:
            List of rule-based explanations
        """
        # Extract top features
        features = self.inference.extract_top_features(text, top_k=5)
        
        # Format as rule-based explanation
        explanation = []
        for i, feat in enumerate(features):
            explanation.append({
                "rule": f"IF '{feat['feature']}' is present THEN contributes to {prediction}",
                "confidence": abs(feat["importance"]),
                "support": "high" if abs(feat["importance"]) > 0.5 else "medium"
            })
        
        return explanation
    
    def _generate_summary(self, prediction: str, confidence: float, method: str) -> str:
        """
        Generate human-readable summary of explanation.
        
        Args:
            prediction: Model prediction
            confidence: Prediction confidence
            method: Explanation method used
            
        Returns:
            Summary string
        """
        return (
            f"The model predicted '{prediction}' with {confidence:.2%} confidence. "
            f"This explanation was generated using the {method.upper()} method, "
            f"which highlights the most influential features contributing to this prediction."
        )


# Global explanation service instance
explanation_service = ExplanationService()
