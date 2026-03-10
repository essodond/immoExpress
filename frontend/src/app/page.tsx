import Link from 'next/link';
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
