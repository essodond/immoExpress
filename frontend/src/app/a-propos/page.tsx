import { Metadata } from 'next';
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
