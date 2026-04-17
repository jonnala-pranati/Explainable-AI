import { motion } from "framer-motion";
import type { LimeExplanation } from "@/services/api";

const sentimentColors = {
  positive: "bg-emerald-500/20 text-emerald-300",
  negative: "bg-rose-500/20 text-rose-300",
  neutral: "bg-muted/30 text-muted-foreground",
};

export default function LimeHighlights({ data }: { data: LimeExplanation }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.2, duration: 0.5 }}
      className="glass rounded-2xl p-6"
    >
      <h3 className="text-sm font-semibold uppercase tracking-wider text-muted-foreground mb-4">
        LIME Text Explanation
      </h3>
      <div className="flex flex-wrap gap-1.5 leading-loose">
        {data.explanation.map((h, i) => {
          const sentiment = h.weight > 0 ? "positive" : h.weight < 0 ? "negative" : "neutral";
          return (
            <motion.span
              key={i}
              initial={{ opacity: 0, scale: 0.8 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ delay: 0.05 * i, duration: 0.3 }}
              className={`inline-block px-2 py-0.5 rounded-md text-sm font-medium ${sentimentColors[sentiment]}`}
            >
              {h.word}
            </motion.span>
          );
        })}
      </div>
      <div className="flex gap-4 mt-6 text-xs text-muted-foreground">
        <span className="flex items-center gap-1.5"><span className="w-3 h-3 rounded bg-emerald-500/30" /> Positive</span>
        <span className="flex items-center gap-1.5"><span className="w-3 h-3 rounded bg-rose-500/30" /> Negative</span>
        <span className="flex items-center gap-1.5"><span className="w-3 h-3 rounded bg-muted/40" /> Neutral</span>
      </div>
    </motion.div>
  );
}
