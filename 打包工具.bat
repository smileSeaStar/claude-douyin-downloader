@echo off
chcp 65001 >nul 2>&1
title 打包工具 - 创建可分发压缩包

echo ========================================
echo   抖音视频下载器 - 打包工具
echo ========================================
echo.

:: 获取当前日期时间
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YYYY=%dt:~0,4%"
set "MM=%dt:~4,2%"
set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%"
set "Min=%dt:~10,2%"
set "SS=%dt:~12,2%"

set "ZIP_NAME=DouyinDownloader_%YYYY%%MM%%DD%_%HH%%Min%%SS%.zip"

echo 正在创建压缩包...
echo.

:: 创建临时目录
set "TEMP_DIR=temp_pack_%RANDOM%"
mkdir "%TEMP_DIR%" 2>nul

:: 复制必要文件
echo 复制文件...
copy /y run.bat "%TEMP_DIR%\" >nul
copy /y check_env.bat "%TEMP_DIR%\" >nul
copy /y gui_launcher.py "%TEMP_DIR%\" >nul
copy /y douyin_downloader.py "%TEMP_DIR%\" >nul
copy /y requirements.txt "%TEMP_DIR%\" >nul
copy /y README.md "%TEMP_DIR%\" >nul
copy /y 使用说明.md "%TEMP_DIR%\" >nul

:: 创建说明文件
echo. > "%TEMP_DIR%\README_同事使用.txt"
echo ======================================== >> "%TEMP_DIR%\README_同事使用.txt"
echo 抖音视频下载器 - 使用说明 >> "%TEMP_DIR%\README_同事使用.txt"
echo ======================================== >> "%TEMP_DIR%\README_同事使用.txt"
echo. >> "%TEMP_DIR%\README_同事使用.txt"
echo 1. 确保已安装 Python 3.8+ >> "%TEMP_DIR%\README_同事使用.txt"
echo    下载地址：https://www.python.org/downloads/ >> "%TEMP_DIR%\README_同事使用.txt"
echo    安装时务必勾选 "Add Python to PATH" >> "%TEMP_DIR%\README_同事使用.txt"
echo. >> "%TEMP_DIR%\README_同事使用.txt"
echo 2. 双击 run.bat 即可启动 >> "%TEMP_DIR%\README_同事使用.txt"
echo    程序会自动安装所有依赖 >> "%TEMP_DIR%\README_同事使用.txt"
echo. >> "%TEMP_DIR%\README_同事使用.txt"
echo 3. 如果 run.bat 打不开，请右键选择 >> "%TEMP_DIR%\README_同事使用.txt"
echo    "打开方式" -> "命令提示符" >> "%TEMP_DIR%\README_同事使用.txt"
echo. >> "%TEMP_DIR%\README_同事使用.txt"

echo.
echo 正在压缩...

:: 使用 PowerShell 创建 ZIP
powershell -Command "& {Compress-Archive -Path '%TEMP_DIR%\*' -DestinationPath '%ZIP_NAME%' -Force}"

if errorlevel 1 (
    echo [X] 压缩失败，请手动压缩文件夹
    pause
    exit /b 1
)

:: 清理临时目录
rmdir /s /q "%TEMP_DIR%"

echo.
echo ========================================
echo [OK] 压缩包已创建：%ZIP_NAME%
echo ========================================
echo.
echo 现在可以将这个 ZIP 文件发给同事了
echo.
pause
