---
title: "HugoでMarkdown内のHTMLを有効にする方法"
date: "2023-01-17T19:20:32+09:00"
lastmod: 2026-11-23
slug: "HUGOでHTMLタグを使う"
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Hugo Goldmarkの設定でMarkdown内の生HTMLを表示する方法を、YAML・TOML・JSONの例とセキュリティ上の注意とともに説明します。"
---

HugoのMarkdownレンダラーGoldmarkは、既定ではMarkdown内の生HTMLを出力しません。必要な場合は、サイト設定の `markup.goldmark.renderer.unsafe` を `true` にします。現在のHugoはYAML、TOML、JSONの設定ファイルに対応しています。たとえば `hugo.yaml` では次のように書けます。

```yaml
markup:
  goldmark:
    renderer:
      unsafe: true
```

TOMLの `hugo.toml` では次のとおりです。

```toml
[markup.goldmark.renderer]
  unsafe = true
```

JSONの `hugo.json` では次のように設定します。

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

既定値は `false` です。`unsafe: true` はMarkdown内の生HTMLをそのまま出力できるようにしますが、Hugoが想定するコンテンツの信頼境界を弱めます。信頼できない投稿者や外部入力のMarkdownを処理するサイトでは有効にしないでください。自分で管理し、内容を確認できるファイルだけを扱う場合に限り、影響を理解したうえで使用してください。複雑なレイアウトにはショートコードやHTML形式のコンテンツが適する場合もあります。

参考: [Configure markup](https://gohugo.io/configuration/markup/) · [Hugoのセキュリティモデル](https://gohugo.io/about/security/)
