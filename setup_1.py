#!/usr/bin/env python3
"""ImmoExpert - Config, types, lib, providers, UI components"""
import os

BASE = r'C:\Users\DELL\Documents\projet\immo\frontend'

def w(path, content):
    full = os.path.join(BASE, path.replace('/', os.sep))
    d = os.path.dirname(full)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(full, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    print(f'  \u2713 {path}')

print('\n[1/4] Config, types, lib, providers, UI...')

# ─── package.json ───
w('package.json', """{
  "name": "immo-frontend",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "next": "14.2.0",
    "react": "^18",
    "react-dom": "^18",
    "axios": "^1.6.7",
    "@tanstack/react-query": "^5.24.1",
    "next-themes": "^0.2.1",
    "swiper": "^11.0.7",
    "react-hot-toast": "^2.4.1",
    "react-hook-form": "^7.51.0",
    "@hookform/resolvers": "^3.3.4",
    "zod": "^3.22.4",
    "lucide-react": "^0.344.0"
  },
  "devDependencies": {
    "typescript": "^5",
    "@types/node": "^20",
    "@types/react": "^18",
    "@types/react-dom": "^18",
    "autoprefixer": "^10.0.1",
    "postcss": "^8",
    "tailwindcss": "^3.3.0",
    "eslint": "^8",
    "eslint-config-next": "14.2.0"
  }
}
""")

# ─── next.config.js ───
w('next.config.js', r"""/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [
      { protocol: 'https', hostname: 'res.cloudinary.com' },
      { protocol: 'https', hostname: 'images.unsplash.com' },
    ],
  },
};
module.exports = nextConfig;
""")

# ─── tailwind.config.ts ───
w('tailwind.config.ts', r"""import type { Config } from 'tailwindcss';

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: {
          50:  '#eff6ff',
          100: '#dbeafe',
          200: '#bfdbfe',
          300: '#93c5fd',
          400: '#60a5fa',
          500: '#3b82f6',
          600: '#2563eb',
          700: '#1d4ed8',
          800: '#1e40af',
          900: '#1e3a8a',
          950: '#172554',
        },
      },
    },
  },
  plugins: [],
};
export default config;
""")

# ─── tsconfig.json ───
w('tsconfig.json', """{
  "compilerOptions": {
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [{ "name": "next" }],
    "paths": { "@/*": ["./src/*"] }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
""")

# ─── postcss.config.js ───
w('postcss.config.js', r"""module.exports = {
  plugins: { tailwindcss: {}, autoprefixer: {} },
};
""")

# ─── .env.local.example ───
w('.env.local.example', r"""NEXT_PUBLIC_API_URL=http://localhost:5000/api
NEXT_PUBLIC_WHATSAPP_NUMBER=+237600000000
""")

# ─── .eslintrc.json ───
w('.eslintrc.json', """{ "extends": "next/core-web-vitals" }
""")

# ─── src/app/globals.css ───
w('src/app/globals.css', r"""@tailwind base;
@tailwind components;
@tailwind utilities;

html {
  scroll-behavior: smooth;
}

body {
  @apply antialiased;
}

/* Swiper overrides */
.swiper-button-next,
.swiper-button-prev {
  color: white !important;
  background: rgba(0,0,0,0.4);
  border-radius: 50%;
  width: 36px !important;
  height: 36px !important;
}
.swiper-button-next::after,
.swiper-button-prev::after {
  font-size: 14px !important;
}
.swiper-pagination-bullet-active {
  background: #2563eb !important;
}

/* Custom scrollbar */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #94a3b8; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #64748b; }
""")

# ─── src/types/index.ts ───
w('src/types/index.ts', r"""export interface Photo {
  id: string;
  url: string;
  publicId: string;
  isMain: boolean;
  maisonId: string;
  createdAt: string;
}

export interface Maison {
  id: string;
  titre: string;
  description: string;
  prix: number;
  type: 'vente' | 'location';
  ville: string;
  quartier: string;
  chambres: number;
  sallesBain: number;
  superficie: number;
  statut: 'disponible' | 'vendu' | 'loue';
  videoUrl?: string | null;
  photos: Photo[];
  createdAt: string;
  updatedAt: string;
}

export interface Filters {
  ville?: string;
  type?: string;
  prixMin?: number;
  prixMax?: number;
  chambres?: number;
  statut?: string;
}

export interface Admin {
  id: string;
  email: string;
  nom: string;
}

export interface LoginCredentials {
  email: string;
  password: string;
}

export interface AuthResponse {
  token: string;
  admin: Admin;
}
""")

# ─── src/lib/auth.ts ───
w('src/lib/auth.ts', r"""const TOKEN_KEY = 'immo_admin_token';

export const saveToken = (token: string): void => {
  if (typeof window !== 'undefined') localStorage.setItem(TOKEN_KEY, token);
};

export const getToken = (): string | null => {
  if (typeof window !== 'undefined') return localStorage.getItem(TOKEN_KEY);
  return null;
};

export const removeToken = (): void => {
  if (typeof window !== 'undefined') localStorage.removeItem(TOKEN_KEY);
};

export const isAuthenticated = (): boolean => !!getToken();
""")

# ─── src/lib/utils.ts ───
w('src/lib/utils.ts', r"""import { Photo } from '@/types';

export const formatPrix = (prix: number): string =>
  new Intl.NumberFormat('fr-FR').format(prix) + ' FCFA';

export const getMainPhoto = (photos: Photo[]): string => {
  if (!photos || photos.length === 0)
    return 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=800&q=80';
  const main = photos.find((p) => p.isMain);
  return main ? main.url : photos[0].url;
};

export const getStatutColor = (statut: string): string => {
  switch (statut) {
    case 'disponible': return 'bg-green-100 text-green-800 dark:bg-green-900/30 dark:text-green-400';
    case 'vendu':      return 'bg-red-100 text-red-800 dark:bg-red-900/30 dark:text-red-400';
    case 'loue':       return 'bg-amber-100 text-amber-800 dark:bg-amber-900/30 dark:text-amber-400';
    default:           return 'bg-slate-100 text-slate-700 dark:bg-slate-700 dark:text-slate-300';
  }
};

export const getStatutLabel = (statut: string): string => {
  switch (statut) {
    case 'disponible': return 'Disponible';
    case 'vendu':      return 'Vendu';
    case 'loue':       return 'Loue';
    default:           return statut;
  }
};

export const getTypeLabel = (type: string): string => {
  switch (type) {
    case 'vente':    return 'A Vendre';
    case 'location': return 'A Louer';
    default:         return type;
  }
};

export const formatDate = (date: string): string =>
  new Intl.DateTimeFormat('fr-FR', {
    day: '2-digit', month: 'long', year: 'numeric',
  }).format(new Date(date));

export const cn = (...classes: (string | undefined | null | false)[]): string =>
  classes.filter(Boolean).join(' ');
""")

# ─── src/lib/api.ts ───
w('src/lib/api.ts', r"""import axios from 'axios';
import { Maison, Filters, AuthResponse, LoginCredentials, Admin } from '@/types';
import { getToken } from './auth';

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:5000/api',
  headers: { 'Content-Type': 'application/json' },
});

api.interceptors.request.use((config) => {
  const token = getToken();
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

api.interceptors.response.use(
  (res) => res,
  (err) => {
    if (
      err.response?.status === 401 &&
      typeof window !== 'undefined' &&
      window.location.pathname.startsWith('/admin') &&
      window.location.pathname !== '/admin/login'
    ) {
      window.location.href = '/admin/login';
    }
    return Promise.reject(err);
  }
);

export const getMaisons = async (filters?: Filters): Promise<Maison[]> => {
  const p = new URLSearchParams();
  if (filters?.ville)                     p.set('ville', filters.ville);
  if (filters?.type && filters.type !== 'tous') p.set('type', filters.type);
  if (filters?.prixMin)                   p.set('prixMin', String(filters.prixMin));
  if (filters?.prixMax)                   p.set('prixMax', String(filters.prixMax));
  if (filters?.chambres)                  p.set('chambres', String(filters.chambres));
  if (filters?.statut && filters.statut !== 'tous') p.set('statut', filters.statut);
  const { data } = await api.get<Maison[]>(`/maisons?${p.toString()}`);
  return data;
};

export const getMaisonsFeatured = async (): Promise<Maison[]> => {
  const { data } = await api.get<Maison[]>('/maisons/featured');
  return data;
};

export const getMaison = async (id: string): Promise<Maison> => {
  const { data } = await api.get<Maison>(`/maisons/${id}`);
  return data;
};

export const createMaison = async (d: Partial<Maison>): Promise<Maison> => {
  const { data } = await api.post<Maison>('/maisons', d);
  return data;
};

export const updateMaison = async (id: string, d: Partial<Maison>): Promise<Maison> => {
  const { data } = await api.put<Maison>(`/maisons/${id}`, d);
  return data;
};

export const deleteMaison = async (id: string): Promise<void> => {
  await api.delete(`/maisons/${id}`);
};

export const uploadPhotos = async (maisonId: string, files: FileList): Promise<void> => {
  const form = new FormData();
  Array.from(files).forEach((f) => form.append('photos', f));
  await api.post(`/upload/photos/${maisonId}`, form, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
};

export const deletePhoto  = async (id: string): Promise<void> => { await api.delete(`/upload/photos/${id}`); };
export const setMainPhoto = async (id: string): Promise<void> => { await api.put(`/upload/photos/${id}/main`); };

export const login = async (creds: LoginCredentials): Promise<AuthResponse> => {
  const { data } = await api.post<AuthResponse>('/auth/login', creds);
  return data;
};

export const getMe = async (): Promise<{ admin: Admin }> => {
  const { data } = await api.get('/auth/me');
  return data;
};

export default api;
""")

# ─── src/providers/Providers.tsx ───
w('src/providers/Providers.tsx', r"""'use client';

import { ThemeProvider } from 'next-themes';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { Toaster } from 'react-hot-toast';
import { useState } from 'react';

export default function Providers({ children }: { children: React.ReactNode }) {
  const [qc] = useState(
    () => new QueryClient({ defaultOptions: { queries: { staleTime: 60_000, retry: 1 } } })
  );
  return (
    <ThemeProvider attribute="class" defaultTheme="light" enableSystem>
      <QueryClientProvider client={qc}>
        {children}
        <Toaster position="top-right" toastOptions={{ duration: 4000 }} />
      </QueryClientProvider>
    </ThemeProvider>
  );
}
""")

# ─── src/components/ui/Badge.tsx ───
w('src/components/ui/Badge.tsx', r"""import React from 'react';

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
""")

# ─── src/components/ui/LoadingSpinner.tsx ───
w('src/components/ui/LoadingSpinner.tsx', r"""const S = { sm: 'w-4 h-4 border-2', md: 'w-8 h-8 border-2', lg: 'w-12 h-12 border-[3px]' };

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
""")

# ─── src/components/ui/ThemeToggle.tsx ───
w('src/components/ui/ThemeToggle.tsx', r"""'use client';

import { useTheme } from 'next-themes';
import { Sun, Moon } from 'lucide-react';
import { useEffect, useState } from 'react';

export default function ThemeToggle() {
  const { theme, setTheme } = useTheme();
  const [m, setM] = useState(false);
  useEffect(() => setM(true), []);
  if (!m) return <div className="w-9 h-9" />;
  return (
    <button
      onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
      className="p-2 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700 transition-colors"
      aria-label="Basculer le theme"
    >
      {theme === 'dark' ? <Sun className="w-5 h-5" /> : <Moon className="w-5 h-5" />}
    </button>
  );
}
""")

# ─── src/components/ui/WhatsAppButton.tsx ───
w('src/components/ui/WhatsAppButton.tsx', r"""import { MessageCircle } from 'lucide-react';

interface P {
  message?: string;
  label?: string;
  className?: string;
  size?: 'sm' | 'md' | 'lg';
}

const SZ = { sm: 'px-3 py-1.5 text-sm gap-1.5', md: 'px-5 py-2.5 text-base gap-2', lg: 'px-8 py-4 text-lg gap-2.5' };
const IC = { sm: 'w-4 h-4', md: 'w-5 h-5', lg: 'w-6 h-6' };

export default function WhatsAppButton({
  message = "Bonjour, je suis interesse(e) par vos services immobiliers.",
  label = "Contacter sur WhatsApp",
  className = '',
  size = 'md',
}: P) {
  const num = (process.env.NEXT_PUBLIC_WHATSAPP_NUMBER || '+237600000000').replace(/\D/g, '');
  const url = `https://wa.me/${num}?text=${encodeURIComponent(message)}`;
  return (
    <a
      href={url}
      target="_blank"
      rel="noopener noreferrer"
      aria-label={label}
      className={`inline-flex items-center font-semibold bg-green-500 hover:bg-green-600 active:bg-green-700 text-white rounded-xl transition-colors duration-200 ${SZ[size]} ${className}`}
    >
      <MessageCircle className={`flex-shrink-0 ${IC[size]}`} />
      {label}
    </a>
  );
}
""")

print('  Done.\n')
