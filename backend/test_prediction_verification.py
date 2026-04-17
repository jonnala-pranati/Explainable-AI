"""
Test script to verify that the model is analyzing input text correctly
This helps verify that predictions are based on actual input text
"""
import requests
import json

API_URL = "http://localhost:8000/api/v1/predict"

def test_prediction(text, expected_sentiment):
    """Test prediction with a specific text and verify the result"""
    print(f"\n{'='*60}")
    print(f"Testing: '{text}'")
    print(f"Expected: {expected_sentiment}")
    print(f"{'='*60}")
    
    try:
        response = requests.post(API_URL, json={"text": text})
        response.raise_for_status()
        result = response.json()
        
        print(f"\n📊 Prediction Result:")
        print(f"  Prediction: {result['prediction']}")
        print(f"  Confidence: {result['confidence']:.2%}")
        
        print(f"\n🔍 Top Features (words that influenced prediction):")
        for i, feature in enumerate(result['top_features'][:5], 1):
            # Check if feature word exists in input text
            word_in_text = feature['feature'].lower() in text.lower()
            status = "✓" if word_in_text else "✗"
            print(f"  {i}. {status} '{feature['feature']}' - importance: {feature['importance']:.4f}")
        
        # Verify if prediction matches expected sentiment
        prediction = result['prediction']
        if (expected_sentiment == "positive" and prediction == "POSITIVE") or \
           (expected_sentiment == "negative" and prediction == "NEGATIVE"):
            print(f"\n✅ Prediction matches expected sentiment!")
        else:
            print(f"\n❌ Prediction does NOT match expected sentiment!")
            print(f"   Expected: {expected_sentiment.upper()}, Got: {prediction}")
        
        # Verify if top features are from input text
        features_from_text = sum(1 for f in result['top_features'][:5] 
                                if f['feature'].lower() in text.lower())
        print(f"\n📝 Feature Analysis:")
        print(f"   {features_from_text}/5 top features found in input text")
        
        if features_from_text >= 3:
            print(f"   ✅ Model is using words from your input text!")
        else:
            print(f"   ⚠️  Model might not be using input text properly")
        
        return result
        
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Error: {e}")
        return None

def main():
    """Run test cases with different texts"""
    print("🧪 Testing Model Prediction Verification")
    print("="*60)
    
    test_cases = [
        ("This movie is amazing and wonderful", "positive"),
        ("This film is terrible and awful", "negative"),
        ("Great acting and plot", "positive"),
        ("Bad script and direction", "negative"),
        ("I absolutely loved this film", "positive"),
        ("Complete waste of time", "negative"),
    ]
    
    results = []
    for text, expected in test_cases:
        result = test_prediction(text, expected)
        results.append(result)
    
    print(f"\n{'='*60}")
    print("📋 Summary")
    print(f"{'='*60}")
    print(f"Total tests: {len(test_cases)}")
    print(f"Successful: {sum(1 for r in results if r)}")
    print(f"Failed: {sum(1 for r in results if not r)}")

if __name__ == "__main__":
    main()
