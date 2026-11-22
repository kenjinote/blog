---
title: "Permitir HTML bruto no Markdown do Hugo"
date: "2023-01-17T19:20:32+09:00"
lastmod: 2026-11-23
slug: "HUGOでHTMLタグを使う"
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Aprenda a habilitar HTML bruto no Markdown do Hugo com exemplos em YAML, TOML e JSON, além dos riscos de segurança e das situações em que não se deve ativar a opção."
---

O renderizador Markdown Goldmark do Hugo não renderiza HTML bruto por padrão. Se precisar desse recurso, defina `markup.goldmark.renderer.unsafe` como `true` na configuração do site. O Hugo aceita arquivos de configuração YAML, TOML e JSON. Por exemplo, em `hugo.yaml`:

```yaml
markup:
  goldmark:
    renderer:
      unsafe: true
```

Em `hugo.toml`:

```toml
[markup.goldmark.renderer]
  unsafe = true
```

Ou em `hugo.json`:

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

O valor padrão é `false`. `unsafe: true` permite que o HTML bruto do Markdown seja incluído na saída e enfraquece a fronteira de confiança de conteúdo do Hugo. Não ative a opção se o site processar Markdown de colaboradores não confiáveis ou de entradas externas. Use-a somente com conteúdo que você controla e revisa, e se compreender as implicações. Para layouts complexos, um shortcode ou arquivo de conteúdo HTML pode ser mais adequado.

Referências: [Configurar markup](https://gohugo.io/configuration/markup/) · [Modelo de segurança do Hugo](https://gohugo.io/about/security/)
