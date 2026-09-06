---
title: "ह्यूगो (hugo) में KaTeX (LaTeX-शैली गणित सूत्र प्रदर्शन) को कैसे सक्षम करें"
slug: "how-to-enable-katex-in-hugo"
date: 2023-03-31T23:11:26+09:00
tags: ["KaTeX", "LaTeX", "सूत्र", "गणित", "hugo"]
draft: false
math: true
image: "img.png"
categories: ["गणित/क्रिप्टोग्राफी/क्वांटम"]
---
# KaTeX क्या है
KaTeX HTML में LaTeX-शैली के गणित सूत्रों को प्रदर्शित करने के लिए एक जावास्क्रिप्ट (javascript) लाइब्रेरी है।

विशेष रूप से, आप नीचे दिए गए जैसे गणित सूत्र प्रदर्शित कर सकते हैं।

$$f(x) = x^2 + x + 41$$

LaTeX-शैली के अन्य गणित सूत्र प्रदर्शन पुस्तकालय भी प्रतीत होते हैं, लेकिन KaTeX अपनी सादगी और गति के लिए जाना जाता है।

# hugo में कैसे शामिल करें
1. hugo के फ़ोल्डर पदानुक्रम में एक नया `layouts/partials/math.html` बनाएँ।

सामग्री इस प्रकार होनी चाहिए।

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

2. इसके बाद, मौजूदा फ़ाइल `layouts/partials/extend_head.html` में निम्नलिखित कोड जोड़ें।

```
{{ if or .Params.math .Site.Params.math }}
{{ partial "math.html" . }}
{{ end }}
```

3. अब आप KaTeX का उपयोग करने के लिए तैयार हैं।

आप पेज के front matter में `math: true` जोड़कर KaTeX को सक्षम कर सकते हैं।

4. इसके बाद आपको बस पेज लेख के मुख्य भाग में LaTeX-शैली में सूत्र लिखना है।

```
$$ e^{i \pi} = -1 $$
```

जैसा कि ऊपर लिखा गया है, यह नीचे दिए गए अनुसार प्रदर्शित होगा।

$$ e^{i \pi} = -1 $$

# संदर्भ
- [Math Typesetting | PaperModX](https://reorx.github.io/hugo-PaperModX/docs/math-typesetting/)
- [KaTex Auto-render Extension](https://katex.org/docs/autorender.html)
- [KaTeX का परिचय | The Strange Storage](https://www.storange.jp/2017/02/katex.html)
