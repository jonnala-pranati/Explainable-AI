import { Brain } from "lucide-react";

export default function Footer() {
  return (
    <footer className="border-t border-border/50 py-12">
      <div className="container mx-auto px-6 flex flex-col md:flex-row items-center justify-between gap-4">
        <div className="flex items-center gap-2">
          <Brain className="h-5 w-5 text-primary" />
          <span className="text-sm font-semibold">XAI Lite</span>
        </div>
        <p className="text-sm text-muted-foreground">
          © {new Date().getFullYear()} Explainable AI Lite. Built for transparency.
        </p>
      </div>
    </footer>
  );
}
