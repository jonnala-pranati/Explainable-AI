#!/bin/bash

echo "Starting Explainable AI Lite - Frontend and Backend"
echo ""

echo "[1/2] Starting FastAPI Backend on port 8000..."
cd backend && python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

sleep 3

echo "[2/2] Starting React Frontend on port 5173..."
cd frontend && npm run dev &
FRONTEND_PID=$!

echo ""
echo "========================================"
echo "Backend: http://localhost:8000"
echo "Frontend: http://localhost:5173"
echo "API Docs: http://localhost:8000/docs"
echo "========================================"
echo ""
echo "Press Ctrl+C to stop both servers..."

# Handle Ctrl+C to stop both processes
trap "kill $BACKEND_PID $FRONTEND_PID; echo 'Servers stopped.'; exit" INT TERM

wait
