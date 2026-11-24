---
title: "P 與 NP 問題：計算複雜度理論中的未解問題"
slug: "P≠NP猜想"
tags: ["P≠NP猜想", "數學", "未解問題"]
draft: false
categories: ["math-cryptography-quantum"]
description: "透過多項式長度證明憑證與 SAT 範例，介紹 P、NP，以及 P 是否等於 NP 這個未解問題。"
image: eyecatch.jpg
date: 2024-09-11T02:22:39+09:00
lastmod: 2026-11-24
---
# 什麼是 P 與 NP？

**P** 是指可在相對於輸入大小的多項式時間內解決的判定問題類別。**NP** 是指對每個答案為「是」的輸入，都有一份長度受輸入大小多項式界定的證明憑證（候選解），且可在多項式時間內驗證其正確性的判定問題類別。P 中的問題也能在多項式時間內驗證，因此 **P ⊆ NP**。

## 以 SAT 為例

SAT 詢問給定布林公式是否存在能使公式為真的變數指派。對答案為「是」的輸入，該指派就是證明憑證；檢查它是否滿足每個子句，只需相對於公式大小的多項式時間。SAT（包括 3-SAT）是 NP 完全問題。因此，若 SAT 有多項式時間演算法，就能推出 **P = NP**。NP 完全表示 NP 中的每個問題都能在多項式時間內歸約至該問題。

## 尚未解決的問題

**P = NP 還是 P ≠ NP** 仍未解決。克雷數學研究所將 P 與 NP 問題列為未解問題。P≠NP 是廣受研究的猜想，並非已證明的定理。簡單來說，這是在問：凡是能有效率地驗證候選解的問題，是否也都能有效率地求解？

## 參考資料

- [Clay Mathematics Institute: P vs NP](https://www.claymath.org/millennium/p-vs-np/)
- [Stephen Cook, official problem description (PDF)](https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf)
- [MIT OpenCourseWare: NP-Completeness, Lecture 16 (PDF)](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/f2829e57caade7e7f21d765b8e7b9058_MIT6_046JS15_lec16.pdf)
