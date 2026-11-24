---
title: "Configurer les Twitter Cards (X Cards) dans Hugo PaperMod"
slug: "PaperModでTwitter Cardを設定する方法"
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "Configurez les images des cartes X avec les paramètres documentés de PaperMod, puis vérifiez le HTML généré et l’aperçu dans le compositeur de publication X."
date: "2022-09-10T18:41:22+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PaperMod peut générer les métadonnées Open Graph et Twitter Card. Le résultat varie selon la version du thème et les modèles personnalisés ; vérifiez le HTML publié au lieu de supposer qu’un exemple produit une carte précise.

## Configuration du site

Les métadonnées SEO de PaperMod sont activées pour les compilations de production. Réglez l’environnement du site sur production.

```toml
[params]
  env = "production"
```

Pour une image de repli à l’échelle du site, placez une image dans `static` et configurez-la ici. Elle peut être utilisée lorsqu’un article ne fournit pas sa propre image. Vérifiez l’URL générée sur le site publié.

```toml
[params]
  images = ["/twitter-card-1200x630.webp"]
```

## Image par article

Pour une image propre à un article, définissez `cover.image` avec une image du Page Bundle. `relative: true` indique un chemin relatif au bundle. PaperMod indique que l’image de couverture est prioritaire ; à défaut, la liste `images` de l’article puis certaines images du bundle peuvent être utilisées.

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
```

## Masquer la couverture dans l’article

Selon la référence des variables PaperMod, `cover.hidden: true` masque la couverture dans l’affichage de l’article tout en la conservant dans les métadonnées structurées. C’est utile si l’image sert uniquement aux cartes sociales. Vérifiez le HTML avec un fork ou des modèles personnalisés.

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
  hidden: true
```

## Type de carte et dimensions

Les anciennes affirmations selon lesquelles PaperMod ne prend en charge que `summary_large_image` et que 800×418 serait une taille fixe ne sont pas universelles. Le type dépend de la version du thème et des modèles du site. Pour une image large, 1200×630 (environ 1,90:1) est un repère pratique, pas une garantie des exigences de X.

## Vérifier le HTML et l’aperçu

Compilez en mode production et inspectez le HTML de l’article : `twitter:card`, `twitter:image`, `og:image`, le titre et la description. L’image doit être accessible publiquement en HTTPS, sans connexion, et être servie directement. En 2022, X a supprimé l’aperçu du Card Validator et renvoyé vers le compositeur de publication. Collez-y le lien pour vérifier l’aperçu sans publier. Le cache peut mettre du temps à se mettre à jour.

Vérifié le 24/11/2026 à partir des références PaperMod et du forum développeur X indiqués. Les forks, modèles personnalisés et évolutions de X peuvent modifier le résultat.

## Références

- [PaperMod: Features and Twitter Cards](https://github.com/adityatelange/hugo-PaperMod/wiki/Features)
- [PaperMod: Variables](https://github.com/adityatelange/hugo-PaperMod/wiki/Variables)
- [Hugo: Page bundles](https://gohugo.io/content-management/page-bundles/)
- [X Developer Community: Card Validator preview removal](https://devcommunity.x.com/t/card-validator-preview-removal/175006)
