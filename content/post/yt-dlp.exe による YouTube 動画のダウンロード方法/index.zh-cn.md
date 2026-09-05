---
title: '使用yt-dlp.exe下载YouTube视频的方法'
date: 2024-09-03T14:09:26+09:00
tags: ["YouTube", "下载"]
draft: false
image: "img_1.png"
categories: ["IT·科技"]
---
# 什么是yt-dlp

`yt-dlp` 是一个用于下载YouTube视频的命令行工具。
除了下载视频，还可以将其作为音频文件以mp3格式下载。

## 下载与安装

1. 从 [yt-dlp的发布页面](https://github.com/yt-dlp/yt-dlp/releases) 下载最新的yt-dlp.exe。
2. 将yt-dlp.exe放置在任意文件夹中。
3. 将yt-dlp.exe所在的文件夹路径添加到环境变量Path中。

## 使用方法

在命令提示符下运行yt-dlp.exe，并指定YouTube视频的URL。

```
yt-dlp.exe "https://www.youtube.com/watch?v=VIDEO_ID"
```
※参数仅指定 VIDEO_ID 的部分也可以。

如果要作为mp3音频文件下载，请执行以下命令。

```
yt-dlp.exe --extract-audio --audio-format mp3 --embed-thumbnail --add-metadata "https://www.youtube.com/watch?v=VIDEO_ID"
```

这样，视频就会被下载到执行命令的当前目录中。

以上。
