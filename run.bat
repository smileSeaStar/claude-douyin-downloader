@echo off
title Douyin Downloader v1.2.4

echo ========================================
echo   Douyin Video Downloader v1.2.4
echo ========================================
echo.

:: Check Python
where python >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found
    echo.
    echo Please install Python 3.8 or higher
    echo Download: https://www.python.org/downloads/
    echo.
    echo IMPORTANT: Check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYVER=%%i
echo [OK] Python installed: %PYVER%

:: Check and install dependencies
echo.
echo Checking dependencies...
python -c "import playwright" 2>nul
if errorlevel 1 (
    echo [INFO] Installing dependencies...
    pip install -r "%~dp0requirements.txt"
    if errorlevel 1 (
        echo [ERROR] Dependency installation failed
        echo.
        echo Please run manually: pip install -r requirements.txt
        echo.
        pause
        exit /b 1
    )
) else (
    echo [OK] Dependencies installed
)

echo.
echo ========================================
echo   Launching...
echo ========================================
echo.

:: Launch GUI
python "%~dp0gui_launcher.py"

if errorlevel 1 (
    echo.
    echo [ERROR] Program error
    pause
)
