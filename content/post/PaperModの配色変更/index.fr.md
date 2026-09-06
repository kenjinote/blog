---
title: "Modification de la palette de couleurs de PaperMod"
slug: "PaperModの配色変更"
date: 2022-09-07T15:30:21+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.png"
categories: ["Administration du blog"]
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
