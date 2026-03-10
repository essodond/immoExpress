#!/usr/bin/env python3
"""ImmoExpert - Layout components, Maison components"""
import os

BASE = r'C:\Users\DELL\Documents\projet\immo\frontend'

def w(path, content):
    full = os.path.join(BASE, path.replace('/', os.sep))
    d = os.path.dirname(full)
    if d: os.makedirs(d, exist_ok=True)
    with open(full, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    print(f'  \u2713 {path}')

print('[2/4] Layout & Maison components...')

# ─── src/components/layout/Navbar.tsx ───
w('src/components/layout/Navbar.tsx', r"""'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { Home, Menu, X } from 'lucide-react';
import ThemeToggle from '@/components/ui/ThemeToggle';
import WhatsAppButton from '@/components/ui/WhatsAppButton';

const links = [
  { href: '/', label: 'Accueil' },
  { href: '/catalogue', label: 'Catalogue' },
  { href: '/a-propos', label: 'A Propos' },
];

export default function Navbar() {
  const [open, setOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const pathname = usePathname();

  useEffect(() => {
    const fn = () => setScrolled(window.scrollY > 10);
    window.addEventListener('scroll', fn, { passive: true });
    return () => window.removeEventListener('scroll', fn);
  }, []);

  useEffect(() => setOpen(false), [pathname]);

  const solid = scrolled || pathname !== '/';

  return (
    <header
      className={`fixed top-0 inset-x-0 z-50 transition-all duration-300 ${
        solid
          ? 'bg-white/95 dark:bg-slate-900/95 backdrop-blur-md shadow-sm border-b border-slate-100 dark:border-slate-800'
          : 'bg-transparent'
      }`}
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link href="/" className="flex items-center gap-2 font-bold text-xl text-primary-600">
            <Home className="w-6 h-6" />
            <span>ImmoExpert</span>
          </Link>

          {/* Desktop nav */}
          <nav className="hidden md:flex items-center gap-6" aria-label="Navigation principale">
            {links.map((l) => (
              <Link
                key={l.href}
                href={l.href}
                className={`font-medium transition-colors text-sm ${
                  pathname === l.href
                    ? 'text-primary-600'
                    : solid
                    ? 'text-slate-600 dark:text-slate-300 hover:text-primary-600 dark:hover:text-primary-400'
                    : 'text-white/90 hover:text-white'
                }`}
              >
                {l.label}
              </Link>
            ))}
          </nav>

          <div className="hidden md:flex items-center gap-2">
            <WhatsAppButton size="sm" label="WhatsApp" />
            <ThemeToggle />
          </div>

          {/* Mobile toggle */}
          <div className="flex md:hidden items-center gap-1">
            <ThemeToggle />
            <button
              onClick={() => setOpen(!open)}
              className="p-2 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700"
              aria-label="Menu"
              aria-expanded={open}
            >
              {open ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
        </div>

        {/* Mobile menu */}
        {open && (
          <div className="md:hidden pb-4 pt-2 space-y-1 bg-white dark:bg-slate-900 border-t border-slate-100 dark:border-slate-800">
            {links.map((l) => (
              <Link
                key={l.href}
                href={l.href}
                className={`block px-4 py-2.5 rounded-lg font-medium text-sm ${
                  pathname === l.href
                    ? 'bg-primary-50 dark:bg-primary-900/20 text-primary-600'
                    : 'text-slate-600 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-800'
                }`}
              >
                {l.label}
              </Link>
            ))}
            <div className="px-4 pt-2">
              <WhatsAppButton size="sm" label="Contacter sur WhatsApp" className="w-full justify-center" />
            </div>
          </div>
        )}
      </div>
    </header>
  );
}
""")

# ─── src/components/layout/Footer.tsx ───
w('src/components/layout/Footer.tsx', r"""import Link from 'next/link';
import { Home, MessageCircle, Mail } from 'lucide-react';

const navLinks = [
  { href: '/', label: 'Accueil' },
  { href: '/catalogue', label: 'Catalogue' },
  { href: '/a-propos', label: 'A Propos' },
];

export default function Footer() {
  const num = (process.env.NEXT_PUBLIC_WHATSAPP_NUMBER || '+237600000000').replace(/\D/g, '');
  const waUrl = `https://wa.me/${num}?text=${encodeURIComponent('Bonjour, je souhaite des informations.')}`;

  return (
    <footer className="bg-slate-900 text-slate-300">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-14">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
          {/* Brand */}
          <div>
            <Link href="/" className="inline-flex items-center gap-2 text-white font-bold text-xl mb-3">
              <Home className="w-6 h-6 text-primary-400" />
              ImmoExpert
            </Link>
            <p className="text-slate-400 text-sm leading-relaxed max-w-xs">
              Votre partenaire de confiance pour tous vos projets immobiliers.
              Vente, location et conseil en Afrique.
            </p>
          </div>

          {/* Links */}
          <div>
            <h3 className="text-white font-semibold mb-4">Navigation</h3>
            <ul className="space-y-2">
              {navLinks.map((l) => (
                <li key={l.href}>
                  <Link href={l.href} className="text-sm hover:text-white transition-colors">
                    {l.label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          {/* Contact */}
          <div>
            <h3 className="text-white font-semibold mb-4">Contact</h3>
            <div className="space-y-3">
              <a href={waUrl} target="_blank" rel="noopener noreferrer"
                className="flex items-center gap-2 text-sm hover:text-green-400 transition-colors">
                <MessageCircle className="w-4 h-4 flex-shrink-0" />
                WhatsApp
              </a>
              <a href="mailto:contact@immoexpert.cm"
                className="flex items-center gap-2 text-sm hover:text-white transition-colors">
                <Mail className="w-4 h-4 flex-shrink-0" />
                contact@immoexpert.cm
              </a>
            </div>
          </div>
        </div>

        <div className="border-t border-slate-800 mt-12 pt-6 text-center text-xs text-slate-500">
          &copy; 2024 ImmoExpert. Tous droits reserves.
        </div>
      </div>
    </footer>
  );
}
""")

# ─── src/components/maison/MaisonCard.tsx ───
w('src/components/maison/MaisonCard.tsx', r"""import Image from 'next/image';
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
""")

# ─── src/components/maison/MaisonGalerie.tsx ───
w('src/components/maison/MaisonGalerie.tsx', r"""'use client';

import { useState } from 'react';
import Image from 'next/image';
import { ChevronLeft, ChevronRight, X, ZoomIn } from 'lucide-react';
import { Photo } from '@/types';

interface Props {
  photos: Photo[];
  titre: string;
}

export default function MaisonGalerie({ photos, titre }: Props) {
  const [current, setCurrent] = useState(0);
  const [lightbox, setLightbox] = useState(false);

  if (!photos || photos.length === 0) {
    return (
      <div className="aspect-video bg-slate-200 dark:bg-slate-700 rounded-2xl flex items-center justify-center">
        <p className="text-slate-400">Aucune photo disponible</p>
      </div>
    );
  }

  const prev = () => setCurrent((c) => (c - 1 + photos.length) % photos.length);
  const next = () => setCurrent((c) => (c + 1) % photos.length);

  return (
    <>
      {/* Main image */}
      <div className="relative aspect-video rounded-2xl overflow-hidden bg-slate-100 dark:bg-slate-800 group">
        <Image
          src={photos[current].url}
          alt={`${titre} - photo ${current + 1}`}
          fill
          className="object-cover"
          priority
          sizes="(max-width: 768px) 100vw, 800px"
        />

        {/* Counter */}
        <div className="absolute bottom-3 left-3 bg-black/60 text-white text-xs px-2.5 py-1 rounded-full">
          {current + 1} / {photos.length}
        </div>

        {/* Zoom button */}
        <button
          onClick={() => setLightbox(true)}
          className="absolute bottom-3 right-3 bg-black/60 hover:bg-black/80 text-white p-2 rounded-full transition-colors"
          aria-label="Agrandir"
        >
          <ZoomIn className="w-4 h-4" />
        </button>

        {/* Arrows (only if >1 photo) */}
        {photos.length > 1 && (
          <>
            <button
              onClick={prev}
              className="absolute left-3 top-1/2 -translate-y-1/2 bg-black/50 hover:bg-black/70 text-white p-2 rounded-full transition-colors opacity-0 group-hover:opacity-100"
              aria-label="Photo precedente"
            >
              <ChevronLeft className="w-5 h-5" />
            </button>
            <button
              onClick={next}
              className="absolute right-3 top-1/2 -translate-y-1/2 bg-black/50 hover:bg-black/70 text-white p-2 rounded-full transition-colors opacity-0 group-hover:opacity-100"
              aria-label="Photo suivante"
            >
              <ChevronRight className="w-5 h-5" />
            </button>
          </>
        )}
      </div>

      {/* Thumbnails */}
      {photos.length > 1 && (
        <div className="flex gap-2 overflow-x-auto pb-1 mt-3">
          {photos.map((photo, i) => (
            <button
              key={photo.id}
              onClick={() => setCurrent(i)}
              className={`relative flex-shrink-0 w-20 h-14 rounded-lg overflow-hidden border-2 transition-all ${
                i === current ? 'border-primary-600 opacity-100' : 'border-transparent opacity-60 hover:opacity-90'
              }`}
              aria-label={`Photo ${i + 1}`}
            >
              <Image src={photo.url} alt={`Miniature ${i + 1}`} fill className="object-cover" sizes="80px" />
            </button>
          ))}
        </div>
      )}

      {/* Lightbox */}
      {lightbox && (
        <div
          className="fixed inset-0 z-[100] bg-black/95 flex items-center justify-center"
          onClick={() => setLightbox(false)}
        >
          <button
            className="absolute top-4 right-4 text-white hover:text-slate-300 p-2"
            onClick={() => setLightbox(false)}
            aria-label="Fermer"
          >
            <X className="w-8 h-8" />
          </button>

          {photos.length > 1 && (
            <>
              <button
                onClick={(e) => { e.stopPropagation(); prev(); }}
                className="absolute left-4 top-1/2 -translate-y-1/2 text-white hover:text-slate-300 bg-white/10 hover:bg-white/20 p-3 rounded-full"
                aria-label="Precedente"
              >
                <ChevronLeft className="w-6 h-6" />
              </button>
              <button
                onClick={(e) => { e.stopPropagation(); next(); }}
                className="absolute right-4 top-1/2 -translate-y-1/2 text-white hover:text-slate-300 bg-white/10 hover:bg-white/20 p-3 rounded-full"
                aria-label="Suivante"
              >
                <ChevronRight className="w-6 h-6" />
              </button>
            </>
          )}

          <div className="relative w-full max-w-4xl max-h-[85vh] aspect-video mx-4" onClick={(e) => e.stopPropagation()}>
            <Image
              src={photos[current].url}
              alt={`${titre} - photo ${current + 1}`}
              fill
              className="object-contain"
              sizes="(max-width: 896px) 100vw, 896px"
            />
          </div>

          <p className="absolute bottom-4 text-white/70 text-sm">
            {current + 1} / {photos.length}
          </p>
        </div>
      )}
    </>
  );
}
""")

# ─── src/components/maison/MaisonFilters.tsx ───
w('src/components/maison/MaisonFilters.tsx', r"""'use client';

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
""")

# ─── src/components/maison/MaisonForm.tsx ───
w('src/components/maison/MaisonForm.tsx', r"""'use client';

import { useEffect, useRef, useState } from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { useRouter } from 'next/navigation';
import toast from 'react-hot-toast';
import Image from 'next/image';
import { Upload, Trash2, Star, Loader2 } from 'lucide-react';
import { Maison, Photo } from '@/types';
import { createMaison, updateMaison, uploadPhotos, deletePhoto, setMainPhoto } from '@/lib/api';

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
  videoUrl:    z.string().optional().or(z.literal('')),
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
      // Reload maison to get updated photos - for simplicity we show a message
      toast.success(`${files.length} photo(s) uploadee(s) avec succes!`);
      router.refresh();
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
            <label className={labelCls}>URL Video (optionnel)</label>
            <input {...register('videoUrl')} className={inputCls} placeholder="https://youtube.com/embed/..." />
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
""")

print('  Done.\n')
