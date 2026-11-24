---
title: "yt-dlp.exe使用方法：下載獲准內容並轉換為MP3"
slug: "yt-dlp.exe による YouTube 影片の下載方法"
tags: ["yt-dlp", "YouTube", "media tools"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "介紹yt-dlp.exe的取得、更新、影片儲存和MP3轉換。請遵守內容權利與YouTube服務條款。"
date: "2024-09-03T14:09:26+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# yt-dlp.exe使用方法：下載獲准內容並轉換為MP3

yt-dlp是用來下載影片與音訊的開放原始碼命令列工具。以下是Windows的基本用法。

## 僅在獲准時使用

僅處理自己擁有權利或已獲權利人授權的內容，並確保符合YouTube服務條款與適用法律。自己上傳的影片可透過YouTube Studio下載。

## 安裝與更新

從官方發行頁面下載Windows版`yt-dlp.exe`並放入資料夾。將資料夾新增至`PATH`後，即可從任何目錄執行。請只從官方發行頁面取得執行檔。

```powershell
yt-dlp.exe --version
yt-dlp.exe -U
```

## 基本用法

在命令提示字元或PowerShell中指定影片URL。輸出檔會儲存在目前目錄。

```powershell
yt-dlp.exe "https://www.youtube.com/watch?v=VIDEO_ID"
```

要將音訊轉成MP3，請使用`-x`和`--audio-format mp3`。

```powershell
yt-dlp.exe -x --audio-format mp3 "https://www.youtube.com/watch?v=VIDEO_ID"
```

使用`yt-dlp.exe --version`查看版本。發行版二進位檔可用`yt-dlp.exe -U`更新。MP3轉換需要`ffmpeg`與`ffprobe`。若YouTube變更後無法擷取，請更新yt-dlp並查看官方README的目前相依項目。

如需嵌入縮圖或中繼資料，可加入`--embed-thumbnail`或`--embed-metadata`；依檔案格式可能還需要其他工具。

## 無法使用時

請更新至最新版本，並查閱官方文件了解目前相依項目與支援狀況。請勿繞過限制或下載未經授權的內容。

## 參考資料

- [yt-dlp official releases](https://github.com/yt-dlp/yt-dlp/releases/latest)
- [yt-dlp README and documentation](https://github.com/yt-dlp/yt-dlp#readme)
- [YouTube Terms of Service](https://www.youtube.com/t/terms)
- [YouTube Help: download your own videos](https://support.google.com/youtube/answer/56100)
