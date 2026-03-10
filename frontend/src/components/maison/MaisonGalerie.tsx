'use client';

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
