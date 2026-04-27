#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试 run.bat 是否正确
"""

import os
import subprocess

def test_run_bat():
    # 读取 run.bat
    with open('run.bat', 'rb') as f:
        content = f.read()

    print('=== run.bat 测试 ===\n')

    # 测试 1: 检查文件是否存在
    print('测试 1: 检查文件是否存在')
    if os.path.exists('run.bat'):
        print('[OK] run.bat 存在')
    else:
        print('[X] run.bat 不存在')
        return False

    # 测试 2: 检查必要命令
    print('\n测试 2: 检查必要命令')
    required_commands = [
        b'pip install',
        b'python',
        b'gui_launcher.py',
        b'playwright',
        b'Add Python to PATH',
    ]

    missing = []
    for cmd in required_commands:
        if cmd not in content:
            missing.append(cmd)

    if missing:
        print('[X] 缺少命令：')
        for cmd in missing:
            print(f'  - {cmd}')
        return False
    else:
        print('[OK] 所有必要命令都存在')

    # 测试 3: 检查编码（应该是 GBK）
    print('\n测试 3: 检查文件编码')
    # GBK 编码的中文字符起始字节
    gbk_chinese = [0xB0, 0xB1, 0xB2, 0xB3, 0xB4, 0xB5, 0xB6, 0xB7, 0xB8, 0xB9, 0xBA, 0xBB, 0xBC, 0xBD, 0xBE, 0xBF,
                   0xC0, 0xC1, 0xC2, 0xC3, 0xC4, 0xC5, 0xC6, 0xC7, 0xC8, 0xC9, 0xCA, 0xCB, 0xCC, 0xCD, 0xCE, 0xCF]

    has_chinese = any(byte in content[:500] for byte in gbk_chinese)

    if has_chinese:
        print('[OK] 包含中文内容（GBK编码）')
    else:
        print('[X] 缺少中文内容')
        return False

    # 测试 4: 检查文件大小
    print('\n测试 4: 检查文件大小')
    file_size = len(content)
    print(f'[OK] 文件大小：{file_size} 字节')

    if file_size < 1000:
        print('[X] 文件太小，可能不完整')
        return False

    print('\n=== 所有测试通过 ===')
    return True

if __name__ == '__main__':
    success = test_run_bat()
    exit(0 if success else 1)
