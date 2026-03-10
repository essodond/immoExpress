import { MessageCircle } from 'lucide-react';

interface P {
  message?: string;
  label?: string;
  className?: string;
  size?: 'sm' | 'md' | 'lg';
}

const SZ = { sm: 'px-3 py-1.5 text-sm gap-1.5', md: 'px-5 py-2.5 text-base gap-2', lg: 'px-8 py-4 text-lg gap-2.5' };
const IC = { sm: 'w-4 h-4', md: 'w-5 h-5', lg: 'w-6 h-6' };

export default function WhatsAppButton({
  message = "Bonjour, je suis interesse(e) par vos services immobiliers.",
  label = "Contacter sur WhatsApp",
  className = '',
  size = 'md',
}: P) {
  const num = (process.env.NEXT_PUBLIC_WHATSAPP_NUMBER || '+237600000000').replace(/\D/g, '');
  const url = `https://wa.me/${num}?text=${encodeURIComponent(message)}`;
  return (
    <a
      href={url}
      target="_blank"
      rel="noopener noreferrer"
      aria-label={label}
      className={`inline-flex items-center font-semibold bg-green-500 hover:bg-green-600 active:bg-green-700 text-white rounded-xl transition-colors duration-200 ${SZ[size]} ${className}`}
    >
      <MessageCircle className={`flex-shrink-0 ${IC[size]}`} />
      {label}
    </a>
  );
}
