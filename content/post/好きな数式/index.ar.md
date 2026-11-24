---
title: "خمسة نتائج رياضية جميلة بصياغة دقيقة"
slug: "好きなصيغة رياضية"
date: 2022-10-05T13:24:50+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["الرياضيات"]
draft: false
math: true
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "عرض دقيق لمبرهنة ويلسون وصيغة أويلر ومتطابقته، ومبرهنة فيرما الأخيرة، ومسألة بازل، والنطاق المحدود لتوليد الأعداد الأولية بكثيرة حدود أويلر."
---
فيما يلي خمس نتائج رياضية مشهورة مع بيان شروطها بدقة. تمثل $p,n,k$ أعدادًا صحيحة، و$i^2=-1$، و$\\pi$ ثابت الدائرة.

## مبرهنة ويلسون

إذا كان $p$ عددًا أوليًا، فإن $(p-1)!\equiv -1 \pmod p$. وبصياغة أدق، يكون العدد الصحيح $m>1$ أوليًا إذا وفقط إذا تحقق $(m-1)!\equiv -1 \pmod m$. والرمز $r!$ هو حاصل ضرب الأعداد الصحيحة من 1 إلى $r$.

## صيغة أويلر ومتطابقة أويلر

لعدد حقيقي $x$ مقاس بالراديان، صيغة أويلر هي $e^{ix}=\cos x+i\sin x$. وعند وضع $x=\pi$ نحصل على الحالة الخاصة المعروفة بمتطابقة أويلر: $e^{i\pi}+1=0$.

## [مبرهنة فيرما الأخيرة](https://kenji.blog/ar/p/fermats-last-theorem/)

لكل عدد صحيح $n\ge 3$، لا توجد أعداد صحيحة موجبة $x,y,z$ تحقق $x^n+y^n=z^n$. وشرطا كونها موجبة وأن يكون الأس 3 أو أكبر أساسيان.

## مسألة بازل

مجموع مقلوبات مربعات جميع الأعداد الصحيحة الموجبة هو المتسلسلة اللانهائية $\displaystyle \sum_{k=1}^{\infty}\frac{1}{k^2}=\frac{\pi^2}{6}$.

## كثيرة حدود أويلر المولدة للأعداد الأولية

تعطي كثيرة الحدود $n^2+n+41$ عددًا أوليًا للأعداد الصحيحة $n=0,1,\ldots,39$. لكنها لا تعطي أعدادًا أولية لكل عدد صحيح: عند $n=40$ تكون القيمة $1681=41^2$، وهو عدد مركب.

## مراجع

- [Wilson’s Theorem — Wolfram MathWorld](https://mathworld.wolfram.com/WilsonsTheorem.html)
- [About Euler’s Identity — Euler-Franeker Memorial University](https://euler.euclid.int/about-eulers-identity/)
- [Fermat’s Last Theorem — University of Cambridge](https://www.maths.cam.ac.uk/features/node/153)
- [The Basel Problem — University of Kentucky](https://clp.math.uky.edu/clp2/chap_seq_ser-5.html)
- [Euler’s prime-producing polynomial revisited — Cambridge University Press](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1F76183BF30CECE688E31E8F10F37AC8/S0025557224000111a.pdf/eulers_primeproducing_polynomial_revisited.pdf)
