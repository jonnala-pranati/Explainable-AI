import { motion } from "framer-motion";
import type { ExplanationFeature } from "@/services/api";

export default function WordImportanceTable({ features }: { features: ExplanationFeature[] }) {
  if (!features || !features.length) return null;

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.3, duration: 0.5 }}
      className="glass rounded-2xl p-6"
    >
      <h3 className="text-sm font-semibold uppercase tracking-wider text-muted-foreground mb-4">
        Word Importance
      </h3>
      <div className="overflow-x-auto">
        <table className="w-full text-sm">
          <thead>
            <tr className="border-b border-border/30">
              <th className="text-left py-2 font-medium text-muted-foreground">Word</th>
              <th className="text-right py-2 font-medium text-muted-foreground">Score</th>
              <th className="text-left py-2 pl-4 font-medium text-muted-foreground">Impact</th>
            </tr>
          </thead>
          <tbody>
            {features.slice(0, 8).map((f, i) => (
              <tr key={i} className="border-b border-border/10">
                <td className="py-2.5 font-medium">{f.feature}</td>
                <td className="py-2.5 text-right font-mono text-xs">{f.value.toFixed(4)}</td>
                <td className="py-2.5 pl-4">
                  <div className="flex items-center gap-2">
                    <div className="w-20 h-1.5 bg-background/50 rounded-full overflow-hidden">
                      <div
                        className={`h-full rounded-full ${f.value >= 0 ? "bg-primary" : "bg-destructive"}`}
                        style={{ width: `${Math.min(Math.abs(f.value) * 200, 100)}%` }}
                      />
                    </div>
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </motion.div>
  );
}
