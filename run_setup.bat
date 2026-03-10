@echo off
cd /d "C:\Users\DELL\Documents\projet\immo"

echo Running setup_backend.py...
python setup_backend.py
if %ERRORLEVEL% EQU 0 (
    echo [SUCCESS] setup_backend.py completed
) else (
    echo [FAILED] setup_backend.py failed with code %ERRORLEVEL%
)

echo.
echo Running create_dirs.py...
python create_dirs.py
if %ERRORLEVEL% EQU 0 (
    echo [SUCCESS] create_dirs.py completed
) else (
    echo [FAILED] create_dirs.py failed with code %ERRORLEVEL%
)

echo.
if exist "create_dirs.js" (
    echo Running create_dirs.js...
    node create_dirs.js
    if %ERRORLEVEL% EQU 0 (
        echo [SUCCESS] create_dirs.js completed
    ) else (
        echo [FAILED] create_dirs.js failed with code %ERRORLEVEL%
    )
) else (
    echo create_dirs.js not found
)

echo.
echo Listing backend directory structure...
dir "C:\Users\DELL\Documents\projet\immo\backend" /s /b 2>nul || echo backend directory does not exist

echo.
echo Listing frontend directory structure...
dir "C:\Users\DELL\Documents\projet\immo\frontend" /s /b 2>nul || echo frontend directory does not exist

pause
