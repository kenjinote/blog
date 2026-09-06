---
title: "在 HUGO 中使用 HTML 標籤"
slug: "在-hugo-中使用-html-標籤"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.png"
categories: ["部落格營運"]
---

預設情況下，HUGO 不允許在文章中使用 HTML 標籤，但您可以透過在 config.toml 中加入以下描述來啟用它。

```toml
[markup.goldmark.renderer]
    unsafe = true
```

參考: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)
