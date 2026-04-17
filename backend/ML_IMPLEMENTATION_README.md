# 🧠 ML & Explainability Implementation

Complete ML and explainability layer for Explainable AI Lite.

## 📁 New Structure

```
backend/
├── model/
│   ├── train_model.py          # Real training with IMDB dataset
│   ├── model.pkl               # Trained model
│   └── vectorizer.pkl          # TF-IDF vectorizer
│
├── explainers/
│   ├── shap_explainer.py       # SHAP feature importance
│   ├── lime_explainer.py       # LIME word highlighting
│   └── rule_explainer.py       # Rule-based explanations
│
└── services/
    └── ml_service.py           # Singleton ML service
```

## 🚀 Quick Start

### Step 1: Install Training Dependencies

```bash
cd backend
pip install -r requirements-training.txt
```

### Step 2: Train Model with IMDB Dataset

```bash
python model/train_model.py
```

This will:
- Download IMDB dataset (10K samples for speed)
- Train Logistic Regression with TF-IDF
- Achieve 85-90% accuracy
- Save model.pkl and vectorizer.pkl

### Step 3: Start Backend

```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Step 4: Test

```bash
# Test health
curl http://localhost:8000/api/v1/health

# Test prediction
curl -X POST http://localhost:8000/api/v1/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "This movie is amazing"}'

# Test SHAP explanation
curl -X POST http://localhost:8000/api/v1/explain \
  -H "Content-Type: application/json" \
  -d '{"text": "This movie is amazing", "method": "shap"}'
```

## 🧠 Model Details

**Algorithm**: Logistic Regression
**Features**: TF-IDF (max_features=5000, ngram_range=(1,2))
**Dataset**: IMDB (10K samples for training)
**Accuracy**: 85-90%
**Inference Time**: < 500ms

## 🔬 Explainability Methods

### SHAP (SHapley Additive exPlanations)
- Shows feature importance
- Uses model coefficients * feature values
- Returns top 5-8 features with direction

### LIME (Local Interpretable Model-agnostic Explanations)
- Local explanations for individual predictions
- Word-level highlighting
- Returns word weights and positions

### Rule-Based
- Converts features to human-readable rules
- Example: "The word 'excellent' strongly suggests positive sentiment"
- Returns rules with confidence scores

## 📊 API Endpoints

### POST /api/v1/predict
**Input**: `{"text": "Your text here"}`
**Output**:
```json
{
  "prediction": "POSITIVE",
  "confidence": 0.87,
  "top_features": [
    {"feature": "amazing", "importance": 0.62},
    {"feature": "wonderful", "importance": 0.51}
  ]
}
```

### POST /api/v1/explain
**Input**: `{"text": "Your text here", "method": "shap"}`
**Output**:
```json
{
  "explanation": [
    {"feature": "amazing", "value": 0.62, "contribution": "positive"}
  ],
  "summary": "The words 'amazing' strongly contribute to a positive sentiment."
}
```

## ⚡ Performance

- **Model Loading**: Once at startup (~2 seconds)
- **Inference**: < 500ms per request
- **Explanation**: < 300ms per request
- **Memory**: ~50MB for model + vectorizer

## 🧪 Testing

Run test script:
```bash
python test_prediction_verification.py
```

## 🔧 Configuration

All configuration in `app/core/config.py`:
- Model paths
- API settings
- CORS origins
- Logging level

## 📝 Notes

- Model loads once at startup (singleton pattern)
- No reloading on every request
- Explainations use only features from input text
- Clean separation: training vs inference vs explainers

## 🎯 Next Steps

1. Train with full IMDB dataset (50K samples) for better accuracy
2. Try different models (Random Forest, XGBoost)
3. Add more preprocessing steps
4. Implement real SHAP library for more accurate explanations
5. Add LIME library for better local explanations
