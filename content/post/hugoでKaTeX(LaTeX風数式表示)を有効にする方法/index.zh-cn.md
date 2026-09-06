---
title: '在hugo中启用KaTeX（类似LaTeX的数学公式显示）的方法'
slug: "hugoでKaTeX(LaTeX風数式表示)を有効にする方法"
date: 2023-03-31T23:11:26+09:00
tags: ["KaTeX", "LaTeX", "数学公式", "数学", "hugo"]
draft: false
math: true
image: "img.png"
categories: ["数学・密码学・量子"]
---
# 什么是KaTeX
KaTeX是一个在HTML中显示类似LaTeX的数学公式的JavaScript库。

具体来说，可以显示如下所示的数学公式。

$$f(x) = x^2 + x + 41$$

似乎还有其他类似LaTeX的数学公式显示库，但KaTeX以简单和高速而闻名。

# 在hugo中的导入方法
1. 在hugo的文件夹层级中新建`layouts/partials/math.html`。

内容请参考如下所示。

```html
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
2. 接下来，在现有的文件`layouts/partials/extend_head.html`中添加以下代码。

```html
{{ if or .Params.math .Site.Params.math }}
{{ partial "math.html" . }}
{{ end }}
```

3. 这样使用KaTeX的准备工作就完成了。

通过在页面的front matter中添加`math: true`，可以启用KaTeX。

4. 之后只需在页面文章的正文中，以类似LaTeX的方式编写数学公式即可。

```text
$$ e^{i \pi} = -1 $$
```

如上编写后，将显示如下。

$$ e^{i \pi} = -1 $$

# 参考
- [Math Typesetting | PaperModX](https://reorx.github.io/hugo-PaperModX/docs/math-typesetting/)
- [KaTex Auto-render Extension](https://katex.org/docs/autorender.html)
- [KaTeXの導入 | The Strange Storage](https://www.storange.jp/2017/02/katex.html)
