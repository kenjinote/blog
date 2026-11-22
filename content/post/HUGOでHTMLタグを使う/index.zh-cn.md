---
title: "在 Hugo Markdown 中启用原始 HTML"
date: "2023-01-17T19:20:32+09:00"
lastmod: 2026-11-23
slug: "HUGOでHTMLタグを使う"
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "介绍如何在 Hugo Markdown 中启用原始 HTML，并提供 YAML、TOML 和 JSON 示例，同时说明安全风险及不应启用此选项的情况。"
---

Hugo 的 Goldmark Markdown 渲染器默认不会输出原始 HTML。如有需要，可在站点配置中将 `markup.goldmark.renderer.unsafe` 设为 `true`。Hugo 支持 YAML、TOML 和 JSON 配置文件。例如，在 `hugo.yaml` 中：

```yaml
markup:
  goldmark:
    renderer:
      unsafe: true
```

在 `hugo.toml` 中：

```toml
[markup.goldmark.renderer]
  unsafe = true
```

或在 `hugo.json` 中：

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

默认值为 `false`。`unsafe: true` 会允许 Markdown 中的原始 HTML 进入输出，并削弱 Hugo 对内容设置的信任边界。如果网站会处理不可信贡献者提供的 Markdown 或外部输入，请不要启用此选项。仅在内容由你控制并经过检查、且你了解其影响时使用。复杂布局也可以考虑使用 shortcode 或 HTML 内容文件。

参考：[配置 markup](https://gohugo.io/configuration/markup/) · [Hugo 安全模型](https://gohugo.io/about/security/)
