# 抖音视频无水印下载器 v1.2.2

支持单个视频下载、Excel 批量下载、关键词检测（语音+字幕OCR）。

## 安装

### 第一步：安装 Python

从 https://www.python.org/downloads/ 下载并安装 Python 3.8 或更高版本。

**重要**：安装时务必勾选 **"Add Python to PATH"** 选项。

### 第二步：运行脚本

双击 `run.bat` 运行，首次运行会自动安装所需依赖和浏览器（约 500MB）。

## 使用方法

### 方式一：图形菜单（推荐）

双击 `run.bat`，按提示选择操作。

### 方式二：命令行

```bash
# 下载单个视频
python douyin_downloader.py "https://www.douyin.com/video/7627089262673154289"

# 从 Excel 批量下载
python douyin_downloader.py -e videos.xlsx

# 下载并检测关键词（语音+字幕）
python douyin_downloader.py "URL" --detect "抖音"

# 仅检测语音（禁用OCR）
python douyin_downloader.py "URL" --detect "抖音" --no-ocr

# 批量检测多个关键词
python douyin_downloader.py -e videos.xlsx --detect "抖音,广告,合作"
```

### 关键词检测功能

下载视频后自动检测：
- **语音内容**：识别视频中说话的内容
- **字幕 OCR**：识别画面中烧录的字幕

检测结果自动保存到报告文件：`detection_report_YYYYMMDD_HHMMSS.txt`

输出示例：
```
============================================================
视频: 想改个好记的抖音号怎么设置.mp4
链接: https://www.douyin.com/video/xxx
时间: 2026-04-23 09:02:51
============================================================

【语音检测】发现关键词:
  "抖音" 出现 7 次
    - 00:00: 抖音号不是大家出车时的手机号
    - 00:03: 而是抖音平台给大家的一个个身份边
    ...

【字幕OCR检测】发现关键词:
  "抖音" 出现 32 次
    - 00:00: 如何修改抖音号
    - 00:01: 如何修改抖音号 抖音号不是大家注册时的手机号
    ...
```

### Excel 格式

第一列为视频链接，第一行为标题行：

| 视频链接 |
|----------|
| https://www.douyin.com/video/xxx |
| https://www.douyin.com/video/yyy |

### 可选参数

| 参数 | 说明 |
|------|------|
| `-o, --output` | 输出目录（默认: ./downloads） |
| `-f, --format` | 文件名格式，支持 `{title}`, `{author}`, `{id}` |
| `--detect` | 检测关键词，多个用逗号分隔 |
| `--no-ocr` | 禁用字幕 OCR 检测 |
| `--model` | 语音识别模型: tiny/base/small/medium（默认: base） |
| `--head` | 显示浏览器窗口（调试用） |

## 支持的链接格式

- 标准链接: `https://www.douyin.com/video/7627089262673154289`
- Note 链接: `https://www.douyin.com/note/7627089262673154289`
- 搜索页面: `https://www.douyin.com/jingxuan/search/xxx?modal_id=xxx`

## 注意事项

1. 首次使用需要安装 Chromium 浏览器（自动完成）
2. 首次使用关键词检测会下载语音识别模型（约 150MB）和 OCR 模型（约 50MB）
3. 下载的视频为无水印高清版本
4. 私密视频或已删除视频无法下载
5. 所有检测完全免费、离线运行

## 依赖

- playwright - 浏览器自动化
- openpyxl - Excel 支持
- aiohttp - 异步 HTTP
- faster-whisper - 语音识别（免费）
- easyocr - 字幕 OCR（免费）
- opencv-python - 视频处理