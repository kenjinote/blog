---
title: "P与NP问题：计算复杂性理论中的未解问题"
slug: "P≠NP猜想"
tags: ["P≠NP猜想", "数学", "未解决问题"]
draft: false
categories: ["math-cryptography-quantum"]
description: "通过多项式长度证书和SAT示例，介绍P、NP以及P是否等于NP这一未解问题。"
image: eyecatch.jpg
date: 2024-09-11T02:22:39+09:00
lastmod: 2026-11-24
---
# 什么是P和NP？

**P**是指能在关于输入规模的多项式时间内求解的判定问题类。**NP**是指对于每个答案为“是”的实例，都存在一个长度受输入规模多项式界定的证书（候选解），并且可以在多项式时间内验证其正确性的判定问题类。P中的问题也能在多项式时间内验证，因此 **P ⊆ NP**。

## 以SAT为例

SAT询问给定布尔公式是否存在使公式为真的变量赋值。对于答案为“是”的实例，该赋值就是证书；检查它是否满足每个子句，只需关于公式长度的多项式时间。SAT（包括3-SAT）是NP完全问题。因此，如果SAT存在多项式时间算法，就能推出 **P = NP**。NP完全表示NP中的每个问题都能在多项式时间内归约到该问题。

## 尚未解决的问题

**P = NP还是P ≠ NP**仍未解决。克雷数学研究所将P与NP问题列为未解决问题。P≠NP是受到广泛研究的猜想，并非已经证明的定理。通俗地说，这个问题是在问：凡是能高效验证候选解的问题，是否也都能高效求解？

## 参考资料

- [Clay Mathematics Institute: P vs NP](https://www.claymath.org/millennium/p-vs-np/)
- [Stephen Cook, official problem description (PDF)](https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf)
- [MIT OpenCourseWare: NP-Completeness, Lecture 16 (PDF)](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/f2829e57caade7e7f21d765b8e7b9058_MIT6_046JS15_lec16.pdf)
