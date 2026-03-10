@echo off
cd /d "C:\Users\DELL\Documents\projet\immo"
python setup_backend.py
if %ERRORLEVEL% EQU 0 (
    echo [SUCCESS] Directories created successfully
    dir "C:\Users\DELL\Documents\projet\immo\backend" /s /b
) else (
    echo [FAILED] setup_backend.py failed
    exit /b 1
)
