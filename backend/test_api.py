"""Test script for FastAPI backend"""
import requests
import json

BASE_URL = "http://localhost:8000/api/v1"

def test_health():
    """Test health endpoint"""
    print("Testing health endpoint...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

def test_predict():
    """Test predict endpoint"""
    print("Testing predict endpoint...")
    payload = {"text": "This movie is amazing"}
    response = requests.post(f"{BASE_URL}/predict", json=payload)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_explain():
    """Test explain endpoint"""
    print("Testing explain endpoint...")
    payload = {"text": "This movie is amazing", "method": "shap"}
    response = requests.post(f"{BASE_URL}/explain", json=payload)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

if __name__ == "__main__":
    try:
        test_health()
        test_predict()
        test_explain()
        print("All tests passed!")
    except Exception as e:
        print(f"Error: {e}")
