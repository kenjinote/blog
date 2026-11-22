---
title: "Allow Raw HTML in Hugo Markdown"
date: "2023-01-17T19:20:32+09:00"
lastmod: 2026-11-23
slug: "HUGOでHTMLタグを使う"
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Learn how to enable raw HTML in Hugo Markdown with YAML, TOML, and JSON examples, plus the security trade-off and when not to enable it."
---

Hugo’s Goldmark Markdown renderer does not render raw HTML by default. If you need it, set `markup.goldmark.renderer.unsafe` to `true` in your site configuration. Hugo supports YAML, TOML, and JSON configuration files. For example, in `hugo.yaml`:

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

Or in `hugo.json`:

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

The default is `false`. Setting `unsafe: true` allows raw HTML in Markdown to pass through, weakening Hugo’s content trust boundary. Do not enable it when the site processes Markdown from untrusted contributors or external input. Use it only when you control and review the content, and understand the implications. For complex layouts, a shortcode or an HTML content file may be a better fit.

References: [Configure markup](https://gohugo.io/configuration/markup/) · [Hugo’s security model](https://gohugo.io/about/security/)
