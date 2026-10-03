---
title: "量子纠缠与贝尔不等式：爱因斯坦最后的败北与量子信息革命的黎明"
description: "“幽灵般的超距作用”与EPR悖论。证明局域实在论破产的贝尔不等式与阿斯佩实验，通往诺贝尔奖的轨迹。"
slug: "quantum-entanglement-bells-theorem-local-realism"
date: "2026-10-03T05:00:00+09:00"
categories: ["physics", "quantum"]
tags: ["quantum-entanglement", "bells-theorem", "quantum-information", "physics-history"]
image: "eyecatch.jpg"
---

# 量子纠缠与贝尔不等式：爱因斯坦最后的败北与量子信息革命的黎明

现代物理学中最大的谜团，同时也是最强工具的“量子纠缠（Quantum Entanglement）”。以及，打破人类直觉“局域实在论”的“贝尔不等式”。这些不仅是物理学的理论游戏，更向我们揭示了宇宙的根本性质，进而成为量子计算机和量子密码通信等下一代技术的基础。

本文将从1935年爱因斯坦等人的EPR论文开始，经历隐变量理论的苦恼、约翰·斯图尔特·贝尔推导出历史性不等式、CHSH不等式与量子力学中最大违背（Tsirelson界限）的数学证明，以及阿斯佩等人进行的实验验证，一直到2022年获得诺贝尔物理学奖的宏大戏剧，从物理学、量子信息科学、科学哲学的视角进行极其详细的解说。此外，还将结合数学公式，深入探讨利用多粒子纠缠的GHZ状态彻底否定局域实在论、量子隐形传态的严格协议、纠缠的定量化方法等。

---

## 第一章：1935年，爱因斯坦的反击

在20世纪20年代，当量子力学由哥本哈根学派（尼尔斯·玻尔和维尔纳·海森堡等人）逐渐定型时，阿尔伯特·爱因斯坦对其概率性和非决定论的解释抱有强烈的布满。“上帝不掷骰子”这句他的名言，表达了对量子力学底层概率性质的拒绝。

1935年，爱因斯坦与鲍里斯·波多尔斯基、内森·罗森共同发表了物理学史上的历史性论文《能认为量子力学对物理实在的描述是完备的吗？（Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?）》，即所谓的“EPR论文”。这篇论文的目的是逻辑性地证明量子力学是“不完备”的，也就是说，必定存在我们还未知的“隐变量”。

### 局域性与实在性的定义

为了理解EPR论文的逻辑展开，有必要准确把握爱因斯坦等人作为前提的两个根本概念。

1. **实在性（Realism）**：
   无论是否被观测，物理系统都具有确定的物理性质（值）的观点。在EPR论文中定义为“如果在不以任何方式干扰系统的情况下，能够确定地（以概率1）预测某个物理量的值，那么就存在一个对应于该物理量的物理实在的要素”。换句话说，在测量之前，对象就确定地保持着其属性，这是经典力学中理所当然的常识。
2. **局域性（Locality）**：
   在空间上分离的两个区域中，对其中一方进行的操作或测量，绝不会以超光速瞬间影响另一方区域的物理实在，这是基于相对论的原则。根据狭义相对论，超光速的信息传递会导致因果律的崩溃，因此任何物理相互作用都受光速限制。

### “幽灵般的超距作用”（Spooky action at a distance）与EPR悖论

在EPR论文中，提出了如下思想实验。
考虑两个在强烈相互作用后远远分离的粒子A和B。在量子力学框架下，这两个粒子处于“纠缠（Entangled）”状态，由整体的波函数来描述。

假设测量了粒子A的位置 $x_A$。根据动量守恒定律等，一旦A的位置确定，粒子B的位置 $x_B$ 也瞬间确定。另一方面，如果测量粒子A的动量 $p_A$，粒子B的动量 $p_B$ 就会瞬间确定。
根据量子力学，位置和动量是不可对易的物理量（$[x, p] = i\hbar$），不能同时具有确定的值（海森堡的不确定性原理）。然而，对A的测量选择（测量位置还是测量动量），似乎超光速地瞬间决定了B的状态（位置确定的状态，还是动量确定的状态）。

如果“局域性”是正确的，那么对A的测量绝不可能瞬间影响到B。爱因斯坦称其为“幽灵般的超距作用（Spukhafte Fernwirkung / Spooky action at a distance）”，并进行了强烈的批评。因此，他们得出结论，B必须在被测量之前就预先具有位置和动量都确定的值（隐变量），而未能完全描述位置和动量的量子力学是一个“不完备的理论”。这个悖论成为了后来量子信息理论中对纠缠本质理解的第一步。

---

## 第二章：隐变量理论的困境与玻姆力学

在EPR论文发表后，物理学家们开始探索一个假设：“量子力学是正确的但不完备，在更深的层次上可能存在决定论的理论（隐变量理论）”。

### 冯·诺伊曼错误的“不可能性定理”

给这场争论泼冷水的是天才数学家约翰·冯·诺伊曼。他在1932年的著作《量子力学的数学基础》中，提出了一个证明（不可能性定理），即在数学上不可能构建出与量子力学给出相同预测的“隐变量理论”。
冯·诺伊曼的权威极大，在此后几十年里，“探索隐变量是毫无意义的”这一风气支配了物理学界。

然而，正如后来所表明的那样，冯·诺伊曼的证明中包含了极具限制性且非物理的假设作为“隐变量应满足的条件”（即不可对易物理量期望值的可加性：$\langle A+B \rangle = \langle A \rangle + \langle B \rangle$ 在隐变量层面上也成立的假设），实际上并非完备的证明。格雷特·赫尔曼很早就注意到了这个缺陷，但在当时并未受到关注。

### 玻姆力学：非局域隐变量理论

1952年，戴维·玻姆打破了冯·诺伊曼的不可能性定理，构建了一个给出与量子力学完全一致预测的决定论“隐变量理论（玻姆力学，或德布罗意-玻姆理论）”。
在玻姆的理论中，粒子始终具有明确的位置（隐变量），并由遍布整个宇宙的“量子势”引导。通过将薛定谔方程转换为极坐标表示得到的这个势 $Q = -\frac{\hbar^2}{2m}\frac{\nabla^2 R}{R}$，具有不依赖距离且不衰减的奇异性质。

然而，玻姆力学付出了巨大的代价。由于量子势能瞬间影响整个空间，该理论在本质上是“非局域的”。爱因斯坦最厌恶的“幽灵般的超距作用”，被玻姆力学作为理论的根基包含在内。
爱因斯坦对玻姆的理论也采取了否定的态度，认为这是“廉价的解决方案”，并依然相信“局域”隐变量理论的存在。

---

## 第三章：自旋1/2粒子的单态与量子力学的严格预测

在进入贝尔不等式之前，让我们先使用泡利矩阵，完整地展开量子力学所预测的纠缠相关性的严格狄拉克符号（bra-ket）计算过程。这将成为后来与局域实在论发生冲突的量子力学核心。

假设产生了一对自旋1/2的粒子，并处于总自旋为零的“单态（Singlet State）”。这个状态 $|\psi^-\rangle$ 被描述如下：

$$ |\psi^-\rangle = \frac{1}{\sqrt{2}} \left( |\uparrow\rangle_A \otimes |\downarrow\rangle_B - |\downarrow\rangle_A \otimes |\uparrow\rangle_B \right) $$

这里，$|\uparrow\rangle, |\downarrow\rangle$ 分别表示自旋向上（$+1$）和向下（$-1$）的本征态（$z$基底）。有时简写为 $|\psi^-\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$。

爱丽丝在方向 $\vec{a}$，鲍勃在方向 $\vec{b}$ 测量各自粒子的自旋。方向向量是单位向量，在球坐标系中可表示为 $\vec{a} = (\sin\theta_a\cos\phi_a, \sin\theta_a\sin\phi_a, \cos\theta_a)$ 等。
各个方向的自旋测量算符，利用泡利矩阵 $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ 可得 $\sigma_a = \vec{a} \cdot \vec{\sigma}$、$\sigma_b = \vec{b} \cdot \vec{\sigma}$。

我们想知道的是，爱丽丝和鲍勃测量结果乘积的期望值 $\langle \sigma_a \otimes \sigma_b \rangle$。为了计算它，我们根据期望值的定义进行展开。

$$ \langle \psi^- | (\vec{a} \cdot \vec{\sigma}) \otimes (\vec{b} \cdot \vec{\sigma}) | \psi^- \rangle $$

首先，作为泡利矩阵的性质，考虑 $\vec{a} \cdot \vec{\sigma} = a_x \sigma_x + a_y \sigma_y + a_z \sigma_z$。作为简化计算的巧妙技巧，可以利用单态 $|\psi^-\rangle$ 具有旋转不变性（在任何基底下形式相同）。但在这里，我们将采用更直接的代数方法进行完整展开。

算符 $(\vec{a} \cdot \vec{\sigma}) \otimes (\vec{b} \cdot \vec{\sigma})$ 展开如下：
$$ \sum_{i \in \{x,y,z\}} \sum_{j \in \{x,y,z\}} a_i b_j (\sigma_i \otimes \sigma_j) $$

根据期望值的线性，
$$ \sum_{i,j} a_i b_j \langle \psi^- | \sigma_i \otimes \sigma_j | \psi^- \rangle $$
在这里，对 $\langle \psi^- | \sigma_i \otimes \sigma_j | \psi^- \rangle$ 的各个分量进行求值。

对于 $|\psi^-\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$，
- $\sigma_z \otimes \sigma_z$:
  $\sigma_z \otimes \sigma_z |01\rangle = (+1)(-1)|01\rangle = -|01\rangle$
  $\sigma_z \otimes \sigma_z |10\rangle = (-1)(+1)|10\rangle = -|10\rangle$
  因此 $\sigma_z \otimes \sigma_z |\psi^-\rangle = -|\psi^-\rangle$，期望值为 $-1$。
- $\sigma_x \otimes \sigma_x$:
  $\sigma_x \otimes \sigma_x |01\rangle = |10\rangle$
  $\sigma_x \otimes \sigma_x |10\rangle = |01\rangle$
  因此 $\sigma_x \otimes \sigma_x \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle) = \frac{1}{\sqrt{2}}(|10\rangle - |01\rangle) = -|\psi^-\rangle$，期望值为 $-1$。
- $\sigma_y \otimes \sigma_y$:
  由 $\sigma_y |0\rangle = i|1\rangle, \sigma_y |1\rangle = -i|0\rangle$ 可得，
  $\sigma_y \otimes \sigma_y |01\rangle = (i|1\rangle) \otimes (-i|0\rangle) = |10\rangle$
  $\sigma_y \otimes \sigma_y |10\rangle = (-i|0\rangle) \otimes (i|1\rangle) = |01\rangle$
  因此 $\sigma_y \otimes \sigma_y |\psi^-\rangle = -|\psi^-\rangle$，期望值为 $-1$。

另一方面，不同分量（例如：$\sigma_x \otimes \sigma_y$）的期望值全为 $0$。
因为 $\sigma_x \otimes \sigma_y |01\rangle = |1\rangle \otimes (-i|0\rangle) = -i|10\rangle$ 等，与 $\langle \psi^-|$ 取内积时，因正交性而抵消。

因此，非零项仅在 $i=j$ 的情况下存在，
$$ \sum_{i} a_i b_i \langle \psi^- | \sigma_i \otimes \sigma_i | \psi^- \rangle = \sum_{i} a_i b_i (-1) = - (a_x b_x + a_y b_y + a_z b_z) = - \vec{a} \cdot \vec{b} $$
得以严格推导。
如果向量 $\vec{a}$ 和 $\vec{b}$ 的夹角为 $\theta$，根据内积定义 $\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta = \cos\theta$（方向向量为单位向量，长度为1）。
故而，量子力学预测的相关性变成极其优美且简单的如下公式：

$$ E(\vec{a}, \vec{b}) = \langle \sigma_a \otimes \sigma_b \rangle = - \cos\theta $$

这个 $-\cos\theta$ 的强大关联，正是经典隐变量理论绝对无法重现的“量子特有行为”的源泉。


---

## 第四章：约翰·斯图尔特·贝尔的冲击与CHSH不等式的严格推导

1964年，在CERN从事粒子物理学研究的爱尔兰物理学家约翰·斯图尔特·贝尔，利用业余时间研究量子力学的基础问题。基于玻姆力学的非局域性，他产生了这样一个深邃的疑问：

“到底是否可能用爱因斯坦所期望的‘局域’隐变量理论，来重现量子力学的所有预测呢？”

贝尔将这个不过是哲学争论的问题，通过严格的数学形式化，升华为可以在实验上验证的形式。这便是科学史上闪耀的“贝尔定理（Bell's Theorem）”和“贝尔不等式”。
并且在1969年，约翰·克劳泽、迈克尔·霍恩、阿伯纳·西蒙尼和理查德·霍尔特四人（CHSH）推导出了能够在现实实验中验证的扩展版不等式——“CHSH不等式”。

### 局域实在论的假设与CHSH不等式的积分及代数展开

假设爱丽丝选择测量仪器设置为 $a$ 或 $a'$，鲍勃选择 $b$ 或 $b'$。
设基于局域实在论的“隐变量”为 $\lambda$，其概率密度函数为 $\rho(\lambda)$。由于概率归一化，
$$ \int \rho(\lambda) d\lambda = 1 $$

爱丽丝的测量结果 $A$，仅由她的测量方向 $a$ 和 $\lambda$ 决定，不依赖鲍勃的测量方向 $b$（局域性）。
同样，鲍勃的测量结果 $B$，仅由 $b$ 和 $\lambda$ 决定（局域性）。并且在测量前结果就已经确定（实在论）。因为结果是 $+1$ 或 $-1$，所以
$$ A(a, \lambda) = \pm 1, \quad B(b, \lambda) = \pm 1 $$
$$ A(a', \lambda) = \pm 1, \quad B(b', \lambda) = \pm 1 $$

爱丽丝和鲍勃测量结果的相关函数（期望值），可以通过对隐变量 $\lambda$ 积分获得。
$$ E(a, b) = \int A(a, \lambda) B(b, \lambda) \rho(\lambda) d\lambda $$

这里，我们考虑CHSH不等式核心的以下量 $S(\lambda)$。
$$ S(\lambda) = A(a, \lambda)B(b, \lambda) + A(a, \lambda)B(b', \lambda) + A(a', \lambda)B(b, \lambda) - A(a', \lambda)B(b', \lambda) $$

将该式对爱丽丝的测量结果进行因式分解（提取公因式）。
$$ S(\lambda) = A(a, \lambda) \left[ B(b, \lambda) + B(b', \lambda) \right] + A(a', \lambda) \left[ B(b, \lambda) - B(b', \lambda) \right] $$

在这里进入了一个极其重要的逻辑步骤。$B(b, \lambda)$ 和 $B(b', \lambda)$ 的取值必然是 $+1$ 或 $-1$。
因此，考虑它们的和与差，只存在以下两种情况。

- 情况1：当 $B(b, \lambda) = B(b', \lambda)$ 时
  和为 $B(b, \lambda) + B(b', \lambda) = \pm 2$，差为 $B(b, \lambda) - B(b', \lambda) = 0$。
- 情况2：当 $B(b, \lambda) = -B(b', \lambda)$ 时
  和为 $B(b, \lambda) + B(b', \lambda) = 0$，差为 $B(b, \lambda) - B(b', \lambda) = \pm 2$。

在任何一种情况中，两个方括号 $\left[ \dots \right]$ 中的一个必然是 $\pm 2$，而另一个必然是 $0$。
而且，乘在那存留下来的 $\pm 2$ 上的 $A(a, \lambda)$ 或 $A(a', \lambda)$ 也是 $\pm 1$。
因此，对于任何隐变量 $\lambda$ 的值，在代数上必然成立：
$$ S(\lambda) = \pm 2 $$

即取绝对值后，
$$ |S(\lambda)| = 2 $$

为了求得这个 $S(\lambda)$ 的期望值 $S$，乘以概率分布 $\rho(\lambda)$ 并在全空间积分。
$$ |S| = \left| \int S(\lambda) \rho(\lambda) d\lambda \right| \le \int |S(\lambda)| \rho(\lambda) d\lambda $$
利用 $|S(\lambda)| = 2$ 以及 $\int \rho(\lambda) d\lambda = 1$，
$$ |S| \le \int 2 \rho(\lambda) d\lambda = 2 $$

这个期望值 $S$ 可以展开为各个相关函数的和与差。
$$ S = E(a, b) + E(a, b') + E(a', b) - E(a', b') $$

由此，导出了以下的“CHSH不等式”。
$$ |E(a, b) + E(a, b') + E(a', b) - E(a', b')| \le 2 $$

如果宇宙遵循“局域实在论”，这就是**绝对无法超越的极限值**。

### 量子力学的最大违背（Tsirelson界限）

请回想第三章推导的量子力学预测 $E(\vec{a}, \vec{b}) = -\cos\theta$。
假设爱丽丝和鲍勃将测量仪器设定为以下角度。
- $a = 0$
- $a' = \pi/2$
- $b = \pi/4$
- $b' = -\pi/4$

（※需要注意的是，当使用光子的偏振时，系数与自旋1/2不同，为 $E = \cos(2\theta)$，但用上述使用自旋的设定进行计算本质是相同的）
各个设定之间的角度差为：
$|a - b| = \pi/4$
$|a - b'| = \pi/4$
$|a' - b| = \pi/4$
$|a' - b'| = 3\pi/4$

代入量子力学的预测中，
$E(a, b) = -\cos(\pi/4) = -1/\sqrt{2}$
$E(a, b') = -\cos(\pi/4) = -1/\sqrt{2}$
$E(a', b) = -\cos(\pi/4) = -1/\sqrt{2}$
$E(a', b') = -\cos(3\pi/4) = +1/\sqrt{2}$

将这些代入CHSH不等式的左边 $S$ 中，
$$ S = \left( -\frac{1}{\sqrt{2}} \right) + \left( -\frac{1}{\sqrt{2}} \right) + \left( -\frac{1}{\sqrt{2}} \right) - \left( +\frac{1}{\sqrt{2}} \right) = -\frac{4}{\sqrt{2}} = -2\sqrt{2} $$
取绝对值则为 $|S| = 2\sqrt{2} \approx 2.828$。

这明显超过了局域实在论的极限 $2$（$2.828 > 2$）。这个由量子力学能够达到的最大值被称为**Tsirelson界限（Tsirelson Bound）**。严格的数学证明显示，局域实在论与量子力学的预测绝对是不相容的。

---

## 第五章：多粒子纠缠与局域实在论的“一击”否定（All-or-Nothing）

贝尔定理基于统计相关的“不等式”。然而在1989年，丹尼尔·格林伯格、迈克尔·霍恩和安东·蔡林格三人指出，如果考虑三个粒子纠缠的状态（GHZ态），无需依赖不等式或统计概率，仅靠一次测量结果的矛盾就能彻底驳倒局域实在论。这被称为“All-or-Nothing证明”或“GHZ定理”。

### GHZ态的性质
3个自旋1/2粒子的GHZ态定义如下：
$$ |GHZ\rangle = \frac{1}{\sqrt{2}} \left( |\uparrow\uparrow\uparrow\rangle - |\downarrow\downarrow\downarrow\rangle \right) $$

在此之上，作用如下泡利算符的乘积：
1. $X_1 Y_2 Y_3 = \sigma_x^{(1)} \otimes \sigma_y^{(2)} \otimes \sigma_y^{(3)}$
2. $Y_1 X_2 Y_3 = \sigma_y^{(1)} \otimes \sigma_x^{(2)} \otimes \sigma_y^{(3)}$
3. $Y_1 Y_2 X_3 = \sigma_y^{(1)} \otimes \sigma_y^{(2)} \otimes \sigma_x^{(3)}$
4. $X_1 X_2 X_3 = \sigma_x^{(1)} \otimes \sigma_x^{(2)} \otimes \sigma_x^{(3)}$

使用
$\sigma_x |\uparrow\rangle = |\downarrow\rangle, \sigma_x |\downarrow\rangle = |\uparrow\rangle$
$\sigma_y |\uparrow\rangle = i|\downarrow\rangle, \sigma_y |\downarrow\rangle = -i|\uparrow\rangle$
将 $X_1 Y_2 Y_3$ 作用于 $|GHZ\rangle$，
$X_1 Y_2 Y_3 |\uparrow\uparrow\uparrow\rangle = |\downarrow\rangle (i|\downarrow\rangle) (i|\downarrow\rangle) = -|\downarrow\downarrow\downarrow\rangle$
$X_1 Y_2 Y_3 |\downarrow\downarrow\downarrow\rangle = |\uparrow\rangle (-i|\uparrow\rangle) (-i|\uparrow\rangle) = -|\uparrow\uparrow\uparrow\rangle$
因此，
$X_1 Y_2 Y_3 |GHZ\rangle = \frac{1}{\sqrt{2}} (-|\downarrow\downarrow\downarrow\rangle + |\uparrow\uparrow\uparrow\rangle) = |GHZ\rangle$
本征值为 $+1$。根据对称性，$Y_1 X_2 Y_3$、$Y_1 Y_2 X_3$ 的本征值同样也为 $+1$。

另一方面，将 $X_1 X_2 X_3$ 作用于其上，
$X_1 X_2 X_3 |\uparrow\uparrow\uparrow\rangle = |\downarrow\downarrow\downarrow\rangle$
$X_1 X_2 X_3 |\downarrow\downarrow\downarrow\rangle = |\uparrow\uparrow\uparrow\rangle$
因此，
$X_1 X_2 X_3 |GHZ\rangle = \frac{1}{\sqrt{2}} (|\downarrow\downarrow\downarrow\rangle - |\uparrow\uparrow\uparrow\rangle) = -|GHZ\rangle$
本征值为 $-1$。量子力学确切地（以概率1）预测了以上结果。

### 局域实在论破产的代数证明
在局域实在论中，认为测量结果是由预先决定的隐变量决定的。
设粒子1的X方向、Y方向测量结果分别为 $m_x^1, m_y^1 \in \{+1, -1\}$。同样地也定义粒子2、3。
为了必须符合量子力学 $+1$ 的预测，局域实在论的模型需要满足以下3个方程：
1. $m_x^1 m_y^2 m_y^3 = +1$
2. $m_y^1 m_x^2 m_y^3 = +1$
3. $m_y^1 m_y^2 m_x^3 = +1$

将这3个方程全部相乘。
$(m_x^1 m_y^2 m_y^3)(m_y^1 m_x^2 m_y^3)(m_y^1 m_y^2 m_x^3) = +1 \times +1 \times +1 = +1$
整理左边，因为每个 $m_y^i$ 都被乘了两次，所以 $(m_y^i)^2 = 1$。
$m_x^1 m_x^2 m_x^3 (m_y^1)^2 (m_y^2)^2 (m_y^3)^2 = m_x^1 m_x^2 m_x^3 = +1$

也就是说，只要遵循局域实在论，$X_1 X_2 X_3$ 的测量结果必须总是 $+1$。
然而，正如我们刚才看到的，量子力学的严格预测（以及实际的实验结果）是 $-1$。
$+1$ 与 $-1$。连统计不等式都不需要，在单次测量中，局域实在论与量子力学发生决定性的矛盾，量子力学的正确性得到了证明。

（※顺便一提，对于3粒子纠缠，还有具有与GHZ态不同性质的W态 $|W\rangle = \frac{1}{\sqrt{3}}(|100\rangle + |010\rangle + |001\rangle)$，它具有即使失去一个粒子纠缠也不会完全被破坏的鲁棒性。）


---

## 第六章：量子信息科学的应用与量子隐形传态的严格展开

纠缠已经从悖论的对象转变为“信息资源”。其代表性例子就是“量子隐形传态（Quantum Teleportation）”。这在1993年由查尔斯·本内特等人提出，并在1997年由安东·蔡林格（2022年诺贝尔奖得主）的团队首次在实验中得到了证实。

### 量子隐形传态协议的数学展开

假设爱丽丝拥有未知的量子态 $|\phi\rangle = \alpha|0\rangle + \beta|1\rangle$，并想把它传送给远处的鲍勃。($|\alpha|^2 + |\beta|^2 = 1$)
根据量子不可克隆定理（No-cloning theorem），无法复制这个状态进行发送。而且，如果对其进行测量，状态就会坍缩，无法准确知道未知的 $\alpha, \beta$。

于是，爱丽丝和鲍勃预先共享一对纠缠粒子（EPR对），具体来说是以下贝尔态 $|\Phi^+\rangle$：
$$ |\Phi^+\rangle_{AB} = \frac{1}{\sqrt{2}}(|0\rangle_A |0\rangle_B + |1\rangle_A |1\rangle_B) $$

爱丽丝手里有想传送的粒子（设为粒子C）和EPR对的一半（粒子A）。鲍勃手里有EPR对的另一半（粒子B）。整个系统的初始状态为：
$$ |\psi_{total}\rangle = |\phi\rangle_C \otimes |\Phi^+\rangle_{AB} = (\alpha|0\rangle_C + \beta|1\rangle_C) \otimes \frac{1}{\sqrt{2}}(|0\rangle_A |0\rangle_B + |1\rangle_A |1\rangle_B) $$
展开后得：
$$ \frac{1}{\sqrt{2}} \left( \alpha|000\rangle + \alpha|011\rangle + \beta|100\rangle + \beta|111\rangle \right) $$
（※下标顺序为 $C, A, B$）

在这里爱丽丝对她手里的粒子C和粒子A进行“贝尔测量（Bell measurement）”。这是将两个粒子投影到以下4个贝尔态基底上的测量。
$|\Phi^\pm\rangle_{CA} = \frac{1}{\sqrt{2}}(|00\rangle \pm |11\rangle)$
$|\Psi^\pm\rangle_{CA} = \frac{1}{\sqrt{2}}(|01\rangle \pm |10\rangle)$

使用这些逆向推导出 $|00\rangle, |01\rangle, |10\rangle, |11\rangle$，再用贝尔基底 $|\cdot\rangle_{CA}$ 重新合并整个系统状态，令人惊讶的是可以变形如下：
$$ |\psi_{total}\rangle = \frac{1}{2} \left[ |\Phi^+\rangle_{CA}(\alpha|0\rangle_B + \beta|1\rangle_B) + |\Phi^-\rangle_{CA}(\alpha|0\rangle_B - \beta|1\rangle_B) + |\Psi^+\rangle_{CA}(\alpha|1\rangle_B + \beta|0\rangle_B) + |\Psi^-\rangle_{CA}(\alpha|1\rangle_B - \beta|0\rangle_B) \right] $$

爱丽丝进行贝尔测量时，系统会以1/4的概率坍缩到这4个项中的某一个。
1. 如果爱丽丝得到 $|\Phi^+\rangle$，鲍勃的状态变为 $\alpha|0\rangle + \beta|1\rangle = |\phi\rangle$，传送已经完成（幺正运算 $I$）。
2. 如果得到 $|\Phi^-\rangle$，鲍勃的状态变为 $\alpha|0\rangle - \beta|1\rangle$。鲍勃应用泡利 $Z$ 算符（$\sigma_z$）即可恢复为 $|\phi\rangle$。
3. 如果得到 $|\Psi^+\rangle$，鲍勃的状态变为 $\alpha|1\rangle + \beta|0\rangle$。鲍勃应用泡利 $X$ 算符（$\sigma_x$）即可恢复为 $|\phi\rangle$。
4. 如果得到 $|\Psi^-\rangle$，鲍勃的状态变为 $\alpha|1\rangle - \beta|0\rangle$。鲍勃先应用 $Z$ 再应用 $X$（即 $XZ$ 或 $i\sigma_y$），即可恢复为 $|\phi\rangle$。

爱丽丝将测量结果（2比特经典信息：00, 01, 10, 11）通过普通通信（电话或互联网）传达给鲍勃。这种通信不超过光速，因此不违反相对论。鲍勃根据接收到的2比特应用适当的泡利算符，漂亮地恢复出未知的量子态 $|\phi\rangle$。
这就是量子隐形传态的完整协议。

---

## 第七章：纠缠的定量化（Quantification）

纠缠不仅是“有”或“无”，还可以对“纠缠有多强”进行定量化。在量子信息理论中，这是极其重要的研究课题。

### 1. 冯·诺伊曼纠缠熵
衡量纯态下两体系统 $AB$ 纠缠程度的标准尺度是冯·诺伊曼熵。设整个系统的密度矩阵为 $\rho_{AB} = |\psi\rangle\langle\psi|$，将系统B求偏迹（约化）求出系统A的约化密度矩阵 $\rho_A = \text{Tr}_B(\rho_{AB})$。
此时，纠缠熵 $S$ 定义如下：
$$ S(\rho_A) = -\text{Tr}(\rho_A \log_2 \rho_A) $$
在贝尔态等最大纠缠态中，$\rho_A$ 会变成完全的混合态（正比于单位矩阵），$S$ 达到最大值 $1$。直观地说，它表现了纠缠的本质：“整体的状态完全已知，但只看局部（系统A）时则完全没有信息（看起来是随机的）”。

### 2. 并发度（Concurrence）
作为衡量包含混合态的二量子比特系统纠缠的尺度，威廉·沃特斯等人提出了“并发度 $C(\rho)$”。
对于密度矩阵 $\rho$，计算自旋反转状态 $\tilde{\rho} = (\sigma_y \otimes \sigma_y) \rho^* (\sigma_y \otimes \sigma_y)$（$\rho^*$ 是复共轭）。
若矩阵 $R = \sqrt{\sqrt{\rho} \tilde{\rho} \sqrt{\rho}}$ 的本征值按从大到小排列为 $\lambda_1, \lambda_2, \lambda_3, \lambda_4$，则并发度定义如下：
$$ C(\rho) = \max(0, \lambda_1 - \lambda_2 - \lambda_3 - \lambda_4) $$
$C(\rho)$ 取值从 $0$（无纠缠）到 $1$（最大纠缠），并且它具有强大的数学性质，即可以直接使用这个值来计算另一个称为“形成纠缠度（Entanglement of Formation）”的尺度。

### 3. 负值度（Negativity）
基于部分转置（Partial Transpose）概念的尺度是负值度 $\mathcal{N}(\rho)$。
对于系统 $AB$ 的密度矩阵 $\rho$，仅对系统B的基底取转置的结果记为 $\rho^{T_B}$。如果 $\rho$ 是非纠缠（可分离）状态，$\rho^{T_B}$ 的所有本征值都将非负（Peres-Horodecki的PPT判据）。
反之，如果存在负的本征值，那就是纠缠的证据。负值度使用 $\rho^{T_B}$ 的迹范数 $||\cdot||_1$ 定义如下：
$$ \mathcal{N}(\rho) = \frac{||\rho^{T_B}||_1 - 1}{2} $$
这等于负本征值绝对值的总和，由于计算简单，在研究高维系统和多体系统纠缠时是非常有用的指标。

---

## 第八章：实验验证与漏洞（Loophole）的彻底封闭

理论已经完成，应用也初见端倪。剩下的就是要在实验室中探究大自然到底遵循哪种法则。

### 阿兰·阿斯佩的切换实验（1982年）
在爱丽丝和鲍勃决定了测量仪器的角度之后，那个信息可能会以光速以下的速度传到对方那里，影响到“隐变量”，必须排除这种可能性。这被称为“局域性漏洞（Locality Loophole）”。
法国的阿兰·阿斯佩等人在光子从光源飞向测量仪器的过程中，成功使用声光偏转器以超高速随机切换测量仪器的角度设置。这样就创造出了即使是光速信号也无法传递信息的状况（空间隔离），并完美地观测到了不等式的违背。爱因斯坦的“幽灵般的超距作用”，成为了现实。

### 终极挑战：完全无漏洞实验（Loophole-free test，2015年）
在阿斯佩的实验之后，仍留下了微小的反驳余地，例如检测效率低（即假设未能测量的光子恰好携带了有利的隐变量，被称为“检测漏洞 / Fair-sampling Loophole”）。
然而在2015年，荷兰代尔夫特理工大学、奥地利维也纳大学、美国NIST等多个研究小组，成功进行了同时堵住所有主要漏洞的“无漏洞贝尔测试（Loophole-free Bell test）”。代尔夫特的实验中，通过使相距1.3公里的钻石NV色心中的电子自旋发生纠缠，完全封锁了局域性漏洞和检测漏洞，在局域实在论的棺材上钉下了最后一颗钉子。

---

## 结语：爱因斯坦的败北带来的曙光

2022年，对量子力学基础做出决定性贡献的阿兰·阿斯佩、约翰·克劳泽、安东·蔡林格三人被授予诺贝尔物理学奖。

爱因斯坦厌恶量子力学的概率性与非局域性，并为了批判它而撰写了EPR论文。但讽刺的是，正是他尖锐的批评清晰地凸显了“纠缠”这一概念，并通过贝尔这位天才，开拓了人类真正理解宇宙非局域性联系并将其作为技术加以利用的道路。

爱因斯坦的“最后败北”，绝非物理学的停滞，而是人类获得量子信息这一全新宇宙语言的伟大黎明。

---
*责任编辑：量子信息科学技术撰稿人*
*本文是一篇涵盖了从量子力学基础到最先进量子信息技术的学术解说。*
