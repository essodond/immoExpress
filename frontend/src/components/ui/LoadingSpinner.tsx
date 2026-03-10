const S = { sm: 'w-4 h-4 border-2', md: 'w-8 h-8 border-2', lg: 'w-12 h-12 border-[3px]' };

export default function LoadingSpinner({ size = 'md', className = '' }: { size?: 'sm'|'md'|'lg'; className?: string }) {
  return <div role="status" aria-label="Chargement" className={`${S[size]} border-primary-200 border-t-primary-600 rounded-full animate-spin ${className}`} />;
}

export function PageLoader() {
  return (
    <div className="flex items-center justify-center min-h-[400px]">
      <div className="text-center">
        <LoadingSpinner size="lg" className="mx-auto mb-4" />
        <p className="text-slate-500 dark:text-slate-400 text-sm">Chargement...</p>
      </div>
    </div>
  );
}
