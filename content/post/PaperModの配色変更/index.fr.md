---
title: 'Comment modifier le schéma de couleurs et le thème de couleur du thème Hugo PaperMod avec CSS'
slug: "PaperModの配色変更"
date: 2022-09-07T15:30:21+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["Administration du blog"]
description: 'Explique comment personnaliser la palette de couleurs globale dans le thème PaperMod de Hugo. Présente des exemples spécifiques de configuration de variables pour éditer le CSS (blank.css) qui inclut des définitions de style pour les couleurs d''arrière-plan, les couleurs de texte et les blocs de code, afin d''appliquer un schéma de couleurs personnalisé.'
---
J'ai modifié la palette de couleurs du thème PaperMod. Je me suis référé au lien suivant pour la méthode de modification.

https://github.com/adityatelange/hugo-PaperMod/discussions/645

Le chemin du CSS est le suivant.

`themes/PaperMod/assets/css/extended/blank.css`

```
:root {
    --entry: #fbf7ef;
    --primary: rgba(113, 103, 91, 1.00);
    --secondary: rgba(113, 103, 91, 0.95);
    --tertiary: rgba(113, 103, 91, 0.50);
    --content: rgba(113, 103, 91, 0.85);
    --hljs-bg: #34231B;
    --code-bg: #ebe4d7;
    --border: #fdfaf5;
    --theme: #fbf7ef;
}
.dark {
}
```

Aucun changement pour le mode sombre pour le moment.
