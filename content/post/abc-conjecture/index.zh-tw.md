---
title: "ABC 猜想與 IUT：一項證明主張及其持續的爭論"
date: "2026-09-14T13:00:00+09:00"
lastmod: 2026-11-23
slug: "abc-conjecture"
image: "eyecatch.jpg"
categories: ["mathematics", "science"]
tags: ["ABC Conjecture", "Number Theory", "IUT Theory", "Shinichi Mochizuki"]
draft: false
description: "介紹 ABC 猜想、望月新一透過 IUT 證明 ABC 的主張、論文在 PRIMS 發表的事實，以及尚未解決的數學爭論。"
---

## ABC 猜想的內容

設 $a,b,c$ 是兩兩互質的正整數，且滿足 $a+b=c$。正整數 $n$ 的**根基**是整除 $n$ 的相異質數之乘積：

$$\operatorname{rad}(n)=\prod_{p\mid n}p$$

例如，$\operatorname{rad}(2^3\cdot3^2)=6$。根基不計質因數的指數，因此可能遠小於整數本身。

ABC 猜想指出：對任意 $\varepsilon>0$，存在常數 $K_\varepsilon$，使每個這樣的三元組都滿足

$$c\le K_\varepsilon\operatorname{rad}(abc)^{1+\varepsilon}.$$

常數可以依賴 $\varepsilon$。約瑟夫·奧斯特萊和大衛·馬瑟於 1985 年提出這項猜想。它表達加法與質因數分解之間的強烈限制，並非「$a$、$b$ 含有小質因數就一定迫使 $c$ 含有大質因數」這種簡單規則。

## 望月新一透過 IUT 提出的證明主張

2012 年，京都大學的望月新一發表論文，提出宇宙際泰希米勒理論（IUT），作為研究包括 ABC 猜想在內的丟番圖幾何問題的新架構。IUT 是高度技術化的理論，研究數域上的橢圓曲線等算術對象，並結合與泰希米勒理論、霍奇–阿拉克洛夫理論及遠阿貝爾幾何相關的想法。霍奇劇場、對數-θ 格等概念用於比較不同結構之間的算術資料。若將它簡化為「把加法和乘法放進不同宇宙」，會造成誤解。

望月主張 ABC 猜想可由 IUT 推出。四篇論文經過漫長的審查，並於 2021 年刊登於《Publications of the Research Institute for Mathematical Sciences》（PRIMS）的 IUT 專刊。論文刊登是重要事實，但本身不代表整個數學界達成共識，也不表示爭論已告終。

## 仍有爭議的部分

彼得·肖爾策和雅各布·斯蒂克斯在 2018 年的報告中指出，從 IUT III 的定理 3.11 到推論 3.12 這個關鍵步驟存在論證缺口；該步驟用於導出 ABC 不等式。望月認為這項批評源自對理論的誤解，並在 2025 年 10 月的報告中再次說明自己的立場。本文僅概述作者公開表達的觀點，並未獨立驗證 IUT 證明。

謹慎的說明應區分三件事：IUT 論文已在 PRIMS 發表；望月聲稱論文證明了 ABC 猜想；數學家對核心論證的歧見尚未解決。將 ABC 猜想說成已普遍確立的定理並不準確。

## 與費馬最後定理的關係

若 ABC 猜想成立，就能推出費馬最後定理：當 $n\ge3$ 時，方程式 $x^n+y^n=z^n$ 沒有正整數解。這是條件式推論，不表示費馬最後定理仍未證明；安德魯·懷爾斯等人早已證明該定理。

假設存在兩兩互質的正整數解 $x,y,z$。那麼對每個正整數 $k$，$(x^{nk},y^{nk},z^{nk})$ 也是符合加法關係的互質三元組。其根基固定不變：$\operatorname{rad}(x^{nk}y^{nk}z^{nk})=\operatorname{rad}(xyz)$，但 $z^{nk}$ 會無限增大。因此會有無限多個三元組違反任意固定 $\varepsilon>0$ 對應的 ABC 上界，導致矛盾。

## 參考資料

- [ABC 猜想的標準表述（Jordan S. Ellenberg）](https://arxiv.org/abs/math/9909098)
- [2021 年 PRIMS 的 IUT 專刊](https://ems.press/journals/prims/issues/1507)
- [肖爾策與斯蒂克斯的報告（2018）](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf)
- [望月的 IUT 報告（2025 年 10 月）](https://www.kurims.kyoto-u.ac.jp/~motizuki/IUT-report-2025-10.pdf)
- [IUT 概覽（望月，2012）](https://www.kurims.kyoto-u.ac.jp/~motizuki/Panoramic%20Overview%20of%20Inter-universal%20Teichmuller%20Theory.pdf)

本文簡短介紹這項猜想及公開爭論，不會重構或評判 IUT 證明。
