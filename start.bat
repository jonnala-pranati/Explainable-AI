@echo off
echo Starting Explainable AI Lite - Frontend and Backend
echo.

echo [1/2] Starting FastAPI Backend on port 8000...
start cmd /k "cd backend && python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"

timeout /t 3 /nobreak > nul

echo [2/2] Starting React Frontend on port 5173...
start cmd /k "cd frontend && npm run dev"

echo.
echo ========================================
echo Backend: http://localhost:8000
echo Frontend: http://localhost:5173
echo API Docs: http://localhost:8000/docs
echo ========================================
echo.
echo Press any key to stop both servers...
pause > nul

echo Stopping servers...
taskkill /F /IM python.exe > nul 2>&1
taskkill /F /IM node.exe > nul 2>&1
echo Servers stopped.
