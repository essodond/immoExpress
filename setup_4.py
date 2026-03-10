#!/usr/bin/env python3
"""ImmoExpert - Admin pages"""
import os

BASE = r'C:\Users\DELL\Documents\projet\immo\frontend'

def w(path, content):
    full = os.path.join(BASE, path.replace('/', os.sep))
    d = os.path.dirname(full)
    if d: os.makedirs(d, exist_ok=True)
    with open(full, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    print(f'  \u2713 {path}')

print('[4/4] Admin pages...')

# ─── src/app/admin/layout.tsx ───
w('src/app/admin/layout.tsx', r"""'use client';

import { useEffect, useState } from 'react';
import { useRouter, usePathname } from 'next/navigation';
import Link from 'next/link';
import { LayoutDashboard, Home, LogOut, Menu, X, ChevronRight } from 'lucide-react';
import { isAuthenticated, removeToken } from '@/lib/auth';

const sideLinks = [
  { href: '/admin/dashboard', icon: LayoutDashboard, label: 'Dashboard' },
  { href: '/admin/maisons',   icon: Home,            label: 'Biens' },
];

export default function AdminLayout({ children }: { children: React.ReactNode }) {
  const router   = useRouter();
  const pathname = usePathname();
  const [sideOpen, setSideOpen] = useState(false);
  const [ready, setReady]       = useState(false);

  useEffect(() => {
    if (pathname === '/admin/login') { setReady(true); return; }
    if (!isAuthenticated()) {
      router.replace('/admin/login');
    } else {
      setReady(true);
    }
  }, [pathname, router]);

  if (!ready) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-50 dark:bg-slate-900">
        <div className="w-8 h-8 border-2 border-primary-200 border-t-primary-600 rounded-full animate-spin" />
      </div>
    );
  }

  if (pathname === '/admin/login') return <>{children}</>;

  const logout = () => {
    removeToken();
    router.push('/admin/login');
  };

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-900 flex">
      {/* Sidebar overlay (mobile) */}
      {sideOpen && (
        <div
          className="fixed inset-0 z-40 bg-black/50 lg:hidden"
          onClick={() => setSideOpen(false)}
        />
      )}

      {/* Sidebar */}
      <aside
        className={`fixed top-0 left-0 h-full z-50 w-64 bg-white dark:bg-slate-800 border-r border-slate-100 dark:border-slate-700 flex flex-col transition-transform duration-200 lg:translate-x-0 ${
          sideOpen ? 'translate-x-0' : '-translate-x-full'
        } lg:static lg:flex`}
      >
        {/* Logo */}
        <div className="h-16 flex items-center justify-between px-5 border-b border-slate-100 dark:border-slate-700">
          <span className="font-bold text-lg text-primary-600">ImmoExpert Admin</span>
          <button className="lg:hidden p-1 text-slate-500" onClick={() => setSideOpen(false)}>
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Nav */}
        <nav className="flex-1 py-4 px-3">
          {sideLinks.map(({ href, icon: Icon, label }) => {
            const active = pathname === href || pathname.startsWith(href + '/');
            return (
              <Link
                key={href}
                href={href}
                className={`flex items-center gap-3 px-3 py-2.5 rounded-xl mb-1 text-sm font-medium transition-colors ${
                  active
                    ? 'bg-primary-50 dark:bg-primary-900/20 text-primary-700 dark:text-primary-400'
                    : 'text-slate-600 dark:text-slate-400 hover:bg-slate-50 dark:hover:bg-slate-700 hover:text-slate-900 dark:hover:text-white'
                }`}
              >
                <Icon className="w-5 h-5 flex-shrink-0" />
                {label}
                {active && <ChevronRight className="w-4 h-4 ml-auto" />}
              </Link>
            );
          })}
        </nav>

        {/* Footer */}
        <div className="p-3 border-t border-slate-100 dark:border-slate-700">
          <Link href="/" className="flex items-center gap-3 px-3 py-2 rounded-xl text-sm text-slate-500 hover:bg-slate-50 dark:hover:bg-slate-700 mb-1">
            <Home className="w-4 h-4" />
            Voir le site
          </Link>
          <button
            onClick={logout}
            className="w-full flex items-center gap-3 px-3 py-2 rounded-xl text-sm text-red-500 hover:bg-red-50 dark:hover:bg-red-900/20 transition-colors"
          >
            <LogOut className="w-4 h-4" />
            Deconnexion
          </button>
        </div>
      </aside>

      {/* Main */}
      <div className="flex-1 flex flex-col min-w-0">
        {/* Top bar */}
        <header className="h-16 bg-white dark:bg-slate-800 border-b border-slate-100 dark:border-slate-700 flex items-center px-4 lg:px-6 gap-4">
          <button
            onClick={() => setSideOpen(true)}
            className="lg:hidden p-2 text-slate-500 hover:bg-slate-100 dark:hover:bg-slate-700 rounded-lg"
            aria-label="Ouvrir le menu"
          >
            <Menu className="w-5 h-5" />
          </button>
          <h1 className="font-semibold text-slate-800 dark:text-white text-sm">
            {sideLinks.find(l => pathname === l.href || pathname.startsWith(l.href + '/'))?.label ?? 'Admin'}
          </h1>
        </header>

        <main className="flex-1 p-4 lg:p-8 overflow-auto">
          {children}
        </main>
      </div>
    </div>
  );
}
""")

# ─── src/app/admin/login/page.tsx ───
w('src/app/admin/login/page.tsx', r"""'use client';

import { useEffect } from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { useRouter } from 'next/navigation';
import toast from 'react-hot-toast';
import { Loader2, Lock, Home } from 'lucide-react';
import { login } from '@/lib/api';
import { saveToken, isAuthenticated } from '@/lib/auth';

const schema = z.object({
  email:    z.string().email('Adresse email invalide'),
  password: z.string().min(6, 'Minimum 6 caracteres'),
});
type F = z.infer<typeof schema>;

export default function LoginPage() {
  const router = useRouter();

  useEffect(() => {
    if (isAuthenticated()) router.replace('/admin/dashboard');
  }, [router]);

  const { register, handleSubmit, formState: { errors, isSubmitting } } = useForm<F>({
    resolver: zodResolver(schema),
  });

  const onSubmit = async (data: F) => {
    try {
      const res = await login(data);
      saveToken(res.token);
      toast.success(`Bienvenue, ${res.admin.nom}!`);
      router.push('/admin/dashboard');
    } catch (err: any) {
      const msg = err?.response?.data?.message || 'Email ou mot de passe incorrect.';
      toast.error(msg);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 to-blue-950 flex items-center justify-center p-4">
      <div className="w-full max-w-md">
        {/* Logo */}
        <div className="text-center mb-8">
          <div className="inline-flex items-center justify-center w-16 h-16 bg-primary-600 rounded-2xl shadow-lg mb-4">
            <Home className="w-8 h-8 text-white" />
          </div>
          <h1 className="text-2xl font-bold text-white">ImmoExpert Admin</h1>
          <p className="text-slate-400 text-sm mt-1">Connexion a votre espace administrateur</p>
        </div>

        {/* Card */}
        <div className="bg-white dark:bg-slate-800 rounded-2xl shadow-2xl p-8">
          <div className="flex items-center gap-2 mb-6">
            <Lock className="w-5 h-5 text-primary-600" />
            <h2 className="font-semibold text-slate-900 dark:text-white">Connexion</h2>
          </div>

          <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1.5">
                Adresse email
              </label>
              <input
                type="email"
                {...register('email')}
                placeholder="admin@immoexpert.cm"
                className="w-full px-4 py-3 rounded-xl border border-slate-200 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent text-sm"
                autoComplete="email"
              />
              {errors.email && <p className="text-xs text-red-500 mt-1">{errors.email.message}</p>}
            </div>

            <div>
              <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1.5">
                Mot de passe
              </label>
              <input
                type="password"
                {...register('password')}
                placeholder="••••••••"
                className="w-full px-4 py-3 rounded-xl border border-slate-200 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent text-sm"
                autoComplete="current-password"
              />
              {errors.password && <p className="text-xs text-red-500 mt-1">{errors.password.message}</p>}
            </div>

            <button
              type="submit"
              disabled={isSubmitting}
              className="w-full flex items-center justify-center gap-2 py-3 bg-primary-600 hover:bg-primary-700 disabled:opacity-60 text-white font-semibold rounded-xl transition-colors mt-2"
            >
              {isSubmitting ? <Loader2 className="w-4 h-4 animate-spin" /> : <Lock className="w-4 h-4" />}
              {isSubmitting ? 'Connexion...' : 'Se connecter'}
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
""")

# ─── src/app/admin/dashboard/page.tsx ───
w('src/app/admin/dashboard/page.tsx', r"""'use client';

import { useQuery } from '@tanstack/react-query';
import Link from 'next/link';
import { Building2, CheckCircle, TrendingUp, Home, Plus, ArrowRight, Loader2 } from 'lucide-react';
import { getMaisons } from '@/lib/api';
import { formatPrix, formatDate } from '@/lib/utils';
import { Maison } from '@/types';

export default function DashboardPage() {
  const { data: maisons = [], isLoading } = useQuery<Maison[]>({
    queryKey: ['admin-maisons'],
    queryFn: () => getMaisons(),
  });

  const stats = {
    total:       maisons.length,
    disponibles: maisons.filter((m) => m.statut === 'disponible').length,
    vendus:      maisons.filter((m) => m.statut === 'vendu').length,
    loues:       maisons.filter((m) => m.statut === 'loue').length,
  };

  const recent = [...maisons].sort((a, b) => new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime()).slice(0, 5);

  const STAT_CARDS = [
    { label: 'Total biens',   value: stats.total,       icon: Building2,    color: 'text-blue-600 bg-blue-50 dark:bg-blue-900/20' },
    { label: 'Disponibles',   value: stats.disponibles, icon: CheckCircle,  color: 'text-green-600 bg-green-50 dark:bg-green-900/20' },
    { label: 'Vendus',        value: stats.vendus,      icon: TrendingUp,   color: 'text-red-600 bg-red-50 dark:bg-red-900/20' },
    { label: 'Loues',         value: stats.loues,       icon: Home,         color: 'text-amber-600 bg-amber-50 dark:bg-amber-900/20' },
  ];

  return (
    <div>
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-2xl font-bold text-slate-900 dark:text-white">Dashboard</h1>
          <p className="text-slate-500 dark:text-slate-400 text-sm mt-1">Vue d'ensemble de votre portefeuille</p>
        </div>
        <Link
          href="/admin/maisons/nouvelle"
          className="flex items-center gap-2 px-4 py-2 bg-primary-600 hover:bg-primary-700 text-white text-sm font-medium rounded-xl transition-colors"
        >
          <Plus className="w-4 h-4" />
          Ajouter un bien
        </Link>
      </div>

      {isLoading ? (
        <div className="flex justify-center py-20"><Loader2 className="w-8 h-8 animate-spin text-primary-600" /></div>
      ) : (
        <>
          {/* Stats grid */}
          <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
            {STAT_CARDS.map(({ label, value, icon: Icon, color }) => (
              <div key={label} className="bg-white dark:bg-slate-800 rounded-2xl p-5 shadow-sm border border-slate-100 dark:border-slate-700">
                <div className={`w-10 h-10 rounded-xl flex items-center justify-center mb-3 ${color}`}>
                  <Icon className="w-5 h-5" />
                </div>
                <p className="text-2xl font-bold text-slate-900 dark:text-white">{value}</p>
                <p className="text-slate-500 dark:text-slate-400 text-sm">{label}</p>
              </div>
            ))}
          </div>

          {/* Recent biens */}
          <div className="bg-white dark:bg-slate-800 rounded-2xl shadow-sm border border-slate-100 dark:border-slate-700">
            <div className="flex items-center justify-between p-5 border-b border-slate-100 dark:border-slate-700">
              <h2 className="font-semibold text-slate-900 dark:text-white">Biens recents</h2>
              <Link href="/admin/maisons" className="text-primary-600 text-sm flex items-center gap-1 hover:underline">
                Voir tout <ArrowRight className="w-3.5 h-3.5" />
              </Link>
            </div>
            {recent.length === 0 ? (
              <p className="text-center text-slate-400 py-8 text-sm">Aucun bien pour l'instant.</p>
            ) : (
              <div className="overflow-x-auto">
                <table className="w-full text-sm">
                  <thead>
                    <tr className="border-b border-slate-100 dark:border-slate-700">
                      {['Titre', 'Ville', 'Prix', 'Type', 'Statut', 'Date'].map((h) => (
                        <th key={h} className="text-left px-5 py-3 text-xs font-medium text-slate-500 dark:text-slate-400 uppercase tracking-wider">{h}</th>
                      ))}
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-50 dark:divide-slate-700/50">
                    {recent.map((m) => (
                      <tr key={m.id} className="hover:bg-slate-50 dark:hover:bg-slate-700/30 transition-colors">
                        <td className="px-5 py-3 font-medium text-slate-900 dark:text-white max-w-[180px] truncate">{m.titre}</td>
                        <td className="px-5 py-3 text-slate-600 dark:text-slate-400">{m.ville}</td>
                        <td className="px-5 py-3 text-slate-600 dark:text-slate-400 whitespace-nowrap">{formatPrix(m.prix)}</td>
                        <td className="px-5 py-3">
                          <span className={`px-2 py-0.5 rounded-full text-xs font-medium ${m.type === 'vente' ? 'bg-blue-100 text-blue-700' : 'bg-slate-100 text-slate-700'}`}>
                            {m.type === 'vente' ? 'Vente' : 'Location'}
                          </span>
                        </td>
                        <td className="px-5 py-3">
                          <span className={`px-2 py-0.5 rounded-full text-xs font-medium ${m.statut === 'disponible' ? 'bg-green-100 text-green-700' : m.statut === 'vendu' ? 'bg-red-100 text-red-700' : 'bg-amber-100 text-amber-700'}`}>
                            {m.statut}
                          </span>
                        </td>
                        <td className="px-5 py-3 text-slate-500 whitespace-nowrap">{formatDate(m.createdAt)}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        </>
      )}
    </div>
  );
}
""")

# ─── src/app/admin/maisons/page.tsx ───
w('src/app/admin/maisons/page.tsx', r"""'use client';

import { useState } from 'react';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import Link from 'next/link';
import Image from 'next/image';
import toast from 'react-hot-toast';
import { Plus, Pencil, Trash2, Loader2, Search } from 'lucide-react';
import { getMaisons, deleteMaison } from '@/lib/api';
import { formatPrix, formatDate, getMainPhoto, getStatutLabel, getStatutColor } from '@/lib/utils';
import { Maison } from '@/types';

export default function AdminMaisonsPage() {
  const qc = useQueryClient();
  const [search, setSearch] = useState('');

  const { data: maisons = [], isLoading } = useQuery<Maison[]>({
    queryKey: ['admin-maisons'],
    queryFn: () => getMaisons(),
  });

  const filtered = maisons.filter((m) =>
    m.titre.toLowerCase().includes(search.toLowerCase()) ||
    m.ville.toLowerCase().includes(search.toLowerCase())
  );

  const handleDelete = async (m: Maison) => {
    if (!confirm(`Supprimer "${m.titre}" ? Cette action est irreversible.`)) return;
    try {
      await deleteMaison(m.id);
      qc.invalidateQueries({ queryKey: ['admin-maisons'] });
      toast.success('Bien supprime.');
    } catch {
      toast.error('Erreur lors de la suppression.');
    }
  };

  return (
    <div>
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-8">
        <div>
          <h1 className="text-2xl font-bold text-slate-900 dark:text-white">Biens immobiliers</h1>
          <p className="text-slate-500 text-sm mt-1">{maisons.length} bien(s) au total</p>
        </div>
        <Link
          href="/admin/maisons/nouvelle"
          className="flex items-center gap-2 px-5 py-2.5 bg-primary-600 hover:bg-primary-700 text-white text-sm font-semibold rounded-xl transition-colors"
        >
          <Plus className="w-4 h-4" />
          Ajouter un bien
        </Link>
      </div>

      {/* Search */}
      <div className="relative mb-6 max-w-sm">
        <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
        <input
          type="text"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          placeholder="Rechercher un bien..."
          className="w-full pl-10 pr-4 py-2.5 rounded-xl border border-slate-200 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white text-sm focus:outline-none focus:ring-2 focus:ring-primary-500"
        />
      </div>

      <div className="bg-white dark:bg-slate-800 rounded-2xl shadow-sm border border-slate-100 dark:border-slate-700 overflow-hidden">
        {isLoading ? (
          <div className="flex justify-center py-20">
            <Loader2 className="w-8 h-8 animate-spin text-primary-600" />
          </div>
        ) : filtered.length === 0 ? (
          <div className="text-center py-16">
            <p className="text-slate-400 text-sm">
              {search ? 'Aucun bien ne correspond a votre recherche.' : 'Aucun bien pour l\'instant.'}
            </p>
          </div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b border-slate-100 dark:border-slate-700 bg-slate-50 dark:bg-slate-700/50">
                  {['Photo', 'Titre', 'Ville', 'Prix', 'Type', 'Statut', 'Date', 'Actions'].map((h) => (
                    <th key={h} className="text-left px-4 py-3 text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider whitespace-nowrap">
                      {h}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-50 dark:divide-slate-700/50">
                {filtered.map((m) => (
                  <tr key={m.id} className="hover:bg-slate-50 dark:hover:bg-slate-700/30 transition-colors">
                    <td className="px-4 py-3">
                      <div className="relative w-14 h-10 rounded-lg overflow-hidden bg-slate-100 dark:bg-slate-700 flex-shrink-0">
                        <Image
                          src={getMainPhoto(m.photos)}
                          alt={m.titre}
                          fill
                          className="object-cover"
                          sizes="56px"
                          unoptimized
                        />
                      </div>
                    </td>
                    <td className="px-4 py-3 max-w-[160px]">
                      <p className="font-medium text-slate-900 dark:text-white truncate">{m.titre}</p>
                    </td>
                    <td className="px-4 py-3 text-slate-500 dark:text-slate-400 whitespace-nowrap">{m.ville}</td>
                    <td className="px-4 py-3 text-slate-700 dark:text-slate-300 whitespace-nowrap font-medium">{formatPrix(m.prix)}</td>
                    <td className="px-4 py-3">
                      <span className={`px-2 py-0.5 rounded-full text-xs font-medium whitespace-nowrap ${m.type === 'vente' ? 'bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-400' : 'bg-slate-100 text-slate-700 dark:bg-slate-700 dark:text-slate-300'}`}>
                        {m.type === 'vente' ? 'Vente' : 'Location'}
                      </span>
                    </td>
                    <td className="px-4 py-3">
                      <span className={`px-2 py-0.5 rounded-full text-xs font-medium whitespace-nowrap ${getStatutColor(m.statut)}`}>
                        {getStatutLabel(m.statut)}
                      </span>
                    </td>
                    <td className="px-4 py-3 text-slate-400 whitespace-nowrap text-xs">{formatDate(m.createdAt)}</td>
                    <td className="px-4 py-3">
                      <div className="flex items-center gap-1">
                        <Link
                          href={`/admin/maisons/${m.id}`}
                          className="p-1.5 text-slate-500 hover:text-primary-600 hover:bg-primary-50 dark:hover:bg-primary-900/20 rounded-lg transition-colors"
                          title="Modifier"
                        >
                          <Pencil className="w-4 h-4" />
                        </Link>
                        <button
                          onClick={() => handleDelete(m)}
                          className="p-1.5 text-slate-500 hover:text-red-600 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition-colors"
                          title="Supprimer"
                        >
                          <Trash2 className="w-4 h-4" />
                        </button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}
""")

# ─── src/app/admin/maisons/nouvelle/page.tsx ───
w('src/app/admin/maisons/nouvelle/page.tsx', r"""import { Metadata } from 'next';
import Link from 'next/link';
import { ArrowLeft } from 'lucide-react';
import MaisonForm from '@/components/maison/MaisonForm';

export const metadata: Metadata = { title: 'Nouveau bien' };

export default function NouvelleMaisonPage() {
  return (
    <div className="max-w-4xl">
      <div className="flex items-center gap-3 mb-8">
        <Link
          href="/admin/maisons"
          className="p-2 text-slate-500 hover:text-slate-700 dark:hover:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700 rounded-lg transition-colors"
          aria-label="Retour"
        >
          <ArrowLeft className="w-5 h-5" />
        </Link>
        <div>
          <h1 className="text-2xl font-bold text-slate-900 dark:text-white">Nouveau bien</h1>
          <p className="text-slate-500 text-sm mt-0.5">Ajoutez un nouveau bien immobilier</p>
        </div>
      </div>
      <MaisonForm />
    </div>
  );
}
""")

# ─── src/app/admin/maisons/[id]/page.tsx ───
w('src/app/admin/maisons/[id]/page.tsx', r"""import { Metadata } from 'next';
import { notFound } from 'next/navigation';
import Link from 'next/link';
import { ArrowLeft } from 'lucide-react';
import MaisonForm from '@/components/maison/MaisonForm';
import { getMaison } from '@/lib/api';

interface Props { params: { id: string } }

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  try {
    const m = await getMaison(params.id);
    return { title: `Modifier: ${m.titre}` };
  } catch {
    return { title: 'Modifier un bien' };
  }
}

export default async function EditMaisonPage({ params }: Props) {
  const maison = await getMaison(params.id).catch(() => null);
  if (!maison) notFound();

  return (
    <div className="max-w-4xl">
      <div className="flex items-center gap-3 mb-8">
        <Link
          href="/admin/maisons"
          className="p-2 text-slate-500 hover:text-slate-700 dark:hover:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700 rounded-lg transition-colors"
          aria-label="Retour"
        >
          <ArrowLeft className="w-5 h-5" />
        </Link>
        <div>
          <h1 className="text-2xl font-bold text-slate-900 dark:text-white">Modifier le bien</h1>
          <p className="text-slate-500 text-sm mt-0.5 truncate max-w-md">{maison.titre}</p>
        </div>
      </div>
      <MaisonForm maison={maison} />
    </div>
  );
}
""")

print('  Done.\n')
