# ⚡ SIMPLIFY - QUICK STEPS

## 🎯 SUPPRIMEZ CE QUI N'EST PAS NÉCESSAIRE

Ouvrez PowerShell dans `frontend/` et exécutez:

```powershell
# 1. Supprimer le dossier admin
rmdir /s /q src\app\admin

# 2. Supprimer les fichiers non utilisés
del src\lib\auth.ts
del src\lib\api.ts

# 3. Renommer le nouvel api
ren src\lib\api-simple.ts api.ts
```

---

## 📤 PUSH

```bash
git add .
git commit -m "Simplify: Remove admin - catalogue demo only"
git push origin main
```

---

## ✅ RÉSULTAT

```
✅ Build réussira
✅ Pas d'erreurs de modules
✅ Juste le catalogue fonctionne
✅ Site en ligne! 🚀
```

---

## 🎉 FIN!

Votre démo sera en ligne sans les complications!

