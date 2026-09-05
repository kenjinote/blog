---
title: 'ffmpeg Parameters for iOS'
date: 2025-03-02T04:16:07+09:00
tags: ["iOS", "ffmpeg"]
draft: false
image: "img.png"
categories: ["PC & Gadgets"]
---

# ffmpeg Conversion Parameters Optimized for iOS

Here is an `ffmpeg` command to convert videos so they can be played smoothly on iOS devices (iPhone and iPad).

```bash
ffmpeg -i input.mp4 \
-c:v libx264 -profile:v high -level 4.1 \
-vf "scale=1920:-2" -r 30 \
-crf 20 -preset slow \
-c:a aac -b:a 128k -ar 48000 \
-movflags +faststart output.mp4
```

### Meaning of Each Option (Brief Explanation)

| Option                        | Description                                          |
| ---------------------------- | ------------------------------------------- |
| `-i input.mp4`               | Input file (source video to be converted)                              |
| `-c:v libx264`               | Encode video with H.264 (iOS compatible)                       |
| `-profile:v high -level 4.1` | Widely compatible profile and level for iOS                      |
| `-vf "scale=1920:-2"`        | Resize width to 1920px, auto-adjust height maintaining aspect ratio               |
| `-r 30`                      | Convert to 30fps frame rate                             |
| `-crf 20`                    | Video quality (lower value means higher quality, recommended 18-23)                   |
| `-preset slow`               | Balance between encode speed and compression ratio (slow means high compression/high quality)              |
| `-c:a aac`                   | Encode audio in AAC format                              |
| `-b:a 128k`                  | Set audio bitrate to 128kbps                         |
| `-ar 48000`                  | Set audio sampling rate to 48kHz (recommended for iOS)                |
| `-movflags +faststart`       | Places the index at the beginning of the video, **speeding up streaming playback on Web and iOS** |

---

Videos converted with these settings can be expected to have high compatibility and smooth playback on Apple devices such as iPhones and iPads.

---

You can adjust file size and image quality by changing the resolution and bitrate as needed. Try setting `-crf` to around 18 if you need high quality, or 22-25 if you want to reduce the file size.
