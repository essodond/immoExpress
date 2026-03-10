'use client';

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
