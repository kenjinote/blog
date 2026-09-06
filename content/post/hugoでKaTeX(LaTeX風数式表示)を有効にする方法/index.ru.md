---
title: "Как включить KaTeX (отображение формул в стиле LaTeX) в hugo"
slug: "hugoでKaTeX(LaTeX風数式表示)を有効にする方法"
date: 2023-03-31T23:11:26+09:00
tags: ["KaTeX", "LaTeX", "формулы", "математика", "hugo"]
draft: false
math: true
image: "img.png"
categories: ["Математика, Криптография, Кванты"]
---
# Что такое KaTeX?
KaTeX — это JavaScript-библиотека для отображения математических формул в стиле LaTeX в HTML.

В частности, вы можете отображать формулы, подобные этой:

$$f(x) = x^2 + x + 41$$

Существуют и другие библиотеки для отображения формул в стиле LaTeX, но KaTeX славится своей простотой и скоростью.

# Как внедрить в hugo
1. Создайте новый файл `layouts/partials/math.html` в структуре папок hugo.

Содержимое должно быть следующим:

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
2. Затем добавьте следующий код в существующий файл `layouts/partials/extend_head.html`.

```
{{ if or .Params.math .Site.Params.math }}
{{ partial "math.html" . }}
{{ end }}
```

3. Теперь вы готовы использовать KaTeX.

Добавив `math: true` в front matter вашей страницы, вы сможете активировать KaTeX.

4. Все, что вам нужно сделать, это написать формулы в стиле LaTeX в теле вашей статьи.

```
$$ e^{i \pi} = -1 $$
```

При написании, как показано выше, это будет отображаться следующим образом:

$$ e^{i \pi} = -1 $$

# Ссылки
- [Math Typesetting | PaperModX](https://reorx.github.io/hugo-PaperModX/docs/math-typesetting/)
- [KaTex Auto-render Extension](https://katex.org/docs/autorender.html)
- [Введение в KaTeX | The Strange Storage](https://www.storange.jp/2017/02/katex.html)
