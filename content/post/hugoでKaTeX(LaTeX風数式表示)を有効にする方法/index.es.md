---



title: "Cómo habilitar KaTeX (fórmulas matemáticas estilo LaTeX) en hugo"
date: 2023-03-31T23:11:26+09:00
tags: ["KaTeX", "LaTeX", "fórmulas", "matemáticas", "hugo"]
draft: false
math: true
image: "img.png"
categories: ["Matemáticas, Criptografía, Cuántica"]
---



# Qué es KaTeX
KaTeX es una biblioteca de JavaScript para mostrar fórmulas matemáticas estilo LaTeX en HTML.

Específicamente, puedes mostrar fórmulas como la siguiente.

$$f(x) = x^2 + x + 41$$

Aunque parece haber otras bibliotecas para mostrar fórmulas matemáticas estilo LaTeX, KaTeX tiene la reputación de ser simple y rápida.

# Cómo introducirlo en hugo
1. Crea un nuevo archivo `layouts/partials/math.html` en la jerarquía de carpetas de hugo.

El contenido debe ser el siguiente.

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
2. A continuación, añade el siguiente código al archivo existente `layouts/partials/extend_head.html`.

```
{{ if or .Params.math .Site.Params.math }}
{{ partial "math.html" . }}
{{ end }}
```

3. Ahora estás listo para usar KaTeX.

Al añadir `math: true` al front matter de la página, puedes habilitar KaTeX.

4. Todo lo que tienes que hacer es escribir las fórmulas matemáticas al estilo LaTeX en el cuerpo del artículo de la página.

```
$$ e^{i \pi} = -1 $$
```

Si lo escribes como arriba, se mostrará de la siguiente manera.

$$ e^{i \pi} = -1 $$

# Referencias
- [Math Typesetting | PaperModX](https://reorx.github.io/hugo-PaperModX/docs/math-typesetting/)
- [KaTex Auto-render Extension](https://katex.org/docs/autorender.html)
- [Introducción a KaTeX | The Strange Storage](https://www.storange.jp/2017/02/katex.html)
