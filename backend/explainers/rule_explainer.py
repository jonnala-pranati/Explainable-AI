"""
Rule-Based Explainer for sentiment analysis
Converts feature importance into human-readable rules
"""
import numpy as np
import joblib
from typing import List, Dict, Any


class RuleExplainer:
    """Rule-based explainer for text sentiment analysis"""
    
    def __init__(self, model_path: str, vectorizer_path: str):
        """Initialize rule explainer with model and vectorizer"""
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)
        self.feature_names = self.vectorizer.get_feature_names_out()
        
        # Get model coefficients
        if hasattr(self.model, 'coef_'):
            self.coef = self.model.coef_[0]
        else:
            raise ValueError("Model must have coef_ attribute for rule explanation")
    
    def explain(self, text: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """
        Generate rule-based explanation for text
        
        Args:
            text: Input text to explain
            top_k: Number of top rules to return
            
        Returns:
            List of dictionaries with rule, confidence, and support
        """
        # Transform text
        features = self.vectorizer.transform([text])
        feature_array = features.toarray()[0]
        
        # Get indices of features present in text
        present_indices = np.where(feature_array > 0)[0]
        
        if len(present_indices) == 0:
            return []
        
        # Get word importance
        word_importance = self.coef[present_indices] * feature_array[present_indices]
        present_features = self.feature_names[present_indices]
        
        # Create rule explanations
        rules = []
        for feature, importance, feature_val in zip(present_features, word_importance, feature_array[present_indices]):
            rule = self._generate_rule(feature, importance)
            confidence = min(abs(importance) * 100, 95)  # Cap at 95%
            support = f"{feature_val:.2f}"
            
            rules.append({
                "rule": rule,
                "confidence": float(confidence),
                "support": support
            })
        
        # Sort by confidence
        rules.sort(key=lambda x: x["confidence"], reverse=True)
        
        # Return top k
        return rules[:top_k]
    
    def _generate_rule(self, word: str, importance: float) -> str:
        """Generate a human-readable rule for a word"""
        if importance > 0.5:
            return f"The word '{word}' strongly suggests a positive sentiment."
        elif importance > 0.1:
            return f"The word '{word}' contributes positively to the sentiment."
        elif importance < -0.5:
            return f"The word '{word}' strongly indicates a negative sentiment."
        elif importance < -0.1:
            return f"The word '{word}' contributes negatively to the sentiment."
        else:
            return f"The word '{word}' has a neutral effect on sentiment."
    
    def get_summary(self, rules: List[Dict[str, Any]]) -> str:
        """Generate a human-readable summary of the explanation"""
        if not rules:
            return "No features found in the input text."
        
        positive_rules = [r for r in rules if "positive" in r["rule"].lower()]
        negative_rules = [r for r in rules if "negative" in r["rule"].lower()]
        
        if len(positive_rules) > len(negative_rules):
            return "The text appears to express a positive sentiment based on the presence of favorable words."
        elif len(negative_rules) > len(positive_rules):
            return "The text appears to express a negative sentiment based on the presence of critical words."
        else:
            return "The text contains a mix of positive and negative indicators, suggesting a neutral or mixed sentiment."


# Singleton instance
_rule_explainer = None


def get_rule_explainer() -> RuleExplainer:
    """Get singleton rule explainer instance"""
    global _rule_explainer
    if _rule_explainer is None:
        _rule_explainer = RuleExplainer(
            model_path="model/model.pkl",
            vectorizer_path="model/vectorizer.pkl"
        )
    return _rule_explainer
