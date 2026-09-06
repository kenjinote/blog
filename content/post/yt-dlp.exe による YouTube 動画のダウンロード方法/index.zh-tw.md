---
title: "如何使用 yt-dlp.exe 下載 YouTube 影片"
slug: "yt-dlp.exe による YouTube 動画のダウンロード方法"
date: 2024-09-03T14:09:26+09:00
tags: ["YouTube", "下載"]
draft: false
image: "img_1.png"
categories: ["IT・科技"]
---
# 什麼是 yt-dlp

`yt-dlp` 是一個用於下載 YouTube 影片的命令列工具。
不僅可以下載影片，還可以將其作為音樂檔案以 mp3 格式下載。

## 下載與安裝

1. 從 [yt-dlp 的發布頁面](https://github.com/yt-dlp/yt-dlp/releases) 下載最新的 yt-dlp.exe。
2. 將 yt-dlp.exe 放置在任意資料夾中。
3. 將 yt-dlp.exe 的資料夾路徑加入到環境變數 Path 中。

## 使用方法

在命令提示字元中執行 yt-dlp.exe，並指定 YouTube 影片的 URL。

```
yt-dlp.exe "https://www.youtube.com/watch?v=VIDEO_ID"
```
※ 參數部分也可以只輸入 VIDEO_ID。

如果要將其下載為 mp3 音樂檔案，請執行以下命令：

```
yt-dlp.exe --extract-audio --audio-format mp3 --embed-thumbnail --add-metadata "https://www.youtube.com/watch?v=VIDEO_ID"
```

這樣，影片就會下載到執行命令的當前目錄中。

以上。
