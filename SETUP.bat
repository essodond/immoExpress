@echo off
setlocal enabledelayedexpansion
title ImmoExpert - Installation automatique

echo.
echo ==============================================================
echo    IMMOEXPERT - Installation de la plateforme immobiliere
echo ==============================================================
echo.

:: Verifier que Python est installe
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERREUR] Python n'est pas installe ou pas dans le PATH.
    echo Installez Python depuis https://python.org
    pause
    exit /b 1
)

echo [1/4] Creation de la structure backend...
python "%~dp0setup_backend.py"
if %errorlevel% neq 0 (
    echo [ERREUR] La creation du backend a echoue.
    pause
    exit /b 1
)

echo.
echo [2/4] Creation de la structure frontend...
python "%~dp0setup.py"
if %errorlevel% neq 0 (
    echo [ERREUR] La creation du frontend a echoue.
    pause
    exit /b 1
)

echo.
echo [3/4] Installation des dependances backend...
cd /d "%~dp0backend"
where npm >nul 2>&1
if %errorlevel% equ 0 (
    npm install
) else (
    echo [AVERTISSEMENT] npm non trouve - installez Node.js puis lancez: cd backend ^&^& npm install
)

echo.
echo [4/4] Installation des dependances frontend...
cd /d "%~dp0frontend"
where npm >nul 2>&1
if %errorlevel% equ 0 (
    npm install
) else (
    echo [AVERTISSEMENT] npm non trouve - installez Node.js puis lancez: cd frontend ^&^& npm install
)

cd /d "%~dp0"

echo.
echo ==============================================================
echo    INSTALLATION TERMINEE!
echo ==============================================================
echo.
echo Prochaines etapes:
echo.
echo  1. Configurez le backend:
echo     cd backend
echo     copy .env.example .env
echo     (editez .env avec vos credentials PostgreSQL, Cloudinary, JWT)
echo.
echo  2. Initialisez la base de donnees:
echo     cd backend
echo     npx prisma migrate dev --name init
echo     node prisma/seed.js
echo.
echo  3. Configurez le frontend:
echo     cd frontend
echo     copy .env.local.example .env.local
echo     (editez .env.local - ajoutez votre numero WhatsApp)
echo.
echo  4. Demarrez les serveurs:
echo     Terminal 1: cd backend  ^&^& npm run dev   (port 5000)
echo     Terminal 2: cd frontend ^&^& npm run dev   (port 3000)
echo.
echo  5. Acces admin:
echo     URL: http://localhost:3000/admin/login
echo     Email: admin@immo.com
echo     Mot de passe: Admin123!
echo.
echo ==============================================================
echo.
pause
