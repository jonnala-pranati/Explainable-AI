"""
SHAP Explainer for sentiment analysis
Uses SHAP Linear Explainer for feature importance
"""
import numpy as np
import joblib
from typing import List, Dict, Any


class SHAPExplainer:
    """SHAP explainer for text sentiment analysis"""
    
    def __init__(self, model_path: str, vectorizer_path: str):
        """Initialize SHAP explainer with model and vectorizer"""
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)
        self.feature_names = self.vectorizer.get_feature_names_out()
        
        # For linear models, we can use coefficients directly
        if hasattr(self.model, 'coef_'):
            self.coef = self.model.coef_[0]
        else:
            raise ValueError("Model must have coef_ attribute for SHAP explanation")
    
    def explain(self, text: str, top_k: int = 8) -> List[Dict[str, Any]]:
        """
        Generate SHAP explanation for text
        
        Args:
            text: Input text to explain
            top_k: Number of top features to return
            
        Returns:
            List of dictionaries with feature, value, and direction
        """
        # Transform text
        features = self.vectorizer.transform([text])
        feature_array = features.toarray()[0]
        
        # Get indices of features present in text
        present_indices = np.where(feature_array > 0)[0]
        
        if len(present_indices) == 0:
            return []
        
        # Get SHAP values (for linear model, this is coef * feature_value)
        shap_values = self.coef[present_indices] * feature_array[present_indices]
        present_features = self.feature_names[present_indices]
        
        # Create explanation list
        explanations = []
        for idx, (feature, shap_val, feature_val) in enumerate(zip(present_features, shap_values, feature_array[present_indices])):
            direction = "positive" if shap_val > 0 else "negative"
            explanations.append({
                "feature": feature,
                "value": float(shap_val),
                "contribution": direction,
                "feature_value": float(feature_val)
            })
        
        # Sort by absolute SHAP value
        explanations.sort(key=lambda x: abs(x["value"]), reverse=True)
        
        # Return top k
        return explanations[:top_k]
    
    def get_summary(self, explanations: List[Dict[str, Any]]) -> str:
        """Generate a human-readable summary of the explanation"""
        if not explanations:
            return "No features found in the input text."
        
        top_positive = [e for e in explanations if e["contribution"] == "positive"][:2]
        top_negative = [e for e in explanations if e["contribution"] == "negative"][:2]
        
        summary_parts = []
        
        if top_positive:
            pos_words = ", ".join([f"'{e['feature']}'" for e in top_positive])
            summary_parts.append(f"The words {pos_words} strongly contribute to a positive sentiment.")
        
        if top_negative:
            neg_words = ", ".join([f"'{e['feature']}'" for e in top_negative])
            summary_parts.append(f"The words {neg_words} suggest a negative sentiment.")
        
        return " ".join(summary_parts) if summary_parts else "The sentiment is based on the overall context of the text."


# Singleton instance
_shap_explainer = None


def get_shap_explainer() -> SHAPExplainer:
    """Get singleton SHAP explainer instance"""
    global _shap_explainer
    if _shap_explainer is None:
        _shap_explainer = SHAPExplainer(
            model_path="model/model.pkl",
            vectorizer_path="model/vectorizer.pkl"
        )
    return _shap_explainer
