---
title: '迷人的數學未解之謎：什麼是完全數、哥德巴赫猜想、黎曼猜想？'
slug: "數學の未解決問題"
tags: ["數學","未解問題"]
draft: false
math: true
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: '淺顯易懂地解說問題本身雖然簡單，卻至今仍未被證明的迷人數學未解之謎。完全數是否無限多？深入探討哥德巴赫猜想與世紀難題黎曼猜想等，不斷困擾著數學家們的眾多神祕問題。'
date: "2024-03-02T22:57:36+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

# 數學的未解問題

本文介紹一些敘述簡潔、但目前尚無已知證明的數論問題，並區分已證明的結果與尚未解決的問題。

## 完全數有無限多個嗎？

完全數是指一個正整數等於其所有不包括自身的正因數之和。

- 6除自身以外的正因數為1、2、3，且1+2+3=6。
- 28除自身以外的正因數為1、2、4、7、14，且1+2+4+7+14=28。

目前已知52個偶完全數，其中包括由2024年確認的梅森質數所對應的完全數。尚未發現奇完全數。偶完全數是否有無限多個、奇完全數是否存在，都是未解問題。

## 哥德巴赫猜想

[哥德巴赫猜想](/zh-tw/p/goldbachs-conjecture/)的強形式（二元形式）指出，任何大於2的偶整數都能表示為兩個質數之和。例如4=2+2、8=3+5、10=3+7。質數是大於1且正因數只有1和自身的整數。強形式至今仍未解決。

與之不同的弱形式（三元形式）指出，任何大於5的奇整數都是三個質數之和。Harald Helfgott已證明此命題。

## [黎曼猜想](https://kenji.blog/zh-tw/p/riemann-hypothesis-prime-distribution-cryptography/)

當複數 $s$ 的實部大於1時，黎曼ζ函數可由下列狄利克雷級數表示：

$$\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}=1+\frac{1}{2^s}+\frac{1}{3^s}+\frac{1}{4^s}+\cdots$$

此級數在 $\operatorname{Re}(s)>1$ 時收斂。ζ函數可亞純延拓至整個複平面，並在 $s=1$ 有一個簡單極點。它在負偶整數 $-2,-4,-6,\ldots$ 的零點稱為平凡零點。非平凡零點位於臨界帶 $0<\operatorname{Re}(s)<1$。黎曼猜想指出所有非平凡零點的實部都是 $1/2$。此猜想仍未解決。

## 參考資料

- [GIMPS：已知梅森質數列表（截至第52個）](https://www.mersenne.org/primes/)
- [NIST DLMF §27.4：ζ函數的狄利克雷級數及其收斂性](https://dlmf.nist.gov/27.4)
- [NIST DLMF §25.2：ζ函數的解析延拓與極點](https://dlmf.nist.gov/25.2)
- [克雷數學研究所：黎曼猜想](https://www.claymath.org/millennium/Riemann-Hypothesis/)
- [H. A. Helfgott：三質數哥德巴赫問題的證明（arXiv）](https://arxiv.org/abs/1312.7748)
