---
title: 'Fascinating Unsolved Math Problems: What are Perfect Numbers, Goldbach''s Conjecture, and the Riemann Hypothesis?'
slug: "MathematicsのUnsolved Problem"
tags: ["Mathematics", "Unsolved Problems"]
draft: false
math: true
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: 'We explain fascinating unsolved math problems that remain unproven despite their simple premises. Are there infinitely many perfect numbers? We explore the mysterious problems that continue to puzzle mathematicians, such as Goldbach''s conjecture and the difficult Riemann Hypothesis.'
date: "2024-03-02T22:57:36+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

# Unsolved Problems in Mathematics

This article introduces number theory problems with concise statements but no known proofs. It distinguishes what has been proved from what remains open.

## Are there infinitely many perfect numbers?

A perfect number is a positive integer equal to the sum of its positive divisors other than itself.

- The proper positive divisors of 6 are 1, 2, and 3, and 1+2+3=6.
- The proper positive divisors of 28 are 1, 2, 4, 7, and 14, and 1+2+4+7+14=28.

There are 52 known even perfect numbers, including the one obtained from the Mersenne prime confirmed in 2024. No odd perfect number is known. Whether infinitely many even perfect numbers exist and whether any odd perfect number exists are both open questions.

## Goldbach's conjecture

The strong (binary) form of [Goldbach's conjecture](/en/p/goldbachs-conjecture/) says that every even integer greater than 2 is the sum of two primes. For example, 4=2+2, 8=3+5, and 10=3+7. A prime is an integer greater than 1 whose only positive divisors are 1 and itself. This strong form remains open.

The distinct weak (ternary) form says that every odd integer greater than 5 is the sum of three primes. Harald Helfgott proved this statement.

## [The Riemann hypothesis](https://kenji.blog/en/p/riemann-hypothesis-prime-distribution-cryptography/)

For a complex number $s$ with real part greater than 1, the Riemann zeta function is represented by the following Dirichlet series:

$$\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}=1+\frac{1}{2^s}+\frac{1}{3^s}+\frac{1}{4^s}+\cdots$$

This series converges for $\operatorname{Re}(s)>1$. The zeta function extends meromorphically to the whole complex plane, with a simple pole at $s=1$. Its zeros at the negative even integers $-2,-4,-6,\ldots$ are called trivial zeros. The nontrivial zeros lie in the critical strip $0<\operatorname{Re}(s)<1$. The Riemann hypothesis states that every nontrivial zero has real part $1/2$. It remains open.

## References

- [GIMPS: list of known Mersenne primes (through the 52nd)](https://www.mersenne.org/primes/)
- [NIST DLMF §27.4: Dirichlet series for the zeta function and its convergence](https://dlmf.nist.gov/27.4)
- [NIST DLMF §25.2: analytic continuation and the pole of the zeta function](https://dlmf.nist.gov/25.2)
- [Clay Mathematics Institute: Riemann Hypothesis](https://www.claymath.org/millennium/Riemann-Hypothesis/)
- [H. A. Helfgott: proof of the ternary Goldbach problem (arXiv)](https://arxiv.org/abs/1312.7748)
