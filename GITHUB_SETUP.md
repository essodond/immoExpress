# GitHub Template - ImmoExpert

Utilisez ce template pour créer votre repository GitHub.

## Étapes pour Ajouter à GitHub

### 1. Créer un Repository sur GitHub

1. Allez sur https://github.com/new
2. Nom: `immo` ou `immoexpert`
3. Description: "Plateforme complète de gestion immobilière"
4. Visibilité: Public ou Private (selon vos préférences)
5. **NE COCHEZ PAS** "Initialize with README" (nous l'avons déjà)
6. Créez le repository

### 2. Initialiser Git Localement

```bash
cd C:\Users\DELL\Documents\projet\immo

# Initialiser Git
git init

# Ajouter tous les fichiers
git add .

# Commit initial
git commit -m "feat: Initial commit - ImmoExpert complete demo"
```

### 3. Connecter à GitHub

```bash
# Remplacez YOUR_USERNAME et YOUR_REPO
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 4. Vérifier sur GitHub

Visitez: https://github.com/YOUR_USERNAME/YOUR_REPO

Vous devriez voir tous vos fichiers!

---

## Fichiers Importants pour GitHub

✅ **README.md** - Présentation du projet
✅ **.gitignore** - Fichiers à ignorer
✅ **LICENSE** - Licence MIT
✅ **CONTRIBUTING.md** - Guide de contribution
✅ **SECURITY.md** - Politique de sécurité
✅ **CHANGELOG.md** - Historique des versions

---

## Structure du Repository

```
immoexpert/
├── frontend/              # Application Next.js
├── backend/               # API Express
├── README.md              # Documentation principale
├── CONTRIBUTING.md        # Guide de contribution
├── LICENSE                # MIT License
├── SECURITY.md            # Politique sécurité
├── CHANGELOG.md           # Historique versions
├── .gitignore             # Fichiers ignorés
├── package.json           # Configuration npm
├── INSTRUCTIONS_FINALES.md
├── DEMO_MODE.md
├── QUICK_START.md
└── ...
```

---

## Commandes Git Utiles

### Après avoir poussé le code

```bash
# Voir le statut
git status

# Voir l'historique
git log

# Créer une branche
git checkout -b feature/ma-feature

# Pousser une branche
git push origin feature/ma-feature
```

### Mettre à jour le code local

```bash
# Récupérer les changements
git pull origin main

# Voir les différences
git diff
```

---

## Configuration Recommandée sur GitHub

### Paramètres du Repository

1. **Settings → General**
   - Description: "Plateforme de gestion immobilière"
   - Website: Votre site (optionnel)

2. **Settings → Branches**
   - Default branch: `main`
   - Add branch protection rule:
     - Branch name: `main`
     - Require pull request reviews

3. **Settings → Actions**
   - Activer GitHub Actions pour CI/CD

4. **Settings → Pages** (optionnel)
   - Déployer la documentation sur GitHub Pages

---

## GitHub Actions (Optionnel)

Créer `.github/workflows/ci.yml`:

```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v2
      
      - uses: actions/setup-node@v2
        with:
          node-version: 16
      
      - name: Install dependencies
        run: npm run install:all
      
      - name: Build
        run: npm run build:frontend
```

---

## Badges pour le README

Ajoutez ces badges au README:

```markdown
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node.js](https://img.shields.io/badge/Node.js-16+-green.svg)](https://nodejs.org/)
[![Next.js](https://img.shields.io/badge/Next.js-14-black.svg)](https://nextjs.org/)
```

---

## Collaboration

### Inviter des Collaborateurs

1. Settings → Collaborators
2. Ajouter les usernames GitHub
3. Choisir le niveau d'accès (Push, Maintain, Admin)

---

## Prochaines Étapes

- [ ] Créer le repository sur GitHub
- [ ] Pousser le code
- [ ] Ajouter des collaborateurs
- [ ] Configurer les protections de branche
- [ ] Ajouter les issues et milestones
- [ ] Configurer GitHub Pages (optionnel)

---

**Besoin d'aide?** Consultez: https://docs.github.com

**Prêt?** Commencez par l'étape 1! 🚀

