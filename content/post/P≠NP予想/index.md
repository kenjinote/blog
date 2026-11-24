---
title: "P≠NP予想：計算量理論の未解決問題"
slug: "P≠NP予想"
tags: ["P≠NP予想", "数学", "未解決問題"]
draft: false
categories: ["math-cryptography-quantum"]
description: "クラスPとNP、証明書の長さ、SATの例を通して、PとNPが等しいかという未解決問題を説明します。"
image: eyecatch.jpg
date: 2024-09-11T02:22:39+09:00
lastmod: 2026-11-24
---
# PとNPとは

**P**は、入力サイズの多項式時間で解ける決定問題のクラスです。**NP**は、Yesである入力について、入力サイズの多項式で抑えられる長さの証明書（解の候補）があれば、それを多項式時間で検証できる決定問題のクラスです。ここで「多項式」は入力サイズに対するものです。解ける問題は解を求めてから検証できるため、**P ⊆ NP**です。

## SATを例にする

SATは、与えられた論理式を真にする変数への割当てが存在するかを問う問題です。Yesの例では、その割当てを証明書として渡し、各節が満たされるかを式のサイズに対して多項式時間で確認できます。SAT（3-SATを含む）はNP完全です。したがってSATに多項式時間アルゴリズムが見つかれば **P = NP** が導かれます。NP完全とは、NPのどの問題も多項式時間でその問題へ帰着できることを指します。

## 未解決の問い

**P = NPか、それともP ≠ NPか**は未解決です。クレイ数学研究所はP対NP問題を未解決問題として掲載しています。P≠NPは広く研究される予想ですが、証明済みの定理として述べることはできません。この問題は、解を効率よく検証できるなら効率よく見つけられるのか、という問いです。

## 参考資料

- [Clay Mathematics Institute: P vs NP](https://www.claymath.org/millennium/p-vs-np/)
- [Stephen Cook, official problem description (PDF)](https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf)
- [MIT OpenCourseWare: NP-Completeness, Lecture 16 (PDF)](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/f2829e57caade7e7f21d765b8e7b9058_MIT6_046JS15_lec16.pdf)
