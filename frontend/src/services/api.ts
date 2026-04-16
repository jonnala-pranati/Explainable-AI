import axios from "axios";

const API_BASE = import.meta.env.VITE_API_URL || "https://api.example.com";

const api = axios.create({
  baseURL: API_BASE,
  timeout: 15000,
  headers: { "Content-Type": "application/json" },
});

export interface PredictionResult {
  label: "Positive" | "Negative";
  confidence: number;
}

export interface ShapExplanation {
  features: { word: string; importance: number }[];
}

export interface LimeExplanation {
  highlights: { word: string; weight: number; sentiment: "positive" | "negative" | "neutral" }[];
}

export interface RuleExplanation {
  rules: string[];
  summary: string;
}

// Mock implementations for demo
const delay = (ms: number) => new Promise((r) => setTimeout(r, ms));

const mockWords = (text: string) =>
  text.split(/\s+/).filter((w) => w.length > 2).slice(0, 12);

export async function predict(text: string): Promise<PredictionResult> {
  await delay(1200);
  const positive = /good|great|love|amazing|excellent|happy|wonderful|best|fantastic/i.test(text);
  return {
    label: positive ? "Positive" : "Negative",
    confidence: 0.78 + Math.random() * 0.2,
  };
}

export async function explainShap(text: string): Promise<ShapExplanation> {
  await delay(800);
  const words = mockWords(text);
  return {
    features: words.map((word) => ({
      word,
      importance: (Math.random() - 0.3) * 0.8,
    })).sort((a, b) => Math.abs(b.importance) - Math.abs(a.importance)),
  };
}

export async function explainLime(text: string): Promise<LimeExplanation> {
  await delay(800);
  return {
    highlights: text.split(/\s+/).map((word) => {
      const r = Math.random();
      return {
        word,
        weight: (Math.random() - 0.4) * 1,
        sentiment: r > 0.6 ? "positive" : r > 0.3 ? "negative" : "neutral",
      };
    }),
  };
}

export async function explainRule(text: string): Promise<RuleExplanation> {
  await delay(600);
  const hasPositive = /good|great|love|amazing/i.test(text);
  return {
    rules: [
      hasPositive
        ? "Contains positive sentiment keywords (good, great, love, amazing)"
        : "Lacks strong positive sentiment indicators",
      `Text length: ${text.length} characters — ${text.length > 50 ? "sufficient" : "short"} context`,
      "Negation patterns: none detected",
      "Overall tone assessment: " + (hasPositive ? "favorable" : "unfavorable"),
    ],
    summary: hasPositive
      ? "The model identified positive sentiment markers contributing to a favorable classification."
      : "The model found insufficient positive indicators, leading to a negative classification.",
  };
}
