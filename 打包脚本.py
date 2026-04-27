#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
打包工具 - 创建可分发压缩包
"""

import zipfile
import os
from datetime import datetime

def main():
    # 要打包的文件列表
    files = [
        'run.bat',
        'check_env.bat',
        'gui_launcher.py',
        'douyin_downloader.py',
        'requirements.txt',
        'README.md',
        '使用说明.md',
    ]

    # 获取当前时间戳
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    zip_name = f'DouyinDownloader_一键安装包_{timestamp}.zip'

    print(f'正在打包 {len(files)} 个文件...')

    # 检查文件是否存在
    missing_files = []
    for file in files:
        if os.path.exists(file):
            print(f'  [OK] {file}')
        else:
            print(f'  [X] {file} 不存在')
            missing_files.append(file)

    if missing_files:
        print(f'\n缺少文件：{", ".join(missing_files)}')
        return False

    # 创建 ZIP 文件
    try:
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in files:
                zipf.write(file)

        print(f'\n[OK] 压缩包已创建：{zip_name}')
        print(f'文件大小：{os.path.getsize(zip_name) / 1024:.1f} KB')
        return True

    except Exception as e:
        print(f'\n[X] 压缩失败：{e}')
        return False

if __name__ == '__main__':
    main()
