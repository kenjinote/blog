---
title: 'How to download YouTube videos with yt-dlp.exe'
date: 2024-09-03T14:09:26+09:00
tags: ["YouTube", "Download"]
draft: false
image: "img_1.png"
categories: ["IT and Technology"]
---
# What is yt-dlp?

`yt-dlp` is a command-line tool for downloading YouTube videos.
Not only can you download videos, but you can also download them as music files in mp3 format.

## Download and Install

1. Download the latest yt-dlp.exe from the [yt-dlp releases page](https://github.com/yt-dlp/yt-dlp/releases).
2. Place yt-dlp.exe in a folder of your choice.
3. Add the folder path of yt-dlp.exe to the Path environment variable.

## Usage

Run yt-dlp.exe in the command prompt and specify the URL of the YouTube video.

```
yt-dlp.exe "https://www.youtube.com/watch?v=VIDEO_ID"
```
* Passing just the VIDEO_ID part as an argument is also OK.

If you want to download it as an mp3 music file, run the following command.

```
yt-dlp.exe --extract-audio --audio-format mp3 --embed-thumbnail --add-metadata "https://www.youtube.com/watch?v=VIDEO_ID"
```

The video will be downloaded to the current directory where you executed the command.

That's it.
