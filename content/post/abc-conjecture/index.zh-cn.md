---
title: "ABC猜想与IUT：一项证明主张及其持续的争论"
date: "2026-09-14T13:00:00+09:00"
lastmod: 2026-11-23
slug: "abc-conjecture"
image: "eyecatch.jpg"
categories: ["mathematics", "science"]
tags: ["ABC Conjecture", "Number Theory", "IUT Theory", "Shinichi Mochizuki"]
draft: false
description: "介绍ABC猜想、望月新一通过IUT证明ABC的主张、论文在PRIMS发表的事实，以及尚未解决的数学争论。"
---

## ABC猜想的内容

设 $a,b,c$ 是两两互素的正整数，且满足 $a+b=c$。正整数 $n$ 的**根基**是整除 $n$ 的不同素数的乘积：

$$\operatorname{rad}(n)=\prod_{p\mid n}p$$

例如，$\operatorname{rad}(2^3\cdot3^2)=6$。根基不计素因子的指数，因此可能远小于整数本身。

ABC猜想称：对任意 $\varepsilon>0$，存在常数 $K_\varepsilon$，使每个这样的三元组都满足

$$c\le K_\varepsilon\operatorname{rad}(abc)^{1+\varepsilon}.$$

常数可以依赖于 $\varepsilon$。约瑟夫·奥斯特莱和戴维·马瑟于1985年提出这一猜想。它表达了加法与素因数分解之间的强约束，并不是“$a$、$b$ 含有小素因子就一定会迫使 $c$ 含有大素因子”这样简单的规则。

## 望月新一通过IUT提出的证明主张

2012年，京都大学的望月新一发表论文，提出宇宙际泰希米勒理论（IUT），作为研究包括ABC猜想在内的丢番图几何问题的新框架。IUT是一套高度技术化的理论，研究数域上的椭圆曲线等算术对象，并结合与泰希米勒理论、霍奇–阿拉克洛夫理论及远阿贝尔几何相关的思想。霍奇剧场、对数-θ格等概念用于比较不同结构之间的算术数据。若把它简化为“把加法和乘法放进不同宇宙”，会造成误解。

望月主张ABC猜想可由IUT推出。四篇论文经历了漫长的审稿过程，并于2021年刊登在《Publications of the Research Institute for Mathematical Sciences》（PRIMS）的IUT专刊中。论文发表是重要事实，但它本身并不等于整个数学界达成共识，也不代表争论已经结束。

## 仍存争议的部分

彼得·肖尔策和雅各布·斯蒂克斯在2018年的报告中指出，从IUT III的定理3.11到推论3.12这一关键步骤存在论证缺口，而该步骤用于导出ABC不等式。望月认为这项批评源自对理论的误解，并在2025年10月的报告中再次阐述了自己的立场。这里仅概述作者公开表达的观点，并非对IUT证明的独立核验。

严谨的介绍应区分三件事：IUT论文已在PRIMS发表；望月声称这些论文证明了ABC猜想；数学家对核心论证的分歧尚未解决。将ABC猜想说成已被普遍确立的定理并不准确。

## 与费马大定理的关系

如果ABC猜想成立，就能推出费马大定理：当 $n\ge3$ 时，方程 $x^n+y^n=z^n$ 没有正整数解。这是一个条件性推论，并不意味着费马大定理尚未证明；安德鲁·怀尔斯等人早已证明该定理。

假设存在两两互素的正整数解 $x,y,z$。那么对每个正整数 $k$，$(x^{nk},y^{nk},z^{nk})$ 也是满足加法关系的互素三元组。其根基保持不变：$\operatorname{rad}(x^{nk}y^{nk}z^{nk})=\operatorname{rad}(xyz)$，而 $z^{nk}$ 会无限增大。因此会有无穷多个三元组违反任意固定 $\varepsilon>0$ 对应的ABC上界，产生矛盾。

## 参考资料

- [ABC猜想的标准表述（Jordan S. Ellenberg）](https://arxiv.org/abs/math/9909098)
- [2021年PRIMS的IUT专刊](https://ems.press/journals/prims/issues/1507)
- [肖尔策与斯蒂克斯的报告（2018）](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf)
- [望月的IUT报告（2025年10月）](https://www.kurims.kyoto-u.ac.jp/~motizuki/IUT-report-2025-10.pdf)
- [IUT概览（望月，2012）](https://www.kurims.kyoto-u.ac.jp/~motizuki/Panoramic%20Overview%20of%20Inter-universal%20Teichmuller%20Theory.pdf)

本文是对猜想和公开争论的简短介绍，不会重构或评判IUT证明。
