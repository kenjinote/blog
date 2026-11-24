---
title: "美しい数式5選：定理と式の正確な意味"
slug: "好きな数式"
date: 2022-10-05T13:24:50+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["数学"]
draft: false
math: true
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "ウィルソンの定理、オイラーの公式、フェルマーの最終定理、バーゼル問題、オイラーの素数生成多項式を、条件と範囲を明記して紹介します。"
---
ここでは5つの有名な数学的結果を、成立条件も含めて紹介します。記号 $p,n,k$ は整数、$i^2=-1$、$pi$ は円周率とします。

## ウィルソンの定理

素数 $p$ について、$(p-1)!\equiv -1 \pmod p$ が成り立ちます。より正確には、整数 $m>1$ が素数であることと $(m-1)!\equiv -1 \pmod m$ は同値です。ここで $r!$ は $1$ から $r$ までの整数の積です。

## オイラーの公式とオイラーの恒等式

実数 $x$ をラジアンで測るとき、オイラーの公式は $e^{ix}=\cos x+i\sin x$ です。$x=\pi$ を代入すると、特別な場合としてオイラーの恒等式 $e^{i\pi}+1=0$ が得られます。

## [フェルマーの最終定理](https://kenji.blog/p/fermats-last-theorem/)

整数 $n\ge 3$ に対して、$x^n+y^n=z^n$ を満たす正の整数 $x,y,z$ は存在しません。条件に「正の整数」と「指数が3以上」を含めるのが大切です。

## バーゼル問題

平方数の逆数をすべて足す無限級数は、$\displaystyle \sum_{k=1}^{\infty}\frac{1}{k^2}=\frac{\pi^2}{6}$ となります。

## オイラーの素数生成多項式

多項式 $n^2+n+41$ は、整数 $n=0,1,\ldots,39$ では素数を与えます。ただし、すべての整数で素数になるわけではありません。$n=40$ では $1681=41^2$ となり、合成数です。

## 参考資料

- [Wilson’s Theorem — Wolfram MathWorld](https://mathworld.wolfram.com/WilsonsTheorem.html)
- [About Euler’s Identity — Euler-Franeker Memorial University](https://euler.euclid.int/about-eulers-identity/)
- [Fermat’s Last Theorem — University of Cambridge](https://www.maths.cam.ac.uk/features/node/153)
- [The Basel Problem — University of Kentucky](https://clp.math.uky.edu/clp2/chap_seq_ser-5.html)
- [Euler’s prime-producing polynomial revisited — Cambridge University Press](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1F76183BF30CECE688E31E8F10F37AC8/S0025557224000111a.pdf/eulers_primeproducing_polynomial_revisited.pdf)
