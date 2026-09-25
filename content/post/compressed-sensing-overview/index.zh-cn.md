---
slug: compressed-sensing-overview
title: "压缩感知：为什么能够用较少的观测来恢复原始信号"
description: "连接医学影像、天文学和图像压缩的现代主题。"
categories: ["mathematics", "computer-science"]
tags: ["math", "signal-processing", "algorithm", "science"]
date: "2026-09-25T11:25:00+09:00"
image: eyecatch.jpg
---

# 什么是压缩感知（Compressed Sensing）？

在现代数据科学和信号处理中，最具革命性的范式转变之一就是“压缩感知（Compressed Sensing / Compressive Sensing）”。传统上，在将音频、图像或电磁波等模拟信号作为数字数据输入计算机时，我们一直遵循“奈奎斯特-香农采样定理（Nyquist-Shannon sampling theorem）”这一绝对法则。然而，压缩感知颠覆了这一常识，它给出了一个惊人的数学保证：“只要信号满足特定条件（稀疏性），就可以从比采样定理要求的少得多的观测数据中完美恢复原始信号”。

本文将从采样定理的基础讲起，深入探讨稀疏性的数学定义、向$L_1$优化问题的松弛，以及结合数学公式详细讲解由Emmanuel Candès和Terence Tao等人带来的理论突破的核心。此外，本文还将涵盖加速MRI扫描和构建黑洞图像等应用案例，以及使用Python的具体实现代码，全面揭示压缩感知的全貌。

## 1. 奈奎斯特-香农采样定理及其局限性

### 采样定理的基础
20世纪中叶，由克劳德·香农（Claude Shannon）和哈里·奈奎斯特（Harry Nyquist）建立的信息论基础中包含“采样定理”。该定理对将连续的模拟信号转换为离散的数字信号时的条件做出了如下规定：

> **奈奎斯特-香农采样定理**
> 为了完美重建带宽被限制在 $f_{\max}$ 的信号，必须以至少 $2f_{\max}$ 的采样频率（奈奎斯特率）对信号进行采样。

例如，人耳能听到的最高频率约为 20 kHz。因此，音乐CD中的采样频率被设定为其两倍以上的 44.1 kHz。用数学公式表示，如果连续信号 $x(t)$ 具有傅里叶变换 $X(f)$，并且在 $|f| > f_{\max}$ 时 $X(f) = 0$，那么可以使用以下基于sinc函数（sinc function）的插值公式完全恢复 $x(t)$：

$$ x(t) = \sum_{n=-\infty}^{\infty} x\left(\frac{n}{2f_{\max}}\right) \operatorname{sinc}\left(2f_{\max}t - n\right) $$

### 数据爆炸与定理的局限性
采样定理非常强大，是现代数字通信的基石。然而，随着技术的进步，传感器捕捉到的信息量呈爆炸式增长。在高分辨率医学影像（如MRI和CT）、射电望远镜阵列、超宽带雷达系统等应用中，如果按照奈奎斯特率进行采样，需要观测的数据量将变得极其庞大。

结果就是会产生以下问题：
1. **扫描时间增加**: 例如在MRI中，收集数据需要很长时间，给患者带来沉重的身体负担。
2. **硬件限制**: 制造用于采样超高频信号的A/D转换器在技术上非常困难，或者成本极其高昂。
3. **数据存储和通信压力**: 存储和传输大量采样数据所需的成本飙升。

传统的范式是“大量采样，然后通过软件压缩（如JPEG或MP3）丢弃不需要的数据”。然而，我们会产生一个疑问：“既然最终都要丢弃，难道不能从一开始就直接感知（获取）所需的信息吗？” 压缩感知正是使这成为可能的技术。

## 2. 稀疏性（Sparsity）的数学定义

压缩感知成立的绝对条件是**稀疏性（Sparsity）**。稀疏性是指，“当在某个合适的基（表示方法）下变换信号时，其几乎所有的分量都变为零（或非常接近于零）”的性质。

### 稀疏向量的数学表达
考虑一个长度为 $N$ 的离散信号（向量） $\mathbf{x} \in \mathbb{R}^N$。假设该信号可以使用某个正交基矩阵 $\mathbf{\Psi} \in \mathbb{R}^{N \times N}$（例如，傅里叶变换矩阵或小波变换矩阵）表示如下：

$$ \mathbf{x} = \mathbf{\Psi} \mathbf{s} $$

这里，$\mathbf{s} \in \mathbb{R}^N$ 是在基 $\mathbf{\Psi}$ 上的系数向量。
如果这个向量 $\mathbf{s}$ 中有 $K$ 个非零元素（$K \ll N$），我们就称 $\mathbf{x}$ 是 **$K$-稀疏（$K$-sparse）** 的。在数学上，使用 $L_0$ 范数（计算非零元素个数的函数）定义如下：

$$ \|\mathbf{s}\|_0 = K $$

### 现实世界中的稀疏性
令人惊讶的是，自然界中存在的许多信号，只要选择合适的基，就会变得稀疏。
- **图像**: 自然图像在像素空间中并不稀疏，但在进行小波变换或离散余弦变换（DCT）后，大部分高频成分趋于零，从而变得稀疏（这也是JPEG压缩的原理）。
- **音频**: 音频信号在时间域上是连续的，但在频率域（傅里叶变换后）中，只有少数主要频率成分（基频和泛音）具有较大的值。

压缩感知利用这种“信号内在的冗余性”，在采样阶段同时完成数据压缩的技术。

## 3. 压缩感知的数学表述与观测矩阵

在信号稀疏的前提下，如何从少量数据中恢复信号呢？
假设对未知信号 $\mathbf{x} \in \mathbb{R}^N$ 进行 $M$ 次线性观测（$M < N$）。观测过程可以使用观测矩阵 $\mathbf{\Phi} \in \mathbb{R}^{M \times N}$ 表示如下：

$$ \mathbf{y} = \mathbf{\Phi} \mathbf{x} = \mathbf{\Phi} \mathbf{\Psi} \mathbf{s} = \mathbf{A} \mathbf{s} $$

其中：
- $\mathbf{y} \in \mathbb{R}^M$: 观测数据向量
- $\mathbf{A} = \mathbf{\Phi} \mathbf{\Psi} \in \mathbb{R}^{M \times N}$: 感知矩阵

我们的目标是，根据给定的观测数据 $\mathbf{y}$ 和矩阵 $\mathbf{A}$，恢复未知的系数向量 $\mathbf{s}$（最终恢复 $\mathbf{x}$）。

### 欠定系统问题
然而，这里我们面临一个数学壁垒。因为 $M < N$（未知数的数量多于方程的数量），这个联立方程 $\mathbf{y} = \mathbf{A} \mathbf{s}$ 成为一个**欠定系统（underdetermined system）**，具有无数个解。在常规线性代数中是不可能求出唯一解的。

这时，我们利用“$\mathbf{s}$ 是稀疏的（非零成分极少）”这一先验知识。在无数个候选解中，寻找最稀疏（非零成分最少）的解，那它很可能就是真实的信号。将其表达为优化问题如下：

$$ (P_0) \quad \min_{\mathbf{s} \in \mathbb{R}^N} \|\mathbf{s}\|_0 \quad \text{subject to} \quad \mathbf{y} = \mathbf{A} \mathbf{s} $$

### $L_0$ 优化的困难性
理想情况下，只要解上述的 $(P_0)$ 问题即可，但在数学上，最小化 $\|\mathbf{s}\|_0$ 的问题被认为是 **NP困难（NP-hard）** 的。这需要穷举搜索非零成分的所有组合，当维度 $N$ 增大时，即使使用现代超级计算机，所花费的时间也会超过宇宙的寿命。

## 4. 向 $L_1$ 优化问题的松弛：Candès和Tao的突破

压缩感知之所以作为实用技术得到爆炸性普及，是因为研究表明：如果将这个无法求解的 $L_0$ 优化问题替换为可计算的 **$L_1$ 优化问题**，在一定条件下，能够**得到完全相同的结果**。这个惊人的数学证明为其奠定了基础。

2004年至2006年期间，Emmanuel Candès、Terence Tao和David Donoho等人为该理论奠定了坚实的基础。

### $L_1$ 范数最小化
我们使用向量各个元素绝对值之和的 $L_1$ 范数来代替 $L_0$ 范数。

$$ \|\mathbf{s}\|_1 = \sum_{i=1}^N |s_i| $$

由此，问题被松弛（relaxation）为如下形式：

$$ (P_1) \quad \min_{\mathbf{s} \in \mathbb{R}^N} \|\mathbf{s}\|_1 \quad \text{subject to} \quad \mathbf{y} = \mathbf{A} \mathbf{s} $$

$L_1$ 最小化问题是凸优化问题的一种，可以使用线性规划（Linear Programming）等现有的高效算法在多项式时间内计算出精确解。

### 为什么是 $L_1$？（几何直觉）
为什么不是 $L_2$ 范数（最小二乘法）而是 $L_1$ 范数呢？这可以从几何学上理解。
约束条件 $\mathbf{y} = \mathbf{A}\mathbf{s}$ 在高维空间中形成一个超平面。最小化范数相当于以原点为中心膨胀一个等高面（球），并寻找最先与该超平面相切的点。

- **$L_2$ 球（$\|\mathbf{s}\|_2 \le R$）**: 形状是一个光滑的球体。与超平面相切的点，绝大多数情况下会远离所有坐标轴，其结果是一个所有元素非零的“密集（dense）”向量。
- **$L_1$ 球（$\|\mathbf{s}\|_1 \le R$）**: 形状是一个多面体（菱形、八面体等），具有许多“角（顶点）”。这些角位于坐标轴上。当超平面与其接触时，有很高的概率会在这些“角”的部分相切。在角处相切意味着其他坐标轴的值为零，从而得到一个稀疏的解。

### RIP（约束等距性，Restricted Isometry Property）
Candès和Tao引入了 **RIP（约束等距性）** 概念，作为 $L_1$ 最小化与 $L_0$ 最小化等价的充分条件。
感知矩阵 $\mathbf{A}$ 满足阶数为 $K$ 的RIP是指，对于任意的 $K$-稀疏向量 $\mathbf{s}$，存在一个足够小的常数 $\delta_K \in (0,1)$，使得以下不等式成立：

$$ (1 - \delta_K) \|\mathbf{s}\|_2^2 \le \|\mathbf{A}\mathbf{s}\|_2^2 \le (1 + \delta_K) \|\mathbf{s}\|_2^2 $$

直观地说，就是“矩阵 $\mathbf{A}$ （几乎）保持任意稀疏向量的长度不变”的性质。Candès和Tao出色地证明了，如果 $\mathbf{A}$ 满足特定的RIP条件，在无噪声的情况下，$(P_1)$ 的解将与 $(P_0)$ 的解完全一致。

从更实用的角度来看，如果观测矩阵 $\mathbf{\Phi}$ 使用**随机矩阵（服从高斯分布或伯努利分布的随机数矩阵）**，研究表明它以极高的概率满足RIP。换句话说，“随机观测”是压缩感知中最有效且最普遍的采样策略。

要保证恢复成功，所需的观测次数 $M$ 与信号长度 $N$ 和稀疏度 $K$ 存在以下数量级关系：

$$ M \ge C \cdot K \log\left(\frac{N}{K}\right) $$
（$C$ 为常数）

这意味着，与采样定理要求的 $N$ 次观测相比，只需要少得多的次数（依赖于 $K$）即可。

## 5. 压缩感知的应用案例

压缩感知理论为信息工程和物理学的各个领域带来了革命。

### 1. 加速MRI（核磁共振成像）扫描
最成功的商业应用之一是MRI。MRI利用强磁场获取人体的断层图像，但在收集数据（称为k空间的频率域数据）时存在物理限制，需要耗费大量时间。
在对儿童患者或跳动的心脏等运动器官进行成像时，长时间保持静止非常困难。通过将压缩感知应用于MRI，我们在k空间对采样数据进行随机欠采样，成功地将扫描时间缩短至传统方法的几分之一。目前，Siemens和GE等主要医疗设备制造商都在销售标配压缩感知技术的MRI设备。

### 2. 黑洞成像（事件视界望远镜，Event Horizon Telescope）
2019年，国际研究团队“事件视界望远镜（EHT）”成功拍摄到人类历史上首张黑洞阴影图像。为了构建一个地球大小的巨大虚拟望远镜，研究人员整合了散布在世界各地射电望远镜的数据（甚长基线干涉测量，VLBI），但由于地球上望远镜的分布有限，观测数据存在巨大的“缝隙（缺失数据）”。
为了从这些稀疏的数据中恢复黑洞图像，他们开发了称为CHIRP（Continuous High-resolution Image Reconstruction using Patch priors）的算法。这也可以说是一种利用了宇宙图像所具有的稀疏性和结构性先验知识的压缩感知的应用。

### 3. 单像素相机（Single-Pixel Camera）
莱斯大学（Rice University）的研究团队开发出了一种只有1个光传感器（像素）的相机。
该相机使用DMD（数字微镜器件）以随机模式反射物体的光线，并用一个传感器测量其总和。将这一过程重复数千次，即可重建出数百万像素的图像。在制造多像素传感器极其昂贵的波段（如红外线或太赫兹波）成像中，该技术非常有用。

## 6. 使用Python的压缩感知实现示例

由于单纯的理论有些难以体会，让我们使用Python来进行实际的压缩感知仿真。
在这里，我们将生成一个一维的稀疏信号，并通过少量的随机观测，使用 $L_1$ 优化来恢复原始信号。我们将使用 `cvxpy` 库进行优化。

### 安装所需的库
```bash
pip install numpy matplotlib cvxpy
```

### 实现代码

```python
import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cp

# 固定随机数种子
np.random.seed(42)

# --- 1. 问题设定 ---
N = 1000  # 信号的维度（原本应该采样的数量）
K = 50    # 稀疏度（非零元素的数量）
M = 250   # 观测次数（仅为N的25%）

# --- 2. 生成稀疏的真实信号 ---
# 创建真实信号 x_true（初始值全为零）
x_true = np.zeros(N)
# 随机选择K个索引，并设置非零值（高斯分布）
nonzero_indices = np.random.choice(N, K, replace=False)
x_true[nonzero_indices] = np.random.randn(K)

# --- 3. 观测过程的仿真 ---
# 生成随机高斯观测矩阵 A (M x N)
A = np.random.randn(M, N)
# 对各列进行归一化（使得范数为1）
A = A / np.linalg.norm(A, axis=0)

# 观测数据 y = A * x_true
y = A @ x_true

# --- 4. 通过压缩感知恢复信号 (L1优化) ---
# 使用cvxpy定义优化问题
x_reconstruct = cp.Variable(N)
# 目标函数: L1范数最小化
objective = cp.Minimize(cp.norm(x_reconstruct, 1))
# 约束条件: y = A * x (与观测数据一致)
constraints = [A @ x_reconstruct == y]

# 定义并求解问题
prob = cp.Problem(objective, constraints)
print("正在执行优化计算...")
prob.solve(solver=cp.ECOS)

# 恢复出的信号
x_rec = x_reconstruct.value

# --- 5. 结果可视化 ---
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(x_true, label='True Signal', alpha=0.7)
plt.title(f'Original Sparse Signal (N={N}, K={K})')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(x_rec, color='red', label='Reconstructed Signal', alpha=0.7)
plt.title(f'Reconstructed via L1 Minimization (M={M} measurements)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# 检查恢复精度
error = np.linalg.norm(x_true - x_rec)
print(f"恢复误差 (L2 norm): {error:.6e}")
```

### 代码讲解
1. **生成信号**: 在维度 $N=1000$ 中，创建一个仅在 $K=50$ 个位置上有值（其余为零）的稀疏向量 `x_true`。
2. **观测**: 如果按照采样定理，需要进行1000次测量，但在这里我们仅使用 $M=250$ 次（25%）的随机观测矩阵 `A`，即可获得数据 `y`。
3. **恢复**: 仅将观测数据 `y` 和矩阵 `A` 作为输入，使用 `cvxpy` 寻找“满足 $\mathbf{y} = \mathbf{A}\mathbf{x}$ 且 $L_1$ 范数最小的 $\mathbf{x}$”。
4. **结果**: 计算完成后，恢复误差变得极小（在 `1e-9` 以下），可以证实仅通过25%的观测数据就**完全（Exact）恢复**了真实信号。

```mermaid
flowchart LR
    X["未知的稀疏信号\nx (N维)"] -->|随机观测\n矩阵 A| Y["观测数据\ny (M维, M < N)"]
    Y -->|L1优化\n(凸优化算法)| X_hat["恢复出的信号\nx^"]
    X -. "保证完全一致" .-> X_hat
```

## 7. 总结与未来展望

压缩感知从根本上改变了信号处理历史中的范式。“不是大量测量后再丢弃，而是一开始就聪明地测量所需的量”，这一方法依赖于深奥的数学理论（凸优化、[随机矩阵理论](/zh-cn/p/random-matrix-theory/)、高维几何学）。

目前，结合深度学习（Deep Learning）和压缩感知的研究正在蓬勃发展。一种利用神经网络更快、更高精度地解决反问题（Deep Unfolding / Algorithm Unrolling）的方法正在逐渐成为主流，取代了传统的 $L_1$ 优化算法。通过这种方法，观测矩阵的设计也可以基于数据驱动来学习，推动了在进一步加速MRI和具有抗噪性的图像重建等方面的应用。

压缩感知利用少量信息就能准确洞察整体的数学魔法，在未来自动驾驶、[物联网](/zh-cn/p/technology-iot/)传感器网络、太空探索等面临数据爆炸挑战的各个领域，必将继续为我们提供一双崭新的“眼睛”。
