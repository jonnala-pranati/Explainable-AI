"""
Test script for new ML implementation
Verifies model loading, prediction, and explanations
"""
import sys
import os

# Add backend to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from services.ml_service import ml_service

def test_ml_service():
    """Test ML service functionality"""
    print("="*60)
    print("🧪 Testing ML Service Implementation")
    print("="*60)
    
    # Test 1: Model Loading
    print("\n1. Testing model loading...")
    try:
        ml_service.load_model()
        print("✅ Model loaded successfully")
    except Exception as e:
        print(f"❌ Model loading failed: {e}")
        return False
    
    # Test 2: Prediction
    print("\n2. Testing prediction...")
    test_text = "This movie is absolutely amazing and wonderful"
    try:
        result = ml_service.predict(test_text)
        print(f"✅ Prediction successful")
        print(f"   Prediction: {result['prediction']}")
        print(f"   Confidence: {result['confidence']:.2%}")
        print(f"   Top features: {[f['feature'] for f in result['top_features'][:3]]}")
    except Exception as e:
        print(f"❌ Prediction failed: {e}")
        return False
    
    # Test 3: SHAP Explanation
    print("\n3. Testing SHAP explanation...")
    try:
        shap_result = ml_service.explain_shap(test_text)
        print(f"✅ SHAP explanation successful")
        print(f"   Features: {len(shap_result['explanation'])}")
        print(f"   Summary: {shap_result['summary'][:80]}...")
    except Exception as e:
        print(f"❌ SHAP explanation failed: {e}")
        return False
    
    # Test 4: LIME Explanation
    print("\n4. Testing LIME explanation...")
    try:
        lime_result = ml_service.explain_lime(test_text)
        print(f"✅ LIME explanation successful")
        print(f"   Features: {len(lime_result['explanation'])}")
        print(f"   Summary: {lime_result['summary'][:80]}...")
    except Exception as e:
        print(f"❌ LIME explanation failed: {e}")
        return False
    
    # Test 5: Rule Explanation
    print("\n5. Testing Rule explanation...")
    try:
        rule_result = ml_service.explain_rule(test_text)
        print(f"✅ Rule explanation successful")
        print(f"   Rules: {len(rule_result['explanation'])}")
        print(f"   Summary: {rule_result['summary'][:80]}...")
    except Exception as e:
        print(f"❌ Rule explanation failed: {e}")
        return False
    
    # Test 6: Different Input
    print("\n6. Testing with negative text...")
    negative_text = "This film is terrible and awful"
    try:
        result = ml_service.predict(negative_text)
        print(f"✅ Negative prediction successful")
        print(f"   Prediction: {result['prediction']}")
        print(f"   Confidence: {result['confidence']:.2%}")
    except Exception as e:
        print(f"❌ Negative prediction failed: {e}")
        return False
    
    print("\n" + "="*60)
    print("✅ All tests passed!")
    print("="*60)
    return True

if __name__ == "__main__":
    success = test_ml_service()
    sys.exit(0 if success else 1)
