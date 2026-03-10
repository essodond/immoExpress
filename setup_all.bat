@echo off
setlocal enabledelayedexpansion

cd /d "C:\Users\DELL\Documents\projet\immo"

REM Create directories for backend
mkdir "backend\src\utils" 2>nul
mkdir "backend\src\middleware" 2>nul
mkdir "backend\src\controllers" 2>nul
mkdir "backend\src\routes" 2>nul
mkdir "backend\prisma" 2>nul

REM Create directories for frontend
mkdir "frontend\src\app\catalogue" 2>nul
mkdir "frontend\src\app\maison\[id]" 2>nul
mkdir "frontend\src\app\a-propos" 2>nul
mkdir "frontend\src\app\admin\login" 2>nul
mkdir "frontend\src\app\admin\dashboard" 2>nul
mkdir "frontend\src\app\admin\maisons\nouvelle" 2>nul
mkdir "frontend\src\app\admin\maisons\[id]" 2>nul
mkdir "frontend\src\components\layout" 2>nul
mkdir "frontend\src\components\maison" 2>nul
mkdir "frontend\src\components\ui" 2>nul
mkdir "frontend\src\lib" 2>nul
mkdir "frontend\src\types" 2>nul
mkdir "frontend\src\providers" 2>nul
mkdir "frontend\public" 2>nul

echo Directories created successfully!

REM Now run the Python scripts
echo.
echo ============================================================
echo Running Python setup scripts...
echo ============================================================
echo.

python setup_backend.py
echo [1/3] setup_backend.py completed with code: %ERRORLEVEL%
echo.

python create_dirs.py
echo [2/3] create_dirs.py completed with code: %ERRORLEVEL%
echo.

if exist create_dirs.js (
    node create_dirs.js
    echo [3/3] create_dirs.js completed with code: %ERRORLEVEL%
) else (
    echo [3/3] create_dirs.js not found, skipping
)

echo.
echo ============================================================
echo BACKEND DIRECTORY STRUCTURE
echo ============================================================
dir "backend" /s /b 2>nul || echo Backend directory not found

echo.
echo ============================================================
echo FRONTEND DIRECTORY STRUCTURE
echo ============================================================
dir "frontend" /s /b 2>nul || echo Frontend directory not found

echo.
echo Press any key to exit...
pause >nul
