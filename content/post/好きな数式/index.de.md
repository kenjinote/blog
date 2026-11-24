---
title: "Fünf schöne mathematische Ergebnisse, präzise formuliert"
slug: "好きなFormel"
date: 2022-10-05T13:24:50+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Mathematik"]
draft: false
math: true
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "Präzise Einführung in den Satz von Wilson, Eulers Formel und Identität, Fermats letzten Satz, das Basler Problem und den begrenzten Primzahlbereich von Eulers Polynom."
---
Hier stehen fünf bekannte mathematische Ergebnisse mit ihren genauen Voraussetzungen. $p,n,k$ sind ganze Zahlen, $i^2=-1$ und $\\pi$ ist die Kreiszahl.

## Satz von Wilson

Für eine Primzahl $p$ gilt $(p-1)!\equiv -1 \pmod p$. Genauer: Eine ganze Zahl $m>1$ ist genau dann prim, wenn $(m-1)!\equiv -1 \pmod m$. Dabei ist $r!$ das Produkt der ganzen Zahlen von 1 bis $r$.

## Eulers Formel und Identität

Für eine reelle, im Bogenmaß gemessene Zahl $x$ lautet Eulers Formel $e^{ix}=\cos x+i\sin x$. Mit $x=\pi$ erhält man den Spezialfall, der Eulers Identität heißt: $e^{i\pi}+1=0$.

## [Großer Satz von Fermat](https://kenji.blog/de/p/fermat/)

Für jede ganze Zahl $n\ge 3$ gibt es keine positiven ganzen Zahlen $x,y,z$ mit $x^n+y^n=z^n$. Die Bedingungen „positiv“ und „Exponent mindestens 3“ sind wesentlich.

## Basler Problem

Die unendliche Summe der Kehrwerte aller positiven ganzzahligen Quadrate ist $\displaystyle \sum_{k=1}^{\infty}\frac{1}{k^2}=\frac{\pi^2}{6}$.

## Eulers primzahlerzeugendes Polynom

Das Polynom $n^2+n+41$ liefert für ganze Zahlen $n=0,1,\ldots,39$ eine Primzahl. Das gilt nicht für alle ganzen Zahlen: Für $n=40$ ergibt sich $1681=41^2$, also eine zusammengesetzte Zahl.

## Quellen

- [Wilson’s Theorem — Wolfram MathWorld](https://mathworld.wolfram.com/WilsonsTheorem.html)
- [About Euler’s Identity — Euler-Franeker Memorial University](https://euler.euclid.int/about-eulers-identity/)
- [Fermat’s Last Theorem — University of Cambridge](https://www.maths.cam.ac.uk/features/node/153)
- [The Basel Problem — University of Kentucky](https://clp.math.uky.edu/clp2/chap_seq_ser-5.html)
- [Euler’s prime-producing polynomial revisited — Cambridge University Press](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1F76183BF30CECE688E31E8F10F37AC8/S0025557224000111a.pdf/eulers_primeproducing_polynomial_revisited.pdf)
