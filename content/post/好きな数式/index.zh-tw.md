---
title: "五個優美的數學結果：精確表述與適用範圍"
slug: "好きな數式"
date: 2022-10-05T13:24:50+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["數學"]
draft: false
math: true
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "精確介紹威爾遜定理、歐拉公式與恆等式、費馬最後定理、巴塞爾問題，以及歐拉多項式產生質數的有限範圍。"
---
以下介紹五個著名的數學結果，並明確列出成立條件。$p,n,k$ 表示整數，$i^2=-1$，$\\pi$ 表示圓周率。

## 威爾遜定理

若 $p$ 是質數，則 $(p-1)!\equiv -1 \pmod p$。更精確地說，對整數 $m>1$，$m$ 是質數若且唯若 $(m-1)!\equiv -1 \pmod m$。$r!$ 表示從 1 到 $r$ 的整數乘積。

## 歐拉公式與歐拉恆等式

對以弧度計量的實數 $x$，歐拉公式為 $e^{ix}=\cos x+i\sin x$。令 $x=\pi$，即可得到特殊情形——歐拉恆等式：$e^{i\pi}+1=0$。

## [費馬最後定理](https://kenji.blog/zh-tw/p/fermats-last-theorem/)

對任意整數 $n\ge 3$，不存在滿足 $x^n+y^n=z^n$ 的正整數 $x,y,z$。正整數條件以及指數至少為 3 都很重要。

## 巴塞爾問題

所有正整數平方的倒數所成的無窮級數為 $\displaystyle \sum_{k=1}^{\infty}\frac{1}{k^2}=\frac{\pi^2}{6}$。

## 歐拉素數生成多項式

整數 $n=0,1,\ldots,39$ 時，多項式 $n^2+n+41$ 的值都是質數。但它並非對所有整數都產生質數：$n=40$ 時，結果為 $1681=41^2$，是合數。

## 參考資料

- [Wilson’s Theorem — Wolfram MathWorld](https://mathworld.wolfram.com/WilsonsTheorem.html)
- [About Euler’s Identity — Euler-Franeker Memorial University](https://euler.euclid.int/about-eulers-identity/)
- [Fermat’s Last Theorem — University of Cambridge](https://www.maths.cam.ac.uk/features/node/153)
- [The Basel Problem — University of Kentucky](https://clp.math.uky.edu/clp2/chap_seq_ser-5.html)
- [Euler’s prime-producing polynomial revisited — Cambridge University Press](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1F76183BF30CECE688E31E8F10F37AC8/S0025557224000111a.pdf/eulers_primeproducing_polynomial_revisited.pdf)
