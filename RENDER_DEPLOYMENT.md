# Render Configuration pour ImmoExpert

## 🚀 Déploiement sur Render

### 1. FRONTEND (Next.js)

**Type**: Static Site (ou Web Service)
**Build Command**: 
```
cd frontend && npm install && npm run build
```

**Start Command** (si Web Service):
```
cd frontend && npm start
```

**Publish Directory**: `frontend/.next`

**Environment Variables**:
```
NODE_ENV=production
NEXT_PUBLIC_API_URL=https://votre-backend-url.onrender.com/api
NEXT_PUBLIC_WHATSAPP_NUMBER=+22871608097
```

---

### 2. BACKEND (Express.js) - Optionnel

**Type**: Web Service
**Build Command**:
```
cd backend && npm install
```

**Start Command**:
```
cd backend && npm start
```

**Environment Variables**:
```
NODE_ENV=production
DATABASE_URL=postgresql://user:password@host:port/database
JWT_SECRET=votre-secret-jwt
PORT=10000
```

---

## 📋 ÉTAPES DE DÉPLOIEMENT

### 1. Créer un compte Render
- Allez sur: https://render.com
- Inscrivez-vous avec GitHub

### 2. Connecter GitHub
- Autorisez Render à accéder à votre repository
- Sélectionnez votre repository `immo`

### 3. Créer le service Frontend
- New+ → Web Service
- Repository: immo
- Branch: main
- Build Command: `cd frontend && npm install && npm run build`
- Start Command: `cd frontend && npm start`
- Plan: Free ou Starter
- Déployer

### 4. Configurer les variables d'environnement
- Settings → Environment
- Ajouter:
  ```
  NODE_ENV=production
  NEXT_PUBLIC_API_URL=http://localhost:5000/api (pour développement local)
  NEXT_PUBLIC_WHATSAPP_NUMBER=+22871608097
  ```

### 5. Déployer
- Cliquez "Deploy"
- Attendez la compilation

---

## ✅ VÉRIFICATION APRÈS DÉPLOIEMENT

- [ ] Le site charge sans erreur
- [ ] Les images s'affichent
- [ ] Les vidéos YouTube se chargent
- [ ] Les boutons WhatsApp fonctionnent
- [ ] La navigation fonctionne
- [ ] Le dark mode fonctionne
- [ ] Mobile responsive

---

## 🎯 URL APRÈS DÉPLOIEMENT

```
https://votre-app-name.onrender.com
```

---

## 📝 NOTES IMPORTANTES

1. **Render free**: Mises en veille après 15 min d'inactivité
2. **Render paid**: Service 24/7
3. **Build time**: ~2-3 minutes
4. **Base de données**: Ajouter PostgreSQL si besoin

---

**Bonne chance! 🚀**

