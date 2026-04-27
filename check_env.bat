@echo off
chcp 65001 >nul 2>&1
title 抖音视频下载器 - 环境检测与安装工具

echo ========================================
echo   抖音视频下载器 - 环境检测工具
echo ========================================
echo.

set "ERRORS=0"

:: 检查 Python
echo [1/4] 检查 Python 环境...
where python >nul 2>&1
if errorlevel 1 (
    echo   [X] Python 未安装
    echo.
    echo   请访问 https://www.python.org/downloads/ 下载并安装 Python 3.8+
    echo   安装时请务必勾选 "Add Python to PATH"
    echo.
    set /a ERRORS+=1
) else (
    for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYVER=%%i
    echo   [OK] Python 已安装：%PYVER%
)
echo.

:: 检查 pip
echo [2/4] 检查 pip 环境...
where pip >nul 2>&1
if errorlevel 1 (
    echo   [X] pip 未安装
    echo.
    echo   请重新安装 Python，并确保勾选 "Install pip"
    echo.
    set /a ERRORS+=1
) else (
    echo   [OK] pip 已安装
)
echo.

:: 检查依赖
echo [3/4] 检查依赖包...
python -c "import playwright" 2>nul
if errorlevel 1 (
    echo   [!] playwright 未安装 - 将自动安装
    set /a ERRORS+=1
) else (
    echo   [OK] playwright 已安装
)

python -c "import openpyxl" 2>nul
if errorlevel 1 (
    echo   [!] openpyxl 未安装 - 将自动安装
    set /a ERRORS+=1
) else (
    echo   [OK] openpyxl 已安装
)

python -c "import aiohttp" 2>nul
if errorlevel 1 (
    echo   [!] aiohttp 未安装 - 将自动安装
    set /a ERRORS+=1
) else (
    echo   [OK] aiohttp 已安装
)

python -c "import faster_whisper" 2>nul
if errorlevel 1 (
    echo   [!] faster-whisper 未安装 - 将自动安装
    set /a ERRORS+=1
) else (
    echo   [OK] faster-whisper 已安装
)

python -c "import easyocr" 2>nul
if errorlevel 1 (
    echo   [!] easyocr 未安装 - 将自动安装
    set /a ERRORS+=1
) else (
    echo   [OK] easyocr 已安装
)

python -c "import cv2" 2>nul
if errorlevel 1 (
    echo   [!] opencv-python 未安装 - 将自动安装
    set /a ERRORS+=1
) else (
    echo   [OK] opencv-python 已安装
)

python -c "import opencc" 2>nul
if errorlevel 1 (
    echo   [!] opencc 未安装 - 将自动安装
    set /a ERRORS+=1
) else (
    echo   [OK] opencc 已安装
)
echo.

:: 检查浏览器
echo [4/4] 检查浏览器...
playwright install chromium --help >nul 2>&1
if errorlevel 1 (
    echo   [!] 请先安装依赖包后再安装浏览器
) else (
    playwright install chromium 2>nul
    if errorlevel 1 (
        echo   [!] Chromium 浏览器未安装 - 需要手动运行：playwright install chromium
    ) else (
        echo   [OK] Chromium 已安装
    )
)
echo.

echo ========================================
if %ERRORS%==0 (
    echo   环境检测完成！所有依赖已就绪
    echo.
    echo   现在可以运行 run.bat 启动程序
) else (
    echo   发现 %ERRORS% 个问题
    echo.
    echo   正在自动安装缺失的依赖...
    echo.
    pip install -r "%~dp0requirements.txt"
    if errorlevel 1 (
        echo   [X] 依赖安装失败，请手动运行：pip install -r requirements.txt
    ) else (
        echo.
        echo   [OK] 依赖安装完成！
        echo.
        echo   现在请运行：playwright install chromium
    )
)
echo ========================================
echo.
pause
