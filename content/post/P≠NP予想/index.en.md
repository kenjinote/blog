---
title: "The P vs. NP Conjecture: An Open Problem in Complexity Theory"
slug: "P!=NP Conjecture"
tags: ["P≠NP conjecture", "Math", "Unsolved problems"]
draft: false
categories: ["math-cryptography-quantum"]
description: "An introduction to P, NP, polynomial-length certificates, SAT, and the open question of whether P equals NP."
image: eyecatch.jpg
date: 2024-09-11T02:22:39+09:00
lastmod: 2026-11-24
---
# What are P and NP?

**P** is the class of decision problems solvable in polynomial time in the input size. **NP** is the class of decision problems for which every yes-instance has a certificate (a proposed solution) whose length is bounded by a polynomial in the input size and whose validity can be checked in polynomial time. Because a solution to a problem in P can also be checked in polynomial time, **P ⊆ NP**.

## SAT as an example

SAT asks whether a given Boolean formula has an assignment that makes it true. For a yes-instance, the assignment is a certificate: checking that it satisfies every clause takes polynomial time in the formula size. SAT, including 3-SAT, is NP-complete. Therefore, a polynomial-time algorithm for SAT would imply **P = NP**. NP-completeness means that every problem in NP can be reduced to the problem in polynomial time.

## The open question

Whether **P = NP** or **P ≠ NP** remains open. The Clay Mathematics Institute lists P vs. NP as unsolved. P≠NP is a widely studied conjecture, not a proved theorem. Informally, the question asks whether every problem whose proposed solution can be checked efficiently can also be solved efficiently.

## References

- [Clay Mathematics Institute: P vs NP](https://www.claymath.org/millennium/p-vs-np/)
- [Stephen Cook, official problem description (PDF)](https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf)
- [MIT OpenCourseWare: NP-Completeness, Lecture 16 (PDF)](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/f2829e57caade7e7f21d765b8e7b9058_MIT6_046JS15_lec16.pdf)
