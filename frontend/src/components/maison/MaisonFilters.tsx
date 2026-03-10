'use client';

import { useState } from 'react';
import { Search, RotateCcw } from 'lucide-react';
import { Filters } from '@/types';

interface Props {
  filters: Filters;
  onApply: (f: Filters) => void;
}

const VILLES = ['Douala', 'Yaounde', 'Bafoussam', 'Garoua', 'Bamenda', 'Maroua'];

export default function MaisonFilters({ filters, onApply }: Props) {
  const [local, setLocal] = useState<Filters>(filters);

  const set = (k: keyof Filters, v: string | number | undefined) =>
    setLocal((p) => ({ ...p, [k]: v }));

  const reset = () => {
    const empty: Filters = {};
    setLocal(empty);
    onApply(empty);
  };

  return (
    <aside className="bg-white dark:bg-slate-800 rounded-2xl shadow-sm border border-slate-100 dark:border-slate-700 p-6">
      <h2 className="font-bold text-lg text-slate-900 dark:text-white mb-5">Filtres</h2>

      <div className="space-y-4">
        {/* Ville */}
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1.5">
            Ville
          </label>
          <input
            type="text"
            list="villes-list"
            value={local.ville || ''}
            onChange={(e) => set('ville', e.target.value || undefined)}
            placeholder="Ex: Douala"
            className="w-full px-3 py-2 rounded-lg border border-slate-200 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white text-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
          />
          <datalist id="villes-list">
            {VILLES.map((v) => <option key={v} value={v} />)}
          </datalist>
        </div>

        {/* Type */}
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1.5">
            Type
          </label>
          <select
            value={local.type || 'tous'}
            onChange={(e) => set('type', e.target.value === 'tous' ? undefined : e.target.value)}
            className="w-full px-3 py-2 rounded-lg border border-slate-200 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white text-sm focus:outline-none focus:ring-2 focus:ring-primary-500"
          >
            <option value="tous">Tous les types</option>
            <option value="vente">A Vendre</option>
            <option value="location">A Louer</option>
          </select>
        </div>

        {/* Prix */}
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1.5">
            Prix (FCFA)
          </label>
          <div className="flex gap-2">
            <input
              type="number"
              value={local.prixMin || ''}
              onChange={(e) => set('prixMin', e.target.value ? Number(e.target.value) : undefined)}
              placeholder="Min"
              className="w-1/2 px-3 py-2 rounded-lg border border-slate-200 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white text-sm focus:outline-none focus:ring-2 focus:ring-primary-500"
            />
            <input
              type="number"
              value={local.prixMax || ''}
              onChange={(e) => set('prixMax', e.target.value ? Number(e.target.value) : undefined)}
              placeholder="Max"
              className="w-1/2 px-3 py-2 rounded-lg border border-slate-200 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white text-sm focus:outline-none focus:ring-2 focus:ring-primary-500"
            />
          </div>
        </div>

        {/* Chambres */}
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1.5">
            Chambres
          </label>
          <select
            value={local.chambres || 'tous'}
            onChange={(e) => set('chambres', e.target.value === 'tous' ? undefined : Number(e.target.value))}
            className="w-full px-3 py-2 rounded-lg border border-slate-200 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white text-sm focus:outline-none focus:ring-2 focus:ring-primary-500"
          >
            <option value="tous">Toutes</option>
            {[1,2,3,4,5].map((n) => (
              <option key={n} value={n}>{n}{n === 5 ? '+' : ''}</option>
            ))}
          </select>
        </div>

        {/* Statut */}
        <div>
          <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1.5">
            Statut
          </label>
          <select
            value={local.statut || 'tous'}
            onChange={(e) => set('statut', e.target.value === 'tous' ? undefined : e.target.value)}
            className="w-full px-3 py-2 rounded-lg border border-slate-200 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white text-sm focus:outline-none focus:ring-2 focus:ring-primary-500"
          >
            <option value="tous">Tous</option>
            <option value="disponible">Disponible</option>
            <option value="vendu">Vendu</option>
            <option value="loue">Loue</option>
          </select>
        </div>

        {/* Buttons */}
        <div className="flex gap-2 pt-2">
          <button
            onClick={() => onApply(local)}
            className="flex-1 flex items-center justify-center gap-2 bg-primary-600 hover:bg-primary-700 text-white font-medium py-2.5 rounded-xl text-sm transition-colors"
          >
            <Search className="w-4 h-4" />
            Appliquer
          </button>
          <button
            onClick={reset}
            className="px-3 py-2.5 rounded-xl border border-slate-200 dark:border-slate-600 text-slate-600 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-700 transition-colors"
            aria-label="Reinitialiser"
          >
            <RotateCcw className="w-4 h-4" />
          </button>
        </div>
      </div>
    </aside>
  );
}
