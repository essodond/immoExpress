# 🔧 Guide de Dépannage - ImmoExpert Démo

## ❓ Problèmes Courants et Solutions

---

## 1. ❌ "Le serveur ne démarre pas"

### Cause: Node.js n'est pas installé

**Solution:**
1. Téléchargez Node.js: https://nodejs.org/
2. Installez la version LTS
3. Redémarrez votre ordinateur
4. Relancez START_DEMO.bat

**Vérifier que Node.js est installé:**
```
Ouvrir CMD et taper: node --version
```

---

## 2. ❌ "Port 3000 is already in use"

### Cause: Un autre service utilise le port 3000

**Solution 1: Fermer l'application conflictuelle**
- Vérifiez si vous avez une autre instance de Next.js
- Fermez les autres applications web
- Fermez les autres navigateurs

**Solution 2: Vider le port**
```powershell
# Ouvrir PowerShell en administrateur
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

---

## 3. ❌ "npm: command not found"

### Cause: Node.js ou npm n'est pas dans le PATH

**Solution:**
1. Installez Node.js depuis: https://nodejs.org/
2. Redémarrez votre ordinateur
3. Relancez START_DEMO.bat

---

## 4. ❌ Le navigateur ne s'ouvre pas automatiquement

### Cause: Configuration du système

**Solution:**
Allez manuellement à: **http://localhost:3000**

---

## 5. ❌ "Erreur: Cannot find module"

### Cause: Les dépendances npm ne sont pas installées

**Solution:**
```bash
cd C:\Users\DELL\Documents\projet\immo\frontend
npm install
npm run dev
```

---

## 6. ❌ Les données disparaissent après rechargement

### Cause: Mode démo (normal!)

**C'est intentionnel!** La démo ne sauvegarde pas les données.

Pour les sauvegarder, vous avez besoin du backend réel:
1. Changer `DEMO_MODE = false` dans `frontend/src/lib/demoConfig.ts`
2. Lancer le backend
3. Relancer le frontend

---

## 7. ❌ Les photos ne s'ajoutent pas

### Cause: Mode démo simulé

**C'est normal!** Les photos sont converties en Data URLs.

Pour les uploads réels (Cloudinary):
1. Configurer le backend
2. Mettre à jour les clés Cloudinary
3. Changer `DEMO_MODE = false`

---

## 8. ❌ Erreur "ERR_NAME_NOT_RESOLVED" pour localhost

### Cause: Problème de connexion

**Solution:**
1. Vérifiez votre connexion Internet
2. Essayez: http://127.0.0.1:3000 (au lieu de localhost)
3. Redémarrez votre routeur

---

## 9. ❌ Le site est très lent

### Cause: Ressources insuffisantes ou cache plein

**Solution:**
1. Fermez les autres applications
2. Videz le cache du navigateur (Ctrl+Shift+Delete)
3. Redémarrez le navigateur
4. Relancez START_DEMO.bat

---

## 10. ❌ La connexion admin échoue

### Identifiants Corrects:
```
Email: admin@immo.com
Mot de passe: Admin123!
```

**Astuce**: Le mot de passe est sensible à la casse!

---

## 11. ❌ Les vidéos ne s'affichent pas

### Cause: Problème d'URL ou de connexion

**Solutions:**
1. Vérifiez que vous avez une connexion Internet
2. Les vidéos YouTube/TikTok doivent être publiques
3. Utilisez le lien embed, pas le lien normal

**Format correct:**
- YouTube: `https://www.youtube.com/embed/VIDEO_ID`
- TikTok: `https://www.tiktok.com/embed/v/VIDEO_ID`

---

## 12. ❌ La page est blanche

### Cause: Erreur JavaScript

**Solution:**
1. Ouvrez la console (F12)
2. Cherchez les erreurs rouges
3. Notez le message d'erreur
4. Redémarrez le serveur

---

## 13. ❌ "Cannot read property 'filter' of undefined"

### Cause: API ne retourne pas un tableau

**Solution:**
Vérifiez que `DEMO_MODE = true` dans `demoConfig.ts`

---

## 14. ❌ Impossible de créer/modifier un bien

### Cause: Erreur dans le formulaire

**Solution:**
1. Vérifiez tous les champs obligatoires
2. Les prix doivent être des nombres
3. Les dates doivent être au bon format

---

## 15. ❌ Le site plante sur mobile

### Cause: Problème de responsive design

**Solution:**
1. Videz le cache du navigateur
2. Forcez un rechargement (Ctrl+Shift+R)
3. Utilisez la mode responsive du navigateur (F12)

---

## 🔍 Comment Déboguer

### Ouvrir la Console Développeur:
```
Chrome/Edge: F12 ou Ctrl+Shift+J
Firefox: F12 ou Ctrl+Shift+K
Safari: Cmd+Option+I
```

### Vérifier les Erreurs:
1. Onglet **Console**
2. Cherchez les messages rouges
3. Notez le détail de l'erreur

### Inspecter les Éléments:
1. Onglet **Elements/Inspector**
2. Cliquez sur un élément
3. Vérifiez le HTML et CSS

---

## 🆘 Si Rien Ne Marche

### Réinitialisation Complète:

```bash
# 1. Arrêtez le serveur (Ctrl+C)

# 2. Supprimez les fichiers temporaires
cd C:\Users\DELL\Documents\projet\immo\frontend
rmdir /s /q node_modules

# 3. Réinstallez les dépendances
npm install

# 4. Lancez à nouveau
npm run dev
```

---

## 📞 Qui Contacter

Si le problème persiste:

1. Vérifiez la **console du navigateur** (F12)
2. Consultez les **fichiers de log** du serveur
3. Cherchez sur **Stack Overflow** avec le message d'erreur
4. Consultez la **documentation Next.js**: https://nextjs.org/

---

## ✅ Points de Vérification

Avant de rapporter un bug, vérifiez:

- [ ] Node.js est installé (`node --version`)
- [ ] npm est installé (`npm --version`)
- [ ] Port 3000 est disponible
- [ ] Vous êtes dans le bon répertoire
- [ ] `npm install` a fonctionné sans erreur
- [ ] `npm run dev` démarre sans erreur
- [ ] Vous avez vidé le cache du navigateur
- [ ] Vous êtes sur la bonne URL (http://localhost:3000)

---

**Besoin d'aide?** Consultez les fichiers:
- `DEMO_MODE.md` - Documentation complète
- `QUICK_START.md` - Guide rapide
- `PROJECT_STATUS.md` - État du projet

---

**Dernière mise à jour**: Mars 2026

