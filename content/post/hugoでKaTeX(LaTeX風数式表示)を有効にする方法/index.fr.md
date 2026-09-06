---
title: "Comment activer KaTeX (affichage de formules mathématiques de style LaTeX) dans hugo"
slug: "how-to-enable-katex-in-hugo"
date: 2023-03-31T23:11:26+09:00
tags: ["KaTeX", "LaTeX", "formules", "mathématiques", "hugo"]
draft: false
math: true
image: "img.png"
categories: ["Mathématiques/Cryptographie/Quantique"]
---
# Qu'est-ce que KaTeX
KaTeX est une bibliothèque javascript permettant d'afficher des formules mathématiques de style LaTeX en HTML.

Plus précisément, vous pouvez afficher des formules comme ci-dessous.

$$f(x) = x^2 + x + 41$$

Il semble y avoir d'autres bibliothèques d'affichage de formules de style LaTeX, mais KaTeX est réputé pour être simple et rapide.

# Comment l'intégrer à hugo
1. Créez un nouveau `layouts/partials/math.html` dans la hiérarchie des dossiers de hugo.

Le contenu doit être le suivant.

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

2. Ensuite, ajoutez le code ci-dessous au fichier existant `layouts/partials/extend_head.html`.

```
{{ if or .Params.math .Site.Params.math }}
{{ partial "math.html" . }}
{{ end }}
```

3. Vous êtes maintenant prêt à utiliser KaTeX.

Vous pouvez activer KaTeX en ajoutant `math: true` au front matter de la page.

4. Il ne vous reste plus qu'à écrire la formule dans le style LaTeX dans le corps de l'article de la page.

```
$$ e^{i \pi} = -1 $$
```

En l'écrivant comme ci-dessus, il s'affichera comme ci-dessous.

$$ e^{i \pi} = -1 $$

# Référence
- [Math Typesetting | PaperModX](https://reorx.github.io/hugo-PaperModX/docs/math-typesetting/)
- [KaTex Auto-render Extension](https://katex.org/docs/autorender.html)
- [Introduction à KaTeX | The Strange Storage](https://www.storange.jp/2017/02/katex.html)
