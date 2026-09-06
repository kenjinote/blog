---
title: "كيفية تفعيل KaTeX (عرض المعادلات بأسلوب LaTeX) في hugo"
slug: "hugoでKaTeX(LaTeX風数式表示)を有効にする方法"
date: 2023-03-31T23:11:26+09:00
tags: ["KaTeX", "LaTeX", "معادلات", "رياضيات", "hugo"]
draft: false
math: true
image: "img.png"
categories: ["رياضيات، تشفير، كم"]
---
# ما هو KaTeX؟
KaTeX هي مكتبة javascript لعرض المعادلات الرياضية بأسلوب LaTeX في HTML.

على وجه التحديد، يمكنك عرض معادلات مثل التالية:

$$f(x) = x^2 + x + 41$$

يبدو أن هناك مكتبات أخرى لعرض المعادلات بأسلوب LaTeX، لكن KaTeX معروفة بكونها بسيطة وسريعة.

# كيفية إضافته إلى hugo
1. قم بإنشاء ملف جديد `layouts/partials/math.html` في بنية مجلدات hugo.

يجب أن يكون المحتوى كالتالي:

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
2. بعد ذلك، أضف الكود التالي إلى الملف الحالي `layouts/partials/extend_head.html`.

```
{{ if or .Params.math .Site.Params.math }}
{{ partial "math.html" . }}
{{ end }}
```

3. الآن أصبحت جاهزًا لاستخدام KaTeX.

عن طريق إضافة `math: true` إلى front matter للصفحة، يمكنك تفعيل KaTeX.

4. كل ما عليك فعله بعد ذلك هو كتابة المعادلات بأسلوب LaTeX في نص المقالة.

```
$$ e^{i \pi} = -1 $$
```

عندما تكتب كما هو موضح أعلاه، سيتم عرضها كالتالي:

$$ e^{i \pi} = -1 $$

# مراجع
- [Math Typesetting | PaperModX](https://reorx.github.io/hugo-PaperModX/docs/math-typesetting/)
- [KaTex Auto-render Extension](https://katex.org/docs/autorender.html)
- [إدخال KaTeX | The Strange Storage](https://www.storange.jp/2017/02/katex.html)
