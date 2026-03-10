import Image from 'next/image';
import Link from 'next/link';
import { MapPin, Bed, Bath, Maximize2 } from 'lucide-react';
import { Maison } from '@/types';
import { formatPrix, getMainPhoto, getTypeLabel, getStatutLabel, getStatutColor } from '@/lib/utils';
import Badge from '@/components/ui/Badge';

export default function MaisonCard({ maison }: { maison: Maison }) {
  const photo = getMainPhoto(maison.photos);
  const typeVariant = maison.type === 'vente' ? 'primary' : 'secondary';

  return (
    <article className="bg-white dark:bg-slate-800 rounded-2xl shadow-md hover:shadow-xl transition-all duration-300 overflow-hidden group flex flex-col">
      {/* Image */}
      <div className="relative aspect-video overflow-hidden bg-slate-100 dark:bg-slate-700">
        <Image
          src={photo}
          alt={maison.titre}
          fill
          sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
          className="object-cover group-hover:scale-105 transition-transform duration-500"
          unoptimized={photo.includes('unsplash.com')}
        />
        <div className="absolute top-3 left-3">
          <Badge variant={typeVariant}>{getTypeLabel(maison.type)}</Badge>
        </div>
        <div className="absolute top-3 right-3">
          <span className={`inline-flex items-center px-2.5 py-1 rounded-full text-xs font-semibold ${getStatutColor(maison.statut)}`}>
            {getStatutLabel(maison.statut)}
          </span>
        </div>
      </div>

      {/* Content */}
      <div className="p-5 flex flex-col flex-1">
        <h3 className="font-bold text-base text-slate-900 dark:text-white mb-1 line-clamp-1">
          {maison.titre}
        </h3>
        <p className="text-xl font-bold text-primary-600 dark:text-primary-400 mb-3">
          {formatPrix(maison.prix)}
        </p>

        <div className="flex items-center text-slate-500 dark:text-slate-400 text-sm mb-4 gap-1">
          <MapPin className="w-4 h-4 flex-shrink-0" />
          <span className="line-clamp-1">{maison.quartier}, {maison.ville}</span>
        </div>

        <div className="flex items-center justify-between text-slate-600 dark:text-slate-300 text-sm border-t border-slate-100 dark:border-slate-700 pt-3 mb-4">
          <div className="flex items-center gap-1" title="Chambres">
            <Bed className="w-4 h-4" />
            <span>{maison.chambres} ch.</span>
          </div>
          <div className="flex items-center gap-1" title="Salles de bain">
            <Bath className="w-4 h-4" />
            <span>{maison.sallesBain} sdb.</span>
          </div>
          <div className="flex items-center gap-1" title="Superficie">
            <Maximize2 className="w-4 h-4" />
            <span>{maison.superficie} m&sup2;</span>
          </div>
        </div>

        <Link
          href={`/maison/${maison.id}`}
          className="mt-auto block text-center bg-primary-600 hover:bg-primary-700 active:bg-primary-800 text-white font-medium py-2.5 rounded-xl transition-colors duration-200 text-sm"
        >
          Voir les details
        </Link>
      </div>
    </article>
  );
}
