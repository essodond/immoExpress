# Script pour lancer ImmoExpert en mode démo

Write-Host ""
Write-Host "======================================"
Write-Host "  🏠 ImmoExpert - Mode Démo"
Write-Host "======================================"
Write-Host ""
Write-Host "Lancement du serveur frontend..."
Write-Host ""

Set-Location 'C:\Users\DELL\Documents\projet\immo\frontend'

# Vérifier si node_modules existe
if (-not (Test-Path 'node_modules')) {
    Write-Host "Installation des dépendances..."
    & npm install
}

Write-Host ""
Write-Host "✅ Démarrage de Next.js..."
Write-Host ""
Write-Host "🌐 Accès au site: http://localhost:3000"
Write-Host "🔐 Admin (tableau de bord): http://localhost:3000/admin/login"
Write-Host ""
Write-Host "Email: admin@immo.com"
Write-Host "Password: Admin123!"
Write-Host ""
Write-Host "Appuyez sur CTRL+C pour arrêter le serveur."
Write-Host ""

& npm run dev

