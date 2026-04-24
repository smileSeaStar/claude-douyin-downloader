@echo off
setlocal enabledelayedexpansion
title Douyin Downloader v1.2.3

where python >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

REM 启动图形界面
python "%~dp0gui_launcher.py"

if errorlevel 1 (
    echo.
    echo [ERROR] Program exited with error
    pause
)
