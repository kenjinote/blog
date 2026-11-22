---
title: "The ABC Conjecture and IUT: A Claimed Proof and an Ongoing Debate"
date: "2026-09-14T13:00:00+09:00"
lastmod: 2026-11-23
slug: "abc-conjecture"
image: "eyecatch.jpg"
categories: ["mathematics", "science"]
tags: ["ABC Conjecture", "Number Theory", "IUT Theory", "Shinichi Mochizuki"]
draft: false
description: "An accessible account of the ABC conjecture, Shinichi Mochizuki’s claimed IUT proof, its publication in PRIMS, and the unresolved mathematical debate."
---

## What the ABC conjecture says

Let $a,b,c$ be pairwise coprime positive integers with $a+b=c$. The **radical** of a positive integer $n$ is the product of its distinct prime divisors:

$$\operatorname{rad}(n)=\prod_{p\mid n}p$$

For example, $\operatorname{rad}(2^3\cdot3^2)=6$. The radical ignores prime exponents and can therefore be much smaller than the integer itself.

The ABC conjecture says that for every $\varepsilon>0$ there is a constant $K_\varepsilon$ such that every such triple satisfies

$$c\le K_\varepsilon\operatorname{rad}(abc)^{1+\varepsilon}.$$

The constant may depend on $\varepsilon$. Joseph Oesterlé and David Masser formulated the conjecture in 1985. It expresses a strong constraint linking addition to prime factorization; it is not the simple rule that small prime factors of $a$ and $b$ force $c$ to have a large prime factor.

## Mochizuki’s claimed proof through IUT

In 2012, Shinichi Mochizuki of Kyoto University released papers introducing Inter-universal Teichmüller theory (IUT) as a new framework for problems in Diophantine geometry, including the ABC conjecture. IUT is a highly technical theory involving arithmetic objects such as elliptic curves over number fields and ideas related to Teichmüller theory, Hodge–Arakelov theory, and anabelian geometry. Concepts such as Hodge theaters and the log-theta lattice are used to compare arithmetic data across structures. Describing it simply as “putting addition and multiplication in separate universes” would be misleading.

Mochizuki claims that the ABC conjecture follows from IUT. The four papers underwent a lengthy refereeing process and appeared in a 2021 special issue of *Publications of the Research Institute for Mathematical Sciences* (PRIMS). Publication is an important fact, but it does not by itself establish consensus across mathematics or end the dispute.

## What remains disputed

In a 2018 report, Peter Scholze and Jakob Stix argued that a key step—moving from Theorem 3.11 to Corollary 3.12 of IUT III, which is used in the route to the ABC inequality—has a gap. Mochizuki rejects their criticism as based on a misunderstanding of the theory and restated his position in an October 2025 report. This paragraph summarizes the authors’ stated positions; it is not an independent verification of the IUT proof.

A careful account therefore distinguishes three points: the IUT papers were published in PRIMS; Mochizuki claims they prove ABC; and mathematicians have not resolved their disagreement about the central argument. It is misleading to present the ABC conjecture as a broadly established theorem.

## Connection to Fermat’s Last Theorem

If true, ABC would imply Fermat’s Last Theorem: there are no positive integer solutions to $x^n+y^n=z^n$ for $n\ge3$. This is a conditional consequence, not a claim that Fermat’s theorem remains unproved; Andrew Wiles and others already proved it. Here is the short implication.

Suppose a pairwise coprime solution $x,y,z$ existed. For every positive integer $k$, $(x^{nk},y^{nk},z^{nk})$ would also be a coprime addition triple. Its radical would stay fixed, $\operatorname{rad}(x^{nk}y^{nk}z^{nk})=\operatorname{rad}(xyz)$, while $z^{nk}$ would grow without bound. Thus infinitely many triples would violate the ABC upper bound for any fixed $\varepsilon>0$, a contradiction.

## References

- [A standard formulation of ABC (Jordan S. Ellenberg)](https://arxiv.org/abs/math/9909098)
- [The 2021 PRIMS IUT special issue](https://ems.press/journals/prims/issues/1507)
- [Scholze–Stix report (2018)](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf)
- [Mochizuki’s IUT report (October 2025)](https://www.kurims.kyoto-u.ac.jp/~motizuki/IUT-report-2025-10.pdf)
- [A panoramic overview of IUT (Mochizuki, 2012)](https://www.kurims.kyoto-u.ac.jp/~motizuki/Panoramic%20Overview%20of%20Inter-universal%20Teichmuller%20Theory.pdf)

This is a brief introduction to the conjecture and the public dispute, not a reconstruction or evaluation of the IUT proof.
