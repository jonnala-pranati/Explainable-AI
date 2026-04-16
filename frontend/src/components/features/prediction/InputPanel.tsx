import { useState, useRef } from "react";
import { motion } from "framer-motion";
import { Sparkles, Trash2 } from "lucide-react";
import type { ExplanationType } from "@/hooks/usePrediction";

const sampleTexts = [
  "This product is absolutely amazing! Best purchase I've ever made.",
  "Terrible experience. The service was slow and the food was cold.",
  "It's okay, nothing special. Average quality for the price.",
];

interface InputPanelProps {
  onAnalyze: (text: string, method: ExplanationType) => void;
  onClear: () => void;
  isLoading: boolean;
}

export default function InputPanel({ onAnalyze, onClear, isLoading }: InputPanelProps) {
  const [text, setText] = useState("");
  const [method, setMethod] = useState<ExplanationType>("shap");
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  const handleSubmit = () => {
    if (!text.trim()) return;
    onAnalyze(text.trim(), method);
  };

  const handleClear = () => {
    setText("");
    onClear();
    textareaRef.current?.focus();
  };

  return (
    <div className="glass rounded-2xl p-6 flex flex-col gap-6 h-full">
      <div>
        <label className="block text-sm font-medium mb-2">Your Text</label>
        <textarea
          ref={textareaRef}
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter text to analyze sentiment..."
          rows={6}
          className="w-full rounded-xl bg-background/50 border border-border/50 px-4 py-3 text-sm placeholder:text-muted-foreground/50 focus:outline-none focus:ring-2 focus:ring-primary/40 focus:border-primary/40 transition-all duration-300 resize-none"
        />
      </div>

      <div>
        <label className="block text-sm font-medium mb-2">Explanation Method</label>
        <div className="flex gap-2">
          {(["shap", "lime", "rule"] as ExplanationType[]).map((m) => (
            <button
              key={m}
              onClick={() => setMethod(m)}
              className={`flex-1 px-4 py-2.5 rounded-xl text-sm font-medium transition-all duration-200 ${
                method === m
                  ? "bg-primary/20 text-foreground ring-1 ring-primary/40"
                  : "bg-background/30 text-muted-foreground hover:text-foreground hover:bg-background/50"
              }`}
            >
              {m.toUpperCase()}
            </button>
          ))}
        </div>
      </div>

      <div className="flex gap-3">
        <motion.button
          whileHover={{ scale: 1.02 }}
          whileTap={{ scale: 0.98 }}
          onClick={handleSubmit}
          disabled={!text.trim() || isLoading}
          className="flex-1 inline-flex items-center justify-center gap-2 px-6 py-3 rounded-xl bg-primary text-primary-foreground font-semibold text-sm transition-all duration-300 glow-sm disabled:opacity-40 disabled:cursor-not-allowed disabled:shadow-none"
        >
          <Sparkles className="h-4 w-4" />
          {isLoading ? "Analyzing…" : "Analyze & Explain"}
        </motion.button>
        <motion.button
          whileHover={{ scale: 1.02 }}
          whileTap={{ scale: 0.98 }}
          onClick={handleClear}
          className="px-4 py-3 rounded-xl glass text-muted-foreground hover:text-foreground transition-colors text-sm"
        >
          <Trash2 className="h-4 w-4" />
        </motion.button>
      </div>

      <div>
        <p className="text-xs text-muted-foreground mb-2">Try a sample:</p>
        <div className="flex flex-col gap-2">
          {sampleTexts.map((s, i) => (
            <button
              key={i}
              onClick={() => setText(s)}
              className="text-left text-xs px-3 py-2 rounded-lg bg-background/30 text-muted-foreground hover:text-foreground hover:bg-background/50 transition-all duration-200 truncate"
            >
              {s}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}
