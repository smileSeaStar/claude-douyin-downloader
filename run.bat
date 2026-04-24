@echo off
setlocal enabledelayedexpansion
title Douyin Downloader v1.2.4

:: 检查 Python 是否安装
where python >nul 2>&1
if errorlevel 1 (
    echo ========================================
    echo [ERROR] Python 未找到
    echo ========================================
    echo.
    echo 请先安装 Python 3.8 或更高版本
    echo 下载地址：https://www.python.org/downloads/
    echo.
    echo 安装时请务必勾选 "Add Python to PATH" 选项
    echo.
    pause
    exit /b 1
)

:: 检查 Python 版本
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYVER=%%i
echo [OK] Python 已安装：!PYVER!

:: 检查依赖是否已安装
python -c "import playwright" 2>nul
if errorlevel 1 (
    echo.
    echo ========================================
    echo [INFO] 正在安装依赖...
    echo ========================================
    pip install -r "%~dp0requirements.txt"
    if errorlevel 1 (
        echo [ERROR] 依赖安装失败
        pause
        exit /b 1
    )
) else (
    echo [OK] 依赖已安装
)

:: 检查浏览器是否已安装
playwright install chromium 2>nul
if errorlevel 1 (
    echo.
    echo ========================================
    echo [INFO] 正在安装 Chromium 浏览器...
    echo ========================================
    playwright install chromium
)

echo.
echo ========================================
echo 启动成功！
echo ========================================
echo.

:: 启动图形界面
python "%~dp0gui_launcher.py"

if errorlevel 1 (
    echo.
    echo [ERROR] 程序运行出错
    pause
)
