'use client';

import { useEffect, useRef, useState } from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { useRouter } from 'next/navigation';
import toast from 'react-hot-toast';
import Image from 'next/image';
import { Upload, Trash2, Star, Loader2, AlertCircle } from 'lucide-react';
import { Maison, Photo } from '@/types';
import { createMaison, updateMaison, uploadPhotos, deletePhoto, setMainPhoto, getMaison } from '@/lib/api';
import { convertVideoUrl } from '@/lib/utils';

const schema = z.object({
  titre:       z.string().min(5, 'Minimum 5 caracteres'),
  description: z.string().min(20, 'Minimum 20 caracteres'),
  prix:        z.coerce.number().min(1, 'Le prix doit etre positif'),
  type:        z.enum(['vente', 'location']),
  ville:       z.string().min(2, 'Ville requise'),
  quartier:    z.string().min(2, 'Quartier requis'),
  chambres:    z.coerce.number().min(0),
  sallesBain:  z.coerce.number().min(0),
  superficie:  z.coerce.number().min(1, 'Superficie requise'),
  statut:      z.enum(['disponible', 'vendu', 'loue']),
  videoUrl:    z.string().optional()
    .refine((url) => !url || /^(https?:\/\/)?(www\.)?(youtube|youtu\.be|tiktok|vt\.tiktok)/.test(url),
      'URL YouTube ou TikTok invalide')
    .or(z.literal('')),
});

type FormData = z.infer<typeof schema>;

interface Props {
  maison?: Maison;
}

const inputCls = "w-full px-3 py-2.5 rounded-xl border border-slate-200 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-900 dark:text-white text-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent placeholder-slate-400";
const labelCls = "block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1.5";
const errorCls = "text-xs text-red-500 mt-1";

export default function MaisonForm({ maison }: Props) {
  const router = useRouter();
  const fileRef = useRef<HTMLInputElement>(null);
  const [photos, setPhotos] = useState<Photo[]>(maison?.photos || []);
  const [uploading, setUploading] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [savedId, setSavedId] = useState<string | undefined>(maison?.id);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormData>({
    resolver: zodResolver(schema),
    defaultValues: maison
      ? {
          titre:       maison.titre,
          description: maison.description,
          prix:        maison.prix,
          type:        maison.type,
          ville:       maison.ville,
          quartier:    maison.quartier,
          chambres:    maison.chambres,
          sallesBain:  maison.sallesBain,
          superficie:  maison.superficie,
          statut:      maison.statut,
          videoUrl:    maison.videoUrl || '',
        }
      : { type: 'vente', statut: 'disponible', chambres: 0, sallesBain: 0, superficie: 0 },
  });

  const onSubmit = async (data: FormData) => {
    setSubmitting(true);
    try {
      let id = savedId;
      if (maison) {
        await updateMaison(maison.id, data);
        toast.success('Bien mis a jour avec succes!');
        id = maison.id;
      } else {
        const created = await createMaison(data);
        setSavedId(created.id);
        id = created.id;
        toast.success('Bien cree avec succes!');
      }
      router.push('/admin/maisons');
    } catch {
      toast.error('Une erreur est survenue.');
    } finally {
      setSubmitting(false);
    }
  };

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = e.target.files;
    if (!files || files.length === 0) return;

    const targetId = savedId;
    if (!targetId) {
      toast.error('Veuillez d\'abord enregistrer le bien avant d\'ajouter des photos.');
      return;
    }

    setUploading(true);
    try {
      await uploadPhotos(targetId, files);
      toast.success(`${files.length} photo(s) uploadée(s) avec succès!`);

      // Recharger les photos depuis l'API
      const updatedMaison = await getMaison(targetId);
      setPhotos(updatedMaison.photos);
    } catch {
      toast.error('Erreur lors de l\'upload des photos.');
    } finally {
      setUploading(false);
      if (fileRef.current) fileRef.current.value = '';
    }
  };

  const handleDeletePhoto = async (photoId: string) => {
    if (!confirm('Supprimer cette photo?')) return;
    try {
      await deletePhoto(photoId);
      setPhotos((p) => p.filter((ph) => ph.id !== photoId));
      toast.success('Photo supprimee.');
    } catch {
      toast.error('Erreur lors de la suppression.');
    }
  };

  const handleSetMain = async (photoId: string) => {
    try {
      await setMainPhoto(photoId);
      setPhotos((p) => p.map((ph) => ({ ...ph, isMain: ph.id === photoId })));
      toast.success('Photo principale definie.');
    } catch {
      toast.error('Erreur.');
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-8">
      {/* Informations generales */}
      <section className="bg-white dark:bg-slate-800 rounded-2xl p-6 shadow-sm border border-slate-100 dark:border-slate-700">
        <h2 className="font-semibold text-slate-900 dark:text-white mb-5">Informations generales</h2>
        <div className="grid grid-cols-1 gap-5">
          <div>
            <label className={labelCls}>Titre *</label>
            <input {...register('titre')} className={inputCls} placeholder="Ex: Villa 4 chambres avec piscine" />
            {errors.titre && <p className={errorCls}>{errors.titre.message}</p>}
          </div>
          <div>
            <label className={labelCls}>Description *</label>
            <textarea {...register('description')} rows={5} className={inputCls} placeholder="Decrivez le bien en detail..." />
            {errors.description && <p className={errorCls}>{errors.description.message}</p>}
          </div>
        </div>
      </section>

      {/* Details */}
      <section className="bg-white dark:bg-slate-800 rounded-2xl p-6 shadow-sm border border-slate-100 dark:border-slate-700">
        <h2 className="font-semibold text-slate-900 dark:text-white mb-5">Details du bien</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
          <div>
            <label className={labelCls}>Prix (FCFA) *</label>
            <input type="number" {...register('prix')} className={inputCls} placeholder="Ex: 5000000" />
            {errors.prix && <p className={errorCls}>{errors.prix.message}</p>}
          </div>
          <div>
            <label className={labelCls}>Type *</label>
            <select {...register('type')} className={inputCls}>
              <option value="vente">A Vendre</option>
              <option value="location">A Louer</option>
            </select>
          </div>
          <div>
            <label className={labelCls}>Ville *</label>
            <input {...register('ville')} className={inputCls} placeholder="Ex: Douala" />
            {errors.ville && <p className={errorCls}>{errors.ville.message}</p>}
          </div>
          <div>
            <label className={labelCls}>Quartier *</label>
            <input {...register('quartier')} className={inputCls} placeholder="Ex: Bonanjo" />
            {errors.quartier && <p className={errorCls}>{errors.quartier.message}</p>}
          </div>
          <div>
            <label className={labelCls}>Chambres</label>
            <input type="number" min={0} {...register('chambres')} className={inputCls} />
          </div>
          <div>
            <label className={labelCls}>Salles de bain</label>
            <input type="number" min={0} {...register('sallesBain')} className={inputCls} />
          </div>
          <div>
            <label className={labelCls}>Superficie (m2) *</label>
            <input type="number" min={1} {...register('superficie')} className={inputCls} />
            {errors.superficie && <p className={errorCls}>{errors.superficie.message}</p>}
          </div>
          <div>
            <label className={labelCls}>Statut</label>
            <select {...register('statut')} className={inputCls}>
              <option value="disponible">Disponible</option>
              <option value="vendu">Vendu</option>
              <option value="loue">Loue</option>
            </select>
          </div>
          <div className="sm:col-span-2">
            <label className={labelCls}>URL Vidéo (optionnel)</label>
            <input
              {...register('videoUrl')}
              className={inputCls}
              placeholder="https://youtube.com/watch?v=... ou https://tiktok.com/video/..."
            />
            {errors.videoUrl && <p className={errorCls}>{errors.videoUrl.message}</p>}
            <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">
              ✓ YouTube: youtube.com/watch?v=... ou youtu.be/...
            </p>
            <p className="text-xs text-slate-500 dark:text-slate-400">
              ✓ TikTok: tiktok.com/video/... ou vt.tiktok.com/...
            </p>
          </div>
        </div>
      </section>

      {/* Photos */}
      <section className="bg-white dark:bg-slate-800 rounded-2xl p-6 shadow-sm border border-slate-100 dark:border-slate-700">
        <div className="flex items-center justify-between mb-5">
          <h2 className="font-semibold text-slate-900 dark:text-white">Photos</h2>
          <button
            type="button"
            onClick={() => fileRef.current?.click()}
            disabled={uploading || !savedId}
            className="flex items-center gap-2 px-4 py-2 bg-primary-600 hover:bg-primary-700 disabled:opacity-50 text-white text-sm font-medium rounded-xl transition-colors"
          >
            {uploading ? <Loader2 className="w-4 h-4 animate-spin" /> : <Upload className="w-4 h-4" />}
            {uploading ? 'Upload...' : 'Ajouter photos'}
          </button>
          <input
            ref={fileRef}
            type="file"
            multiple
            accept="image/*"
            className="hidden"
            onChange={handleFileChange}
          />
        </div>

        {!savedId && (
          <p className="text-sm text-amber-600 bg-amber-50 dark:bg-amber-900/20 px-3 py-2 rounded-lg mb-4">
            Enregistrez d'abord le bien pour pouvoir ajouter des photos.
          </p>
        )}

        {photos.length > 0 ? (
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-3">
            {photos.map((photo) => (
              <div key={photo.id} className="relative group aspect-square rounded-xl overflow-hidden bg-slate-100 dark:bg-slate-700">
                <Image src={photo.url} alt="Photo" fill className="object-cover" sizes="200px" />
                {photo.isMain && (
                  <div className="absolute top-1 left-1 bg-primary-600 text-white text-xs px-2 py-0.5 rounded-full flex items-center gap-1">
                    <Star className="w-3 h-3" /> Principal
                  </div>
                )}
                <div className="absolute inset-0 bg-black/0 group-hover:bg-black/40 transition-colors flex items-center justify-center gap-2 opacity-0 group-hover:opacity-100">
                  {!photo.isMain && (
                    <button
                      type="button"
                      onClick={() => handleSetMain(photo.id)}
                      className="bg-primary-600 text-white p-1.5 rounded-lg hover:bg-primary-700"
                      title="Definir comme principal"
                    >
                      <Star className="w-4 h-4" />
                    </button>
                  )}
                  <button
                    type="button"
                    onClick={() => handleDeletePhoto(photo.id)}
                    className="bg-red-500 text-white p-1.5 rounded-lg hover:bg-red-600"
                    title="Supprimer"
                  >
                    <Trash2 className="w-4 h-4" />
                  </button>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="border-2 border-dashed border-slate-200 dark:border-slate-600 rounded-xl p-10 text-center">
            <Upload className="w-10 h-10 text-slate-300 mx-auto mb-3" />
            <p className="text-slate-400 text-sm">Aucune photo. Ajoutez des photos ci-dessus.</p>
          </div>
        )}
      </section>

      {/* Submit */}
      <div className="flex gap-3">
        <button
          type="submit"
          disabled={submitting}
          className="flex items-center gap-2 px-8 py-3 bg-primary-600 hover:bg-primary-700 disabled:opacity-60 text-white font-semibold rounded-xl transition-colors"
        >
          {submitting && <Loader2 className="w-4 h-4 animate-spin" />}
          {maison ? 'Mettre a jour' : 'Creer le bien'}
        </button>
        <button
          type="button"
          onClick={() => router.push('/admin/maisons')}
          className="px-6 py-3 border border-slate-200 dark:border-slate-600 text-slate-700 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-700 font-medium rounded-xl transition-colors"
        >
          Annuler
        </button>
      </div>
    </form>
  );
}
