# ImmoExpert — Plateforme Immobilière Professionnelle

Une plateforme immobilière fullstack complète construite avec **Next.js 14**, **Express.js**, **PostgreSQL** et **Cloudinary**.

---

## 🚀 Installation rapide

### Prérequis
- [Node.js](https://nodejs.org) v18+
- [Python](https://python.org) 3.8+
- [PostgreSQL](https://postgresql.org) 14+
- Un compte [Cloudinary](https://cloudinary.com) (gratuit)

### Étape 1 — Générer le projet

Double-cliquez sur `SETUP.bat` **ou** depuis un terminal :

```cmd
cd C:\Users\DELL\Documents\projet\immo
python setup_backend.py
python setup.py
```

### Étape 2 — Configurer le backend

```cmd
cd backend
copy .env.example .env
```

Éditez `.env` :
```env
DATABASE_URL="postgresql://postgres:motdepasse@localhost:5432/immo_db"
JWT_SECRET="une-cle-secrete-longue-et-aleatoire-ici"
JWT_EXPIRES_IN="7d"
CLOUDINARY_CLOUD_NAME="votre-cloud-name"
CLOUDINARY_API_KEY="votre-api-key"
CLOUDINARY_API_SECRET="votre-api-secret"
FRONTEND_URL="http://localhost:3000"
PORT=5000
```

### Étape 3 — Initialiser la base de données

```cmd
cd backend
npm install
npx prisma migrate dev --name init
node prisma/seed.js
```

### Étape 4 — Configurer le frontend

```cmd
cd frontend
copy .env.local.example .env.local
```

Éditez `.env.local` :
```env
NEXT_PUBLIC_API_URL=http://localhost:5000/api
NEXT_PUBLIC_WHATSAPP_NUMBER=+237600000000
```

```cmd
npm install
```

### Étape 5 — Démarrer les serveurs

**Terminal 1 (Backend) :**
```cmd
cd backend
npm run dev
```
> API disponible sur http://localhost:5000

**Terminal 2 (Frontend) :**
```cmd
cd frontend
npm run dev
```
> Site disponible sur http://localhost:3000

---

## 🔐 Accès Administrateur

| URL | `http://localhost:3000/admin/login` |
|-----|-------------------------------------|
| Email | `admin@immo.com` |
| Mot de passe | `Admin123!` |

> ⚠️ **Changez le mot de passe après la première connexion !**

---

## 📁 Structure du projet

```
immo/
├── backend/                    # API Express.js
│   ├── prisma/
│   │   ├── schema.prisma       # Modèles DB (Maison, Photo, Admin)
│   │   └── seed.js             # Données initiales (admin par défaut)
│   ├── src/
│   │   ├── controllers/        # Logique métier
│   │   │   ├── authController.js
│   │   │   ├── maisonController.js
│   │   │   └── uploadController.js
│   │   ├── middleware/
│   │   │   ├── authMiddleware.js  # Protection JWT
│   │   │   ├── errorHandler.js
│   │   │   └── validate.js
│   │   ├── routes/
│   │   │   ├── auth.js
│   │   │   ├── maisons.js
│   │   │   └── upload.js
│   │   ├── utils/
│   │   │   ├── cloudinary.js   # Upload/suppression photos
│   │   │   └── jwt.js
│   │   └── server.js           # Point d'entrée Express
│   └── package.json
│
└── frontend/                   # Application Next.js 14
    └── src/
        ├── app/
        │   ├── page.tsx                      # Page d'accueil
        │   ├── catalogue/page.tsx            # Liste des annonces
        │   ├── maison/[id]/page.tsx          # Détail d'un bien
        │   ├── a-propos/page.tsx             # Page À Propos
        │   └── admin/                        # Dashboard admin
        │       ├── login/page.tsx
        │       ├── dashboard/page.tsx
        │       └── maisons/
        │           ├── page.tsx              # Gérer les biens
        │           ├── nouvelle/page.tsx     # Créer un bien
        │           └── [id]/page.tsx         # Modifier un bien
        ├── components/
        │   ├── layout/                       # Navbar, Footer
        │   ├── maison/                       # MaisonCard, Galerie, Filtres, Form
        │   └── ui/                           # Badge, WhatsApp, ThemeToggle
        ├── lib/                              # API client, auth, utils
        ├── types/                            # TypeScript interfaces
        └── providers/                        # Theme + React Query
```

---

## 🌐 API REST — Endpoints

### Public (sans authentification)
| Méthode | Route | Description |
|---------|-------|-------------|
| GET | `/api/health` | Statut de l'API |
| GET | `/api/maisons` | Liste des biens (avec filtres) |
| GET | `/api/maisons/featured` | 6 derniers biens disponibles |
| GET | `/api/maisons/:id` | Détail d'un bien |

**Filtres disponibles :** `?ville=Douala&type=vente&prixMin=5000000&prixMax=50000000&chambres=3&statut=disponible`

### Admin (authentification JWT requise)
| Méthode | Route | Description |
|---------|-------|-------------|
| POST | `/api/auth/login` | Connexion admin |
| GET | `/api/auth/me` | Profil admin |
| POST | `/api/maisons` | Créer un bien |
| PUT | `/api/maisons/:id` | Modifier un bien |
| DELETE | `/api/maisons/:id` | Supprimer un bien |
| POST | `/api/upload/photos/:maisonId` | Uploader des photos |
| DELETE | `/api/upload/photos/:photoId` | Supprimer une photo |
| PUT | `/api/upload/photos/:photoId/main` | Définir la photo principale |

---

## 🛠️ Technologies

| Couche | Technologies |
|--------|-------------|
| Frontend | Next.js 14, TypeScript, TailwindCSS, TanStack Query |
| Backend | Express.js, Prisma ORM, Zod validation |
| Base de données | PostgreSQL |
| Médias | Cloudinary |
| Auth | JWT (jsonwebtoken + bcryptjs) |
| UI | lucide-react, next-themes, react-hot-toast |

---

## 🌙 Mode Sombre / Clair

Le mode sombre est intégré via `next-themes`. Le bouton toggle est disponible dans la navbar.

---

## 📱 Contact WhatsApp

Configurez votre numéro WhatsApp dans `.env.local` :
```env
NEXT_PUBLIC_WHATSAPP_NUMBER=+237600000000
```

Le bouton WhatsApp génère automatiquement des messages personnalisés selon le contexte (accueil, fiche bien, à propos).

---

## 🚀 Déploiement

### Backend (ex: Railway, Render, Heroku)
```cmd
cd backend
npm run build  # (si nécessaire)
npm start
```

### Frontend (ex: Vercel)
```cmd
cd frontend
npm run build
```
Configurez les variables d'environnement sur votre plateforme de déploiement.

---

## 📞 Support

Pour toute question, contactez l'agent immobilier via WhatsApp : **+237600000000**

---

*Développé avec ❤️ pour ImmoExpert*
