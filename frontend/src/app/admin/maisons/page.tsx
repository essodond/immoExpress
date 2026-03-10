'use client';

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
