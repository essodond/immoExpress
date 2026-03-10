#!/usr/bin/env python3
"""ImmoExpert - Public pages (root layout, homepage, catalogue, detail, a-propos)"""
import os

BASE = r'C:\Users\DELL\Documents\projet\immo\frontend'

def w(path, content):
    full = os.path.join(BASE, path.replace('/', os.sep))
    d = os.path.dirname(full)
    if d: os.makedirs(d, exist_ok=True)
    with open(full, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    print(f'  \u2713 {path}')

print('[3/4] Public pages...')

# ─── src/app/layout.tsx ───
w('src/app/layout.tsx', r"""import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';
import Providers from '@/providers/Providers';
import Navbar from '@/components/layout/Navbar';
import Footer from '@/components/layout/Footer';

const inter = Inter({ subsets: ['latin'], variable: '--font-inter' });

export const metadata: Metadata = {
  title: { default: 'ImmoExpert - Votre Expert Immobilier', template: '%s | ImmoExpert' },
  description: 'Trouvez votre bien immobilier ideal avec ImmoExpert. Vente et location de maisons et appartements.',
  keywords: ['immobilier', 'vente', 'location', 'maison', 'appartement', 'Cameroun'],
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="fr" suppressHydrationWarning className={inter.variable}>
      <body className="font-sans bg-white dark:bg-slate-900 text-slate-900 dark:text-white transition-colors duration-200">
        <Providers>
          <Navbar />
          <main>{children}</main>
          <Footer />
        </Providers>
      </body>
    </html>
  );
}
""")

# ─── src/app/page.tsx ───
w('src/app/page.tsx', r"""import Link from 'next/link';
import { Building2, MapPin, Users, ArrowRight } from 'lucide-react';
import MaisonCard from '@/components/maison/MaisonCard';
import WhatsAppButton from '@/components/ui/WhatsAppButton';
import { getMaisonsFeatured } from '@/lib/api';
import { Maison } from '@/types';

const STATS = [
  { icon: Building2, value: '200+', label: 'Biens geres' },
  { icon: MapPin,    value: '15+',  label: 'Villes couvertes' },
  { icon: Users,     value: '500+', label: 'Clients satisfaits' },
];

export default async function HomePage() {
  let featured: Maison[] = [];
  try {
    featured = await getMaisonsFeatured();
  } catch {
    featured = [];
  }

  return (
    <div>
      {/* ── Hero ── */}
      <section className="relative min-h-screen flex items-center justify-center overflow-hidden bg-gradient-to-br from-slate-900 via-blue-950 to-slate-900">
        {/* Grid overlay */}
        <div
          className="absolute inset-0 opacity-10"
          style={{
            backgroundImage: 'linear-gradient(rgba(255,255,255,.05) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,.05) 1px, transparent 1px)',
            backgroundSize: '60px 60px',
          }}
        />
        {/* Glow */}
        <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-primary-600/20 rounded-full blur-3xl" />
        <div className="absolute bottom-1/4 right-1/4 w-80 h-80 bg-blue-500/10 rounded-full blur-3xl" />

        <div className="relative z-10 text-center max-w-4xl mx-auto px-4 sm:px-6 pt-20 pb-10">
          <span className="inline-block text-primary-400 text-sm font-semibold tracking-widest uppercase mb-4 bg-primary-400/10 px-4 py-1.5 rounded-full border border-primary-400/20">
            Expert Immobilier #1
          </span>
          <h1 className="text-5xl sm:text-6xl md:text-7xl font-bold text-white mb-6 leading-tight">
            Trouvez votre{' '}
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-primary-400 to-blue-300">
              maison ideale
            </span>
          </h1>
          <p className="text-lg sm:text-xl text-slate-300 mb-10 max-w-2xl mx-auto leading-relaxed">
            Decouvrez notre selection exclusive de biens immobiliers &mdash; villas,
            maisons et appartements a vendre ou a louer.
          </p>
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
            <Link
              href="/catalogue"
              className="inline-flex items-center gap-2 bg-primary-600 hover:bg-primary-500 text-white font-semibold px-8 py-4 rounded-xl text-lg transition-colors shadow-lg shadow-primary-600/25"
            >
              Voir le catalogue
              <ArrowRight className="w-5 h-5" />
            </Link>
            <WhatsAppButton
              size="lg"
              label="Nous contacter"
              message="Bonjour, je souhaite des informations sur vos biens immobiliers."
            />
          </div>
        </div>

        {/* Scroll indicator */}
        <div className="absolute bottom-8 left-1/2 -translate-x-1/2 animate-bounce">
          <div className="w-6 h-10 rounded-full border-2 border-white/30 flex items-start justify-center pt-2">
            <div className="w-1.5 h-1.5 bg-white/60 rounded-full animate-pulse" />
          </div>
        </div>
      </section>

      {/* ── Stats ── */}
      <section className="py-20 bg-white dark:bg-slate-900">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {STATS.map(({ icon: Icon, value, label }) => (
              <div
                key={label}
                className="text-center p-8 bg-gradient-to-br from-primary-50 to-blue-50 dark:from-slate-800 dark:to-slate-800 rounded-2xl border border-primary-100 dark:border-slate-700 hover:shadow-md transition-shadow"
              >
                <div className="inline-flex items-center justify-center w-14 h-14 bg-primary-600/10 rounded-2xl mb-4">
                  <Icon className="w-7 h-7 text-primary-600" />
                </div>
                <p className="text-4xl font-bold text-slate-900 dark:text-white mb-1">{value}</p>
                <p className="text-slate-500 dark:text-slate-400 font-medium">{label}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ── Featured properties ── */}
      <section className="py-20 bg-slate-50 dark:bg-slate-800/50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-12 gap-4">
            <div>
              <h2 className="text-3xl font-bold text-slate-900 dark:text-white">Dernieres Annonces</h2>
              <p className="text-slate-500 dark:text-slate-400 mt-1">Nos biens disponibles recemment ajoutes</p>
            </div>
            <Link
              href="/catalogue"
              className="inline-flex items-center gap-1.5 text-primary-600 hover:text-primary-700 font-medium text-sm"
            >
              Voir tout le catalogue
              <ArrowRight className="w-4 h-4" />
            </Link>
          </div>

          {featured.length > 0 ? (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              {featured.slice(0, 6).map((m) => (
                <MaisonCard key={m.id} maison={m} />
              ))}
            </div>
          ) : (
            <div className="text-center py-16">
              <Building2 className="w-12 h-12 text-slate-300 mx-auto mb-3" />
              <p className="text-slate-400">Aucune annonce disponible pour le moment.</p>
            </div>
          )}
        </div>
      </section>

      {/* ── Agent section ── */}
      <section className="py-20 bg-white dark:bg-slate-900">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            {/* Photo placeholder */}
            <div className="relative max-w-md mx-auto lg:mx-0 w-full">
              <div className="aspect-square rounded-3xl bg-gradient-to-br from-primary-100 to-blue-100 dark:from-slate-700 dark:to-slate-800 flex items-center justify-center shadow-xl">
                <Users className="w-32 h-32 text-primary-300 dark:text-slate-600" />
              </div>
              {/* Floating badge */}
              <div className="absolute -bottom-4 -right-4 bg-primary-600 text-white px-5 py-3 rounded-2xl shadow-lg">
                <p className="text-2xl font-bold">10+</p>
                <p className="text-xs opacity-90">ans d'experience</p>
              </div>
            </div>

            <div>
              <span className="text-primary-600 text-sm font-semibold uppercase tracking-wider">Votre agent de confiance</span>
              <h2 className="text-3xl font-bold text-slate-900 dark:text-white mt-2 mb-5">
                Expert Immobilier Certifie
              </h2>
              <p className="text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">
                Avec plus de 10 annees d'experience dans l'immobilier residentiel et commercial,
                je vous accompagne dans tous vos projets &mdash; de la recherche a la signature.
              </p>
              <p className="text-slate-600 dark:text-slate-400 mb-8 leading-relaxed">
                Mon objectif : trouver le bien qui correspond parfaitement a vos besoins,
                a votre budget et a votre style de vie.
              </p>
              <div className="flex flex-wrap gap-3">
                <WhatsAppButton
                  label="Prendre rendez-vous"
                  message="Bonjour, je souhaite prendre rendez-vous avec un agent immobilier."
                />
                <Link
                  href="/a-propos"
                  className="inline-flex items-center gap-2 px-5 py-2.5 border border-slate-200 dark:border-slate-600 text-slate-700 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-800 font-medium rounded-xl transition-colors text-base"
                >
                  En savoir plus
                </Link>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ── CTA ── */}
      <section className="py-20 bg-gradient-to-r from-slate-900 to-blue-950 text-white">
        <div className="max-w-3xl mx-auto px-4 text-center">
          <h2 className="text-3xl sm:text-4xl font-bold mb-4">
            Vous avez un bien a vendre ou a louer?
          </h2>
          <p className="text-slate-300 mb-8 text-lg">
            Contactez-nous pour une estimation gratuite et professionnelle de votre bien.
          </p>
          <WhatsAppButton
            size="lg"
            label="Discutons de votre projet"
            message="Bonjour, j'ai un bien immobilier a vendre/louer et je souhaite une estimation gratuite."
          />
        </div>
      </section>
    </div>
  );
}
""")

# ─── src/app/catalogue/page.tsx ───
w('src/app/catalogue/page.tsx', r"""'use client';

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
""")

# ─── src/app/maison/[id]/page.tsx ───
w('src/app/maison/[id]/page.tsx', r"""import { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { Bed, Bath, Maximize2, MapPin, Calendar, Tag } from 'lucide-react';
import MaisonGalerie from '@/components/maison/MaisonGalerie';
import WhatsAppButton from '@/components/ui/WhatsAppButton';
import { getMaison } from '@/lib/api';
import { formatPrix, formatDate, getTypeLabel, getStatutLabel, getStatutColor } from '@/lib/utils';

interface Props { params: { id: string } }

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  try {
    const m = await getMaison(params.id);
    return {
      title: m.titre,
      description: m.description.slice(0, 160),
    };
  } catch {
    return { title: 'Bien introuvable' };
  }
}

export default async function MaisonDetailPage({ params }: Props) {
  const maison = await getMaison(params.id).catch(() => null);
  if (!maison) notFound();

  const waMessage = `Bonjour, je suis interesse(e) par votre bien: ${maison.titre} - ${formatPrix(maison.prix)}`;

  const stats = [
    { icon: Bed,      label: 'Chambres',      value: String(maison.chambres) },
    { icon: Bath,     label: 'Salles de bain', value: String(maison.sallesBain) },
    { icon: Maximize2, label: 'Superficie',    value: `${maison.superficie} m\u00b2` },
  ];

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-900 pt-20">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-10">

        {/* Breadcrumb */}
        <nav className="text-sm text-slate-500 dark:text-slate-400 mb-6">
          <a href="/" className="hover:text-primary-600">Accueil</a>
          <span className="mx-2">/</span>
          <a href="/catalogue" className="hover:text-primary-600">Catalogue</a>
          <span className="mx-2">/</span>
          <span className="text-slate-700 dark:text-slate-200 line-clamp-1">{maison.titre}</span>
        </nav>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Left: Gallery + details */}
          <div className="lg:col-span-2 space-y-6">
            <MaisonGalerie photos={maison.photos} titre={maison.titre} />

            {/* Video */}
            {maison.videoUrl && (
              <div className="rounded-2xl overflow-hidden aspect-video bg-black">
                <iframe
                  src={maison.videoUrl}
                  className="w-full h-full"
                  title={`Video: ${maison.titre}`}
                  allowFullScreen
                />
              </div>
            )}

            {/* Description */}
            <div className="bg-white dark:bg-slate-800 rounded-2xl p-6 shadow-sm border border-slate-100 dark:border-slate-700">
              <h2 className="text-xl font-bold text-slate-900 dark:text-white mb-4">Description</h2>
              <p className="text-slate-600 dark:text-slate-300 leading-relaxed whitespace-pre-wrap">
                {maison.description}
              </p>
            </div>
          </div>

          {/* Right: Info card */}
          <div className="space-y-4">
            <div className="bg-white dark:bg-slate-800 rounded-2xl p-6 shadow-sm border border-slate-100 dark:border-slate-700 sticky top-24">
              {/* Badges */}
              <div className="flex gap-2 mb-4">
                <span className="inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold bg-primary-600 text-white">
                  {getTypeLabel(maison.type)}
                </span>
                <span className={`inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold ${getStatutColor(maison.statut)}`}>
                  {getStatutLabel(maison.statut)}
                </span>
              </div>

              <h1 className="text-2xl font-bold text-slate-900 dark:text-white mb-2 leading-tight">
                {maison.titre}
              </h1>

              <p className="text-3xl font-bold text-primary-600 dark:text-primary-400 mb-4">
                {formatPrix(maison.prix)}
              </p>

              {/* Location */}
              <div className="flex items-start gap-2 text-slate-500 dark:text-slate-400 text-sm mb-5">
                <MapPin className="w-4 h-4 mt-0.5 flex-shrink-0" />
                <span>{maison.quartier}, {maison.ville}</span>
              </div>

              {/* Stats grid */}
              <div className="grid grid-cols-3 gap-3 mb-6">
                {stats.map(({ icon: Icon, label, value }) => (
                  <div key={label} className="text-center p-3 bg-slate-50 dark:bg-slate-700 rounded-xl">
                    <Icon className="w-5 h-5 text-primary-600 mx-auto mb-1" />
                    <p className="text-base font-bold text-slate-900 dark:text-white">{value}</p>
                    <p className="text-xs text-slate-500 dark:text-slate-400">{label}</p>
                  </div>
                ))}
              </div>

              {/* Date */}
              <div className="flex items-center gap-2 text-slate-400 text-xs mb-6">
                <Calendar className="w-3.5 h-3.5" />
                <span>Publie le {formatDate(maison.createdAt)}</span>
              </div>

              {/* CTA */}
              <WhatsAppButton
                message={waMessage}
                label="Contacter l'agent"
                size="md"
                className="w-full justify-center"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
""")

# ─── src/app/a-propos/page.tsx ───
w('src/app/a-propos/page.tsx', r"""import { Metadata } from 'next';
import { Users, CheckCircle, Phone, Mail, Award, TrendingUp } from 'lucide-react';
import WhatsAppButton from '@/components/ui/WhatsAppButton';

export const metadata: Metadata = {
  title: 'A Propos',
  description: "Decouvrez votre agent immobilier de confiance avec plus de 10 ans d'experience.",
};

const SERVICES = [
  { icon: TrendingUp, title: 'Vente', desc: "Vente de biens immobiliers residentiels et commerciaux avec une expertise locale inegalee." },
  { icon: Award,      title: 'Location', desc: "Gestion locative et mise en location de vos biens pour un rendement optimal." },
  { icon: CheckCircle, title: 'Conseil', desc: "Accompagnement personnalise a chaque etape de votre projet immobilier." },
  { icon: TrendingUp, title: 'Estimation', desc: "Estimation gratuite et precise de la valeur de votre bien selon le marche actuel." },
];

const STATS = [
  { value: '10+', label: 'Annees d\'experience' },
  { value: '200+', label: 'Biens vendus/loues' },
  { value: '500+', label: 'Clients satisfaits' },
  { value: '15+', label: 'Villes couvertes' },
];

export default function AProposPage() {
  return (
    <div className="min-h-screen bg-white dark:bg-slate-900 pt-20">

      {/* Hero */}
      <section className="bg-gradient-to-br from-slate-900 to-blue-950 text-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <span className="text-primary-400 text-sm font-semibold uppercase tracking-wider">A Propos</span>
          <h1 className="text-4xl sm:text-5xl font-bold mt-2 mb-4">Votre Agent de Confiance</h1>
          <p className="text-slate-300 text-lg max-w-2xl mx-auto">
            Expert immobilier certifie, je mets mon expertise et mon reseau au service de vos projets.
          </p>
        </div>
      </section>

      {/* Profile */}
      <section className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            {/* Photo */}
            <div className="relative max-w-sm mx-auto lg:mx-0 w-full">
              <div className="aspect-square rounded-3xl bg-gradient-to-br from-primary-100 to-blue-100 dark:from-slate-700 dark:to-slate-800 flex items-center justify-center shadow-2xl">
                <Users className="w-40 h-40 text-primary-300 dark:text-slate-600" />
              </div>
              <div className="absolute -bottom-5 -right-5 bg-primary-600 text-white p-5 rounded-2xl shadow-xl">
                <p className="text-3xl font-bold leading-none">10+</p>
                <p className="text-xs opacity-80 mt-1">ans d'experience</p>
              </div>
            </div>

            {/* Bio */}
            <div>
              <h2 className="text-3xl font-bold text-slate-900 dark:text-white mb-2">Jean-Paul Mbarga</h2>
              <p className="text-primary-600 font-semibold mb-5">Expert Immobilier Certifie &bull; ImmoExpert</p>

              <div className="space-y-3 text-slate-600 dark:text-slate-400 leading-relaxed mb-6">
                <p>
                  Passionne par l'immobilier depuis plus de 10 ans, j'accompagne mes clients dans leurs projets
                  d'achat, de vente et de location avec professionnalisme et transparence.
                </p>
                <p>
                  Mon expertise couvre l'immobilier residentiel (villas, maisons, appartements) et commercial
                  (bureaux, entrepots, locaux commerciaux) dans les principales villes du Cameroun.
                </p>
                <p>
                  Chaque client est unique: j'adapte mon approche a vos besoins specifiques pour vous garantir
                  les meilleures conditions dans votre projet immobilier.
                </p>
              </div>

              {/* Contact */}
              <div className="flex flex-wrap gap-3">
                <WhatsAppButton
                  label="Contacter par WhatsApp"
                  message="Bonjour Jean-Paul, je souhaite discuter d'un projet immobilier."
                />
                <a
                  href="mailto:contact@immoexpert.cm"
                  className="inline-flex items-center gap-2 px-5 py-2.5 border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-800 font-medium rounded-xl transition-colors"
                >
                  <Mail className="w-4 h-4" />
                  Email
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Stats */}
      <section className="py-16 bg-primary-600">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-white text-center">
            {STATS.map(({ value, label }) => (
              <div key={label}>
                <p className="text-4xl font-bold mb-1">{value}</p>
                <p className="text-primary-200 text-sm">{label}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Services */}
      <section className="py-20 bg-slate-50 dark:bg-slate-800/50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-slate-900 dark:text-white">Mes Services</h2>
            <p className="text-slate-500 dark:text-slate-400 mt-2">Un accompagnement complet pour tous vos projets</p>
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {SERVICES.map(({ icon: Icon, title, desc }) => (
              <div key={title} className="bg-white dark:bg-slate-800 rounded-2xl p-6 shadow-sm border border-slate-100 dark:border-slate-700 hover:shadow-md transition-shadow">
                <div className="w-12 h-12 bg-primary-50 dark:bg-primary-900/20 rounded-xl flex items-center justify-center mb-4">
                  <Icon className="w-6 h-6 text-primary-600" />
                </div>
                <h3 className="font-bold text-slate-900 dark:text-white mb-2">{title}</h3>
                <p className="text-slate-500 dark:text-slate-400 text-sm leading-relaxed">{desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Contact CTA */}
      <section className="py-20 bg-white dark:bg-slate-900">
        <div className="max-w-2xl mx-auto px-4 text-center">
          <h2 className="text-3xl font-bold text-slate-900 dark:text-white mb-4">Pret a demarrer votre projet?</h2>
          <p className="text-slate-500 dark:text-slate-400 mb-8">
            Contactez-moi aujourd'hui pour une consultation gratuite et sans engagement.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <WhatsAppButton
              size="lg"
              label="WhatsApp"
              message="Bonjour, je souhaite prendre contact pour un projet immobilier."
            />
            <a
              href="mailto:contact@immoexpert.cm"
              className="inline-flex items-center justify-center gap-2 px-8 py-4 border-2 border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-800 font-semibold rounded-xl transition-colors text-lg"
            >
              <Mail className="w-5 h-5" />
              Envoyer un email
            </a>
          </div>
        </div>
      </section>
    </div>
  );
}
""")

print('  Done.\n')
