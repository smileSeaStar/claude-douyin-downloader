# 抖音视频无水印下载器 v1.2.4

支持单个视频下载、Excel 批量下载、关键词检测（语音 + 字幕 OCR）。

## 一键安装运行（推荐）

**Windows 用户：**
1. 确保已安装 Python 3.8+（安装时勾选 "Add Python to PATH"）
2. 双击 `run.bat`
3. 脚本会自动安装所有依赖并配置浏览器

## 手动安装

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 安装浏览器
playwright install chromium
```

## 使用方法

### 方式一：图形菜单（推荐）

双击 `run.bat`，按提示选择操作。

### 方式二：命令行

```bash
# 下载单个视频
python douyin_downloader.py "视频链接"

# 从 Excel 批量下载
python douyin_downloader.py -e videos.xlsx

# 下载并检测关键词（语音 + 字幕）
python douyin_downloader.py "视频链接" --detect "关键词 1，关键词 2"

# 仅检测语音（禁用 OCR）
python douyin_downloader.py "视频链接" --detect "关键词" --no-ocr

# 批量检测多个关键词
python douyin_downloader.py -e videos.xlsx --detect "抖音，广告，合作"
```

### 关键词检测功能

下载视频后自动检测：
- **语音内容**：识别视频中说话的内容
- **字幕 OCR**：识别画面中烧录的字幕

检测结果自动保存到报告文件：`detection_report_YYYYMMDD_HHMMSS.txt`

输出示例：
```
============================================================
视频：想改个好记的抖音号怎么设置.mp4
链接：https://www.douyin.com/video/xxx
时间：2026-04-23 09:02:51
============================================================

【语音检测】发现关键词:
  "抖音" 出现 7 次
    - 00:00: 抖音号不是大家出车时的手机号
    - 00:03: 而是抖音平台给大家的一个个身份边
    ...

【字幕 OCR 检测】发现关键词:
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
| `-o, --output` | 输出目录（默认：./downloads） |
| `-f, --format` | 文件名格式，支持 `{title}`, `{author}`, `{id}` |
| `--detect` | 检测关键词，多个用逗号分隔 |
| `--no-ocr` | 禁用字幕 OCR 检测 |
| `--no-speech` | 禁用语音检测 |
| `--model` | 语音识别模型：tiny/base/small/medium（默认：base） |
| `--head` | 显示浏览器窗口（调试用） |

## 支持的链接格式

- 标准链接：`https://www.douyin.com/video/xxx`
- Note 链接：`https://www.douyin.com/note/xxx`
- 搜索页面：`https://www.douyin.com/jingxuan/search/xxx?modal_id=xxx`

## 常见问题

### 1. 首次运行提示找不到模块

```bash
pip install -r requirements.txt
playwright install chromium
```

### 2. 下载失败或视频无法播放

- 检查网络连接
- 确保视频不是私密或已删除状态
- 尝试使用 `--head` 参数查看浏览器输出

### 3. 语音/字幕识别速度慢

- 首次使用会下载模型文件（约 200MB），之后会缓存
- 模型文件位置：
  - Whisper 模型：`~/.cache/huggingface/hub/`
  - EasyOCR 模型：`~/.cache/easyocr/`

## 注意事项

1. 首次使用需要安装 Chromium 浏览器（自动完成，约 500MB）
2. 首次使用关键词检测会下载语音识别模型（约 150MB）和 OCR 模型（约 50MB）
3. 下载的视频为无水印高清版本
4. 私密视频或已删除视频无法下载
5. 所有检测完全免费、离线运行
6. 支持简体和繁体关键词匹配

## 依赖

- playwright - 浏览器自动化
- openpyxl - Excel 支持
- aiohttp - 异步 HTTP
- faster-whisper - 语音识别（免费）
- easyocr - 字幕 OCR（免费）
- opencv-python - 视频处理
- opencc-chinese - 简繁转换

## 更新日志

### v1.2.4
- 优化简繁关键词匹配，支持简体和繁体输入
- 使用 opencc 库替代硬编码映射表

### v1.2.3
- 修复关键词检测功能
- 优化下载稳定性

### v1.2.2
- 初始版本
