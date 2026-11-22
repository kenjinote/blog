---
title: "Permitir HTML sin procesar en Markdown de Hugo"
date: "2023-01-17T19:20:32+09:00"
lastmod: 2026-11-23
slug: "HUGOでHTMLタグを使う"
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Aprende a habilitar HTML sin procesar en Markdown de Hugo con ejemplos en YAML, TOML y JSON, además de sus riesgos de seguridad y cuándo no activarlo."
---

El renderizador Markdown Goldmark de Hugo no muestra HTML sin procesar de forma predeterminada. Si lo necesitas, establece `markup.goldmark.renderer.unsafe` en `true` en la configuración del sitio. Hugo admite archivos de configuración YAML, TOML y JSON. Por ejemplo, en `hugo.yaml`:

```yaml
markup:
  goldmark:
    renderer:
      unsafe: true
```

En `hugo.toml`:

```toml
[markup.goldmark.renderer]
  unsafe = true
```

O en `hugo.json`:

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

El valor predeterminado es `false`. `unsafe: true` permite que el HTML sin procesar de Markdown llegue a la salida y debilita el límite de confianza de contenido de Hugo. No lo actives si el sitio procesa Markdown de colaboradores no confiables o de fuentes externas. Úsalo solo con contenido que controles y revises, y si comprendes sus implicaciones. Para diseños complejos, un shortcode o un archivo de contenido HTML puede ser más adecuado.

Referencias: [Configurar el marcado](https://gohugo.io/configuration/markup/) · [Modelo de seguridad de Hugo](https://gohugo.io/about/security/)
