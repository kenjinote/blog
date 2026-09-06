---




title: "'hugo에서 KaTeX(LaTeX 스타일 수식 표시) 활성화하는 방법'"
slug: "hugoでKaTeX(LaTeX風数式表示)を有効にする方法"
date: 2023-03-31T23:11:26+09:00
tags: ["KaTeX", "LaTeX", "수식", "수학", "hugo"]
draft: false
math: true
image: "img.png"
categories: ["수학・암호・양자"]
---




# KaTeX란?
KaTeX는 LaTeX 스타일의 수식을 HTML로 표시하기 위한 javascript 라이브러리입니다.

구체적으로는 아래와 같은 수식을 표시할 수 있습니다.

$$f(x) = x^2 + x + 41$$

그 외에도 LaTeX 스타일의 수식 표시 라이브러리도 있는 것 같습니다만, KaTeX는 심플하고 빠르다는 정평이 나 있습니다.

# hugo에 도입하는 방법
1. hugo의 폴더 계층에서 `layouts/partials/math.html`을 새로 작성합니다.

내용은 아래와 같이 작성해 주세요.

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
2. 다음으로 기존 파일 `layouts/partials/extend_head.html`에 아래의 코드를 추가합니다.

```
{{ if or .Params.math .Site.Params.math }}
{{ partial "math.html" . }}
{{ end }}
```

3. 이것으로 KaTeX를 사용할 준비가 완료되었습니다.

페이지의 front matter에 `math: true`를 추가함으로써, KaTeX를 활성화할 수 있습니다.

4. 이제 페이지 본문에 수식을 LaTeX 스타일로 작성하기만 하면 됩니다.

```
$$ e^{i \pi} = -1 $$
```

위와 같이 작성하면, 아래와 같이 표시됩니다.

$$ e^{i \pi} = -1 $$

# 참고
- [Math Typesetting | PaperModX](https://reorx.github.io/hugo-PaperModX/docs/math-typesetting/)
- [KaTex Auto-render Extension](https://katex.org/docs/autorender.html)
- [KaTeX 도입 | The Strange Storage](https://www.storange.jp/2017/02/katex.html)
