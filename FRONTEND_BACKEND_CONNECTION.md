# Connecting React Frontend to FastAPI Backend

Complete guide to connect your React frontend with the FastAPI backend.

## 📋 Prerequisites

- Backend running on port 8000
- Frontend running on port 5173 (default Vite port)
- Both projects in the same directory

## 🚀 Step-by-Step Setup

### Step 1: Start the Backend

```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at: **http://localhost:8000**

### Step 2: Start the Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend will be available at: **http://localhost:5173**

### Step 3: Configure Environment Variables

The frontend `.env` file is already configured:

```env
VITE_API_URL=http://localhost:8000/api/v1
```

For production, create `.env.production`:

```env
VITE_API_URL=https://your-production-api.com/api/v1
```

## 🔧 CORS Configuration

CORS is already configured in the backend (`backend/app/core/config.py`):

```python
CORS_ORIGINS = ["http://localhost:3000", "http://localhost:5173"]
```

If your frontend runs on a different port, add it to this list.

## 📡 API Endpoints

The frontend now calls these real FastAPI endpoints:

### Prediction
```typescript
import { predict } from "./services/api";

const result = await predict("This movie is amazing");
// Returns: { prediction: "POSITIVE", confidence: 0.94, top_features: [...] }
```

### Explanation (SHAP)
```typescript
import { explainShap } from "./services/api";

const explanation = await explainShap("This movie is amazing");
// Returns: { explanation: [...], summary: "..." }
```

### Explanation (LIME)
```typescript
import { explainLime } from "./services/api";

const explanation = await explainLime("This movie is amazing");
// Returns: { explanation: [...], summary: "..." }
```

### Explanation (Rule-based)
```typescript
import { explainRule } from "./services/api";

const explanation = await explainRule("This movie is amazing");
// Returns: { explanation: [...], summary: "..." }
```

### Health Check
```typescript
import { checkHealth } from "./services/api";

const health = await checkHealth();
// Returns: { status: "ok" }
```

## 🎯 Using the Custom Hook

Use the `useApi` hook in your components:

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
    <div>
      <button onClick={handlePredict} disabled={loading}>
        {loading ? "Predicting..." : "Predict"}
      </button>
      {error && <p className="text-red-500">{error}</p>}
    </div>
  );
}
```

## 🔐 Authentication (Optional)

If you need authentication in the future:

### Backend Setup

Add authentication middleware in `backend/app/main.py`:

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    # Verify token logic here
    if token != "your-secret-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

# Protect endpoints
@router.post("/predict", dependencies=[Depends(verify_token)])
async def predict(request: PredictRequest):
    # ...
```

### Frontend Setup

Add API key to `.env`:

```env
VITE_API_URL=http://localhost:8000/api/v1
VITE_API_KEY=your-secret-token
```

Update `frontend/src/services/api.ts`:

```typescript
const API_KEY = import.meta.env.VITE_API_KEY;

const api = axios.create({
  baseURL: API_BASE,
  timeout: 15000,
  headers: { 
    "Content-Type": "application/json",
    ...(API_KEY && { "Authorization": `Bearer ${API_KEY}` })
  },
});
```

## 🛡️ Error Handling

The API service includes automatic error handling:

- **Network errors**: "No response from server. Check if backend is running."
- **Server errors**: Displays the error message from backend
- **Validation errors**: Shows validation messages from Pydantic

## 🧪 Testing the Connection

### Test Backend Alone

```bash
curl http://localhost:8000/api/v1/health
```

Should return: `{"status":"ok"}`

### Test Frontend Connection

1. Start both servers
2. Open browser to http://localhost:5173
3. Check browser console for any CORS errors
4. Use the API in your components

## 📝 Best Practices

### 1. Environment Variables
- Never commit `.env` files
- Use `.env.example` as template
- Different configs for dev/staging/prod

### 2. Error Handling
- Always handle errors in UI
- Show user-friendly error messages
- Log errors for debugging

### 3. Loading States
- Show loading indicators during API calls
- Disable buttons while loading
- Provide feedback to users

### 4. Type Safety
- TypeScript interfaces match backend schemas
- Keep types in sync when backend changes
- Use strict type checking

### 5. API Versioning
- Use `/api/v1` prefix for versioning
- Maintain backward compatibility
- Document breaking changes

### 6. Performance
- Use React Query or SWR for caching
- Implement request debouncing
- Optimize payload sizes

## 🔄 Syncing Frontend and Backend

### When Backend Changes:

1. **Update TypeScript interfaces** in `frontend/src/services/api.ts`
2. **Test the new endpoints** with curl or Postman
3. **Update frontend components** using the API
4. **Run tests** to ensure compatibility

### When Frontend Changes:

1. **Check API usage** in components
2. **Ensure environment variables** are correct
3. **Test with running backend**
4. **Update documentation** if needed

## 🐛 Common Issues

### CORS Errors

**Problem**: Browser shows CORS error

**Solution**:
1. Check backend CORS origins in `backend/app/core/config.py`
2. Ensure frontend port is listed
3. Restart backend after changes

### Connection Refused

**Problem**: "No response from server"

**Solution**:
1. Check if backend is running
2. Verify port (default: 8000)
3. Check firewall settings

### Type Mismatches

**Problem**: TypeScript errors with API responses

**Solution**:
1. Update TypeScript interfaces to match backend
2. Check backend response format
3. Use `any` temporarily for debugging

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [Axios Documentation](https://axios-http.com/)
- [Vite Environment Variables](https://vitejs.dev/guide/env-and-mode.html)

## ✅ Checklist

- [ ] Backend running on port 8000
- [ ] Frontend running on port 5173
- [ ] `.env` file configured in frontend
- [ ] CORS configured in backend
- [ ] API calls working in browser
- [ ] Error handling tested
- [ ] Loading states implemented
- [ ] TypeScript types match backend
