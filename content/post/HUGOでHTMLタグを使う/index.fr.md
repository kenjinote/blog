---
title: "Utiliser des balises HTML dans HUGO"
slug: "utiliser-des-balises-html-dans-hugo"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.png"
categories: ["Gestion de blog"]
---

Par défaut, HUGO n'autorise pas l'utilisation de balises HTML dans les articles, mais vous pouvez l'activer en ajoutant la description suivante au config.toml.

```toml
[markup.goldmark.renderer]
    unsafe = true
```

Référence: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)
