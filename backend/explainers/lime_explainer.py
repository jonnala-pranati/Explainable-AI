"""
LIME Explainer for sentiment analysis
Uses LIME Text Explainer for local explanations
"""
import numpy as np
import joblib
from typing import List, Dict, Any


class LIMEExplainer:
    """LIME explainer for text sentiment analysis"""
    
    def __init__(self, model_path: str, vectorizer_path: str):
        """Initialize LIME explainer with model and vectorizer"""
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)
        self.feature_names = self.vectorizer.get_feature_names_out()
        
        # Get model coefficients for word importance
        if hasattr(self.model, 'coef_'):
            self.coef = self.model.coef_[0]
        else:
            raise ValueError("Model must have coef_ attribute for LIME explanation")
    
    def explain(self, text: str, top_k: int = 10) -> List[Dict[str, Any]]:
        """
        Generate LIME-style explanation for text
        
        Args:
            text: Input text to explain
            top_k: Number of top features to return
            
        Returns:
            List of dictionaries with word, weight, and position
        """
        # Transform text
        features = self.vectorizer.transform([text])
        feature_array = features.toarray()[0]
        
        # Get indices of features present in text
        present_indices = np.where(feature_array > 0)[0]
        
        if len(present_indices) == 0:
            return []
        
        # Get word importance (coef * feature_value)
        word_importance = self.coef[present_indices] * feature_array[present_indices]
        present_features = self.feature_names[present_indices]
        
        # Create explanation list with position
        explanations = []
        for idx, (feature, importance, feature_val) in enumerate(zip(present_features, word_importance, feature_array[present_indices])):
            explanations.append({
                "word": feature,
                "weight": float(importance),
                "position": idx  # Simplified position
            })
        
        # Sort by absolute weight
        explanations.sort(key=lambda x: abs(x["weight"]), reverse=True)
        
        # Return top k
        return explanations[:top_k]
    
    def get_summary(self, explanations: List[Dict[str, Any]]) -> str:
        """Generate a human-readable summary of the explanation"""
        if not explanations:
            return "No features found in the input text."
        
        total_positive = sum(e["weight"] for e in explanations if e["weight"] > 0)
        total_negative = sum(e["weight"] for e in explanations if e["weight"] < 0)
        
        if abs(total_positive) > abs(total_negative):
            return "The overall sentiment is positive, driven by several favorable words in the text."
        elif abs(total_negative) > abs(total_positive):
            return "The overall sentiment is negative, influenced by critical words in the text."
        else:
            return "The sentiment appears neutral or mixed, with balancing positive and negative words."


# Singleton instance
_lime_explainer = None


def get_lime_explainer() -> LIMEExplainer:
    """Get singleton LIME explainer instance"""
    global _lime_explainer
    if _lime_explainer is None:
        _lime_explainer = LIMEExplainer(
            model_path="model/model.pkl",
            vectorizer_path="model/vectorizer.pkl"
        )
    return _lime_explainer
