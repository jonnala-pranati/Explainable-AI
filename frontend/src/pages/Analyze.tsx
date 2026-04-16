import { useRef, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { AlertCircle, Search } from "lucide-react";
import { usePrediction } from "@/hooks/usePrediction";
import Navbar from "@/components/layout/Navbar";
import Footer from "@/components/layout/Footer";
import InputPanel from "@/components/features/prediction/InputPanel";
import PredictionBadge from "@/components/features/prediction/PredictionBadge";
import ResultSkeleton from "@/components/features/prediction/ResultSkeleton";
import ShapChart from "@/components/features/explanation/ShapChart";
import LimeHighlights from "@/components/features/explanation/LimeHighlights";
import RuleExplainer from "@/components/features/explanation/RuleExplainer";
import WordImportanceTable from "@/components/features/table/WordImportanceTable";

export default function Analyze() {
  const { prediction, shap, lime, rule, isLoading, error, analyze, clear } = usePrediction();
  const resultRef = useRef<HTMLDivElement>(null);
  const hasResult = prediction || isLoading || error;

  useEffect(() => {
    if (prediction && resultRef.current) {
      resultRef.current.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }, [prediction]);

  return (
    <div className="min-h-screen">
      <Navbar />
      <main className="pt-24 pb-20 px-6">
        <div className="container mx-auto max-w-[1200px]">
          <div className="text-center mb-12">
            <h1 className="text-3xl sm:text-4xl font-bold mb-3">
              <span className="gradient-text">Analyze</span> & Explain
            </h1>
            <p className="text-muted-foreground">Enter text, pick a method, and see the explanation.</p>
          </div>

          <div className="grid lg:grid-cols-2 gap-8 items-start">
            {/* Input */}
            <InputPanel onAnalyze={analyze} onClear={clear} isLoading={isLoading} />

            {/* Results */}
            <div ref={resultRef} className="flex flex-col gap-6">
              <AnimatePresence mode="wait">
                {isLoading && (
                  <motion.div key="loading" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
                    <ResultSkeleton />
                  </motion.div>
                )}

                {error && (
                  <motion.div key="error" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
                    className="glass rounded-2xl p-8 text-center"
                  >
                    <AlertCircle className="h-10 w-10 text-destructive mx-auto mb-3" />
                    <p className="text-sm text-muted-foreground">{error}</p>
                  </motion.div>
                )}

                {!hasResult && (
                  <motion.div key="empty" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
                    className="glass rounded-2xl p-12 text-center"
                  >
                    <Search className="h-10 w-10 text-muted-foreground/30 mx-auto mb-4" />
                    <p className="text-muted-foreground text-sm">Enter text and click analyze to see results here.</p>
                  </motion.div>
                )}

                {prediction && !isLoading && !error && (
                  <motion.div key="results" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
                    className="flex flex-col gap-6"
                  >
                    <PredictionBadge prediction={prediction} />
                    {shap && <ShapChart data={shap} />}
                    {lime && <LimeHighlights data={lime} />}
                    {rule && <RuleExplainer data={rule} />}
                    {shap && <WordImportanceTable features={shap.features} />}
                  </motion.div>
                )}
              </AnimatePresence>
            </div>
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
}
