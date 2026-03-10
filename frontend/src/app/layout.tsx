import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';
import Providers from '@/providers/Providers';
import Navbar from '@/components/layout/Navbar';
import Footer from '@/components/layout/Footer';

const inter = Inter({ subsets: ['latin'], variable: '--font-inter' });

export const metadata: Metadata = {
  title: { default: 'ImmoExpert - Votre Expert Immobilier', template: '%s | ImmoExpert' },
  description: 'Trouvez votre bien immobilier ideal avec ImmoExpert. Vente et location de maisons et appartements.',
  keywords: ['immobilier', 'vente', 'location', 'maison', 'appartement', 'Cameroun'],
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="fr" suppressHydrationWarning className={inter.variable}>
      <body className="font-sans bg-white dark:bg-slate-900 text-slate-900 dark:text-white transition-colors duration-200">
        <Providers>
          <Navbar />
          <main>{children}</main>
          <Footer />
        </Providers>
      </body>
    </html>
  );
}
