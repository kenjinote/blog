---
title: "Wie man KaTeX (LaTeX-ähnliche mathematische Formelanzeige) in hugo aktiviert"
slug: "how-to-enable-katex-in-hugo"
date: 2023-03-31T23:11:26+09:00
tags: ["KaTeX", "LaTeX", "Formeln", "Mathematik", "hugo"]
draft: false
math: true
image: "img.png"
categories: ["Mathematik/Kryptographie/Quanten"]
---
# Was ist KaTeX
KaTeX ist eine JavaScript-Bibliothek zur Anzeige von mathematischen Formeln im LaTeX-Stil in HTML.

Konkret können Sie Formeln wie die folgende anzeigen.

$$f(x) = x^2 + x + 41$$

Es scheint auch andere LaTeX-ähnliche Formelanzeige-Bibliotheken zu geben, aber KaTeX ist dafür bekannt, einfach und schnell zu sein.

# Wie man es in hugo integriert
1. Erstellen Sie ein neues `layouts/partials/math.html` in der Ordnerhierarchie von hugo.

Der Inhalt sollte wie folgt sein.

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

2. Als Nächstes fügen Sie den folgenden Code zur vorhandenen Datei `layouts/partials/extend_head.html` hinzu.

```
{{ if or .Params.math .Site.Params.math }}
{{ partial "math.html" . }}
{{ end }}
```

3. Jetzt sind Sie bereit, KaTeX zu verwenden.

Sie können KaTeX aktivieren, indem Sie `math: true` in das Front Matter der Seite einfügen.

4. Alles, was noch zu tun ist, ist die Formel im LaTeX-Stil in den Textkörper des Seitenartikels zu schreiben.

```
$$ e^{i \pi} = -1 $$
```

Wenn Sie es wie oben schreiben, wird es wie unten angezeigt.

$$ e^{i \pi} = -1 $$

# Referenz
- [Math Typesetting | PaperModX](https://reorx.github.io/hugo-PaperModX/docs/math-typesetting/)
- [KaTex Auto-render Extension](https://katex.org/docs/autorender.html)
- [Einführung in KaTeX | The Strange Storage](https://www.storange.jp/2017/02/katex.html)
