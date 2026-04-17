import axios from "axios";

const API_BASE = import.meta.env.VITE_API_URL || "http://localhost:8000/api/v1";

const api = axios.create({
  baseURL: API_BASE,
  timeout: 15000,
  headers: { "Content-Type": "application/json" },
});

// Request interceptor for error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error("API Error:", error);
    if (error.response) {
      // Server responded with error status
      throw new Error(error.response.data?.detail || error.response.statusText);
    } else if (error.request) {
      // Request made but no response
      throw new Error("No response from server. Check if backend is running.");
    } else {
      // Error setting up request
      throw new Error(error.message || "Request failed");
    }
  }
);

// TypeScript interfaces matching FastAPI backend schemas
export interface PredictionResult {
  prediction: string;
  confidence: number;
  top_features: { feature: string; importance: number }[];
}

export interface ExplanationFeature {
  feature: string;
  value: number;
  contribution: "positive" | "negative";
}

export interface ShapExplanation {
  explanation: ExplanationFeature[];
  summary: string;
}

export interface LimeExplanation {
  explanation: { word: string; weight: number; position: number }[];
  summary: string;
}

export interface RuleExplanation {
  explanation: { rule: string; confidence: number; support: string }[];
  summary: string;
}

export interface HealthStatus {
  status: string;
}

// API Functions

export async function predict(text: string): Promise<PredictionResult> {
  const response = await api.post<PredictionResult>("/predict", { text });
  return response.data;
}

export async function explainShap(text: string): Promise<ShapExplanation> {
  const response = await api.post<ShapExplanation>("/explain", {
    text,
    method: "shap",
  });
  return response.data;
}

export async function explainLime(text: string): Promise<LimeExplanation> {
  const response = await api.post<LimeExplanation>("/explain", {
    text,
    method: "lime",
  });
  return response.data;
}

export async function explainRule(text: string): Promise<RuleExplanation> {
  const response = await api.post<RuleExplanation>("/explain", {
    text,
    method: "rule",
  });
  return response.data;
}

export async function checkHealth(): Promise<HealthStatus> {
  const response = await api.get<HealthStatus>("/health");
  return response.data;
}
