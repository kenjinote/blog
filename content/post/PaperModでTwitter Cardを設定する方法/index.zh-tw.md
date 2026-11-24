---
title: "如何在 Hugo PaperMod 中設定 Twitter Card（X 卡片）"
slug: "PaperModでTwitter Cardを設定する方法"
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "依照 PaperMod 文件設定 X 卡片圖片，並檢查產生的 HTML 與 X 發文編輯器中的預覽。"
date: "2022-09-10T18:41:22+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PaperMod 可產生 Open Graph 和 Twitter Card 中繼資料。輸出會因佈景主題版本和自訂版型而異，因此請檢查已發布的 HTML，不要假設某個設定範例一定會產生特定卡片。

## 全站設定

PaperMod 的 SEO 中繼資料會在 production 建置時啟用。請將網站環境設為 production。

```toml
[params]
  env = "production"
```

若要設定全站預設圖片，可將圖片放在 `static` 目錄並於此設定。文章未指定專屬圖片時，這張圖可能成為候選圖片。也請確認部署後實際輸出的圖片 URL。

```toml
[params]
  images = ["/twitter-card-1200x630.webp"]
```

## 個別文章圖片

若要為個別文章指定圖片，請將 Page Bundle 中的圖片設為 `cover.image`。`relative: true` 表示使用相對於 Bundle 的路徑。PaperMod 文件優先使用封面圖；若沒有封面圖，可能使用頁面的 `images` 清單，再使用符合條件的 Bundle 圖片。

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
```

## 隱藏文章中的封面

依 PaperMod 變數文件，`cover.hidden: true` 會在文章畫面隱藏封面，但保留結構化中繼資料中的圖片。如果圖片只供社群卡片使用，這項設定很方便。若使用主題 fork 或自訂版型，請檢查產生的 HTML。

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
  hidden: true
```

## 卡片類型與圖片尺寸

舊文所說「PaperMod 僅支援 `summary_large_image`」及「固定為 800×418」不能套用至所有情況。卡片類型可能取決於主題版本或網站版型。寬幅圖片可將 1200×630（約 1.90:1）作為實用的設計參考，但這不是 X 保證的顯示規格。

## 檢查輸出與預覽

以 production 設定建置後，檢查文章 HTML 中的 `twitter:card`、`twitter:image`、`og:image`、標題和描述。圖片 URL 必須可透過 HTTPS 公開直接存取，且不需登入。X 在 2022 年移除 Card Validator 的預覽功能，並建議改用發文編輯器。將連結貼入編輯器，在不發布的情況下查看預覽。快取更新可能需要時間。

已於 2026-11-24 依照連結的 PaperMod 文件與 X 開發者論壇核對。主題 fork、自訂版型及 X 的變更都可能影響輸出。

## 參考資料

- [PaperMod: Features and Twitter Cards](https://github.com/adityatelange/hugo-PaperMod/wiki/Features)
- [PaperMod: Variables](https://github.com/adityatelange/hugo-PaperMod/wiki/Variables)
- [Hugo: Page bundles](https://gohugo.io/content-management/page-bundles/)
- [X Developer Community: Card Validator preview removal](https://devcommunity.x.com/t/card-validator-preview-removal/175006)
