---
title: '使用 CSS 變更 Hugo PaperMod 主題的配色與色彩主題方法'
slug: "PaperModの配色変更"
date: 2022-09-07T15:30:21+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["部落格營運"]
description: '說明如何自訂 Hugo 的 PaperMod 主題的整體配色。介紹如何編輯包含背景色、文字顏色、程式碼區塊等樣式定義的 CSS (blank.css)，並提供具體的變數設定範例，以套用您喜歡的配色方案。'
---
我更改了 PaperMod 主題的配色方案。更改方法參考了以下連結。

https://github.com/adityatelange/hugo-PaperMod/discussions/645

CSS 的路徑如下。

`themes/PaperMod/assets/css/extended/blank.css`

```
:root {
    --entry: #fbf7ef;
    --primary: rgba(113, 103, 91, 1.00);
    --secondary: rgba(113, 103, 91, 0.95);
    --tertiary: rgba(113, 103, 91, 0.50);
    --content: rgba(113, 103, 91, 0.85);
    --hljs-bg: #34231B;
    --code-bg: #ebe4d7;
    --border: #fdfaf5;
    --theme: #fbf7ef;
}
.dark {
}
```

黑暗模式暫時沒有更改。
