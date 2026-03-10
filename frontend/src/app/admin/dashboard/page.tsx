'use client';

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
