import { BarChart3, Highlighter, BookOpen, Zap, Shield, Eye } from "lucide-react";
import SectionWrapper from "@/components/ui/SectionWrapper";
import GlassCard from "@/components/ui/GlassCard";
import GradientText from "@/components/ui/GradientText";

const features = [
  { icon: BarChart3, title: "SHAP Visualizations", desc: "Feature importance charts showing each word's contribution to the prediction." },
  { icon: Highlighter, title: "LIME Highlights", desc: "Color-coded text overlays that reveal local explanations word by word." },
  { icon: BookOpen, title: "Rule-Based Explanations", desc: "Human-readable rules describing why the model reached its conclusion." },
  { icon: Zap, title: "Instant Analysis", desc: "Get predictions and explanations in seconds with a streamlined workflow." },
  { icon: Shield, title: "Transparent AI", desc: "Build trust by understanding model behavior before deploying decisions." },
  { icon: Eye, title: "Visual Clarity", desc: "Beautiful charts and highlighted text make complex ML outputs intuitive." },
];

export default function FeaturesSection() {
  return (
    <SectionWrapper id="features">
      <div className="text-center mb-16">
        <h2 className="text-3xl sm:text-4xl font-bold mb-4">
          Everything you need for <GradientText>explainability</GradientText>
        </h2>
        <p className="text-muted-foreground max-w-lg mx-auto">
          A complete toolkit to understand, visualize, and trust your AI model's decisions.
        </p>
      </div>
      <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {features.map((f, i) => (
          <GlassCard key={f.title} initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} transition={{ delay: i * 0.08, duration: 0.5 }}>
            <div className="w-10 h-10 rounded-xl bg-primary/10 flex items-center justify-center mb-4">
              <f.icon className="h-5 w-5 text-primary" />
            </div>
            <h3 className="text-lg font-semibold mb-2">{f.title}</h3>
            <p className="text-sm text-muted-foreground leading-relaxed">{f.desc}</p>
          </GlassCard>
        ))}
      </div>
    </SectionWrapper>
  );
}
