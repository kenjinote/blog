---
title: '在Hugo中啟用HTML標籤的方法（config.toml設定）'
slug: "HUGOでHTMLタグを使う"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["部落格營運"]
description: '為您解說如何在靜態網站產生器Hugo的Markdown文章中，直接撰寫並使用HTML標籤的方法。只要在config.toml中新增markup.goldmark.renderer的unsafe設定即可完成。'
---

預設情況下，HUGO 不允許在文章中使用 HTML 標籤，但您可以透過在 config.toml 中加入以下描述來啟用它。

```toml
[markup.goldmark.renderer]
    unsafe = true
```

參考: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)
