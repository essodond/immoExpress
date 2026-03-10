# 🚀 DÉPLOYER IMMOEXPERT SUR RENDER - GUIDE COMPLET

## ✅ AVANT DE COMMENCER

- [ ] Compte GitHub créé
- [ ] Repository `immo` pushé sur GitHub
- [ ] Code en bon état
- [ ] Fichier `.env.local` CONFIGURÉ

---

## 📋 ÉTAPES DE DÉPLOIEMENT

### ÉTAPE 1: Créer un compte Render
1. Allez sur: https://render.com
2. Cliquez "Sign Up"
3. Inscrivez-vous avec **GitHub**
4. Autorisez Render à accéder à vos repositories

### ÉTAPE 2: Créer un nouveau service
1. Dashboard Render
2. Cliquez "New +" (en haut à droite)
3. Sélectionnez "Web Service"

### ÉTAPE 3: Configurer le repository
1. Repository: Cherchez **immo**
2. Branche: **main**
3. Cliquez "Connect"

### ÉTAPE 4: Configurer le service
**Remplissez les champs:**

```
Name: immoexpert (ou ce que vous voulez)
Environment: Node
Build Command: cd frontend && npm install && npm run build
Start Command: cd frontend && npm start
Plan: Free (ou Starter si vous avez besoin 24/7)
```

### ÉTAPE 5: Variables d'environnement
1. Scroll down jusqu'à "Environment"
2. Ajouter les variables:

```
NODE_ENV = production
NEXT_PUBLIC_API_URL = http://localhost:5000/api
NEXT_PUBLIC_WHATSAPP_NUMBER = +22871608097
```

### ÉTAPE 6: Déployer
1. Cliquez "Create Web Service"
2. Attendez la compilation (~2-3 minutes)
3. Vérifiez les logs
4. Allez à votre URL (elle s'affichera sur le dashboard)

---

## 🎯 URL DE VOTRE SITE

```
https://immoexpert.onrender.com
(ou le nom que vous avez choisi)
```

---

## ✅ APRÈS DÉPLOIEMENT - CHECKLIST

```
[ ] Site accessible: https://votre-url.onrender.com
[ ] Accueil charge sans erreur
[ ] Images s'affichent correctement
[ ] Navigation fonctionne
[ ] Boutons WhatsApp fonctionnent
[ ] Catalogue charge les 6 maisons
[ ] Dark mode fonctionne
[ ] Mobile responsive OK
```

---

## 🔧 PROBLÈMES COURANTS

### ❌ "Build failed"
**Solution:**
1. Vérifiez les logs
2. Assurez-vous que `package.json` existe dans `frontend/`
3. Vérifiez que les dépendances sont correctes

### ❌ "Port already in use"
**Solution:**
```
Start Command: cd frontend && npm start -- -p $PORT
```

### ❌ "Images ne s'affichent pas"
**Solution:**
- Images de Unsplash: Vérifiez votre connexion
- Assurez-vous que NEXT_PUBLIC_API_URL est correct

### ❌ "Site va en veille"
**Solution:**
- Plan Free: Normal (15 min inactivité)
- Passer à plan Starter pour 24/7

---

## 📱 TESTER EN PRODUCTION

1. Visitez votre URL
2. Testez les fonctionnalités:
   - Catalogue
   - Filtres
   - Détails
   - WhatsApp
   - Dark mode

---

## 🔄 MISES À JOUR

**Pour déployer les changements:**
```bash
git add .
git commit -m "Update: ..."
git push origin main
```

Render se redéploiera automatiquement! 🚀

---

## 💡 ASTUCES

✅ **Logs**: Cliquez sur "Logs" pour voir les erreurs
✅ **Redémarrer**: Cliquez "Manual Deploy" pour forcer
✅ **Custom Domain**: Allez dans Settings pour ajouter votre domaine
✅ **Environment**: Modifiez les variables sans redéployer

---

## 🎊 C'EST FAIT!

Votre ImmoExpert est maintenant en ligne! 🎉

**URL finale**: https://votre-url.onrender.com

Partagez-la avec vos clients! 🌍

---

**Besoin d'aide?** Consultez: https://render.com/docs

