import { cn } from "@/lib/utils";

export default function SkeletonBlock({ className }: { className?: string }) {
  return (
    <div
      className={cn(
        "animate-pulse rounded-xl bg-muted/40",
        className
      )}
    />
  );
}
