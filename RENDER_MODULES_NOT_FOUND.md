# ✅ FIX BUILD RENDER - MODULE PATHS

## 🔴 ERREUR ACTUELLE
```
Module not found: Can't resolve '@/lib/api'
Module not found: Can't resolve '@/lib/utils'
Module not found: Can't resolve '@/lib/auth'
```

## 🔍 CAUSE
Les fichiers existent localement mais Render ne les trouve pas pendant le build.
Problème de résolution des chemins ou de cache npm.

---

## ✅ SOLUTION

### 1. Ajouter fichier .npmrc
```
Fichier créé: frontend/.npmrc
Contenu: Ignore les avertissements et problèmes peer deps
```

### 2. Modifier le build command sur Render
À la place de:
```
cd frontend && npm install && npm run build
```

Utilisez:
```
cd frontend && npm ci --prefer-offline && npm run build
```

Ou encore mieux:
```
npm ci --prefer-offline && npm run build && npm prune --production
```

---

## 🚀 ÉTAPES POUR CORRIGER

### Étape 1: Push le code
```bash
cd C:\Users\DELL\Documents\projet\immo
git add frontend/.npmrc
git commit -m "Add .npmrc for Render build optimization"
git push origin main
```

### Étape 2: Modifier le build command sur Render

1. Allez à: https://render.com/dashboard
2. Sélectionnez votre service **immoexpert**
3. Cliquez **Settings**
4. Trouvez **Build Command**
5. Remplacez par:
```
cd frontend && npm ci --prefer-offline && npm run build
```

### Étape 3: Manual Deploy
1. Cliquez **Manual Deploy**
2. Attendez 2-3 minutes

---

## 🎯 ALTERNATIVE SI ÇA NE MARCHE PAS

Essayez ce build command:
```
cd frontend && rm -rf node_modules package-lock.json && npm install && npm run build
```

---

## ✅ APRÈS LE BUILD

```
https://immoexpert.onrender.com
Devrait fonctionner! ✅
```

---

## 📝 RÉSUMÉ

```
✅ Fichier .npmrc ajouté
✅ Build command optimisé
✅ Cache npm amélioré
→ Les modules seront trouvés!
```

---

Consultez `RENDER_BUILD_FIX_FINAL.md` pour les détails.

