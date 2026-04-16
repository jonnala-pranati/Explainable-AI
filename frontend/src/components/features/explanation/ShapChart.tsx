import { motion } from "framer-motion";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell } from "recharts";
import type { ShapExplanation } from "@/services/api";

export default function ShapChart({ data }: { data: ShapExplanation }) {
  const chartData = data.features.map((f) => ({
    word: f.word,
    importance: parseFloat(f.importance.toFixed(3)),
  }));

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.2, duration: 0.5 }}
      className="glass rounded-2xl p-6"
    >
      <h3 className="text-sm font-semibold uppercase tracking-wider text-muted-foreground mb-4">
        SHAP Feature Importance
      </h3>
      <div className="w-full overflow-x-auto">
        <div className="min-w-[400px] h-[300px]">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={chartData} layout="vertical" margin={{ top: 0, right: 16, bottom: 0, left: 60 }}>
              <XAxis type="number" tick={{ fill: "hsl(215 20% 65%)", fontSize: 11 }} axisLine={false} tickLine={false} />
              <YAxis type="category" dataKey="word" tick={{ fill: "hsl(210 40% 98%)", fontSize: 12 }} axisLine={false} tickLine={false} width={55} />
              <Tooltip
                contentStyle={{
                  background: "hsl(222 47% 14%)",
                  border: "1px solid hsl(217 33% 22%)",
                  borderRadius: "12px",
                  color: "hsl(210 40% 98%)",
                  fontSize: 12,
                }}
              />
              <Bar dataKey="importance" radius={[0, 6, 6, 0]} maxBarSize={24}>
                {chartData.map((entry, i) => (
                  <Cell key={i} fill={entry.importance >= 0 ? "hsl(239 84% 67%)" : "hsl(0 84% 60%)"} fillOpacity={0.8} />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
    </motion.div>
  );
}
