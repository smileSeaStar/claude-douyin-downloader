@echo off
title 打包工具 - 创建可分发压缩包

echo ========================================
echo   抖音视频下载器 - 打包工具
echo ========================================
echo.

echo 正在创建压缩包...
echo.

:: 使用 Python 进行压缩
python 打包脚本.py

if errorlevel 1 (
    echo.
    echo [X] 打包失败
    pause
    exit /b 1
)

echo.
echo ========================================
echo [OK] 打包完成！
echo ========================================
echo.
pause
