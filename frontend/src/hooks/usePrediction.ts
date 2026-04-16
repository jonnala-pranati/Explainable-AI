import { useState, useCallback } from "react";
import {
  predict,
  explainShap,
  explainLime,
  explainRule,
  type PredictionResult,
  type ShapExplanation,
  type LimeExplanation,
  type RuleExplanation,
} from "@/services/api";

export type ExplanationType = "shap" | "lime" | "rule";

interface PredictionState {
  prediction: PredictionResult | null;
  shap: ShapExplanation | null;
  lime: LimeExplanation | null;
  rule: RuleExplanation | null;
  isLoading: boolean;
  error: string | null;
}

export function usePrediction() {
  const [state, setState] = useState<PredictionState>({
    prediction: null,
    shap: null,
    lime: null,
    rule: null,
    isLoading: false,
    error: null,
  });

  const analyze = useCallback(async (text: string, method: ExplanationType) => {
    setState((s) => ({ ...s, isLoading: true, error: null }));
    try {
      const [predResult, explanation] = await Promise.all([
        predict(text),
        method === "shap"
          ? explainShap(text)
          : method === "lime"
          ? explainLime(text)
          : explainRule(text),
      ]);

      setState({
        prediction: predResult,
        shap: method === "shap" ? (explanation as ShapExplanation) : null,
        lime: method === "lime" ? (explanation as LimeExplanation) : null,
        rule: method === "rule" ? (explanation as RuleExplanation) : null,
        isLoading: false,
        error: null,
      });
    } catch {
      setState((s) => ({
        ...s,
        isLoading: false,
        error: "Analysis failed. Please try again.",
      }));
    }
  }, []);

  const clear = useCallback(() => {
    setState({
      prediction: null,
      shap: null,
      lime: null,
      rule: null,
      isLoading: false,
      error: null,
    });
  }, []);

  return { ...state, analyze, clear };
}
