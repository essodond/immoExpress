import Link from 'next/link';
import { Home, MessageCircle, Mail } from 'lucide-react';

const navLinks = [
  { href: '/', label: 'Accueil' },
  { href: '/catalogue', label: 'Catalogue' },
  { href: '/a-propos', label: 'A Propos' },
];

export default function Footer() {
  const num = (process.env.NEXT_PUBLIC_WHATSAPP_NUMBER || '+22871608097').replace(/\D/g, '');
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
