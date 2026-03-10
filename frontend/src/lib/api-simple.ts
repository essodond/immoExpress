import { DEMO_MAISONS } from './demoData';
import { Maison, Filters } from '@/types';

/**
 * API simplifié pour la démo - CATALOGUE UNIQUEMENT
 * Pas d'authentification, pas d'upload, juste les données statiques
 */

export const getMaisons = async (filters?: Filters): Promise<Maison[]> => {
  // Simulation d'un délai réseau
  await new Promise(resolve => setTimeout(resolve, 100));

  let result = [...DEMO_MAISONS];

  if (filters?.ville) {
    result = result.filter(m => m.ville.toLowerCase().includes(filters.ville!.toLowerCase()));
  }
  if (filters?.type && filters.type !== 'tous') {
    result = result.filter(m => m.type === filters.type);
  }
  if (filters?.prixMin) {
    result = result.filter(m => m.prix >= filters.prixMin!);
  }
  if (filters?.prixMax) {
    result = result.filter(m => m.prix <= filters.prixMax!);
  }
  if (filters?.chambres) {
    result = result.filter(m => m.chambres >= filters.chambres!);
  }
  if (filters?.statut && filters.statut !== 'tous') {
    result = result.filter(m => m.statut === filters.statut);
  }

  return result;
};

export const getMaisonsFeatured = async (): Promise<Maison[]> => {
  await new Promise(resolve => setTimeout(resolve, 100));
  return DEMO_MAISONS.slice(0, 3);
};

export const getMaison = async (id: string): Promise<Maison> => {
  await new Promise(resolve => setTimeout(resolve, 100));
  const maison = DEMO_MAISONS.find(m => m.id === id);
  if (!maison) throw new Error('Maison not found');
  return maison;
};

export default null;

