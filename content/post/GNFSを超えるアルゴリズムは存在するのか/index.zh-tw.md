---
title: '超越 GNFS（一般數體篩法）的演算法存在嗎？'
slug: "beyond-gnfs-integer-factorization-algorithms"
date: "2026-09-11T09:00:00+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["mathematics", "cryptography"]
tags: ["GNFS", "Integer Factorization", "RSA", "Algorithms"]
---

## 1. 簡介：質因數分解與現代密碼學的基礎

RSA 是多種公開金鑰密碼系統之一，其安全性部分建立在大整數難以分解的假設上。但網際網路整體安全並非只依賴 RSA。高效率的分解演算法會威脅採用 RSA 的情境，卻不會自動造成所有通訊基礎設施崩潰。

對一般大整數分解而言，GNFS 是最知名的古典方法之一，曾用於分解 RSA-768、RSA-250 等整數；具有特殊結構的整數可能更適合 SNFS 等方法。[RSA-250 報告](https://eprint.iacr.org/2020/697)

然而，密碼學家與數學家們始終抱持著以下疑問：「超越 GNFS 的古典演算法存在嗎？」「古典電腦的極限在哪裡？」以及「量子電腦將如何打破這個局面？」

本文將徹底解剖 GNFS 背後深奧的數學結構，並針對多項式選擇、篩選處理、基於區塊魏德曼（Block Wiedemann）法的線性代數步驟等進行詳細的技術分析。此外，我們將探討藉由 Coppersmith 改良等對 GNFS 的擴充方法，並從數學的觀點比較與解說古典的次指數時間（Sub-exponential time）演算法與量子多項式時間演算法的決定性差異。

---

## 2. 漸近複雜度與 L 符號（L-notation）

在評估質因數分解演算法的計算[複雜度](/zh-tw/p/time-space-complexity-big-o-notation-examples/)時，通常不使用標準的多項式時間表示法（如 $O(n^k)$ 等），而是使用 **L 符號（L-notation）** 來表達相對於輸入 $n$ 之位數的次指數時間。L 符號定義如下：

$$
L_n[\alpha, c] = \exp \left( (c + o(1)) (\ln n)^\alpha (\ln \ln n)^{1-\alpha} \right)
$$

這裡，$n$ 是質因數分解的目標整數，$\ln n$ 是自然對數，且與 $n$ 的位元長度成正比。
- 當 $\alpha = 0$ 時：$L_n[0, c] = \exp(c \ln \ln n) = (\ln n)^c$，這表示相對於位元長度的 **多項式時間（Polynomial time）** 。
- 當 $\alpha = 1$ 時：$L_n[1, c] = \exp(c \ln n) = n^c$，這表示相對於位元長度的 **指數時間（Exponential time）** 。
- 當 $0 < \alpha < 1$ 時：這介於多項式時間與指數時間之間，稱為 **次指數時間（Sub-exponential time）** 。

過去質因數分解演算法的演進，其實就是逐漸縮小這個 $\alpha$ 值的歷史。
- **CFRAC**：啟發式預期執行時間為 $L_n[1/2,\sqrt{2}]$（[參考資料](https://cacr.uwaterloo.ca/hac/about/chap3.pdf)）。
- **MPQS/QS**：啟發式預期執行時間為 $L_n[1/2,1]$（[FLINT 文件](https://flintlib.org/doc/algorithms/number-theory/quadratic-sieve.html)）。
- **GNFS**：一般的啟發式估算為 $L_n[1/3,(64/9)^{1/3}]$；這不是已證明的下界，也不是直接的實際執行時間（[NFS 分析](https://arxiv.org/abs/2007.02730)）。

---

## 3. GNFS（一般數體篩法）的演算法全貌與數學結構

GNFS 擁有非常複雜且高度的數學基礎。其基本概念是[費馬小定理](https://kenji.blog/zh-tw/p/fermats-little-theorem/)和二次篩法（QS）的延伸，透過找到滿足同餘式 $X^2 \equiv Y^2 \pmod n$ 且 $X \not\equiv \pm Y \pmod n$ 的非平凡解 $(X, Y)$，進而導出 $n$ 的因數 $\gcd(X-Y, n)$。

然而，GNFS 的精髓在於，它並非僅在有理數體 $\mathbb{Q}$ 上進行，而是同時在稱為代數數體（Algebraic Number Field）的擴充體 $\mathbb{Q}(\alpha)$ 及有理數體兩端探索「平滑數（Smooth numbers）」，並透過同態映射來建構同餘關係。

GNFS 的過程大致可以分為 5 個階段。

```mermaid
graph TD
  A["質因數分解問題 (輸入 n)"] --> B["1. 多項式選擇 (Polynomial Selection)"]
  B --> C["2. 篩選處理 (Sieving Phase)"]
  C --> D["3. 濾波階段 (Filtering Phase)"]
  D --> E["4. 線性代數 (Linear Algebra Phase)"]
  E --> F["5. 平方根階段 (Square Root Phase)"]
  F --> G["輸出質因數 p, q"]```

### 3.1 階段 1：多項式選擇 (Polynomial Selection)

GNFS 的成功很大程度上取決於選擇適當的多項式。目標是找到擁有共同根 $m$ 的兩個不可約多項式 $f_1(x)$（有理數側）與 $f_2(x)$（代數數側）。也就是說，
必須滿足 $f_1(m) \equiv f_2(m) \equiv 0 \pmod n$。

通常，有理數側的多項式選擇一次式 $f_1(x) = x - m$，而代數數側的多項式 $f_2(x)$ 則選擇次數為 $d$（典型為 5 或 6）的首一多項式。最經典的方法是 **Base-$m$ 方法** 。
選擇接近 $n$ 的 $1/(d+1)$ 次方的整數 $m = \lfloor n^{1/(d+1)} \rfloor$，並將 $n$ 展開為 $m$ 進位。
$n = c_d m^d + c_{d-1} m^{d-1} + \dots + c_1 m + c_0$
藉此，可以獲得多項式 $f_2(x) = c_d x^d + c_{d-1} x^{d-1} + \dots + c_0$。很明顯地，$f_2(m) = n \equiv 0 \pmod n$。

然而，現代的實作中會使用 **Kleinjung 的演算法** 。此方法在確保多項式係數不會變得極端巨大的同時（偏態/Skewness 的最佳化），還會最佳化代數性質（Murphy 的 $E$ 值或 $\alpha$ 值），以尋找容易在篩選處理中產生平滑數的多項式。僅僅是這個步驟就會投入龐大的運算資源。

### 3.2 階段 2：篩選處理 (Sieving Phase)

當多項式決定後，就會進入演算法中運算負載最重的「篩選（Sieving）」階段。在這裡，我們要探索一對互質的數組 $(a, b)$，這對數組必須滿足以下兩個值同時為「平滑（Smooth）」：

1. **有理數側的範數**: $F_1(a, b) = b \cdot f_1(a/b) = a - bm$
2. **代數數側的範數**: $F_2(a, b) = b^d \cdot f_2(a/b)$

「平滑」意味著該數字僅能被小於或等於指定上限（Sieve bound）的質數進行因數分解。準備好有理數側的質數基底（Factor base）與代數數側的質數基底，並在龐大的探索空間上，利用類似埃拉托斯特尼篩法的方式，高效率地找出平滑數。
目前主流是稱為 **晶格篩法（Lattice Sieving）** 的技術，藉由固定特定的質數 $q$，僅對有理數側與代數數側皆為 $q$ 的倍數的部分晶格上的 $(a, b)$ 數組進行篩選，從而實現了極高的效率。

### 3.3 階段 3：濾波階段 (Filtering Phase)

在篩選處理中找到的平滑關係式（Relations）數量高達數億、甚至數十億。然而，這些也包含了許多無用的資訊。
濾波的目的，是在建構龐大的稀疏矩陣（Sparse Matrix）時，盡可能縮小其維度。

具體來說，會進行以下操作：
- **Singleton removal**: 刪除包含只出現 1 次質因數的關係式。
- **Clique removal / Merging**: 將擁有出現 2 次以上質因數的關係式互相相乘，以消去變數，從而縮減成密度較高、但維度較小的方程式系統。

透過這個過程，數十億行的矩陣將會被壓縮成擁有數千萬行規模的巨大稀疏矩陣 $\mathbf{A}$（元素為體 $\mathbb{F}_2$ 上的 0 與 1）。

### 3.4 階段 4：線性代數 (Linear Algebra Phase)

此處要在 $\mathbb{F}_2$ 上尋找滿足 $\mathbf{A}\mathbf{x}=\mathbf{0}$ 的非零向量 $\mathbf{x}$，也就是稀疏矩陣核空間中的向量。

對於稀疏矩陣，會使用 Block Lanczos、Block Wiedemann 等 Krylov 反覆方法。RSA-250 分解報告記錄了 Block Wiedemann 的實際使用；方法選擇與效能取決於矩陣、實作與計算架構。[RSA-250 報告](https://eprint.iacr.org/2020/697)


### 3.5 階段 5：平方根 (Square Root Phase)

從線性代數的解中，將在有理數側與代數數側各自建構出成為「完全平方」的乘積。
在有理數側，$\prod (a-bm)$ 會成為某個整數 $X$ 的平方 $X^2$；而在代數數側，對應的理想的乘積會在代數數體上成為完全平方 $\gamma^2$。
藉由在代數數體上計算出這個 $\gamma$，並套用映射到有理整數環的同態映射 $\phi: \alpha \mapsto m \pmod n$，便可得到同餘式：
$X^2 \equiv \phi(\gamma)^2 \equiv Y^2 \pmod n$

計算代數數體上的平方根需要使用如 **Montgomery 方法（Montgomery's Method）** 等複雜演算法，且需要深厚的代數數論知識。最後只要計算出 $\gcd(X-Y, n)$，若獲得非平凡的因數，便完成了質因數分解。

---

## 4. 超越 GNFS 的古典演算法存在嗎？

截至目前為止，在一般整數的質因數分解中，尚未發現漸近[複雜度](/zh-tw/p/time-space-complexity-big-o-notation-examples/)低於 $L_n[1/3, c]$ 的古典演算法。然而，為了突破理論上與實務上的極限，存在著一些嘗試與衍生的演算法。

### 4.1 多重數體篩法 (MNFS: Multiple Number Field Sieve)

作為 GNFS 的擴充方法，有 D. Coppersmith 所提出的 **多重數體篩法（MNFS）** 。GNFS 使用了 2 個多項式（有理數側與代數數側），而 MNFS 則是對 1 個有理數側多項式，同時使用多個不同的代數數側多項式。

$$ f_1(x), f_{2,1}(x), f_{2,2}(x), \dots, f_{2,V}(x) $$

透過利用多個代數數體，可以在每個篩選步驟中，飛躍性地提高「在其中一個代數數體中變得平滑」的機率。Coppersmith 成功地藉由這種方法讓[複雜度](/zh-tw/p/time-space-complexity-big-o-notation-examples/) $L_n[1/3, c]$ 中的常數 $c$ 些微減少。
但在實務上，管理多個數體會帶來巨大的額外開銷，因此並未在實用規模的 [RSA](https://kenji.blog/zh-tw/p/modern-cryptography-public-key-hash-signature/) 模數分解上達到決定性的突破。

### 4.2 $L_n[1/4]$ 類別的演算法有可能嗎？

目前尚無漸近複雜度低於一般 GNFS 形式的通用古典質因數分解演算法，但這不能證明更好的演算法不可能存在。平滑數分析描述已知篩法的限制，並未證明所有演算法的下界；此問題仍未解決。
---

## 5. 量子運算的突破：Shor 演算法

在古典電腦面臨 $L_n[1/3]$ 障礙的同時，Peter Shor 於 1994 年發表的 **Shor 演算法（[Shor's Algorithm](https://kenji.blog/zh-tw/p/quantum-computing-shors-algorithm/)）** 透過從根本上改變運算模型，粉碎了這個障礙。

### 5.1 量子多項式時間的衝擊

Shor 演算法將質因數分解問題化約為「求階問題（Order Finding Problem）」。對於某個整數 $a$，這是一個找出函數 $f(x) = a^x \pmod n$ 之週期（階數）$r$ 的問題。
Shor 利用量子干涉萃取函數週期的資訊；這不代表能平行讀取所有疊加態。

從計算[複雜度](/zh-tw/p/time-space-complexity-big-o-notation-examples/)的角度來看，Shor 演算法的執行時間屬於 **量子多項式時間** ，具體如下所示：
$$ O((\log n)^3) $$

```mermaid
graph LR
  A["古典演算法 (GNFS)"] -->|"極限"| B["次指數時間 L_n[1/3]"]
  C["量子演算法 (Shor)"] -->|"突破"| D["多項式時間 O((log n)^3)"]
  B --> E["持續使用 RSA 密碼 (增加金鑰長度)"]
  D --> F["若出現能力足夠的容錯量子電腦，RSA 將面臨風險"]
```

### 5.2 古典次指數時間 vs 量子多項式時間

Shor 在理想化量子模型中可於多項式時間分解整數，但這本身無法提供容錯設備的實際成本。Gidney 與 Ekerå 於 2021 年在特定假設下估計約需 2,000 萬個物理量子位元及 8 小時；Gidney 於 2025 年針對另一種設計與假設估計少於 100 萬個具雜訊的物理量子位元、少於一週。這些都是有條件的估算，並非破解 RSA-2048 的展示；目前尚無量子電腦分解過如此規模的整數。單靠 $2048^3$ 無法推得閘數或執行時間。[2021 年估算](https://doi.org/10.22331/q-2021-04-15-433) · [2025 年估算](https://arxiv.org/abs/2505.15917)

GNFS 漸近公式也無法直接換算為運算次數或時間；這需要明確的成本模型與參數。
## 6. 總結：對次世代的展望

GNFS 是已知最佳通用方法，但不是已證明的極限。實務改良無法保證所需時間，也不能據此斷言 RSA 未來數十年安全。Shor 資源估算有條件限制，並不代表現有設備的能力。後量子密碼遷移應遵循適用標準與官方指引。
