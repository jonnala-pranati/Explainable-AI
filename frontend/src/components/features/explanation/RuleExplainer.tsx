import { motion } from "framer-motion";
import { CheckCircle2 } from "lucide-react";
import type { RuleExplanation } from "@/services/api";

export default function RuleExplainer({ data }: { data: RuleExplanation }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.2, duration: 0.5 }}
      className="glass rounded-2xl p-6"
    >
      <h3 className="text-sm font-semibold uppercase tracking-wider text-muted-foreground mb-4">
        Rule-Based Explanation
      </h3>
      <ul className="space-y-3 mb-6">
        {data.rules.map((rule, i) => (
          <motion.li
            key={i}
            initial={{ opacity: 0, x: -10 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.1 * i, duration: 0.3 }}
            className="flex items-start gap-3 text-sm"
          >
            <CheckCircle2 className="h-4 w-4 text-primary mt-0.5 shrink-0" />
            <span className="text-muted-foreground">{rule}</span>
          </motion.li>
        ))}
      </ul>
      <div className="p-4 rounded-xl bg-primary/5 border border-primary/10">
        <p className="text-sm text-foreground/80 leading-relaxed">{data.summary}</p>
      </div>
    </motion.div>
  );
}
