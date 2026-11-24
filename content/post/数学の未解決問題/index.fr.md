---
title: 'Les fascinants problèmes mathématiques non résolus : Qu''est-ce que les nombres parfaits, la conjecture de Goldbach et l''hypothèse de Riemann ?'
slug: "MathématiquesのProblèmes non résolus"
tags: ["Mathématiques","Problèmes non résolus"]
draft: false
math: true
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: 'Nous expliquons simplement des problèmes mathématiques fascinants non résolus dont l''énoncé est simple mais qui n''ont pas encore été prouvés. Les nombres parfaits sont-ils infinis ? Nous plongeons dans de nombreux problèmes mystérieux qui continuent de tourmenter les mathématiciens, comme la conjecture de Goldbach et la difficile hypothèse de Riemann.'
date: "2024-03-02T22:57:36+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

# Problèmes non résolus en mathématiques

Cet article présente des problèmes de théorie des nombres dont l'énoncé est simple, mais pour lesquels aucune preuve n'est connue. Il distingue les résultats démontrés des questions ouvertes.

## Existe-t-il une infinité de nombres parfaits ?

Un nombre parfait est un entier positif égal à la somme de ses diviseurs positifs propres, c'est-à-dire différents du nombre lui-même.

- Les diviseurs positifs propres de 6 sont 1, 2 et 3 ; 1+2+3=6.
- Ceux de 28 sont 1, 2, 4, 7 et 14 ; 1+2+4+7+14=28.

On connaît 52 nombres parfaits pairs, dont celui obtenu à partir du nombre premier de Mersenne confirmé en 2024. Aucun nombre parfait impair n'est connu. La question de savoir s'il existe une infinité de nombres parfaits pairs ou un nombre parfait impair reste ouverte.

## Conjecture de Goldbach

La forme forte (binaire) de la [conjecture de Goldbach](/fr/p/goldbachs-conjecture/) affirme que tout entier pair supérieur à 2 est la somme de deux nombres premiers. Par exemple, 4=2+2, 8=3+5 et 10=3+7. Un nombre premier est un entier supérieur à 1 dont les seuls diviseurs positifs sont 1 et lui-même. Cette forme forte reste ouverte.

La forme faible (ternaire), distincte, affirme que tout entier impair supérieur à 5 est la somme de trois nombres premiers. Harald Helfgott l'a démontrée.

## [Hypothèse de Riemann](https://kenji.blog/fr/p/riemann-hypothesis-prime-distribution-cryptography/)

Pour un nombre complexe $s$ dont la partie réelle est supérieure à 1, la fonction zêta de Riemann est représentée par la série de Dirichlet suivante :

$$\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}=1+\frac{1}{2^s}+\frac{1}{3^s}+\frac{1}{4^s}+\cdots$$

Cette série converge lorsque $\operatorname{Re}(s)>1$. La fonction zêta se prolonge méromorphiquement à tout le plan complexe et possède un pôle simple en $s=1$. Ses zéros aux entiers pairs négatifs $-2,-4,-6,\ldots$ sont appelés zéros triviaux. Les zéros non triviaux se trouvent dans la bande critique $0<\operatorname{Re}(s)<1$. L'hypothèse de Riemann affirme que leur partie réelle vaut toujours $1/2$. Elle reste ouverte.

## Références

- [GIMPS : liste des nombres premiers de Mersenne connus (jusqu'au 52e)](https://www.mersenne.org/primes/)
- [NIST DLMF §27.4 : série de Dirichlet de la fonction zêta et convergence](https://dlmf.nist.gov/27.4)
- [NIST DLMF §25.2 : prolongement analytique et pôle de la fonction zêta](https://dlmf.nist.gov/25.2)
- [Clay Mathematics Institute : hypothèse de Riemann](https://www.claymath.org/millennium/Riemann-Hypothesis/)
- [H. A. Helfgott : preuve du problème ternaire de Goldbach (arXiv)](https://arxiv.org/abs/1312.7748)
