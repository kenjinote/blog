---
title: 'How to Enable HTML Tags in Hugo (config.toml Settings)'
slug: "HUGOでHTMLタグを使う"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["Blog Management"]
description: 'We explain how to enable directly writing and using HTML tags within the Markdown articles of the static site generator Hugo. It is completed simply by adding the unsafe setting of markup.goldmark.renderer to config.toml.'
---

By default, HUGO does not allow the use of HTML tags in articles, but you can enable them by adding the following to your config.toml.

```toml
[markup.goldmark.renderer]
    unsafe = true
```

Reference: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)
