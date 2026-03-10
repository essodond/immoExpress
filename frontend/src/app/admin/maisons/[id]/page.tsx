import { Metadata } from 'next';
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
