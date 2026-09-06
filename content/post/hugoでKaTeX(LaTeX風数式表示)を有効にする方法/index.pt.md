---
title: "Como habilitar KaTeX (exibição de fórmulas no estilo LaTeX) no hugo"
slug: "como-habilitar-katex-no-hugo"
date: 2023-03-31T23:11:26+09:00
tags: ["KaTeX", "LaTeX", "fórmulas", "matemática", "hugo"]
draft: false
math: true
image: "img.png"
categories: ["Matemática/Criptografia/Quântica"]
---
# O que é KaTeX
KaTeX é uma biblioteca javascript para exibir fórmulas no estilo LaTeX em HTML.

Especificamente, você pode exibir fórmulas como a abaixo.

$$f(x) = x^2 + x + 41$$

Parece haver outras bibliotecas de exibição de fórmulas no estilo LaTeX, mas o KaTeX tem a reputação de ser simples e rápido.

# Como introduzir no hugo
1. Crie um novo `layouts/partials/math.html` na hierarquia de pastas do hugo.

O conteúdo deve ser o seguinte.

```
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/katex.min.css" integrity="sha384-vKruj+a13U8yHIkAyGgK1J3ArTLzrFGBbBc0tDp4ad/EyewESeXE/Iv67Aj8gKZ0" crossorigin="anonymous">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/katex.min.js" integrity="sha384-PwRUT/YqbnEjkZO0zZxNqcxACrXe+j766U2amXcgMg5457rve2Y7I6ZJSm2A0mS4" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script>
<script>
document.addEventListener("DOMContentLoaded", function() {
  renderMathInElement(
    document.body,
    {
      delimiters: [
        {left: "$$", right: "$$", display: true},
        {left: "\\[", right: "\\]", display: true},
        {left: "$", right: "$", display: false},
        {left: "\\(", right: "\\)", display: false}
      ]
    });
  });
</script>
```

2. Em seguida, adicione o código abaixo ao arquivo existente `layouts/partials/extend_head.html`.

```
{{ if or .Params.math .Site.Params.math }}
{{ partial "math.html" . }}
{{ end }}
```

3. Agora você está pronto para usar o KaTeX.

Você pode habilitar o KaTeX adicionando `math: true` ao front matter da página.

4. Tudo o que resta é escrever a fórmula no estilo LaTeX no corpo do artigo da página.

```
$$ e^{i \pi} = -1 $$
```

Ao escrever como acima, será exibido como abaixo.

$$ e^{i \pi} = -1 $$

# Referência
- [Math Typesetting | PaperModX](https://reorx.github.io/hugo-PaperModX/docs/math-typesetting/)
- [KaTex Auto-render Extension](https://katex.org/docs/autorender.html)
- [Introdução ao KaTeX | The Strange Storage](https://www.storange.jp/2017/02/katex.html)
