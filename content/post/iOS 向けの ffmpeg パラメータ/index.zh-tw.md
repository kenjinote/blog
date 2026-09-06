---
title: "iOS 的 ffmpeg 參數"
slug: "iOS 向けの ffmpeg パラメータ"
date: 2025-03-02T04:16:07+09:00
tags: ["iOS", "ffmpeg"]
draft: false
image: "img.png"
categories: ["PC・ガジェット"]
---

# 針對 iOS 最佳化的 ffmpeg 轉換參數

我們將介紹 `ffmpeg` 命令來轉換影片，以便在 iOS 裝置（iPhone 和 iPad）上流暢播放。

```bash
ffmpeg -i input.mp4 \
-c:v libx264 -profile:v high -level 4.1 \
-vf "scale=1920:-2" -r 30 \
-crf 20 -preset slow \
-c:a aac -b:a 128k -ar 48000 \
-movflags +faststart output.mp4
```

### 各選項的含義（簡要說明）

| 選項                        | 說明                                          |
| ---------------------------- | ------------------------------------------- |
| `-i input.mp4`               | 輸入檔案（要轉換的影片）                              |
| `-c:v libx264`               | 使用 H.264 編碼影片（支援 iOS）                       |
| `-profile:v high -level 4.1` | 在 iOS 上廣泛相容的設定檔和等級                      |
| `-vf "scale=1920:-2"`        | 調整大小為 1920px 寬，高度會自動調整以保持寬高比               |
| `-r 30`                      | 轉換為 30fps 的幀率                             |
| `-crf 20`                    | 影片品質（數值越低畫質越高，建議 18-23）                   |
| `-preset slow`               | 編碼速度與壓縮率的平衡（slow 表示高壓縮、高畫質）              |
| `-c:a aac`                   | 音訊以 AAC 格式編碼                              |
| `-b:a 128k`                  | 將音訊位元率設定為 128kbps                         |
| `-ar 48000`                  | 將音訊取樣率設定為 48kHz（iOS 建議）                |
| `-movflags +faststart`       | 在影片開頭放置索引， **加速在 Web 和 iOS 上的串流播放** |

---

使用這些設定轉換的影片，預期在 iPhone 和 iPad 等 Apple 裝置上具有高相容性且能流暢播放。

---

如有需要，您可以透過變更解析度或位元率來調整檔案大小和畫質。如果需要高畫質，請嘗試將 `-crf` 設定為 18 左右；如果想要縮小檔案大小，請設定為 22-25。
