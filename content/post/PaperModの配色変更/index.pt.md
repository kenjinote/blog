---
title: "Alterando o esquema de cores do PaperMod"
slug: "PaperModの配色変更"
date: 2022-09-07T15:30:21+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.png"
categories: ["Administração do Blog"]
---
Alterei o esquema de cores do tema PaperMod. Consultei o seguinte link para o método de alteração.

https://github.com/adityatelange/hugo-PaperMod/discussions/645

O caminho do CSS é o seguinte.

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

Nenhuma alteração para o modo escuro por enquanto.
