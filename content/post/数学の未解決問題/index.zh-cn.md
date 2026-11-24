---
title: '充满魅力的数学未解之谜：什么是完全数、哥德巴赫猜想、黎曼猜想？'
slug: "数学の未解决问题"
tags: ["数学","未解决问题"]
draft: false
math: true
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: '通俗易懂地解说题目本身看似简单却至今仍未被证明的、充满魅力的数学未解之谜。完全数有无数个吗？我们将带您走近哥德巴赫猜想、世纪难题黎曼猜想等一直困扰着数学家们的各种神秘问题。'
date: "2024-03-02T22:57:36+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

# 数学中的未解问题

本文介绍一些表述简洁但尚无已知证明的数论问题，并区分已经证明的结论与仍未解决的问题。

## 完全数有无穷多个吗？

完全数是指一个正整数等于其所有不包括自身的正因数之和。

- 6除自身以外的正因数为1、2、3，且1+2+3=6。
- 28除自身以外的正因数为1、2、4、7、14，且1+2+4+7+14=28。

目前已知52个偶完全数，其中包括由2024年确认的梅森素数所对应的完全数。尚未发现奇完全数。偶完全数是否有无穷多个、奇完全数是否存在，都是未解问题。

## 哥德巴赫猜想

[哥德巴赫猜想](/zh-cn/p/goldbachs-conjecture/)的强形式（二元形式）称，任何大于2的偶整数都能表示为两个素数之和。例如4=2+2、8=3+5、10=3+7。素数是大于1且正因数只有1和自身的整数。强形式至今仍未解决。

与之不同的弱形式（三元形式）称，任何大于5的奇整数都是三个素数之和。Harald Helfgott已证明这一命题。

## [黎曼猜想](https://kenji.blog/zh-cn/p/riemann-hypothesis-prime-distribution-cryptography/)

当复数 $s$ 的实部大于1时，黎曼ζ函数可由以下狄利克雷级数表示：

$$\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}=1+\frac{1}{2^s}+\frac{1}{3^s}+\frac{1}{4^s}+\cdots$$

该级数在 $\operatorname{Re}(s)>1$ 时收敛。ζ函数可亚纯延拓到整个复平面，并在 $s=1$ 处有一个简单极点。它在负偶整数 $-2,-4,-6,\ldots$ 处的零点称为平凡零点。非平凡零点位于临界带 $0<\operatorname{Re}(s)<1$。黎曼猜想称所有非平凡零点的实部均为 $1/2$。该猜想仍未解决。

## 参考资料

- [GIMPS：已知梅森素数列表（截至第52个）](https://www.mersenne.org/primes/)
- [NIST DLMF §27.4：ζ函数的狄利克雷级数及其收敛性](https://dlmf.nist.gov/27.4)
- [NIST DLMF §25.2：ζ函数的解析延拓与极点](https://dlmf.nist.gov/25.2)
- [克雷数学研究所：黎曼猜想](https://www.claymath.org/millennium/Riemann-Hypothesis/)
- [H. A. Helfgott：三素数哥德巴赫问题的证明（arXiv）](https://arxiv.org/abs/1312.7748)
