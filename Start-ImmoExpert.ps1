#!/usr/bin/env powershell
# ImmoExpert - Script de démarrage avec vérifications

$SCRIPT_PATH = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $SCRIPT_PATH

Write-Host "`n" -ForegroundColor Green
Write-Host "╔════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  ImmoExpert - Plateforme Immo    ║" -ForegroundColor Cyan
Write-Host "║  Démarrage des Services           ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host "`n"

# Vérifications préalables
Write-Host "[1/5] Vérification de la structure du projet..." -ForegroundColor Yellow
$checks = @("backend\package.json", "frontend\package.json", "backend\prisma\dev.db")
foreach ($file in $checks) {
    if (Test-Path $file) {
        Write-Host "  ✓ $file" -ForegroundColor Green
    } else {
        Write-Host "  ✗ $file - MANQUANT" -ForegroundColor Red
    }
}

# Arrêter les anciens processus
Write-Host "`n[2/5] Nettoyage des processus Node précédents..." -ForegroundColor Yellow
$nodeProcesses = Get-Process node -ErrorAction SilentlyContinue
if ($nodeProcesses) {
    Write-Host "  Arrêt de $(($nodeProcesses | Measure-Object).Count) processus Node..." -ForegroundColor Yellow
    Stop-Process -Name node -Force -ErrorAction SilentlyContinue
    Start-Sleep -Seconds 2
    Write-Host "  ✓ Processus fermés" -ForegroundColor Green
} else {
    Write-Host "  ✓ Aucun processus Node à arrêter" -ForegroundColor Green
}

# Démarrer le backend
Write-Host "`n[3/5] Démarrage du Backend (Express.js - Port 5001)..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$SCRIPT_PATH\backend'; npm run dev" -WindowTitle "ImmoExpert Backend"
Start-Sleep -Seconds 4
Write-Host "  ✓ Backend en cours de démarrage" -ForegroundColor Green

# Démarrer le frontend
Write-Host "`n[4/5] Démarrage du Frontend (Next.js - Port 3000)..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$SCRIPT_PATH\frontend'; npm run dev" -WindowTitle "ImmoExpert Frontend"
Start-Sleep -Seconds 8
Write-Host "  ✓ Frontend en cours de démarrage" -ForegroundColor Green

# Vérification des ports
Write-Host "`n[5/5] Vérification des services..." -ForegroundColor Yellow
Start-Sleep -Seconds 2

$backend_active = Get-Process node -ErrorAction SilentlyContinue | Select-Object -First 1
$frontend_active = Get-Process node -ErrorAction SilentlyContinue | Select-Object -Last 1

Write-Host "`n"
Write-Host "╔════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║     Services Démarrés avec Succès   ║" -ForegroundColor Green
Write-Host "╚════════════════════════════════════╝" -ForegroundColor Green
Write-Host "`n"

Write-Host "🌐 Frontend  : " -ForegroundColor Cyan -NoNewLine
Write-Host "http://localhost:3000" -ForegroundColor White

Write-Host "🔌 Backend   : " -ForegroundColor Cyan -NoNewLine
Write-Host "http://localhost:5001" -ForegroundColor White

Write-Host "🏠 Admin     : " -ForegroundColor Cyan -NoNewLine
Write-Host "http://localhost:3000/admin/login" -ForegroundColor White

Write-Host "`n📝 Credentials Admin:" -ForegroundColor Yellow
Write-Host "   Email    : admin@immo.com" -ForegroundColor White
Write-Host "   Password : Admin123!" -ForegroundColor White

Write-Host "`n⚠️  IMPORTANT: Changez le mot de passe admin après la première connexion!" -ForegroundColor Red
Write-Host "`n💾 Base de données: SQLite (backend/prisma/dev.db)" -ForegroundColor Magenta
Write-Host "`n"

Write-Host "Les serveurs tournent dans d'autres fenêtres PowerShell. Fermez-les pour arrêter les services." -ForegroundColor Gray

