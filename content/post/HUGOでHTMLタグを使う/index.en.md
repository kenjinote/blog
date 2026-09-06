---
title: 'Using HTML Tags in HUGO'
slug: "HUGOでHTMLタグを使う"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.png"
categories: ["Blog Management"]
---

By default, HUGO does not allow the use of HTML tags in articles, but you can enable them by adding the following to your config.toml.

```toml
[markup.goldmark.renderer]
    unsafe = true
```

Reference: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)
