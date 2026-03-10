@echo off
REM ImmoExpert - Script de démarrage rapide

echo.
echo ====================================
echo  ImmoExpert - Plateforme Immobiliere
echo ====================================
echo.

REM Vérifier que nous sommes dans le bon répertoire
if not exist "backend\package.json" (
    echo ERREUR: Assurez-vous d'être dans le dossier racine du projet
    pause
    exit /b 1
)

echo [1/3] Démarrage du Backend (Express.js sur port 5001)...
echo.

REM Ouvrir le backend dans une nouvelle fenêtre
start "ImmoExpert Backend" cmd /k "cd backend && npm run dev"

echo [2/3] Attente du démarrage du backend (5 secondes)...
timeout /t 5 /nobreak

echo [3/3] Démarrage du Frontend (Next.js sur port 3000)...
echo.

REM Ouvrir le frontend dans une nouvelle fenêtre
start "ImmoExpert Frontend" cmd /k "cd frontend && npm run dev"

echo.
echo ====================================
echo  ✓ Services en cours de démarrage
echo ====================================
echo.
echo Frontend  : http://localhost:3000
echo Backend   : http://localhost:5001
echo Admin     : http://localhost:3000/admin/login
echo.
echo Credentials Admin:
echo   Email    : admin@immo.com
echo   Password : Admin123!
echo.
pause

