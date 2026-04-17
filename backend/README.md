# Explainable AI Lite - FastAPI Backend

Production-grade FastAPI backend for the Explainable AI Lite project.

## 🏗️ Architecture

```
backend/
├── app/
│   ├── main.py                    # FastAPI application entry point
│   ├── api/
│   │   ├── routes/
│   │   │   ├── predict.py         # POST /predict endpoint
│   │   │   ├── explain.py         # POST /explain endpoint
│   │   │   └── health.py          # GET /health endpoint
│   ├── models/
│   │   └── schema.py              # Pydantic models for validation
│   ├── services/
│   │   ├── prediction_service.py  # Business logic for predictions
│   │   └── explanation_service.py # Business logic for explanations
│   ├── ml_bridge/
│   │   ├── model_loader.py       # Singleton model loader
│   │   └── inference.py          # ML inference engine
│   ├── core/
│   │   ├── config.py             # Application configuration
│   │   └── logging.py            # Logging setup
│   └── utils/
├── model/
│   ├── model.pkl                 # Trained ML model
│   └── vectorizer.pkl            # Text vectorizer
└── requirements.txt              # Python dependencies
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the Server

```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Or run directly:

```bash
python app/main.py
```

### 3. Access API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📡 API Endpoints

### POST /api/v1/predict

Generate prediction for input text.

**Request:**
```json
{
  "text": "This movie is amazing"
}
```

**Response:**
```json
{
  "prediction": "POSITIVE",
  "confidence": 0.94,
  "top_features": [
    {
      "feature": "amazing",
      "importance": 0.85
    }
  ]
}
```

### POST /api/v1/explain

Generate explanation for prediction.

**Request:**
```json
{
  "text": "This movie is amazing",
  "method": "shap"
}
```

**Response:**
```json
{
  "explanation": [
    {
      "feature": "amazing",
      "value": 0.85,
      "contribution": "positive"
    }
  ],
  "summary": "The model predicted 'POSITIVE' with 94% confidence..."
}
```

**Methods:** `shap`, `lime`, `rule`

### GET /api/v1/health

Check service health status.

**Response:**
```json
{
  "status": "ok"
}
```

## 🔧 FastAPI Concepts Explained

### What is FastAPI?

FastAPI is a modern, fast web framework for building APIs with Python. It's built on top of Starlette (for web parts) and Pydantic (for data validation).

### Key Concepts:

1. **Pydantic Models**: Used for data validation. Automatically validates incoming request data against defined schemas.
   - Example: `PredictRequest` ensures text is not empty and within length limits

2. **Dependency Injection**: FastAPI's powerful system for managing dependencies.
   - Used in our service layer to inject services into routes

3. **Async/Await**: FastAPI supports async operations for better performance.
   - Our endpoints are async to handle multiple requests concurrently

4. **Middleware**: Used for cross-cutting concerns like CORS.
   - We added CORS middleware to allow frontend access

5. **Routers**: Organize endpoints into logical groups.
   - We have separate routers for predict, explain, and health

6. **Lifespan Events**: Startup/shutdown hooks.
   - We load models once at startup using the lifespan context manager

7. **Automatic Documentation**: FastAPI auto-generates Swagger UI and ReDoc.
   - Access at `/docs` and `/redoc`

## 🏛️ Clean Architecture Principles

### Layer Separation:

1. **API Layer** (`api/routes/`): Handles HTTP requests/responses only
   - No business logic
   - Delegates to service layer

2. **Service Layer** (`services/`): Contains business logic
   - Coordinates between ML bridge and API
   - Handles error handling

3. **ML Bridge** (`ml_bridge/`): Connects to ML models
   - Singleton pattern ensures models load once
   - Handles inference operations

4. **Core** (`core/`): Infrastructure concerns
   - Configuration management
   - Logging setup

5. **Models** (`models/`): Data validation schemas
   - Pydantic models for request/response validation

### Why This Architecture?

- **Maintainability**: Each layer has a single responsibility
- **Testability**: Easy to mock dependencies for testing
- **Scalability**: Can scale layers independently
- **Performance**: Models load once, not per request

## ⚡ Performance Optimizations

1. **Singleton Pattern**: Models load once at startup
2. **No Reloading**: Models stay in memory between requests
3. **Async Endpoints**: Handle concurrent requests efficiently
4. **Fast Validation**: Pydantic validates requests quickly

## 🔐 Validation & Error Handling

- **Input Validation**: Pydantic ensures valid input before processing
- **Structured Errors**: Consistent error response format
- **Logging**: All errors logged with context

## 🧪 Testing the API

### Using curl:

```bash
# Health check
curl http://localhost:8000/api/v1/health

# Prediction
curl -X POST http://localhost:8000/api/v1/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "This movie is amazing"}'

# Explanation
curl -X POST http://localhost:8000/api/v1/explain \
  -H "Content-Type: application/json" \
  -d '{"text": "This movie is amazing", "method": "shap"}'
```

### Using Python:

```python
import requests

# Prediction
response = requests.post(
    "http://localhost:8000/api/v1/predict",
    json={"text": "This movie is amazing"}
)
print(response.json())
```

## 📝 Notes

- Dummy models are included for testing. Replace with your trained models.
- Configure CORS origins in `app/core/config.py`
- Adjust logging level in configuration
- Model paths can be changed in config

## 🔄 Replacing with Real Models

1. Train your model using your ML pipeline
2. Save as `model/model.pkl`
3. Save your vectorizer as `model/vectorizer.pkl`
4. Restart the server - models will auto-load

## 🛠️ Development

- Enable hot reload with `--reload` flag
- Check logs for errors
- Use `/docs` for interactive API testing
