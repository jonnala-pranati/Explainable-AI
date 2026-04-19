# 🎬 Explainable AI 

A production-grade full-stack application for sentiment analysis with explainable AI (XAI) capabilities. Built with React (frontend) and FastAPI (backend), featuring SHAP, LIME, and rule-based explanations.

## ✨ Features

- 🤖 **Sentiment Analysis**: Predict positive/negative sentiment from text
- 🔍 **SHAP Explanations**: Feature importance with direction
- 🎨 **LIME Explanations**: Word-level highlighting
- 📝 **Rule-Based Explanations**: Human-readable rules
- ⚡ **Fast Inference**: < 500ms response time
- 🎨 **Modern UI**: Beautiful dark theme with animations
- 📱 **Responsive Design**: Works on all devices
- 🚀 **Production-Ready**: Clean architecture, error handling, logging

## 🏗️ Architecture

```
Explainable-AI/
├── frontend/                 # React + Vite + TypeScript
│   ├── src/
│   │   ├── components/       # UI components
│   │   ├── pages/           # Page components
│   │   ├── hooks/           # Custom React hooks
│   │   ├── services/        # API service
│   │   └── lib/             # Utilities
│   ├── package.json
│   └── vite.config.ts
│
├── backend/                  # FastAPI + Python
│   ├── app/
│   │   ├── api/            # API routes
│   │   ├── core/           # Configuration & logging
│   │   ├── models/         # Pydantic schemas
│   │   └── services/       # Business logic
│   ├── model/              # ML training
│   │   ├── train_model.py
│   │   ├── model.pkl
│   │   └── vectorizer.pkl
│   ├── explainers/         # XAI methods
│   │   ├── shap_explainer.py
│   │   ├── lime_explainer.py
│   │   └── rule_explainer.py
│   ├── services/           # ML service
│   │   └── ml_service.py
│   ├── requirements.txt
│   └── main.py
│
└── README.md               # This file
```

## 🚀 Quick Start

### Prerequisites

- **Node.js** (v18+) - [Download](https://nodejs.org/)
- **Python** (v3.8+) - [Download](https://python.org/)
- **pip** (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jonnala-pranati/Explainable-AI.git
   cd Explainable-AI
   ```

2. **Backend Setup**
   ```bash
   cd backend
   pip install -r requirements.txt
   pip install -r requirements-training.txt
   ```

3. **Frontend Setup**
   ```bash
   cd ../frontend
   npm install
   ```

### Running the Application

#### Option 1: Run Both (Recommended)

**Terminal 1 - Backend:**
```bash
cd backend
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

#### Option 2: Run Backend Only

```bash
cd backend
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Access API docs at: http://localhost:8000/docs

#### Option 3: Run Frontend Only

```bash
cd frontend
npm run dev
```

Access app at: http://localhost:8080

## 📊 Model Training

### Current Model
- **Algorithm**: Logistic Regression
- **Features**: TF-IDF (max_features=5000)
- **Dataset**: Sample data (40 samples)
- **Accuracy**: 50-65%

### Train with IMDB Dataset (Recommended for 85-90% accuracy)

1. **Download IMDB Dataset**
   - Kaggle: https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews
   - Download `IMDB Dataset.csv`
   - Place in `backend/` folder

2. **Train Model**
   ```bash
   cd backend
   python model/train_model.py
   ```

3. **Restart Backend**
   ```bash
   # Stop backend (Ctrl+C)
   python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

## 🔧 Configuration

### Backend Configuration

File: `backend/app/core/config.py`

```python
class Settings(BaseSettings):
    API_TITLE: str = "Explainable AI Lite API"
    API_VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"
    LOG_LEVEL: str = "INFO"
    CORS_ORIGINS: List[str] = ["http://localhost:8080"]
```

### Frontend Configuration

File: `frontend/.env`

```env
VITE_API_URL=http://localhost:8000/api/v1
```

## 📡 API Endpoints

### Health Check
```http
GET /api/v1/health
```

### Prediction
```http
POST /api/v1/predict
Content-Type: application/json

{
  "text": "This movie is amazing"
}

Response:
{
  "prediction": "POSITIVE",
  "confidence": 0.87,
  "top_features": [
    {"feature": "amazing", "importance": 0.62}
  ]
}
```

### SHAP Explanation
```http
POST /api/v1/explain
Content-Type: application/json

{
  "text": "This movie is amazing",
  "method": "shap"
}

Response:
{
  "explanation": [
    {
      "feature": "amazing",
      "value": 0.62,
      "contribution": "positive"
    }
  ],
  "summary": "The words 'amazing' strongly contribute to a positive sentiment."
}
```

### LIME Explanation
```http
POST /api/v1/explain
Content-Type: application/json

{
  "text": "This movie is amazing",
  "method": "lime"
}

Response:
{
  "explanation": [
    {
      "word": "amazing",
      "weight": 0.62,
      "position": 0
    }
  ],
  "summary": "The overall sentiment is positive, driven by favorable words."
}
```

### Rule-Based Explanation
```http
POST /api/v1/explain
Content-Type: application/json

{
  "text": "This movie is amazing",
  "method": "rule"
}

Response:
{
  "explanation": [
    {
      "rule": "The word 'amazing' strongly suggests a positive sentiment.",
      "confidence": 62.0,
      "support": "0.62"
    }
  ],
  "summary": "The text appears to express a positive sentiment."
}
```

## 🎨 Frontend Components

### Pages
- **Home**: Landing page with hero section and features
- **Analyze**: Main analysis page with input panel and results

### Components
- **Navbar**: Navigation bar
- **Footer**: Footer with links
- **InputPanel**: Text input and method selection
- **PredictionBadge**: Displays prediction result
- **ShapChart**: SHAP feature importance chart
- **LimeHighlights**: LIME word highlighting
- **RuleExplainer**: Rule-based explanation display
- **WordImportanceTable**: Feature importance table

### Hooks
- **usePrediction**: Custom hook for prediction and explanation logic

## 🔬 Tech Stack

### Frontend
- **React 18**: UI library
- **TypeScript**: Type safety
- **Vite**: Build tool
- **Tailwind CSS**: Styling
- **Framer Motion**: Animations
- **React Query**: Data fetching
- **Axios**: HTTP client
- **Recharts**: Charts
- **Lucide React**: Icons

### Backend
- **FastAPI**: Web framework
- **Python 3.8+**: Language
- **scikit-learn**: ML library
- **pandas**: Data manipulation
- **numpy**: Numerical computing
- **joblib**: Model serialization
- **Pydantic**: Data validation
- **Uvicorn**: ASGI server

### ML/XAI
- **Logistic Regression**: Classification model
- **TF-IDF**: Feature extraction
- **SHAP**: Feature importance (simplified)
- **LIME**: Local explanations (simplified)
- **Rule-Based**: Human-readable rules

## 📈 Performance

- **Model Loading**: ~2 seconds (once at startup)
- **Inference Time**: < 500ms
- **Explanation Time**: < 300ms
- **Memory Usage**: ~50MB
- **API Response**: < 1 second total

## 🧪 Testing

### Backend Tests
```bash
cd backend
python test_ml_implementation.py
python test_prediction_verification.py
```

### Frontend Tests
```bash
cd frontend
npm test
```

## 🐛 Troubleshooting

### Backend Issues

**Issue: "Module not found"**
```bash
cd backend
pip install -r requirements.txt
```

**Issue: "Model file not found"**
```bash
cd backend
python model/train_model.py
```

**Issue: Port already in use**
```bash
# Change port in uvicorn command
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8001
```

### Frontend Issues

**Issue: "npm install fails"**
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

**Issue: "API connection refused"**
- Check backend is running
- Check `frontend/.env` has correct API URL
- Check CORS configuration in backend

**Issue: "Port already in use"**
```bash
# Change port in vite.config.ts
# or kill the process
npx kill-port 8080
```

## 🚀 Deployment

### Frontend Deployment (Vercel)

1. Push code to GitHub
2. Import project in Vercel
3. Configure build settings:
   - Framework: Vite
   - Root directory: `frontend`
4. Add environment variable: `VITE_API_URL`
5. Deploy

### Backend Deployment (Railway/Render)

1. Push code to GitHub
2. Import project in Railway/Render
3. Configure:
   - Build command: `pip install -r requirements.txt`
   - Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
4. Add environment variables
5. Deploy

## 📝 Project Structure

### Backend Structure
```
backend/
├── app/
│   ├── api/
│   │   └── routes/          # API endpoints
│   │       ├── predict.py    # POST /predict
│   │       ├── explain.py    # POST /explain
│   │       └── health.py     # GET /health
│   ├── core/
│   │   ├── config.py         # Configuration
│   │   └── logging.py        # Logging setup
│   ├── models/
│   │   └── schema.py         # Pydantic models
│   └── services/
│       ├── prediction_service.py
│       └── explanation_service.py
├── model/
│   ├── train_model.py        # Training script
│   ├── model.pkl             # Trained model
│   └── vectorizer.pkl        # TF-IDF vectorizer
├── explainers/
│   ├── shap_explainer.py     # SHAP implementation
│   ├── lime_explainer.py     # LIME implementation
│   └── rule_explainer.py     # Rule-based implementation
├── services/
│   └── ml_service.py         # Singleton ML service
└── main.py                   # FastAPI app
```

### Frontend Structure
```
frontend/
├── src/
│   ├── components/
│   │   ├── features/
│   │   │   ├── prediction/   # Prediction components
│   │   │   ├── explanation/ # Explanation components
│   │   │   └── table/       # Table components
│   │   ├── layout/          # Layout components
│   │   └── ui/              # UI components
│   ├── pages/
│   │   ├── Home.tsx
│   │   ├── Analyze.tsx
│   │   └── NotFound.tsx
│   ├── hooks/
│   │   └── usePrediction.ts
│   ├── services/
│   │   └── api.ts
│   ├── lib/
│   │   └── utils.ts
│   ├── App.tsx
│   └── main.tsx
├── public/                   # Static assets
└── package.json
```

## 🔐 Security

- Input validation with Pydantic
- CORS configuration
- Error handling and logging
- No sensitive data in logs
- Environment variables for configuration

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions or support, please open an issue on GitHub.

## 🙏 Acknowledgments

- IMDB dataset for sentiment analysis
- scikit-learn for ML tools
- SHAP and LIME for explainability concepts
- React and FastAPI communities

---

**Built with ❤️ using React, FastAPI, and Explainable AI**
