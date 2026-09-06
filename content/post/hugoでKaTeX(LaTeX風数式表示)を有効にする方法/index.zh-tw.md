---
title: "如何在 hugo 中啟用 KaTeX（LaTeX 風格的數學公式顯示）"
slug: "how-to-enable-katex-in-hugo"
date: 2023-03-31T23:11:26+09:00
tags: ["KaTeX", "LaTeX", "公式", "數學", "hugo"]
draft: false
math: true
image: "img.png"
categories: ["數學・密碼學・量子"]
---
# 什麼是 KaTeX
KaTeX 是一個用於在 HTML 中顯示 LaTeX 風格數學公式的 javascript 函式庫。

具體來說，您可以顯示如下的數學公式。

$$f(x) = x^2 + x + 41$$

似乎還有其他 LaTeX 風格的數學公式顯示函式庫，但 KaTeX 以簡單且快速而聞名。

# 如何導入到 hugo
1. 在 hugo 的資料夾層次結構中建立一個新的 `layouts/partials/math.html`。

內容應如下所示。

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

2. 接下來，將以下程式碼新增至現有檔案 `layouts/partials/extend_head.html` 中。

```
{{ if or .Params.math .Site.Params.math }}
{{ partial "math.html" . }}
{{ end }}
```

3. 現在您已經準備好使用 KaTeX 了。

您可以透過在頁面的 front matter 中加入 `math: true` 來啟用 KaTeX。

4. 剩下的就是在頁面文章的正文中以 LaTeX 風格編寫公式即可。

```
$$ e^{i \pi} = -1 $$
```

如上所述編寫，將會如下顯示。

$$ e^{i \pi} = -1 $$

# 參考資料
- [Math Typesetting | PaperModX](https://reorx.github.io/hugo-PaperModX/docs/math-typesetting/)
- [KaTex Auto-render Extension](https://katex.org/docs/autorender.html)
- [導入 KaTeX | The Strange Storage](https://www.storange.jp/2017/02/katex.html)
