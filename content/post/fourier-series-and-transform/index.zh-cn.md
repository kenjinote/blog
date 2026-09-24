---
title: "傅里叶级数与傅里叶变换：将任何复杂波形分解为正弦和余弦之和"
description: "详细解释将复杂波形表示为简单正弦波和余弦波叠加的“傅里叶级数”，以及其向非周期函数扩展的“傅里叶变换”。"
slug: "fourier-series-and-transform"
date: "2026-09-24T16:08:36+09:00"
image: "eyecatch.jpg"
categories:
  - "mathematics"
tags:
  - "傅里叶"
  - "数学"
  - "物理"
---

## 1. 简介：波相加的魔法

我们的周围充满了各种 **“波”**，如声音、光和电磁波。如果乍一看非常复杂和不规则的波形实际上是由简单的波组合而成的呢？这一惊人事实的数学表示就是约瑟夫·傅里叶提出的 **“傅里叶级数”**，以及其进一步的发展 **“傅里叶变换”**。

在本文中，我们将深入探讨这种迷人的数学方法，从其基础到直观的理解，以及在现代技术中的应用。

## 2. 傅里叶级数：分解周期波

傅里叶级数的基本思想是“任何周期函数都可以表示为具有不同频率的正弦波和余弦波的无限总和”。

### 2.1 实数形式的傅里叶级数

周期为 $2\pi$ 的函数 $f(x)$ 可以展开如下。

$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n \cos(nx) + b_n \sin(nx) \right)
$$

这里，$a_0$、$a_n$ 和 $b_n$ 被称为 **“傅里叶系数”**，它们表示每种波包含的强度。这些系数由以下积分计算。

$$
a_0 = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) dx \quad (\text{直流分量})
$$
$$
a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos(nx) dx \quad (\text{余弦分量的权重})
$$
$$
b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin(nx) dx \quad (\text{正弦分量的权重})
$$

### 2.2 复数傅里叶级数

使用欧拉公式 $e^{i\theta} = \cos\theta + i\sin\theta$，傅里叶级数可以更优雅地写成复指数函数的形式。

$$
f(x) = \sum_{n=-\infty}^{\infty} c_n e^{inx}
$$

$$
c_n = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(x) e^{-inx} dx \quad (\text{复傅里叶系数})
$$

复数形式作为通往后文所述的傅里叶变换的桥梁，起着非常重要的作用。

## 3. 傅里叶变换：向非周期函数的扩展

傅里叶级数只能应用于周期函数。然而，现实世界中的许多信号（如简短的声音或一次性脉冲信号）是非周期的。因此，通过考虑周期趋于无穷大（$T \to \infty$）的极限，推导出了 **“傅里叶变换”**。

### 3.1 傅里叶变换的定义

函数 $f(t)$ 的傅里叶变换 $\mathcal{F}\{f(t)\}$ 和逆傅里叶变换定义如下。

$$
F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt \quad (\text{从时域到频域的变换})
$$

$$
f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i\omega t} d\omega \quad (\text{从频域到时域的逆变换})
$$

这里，$t$ 表示时间，$\omega$ 表示角频率。$F(\omega)$ 是一个函数，指示原始信号 $f(t)$ 中包含了多少频率为 $\omega$ 的分量（振幅和相位）。

### 3.2 信号处理流程

下图展示了如何使用傅里叶变换处理输入信号。

```mermaid
flowchart LR
    A["输入信号的时间波形"] -->|"傅里叶变换"| B["频谱"]
    B -->|"滤波处理"| C["处理后的频谱"]
    C -->|"逆傅里叶变换"| D["输出信号的时间波形"]
    
    %% 节点样式
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bbf,stroke:#333,stroke-width:2px
    style D fill:#f9f,stroke:#333,stroke-width:2px
```

## 4. 离散傅里叶变换（DFT）和快速傅里叶变换（FFT）

为了用计算机处理信号，连续时间和具有无限长度的积分必须被有限数量的离散数据点之和所取代。这就是 **离散傅里叶变换（DFT）**。

$$
X_k = \sum_{n=0}^{N-1} x_n e^{-i \frac{2\pi}{N} k n} \quad \text{对于 } k = 0, 1, \dots, N-1
$$

此外，将此 DFT 的计算复杂度从 $O(N^2)$ 显着降低到 $O(N \log N)$ 的算法是 **快速傅里叶变换（FFT）**。随着 FFT 的出现，数字信号处理（DSP）领域经历了爆炸性的发展。我们熟悉的许多技术，例如智能手机上的语音识别和 JPEG 图像压缩，都得益于 FFT。

```python
import numpy as np
import matplotlib.pyplot as plt

# 创建时间轴（从0到1秒，采样频率1000Hz）
t = np.linspace(0, 1, 1000, endpoint=False)

# 合成50Hz和120Hz正弦波的信号
signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

# 执行FFT
fft_result = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(t), 1/1000)

# 仅绘制正频率域的索引
positive_freqs = frequencies > 0
```

## 5. 结论

傅里叶级数和傅里叶变换是科学和工程中最强大的工具之一，将复杂的现象分解为简单的元素。通过将时间转换为频率的这种数学“镜头”来看待世界，我们可以发现隐藏的模式并高效地处理信息。

今天，波相加的魔法继续作为现代技术的基础发挥着积极作用。
