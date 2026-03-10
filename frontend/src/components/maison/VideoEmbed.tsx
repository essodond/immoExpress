'use client';

import { convertVideoUrl } from '@/lib/utils';

interface VideoEmbedProps {
  url?: string | null;
  titre: string;
}

export default function VideoEmbed({ url, titre }: VideoEmbedProps) {
  if (!url) return null;

  const embedUrl = convertVideoUrl(url);
  if (!embedUrl) return null;

  // Déterminer le ratio d'aspect approprié
  const isTikTok = embedUrl.includes('tiktok.com');
  const aspectClass = isTikTok ? 'aspect-[9/16]' : 'aspect-video';

  return (
    <div className={`rounded-2xl overflow-hidden bg-black ${aspectClass} w-full max-w-4xl`}>
      <iframe
        src={embedUrl}
        className="w-full h-full"
        title={`Video: ${titre}`}
        allowFullScreen
        allow={isTikTok ? 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' : 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture'}
      />
    </div>
  );
}

