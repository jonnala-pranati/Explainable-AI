import { motion } from "framer-motion";
import { Link } from "react-router-dom";
import { ArrowRight, Sparkles } from "lucide-react";
import GradientText from "@/components/ui/GradientText";

export default function HeroSection() {
  return (
    <section className="relative min-h-[90vh] flex items-center justify-center px-6 overflow-hidden">
      {/* Background blobs */}
      <div className="absolute inset-0 pointer-events-none overflow-hidden">
        <div className="absolute top-1/4 left-1/4 w-96 h-96 rounded-full bg-primary/10 blur-[128px] animate-glow-pulse" />
        <div className="absolute bottom-1/4 right-1/4 w-80 h-80 rounded-full bg-[hsl(var(--glow-secondary)/0.08)] blur-[128px] animate-glow-pulse" style={{ animationDelay: "1.5s" }} />
      </div>

      <div className="relative z-10 text-center max-w-3xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="inline-flex items-center gap-2 px-4 py-1.5 mb-8 rounded-full glass text-sm text-muted-foreground"
        >
          <Sparkles className="h-3.5 w-3.5 text-primary" />
          Understand what your AI thinks
        </motion.div>

        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.1 }}
          className="text-5xl sm:text-6xl lg:text-7xl font-extrabold tracking-tight leading-[1.1] mb-6"
        >
          AI predictions,{" "}
          <GradientText>explained</GradientText>
        </motion.h1>

        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.2 }}
          className="text-lg sm:text-xl text-muted-foreground mb-10 max-w-xl mx-auto leading-relaxed"
        >
          Analyze text sentiment and see exactly why the model made its decision — with SHAP, LIME, and rule-based explanations.
        </motion.p>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.3 }}
          className="flex flex-col sm:flex-row items-center justify-center gap-4"
        >
          <Link
            to="/analyze"
            className="group inline-flex items-center gap-2 px-8 py-3.5 rounded-xl bg-primary text-primary-foreground font-semibold text-sm transition-all duration-300 hover:scale-[1.02] glow-primary hover:shadow-[0_0_60px_-10px_hsl(var(--glow-primary)/0.5)]"
          >
            Try it now
            <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-1" />
          </Link>
          <a
            href="#features"
            className="inline-flex items-center gap-2 px-8 py-3.5 rounded-xl glass font-semibold text-sm text-muted-foreground transition-all duration-300 hover:text-foreground hover:bg-[hsl(var(--glass-bg)/0.1)]"
          >
            Learn more
          </a>
        </motion.div>
      </div>
    </section>
  );
}
