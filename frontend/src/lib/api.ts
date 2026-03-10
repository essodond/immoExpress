import axios from 'axios';
import { Maison, Filters, AuthResponse, LoginCredentials, Admin } from '@/types';
import { getToken } from './auth';
import { DEMO_MAISONS } from './demoData';
import { DEMO_MODE } from './demoConfig';

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:5000/api',
  headers: { 'Content-Type': 'application/json' },
});

api.interceptors.request.use((config) => {
  const token = getToken();
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

api.interceptors.response.use(
  (res) => res,
  (err) => {
    if (
      err.response?.status === 401 &&
      typeof window !== 'undefined' &&
      window.location.pathname.startsWith('/admin') &&
      window.location.pathname !== '/admin/login'
    ) {
      window.location.href = '/admin/login';
    }
    return Promise.reject(err);
  }
);

export const getMaisons = async (filters?: Filters): Promise<Maison[]> => {
  // Mode démo : retourner les données statiques
  if (DEMO_MODE) {
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
  }

  // Mode production : appeler le backend
  const p = new URLSearchParams();
  if (filters?.ville)                     p.set('ville', filters.ville);
  if (filters?.type && filters.type !== 'tous') p.set('type', filters.type);
  if (filters?.prixMin)                   p.set('prixMin', String(filters.prixMin));
  if (filters?.prixMax)                   p.set('prixMax', String(filters.prixMax));
  if (filters?.chambres)                  p.set('chambres', String(filters.chambres));
  if (filters?.statut && filters.statut !== 'tous') p.set('statut', filters.statut);
  const { data } = await api.get<{ success: boolean; data: Maison[] }>(`/maisons?${p.toString()}`);
  return data.data || [];
};

export const getMaisonsFeatured = async (): Promise<Maison[]> => {
  if (DEMO_MODE) {
    return DEMO_MAISONS.slice(0, 3);
  }
  const { data } = await api.get<{ success: boolean; data: Maison[] }>('/maisons/featured');
  return data.data || [];
};

export const getMaison = async (id: string): Promise<Maison> => {
  if (DEMO_MODE) {
    const maison = DEMO_MAISONS.find(m => m.id === id);
    if (maison) return maison;
    throw new Error('Maison non trouvée');
  }
  const { data } = await api.get<{ success: boolean; data: Maison }>(`/maisons/${id}`);
  return data.data;
};

export const createMaison = async (d: Partial<Maison>): Promise<Maison> => {
  if (DEMO_MODE) {
    const newMaison: Maison = {
      id: String(DEMO_MAISONS.length + 1),
      titre: d.titre || 'Sans titre',
      description: d.description || '',
      prix: d.prix || 0,
      type: d.type || 'vente',
      ville: d.ville || '',
      quartier: d.quartier || '',
      chambres: d.chambres || 0,
      sallesBain: d.sallesBain || 0,
      superficie: d.superficie || 0,
      statut: d.statut || 'disponible',
      videoUrl: d.videoUrl || null,
      photos: [],
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
    };
    DEMO_MAISONS.push(newMaison);
    return newMaison;
  }
  const { data } = await api.post<{ success: boolean; data: Maison }>('/maisons', d);
  return data.data;
};

export const updateMaison = async (id: string, d: Partial<Maison>): Promise<Maison> => {
  if (DEMO_MODE) {
    const index = DEMO_MAISONS.findIndex(m => m.id === id);
    if (index !== -1) {
      DEMO_MAISONS[index] = { ...DEMO_MAISONS[index], ...d, updatedAt: new Date().toISOString() };
      return DEMO_MAISONS[index];
    }
    throw new Error('Maison non trouvée');
  }
  const { data } = await api.put<{ success: boolean; data: Maison }>(`/maisons/${id}`, d);
  return data.data;
};

export const deleteMaison = async (id: string): Promise<void> => {
  if (DEMO_MODE) {
    const index = DEMO_MAISONS.findIndex(m => m.id === id);
    if (index !== -1) {
      DEMO_MAISONS.splice(index, 1);
    }
    return;
  }
  await api.delete(`/maisons/${id}`);
};

export const uploadPhotos = async (maisonId: string, files: FileList): Promise<void> => {
  if (DEMO_MODE) {
    // En mode démo, simuler l'upload en utilisant des URLs de données
    const maison = DEMO_MAISONS.find(m => m.id === maisonId);
    if (maison) {
      Array.from(files).forEach((file, index) => {
        const reader = new FileReader();
        reader.onload = (e) => {
          const photo = {
            id: `photo-${Date.now()}-${index}`,
            url: e.target?.result as string,
            publicId: `immo/photo-${Date.now()}-${index}`,
            isMain: maison.photos.length === 0,
            maisonId: maisonId,
            createdAt: new Date().toISOString(),
          };
          maison.photos.push(photo);
        };
        reader.readAsDataURL(file);
      });
    }
    return;
  }
  const form = new FormData();
  Array.from(files).forEach((f) => form.append('photos', f));
  await api.post(`/upload/photos/${maisonId}`, form, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
};

export const deletePhoto = async (id: string): Promise<void> => {
  if (DEMO_MODE) {
    for (const maison of DEMO_MAISONS) {
      const photoIndex = maison.photos.findIndex(p => p.id === id);
      if (photoIndex !== -1) {
        maison.photos.splice(photoIndex, 1);
        break;
      }
    }
    return;
  }
  await api.delete(`/upload/photos/${id}`);
};

export const setMainPhoto = async (id: string): Promise<void> => {
  if (DEMO_MODE) {
    for (const maison of DEMO_MAISONS) {
      const photo = maison.photos.find(p => p.id === id);
      if (photo) {
        maison.photos.forEach(p => p.isMain = false);
        photo.isMain = true;
        break;
      }
    }
    return;
  }
  await api.put(`/upload/photos/${id}/main`);
};

export const login = async (creds: LoginCredentials): Promise<AuthResponse> => {
  if (DEMO_MODE) {
    // Mode démo : accepter credentials par défaut
    if (creds.email === 'admin@immo.com' && creds.password === 'Admin123!') {
      return {
        token: 'demo-token-' + Date.now(),
        admin: {
          id: '1',
          email: 'admin@immo.com',
          nom: 'Administrateur',
        },
      };
    }
    throw new Error('Identifiants invalides');
  }
  const { data } = await api.post<{ success: boolean; data: AuthResponse }>('/auth/login', creds);
  return data.data;
};

export const getMe = async (): Promise<{ admin: Admin }> => {
  if (DEMO_MODE) {
    return {
      admin: {
        id: '1',
        email: 'admin@immo.com',
        nom: 'Administrateur',
      },
    };
  }
  const { data } = await api.get<{ success: boolean; data: { admin: Admin } }>('/auth/me');
  return data.data;
};

export default api;
