# 抖音视频下载器 v1.3.0 - 发布说明

## 🎉 新功能

### 1. 自定义下载路径
- GUI 界面新增"浏览"按钮，可选择任意文件夹作为下载目录
- 解决了固定路径限制，支持灵活管理下载文件

### 2. Excel 结果自动回写
- 批量下载后，结果自动填充回 Excel B 列
- 显示格式：`✓ 下载成功` / `✗ 下载失败`
- 自动清空 B 列旧数据，避免重复显示

### 3. 短链接支持增强
- 自动识别并解析抖音短链接
- 兼容多种链接格式（完整链接/短链接）

## 📦 安装包

**文件名**：`抖音视频下载器_v1.3.0_一键安装包.zip`  
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

## 📋 更新日志

### v1.3.0 (2026-04-30)
- ✅ 新增自定义下载路径选择
- ✅ Excel 结果自动回写
- ✅ 优化短链接识别
- ✅ 界面布局优化

### v1.2.4 (2026-04-28)
- ✅ 基础下载功能
- ✅ Excel 批量下载
- ✅ 关键词检测（语音+字幕 OCR）
- ✅ 短链接支持

## 🔧 技术栈

- Python 3.8+
- Playwright 浏览器自动化
- OpenPyExcel 处理 Excel
- Tkinter GUI

## 📝 注意事项

1. 首次运行会自动下载浏览器驱动（约 100MB）
2. 确保网络连接正常，需要访问抖音服务器
3. 下载的文件名格式：`{标题}.mp4`
4. 批量下载时，Excel 文件中 A 列为视频链接

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License
