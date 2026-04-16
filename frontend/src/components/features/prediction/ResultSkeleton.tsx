import SkeletonBlock from "@/components/ui/SkeletonBlock";

export default function ResultSkeleton() {
  return (
    <div className="flex flex-col gap-6">
      <div className="glass rounded-2xl p-6">
        <SkeletonBlock className="h-4 w-24 mx-auto mb-4" />
        <SkeletonBlock className="h-12 w-40 mx-auto mb-3" />
        <SkeletonBlock className="h-3 w-32 mx-auto" />
      </div>
      <div className="glass rounded-2xl p-6">
        <SkeletonBlock className="h-4 w-48 mb-4" />
        <SkeletonBlock className="h-[200px] w-full" />
      </div>
      <div className="glass rounded-2xl p-6">
        <SkeletonBlock className="h-4 w-36 mb-4" />
        <div className="space-y-2">
          <SkeletonBlock className="h-8 w-full" />
          <SkeletonBlock className="h-8 w-full" />
          <SkeletonBlock className="h-8 w-full" />
        </div>
      </div>
    </div>
  );
}
