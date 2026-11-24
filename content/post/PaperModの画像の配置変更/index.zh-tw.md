---
title: "調整 PaperMod 文章列表中封面圖片的大小與位置"
slug: "PaperModの圖片の配置変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "使用 PaperMod 的擴充 CSS 功能與 CSS Grid 縮小文章卡片封面圖，並將它放在摘要旁邊。"
date: "2022-09-11T18:50:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

本文範例會縮小 PaperMod 文章列表卡片中的封面圖，並將它放在標題下方、摘要旁邊。透過網站端的擴充 CSS 完成，不必直接修改主題內附的樣式表或版型。選擇器依賴 PaperMod 類別名稱，更新主題後請在瀏覽器檢查結果。

## 新增擴充 CSS

在網站根目錄建立 `assets/css/extended/custom.css`。PaperMod 會將此目錄中的 CSS 與主題樣式一併載入。CSS Grid 可調整視覺排列，同時保留現有 HTML 結構。

```css
/* Add to assets/css/extended/custom.css */
.post-entry {
    display: grid;
    grid-template-columns: minmax(0, 150px) minmax(0, 1fr);
    grid-template-areas:
        "cover title"
        "cover summary"
        "cover meta";
    column-gap: 1rem;
    align-items: start;
}

.post-entry > .entry-cover {
    grid-area: cover;
    margin-bottom: 0;
}

.post-entry > .entry-header {
    grid-area: title;
    min-width: 0;
}

.post-entry > .entry-content {
    grid-area: summary;
    min-width: 0;
}

.post-entry > .entry-footer {
    grid-area: meta;
}

.post-entry .entry-cover img {
    display: block;
    width: 100%;
    height: auto;
}

@media (max-width: 600px) {
    .post-entry {
        grid-template-columns: minmax(0, 96px) minmax(0, 1fr);
        column-gap: 0.75rem;
    }
}
```

## 調整窄螢幕版面

在窄螢幕上縮小欄寬與間距，讓摘要維持易讀。可依設計調整 150px 和斷點。`height: auto` 會保留圖片比例。只有需要統一裁切形狀時才加入 `aspect-ratio` 和 `object-fit: cover`。

## 避免直接修改主題檔案

PaperMod 文件說明，`blank.css` 是擴充 CSS 目錄沒有檔案時使用的佔位檔。不必修改主題內附的 `post-entry.css`，也不必刪除其中註解掉的 `/* width: 100%; */`；移除 CSS 註解不會改變樣式。若要更改 HTML 結構，可將版型複製到網站的 `layouts/` 目錄覆寫，但主題更新後必須維護這份副本。

## 檢查版面

執行 Hugo，並在寬螢幕和窄螢幕檢查首頁、標籤頁與分類頁列表。圖片、標題、摘要和中繼資料不可互相遮擋，覆蓋整張卡片的連結也應正常運作。若主題更新變更類別名稱或 HTML，請調整 CSS。此範例只影響列表卡片封面，不影響文章內文圖片。

## 參考資料

- [PaperMod FAQ: bundling custom CSS and overriding templates](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current post-entry CSS selectors](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/common/post-entry.css)
- [PaperMod discussion #159](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)
