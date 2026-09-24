---
title: 'Comment activer les balises HTML dans Hugo (configuration de config.toml)'
slug: "HUGOでHTMLタグを使う"
date: "2026-09-24T16:08:36+09:00"
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Nous expliquons comment activer l''utilisation directe de balises HTML dans les articles Markdown du générateur de site statique Hugo. Il vous suffit d''ajouter le paramètre unsafe à markup.goldmark.renderer dans le fichier config.toml.'
---

Par défaut, HUGO n'autorise pas l'utilisation de balises HTML dans les articles, mais vous pouvez l'activer en ajoutant la description suivante au config.toml.

```toml
[markup.goldmark.renderer]
    unsafe = true
```

Référence: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)
