---
title: "在 Hugo Markdown 中啟用原始 HTML"
date: "2023-01-17T19:20:32+09:00"
lastmod: 2026-11-23
slug: "HUGOでHTMLタグを使う"
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "介紹如何在 Hugo Markdown 中啟用原始 HTML，並提供 YAML、TOML 與 JSON 範例，同時說明安全風險及不應啟用此選項的情況。"
---

Hugo 的 Goldmark Markdown 渲染器預設不會輸出原始 HTML。如有需要，可在網站設定中將 `markup.goldmark.renderer.unsafe` 設為 `true`。Hugo 支援 YAML、TOML 和 JSON 設定檔。例如，在 `hugo.yaml` 中：

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

預設值為 `false`。`unsafe: true` 會讓 Markdown 中的原始 HTML 進入輸出，並削弱 Hugo 對內容設定的信任邊界。如果網站會處理不可信投稿者提供的 Markdown 或外部輸入，請勿啟用此選項。只有在內容由你掌控並經過檢查，且你了解其影響時才使用。複雜版面也可考慮使用 shortcode 或 HTML 內容檔。

參考：[設定 markup](https://gohugo.io/configuration/markup/) · [Hugo 安全模型](https://gohugo.io/about/security/)
