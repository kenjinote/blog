---
title: "yt-dlp.exe使用方法：保存获准下载的视频并转换为MP3"
slug: "yt-dlp.exe による YouTube 视频の下载方法"
tags: ["yt-dlp", "YouTube", "media tools"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "介绍yt-dlp.exe的获取、更新、视频保存和MP3转换。请遵守内容权利要求和YouTube服务条款。"
date: "2024-09-03T14:09:26+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# yt-dlp.exe使用方法：保存获准下载的视频并转换为MP3

yt-dlp是一款用于下载视频和音频的开源命令行工具。以下示例介绍Windows上的基本用法。

## 仅在获准时使用

仅处理自己拥有权利或已获得权利人许可的内容，并确保符合YouTube服务条款和适用法律。自己上传的视频可以从YouTube Studio下载。

## 安装与更新

从官方发布页面下载Windows版`yt-dlp.exe`并放入文件夹。将该文件夹添加到`PATH`后，即可在任意目录运行。请只从官方发布页面获取可执行文件。

```powershell
yt-dlp.exe --version
yt-dlp.exe -U
```

## 基本用法

在命令提示符或PowerShell中指定视频URL。输出文件会保存到当前目录。

```powershell
yt-dlp.exe "https://www.youtube.com/watch?v=VIDEO_ID"
```

将音频转换为MP3时，使用`-x`和`--audio-format mp3`。

```powershell
yt-dlp.exe -x --audio-format mp3 "https://www.youtube.com/watch?v=VIDEO_ID"
```

运行`yt-dlp.exe --version`查看版本。发布版可通过`yt-dlp.exe -U`更新。转换MP3需要`ffmpeg`和`ffprobe`。如果YouTube调整后无法提取，请更新yt-dlp并查看官方README中的当前依赖项。

如需嵌入缩略图或元数据，可以添加`--embed-thumbnail`或`--embed-metadata`；根据文件格式可能还需要其他工具。

## 无法使用时

请更新到最新版本，并查看官方文档了解当前依赖项和支持情况。不要绕过限制，也不要下载未经授权的内容。

## 参考资料

- [yt-dlp official releases](https://github.com/yt-dlp/yt-dlp/releases/latest)
- [yt-dlp README and documentation](https://github.com/yt-dlp/yt-dlp#readme)
- [YouTube Terms of Service](https://www.youtube.com/t/terms)
- [YouTube Help: download your own videos](https://support.google.com/youtube/answer/56100)
