#!/bin/bash

# Supprimer le dossier admin qui n'est pas nécessaire
echo "🗑️ Removing admin folder..."
rm -rf src/app/admin

# Supprimer les fichiers non utilisés
echo "🗑️ Removing unnecessary lib files..."
rm -f src/lib/auth.ts
rm -f src/lib/api.ts  # We don't need the API - we use demoData

echo "✅ Cleanup complete!"

