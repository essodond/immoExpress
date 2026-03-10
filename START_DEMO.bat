@echo off
REM Script pour lancer ImmoExpert en mode démo

echo.
echo ======================================
echo   🏠 ImmoExpert - Mode Démo
echo ======================================
echo.
echo Lancement du serveur frontend...
echo.

cd frontend

REM Vérifier si node_modules existe
if not exist "node_modules" (
    echo Installation des dépendances...
    call npm install
)

echo.
echo ✅ Démarrage de Next.js...
echo.
echo 🌐 Accès au site: http://localhost:3000
echo 🔐 Admin (tableau de bord): http://localhost:3000/admin/login
echo.
echo Email: admin@immo.com
echo Password: Admin123!
echo.
echo Appuyez sur CTRL+C pour arrêter le serveur.
echo.

npm run dev

