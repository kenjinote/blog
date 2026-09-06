---
title: "如何在 PaperMod 中設定 Twitter Card"
slug: "PaperModでTwitter Cardを設定する方法"
date: 2022-09-10T18:41:22+09:00
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.png"
categories: ["ブログ運営"]
---
# 簡介
PaperMod 主題支援 Twitter Card。
但是，Twitter Card 的設定必須寫在 `config.toml` 或每篇文章的 `*.md` 的標頭資訊中。
如果您在每篇文章和 `config.toml` 中都進行了設定，則每篇文章的標頭資訊將優先。

# 設定方法
## config.toml
在 `config.toml` 中，於 `[params]` 下方新增一個名為 `images` 的項目。
在 `images` 中，描述要在 Twitter Card 顯示的圖片路徑。
如果您將圖片放在 `static` 資料夾中，只需指定檔案名稱即可。

```
[params]
  images = ["twitter_card.jpg"]
```

資料夾結構
```
root
│  config.toml (寫在這裡)
├─content
│  └─posts
│      └─文章資料夾
│         │  index.md (寫在這裡)
│         └─images
│             cover.png (放在這裡)
└─static
    twitter_card.jpg (放在這裡)
```

## 每篇文章的標頭資訊
在每篇文章的標頭資訊中，於 `cover` 下方新增一個名為 `image` 的項目。
如果將 `relative` 設定為 `true`，您可以透過文章的 `*.md` 的相對路徑來指定。

```
cover:
  image: "images/cover.jpg"
  relative: true
```

### 如果不想顯示在文章頂部
如果您不想在文章頂部顯示封面圖片，請在 `cover` 下方新增一個名為 `hidden` 的項目，並將其設定為 `true`。
```
cover:
  image: "images/cover.jpg"
  relative: true
  hidden: true
```

# 關於圖片大小

在 PaperMod 目前的規格中，Twitter Card 的大小似乎只支援 `summary_large_image`。
對於 `summary_large_image` 的合適大小（解析度）有各種說法，但大約 `800 x 418`（圖片比例 1.91:1）似乎不錯。

[參考網站 1](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary-card-with-large-image)
[參考網站 2](https://developers.facebook.com/docs/sharing/best-practices)


如果可能的話，建議在發布前調整圖片大小。

# 如何檢查設定
要檢查 Twitter Card 的設定，請使用 [Twitter Card Validator](https://cards-dev.twitter.com/validator)。
但是，由於預覽在我的環境中無法正確顯示，如果無法顯示預覽，我建議您在發布前使用私人帳號等檢查一次。
