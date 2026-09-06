---
title: "Comment configurer Twitter Card avec PaperMod"
slug: "PaperModでTwitter Cardを設定する方法"
date: 2022-09-10T18:41:22+09:00
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.png"
categories: ["ブログ運営"]
---
# Introduction
Le thème PaperMod prend en charge Twitter Card.
Cependant, les paramètres de Twitter Card doivent être écrits dans le `config.toml` ou dans les informations d'en-tête du `*.md` de chaque article.
Si vous le configurez à la fois dans chaque article et dans le `config.toml`, les informations d'en-tête de chaque article seront prioritaires.

# Comment configurer
## config.toml
Dans `config.toml`, ajoutez un élément appelé `images` sous `[params]`.
Dans `images`, décrivez le chemin de l'image à afficher sur Twitter Card.
Si vous placez l'image dans le dossier `static`, il suffit de spécifier uniquement le nom du fichier.

```
[params]
  images = ["twitter_card.jpg"]
```

Structure des dossiers
```
root
│  config.toml (Écrire ici)
├─content
│  └─posts
│      └─Dossier de l'article
│         │  index.md (Écrire ici)
│         └─images
│             cover.png (Placer ici)
└─static
    twitter_card.jpg (Placer ici)
```

## Informations d'en-tête de chaque article
Dans les informations d'en-tête de chaque article, ajoutez un élément appelé `image` sous `cover`.
Si vous définissez `relative` sur `true`, vous pouvez spécifier avec un chemin relatif à partir du `*.md` de l'article.

```
cover:
  image: "images/cover.jpg"
  relative: true
```

### Si vous ne souhaitez pas l'afficher en haut de l'article
Si vous ne souhaitez pas afficher l'image de couverture en haut de l'article, ajoutez un élément appelé `hidden` sous `cover` et définissez-le sur `true`.
```
cover:
  image: "images/cover.jpg"
  relative: true
  hidden: true
```

# À propos de la taille de l'image

Dans les spécifications actuelles de PaperMod, il semble que la taille de Twitter Card ne prenne en charge que `summary_large_image`.
La taille appropriée (résolution) de `summary_large_image` a plusieurs théories, mais autour de `800 x 418` (ratio d'image 1.91:1) semble être bon.

[Site de référence 1](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary-card-with-large-image)
[Site de référence 2](https://developers.facebook.com/docs/sharing/best-practices)


Si possible, nous vous recommandons de redimensionner la taille de l'image avant de publier.

# Comment vérifier les paramètres
Pour vérifier les paramètres de Twitter Card, utilisez le [Twitter Card Validator](https://cards-dev.twitter.com/validator).
Cependant, comme l'aperçu ne s'est pas affiché correctement dans mon environnement, si l'aperçu n'apparaît pas, je vous recommande de vérifier une fois avant de publier en utilisant un compte privé ou similaire.
