---
title: "使用 CSS 變數自訂 Hugo PaperMod 配色"
slug: "PaperModの配色変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "透過擴充 CSS 覆寫 PaperMod 的淺色與深色主題變數，並檢查文字對比度。"
date: "2022-09-07T15:30:21+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PaperMod 的色彩可透過 CSS 自訂屬性（變數）調整。請將覆寫樣式放在網站的 `assets/css/extended/`，不要直接編輯主題檔案，如此在主題更新時較容易保留修改。以下範例提供暖色淺色主題與深色主題，可依網站需求調整。

## 深色模式與目前變數

目前 PaperMod 透過在 `html` 元素設定 `data-theme="dark"` 切換深色模式。舊範例若只選取 `.dark`，可能無法符合目前的主題選擇器。`--hljs-bg` 也不是目前的程式碼區塊背景變數；目前使用的名稱是 `--code-block-bg`。

```css
/* Save as assets/css/extended/theme-colors.css */
:root {
    color-scheme: light;
    --theme: #fbf7ef;
    --entry: #fffdfa;
    --primary: #433a32;
    --secondary: #665b50;
    --tertiary: #8b7f72;
    --content: #453d35;
    --code-block-bg: #34231b;
    --code-bg: #efe7da;
    --border: #ddd3c5;
}

:root[data-theme="dark"] {
    color-scheme: dark;
    --theme: #1d1e20;
    --entry: #22252a;
    --primary: #e8e6e1;
    --secondary: #b5b2ac;
    --tertiary: #55575c;
    --content: #d2d0ca;
    --code-block-bg: #17181a;
    --code-bg: #37383e;
    --border: #48484c;
}
```

## 文字對比度

範例中的一般文字顏色 `--primary` 和 `--content` 與背景有明顯對比。`--primary` 對 `--theme` 的範例對比度在淺色模式約為 10.4:1，深色模式約為 13.4:1。WCAG 2.2 AA 對一般文字要求 4.5:1；語法醒目顯示顏色、連結、邊框和其他狀態仍需個別檢查。

## 新增並檢查擴充 CSS

在網站根目錄將樣式表存為 `assets/css/extended/theme-colors.css`。PaperMod FAQ 說明，`assets/css/extended/` 中的 CSS 會和主題樣式一起打包。執行 Hugo 後檢查淺色／深色切換、卡片、內文、行內程式碼、程式碼區塊和連結。

## 範圍

此配色只是範例，無法保證每段文字、圖片和互動元件都符合無障礙要求。語法醒目顯示顏色與 `--code-block-bg` 分開定義，因此修改程式碼區塊背景後，請再次檢查程式碼的可讀性。

## 參考資料

- [PaperMod FAQ: custom CSS and theme assets](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current theme color variables](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/core/theme-vars.css)
- [PaperMod discussion: changing background and text colors](https://github.com/adityatelange/hugo-PaperMod/discussions/645)
- [W3C: WCAG 2.2 contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum)
