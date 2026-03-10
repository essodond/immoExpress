import { Photo } from '@/types';

export const formatPrix = (prix: number): string =>
  new Intl.NumberFormat('fr-FR').format(prix) + ' FCFA';

export const getMainPhoto = (photos: Photo[]): string => {
  if (!photos || photos.length === 0)
    return 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=800&q=80';
  const main = photos.find((p) => p.isMain);
  return main ? main.url : photos[0].url;
};

export const getStatutColor = (statut: string): string => {
  switch (statut) {
    case 'disponible': return 'bg-green-100 text-green-800 dark:bg-green-900/30 dark:text-green-400';
    case 'vendu':      return 'bg-red-100 text-red-800 dark:bg-red-900/30 dark:text-red-400';
    case 'loue':       return 'bg-amber-100 text-amber-800 dark:bg-amber-900/30 dark:text-amber-400';
    default:           return 'bg-slate-100 text-slate-700 dark:bg-slate-700 dark:text-slate-300';
  }
};

export const getStatutLabel = (statut: string): string => {
  switch (statut) {
    case 'disponible': return 'Disponible';
    case 'vendu':      return 'Vendu';
    case 'loue':       return 'Loue';
    default:           return statut;
  }
};

export const getTypeLabel = (type: string): string => {
  switch (type) {
    case 'vente':    return 'A Vendre';
    case 'location': return 'A Louer';
    default:         return type;
  }
};

export const formatDate = (date: string): string =>
  new Intl.DateTimeFormat('fr-FR', {
    day: '2-digit', month: 'long', year: 'numeric',
  }).format(new Date(date));

export const cn = (...classes: (string | undefined | null | false)[]): string =>
  classes.filter(Boolean).join(' ');

export const convertVideoUrl = (url: string): string | null => {
  if (!url) return null;

  // Regex pour extraire l'ID TikTok
  const tiktokRegex = /(?:tiktok\.com|vt\.tiktok\.com)\/(?:v\/)?(\d+)|@[\w.-]+\/video\/(\d+)/;
  const tiktokMatch = url.match(tiktokRegex);

  if (tiktokMatch) {
    const videoId = tiktokMatch[1] || tiktokMatch[2];
    return `https://www.tiktok.com/embed/v/${videoId}`;
  }

  // Regex pour extraire l'ID YouTube
  const youtubeRegex = /(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([a-zA-Z0-9_-]{11})/;
  const youtubeMatch = url.match(youtubeRegex);

  if (youtubeMatch) {
    return `https://www.youtube.com/embed/${youtubeMatch[1]}`;
  }

  // Si c'est déjà une URL embed, la retourner
  if (url.includes('youtube.com/embed') || url.includes('tiktok.com/embed')) {
    return url;
  }

  return url;
};

