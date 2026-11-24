---
title: "Personalizar as cores do Hugo PaperMod com variáveis CSS"
slug: "PaperModの配色変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Substitua as variáveis de cor do PaperMod para os temas claro e escuro com CSS estendido e verifique o contraste do texto."
date: "2022-09-07T15:30:21+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

As cores do PaperMod podem ser personalizadas com propriedades customizadas do CSS (variáveis). Coloque as substituições em `assets/css/extended/` do site em vez de editar arquivos do tema, para facilitar a manutenção nas atualizações. O exemplo define uma paleta clara quente e uma escura; ajuste os valores ao seu site.

## Modo escuro e variáveis atuais

O PaperMod atual alterna para o modo escuro definindo `data-theme="dark"` no elemento `html`. Exemplos antigos que selecionam apenas `.dark` podem não corresponder a esse seletor. Além disso, `--hljs-bg` não é mais a variável atual do fundo dos blocos de código; o nome usado agora é `--code-block-bg`.

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

## Contraste do texto

Neste exemplo, as cores de texto normal `--primary` e `--content` contrastam bastante com o fundo. O contraste de `--primary` com `--theme` é de cerca de 10,4:1 no modo claro e 13,4:1 no escuro. WCAG 2.2 AA exige 4,5:1 para texto normal; confira separadamente as cores de sintaxe, links, bordas e outros estados.

## Adicionar e conferir CSS estendido

Salve a folha de estilos como `assets/css/extended/theme-colors.css` na raiz do site. A FAQ do PaperMod informa que CSS em `assets/css/extended/` é agrupado com os estilos do tema. Execute Hugo e confira o seletor claro/escuro, cartões, texto, código em linha, blocos de código e links.

## Escopo

Esta paleta é um exemplo e não garante conformidade de acessibilidade para todo texto, imagem ou componente interativo. As cores de realce de sintaxe são definidas separadamente de `--code-block-bg`; revise a legibilidade do código após mudar o fundo do bloco.

## Referências

- [PaperMod FAQ: custom CSS and theme assets](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current theme color variables](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/core/theme-vars.css)
- [PaperMod discussion: changing background and text colors](https://github.com/adityatelange/hugo-PaperMod/discussions/645)
- [W3C: WCAG 2.2 contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum)
