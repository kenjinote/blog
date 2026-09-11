---
title: 'Como alterar as cores e o tema de cores do tema Hugo PaperMod com CSS'
slug: "PaperModの配色変更"
date: 2022-09-07T15:30:21+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["Administração do Blog"]
description: 'Explicamos como personalizar as cores gerais do tema Hugo PaperMod. Apresentamos exemplos específicos de configuração de variáveis ​​para aplicar o esquema de cores de sua preferência, editando o CSS (blank.css) que inclui as definições de estilo, como cor de fundo, cor de texto, blocos de código, etc.'
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
