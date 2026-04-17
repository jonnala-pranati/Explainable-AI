# ✅ React + FastAPI Integration Complete

Your React frontend is now connected to the FastAPI backend!

## 📁 What Was Created/Updated

### Frontend Changes
- ✅ `.env` - API URL configuration
- ✅ `.env.example` - Template for environment variables
- ✅ `src/services/api.ts` - Real API calls to FastAPI (replaced mocks)
- ✅ `src/hooks/useApi.ts` - Custom React hook with loading/error states
- ✅ `src/components/ApiExample.tsx` - Example component demonstrating API usage
- ✅ `.gitignore` - Updated to ignore .env files

### Backend Changes
- ✅ `.gitignore` - Created to ignore .env and Python cache files
- ✅ CORS already configured for port 5173 (Vite default)

### Root Directory
- ✅ `FRONTEND_BACKEND_CONNECTION.md` - Complete integration guide
- ✅ `start.bat` - Windows script to start both servers
- ✅ `start.sh` - Unix/Mac script to start both servers

## 🚀 Quick Start

### Option 1: Using Start Scripts (Recommended)

**Windows:**
```bash
cd AI
start.bat
```

**Mac/Linux:**
```bash
cd AI
chmod +x start.sh
./start.sh
```

### Option 2: Manual Start

**Terminal 1 - Backend:**
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## 🔗 Access Points

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/api/v1/health

## 📡 API Usage Examples

### In Your React Components

```typescript
import { useApi } from "../hooks/useApi";

function MyComponent() {
  const { predictText, loading, error } = useApi();

  const handlePredict = async () => {
    const result = await predictText("This movie is amazing");
    if (result) {
      console.log("Prediction:", result.prediction);
      console.log("Confidence:", result.confidence);
    }
  };

  return (
    <button onClick={handlePredict} disabled={loading}>
      {loading ? "Loading..." : "Predict"}
    </button>
  );
}
```

### Direct API Calls

```typescript
import { predict, explainShap } from "../services/api";

// Prediction
const result = await predict("Great movie!");
// Returns: { prediction: "POSITIVE", confidence: 0.94, top_features: [...] }

// Explanation
const explanation = await explainShap("Great movie!");
// Returns: { explanation: [...], summary: "..." }
```

## 🔧 Configuration

### Frontend Environment Variables

Edit `frontend/.env`:
```env
VITE_API_URL=http://localhost:8000/api/v1
```

For production, create `frontend/.env.production`:
```env
VITE_API_URL=https://your-api.com/api/v1
```

### Backend CORS Configuration

Edit `backend/app/core/config.py` if you need different origins:
```python
CORS_ORIGINS = ["http://localhost:3000", "http://localhost:5173"]
```

## 🛡️ Error Handling

The API service includes automatic error handling:

- **Network errors**: "No response from server. Check if backend is running."
- **Server errors**: Displays backend error messages
- **Validation errors**: Shows Pydantic validation messages

Example usage:
```typescript
const { predictText, loading, error } = useApi();

if (error) {
  return <div className="error">{error}</div>;
}
```

## 🔐 Adding Authentication (Optional)

If you need authentication later:

1. **Backend**: Add JWT or API key middleware in `backend/app/main.py`
2. **Frontend**: Add `VITE_API_KEY` to `.env` and update `api.ts` headers
3. See `FRONTEND_BACKEND_CONNECTION.md` for detailed instructions

## 🧪 Testing the Connection

### Test Backend Health
```bash
curl http://localhost:8000/api/v1/health
```

Should return: `{"status":"ok"}`

### Test Prediction
```bash
curl -X POST http://localhost:8000/api/v1/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "This movie is amazing"}'
```

### Test in Browser
1. Start both servers
2. Open http://localhost:5173
3. Import and use `ApiExample` component
4. Check browser console for any errors

## 📝 Best Practices Implemented

✅ **Environment Variables**: Separated config from code  
✅ **Type Safety**: TypeScript interfaces match backend schemas  
✅ **Error Handling**: Centralized error handling in API service  
✅ **Loading States**: Custom hook manages loading/error states  
✅ **CORS Configured**: Backend allows frontend origin  
✅ **Git Safety**: .env files ignored by git  
✅ **Clean Architecture**: Separation of API service and UI logic  
✅ **Reusable Hook**: `useApi` can be used across components  

## 🐛 Troubleshooting

### CORS Errors
- Check backend CORS origins in `backend/app/core/config.py`
- Ensure frontend port (5173) is in the list
- Restart backend after changes

### Connection Refused
- Verify backend is running on port 8000
- Check firewall settings
- Ensure no other service is using port 8000

### Type Errors
- Backend response format changed? Update TypeScript interfaces in `api.ts`
- Check browser console for specific type errors
- Use `any` temporarily for debugging

### Environment Variables Not Loading
- Restart frontend after changing `.env`
- Ensure variable names start with `VITE_`
- Check that `.env` is in the frontend root directory

## 📚 Documentation

- **Integration Guide**: `FRONTEND_BACKEND_CONNECTION.md`
- **Backend README**: `backend/README.md`
- **API Docs**: http://localhost:8000/docs (when running)

## ✅ Next Steps

1. **Start both servers** using the scripts or manually
2. **Test the connection** using the health endpoint
3. **Integrate API calls** into your existing components
4. **Customize the UI** to display predictions and explanations
5. **Deploy** both frontend and backend when ready

## 🎯 Summary

Your React frontend is now fully connected to the FastAPI backend with:
- ✅ Real API calls replacing mock data
- ✅ Proper error handling and loading states
- ✅ TypeScript type safety
- ✅ Environment variable configuration
- ✅ CORS properly configured
- ✅ Example component for reference
- ✅ Custom React hook for easy API usage
- ✅ Start scripts for convenience

Everything is ready to go! Start both servers and begin building your features. 🚀
