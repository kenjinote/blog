---



title: "Cambio de paleta de colores de PaperMod"
date: 2022-09-07T15:30:21+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.png"
categories: ["Administración del blog"]
---



He cambiado la paleta de colores del tema PaperMod. Me referí al siguiente enlace para saber cómo hacerlo:

https://github.com/adityatelange/hugo-PaperMod/discussions/645

La ruta del CSS es la siguiente:

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

Por ahora, no hay cambios en el modo oscuro.
