---
title: 'How to enable KaTeX (LaTeX-style math formulas) in Hugo'
slug: "hugoでKaTeX(LaTeX風数式表示)を有効にする方法"
date: 2023-03-31T23:11:26+09:00
tags: ["KaTeX", "LaTeX", "math", "mathematics", "hugo"]
draft: false
math: true
image: "img.png"
categories: ["Mathematics, Cryptography, Quantum"]
---
# What is KaTeX
KaTeX is a JavaScript library for displaying LaTeX-style mathematical formulas in HTML.

Specifically, it can display formulas like the following:

$$f(x) = x^2 + x + 41$$

There seem to be other LaTeX-style math rendering libraries, but KaTeX is known for being simple and fast.

# How to introduce it to Hugo
1. Create a new `layouts/partials/math.html` in your Hugo folder hierarchy.

Make the contents as follows:

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
2. Next, add the following code to the existing file `layouts/partials/extend_head.html`.

```
{{ if or .Params.math .Site.Params.math }}
{{ partial "math.html" . }}
{{ end }}
```

3. Now you are ready to use KaTeX.

You can enable KaTeX by adding `math: true` to the front matter of a page.

4. All you have to do is write formulas in LaTeX style in the body of the page article.

```
$$ e^{i \pi} = -1 $$
```

If you describe it as above, it will be displayed as follows:

$$ e^{i \pi} = -1 $$

# References
- [Math Typesetting | PaperModX](https://reorx.github.io/hugo-PaperModX/docs/math-typesetting/)
- [KaTex Auto-render Extension](https://katex.org/docs/autorender.html)
- [Introduction to KaTeX | The Strange Storage](https://www.storange.jp/2017/02/katex.html)
