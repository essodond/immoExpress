@echo off
setlocal enabledelayedexpansion
cd /d "C:\Users\DELL\Documents\projet\immo"
python setup_complete.py
if %ERRORLEVEL% EQU 0 (
    echo.
    echo SUCCESS! All directories and files have been created.
    echo.
    dir /s /b "C:\Users\DELL\Documents\projet\immo\backend" 2>nul | find /c /v ""
    echo Backend files/dirs created above.
    echo.
    dir /s /b "C:\Users\DELL\Documents\projet\immo\frontend" 2>nul | find /c /v ""
    echo Frontend files/dirs created above.
) else (
    echo FAILED! Exit code: %ERRORLEVEL%
)
pause
