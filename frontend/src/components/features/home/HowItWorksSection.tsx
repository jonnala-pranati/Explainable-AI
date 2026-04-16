import SectionWrapper from "@/components/ui/SectionWrapper";
import GlassCard from "@/components/ui/GlassCard";
import GradientText from "@/components/ui/GradientText";

const steps = [
  { num: "01", title: "Enter Text", desc: "Paste or type any text you want to analyze for sentiment." },
  { num: "02", title: "Choose Method", desc: "Select SHAP, LIME, or Rule-based explanation approach." },
  { num: "03", title: "Get Insights", desc: "See the prediction and detailed visual explanation instantly." },
];

export default function HowItWorksSection() {
  return (
    <SectionWrapper>
      <div className="text-center mb-16">
        <h2 className="text-3xl sm:text-4xl font-bold mb-4">
          How it <GradientText>works</GradientText>
        </h2>
        <p className="text-muted-foreground max-w-lg mx-auto">Three simple steps to explainable AI.</p>
      </div>
      <div className="grid md:grid-cols-3 gap-8">
        {steps.map((s, i) => (
          <GlassCard
            key={s.num}
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: i * 0.15, duration: 0.5 }}
            className="text-center relative"
          >
            <span className="text-5xl font-black gradient-text opacity-30 absolute top-4 right-6">{s.num}</span>
            <div className="relative z-10">
              <h3 className="text-xl font-bold mb-3 mt-4">{s.title}</h3>
              <p className="text-sm text-muted-foreground leading-relaxed">{s.desc}</p>
            </div>
          </GlassCard>
        ))}
      </div>
    </SectionWrapper>
  );
}
