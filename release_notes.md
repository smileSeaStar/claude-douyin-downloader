# 抖音视频下载器 v1.4.1 - 发布说明

## 🎉 新功能

### 1. 文件名序号功能
- 同名标题的视频自动添加序号（1_, 2_, 3_...）
- 彻底解决文件覆盖问题
- 文件名格式：`1_标题.mp4`, `2_标题.mp4`, `3_标题.mp4`...

### 2. 检测功能选择
- GUI新增"启用语音检测"复选框（默认选中）
- GUI新增"启用OCR文字检测"复选框（默认选中）
- 用户可以自由选择启用/禁用检测功能
- 支持命令行参数 `--no-speech` 和 `--no-ocr`

### 3. 界面修复
- 修复批量下载检测模式下复选框不显示的问题
- 调整窗口高度，确保内容完整显示

## 📦 安装包

**文件名**：`抖音视频下载器_v1.4.1_一键安装包.zip`  
**大小**：19 KB  
**包含文件**：
- `gui_launcher.py` - GUI 启动器
- `douyin_downloader.py` - 核心下载器
- `run.bat` - 一键启动脚本
- `check_env.bat` - 环境检查脚本
- `requirements.txt` - Python 依赖
- `README.md` - 使用说明
- `使用说明.md` - 详细文档

## 🚀 使用方式

### 方式一：一键运行（推荐）
```bash
# 解压后双击 run.bat
run.bat
```

### 方式二：Python 运行
```bash
# 安装依赖
pip install -r requirements.txt
playwright install chromium

# 启动 GUI
python gui_launcher.py
```

### 检测功能选择
1. 选择"关键词检测"或"批量下载+检测"模式
2. 根据需要勾选/取消"启用语音检测"
3. 根据需要勾选/取消"启用OCR文字检测"
4. 开始下载

### 命令行使用
```bash
# 仅下载，不检测
python douyin_downloader.py "URL"

# 仅下载，禁用语音检测
python douyin_downloader.py "URL" --no-speech

# 仅下载，禁用OCR检测
python douyin_downloader.py "URL" --no-ocr

# 下载并检测，禁用语音检测
python douyin_downloader.py "URL" --detect "关键词" --no-speech

# 下载并检测，禁用OCR检测
python douyin_downloader.py "URL" --detect "关键词" --no-ocr
```

## 📋 更新日志

### v1.4.1 (2026-05-08)
- ✅ 修复批量下载检测模式复选框不显示问题
- ✅ 调整窗口高度，确保内容完整显示

### v1.4.0 (2026-05-07)
- ✅ 新增文件名序号功能，避免同名文件覆盖
- ✅ 新增检测功能选择复选框
- ✅ 支持命令行参数控制检测功能

### v1.3.0 (2026-04-30)
- ✅ 新增自定义下载路径
- ✅ Excel 结果自动回写
- ✅ 短链接支持增强

## 🔧 技术栈

- Python 3.8+
- Playwright 浏览器自动化
- OpenPyExcel 处理 Excel
- Tkinter GUI

## 📝 注意事项

1. 首次运行会自动下载浏览器驱动（约 100MB）
2. 确保网络连接正常，需要访问抖音服务器
3. 下载的文件名格式：`序号_标题.mp4`
4. 批量下载时，Excel 文件中 A 列为视频链接
5. 用户可以自由选择启用/禁用语音检测和 OCR 检测

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License
