import { useState } from "react";
import { useApi } from "../hooks/useApi";
import { PredictionResult } from "../services/api";

export function ApiExample() {
  const [text, setText] = useState("");
  const [result, setResult] = useState<PredictionResult | null>(null);
  const { predictText, loading, error } = useApi();

  const handlePredict = async () => {
    if (!text.trim()) return;
    
    const prediction = await predictText(text);
    if (prediction) {
      setResult(prediction);
    }
  };

  return (
    <div className="p-6 max-w-2xl mx-auto space-y-4">
      <h2 className="text-2xl font-bold">API Connection Test</h2>
      
      <div className="space-y-2">
        <label className="block text-sm font-medium">Enter text to analyze:</label>
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="This movie is amazing..."
          className="w-full p-3 border rounded-lg"
          rows={4}
        />
      </div>

      <button
        onClick={handlePredict}
        disabled={loading || !text.trim()}
        className="px-4 py-2 bg-blue-500 text-white rounded-lg disabled:bg-gray-300"
      >
        {loading ? "Analyzing..." : "Analyze"}
      </button>

      {error && (
        <div className="p-3 bg-red-100 border border-red-400 text-red-700 rounded">
          {error}
        </div>
      )}

      {result && (
        <div className="p-4 bg-green-100 border border-green-400 rounded-lg space-y-2">
          <h3 className="font-semibold">Prediction Result:</h3>
          <p><strong>Prediction:</strong> {result.prediction}</p>
          <p><strong>Confidence:</strong> {(result.confidence * 100).toFixed(2)}%</p>
          
          {result.top_features && result.top_features.length > 0 && (
            <div>
              <h4 className="font-semibold mt-2">Top Features:</h4>
              <ul className="list-disc list-inside space-y-1">
                {result.top_features.slice(0, 5).map((feature, index) => (
                  <li key={index}>
                    {feature.feature}: {feature.importance.toFixed(4)}
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
