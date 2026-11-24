---
title: 'Fascinantes problemas não resolvidos da matemática: O que são números perfeitos, a Conjectura de Goldbach e a Hipótese de Riemann?'
slug: "MatemáticaのProblema Não Resolvido"
tags: ["Matemática","Problemas não resolvidos"]
draft: false
math: true
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: 'Explicaremos de forma fácil de entender problemas matemáticos fascinantes e não resolvidos que, embora simples em si mesmos, ainda não foram provados. Existem infinitos números perfeitos? Abordaremos vários problemas misteriosos que continuam a atormentar os matemáticos, como a Conjectura de Goldbach e a difícil Hipótese de Riemann.'
date: "2024-03-02T22:57:36+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

# Problemas não resolvidos da matemática

Este artigo apresenta problemas de teoria dos números com enunciados simples, mas sem demonstração conhecida. Separamos o que já foi provado das questões ainda em aberto.

## Existem infinitos números perfeitos?

Um número perfeito é um inteiro positivo igual à soma de seus divisores positivos próprios, isto é, os divisores positivos diferentes do próprio número.

- Os divisores próprios positivos de 6 são 1, 2 e 3; 1+2+3=6.
- Os de 28 são 1, 2, 4, 7 e 14; 1+2+4+7+14=28.

São conhecidos 52 números perfeitos pares, incluindo o obtido a partir do primo de Mersenne confirmado em 2024. Não se conhece nenhum número perfeito ímpar. Continua em aberto se há infinitos números perfeitos pares ou se existe algum ímpar.

## Conjectura de Goldbach

A forma forte (binária) da [conjectura de Goldbach](/pt/p/goldbachs-conjecture/) afirma que todo inteiro par maior que 2 é a soma de dois números primos. Por exemplo, 4=2+2, 8=3+5 e 10=3+7. Um primo é um inteiro maior que 1 cujos únicos divisores positivos são 1 e ele próprio. Essa forma forte continua em aberto.

A forma fraca (ternária), que é diferente, afirma que todo inteiro ímpar maior que 5 é a soma de três primos. Harald Helfgott provou essa afirmação.

## [Hipótese de Riemann](https://kenji.blog/pt/p/riemann-hypothesis-prime-distribution-cryptography/)

Para um número complexo $s$ cuja parte real é maior que 1, a função zeta de Riemann é representada pela seguinte série de Dirichlet:

$$\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}=1+\frac{1}{2^s}+\frac{1}{3^s}+\frac{1}{4^s}+\cdots$$

Essa série converge para $\operatorname{Re}(s)>1$. A função zeta admite continuação meromorfa a todo o plano complexo e tem um polo simples em $s=1$. Seus zeros nos inteiros pares negativos $-2,-4,-6,\ldots$ são chamados de zeros triviais. Os zeros não triviais ficam na faixa crítica $0<\operatorname{Re}(s)<1$. A hipótese de Riemann afirma que todos eles têm parte real igual a $1/2$. Ela continua em aberto.

## Referências

- [GIMPS: lista dos números primos de Mersenne conhecidos (até o 52.º)](https://www.mersenne.org/primes/)
- [NIST DLMF §27.4: série de Dirichlet da função zeta e sua convergência](https://dlmf.nist.gov/27.4)
- [NIST DLMF §25.2: continuação analítica e polo da função zeta](https://dlmf.nist.gov/25.2)
- [Clay Mathematics Institute: hipótese de Riemann](https://www.claymath.org/millennium/Riemann-Hypothesis/)
- [H. A. Helfgott: prova do problema ternário de Goldbach (arXiv)](https://arxiv.org/abs/1312.7748)
