export interface Photo {
  id: string;
  url: string;
  publicId: string;
  isMain: boolean;
  maisonId: string;
  createdAt: string;
}

export interface Maison {
  id: string;
  titre: string;
  description: string;
  prix: number;
  type: 'vente' | 'location';
  ville: string;
  quartier: string;
  chambres: number;
  sallesBain: number;
  superficie: number;
  statut: 'disponible' | 'vendu' | 'loue';
  videoUrl?: string | null;
  photos: Photo[];
  createdAt: string;
  updatedAt: string;
}

export interface Filters {
  ville?: string;
  type?: string;
  prixMin?: number;
  prixMax?: number;
  chambres?: number;
  statut?: string;
}

export interface Admin {
  id: string;
  email: string;
  nom: string;
}

export interface LoginCredentials {
  email: string;
  password: string;
}

export interface AuthResponse {
  token: string;
  admin: Admin;
}
