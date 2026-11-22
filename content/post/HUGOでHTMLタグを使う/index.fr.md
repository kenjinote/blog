---
title: "Autoriser le HTML brut dans le Markdown de Hugo"
date: "2023-01-17T19:20:32+09:00"
lastmod: 2026-11-23
slug: "HUGOでHTMLタグを使う"
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Apprenez à autoriser le HTML brut dans le Markdown de Hugo avec des exemples YAML, TOML et JSON, ainsi que les risques de sécurité et les cas où ne pas activer cette option."
---

Par défaut, le moteur Markdown Goldmark de Hugo ne restitue pas le HTML brut. Si vous en avez besoin, définissez `markup.goldmark.renderer.unsafe` sur `true` dans la configuration du site. Hugo accepte les fichiers de configuration YAML, TOML et JSON. Par exemple, dans `hugo.yaml` :

```yaml
markup:
  goldmark:
    renderer:
      unsafe: true
```

Dans `hugo.toml` :

```toml
[markup.goldmark.renderer]
  unsafe = true
```

Ou dans `hugo.json` :

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

La valeur par défaut est `false`. Le réglage `unsafe: true` laisse passer le HTML brut du Markdown et affaiblit la frontière de confiance appliquée par Hugo au contenu. Ne l’activez pas si le site traite du Markdown fourni par des contributeurs non fiables ou issu de sources externes. Utilisez-le uniquement pour du contenu que vous contrôlez et vérifiez, en comprenant les conséquences. Pour des mises en page complexes, un shortcode ou un fichier de contenu HTML peut être plus approprié.

Références : [Configurer le balisage](https://gohugo.io/configuration/markup/) · [Modèle de sécurité de Hugo](https://gohugo.io/about/security/)
