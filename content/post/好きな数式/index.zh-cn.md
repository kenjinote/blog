---
title: "五个优美的数学结果：准确表述与范围"
slug: "好きな数学公式"
date: 2022-10-05T13:24:50+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["数学"]
draft: false
math: true
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "准确介绍威尔逊定理、欧拉公式与恒等式、费马大定理、巴塞尔问题，以及欧拉多项式产生素数的有限范围。"
---
下面介绍五个著名的数学结果，并明确写出成立条件。$p,n,k$ 表示整数，$i^2=-1$，$\\pi$ 表示圆周率。

## 威尔逊定理

若 $p$ 是素数，则 $(p-1)!\equiv -1 \pmod p$。更准确地说，对于整数 $m>1$，$m$ 是素数当且仅当 $(m-1)!\equiv -1 \pmod m$。$r!$ 表示从 1 到 $r$ 的整数乘积。

## 欧拉公式与欧拉恒等式

对于以弧度计量的实数 $x$，欧拉公式为 $e^{ix}=\cos x+i\sin x$。令 $x=\pi$，便得到特殊情形——欧拉恒等式：$e^{i\pi}+1=0$。

## [费马大定理](https://kenji.blog/zh-cn/p/fermats-last-theorem/)

对于任意整数 $n\ge 3$，不存在满足 $x^n+y^n=z^n$ 的正整数 $x,y,z$。正整数条件以及指数至少为 3 都不可省略。

## 巴塞尔问题

所有正整数平方的倒数构成的无穷级数满足：$\displaystyle \sum_{k=1}^{\infty}\frac{1}{k^2}=\frac{\pi^2}{6}$。

## 欧拉素数生成多项式

当整数 $n=0,1,\ldots,39$ 时，多项式 $n^2+n+41$ 的值都是素数。但它并非对所有整数都产生素数：$n=40$ 时，结果为 $1681=41^2$，是合数。

## 参考资料

- [Wilson’s Theorem — Wolfram MathWorld](https://mathworld.wolfram.com/WilsonsTheorem.html)
- [About Euler’s Identity — Euler-Franeker Memorial University](https://euler.euclid.int/about-eulers-identity/)
- [Fermat’s Last Theorem — University of Cambridge](https://www.maths.cam.ac.uk/features/node/153)
- [The Basel Problem — University of Kentucky](https://clp.math.uky.edu/clp2/chap_seq_ser-5.html)
- [Euler’s prime-producing polynomial revisited — Cambridge University Press](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1F76183BF30CECE688E31E8F10F37AC8/S0025557224000111a.pdf/eulers_primeproducing_polynomial_revisited.pdf)
