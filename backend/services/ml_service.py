"""
ML Service - Singleton service for model loading and inference
Loads model once at startup and provides prediction/explanation methods
"""
import numpy as np
import joblib
from typing import Dict, Any, List
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from explainers.shap_explainer import get_shap_explainer
from explainers.lime_explainer import get_lime_explainer
from explainers.rule_explainer import get_rule_explainer


class MLService:
    """Singleton ML service for model inference"""
    
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Initialize ML service (only once)"""
        if not self._initialized:
            self.model = None
            self.vectorizer = None
            self.shap_explainer = None
            self.lime_explainer = None
            self.rule_explainer = None
            self._initialized = True
    
    def load_model(self, model_path: str = "model/model.pkl", vectorizer_path: str = "model/vectorizer.pkl"):
        """Load model and vectorizer (only once)"""
        if self.model is None:
            print("📦 Loading ML model...")
            self.model = joblib.load(model_path)
            self.vectorizer = joblib.load(vectorizer_path)
            print("✅ Model loaded successfully")
            
            # Initialize explainers
            self.shap_explainer = get_shap_explainer()
            self.lime_explainer = get_lime_explainer()
            self.rule_explainer = get_rule_explainer()
            print("✅ Explainers initialized")
    
    def predict(self, text: str) -> Dict[str, Any]:
        """
        Predict sentiment for input text
        
        Args:
            text: Input text to analyze
            
        Returns:
            Dictionary with prediction, confidence, and top_features
        """
        if self.model is None or self.vectorizer is None:
            self.load_model()
        
        # Transform text
        features = self.vectorizer.transform([text])
        
        # Get prediction
        prediction = self.model.predict(features)[0]
        
        # Convert to label
        prediction_label = "POSITIVE" if prediction == 1 else "NEGATIVE"
        
        # Get confidence
        if hasattr(self.model, 'predict_proba'):
            probabilities = self.model.predict_proba(features)[0]
            confidence = float(max(probabilities))
        else:
            confidence = 1.0
        
        # Extract top features from input text
        top_features = self._extract_top_features(text, features, top_k=10)
        
        return {
            "prediction": prediction_label,
            "confidence": confidence,
            "top_features": top_features
        }
    
    def _extract_top_features(self, text: str, features, top_k: int = 10) -> List[Dict[str, Any]]:
        """Extract top contributing features from input text"""
        feature_array = features.toarray()[0]
        present_indices = np.where(feature_array > 0)[0]
        
        if len(present_indices) == 0:
            return []
        
        # Get feature importance
        if hasattr(self.model, 'coef_'):
            importance = self.model.coef_[0]
        else:
            importance = feature_array
        
        # Get importance for present features
        present_importance = importance[present_indices]
        present_feature_names = self.vectorizer.get_feature_names_out()[present_indices]
        
        # Sort by absolute importance
        sorted_indices = np.argsort(np.abs(present_importance))[::-1]
        
        # Get top k
        top_k = min(top_k, len(sorted_indices))
        top_indices = sorted_indices[:top_k]
        
        # Build feature list
        top_features = []
        for idx in top_indices:
            top_features.append({
                "feature": present_feature_names[idx],
                "importance": float(present_importance[idx])
            })
        
        return top_features
    
    def explain_shap(self, text: str) -> Dict[str, Any]:
        """
        Generate SHAP explanation
        
        Args:
            text: Input text to explain
            
        Returns:
            Dictionary with explanation array and summary
        """
        if self.shap_explainer is None:
            self.load_model()
        
        explanation = self.shap_explainer.explain(text)
        summary = self.shap_explainer.get_summary(explanation)
        
        return {
            "explanation": explanation,
            "summary": summary
        }
    
    def explain_lime(self, text: str) -> Dict[str, Any]:
        """
        Generate LIME explanation
        
        Args:
            text: Input text to explain
            
        Returns:
            Dictionary with explanation array and summary
        """
        if self.lime_explainer is None:
            self.load_model()
        
        explanation = self.lime_explainer.explain(text)
        summary = self.lime_explainer.get_summary(explanation)
        
        return {
            "explanation": explanation,
            "summary": summary
        }
    
    def explain_rule(self, text: str) -> Dict[str, Any]:
        """
        Generate rule-based explanation
        
        Args:
            text: Input text to explain
            
        Returns:
            Dictionary with explanation array and summary
        """
        if self.rule_explainer is None:
            self.load_model()
        
        explanation = self.rule_explainer.explain(text)
        summary = self.rule_explainer.get_summary(explanation)
        
        return {
            "explanation": explanation,
            "summary": summary
        }


# Global singleton instance
ml_service = MLService()
