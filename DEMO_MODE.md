# 🎬 Mode Démo - ImmoExpert

## Vue d'ensemble

Le mode **Démo** a été configuré pour vous permettre de tester l'application **sans avoir besoin du backend**. Toutes les données sont statiques et stockées en mémoire dans le frontend.

## ✨ Caractéristiques du Mode Démo

- ✅ **6 maisons de démonstration** pré-chargées
- ✅ **Connexion admin** fonctionnelle avec identifiants par défaut
- ✅ **Dashboard** affichant les statistiques
- ✅ **Filtrages** fonctionnels (par ville, type, prix, chambres, statut)
- ✅ **Galerie de photos** avec support de vidéos YouTube et TikTok
- ✅ **Gestion des photos** (upload simulé, suppression, définir comme principale)
- ✅ **CRUD complet** des maisons (créer, lire, modifier, supprimer)
- ✅ **Mode clair/sombre** fonctionnel
- ✅ **Bouton WhatsApp** intégré

## 🔑 Identifiants de Connexion Admin

```
Email: admin@immo.com
Mot de passe: Admin123!
```

## 🚀 Comment Démarrer

### 1. Lancer le Frontend

```bash
cd C:\Users\DELL\Documents\projet\immo\frontend
npm run dev
```

Le site sera accessible sur : **http://localhost:3000**

### 2. Accéder à l'Admin

1. Allez sur : http://localhost:3000/admin/login
2. Entrez les identifiants ci-dessus
3. Vous accédrez au dashboard avec les 6 maisons de démo

## 📊 Les 6 Maisons de Démo

### 1. Villa Moderne avec Piscine - Douala (45M FCFA)
- **Type**: Vente
- **Quartier**: Bonanjo
- **Chambres**: 4 | **Salles de bain**: 3 | **Superficie**: 250m²
- **Statut**: Disponible
- **Vidéo**: YouTube (exemple)

### 2. Appartement de Luxe - Yaoundé Centre (28M FCFA)
- **Type**: Vente
- **Quartier**: Centre
- **Chambres**: 3 | **Salles de bain**: 2 | **Superficie**: 180m²
- **Statut**: Disponible

### 3. Maison Familiale - Douala, Bonakuma (22M FCFA)
- **Type**: Vente
- **Quartier**: Bonakuma
- **Chambres**: 3 | **Salles de bain**: 2 | **Superficie**: 200m²
- **Statut**: Disponible

### 4. Studio Meublé - Douala, Akwa (3.5M FCFA/mois)
- **Type**: Location
- **Quartier**: Akwa
- **Chambres**: 1 | **Salles de bain**: 1 | **Superficie**: 45m²
- **Statut**: Loué

### 5. Terrain Constructible - Yaoundé Plateau (15M FCFA)
- **Type**: Vente
- **Quartier**: Plateau
- **Superficie**: 500m²
- **Statut**: Vendu

### 6. Duplex Moderne - Douala, Deido (55M FCFA)
- **Type**: Vente
- **Quartier**: Deido
- **Chambres**: 5 | **Salles de bain**: 4 | **Superficie**: 350m²
- **Statut**: Disponible
- **Vidéo**: YouTube (exemple)

## 🎮 Fonctionnalités Testables

### Dashboard Admin
- [ ] Voir les statistiques (total, disponibles, vendus, loués)
- [ ] Afficher la liste des biens récents
- [ ] Créer une nouvelle maison
- [ ] Voir les détails d'une maison

### Catalogue Publique
- [ ] Afficher tous les biens disponibles
- [ ] Filtrer par ville, type (vente/location), prix, chambres
- [ ] Voir les détails d'une maison avec photos et vidéos

### Gestion des Photos (Admin)
- [ ] Upload de photos (simulé en mode démo)
- [ ] Supprimer une photo
- [ ] Définir une photo comme principale
- [ ] Voir les photos dans la galerie

### Gestion des Vidéos
- [ ] Ajouter un lien vidéo YouTube
- [ ] Ajouter un lien vidéo TikTok
- [ ] Afficher les vidéos en mode responsive

## 🔧 Configuration du Mode Démo

Le mode démo est **activé par défaut**. Pour le désactiver et utiliser le backend réel :

### Fichier: `frontend/src/lib/demoConfig.ts`

```typescript
// Mettre à false pour utiliser le backend réel
export const DEMO_MODE = false;
```

## 📝 Notes Importantes

1. **Données en mémoire** : Les modifications sont perdues au rechargement de la page
2. **Upload de photos** : Les photos sont converties en Data URLs et stockées en mémoire
3. **Pas de persistance** : Aucune donnée n'est sauvegardée
4. **Authentification simplifié** : Accepte uniquement les identifiants par défaut

## 🎯 Cas d'Utilisation

- ✅ **Démo client** : Montrer le produit sans configuration serveur
- ✅ **Développement frontend** : Travailler sur l'UI sans dépendre du backend
- ✅ **Tests E2E** : Scénarios de test prédéfinis
- ✅ **Prototype** : Présentation rapide des fonctionnalités

## 🔄 Migration vers le Backend Réel

Quand vous êtes prêt à utiliser le backend réel :

1. Lancez le backend : `cd backend && npm run dev`
2. Changez `DEMO_MODE` à `false` dans `demoConfig.ts`
3. Redémarrez le frontend
4. Les appels API iront vers votre backend

## 📞 Support

Pour toute question ou problème avec le mode démo, veuillez consulter la documentation du projet.

---

**Mode Démo Version**: 1.0  
**Dernier mise à jour**: Mars 2026

