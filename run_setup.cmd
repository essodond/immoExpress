@echo off
REM Try python first
python C:\Users\DELL\Documents\projet\immo\final_setup.py
if errorlevel 1 (
    echo Python failed, trying python3...
    python3 C:\Users\DELL\Documents\projet\immo\final_setup.py
    if errorlevel 1 (
        echo Python3 failed, trying node...
        node C:\Users\DELL\Documents\projet\immo\master_setup.js
    )
)
