#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
抖音视频下载器 - 图形界面启动器
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import subprocess
import sys
import os
import threading
from pathlib import Path

# 设置 UTF-8 编码
if sys.platform == 'win32':
    import locale
    try:
        locale.setlocale(locale.LC_ALL, 'zh-CN.UTF-8')
    except:
        pass
    # 设置控制台编码
    os.environ['PYTHONIOENCODING'] = 'utf-8'


class DouyinDownloaderGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("抖音视频下载器 v1.2.3")
        self.root.geometry("550x620")
        self.root.resizable(False, False)

        # 获取脚本目录
        self.script_dir = Path(__file__).parent
        self.main_script = self.script_dir / "douyin_downloader.py"

        # 下载目录
        self.download_dir = self.script_dir / "downloads"

        self.setup_ui()

    def setup_ui(self):
        """设置界面"""
        # 标题
        title_frame = tk.Frame(self.root, bg="#FF2C55", height=50)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)

        title_label = tk.Label(
            title_frame,
            text="🎵 抖音视频下载器 v1.2.3",
            font=("Microsoft YaHei", 14, "bold"),
            bg="#FF2C55",
            fg="white"
        )
        title_label.pack(expand=True)

        # 主内容区
        content_frame = tk.Frame(self.root, padx=15, pady=15)
        content_frame.pack(fill=tk.BOTH, expand=True)

        # 模式选择
        mode_frame = tk.LabelFrame(content_frame, text=" 选择模式 ", font=("Microsoft YaHei", 10, "bold"))
        mode_frame.pack(fill=tk.X, pady=(0, 10))

        self.mode_var = tk.StringVar(value="single")

        modes = [
            ("single", "单个视频下载"),
            ("batch", "批量下载（Excel）"),
            ("detect", "关键词检测（单个视频）"),
            ("batch_detect", "批量下载+检测（Excel）"),
        ]

        for value, text in modes:
            rb = tk.Radiobutton(
                mode_frame,
                text=text,
                variable=self.mode_var,
                value=value,
                command=self.on_mode_change,
                font=("Microsoft YaHei", 9),
                activebackground="#f0f0f0"
            )
            rb.pack(anchor=tk.W, padx=10, pady=3)

        # 输入区域
        self.input_frame = tk.LabelFrame(content_frame, text=" 输入信息 ", font=("Microsoft YaHei", 10, "bold"))
        self.input_frame.pack(fill=tk.X, pady=(0, 10))

        # URL 输入
        self.url_label = tk.Label(self.input_frame, text="视频链接：", font=("Microsoft YaHei", 9))
        self.url_entry = tk.Entry(self.input_frame, font=("Microsoft YaHei", 10), width=50)

        # Excel 文件选择
        self.excel_label = tk.Label(self.input_frame, text="Excel 文件：", font=("Microsoft YaHei", 9))
        self.excel_path_var = tk.StringVar()
        self.excel_entry = tk.Entry(self.input_frame, textvariable=self.excel_path_var, font=("Microsoft YaHei", 10), width=38)
        self.browse_btn = tk.Button(
            self.input_frame,
            text="浏览...",
            command=self.browse_excel,
            font=("Microsoft YaHei", 9),
            width=8
        )

        # 关键词输入
        self.keyword_label = tk.Label(self.input_frame, text="检测关键词（逗号分隔）：", font=("Microsoft YaHei", 9))
        self.keyword_entry = tk.Entry(self.input_frame, font=("Microsoft YaHei", 10), width=50)
        self.keyword_entry.insert(0, "抖音,广告")

        # 初始化显示
        self.on_mode_change()

        # 进度显示
        progress_frame = tk.LabelFrame(content_frame, text=" 运行日志 ", font=("Microsoft YaHei", 10, "bold"))
        progress_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        # 创建带滚动条的文本框
        text_frame = tk.Frame(progress_frame)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.log_text = tk.Text(text_frame, height=10, font=("Consolas", 9), wrap=tk.WORD)
        scrollbar = tk.Scrollbar(text_frame, command=self.log_text.yview)
        self.log_text.config(yscrollcommand=scrollbar.set)

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 按钮区
        btn_frame = tk.Frame(content_frame)
        btn_frame.pack(fill=tk.X, pady=(5, 0))

        self.start_btn = tk.Button(
            btn_frame,
            text="▶ 开始执行",
            command=self.start_download,
            font=("Microsoft YaHei", 11, "bold"),
            bg="#FF2C55",
            fg="white",
            width=14,
            height=2,
            cursor="hand2",
            activebackground="#E0284A"
        )
        self.start_btn.pack(side=tk.LEFT, padx=(0, 10))

        self.open_dir_btn = tk.Button(
            btn_frame,
            text="📂 打开目录",
            command=self.open_download_dir,
            font=("Microsoft YaHei", 10),
            width=10,
            cursor="hand2"
        )
        self.open_dir_btn.pack(side=tk.LEFT, padx=(0, 10))

        self.view_log_btn = tk.Button(
            btn_frame,
            text="📄 查看识别日志",
            command=self.view_detection_logs,
            font=("Microsoft YaHei", 10),
            width=12,
            cursor="hand2"
        )
        self.view_log_btn.pack(side=tk.LEFT, padx=(0, 10))

        self.clear_btn = tk.Button(
            btn_frame,
            text="🗑 清空日志",
            command=self.clear_log,
            font=("Microsoft YaHei", 10),
            width=10,
            cursor="hand2"
        )
        self.clear_btn.pack(side=tk.LEFT)

    def on_mode_change(self):
        """模式切换时更新界面"""
        mode = self.mode_var.get()

        # 隐藏所有输入控件
        self.url_label.pack_forget()
        self.url_entry.pack_forget()
        self.excel_label.pack_forget()
        self.excel_entry.pack_forget()
        self.browse_btn.pack_forget()
        self.keyword_label.pack_forget()
        self.keyword_entry.pack_forget()

        # 根据模式显示对应的输入控件
        if mode == "single":
            self.url_label.pack(anchor=tk.W, padx=10, pady=(10, 0))
            self.url_entry.pack(fill=tk.X, padx=10, pady=(0, 10))

        elif mode == "batch":
            self.excel_label.pack(anchor=tk.W, padx=10, pady=(10, 0))
            excel_row = tk.Frame(self.input_frame)
            excel_row.pack(fill=tk.X, padx=10, pady=(0, 10))
            self.excel_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
            self.browse_btn.pack(side=tk.LEFT, padx=(5, 0))

        elif mode == "detect":
            self.url_label.pack(anchor=tk.W, padx=10, pady=(10, 0))
            self.url_entry.pack(fill=tk.X, padx=10, pady=(0, 5))
            self.keyword_label.pack(anchor=tk.W, padx=10)
            self.keyword_entry.pack(fill=tk.X, padx=10, pady=(0, 10))

        elif mode == "batch_detect":
            self.excel_label.pack(anchor=tk.W, padx=10, pady=(10, 0))
            excel_row = tk.Frame(self.input_frame)
            excel_row.pack(fill=tk.X, padx=10, pady=(0, 5))
            self.excel_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
            self.browse_btn.pack(side=tk.LEFT, padx=(5, 0))
            self.keyword_label.pack(anchor=tk.W, padx=10)
            self.keyword_entry.pack(fill=tk.X, padx=10, pady=(0, 10))

    def browse_excel(self):
        """浏览选择 Excel 文件"""
        file_path = filedialog.askopenfilename(
            title="选择 Excel 文件",
            filetypes=[("Excel 文件", "*.xlsx *.xls"), ("所有文件", "*.*")]
        )
        if file_path:
            self.excel_path_var.set(file_path)

    def view_detection_logs(self):
        """查看识别日志"""
        log_dir = self.script_dir / "downloads"
        speech_file = log_dir / "debug_speech.txt"
        ocr_file = log_dir / "debug_ocr.txt"

        if speech_file.exists():
            with open(speech_file, 'r', encoding='utf-8') as f:
                content = f.read()
            # 创建新窗口显示
            win = tk.Toplevel(self.root)
            win.title("语音识别结果")
            win.geometry("600x400")
            text = tk.Text(win, wrap=tk.WORD, font=("Consolas", 10))
            text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            text.insert('1.0', content)
            scrollbar = tk.Scrollbar(text)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        else:
            messagebox.showinfo("提示", "暂无语音识别日志，请先运行检测任务")

    def log(self, message):
        """添加日志"""
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update()

    def clear_log(self):
        """清空日志"""
        self.log_text.delete(1.0, tk.END)

    def open_download_dir(self):
        """打开下载目录"""
        if not self.download_dir.exists():
            self.download_dir.mkdir(parents=True)
        os.startfile(self.download_dir)

    def start_download(self):
        """开始下载"""
        mode = self.mode_var.get()

        # 验证输入
        url = self.url_entry.get().strip()
        excel_path = self.excel_path_var.get().strip()
        keywords = self.keyword_entry.get().strip()

        # 构建命令
        cmd = [sys.executable, str(self.main_script)]

        if mode == "single":
            if not url:
                messagebox.showerror("错误", "请输入视频链接")
                return
            cmd.append(url)

        elif mode == "batch":
            if not excel_path:
                messagebox.showerror("错误", "请选择 Excel 文件")
                return
            cmd.extend(["-e", excel_path])

        elif mode == "detect":
            if not url:
                messagebox.showerror("错误", "请输入视频链接")
                return
            if not keywords:
                messagebox.showerror("错误", "请输入检测关键词")
                return
            cmd.extend([url, "--detect", keywords])

        elif mode == "batch_detect":
            if not excel_path:
                messagebox.showerror("错误", "请选择 Excel 文件")
                return
            if not keywords:
                messagebox.showerror("错误", "请输入检测关键词")
                return
            cmd.extend(["-e", excel_path, "--detect", keywords])

        # 禁用按钮
        self.start_btn.config(state=tk.DISABLED, text="⏳ 运行中...")
        self.clear_log()

        # 在线程中运行
        def run_command():
            try:
                self.log(f"正在启动...")
                self.log(f"模式: {mode}")
                self.log(f"命令: {' '.join(cmd)}")
                self.log("-" * 40)

                # 使用无缓冲模式运行
                env = os.environ.copy()
                env['PYTHONUNBUFFERED'] = '1'
                env['PYTHONIOENCODING'] = 'utf-8'

                process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    encoding='utf-8',
                    errors='ignore',
                    cwd=str(self.script_dir),
                    env=env,
                    bufsize=0
                )

                for line in process.stdout:
                    self.log(line.rstrip())

                process.wait()

                if process.returncode == 0:
                    self.log("\n" + "=" * 40)
                    self.log("✓ 任务完成！")
                    messagebox.showinfo("完成", "任务已完成！")
                else:
                    self.log(f"\n✗ 任务失败，错误码: {process.returncode}")

            except Exception as e:
                self.log(f"\n✗ 错误: {e}")
                messagebox.showerror("错误", f"运行失败: {e}")

            finally:
                self.start_btn.config(state=tk.NORMAL, text="▶ 开始执行")

        thread = threading.Thread(target=run_command, daemon=True)
        thread.start()

    def run(self):
        """运行主循环"""
        self.root.mainloop()


if __name__ == "__main__":
    app = DouyinDownloaderGUI()
    app.run()
