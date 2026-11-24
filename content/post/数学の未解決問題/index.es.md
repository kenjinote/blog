---







title: 'Los fascinantes problemas no resueltos de las matemáticas: ¿Qué son los números perfectos, la conjetura de Goldbach y la hipótesis de Riemann?'
slug: "MatemáticasのProblema no resuelto"
tags: ["Matemáticas", "Problemas no resueltos"]
draft: false
math: true
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: 'Explicamos de forma sencilla los fascinantes problemas matemáticos sin resolver que, a pesar de su simplicidad, siguen sin ser demostrados. ¿Existen infinitos números perfectos? Nos adentramos en numerosos problemas misteriosos que continúan desconcertando a los matemáticos, como la conjetura de Goldbach y la difícil hipótesis de Riemann.'
date: "2024-03-02T22:57:36+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

# Problemas no resueltos de las matemáticas

Este artículo presenta problemas de teoría de números cuya formulación es sencilla, pero para los que no se conoce una demostración. Distinguimos los resultados probados de las cuestiones abiertas.

## ¿Hay infinitos números perfectos?

Un número perfecto es un entero positivo igual a la suma de sus divisores positivos propios, es decir, los divisores positivos distintos del propio número.

- Los divisores propios positivos de 6 son 1, 2 y 3; 1+2+3=6.
- Los de 28 son 1, 2, 4, 7 y 14; 1+2+4+7+14=28.

Se conocen 52 números perfectos pares, incluido el que se obtiene del primo de Mersenne confirmado en 2024. No se conoce ningún número perfecto impar. Sigue abierto si existen infinitos números perfectos pares y si existe alguno impar.

## Conjetura de Goldbach

La forma fuerte (binaria) de la [conjetura de Goldbach](/es/p/goldbachs-conjecture/) afirma que todo entero par mayor que 2 es la suma de dos primos. Por ejemplo, 4=2+2, 8=3+5 y 10=3+7. Un primo es un entero mayor que 1 cuyos únicos divisores positivos son 1 y él mismo. Esta forma fuerte sigue sin resolverse.

La forma débil (ternaria), que es distinta, afirma que todo entero impar mayor que 5 es la suma de tres primos. Harald Helfgott demostró esta afirmación.

## [Hipótesis de Riemann](https://kenji.blog/es/p/riemann-hypothesis-prime-distribution-cryptography/)

Para un número complejo $s$ cuya parte real es mayor que 1, la función zeta de Riemann se representa mediante la siguiente serie de Dirichlet:

$$\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}=1+\frac{1}{2^s}+\frac{1}{3^s}+\frac{1}{4^s}+\cdots$$

Esta serie converge cuando $\operatorname{Re}(s)>1$. La función zeta admite continuación meromorfa a todo el plano complejo y tiene un polo simple en $s=1$. Sus ceros en los enteros pares negativos $-2,-4,-6,\ldots$ se llaman ceros triviales. Los ceros no triviales se encuentran en la franja crítica $0<\operatorname{Re}(s)<1$. La hipótesis de Riemann afirma que todos ellos tienen parte real $1/2$. Sigue sin resolverse.

## Referencias

- [GIMPS: lista de primos de Mersenne conocidos (hasta el 52.º)](https://www.mersenne.org/primes/)
- [NIST DLMF §27.4: serie de Dirichlet de la función zeta y su convergencia](https://dlmf.nist.gov/27.4)
- [NIST DLMF §25.2: continuación analítica y polo de la función zeta](https://dlmf.nist.gov/25.2)
- [Clay Mathematics Institute: hipótesis de Riemann](https://www.claymath.org/millennium/Riemann-Hypothesis/)
- [H. A. Helfgott: demostración del problema ternario de Goldbach (arXiv)](https://arxiv.org/abs/1312.7748)
