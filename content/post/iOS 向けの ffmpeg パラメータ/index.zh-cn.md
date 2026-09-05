---
title: '面向 iOS 的 ffmpeg 参数'
date: 2025-03-02T04:16:07+09:00
tags: ["iOS", "ffmpeg"]
draft: false
image: "img.png"
categories: ["PC与数码"]
---

# 面向 iOS 优化的 ffmpeg 转换参数

为了能在 iOS 设备（iPhone 或 iPad）上流畅播放，向您介绍用于转换视频的 `ffmpeg` 命令。

```bash
ffmpeg -i input.mp4 \
-c:v libx264 -profile:v high -level 4.1 \
-vf "scale=1920:-2" -r 30 \
-crf 20 -preset slow \
-c:a aac -b:a 128k -ar 48000 \
-movflags +faststart output.mp4
```

### 各选项的含义（简单解说）

| 选项                        | 说明                                          |
| ---------------------------- | ------------------------------------------- |
| `-i input.mp4`               | 输入文件（转换源视频）                              |
| `-c:v libx264`               | 使用 H.264 编码视频（支持 iOS）                       |
| `-profile:v high -level 4.1` | 在 iOS 上广泛兼容的配置文件和级别                      |
| `-vf "scale=1920:-2"`        | 调整宽度为 1920px，高度保持宽高比自动调整               |
| `-r 30`                      | 转换为 30fps 的帧率                             |
| `-crf 20`                    | 视频质量（数值越低画质越高，推荐 18～23）                   |
| `-preset slow`               | 编码速度与压缩率的平衡（slow 代表高压缩・高画质）              |
| `-c:a aac`                   | 音频使用 AAC 格式编码                              |
| `-b:a 128k`                  | 设置音频比特率为 128kbps                         |
| `-ar 48000`                  | 设置音频采样率为 48kHz（iOS 推荐）                |
| `-movflags +faststart`       | 将索引放置在视频开头，**加快在 Web 和 iOS 上的流媒体播放速度** |

---

使用此设置转换的视频，有望在 iPhone、iPad 等 Apple 设备上获得高兼容性和流畅的播放体验。

---

您可以根据需要通过更改分辨率或比特率来调整文件大小或画质。如果需要高画质，请尝试将 `-crf` 设置为 18 左右；如果想减小文件大小，请将其设置为 22～25。
