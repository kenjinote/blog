---
title: 'hugoでKaTeX(LaTeX風数式表示)を有効にする方法'
date: 2023-03-31T23:11:26+09:00
tags: ["KaTeX", "LaTeX", "数式", "数学", "hugo"]
draft: false
math: true
image: "img.png"
---
# KaTeXとは
KaTeXは、LaTeX風の数式をHTMLで表示するためのjavascriptライブラリです。

具体的には下記のような数式を表示することができます。

$$f(x) = x^2 + x + 41$$

他にもLaTeX風な数式表示ライブラリもあるようですが、KaTeXはシンプルで高速と定評があるようです。

# hugoへの導入方法
1. hugoのフォルダ階層で`layouts/partials/math.html`を新規作成します。

中身は下記の通りにしてください。

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
2. 次に既存のファイル`layouts/partials/extend_head.html`に下記のコードを追加します。

```
{{ if or .Params.math .Site.Params.math }}
{{ partial "math.html" . }}
{{ end }}
```

3. これでKaTeXを使う準備が整いました。

ページのfront matterに`math: true`を追加することで、KaTeXを有効にすることができます。

4. あとはページ記事の本文に、数式をLaTeX風に書くだけです。

```
$$ e^{i \pi} = -1 $$
```

上記のように記述すると、下記のように表示されます。

$$ e^{i \pi} = -1 $$

# 参考
- [Math Typesetting | PaperModX](https://reorx.github.io/hugo-PaperModX/docs/math-typesetting/)
- [KaTex Auto-render Extension](https://katex.org/docs/autorender.html)
- [KaTeXの導入 | The Strange Storage](https://www.storange.jp/2017/02/katex.html)