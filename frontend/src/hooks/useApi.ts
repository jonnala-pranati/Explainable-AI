import { useState, useCallback } from "react";
import {
  predict,
  explainShap,
  explainLime,
  explainRule,
  checkHealth,
  PredictionResult,
  ShapExplanation,
  LimeExplanation,
  RuleExplanation,
  HealthStatus,
} from "../services/api";

export function useApi() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const predictText = useCallback(async (text: string): Promise<PredictionResult | null> => {
    setLoading(true);
    setError(null);
    try {
      const result = await predict(text);
      return result;
    } catch (err) {
      setError(err instanceof Error ? err.message : "Prediction failed");
      return null;
    } finally {
      setLoading(false);
    }
  }, []);

  const explainWithShap = useCallback(async (text: string): Promise<ShapExplanation | null> => {
    setLoading(true);
    setError(null);
    try {
      const result = await explainShap(text);
      return result;
    } catch (err) {
      setError(err instanceof Error ? err.message : "Explanation failed");
      return null;
    } finally {
      setLoading(false);
    }
  }, []);

  const explainWithLime = useCallback(async (text: string): Promise<LimeExplanation | null> => {
    setLoading(true);
    setError(null);
    try {
      const result = await explainLime(text);
      return result;
    } catch (err) {
      setError(err instanceof Error ? err.message : "Explanation failed");
      return null;
    } finally {
      setLoading(false);
    }
  }, []);

  const explainWithRule = useCallback(async (text: string): Promise<RuleExplanation | null> => {
    setLoading(true);
    setError(null);
    try {
      const result = await explainRule(text);
      return result;
    } catch (err) {
      setError(err instanceof Error ? err.message : "Explanation failed");
      return null;
    } finally {
      setLoading(false);
    }
  }, []);

  const checkApiHealth = useCallback(async (): Promise<HealthStatus | null> => {
    setLoading(true);
    setError(null);
    try {
      const result = await checkHealth();
      return result;
    } catch (err) {
      setError(err instanceof Error ? err.message : "Health check failed");
      return null;
    } finally {
      setLoading(false);
    }
  }, []);

  return {
    loading,
    error,
    predictText,
    explainWithShap,
    explainWithLime,
    explainWithRule,
    checkApiHealth,
  };
}
