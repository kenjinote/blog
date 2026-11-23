---
title: '是否存在超越GNFS（普通数域筛选法）的算法？'
slug: "beyond-gnfs-integer-factorization-algorithms"
date: "2026-09-11T09:00:00+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["mathematics", "cryptography"]
tags: ["GNFS", "Integer Factorization", "RSA", "Algorithms"]
---

## 1. 引言：整数分解与现代密码学的根基

RSA 是多种公钥密码系统之一，其安全性部分基于大整数难以分解这一假设。但互联网整体安全并非只依赖 RSA。高效的分解算法会威胁使用 RSA 的场景，却不会自动导致所有通信基础设施崩溃。

对于一般的大整数分解，GNFS 是最知名的经典方法之一。它曾用于分解 RSA-768、RSA-250 等整数；具有特殊结构的整数可能更适合 SNFS 等方法。[RSA-250 报告](https://eprint.iacr.org/2020/697)

然而，密码学家和数学家们始终抱有如下疑问：“是否存在超越GNFS的经典算法？”“经典计算机的极限在哪里？”以及，“量子计算机将如何打破这一僵局？”

本文将深入剖析GNFS背后的深邃数学结构，并对多项式选择、筛选处理、以及利用Block Wiedemann方法的线性代数步骤等进行详细的技术分析。此外，还将探讨通过Coppersmith改进等方法对GNFS进行扩展的技术，并从数学角度比较和解释经典次指数时间（Sub-exponential time）算法与量子多项式时间算法之间的决定性差异。

---

## 2. 渐进复杂度与L记号（L-notation）

在评估整数分解算法的计算[复杂度](/zh-cn/p/time-space-complexity-big-o-notation-examples/)时，标准的多项式时间表示（如 $O(n^k)$ 等）不再适用，为了表示相对于输入 $n$ 的位数的次指数时间，我们使用 **L记号（L-notation）** 。L记号的定义如下：

$$
L_n[\alpha, c] = \exp \left( (c + o(1)) (\ln n)^\alpha (\ln \ln n)^{1-\alpha} \right)
$$

在这里，$n$ 是待分解的整数，$\ln n$ 是自然对数，与 $n$ 的位长成正比。
- 当 $\alpha = 0$ 时：$L_n[0, c] = \exp(c \ln \ln n) = (\ln n)^c$，表示相对于位长的 **多项式时间（Polynomial time）** 。
- 当 $\alpha = 1$ 时：$L_n[1, c] = \exp(c \ln n) = n^c$，表示相对于位长的 **指数时间（Exponential time）** 。
- 当 $0 < \alpha < 1$ 时：介于多项式时间和指数时间之间，称为 **次指数时间（Sub-exponential time）** 。

过去整数分解算法的进化史，同时也是这个 $\alpha$ 值逐渐减小的历史。
- **CFRAC**：启发式期望运行时间为 $L_n[1/2,\sqrt{2}]$（[参考资料](https://cacr.uwaterloo.ca/hac/about/chap3.pdf)）。
- **MPQS/QS**：启发式期望运行时间为 $L_n[1/2,1]$（[FLINT 文档](https://flintlib.org/doc/algorithms/number-theory/quadratic-sieve.html)）。
- **GNFS**：通常的启发式估算为 $L_n[1/3,(64/9)^{1/3}]$；这不是已证明的下界，也不是直接的实际运行时间（[NFS 分析](https://arxiv.org/abs/2007.02730)）。

---

## 3. GNFS（普通数域筛选法）算法全貌与数学结构

GNFS拥有非常复杂且高级的数学基础。其基本思想是[费马小定理](https://kenji.blog/zh-cn/p/fermats-little-theorem/)和二次筛选法（QS）的延伸，即寻找满足同余式 $X^2 \equiv Y^2 \pmod n$ 且 $X \not\equiv \pm Y \pmod n$ 的非平凡组合 $(X, Y)$，从而推导出 $n$ 的因子 $\gcd(X-Y, n)$。

然而，GNFS的精髓在于，它不仅仅在有理数域 $\mathbb{Q}$ 中进行计算，而是同时在称为代数数域（Algebraic Number Field）的扩域 $\mathbb{Q}(\alpha)$ 和有理数域中寻找“光滑数（Smooth numbers）”，并通过同态映射构建同余关系。

GNFS的过程大致分为5个阶段。

```mermaid
graph TD
  A["素数分解问题 (输入 n)"] --> B["1. 多项式选择 (Polynomial Selection)"]
  B --> C["2. 筛选处理 (Sieving Phase)"]
  C --> D["3. 过滤处理 (Filtering Phase)"]
  D --> E["4. 线性代数 (Linear Algebra Phase)"]
  E --> F["5. 平方根阶段 (Square Root Phase)"]
  F --> G["输出素因子 p, q"]```

### 3.1 阶段1：多项式选择 (Polynomial Selection)

GNFS的成功在很大程度上取决于如何选择合适的多项式。目标是找到具有公共根 $m$ 的两个不可约多项式 $f_1(x)$（有理侧）和 $f_2(x)$（代数侧）。也就是说，满足：
$f_1(m) \equiv f_2(m) \equiv 0 \pmod n$

通常，有理侧的多项式选择一次方程 $f_1(x) = x - m$，而代数侧的多项式 $f_2(x)$ 选择一个次数为 $d$（通常为5或6）的首一多项式。最经典的方法是 **Base-$m$ 方法** 。
选择一个接近 $n$ 的 $1/(d+1)$ 次方的整数 $m = \lfloor n^{1/(d+1)} \rfloor$，并将 $n$ 展开为 $m$ 进制形式：
$n = c_d m^d + c_{d-1} m^{d-1} + \dots + c_1 m + c_0$
由此可以得到多项式 $f_2(x) = c_d x^d + c_{d-1} x^{d-1} + \dots + c_0$。显然 $f_2(m) = n \equiv 0 \pmod n$。

但是在现代实现中，使用的是 **Kleinjung算法** 。这是一种在避免多项式系数过大（优化偏度，Skewness）的同时，优化代数性质（Murphy's $E$ value 或 $\alpha$-value），寻找能在筛选阶段更容易生成光滑数的多项式的算法。仅仅是这一步骤就会投入大量的计算资源。

### 3.2 阶段2：筛选处理 (Sieving Phase)

多项式确定后，算法进入计算负载最高的“筛选（Sieving）”阶段。在这里，我们需要寻找数据对 $(a, b)$。这个数据对必须是互素的，并且要求以下两个值同时为“光滑（Smooth）”：

1. **有理侧的范数**: $F_1(a, b) = b \cdot f_1(a/b) = a - bm$
2. **代数侧的范数**: $F_2(a, b) = b^d \cdot f_2(a/b)$

在基本定义中，光滑数的素因子均不超过选定的筛选上限。部分实际变体也允许额外的大素因子，因此关系式的接受条件取决于具体实现。
目前的主流方法被称为 **格筛选（Lattice Sieving）** 。通过固定某个特定的素数 $q$，仅对使有理侧和代数侧同时为 $q$ 的倍数的子格上的 $(a, b)$ 对进行筛选，从而实现了极高的效率。

### 3.3 阶段3：过滤处理 (Filtering Phase)

在筛选阶段找到的光滑关系式（Relations）数量将高达数亿甚至数十亿。但其中也包含了大量无用的信息。
过滤的目的是在构建巨大的稀疏矩阵（Sparse Matrix）的同时，尽可能地缩小其维度。

具体进行如下操作：
- **Singleton removal（单例移除）**: 删除包含只出现过一次的素因子的关系式。
- **Clique removal / Merging（团移除/合并）**: 将包含出现两次以上素因子的关系式相互相乘，消去变量，将其压缩为密度更高但维度更小的方程组。

通过这一过程，数十亿行的矩阵被压缩为数千万行级别的巨大稀疏矩阵 $\mathbf{A}$（元素为域 $\mathbb{F}_2$ 上的0和1）。

### 3.4 阶段4：线性代数 (Linear Algebra Phase)

这里要在 $\mathbb{F}_2$ 上寻找满足 $\mathbf{A}\mathbf{x}=\mathbf{0}$ 的非零向量 $\mathbf{x}$，也就是稀疏矩阵核空间中的向量。

对于稀疏矩阵，会使用 Block Lanczos、Block Wiedemann 等 Krylov 迭代方法。RSA-250 分解报告记录了 Block Wiedemann 的实际使用；方法选择与性能取决于矩阵、实现和计算架构。[RSA-250 报告](https://eprint.iacr.org/2020/697)


### 3.5 阶段5：平方根 (Square Root Phase)

利用线性代数求得的解，我们可以在有理侧和代数侧分别构造出“完全平方”的乘积。
在有理侧，$\prod (a-bm)$ 会成为某个整数 $X$ 的平方 $X^2$；在代数侧，对应的理想（Ideal）的乘积在代数数域上成为完全平方 $\gamma^2$。
在代数数域上计算出这个 $\gamma$，并通过映射到有理整数环的同态映射 $\phi: \alpha \mapsto m \pmod n$，我们可以得到同余式：
$X^2 \equiv \phi(\gamma)^2 \equiv Y^2 \pmod n$

计算代数数域上的平方根时，使用了 **Montgomery方法（Montgomery's Method）** 等复杂算法，这需要代数数论的深厚知识。最终，通过计算 $\gcd(X-Y, n)$，如果能得到非平凡的因子，因数分解即告完成。

---

## 4. 是否存在超越GNFS的经典算法？

迄今为止，对于一般整数的因数分解，尚未发现渐进[复杂度](/zh-cn/p/time-space-complexity-big-o-notation-examples/)低于 $L_n[1/3, c]$ 的经典算法。不过，为了突破理论与实践的局限，存在一些尝试与衍生算法。

### 4.1 多重数域筛选法 (MNFS: Multiple Number Field Sieve)

作为对GNFS的扩展，D. Coppersmith提出了 **多重数域筛选法（MNFS）** 。GNFS使用了两个多项式（有理侧和代数侧），而MNFS则对一个有理侧多项式同时使用多个不同的代数侧多项式。

$$ f_1(x), f_{2,1}(x), f_{2,2}(x), \dots, f_{2,V}(x) $$

通过利用多个代数数域，可以在每次筛选步骤中极大地提高“在任一代数数域中变光滑”的概率。Coppersmith通过这种方法成功地稍微减小了计算[复杂度](/zh-cn/p/time-space-complexity-big-o-notation-examples/) $L_n[1/3, c]$ 中的常数 $c$。
然而，在实际应用中，管理多个数域带来的开销很大，因此尚未在实际规模的[RSA](https://kenji.blog/zh-cn/p/modern-cryptography-public-key-hash-signature/)模数上取得决定性的突破。

### 4.2 $L_n[1/4]$ 级别的算法可能存在吗？

目前尚无渐进复杂度低于通常 GNFS 形式的一般经典整数分解算法，但这并不能证明更好的算法不可能存在。光滑数分析描述已知筛法的限制，并未证明所有算法的下界；该问题仍未解决。
---

## 5. 量子计算机的突破：Shor算法

虽然经典计算机面临着 $L_n[1/3]$ 的壁垒，但通过彻底改变计算模型本身而粉碎这一壁垒的，正是Peter Shor于1994年发表的 **Shor算法（[Shor's Algorithm](https://kenji.blog/zh-cn/p/quantum-computing-shors-algorithm/)）** 。

### 5.1 量子多项式时间的冲击

Shor算法将素数分解问题归约为“求阶问题（Order Finding Problem）”。即对于某个整数 $a$，寻找函数 $f(x) = a^x \pmod n$ 的周期（阶） $r$ 的问题。
Shor 利用量子干涉提取函数周期的信息；这并不意味着可以并行读取所有叠加态。

从计算[复杂度](/zh-cn/p/time-space-complexity-big-o-notation-examples/)的角度来看，Shor算法的执行时间属于 **量子多项式时间** ，具体如下：
$$ O((\log n)^3) $$

```mermaid
graph LR
  A["经典算法 (GNFS)"] -->|"极限"| B["次指数时间 L_n[1/3]"]
  C["量子算法 (Shor)"] -->|"突破"| D["多项式时间 O((log n)^3)"]
  B --> E["RSA密码的继续使用 (增加密钥长度)"]
  D --> F["若出现能力足够的容错量子计算机，RSA 将面临风险"]
```

### 5.2 经典次指数时间 vs 量子多项式时间

Shor 在理想化量子模型中可用多项式时间分解整数，但这本身不能给出容错设备的实际成本。Gidney 和 Ekerå 于 2021 年在特定假设下估算约需 2,000 万个物理量子比特和 8 小时；Gidney 于 2025 年针对另一种设计和假设估算少于 100 万个带噪物理量子比特、少于一周。这些是有条件的估算，并非破解 RSA-2048 的演示；目前还没有量子计算机分解过如此规模的整数。仅凭 $2048^3$ 无法推导门数或运行时间。[2021 年](https://doi.org/10.22331/q-2021-04-15-433) · [2025 年](https://arxiv.org/abs/2505.15917)

GNFS 渐进公式也不能直接换算为运算次数或时间；这需要明确的成本模型和参数。
## 6. 总结：下一代展望

GNFS 是已知最佳通用方法，但不是已证明的极限。实际改进不能保证耗时，也不能据此断言 RSA 未来几十年安全。Shor 资源估算有条件限制，并不代表现有设备的能力。后量子密码迁移应遵循适用标准和官方指导。
