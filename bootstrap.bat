@echo off
title ImmoExpert Frontend Setup
cd /d "%~dp0"

echo.
echo ===================================
echo   ImmoExpert - Frontend Setup
echo ===================================
echo.

:: Try Python first
python --version >nul 2>&1
if not errorlevel 1 (
    echo Using Python...
    python setup.py
    goto :done
)

:: Fallback to Node.js
node --version >nul 2>&1
if not errorlevel 1 (
    echo Using Node.js...
    node run_setup.js
    goto :done
)

echo [ERROR] Neither Python nor Node.js found in PATH.
echo Please install Python 3: https://www.python.org/
pause
exit /b 1

:done
if errorlevel 1 (
    echo.
    echo [ERROR] Setup failed. Check the output above.
    pause
    exit /b 1
)

echo.
echo ===================================
echo   Setup complete!
echo ===================================
echo.
echo Next steps:
echo   1. cd frontend
echo   2. npm install
echo   3. copy .env.local.example .env.local
echo   4. Edit .env.local with your API URL and WhatsApp number
echo   5. npm run dev
echo.
echo   Site:  http://localhost:3000
echo   Admin: http://localhost:3000/admin/login
echo.
pause
