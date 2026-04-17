import { motion } from "framer-motion";
import type { PredictionResult } from "@/services/api";

export default function PredictionBadge({ prediction }: { prediction: PredictionResult }) {
  const isPositive = prediction.prediction === "POSITIVE";

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.9 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ type: "spring", stiffness: 300, damping: 20 }}
      className="glass rounded-2xl p-6 text-center"
    >
      <p className="text-xs uppercase tracking-widest text-muted-foreground mb-3">Prediction</p>
      <div
        className={`inline-flex items-center gap-2 px-6 py-3 rounded-xl text-lg font-bold ${
          isPositive
            ? "bg-emerald-500/15 text-emerald-400 ring-1 ring-emerald-500/30"
            : "bg-rose-500/15 text-rose-400 ring-1 ring-rose-500/30"
        }`}
      >
        <span className={`w-2.5 h-2.5 rounded-full ${isPositive ? "bg-emerald-400" : "bg-rose-400"}`} />
        {prediction.prediction}
      </div>
      <p className="text-sm text-muted-foreground mt-3">
        Confidence: <span className="text-foreground font-medium">{(prediction.confidence * 100).toFixed(1)}%</span>
      </p>
    </motion.div>
  );
}
