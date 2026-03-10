# Sécurité

## Signaler une Vulnérabilité

Si vous découvrez une vulnérabilité de sécurité, **ne l'ouvrez pas en issue publique**.

### Comment Signaler

1. **Email**: security@immoexpert.dev
2. **Décrivez la vulnérabilité**
3. **Fournissez des étapes pour la reproduire**
4. **Donnez-nous du temps pour corriger** (habituellement 48-72 heures)

### Ce Que Nous Faisons

- ✅ Accusons réception rapidement
- ✅ Confirmamos la vulnérabilité
- ✅ Travaillons sur un correctif
- ✅ Publions un correctif
- ✅ Vous crédite (si vous le souhaitez)

### Domaines de Sécurité

- Authentification & Autorisation
- Injection SQL
- XSS (Cross-Site Scripting)
- CSRF (Cross-Site Request Forgery)
- Fuite de données
- Dépendances obsolètes

## Bonnes Pratiques

- Gardez Node.js à jour
- Utilisez `npm audit` régulièrement
- Changez les identifiants par défaut
- Ne committez jamais de secrets
- Utilisez HTTPS en production

## Dépendances

Nous suivons les mises à jour de sécurité des dépendances :

```bash
npm audit
npm audit fix
```

Merci de nous aider à garder ImmoExpert sécurisé! 🔒

