---
title: "Personnaliser les couleurs de Hugo PaperMod avec des variables CSS"
slug: "PaperModの配色変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Remplacez les variables de couleur de PaperMod pour les thèmes clair et sombre avec du CSS étendu, puis vérifiez le contraste du texte."
date: "2022-09-07T15:30:21+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Les couleurs de PaperMod se personnalisent avec des propriétés personnalisées CSS (variables). Placez vos remplacements dans `assets/css/extended/` du site plutôt que de modifier les fichiers du thème ; ils seront ainsi plus faciles à conserver lors des mises à jour. L’exemple propose une palette claire chaude et une palette sombre, à adapter à votre site.

## Mode sombre et variables actuelles

La version actuelle de PaperMod active le mode sombre en définissant `data-theme="dark"` sur l’élément `html`. Les anciens exemples qui ciblent uniquement `.dark` peuvent ne pas correspondre à ce sélecteur. De plus, `--hljs-bg` n’est plus la variable actuelle du fond des blocs de code ; son nom actuel est `--code-block-bg`.

```css
/* Save as assets/css/extended/theme-colors.css */
:root {
    color-scheme: light;
    --theme: #fbf7ef;
    --entry: #fffdfa;
    --primary: #433a32;
    --secondary: #665b50;
    --tertiary: #8b7f72;
    --content: #453d35;
    --code-block-bg: #34231b;
    --code-bg: #efe7da;
    --border: #ddd3c5;
}

:root[data-theme="dark"] {
    color-scheme: dark;
    --theme: #1d1e20;
    --entry: #22252a;
    --primary: #e8e6e1;
    --secondary: #b5b2ac;
    --tertiary: #55575c;
    --content: #d2d0ca;
    --code-block-bg: #17181a;
    --code-bg: #37383e;
    --border: #48484c;
}
```

## Contraste du texte

Dans cet exemple, les couleurs du texte courant `--primary` et `--content` contrastent fortement avec leur arrière-plan. Le contraste de `--primary` sur `--theme` est d’environ 10,4:1 en mode clair et 13,4:1 en mode sombre. WCAG 2.2 AA demande 4,5:1 pour le texte courant ; vérifiez séparément les couleurs de syntaxe, les liens, les bordures et les autres états.

## Ajouter et vérifier le CSS étendu

Enregistrez la feuille de style sous `assets/css/extended/theme-colors.css` à la racine du site. La FAQ PaperMod précise que les CSS de `assets/css/extended/` sont regroupés avec les styles du thème. Lancez Hugo et vérifiez le basculement clair/sombre, les cartes, le texte, le code en ligne, les blocs de code et les liens.

## Périmètre

Cette palette est illustrative et ne garantit pas l’accessibilité de chaque texte, image ou composant interactif. Les couleurs de coloration syntaxique sont définies séparément de `--code-block-bg` ; vérifiez à nouveau la lisibilité du code après avoir changé le fond du bloc.

## Références

- [PaperMod FAQ: custom CSS and theme assets](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current theme color variables](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/core/theme-vars.css)
- [PaperMod discussion: changing background and text colors](https://github.com/adityatelange/hugo-PaperMod/discussions/645)
- [W3C: WCAG 2.2 contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum)
