import { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { Bed, Bath, Maximize2, MapPin, Calendar, Tag } from 'lucide-react';
import MaisonGalerie from '@/components/maison/MaisonGalerie';
import VideoEmbed from '@/components/maison/VideoEmbed';
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
            <VideoEmbed url={maison.videoUrl} titre={maison.titre} />

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
