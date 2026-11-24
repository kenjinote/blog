---
title: 'Faszinierende ungelöste mathematische Probleme: Was sind vollkommene Zahlen, die Goldbachsche Vermutung und die Riemannsche Vermutung?'
slug: "MathematikのUngelöstes Problem"
tags: ["Mathematik","Ungelöste Probleme"]
draft: false
math: true
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: 'Wir erklären leicht verständlich faszinierende ungelöste mathematische Probleme, die zwar an sich einfach sind, aber noch nicht bewiesen wurden. Gibt es unendlich viele vollkommene Zahlen? Wir befassen uns mit zahlreichen mysteriösen Problemen, die Mathematiker weiterhin beschäftigen, wie der Goldbachschen Vermutung und der schwierigen Riemannschen Vermutung.'
date: "2024-03-02T22:57:36+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

# Ungelöste Probleme der Mathematik

Hier geht es um zahlentheoretische Probleme mit einfacher Formulierung, für die kein Beweis bekannt ist. Wir unterscheiden zwischen bewiesenen Aussagen und offenen Fragen.

## Gibt es unendlich viele vollkommene Zahlen?

Eine vollkommene Zahl ist eine positive ganze Zahl, die gleich der Summe ihrer positiven echten Teiler ist, also der positiven Teiler außer der Zahl selbst.

- Die echten positiven Teiler von 6 sind 1, 2 und 3; 1+2+3=6.
- Die echten positiven Teiler von 28 sind 1, 2, 4, 7 und 14; 1+2+4+7+14=28.

Es sind 52 gerade vollkommene Zahlen bekannt, darunter diejenige, die sich aus der 2024 bestätigten Mersenne-Primzahl ergibt. Eine ungerade vollkommene Zahl ist nicht bekannt. Ob es unendlich viele gerade vollkommene Zahlen oder überhaupt eine ungerade gibt, ist offen.

## Goldbachsche Vermutung

Die starke (binäre) Form der [Goldbachschen Vermutung](/de/p/goldbachs-conjecture/) besagt, dass jede gerade ganze Zahl größer als 2 die Summe zweier Primzahlen ist. Beispiele sind 4=2+2, 8=3+5 und 10=3+7. Eine Primzahl ist eine ganze Zahl größer als 1, deren einzige positive Teiler 1 und sie selbst sind. Diese starke Form ist weiterhin offen.

Die davon zu unterscheidende schwache (ternäre) Form besagt, dass jede ungerade ganze Zahl größer als 5 die Summe dreier Primzahlen ist. Harald Helfgott hat diese Aussage bewiesen.

## [Riemannsche Vermutung](https://kenji.blog/de/p/riemann-hypothesis-prime-distribution-cryptography/)

Für eine komplexe Zahl $s$ mit Realteil größer als 1 wird die Riemannsche Zetafunktion durch die folgende Dirichlet-Reihe dargestellt:

$$\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}=1+\frac{1}{2^s}+\frac{1}{3^s}+\frac{1}{4^s}+\cdots$$

Diese Reihe konvergiert für $\operatorname{Re}(s)>1$. Die Zetafunktion lässt sich meromorph auf die ganze komplexe Ebene fortsetzen und hat bei $s=1$ einen einfachen Pol. Ihre Nullstellen bei den negativen geraden ganzen Zahlen $-2,-4,-6,\ldots$ heißen triviale Nullstellen. Die nichttrivialen Nullstellen liegen im kritischen Streifen $0<\operatorname{Re}(s)<1$. Die Riemannsche Vermutung besagt, dass alle nichttrivialen Nullstellen den Realteil $1/2$ haben. Sie ist offen.

## Quellen

- [GIMPS: Liste bekannter Mersenne-Primzahlen (bis zur 52.)](https://www.mersenne.org/primes/)
- [NIST DLMF §27.4: Dirichlet-Reihe der Zetafunktion und ihr Konvergenzbereich](https://dlmf.nist.gov/27.4)
- [NIST DLMF §25.2: analytische Fortsetzung und Pol der Zetafunktion](https://dlmf.nist.gov/25.2)
- [Clay Mathematics Institute: Riemannsche Vermutung](https://www.claymath.org/millennium/Riemann-Hypothesis/)
- [H. A. Helfgott: Beweis des ternären Goldbach-Problems (arXiv)](https://arxiv.org/abs/1312.7748)
