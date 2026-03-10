'use client';

import { useState, useCallback } from 'react';
import { useQuery } from '@tanstack/react-query';
import { SlidersHorizontal, X } from 'lucide-react';
import MaisonCard from '@/components/maison/MaisonCard';
import MaisonFilters from '@/components/maison/MaisonFilters';
import { PageLoader } from '@/components/ui/LoadingSpinner';
import { getMaisons } from '@/lib/api';
import { Filters, Maison } from '@/types';

export default function CataloguePage() {
  const [filters, setFilters] = useState<Filters>({});
  const [showMobileFilters, setShowMobileFilters] = useState(false);

  const { data, isLoading, isError } = useQuery<Maison[]>({
    queryKey: ['maisons', filters],
    queryFn: () => getMaisons(filters),
  });

  const handleApply = useCallback((f: Filters) => {
    setFilters(f);
    setShowMobileFilters(false);
  }, []);

  const activeFilterCount = Object.values(filters).filter(Boolean).length;

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-900 pt-20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">

        {/* Header */}
        <div className="flex items-center justify-between mb-8">
          <div>
            <h1 className="text-3xl font-bold text-slate-900 dark:text-white">Catalogue</h1>
            {!isLoading && (
              <p className="text-slate-500 dark:text-slate-400 mt-1 text-sm">
                {data?.length ?? 0} bien{(data?.length ?? 0) !== 1 ? 's' : ''} trouve{(data?.length ?? 0) !== 1 ? 's' : ''}
              </p>
            )}
          </div>

          {/* Mobile filter toggle */}
          <button
            onClick={() => setShowMobileFilters(true)}
            className="lg:hidden flex items-center gap-2 px-4 py-2 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl text-sm font-medium text-slate-700 dark:text-slate-300 shadow-sm"
          >
            <SlidersHorizontal className="w-4 h-4" />
            Filtres
            {activeFilterCount > 0 && (
              <span className="bg-primary-600 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center">
                {activeFilterCount}
              </span>
            )}
          </button>
        </div>

        <div className="flex gap-8">
          {/* Sidebar filters (desktop) */}
          <aside className="hidden lg:block w-72 flex-shrink-0">
            <div className="sticky top-24">
              <MaisonFilters filters={filters} onApply={handleApply} />
            </div>
          </aside>

          {/* Results */}
          <div className="flex-1">
            {isLoading && <PageLoader />}

            {isError && (
              <div className="text-center py-16">
                <p className="text-red-500 font-medium mb-2">Erreur de chargement</p>
                <p className="text-slate-400 text-sm">Impossible de charger les biens. Verifiez votre connexion.</p>
              </div>
            )}

            {!isLoading && !isError && data && (
              data.length > 0 ? (
                <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
                  {data.map((m) => <MaisonCard key={m.id} maison={m} />)}
                </div>
              ) : (
                <div className="text-center py-20">
                  <SlidersHorizontal className="w-12 h-12 text-slate-300 mx-auto mb-3" />
                  <p className="text-slate-500 font-medium">Aucun bien ne correspond a vos filtres.</p>
                  <button
                    onClick={() => setFilters({})}
                    className="mt-4 text-primary-600 hover:underline text-sm"
                  >
                    Reinitialiser les filtres
                  </button>
                </div>
              )
            )}
          </div>
        </div>
      </div>

      {/* Mobile filters drawer */}
      {showMobileFilters && (
        <div className="fixed inset-0 z-50 lg:hidden">
          <div className="absolute inset-0 bg-black/50" onClick={() => setShowMobileFilters(false)} />
          <div className="absolute right-0 top-0 bottom-0 w-80 bg-white dark:bg-slate-900 overflow-y-auto shadow-2xl">
            <div className="flex items-center justify-between p-4 border-b border-slate-100 dark:border-slate-800">
              <h2 className="font-semibold text-slate-900 dark:text-white">Filtres</h2>
              <button onClick={() => setShowMobileFilters(false)} className="p-1 text-slate-500">
                <X className="w-5 h-5" />
              </button>
            </div>
            <div className="p-4">
              <MaisonFilters filters={filters} onApply={handleApply} />
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
