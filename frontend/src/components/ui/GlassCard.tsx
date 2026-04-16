import { motion, type HTMLMotionProps } from "framer-motion";
import { cn } from "@/lib/utils";

interface GlassCardProps extends HTMLMotionProps<"div"> {
  children: React.ReactNode;
  className?: string;
  hover?: boolean;
}

export default function GlassCard({ children, className, hover = true, ...props }: GlassCardProps) {
  return (
    <motion.div
      className={cn(
        "glass rounded-2xl p-6",
        hover && "transition-shadow duration-300 hover:shadow-[0_8px_32px_-8px_hsl(var(--glow-primary)/0.2)]",
        className
      )}
      whileHover={hover ? { y: -2 } : undefined}
      transition={{ duration: 0.2 }}
      {...props}
    >
      {children}
    </motion.div>
  );
}
