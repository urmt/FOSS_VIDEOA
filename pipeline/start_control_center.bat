@echo off
REM FOSS_VIDEOA Control Center - Startup Script
REM Starts the Flask backend and opens the control center in browser

echo ============================================================
echo FOSS_VIDEOA Control Center
echo ============================================================
echo.

REM Navigate to pipeline directory
cd /d "%~dp0"

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from python.org
    pause
    exit /b 1
)

REM Check if Flask is installed
python -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo Flask not found. Installing dependencies...
    python -m pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
)

echo Starting backend API server...
echo.
echo The control center will open in your browser shortly.
echo Press Ctrl+C to stop the server.
echo.

REM Start the Flask backend
python backend_api.py

pause
