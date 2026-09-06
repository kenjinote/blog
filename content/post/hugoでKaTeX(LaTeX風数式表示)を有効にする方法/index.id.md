---
title: "Cara Mengaktifkan KaTeX (Tampilan Rumus Gaya LaTeX) di hugo"
slug: "hugoでKaTeX(LaTeX風数式表示)を有効にする方法"
date: 2023-03-31T23:11:26+09:00
tags: ["KaTeX", "LaTeX", "rumus", "matematika", "hugo"]
draft: false
math: true
image: "img.png"
categories: ["Matematika, Kriptografi, Kuantum"]
---
# Apa itu KaTeX?
KaTeX adalah pustaka javascript untuk menampilkan rumus matematika bergaya LaTeX dalam HTML.

Secara khusus, Anda dapat menampilkan rumus seperti berikut ini:

$$f(x) = x^2 + x + 41$$

Tampaknya ada pustaka tampilan rumus bergaya LaTeX lainnya, tetapi KaTeX dikenal karena sederhana dan cepat.

# Cara menambahkan ke hugo
1. Buat file baru `layouts/partials/math.html` dalam hierarki folder hugo.

Isinya harus sebagai berikut:

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
2. Selanjutnya, tambahkan kode berikut ke file yang sudah ada `layouts/partials/extend_head.html`.

```
{{ if or .Params.math .Site.Params.math }}
{{ partial "math.html" . }}
{{ end }}
```

3. Sekarang Anda siap menggunakan KaTeX.

Dengan menambahkan `math: true` ke front matter halaman, Anda dapat mengaktifkan KaTeX.

4. Yang harus Anda lakukan adalah menulis rumus gaya LaTeX di badan artikel.

```
$$ e^{i \pi} = -1 $$
```

Saat ditulis seperti di atas, ini akan ditampilkan sebagai berikut:

$$ e^{i \pi} = -1 $$

# Referensi
- [Math Typesetting | PaperModX](https://reorx.github.io/hugo-PaperModX/docs/math-typesetting/)
- [KaTex Auto-render Extension](https://katex.org/docs/autorender.html)
- [Pengenalan KaTeX | The Strange Storage](https://www.storange.jp/2017/02/katex.html)
