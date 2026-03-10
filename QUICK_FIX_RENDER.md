# ⚡ QUICK FIX - 2 MINUTES

## 🔴 ERREUR
```
Module not found: Can't resolve '@/lib/api'
```

## ✅ SOLUTION RAPIDE

### 1. Push code
```bash
git add .
git commit -m "Fix Render build"
git push
```

### 2. Sur Render Dashboard
```
Settings → Build Command

Remplacer:
cd frontend && npm install && npm run build

Par:
cd frontend && npm ci && npm run build

Cliquez Save
```

### 3. Manual Deploy
```
Cliquez "Manual Deploy"
Attendez 3-5 min
C'est bon! ✅
```

---

## 🎉 FIN!

Votre site sera en ligne! 🚀

---

Consultez `RENDER_BUILD_FIX_FINAL.md` pour plus de détails.

