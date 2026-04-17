import numpy as np
from typing import Dict, Any, List
from app.ml_bridge.model_loader import model_loader
from app.core.logging import get_logger

logger = get_logger(__name__)


class InferenceEngine:
    """Handles ML inference operations."""
    
    def __init__(self):
        self.model = None
        self.vectorizer = None
    
    def initialize(self) -> None:
        """Initialize inference engine with loaded models."""
        self.model = model_loader.get_model()
        self.vectorizer = model_loader.get_vectorizer()
        logger.info("Inference engine initialized")
    
    def transform_text(self, text: str) -> np.ndarray:
        """
        Transform input text using the vectorizer.
        
        Args:
            text: Input text to transform
            
        Returns:
            Transformed feature matrix
        """
        try:
            # Transform text to feature vector
            features = self.vectorizer.transform([text])
            return features
        except Exception as e:
            logger.error(f"Error transforming text: {e}")
            raise
    
    def predict(self, text: str) -> tuple[str, float]:
        """
        Run prediction on input text.
        
        Args:
            text: Input text for prediction
            
        Returns:
            Tuple of (prediction_label, confidence_score)
        """
        try:
            # Transform text
            features = self.transform_text(text)
            
            # Get prediction
            prediction = self.model.predict(features)[0]
            
            # Convert numeric prediction to label
            if prediction == 1 or prediction == "1":
                prediction_label = "POSITIVE"
            else:
                prediction_label = "NEGATIVE"
            
            # Get probability/confidence
            if hasattr(self.model, 'predict_proba'):
                probabilities = self.model.predict_proba(features)[0]
                confidence = float(max(probabilities))
            else:
                # For models without predict_proba, use decision function or default to 1.0
                if hasattr(self.model, 'decision_function'):
                    decision = self.model.decision_function(features)[0]
                    confidence = float(1 / (1 + np.exp(-decision)))  # Sigmoid
                else:
                    confidence = 1.0
            
            logger.info(f"Prediction: {prediction_label}, Confidence: {confidence:.4f}")
            return prediction_label, confidence
            
        except Exception as e:
            logger.error(f"Error during prediction: {e}")
            raise
    
    def extract_top_features(self, text: str, top_k: int = 10) -> List[Dict[str, Any]]:
        """
        Extract top contributing features for the prediction.
        Only returns features that are present in the input text.
        
        Args:
            text: Input text
            top_k: Number of top features to return
            
        Returns:
            List of dictionaries with feature names and importance scores
        """
        try:
            # Transform text
            features = self.transform_text(text)
            
            # Get feature names from vectorizer
            feature_names = self.vectorizer.get_feature_names_out()
            
            # Get feature importance from model
            if hasattr(self.model, 'coef_'):
                # Linear models
                importance = self.model.coef_[0]
            elif hasattr(self.model, 'feature_importances_'):
                # Tree-based models
                importance = self.model.feature_importances_
            else:
                # Fallback: use TF-IDF values
                importance = features.toarray()[0]
            
            # Get indices of features present in the input text (non-zero values)
            feature_array = features.toarray()[0]
            present_indices = np.where(feature_array > 0)[0]
            
            # If no features present, return empty list
            if len(present_indices) == 0:
                logger.warning("No features found in input text")
                return []
            
            # Get importance only for features present in text
            present_importance = importance[present_indices]
            present_feature_names = feature_names[present_indices]
            
            # Sort by absolute importance
            sorted_indices = np.argsort(np.abs(present_importance))[::-1]
            
            # Get top k features
            top_k = min(top_k, len(sorted_indices))
            top_indices = sorted_indices[:top_k]
            
            # Build feature list
            top_features = []
            for idx in top_indices:
                original_idx = present_indices[idx]
                top_features.append({
                    "feature": present_feature_names[idx],
                    "importance": float(present_importance[idx])
                })
            
            logger.info(f"Extracted {len(top_features)} top features from {len(present_indices)} present features")
            return top_features
            
        except Exception as e:
            logger.error(f"Error extracting features: {e}")
            return []


# Global inference engine instance
inference_engine = InferenceEngine()
