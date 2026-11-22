---
title: "Rohes HTML in Hugo-Markdown erlauben"
date: "2023-01-17T19:20:32+09:00"
lastmod: 2026-11-23
slug: "HUGOでHTMLタグを使う"
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "So erlauben Sie rohes HTML in Hugo-Markdown mit Beispielen für YAML, TOML und JSON – einschließlich Sicherheitsrisiko und Fällen, in denen Sie die Option nicht aktivieren sollten."
---

Hugos Goldmark-Markdown-Renderer gibt rohes HTML standardmäßig nicht aus. Wenn Sie es benötigen, setzen Sie `markup.goldmark.renderer.unsafe` in der Site-Konfiguration auf `true`. Hugo unterstützt YAML-, TOML- und JSON-Konfigurationsdateien. Zum Beispiel in `hugo.yaml`:

```yaml
markup:
  goldmark:
    renderer:
      unsafe: true
```

In `hugo.toml`:

```toml
[markup.goldmark.renderer]
  unsafe = true
```

Oder in `hugo.json`:

```json
{
  "markup": {
    "goldmark": {
      "renderer": {
        "unsafe": true
      }
    }
  }
}
```

Der Standardwert ist `false`. Mit `unsafe: true` wird rohes HTML im Markdown ausgegeben; dadurch wird Hugos Vertrauensgrenze für Inhalte geschwächt. Aktivieren Sie die Option nicht, wenn die Site Markdown von nicht vertrauenswürdigen Mitwirkenden oder aus externen Eingaben verarbeitet. Verwenden Sie sie nur für Inhalte, die Sie kontrollieren und prüfen, und wenn Sie die Folgen verstehen. Für komplexe Layouts eignen sich Shortcodes oder HTML-Dateien möglicherweise besser.

Quellen: [Markup konfigurieren](https://gohugo.io/configuration/markup/) · [Hugos Sicherheitsmodell](https://gohugo.io/about/security/)
