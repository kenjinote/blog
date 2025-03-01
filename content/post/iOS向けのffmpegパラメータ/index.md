---
title: 'iOS向けのffmpegパラメータ'
date: 2025-03-02T04:16:07+09:00
tags: ["iOS", "ffmpeg"]
draft: false
---

# iOS向けのffmpegパラメータ

```bash

ffmpeg -i input.mp4 -c:v libx264 -profile:v high -level 4.1 -vf "scale=1920:-2" -r 30 -crf 20 -preset slow -c:a aac -b:a 128k -ar 48000 -movflags +faststart output.mp4

```