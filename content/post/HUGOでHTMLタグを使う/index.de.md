---
title: 'Wie man HTML-Tags in Hugo aktiviert (Konfiguration der config.toml)'
slug: "verwendung-von-html-tags-in-hugo"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["Blog-Management"]
description: 'Wir erklären, wie Sie in Markdown-Artikeln des Static Site Generators Hugo direkt HTML-Tags schreiben und verwenden können. Es ist so einfach wie das Hinzufügen der unsafe-Einstellung zu markup.goldmark.renderer in der config.toml.'
---

Standardmäßig erlaubt HUGO die Verwendung von HTML-Tags in Artikeln nicht, aber Sie können dies aktivieren, indem Sie die folgende Beschreibung in die config.toml einfügen.

```toml
[markup.goldmark.renderer]
    unsafe = true
```

Referenz: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)
