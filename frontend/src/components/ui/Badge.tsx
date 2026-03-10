import React from 'react';

type Variant = 'primary' | 'secondary' | 'success' | 'danger' | 'warning' | 'default';

const V: Record<Variant, string> = {
  primary:   'bg-primary-600 text-white',
  secondary: 'bg-slate-600 text-white',
  success:   'bg-green-500 text-white',
  danger:    'bg-red-500 text-white',
  warning:   'bg-amber-500 text-white',
  default:   'bg-slate-100 text-slate-700 dark:bg-slate-700 dark:text-slate-200',
};

export default function Badge({
  variant = 'default',
  children,
  className = '',
}: {
  variant?: Variant;
  children: React.ReactNode;
  className?: string;
}) {
  return (
    <span className={`inline-flex items-center px-2.5 py-1 rounded-full text-xs font-semibold ${V[variant]} ${className}`}>
      {children}
    </span>
  );
}
