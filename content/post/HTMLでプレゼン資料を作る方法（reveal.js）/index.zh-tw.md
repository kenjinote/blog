---
date: 2023-04-06T23:23:46+09:00
lastmod: 2026-11-23
title: 'reveal.js使用教學：透過HTML與Markdown製作簡報資料'
slug: "HTMLで簡報資料を作る方法（reveal.js）"
tags: ["HTML", "reveal.js", "簡報"]
draft: false
image: "img.webp"
categories: ["programming"]
description: '解說能透過HTML與Markdown直覺地製作簡報的工具「reveal.js」的安裝與基本用法。除了支援動畫與輸出PDF外，我們也將介紹其與Git等版本控制系統極度契合的活用方法。'
---

# 如何使用 HTML 製作簡報資料

reveal.js 是一個使用 HTML 和 Markdown 的簡報製作工具，具有以下功能：

- 豐富的簡報功能，如數學公式、動畫和滑動操作
- 主題和版面可以自訂
- 支援多種裝置的導航功能，如滑鼠、鍵盤和觸控板
- 提供進階功能，如自動播放投影片和嵌入影片
- 支援匯出為 PDF 格式

透過這些功能，使用者可以輕鬆建立互動且具吸引力的簡報。

# reveal.js 的安裝與使用方法

最簡單的使用方法是從以下頁面下載整個 ZIP 檔案並解壓縮。

1. 打開 [https://revealjs.com/installation](https://revealjs.com/installation) 並從連結下載 `master.zip`
2. 在瀏覽器中打開解壓縮資料夾內的 index.html
3. 修改 index.html 以建立自己的簡報資料

※ demo.html 中寫有展示用的 HTML 程式碼，可以作為參考。

# 應用方式

製作好的簡報資料可以直接作為網頁發布，或匯出為 PDF。
此外，由於簡報的原始碼是文字，因此很容易使用版本控制系統進行管理。

似乎也可以使用 Markdown 格式建立簡報資料。

# 建立基本投影片

最簡單的方式是下載最新版 Basic Setup ZIP、解壓縮後編輯 `index.html`。如以下 HTML 範例所示，每張投影片都放在 `<section>` 中。Basic Setup 範例檔已包含所需的樣式與初始化程式碼。

```html
<div class="reveal">
  <div class="slides">
    <section>Slide 1</section>
    <section>Slide 2</section>
    <section>Reveal this item <span class="fragment">when activated</span></section>
  </div>
</div>
```

# 使用 Markdown 撰寫投影片

內建的 Markdown 外掛可讓你直接在 HTML 檔中撰寫 Markdown。以 `---` 分隔水平投影片，並將以下範例加入 `index.html`。若要載入外部 Markdown 檔案，必須使用本機網頁伺服器。

```html
<section data-markdown>
  <textarea data-template>
## Slide 1
---
## Slide 2
  </textarea>
</section>
```

# 開發環境設定

若需要本機伺服器或原始碼開發工具，請使用官方 Full Setup。執行下列命令後，在瀏覽器開啟 `http://localhost:8000`。

```sh
git clone https://github.com/hakimel/reveal.js.git
cd reveal.js
npm install
npm start
```

# 匯出 PDF

在網址結尾加上 `?print-pdf`。在 Chrome 或 Chromium 的列印畫面選擇另存為 PDF、橫向、無邊界，並啟用背景圖形。官方指南確認的瀏覽器為 Chrome 與 Chromium。

# 講者備註

按 `S` 可在另一個視窗開啟講者檢視。在投影片的 `<aside class="notes">` 中加入備註。本機使用講者檢視需要網頁伺服器。

```html
<section>
  <h2>Slide</h2>
  <aside class="notes">Notes visible to the presenter only</aside>
</section>
```

# 官方文件

- [Installation](https://revealjs.com/installation/)
- [Markup](https://revealjs.com/markup/)
- [Markdown](https://revealjs.com/markdown/)
- [Fragments](https://revealjs.com/fragments/)
- [PDF export](https://revealjs.com/pdf-export/)
- [Speaker view](https://revealjs.com/speaker-view/)

請確認投影片中圖片與影片的使用權，並檢查公開資料是否含有機密資訊或不應公開的講者備註。
