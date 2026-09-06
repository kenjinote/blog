---
title: "Verwendung von HTML-Tags in HUGO"
slug: "verwendung-von-html-tags-in-hugo"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.png"
categories: ["Blog-Management"]
---

Standardmäßig erlaubt HUGO die Verwendung von HTML-Tags in Artikeln nicht, aber Sie können dies aktivieren, indem Sie die folgende Beschreibung in die config.toml einfügen.

```toml
[markup.goldmark.renderer]
    unsafe = true
```

Referenz: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)
