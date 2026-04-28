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
echo.

:: Check playwright
python -c "import playwright" 2>nul
if errorlevel 1 (
    echo [!] playwright not found
) else (
    echo [OK] playwright
)

:: Check openpyxl
python -c "import openpyxl" 2>nul
if errorlevel 1 (
    echo [!] openpyxl not found
) else (
    echo [OK] openpyxl
)

:: Check aiohttp
python -c "import aiohttp" 2>nul
if errorlevel 1 (
    echo [!] aiohttp not found
) else (
    echo [OK] aiohttp
)

:: Check faster-whisper
python -c "import faster_whisper" 2>nul
if errorlevel 1 (
    echo [!] faster-whisper not found
) else (
    echo [OK] faster-whisper
)

:: Check easyocr
python -c "import easyocr" 2>nul
if errorlevel 1 (
    echo [!] easyocr not found
) else (
    echo [OK] easyocr
)

:: Check opencv-python
python -c "import cv2" 2>nul
if errorlevel 1 (
    echo [!] opencv-python not found
) else (
    echo [OK] opencv-python
)

echo.
echo Installing all dependencies...
pip install -r "%~dp0requirements.txt"

if errorlevel 1 (
    echo [ERROR] Dependency installation failed
    echo.
    echo Please run manually: pip install -r requirements.txt
    echo.
    pause
    exit /b 1
)

echo [OK] All dependencies installed

echo.
echo Installing Chromium browser...
playwright install chromium

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
