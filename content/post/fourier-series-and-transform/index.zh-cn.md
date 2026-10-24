---
title: "傅里叶级数与傅里叶变换：用正弦与余弦成分理解波形"
description: "详细解释将复杂波形表示为简单正弦波和余弦波叠加的“傅里叶级数”，以及其向非周期函数扩展的“傅里叶变换”。"
slug: "fourier-series-and-transform"
date: "2026-09-20T14:30:00+09:00"
lastmod: 2026-10-24
image: "eyecatch.jpg"
categories:
  - "mathematics"
tags:
  - "傅里叶"
  - "数学"
  - "物理"
---

## 1. 引言：从波的叠加来思考

声音、光、电磁波等各种**波**无处不在。看起来复杂而不规则的波形，能否理解为简单波形的组合？与约瑟夫·傅里叶相关的**傅里叶级数**，以及使用连续频率的**傅里叶变换**，为这种思路提供了数学表达。不过，使用时需要说明函数满足的条件，以及收敛的含义。

本文从基本公式和直观理解出发，介绍它们在现代信号处理中的应用。

## 2. 傅里叶级数：分解周期波形

傅里叶级数用频率为基频整数倍的三角函数成分来表示周期函数。能够计算出系数，并不意味着级数在每一点都收敛到原函数的值。这里考虑分段光滑的周期函数：一周期可以分成有限个区间，函数在各区间内部连续可微，且函数及其导函数在端点处具有有限的单侧极限。在这个充分条件下，级数在连续点收敛到原函数的值，在跳跃间断点则收敛到左右极限的平均值。

$$
\lim_{M\to\infty} S_M(x)=\frac{f(x-)+f(x+)}{2}
$$

$S_M$ 表示保留到第 $M$ 次谐波的部分和。在两个周期的连接处，也要使用周期延拓后的左右极限。跳跃附近存在吉布斯现象所产生的过冲；增加项数时，这种过冲并不会消失。因此，不能认为增加项数就会使整个区间上的误差一致趋于零。

### 2.1 实数形式的傅里叶级数

对于满足上述条件、周期为 $2\pi$ 的实值函数，下面的等式在连续点成立。角度以弧度表示。在跳跃间断点，应把左端替换为左右极限的平均值。

$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n \cos(nx) + b_n \sin(nx) \right)
$$

$a_0,a_n,b_n$ 称为**傅里叶系数**。常数项，即直流分量和一周期的平均值，是 $a_0/2$，不是 $a_0$。对于 $n\ge1$，$a_n,b_n$ 分别是余弦和正弦的权重。利用三角函数的正交性，可以得到以下系数公式。

$$
a_0 = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) dx
$$

$$
a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos(nx) dx
$$

$$
b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin(nx) dx
$$

### 2.2 复数形式的傅里叶级数

利用[欧拉公式](/zh-cn/p/eulers-identity/) $e^{i\theta}=\cos\theta+i\sin\theta$，同一个级数可以写成复指数函数的形式。下面的双边求和，应理解为从 $n=-M$ 到 $M$ 的对称部分和的极限。连续点的等式和跳跃处的注意事项与实数形式相同。

$$
f(x) = \sum_{n=-\infty}^{\infty} c_n e^{inx}
$$

$$
c_n = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(x) e^{-inx} dx
$$

当 $f$ 为实值函数时，$c_0=a_0/2$，$c_n=(a_n-ib_n)/2$，$c_{-n}=(a_n+ib_n)/2$（$n\ge1$）。因此，即使原波形是实值的，用复指数函数表示时也会出现负频率。复数形式还便于理解级数与傅里叶变换的联系。

## 3. 傅里叶变换：扩展到非周期函数

傅里叶级数也能用于经过周期延拓的函数。但若要在整个实数轴上描述单个脉冲等信号，具有连续频率的**傅里叶变换**更为合适。把周期逐渐增大、使频率间隔逐渐缩小，可以提供直观的联系。不过，交换极限与积分需要满足条件，单凭这个直观过程还不能作为一般性证明。

### 3.1 定义与逆变换

本文约定正变换的指数带负号，逆变换带因子 $1/(2\pi)$。如果 $\int_{-\infty}^{\infty}|f(t)|\,dt<\infty$，则下面的正变换对所有实数 $\omega$ 都绝对收敛。

$$
F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt
$$

例如，如果 $f$ 连续，且 $f$ 和 $F$ 都绝对可积，就可以用下面的逆变换还原 $f$。不能对任意函数无条件使用这个公式。

$$
f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i\omega t} d\omega
$$

这里取 $t$ 的单位为秒，$\omega$ 为角频率，单位是 rad/s。以 Hz 表示的频率 $\nu$ 与它的关系为 $\omega=2\pi\nu$。复值函数 $F(\omega)$ 表示连续频谱中的权重；在 $F\ne0$ 处，可由模和辐角读取大小与相位。连续频谱的权重，不能直接等同于周期信号中单个成分的振幅。

对于有跳跃的函数，在附加正则性条件下，采用对称的反常积分，有时可以还原左右极限的平均值。平方可积函数和周期信号则可能分别需要 $L^2$ 意义和广义函数意义下的扩展。本文不展开这些理论。不同文献可能采用不同的符号和归一化约定，因此要把正变换和逆变换作为一对来核对。

### 3.2 信号处理流程

下图展示了在频域处理输入信号的流程。

```mermaid
flowchart LR
    A["输入信号的时间波形"] -->|"傅里叶变换"| B["频谱"]
    B -->|"滤波处理"| C["处理后的频谱"]
    C -->|"逆傅里叶变换"| D["输出信号的时间波形"]

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bbf,stroke:#333,stroke-width:2px
    style D fill:#f9f,stroke:#333,stroke-width:2px
```

## 4. 离散傅里叶变换（DFT）与快速傅里叶变换（FFT）

**离散傅里叶变换（DFT）**把有限序列 $x_0,\ldots,x_{N-1}$ 映射为同样数量的频率成分。它不是简单地把连续傅里叶变换中的积分换成有限和。处理时间信号时，应先进行采样和有限时间截取。正变换与逆变换为：

$$
X_k = \sum_{n=0}^{N-1} x_n e^{-i \frac{2\pi}{N} k n} \quad \text{for } k = 0, 1, \dots, N-1
$$

$$
x_n=\frac{1}{N}\sum_{k=0}^{N-1}X_k e^{i\frac{2\pi}{N}kn} \quad \text{for } n=0,1,\dots,N-1
$$

设采样频率为 $f_s$，则频率格点（bin）之间的间隔为 $f_s/N$ Hz。DFT对应于把有限序列作周期重复的理解。采样前的信号若含有 $f_s/2$ 或更高频率的成分，就会有混叠或歧义问题，因此还原连续信号需要带限等假设。若正弦波在观测区间内没有恰好完成整数个周期，还会出现频谱泄漏，其能量分散到多个频率格点。

直接按定义计算全部 $N$ 个DFT成分需要 $O(N^2)$ 次运算。[快速傅里叶变换（FFT）](/zh-cn/p/fast-fourier-transform-algorithm/)是高效计算同一个DFT的一类算法。例如，长度为2的幂时，分治方法可以把计算量降到 $O(N\log N)$。FFT不是另一种变换，也不意味着该方法本身是一种近似。它广泛用于音频等数字信号处理。另一方面，通常的有损JPEG基本编码方式采用离散余弦变换（DCT）。这些变换虽有关联，却不应直接把JPEG列为使用FFT的例子。

### 4.1 用Python检查两种频率及其振幅

以下示例使用NumPy和Matplotlib，以1,000 Hz采样1秒，将50 Hz、振幅1和120 Hz、振幅0.5的正弦波叠加。输入为实数，因此使用 `rfft` 和 `rfftfreq`。两种频率都与间隔1 Hz的频率格点对齐，且都低于500 Hz。

```python
import numpy as np
import matplotlib.pyplot as plt

# 以1000 Hz采样1秒，不包含终点1秒
fs = 1000.0
N = 1000
t = np.arange(N) / fs
signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

# 实信号的非负频率部分的DFT
fft_result = np.fft.rfft(signal)
frequencies = np.fft.rfftfreq(N, d=1 / fs)

# 单边振幅：直流成分及偶数长度的奈奎斯特成分不乘以2
amplitude = np.abs(fft_result) / N
if N % 2 == 0:
    amplitude[1:-1] *= 2
else:
    amplitude[1:] *= 2

peak_indices = np.argsort(amplitude)[-2:]
for k in sorted(peak_indices, key=lambda k: frequencies[k]):
    print(f"{frequencies[k]:.0f} Hz: {amplitude[k]:.3f}")

fig, ax = plt.subplots()
ax.plot(frequencies, amplitude)
ax.set(xlim=(0, 200), xlabel="Frequency (Hz)", ylabel="Amplitude",
       title="One-sided amplitude spectrum")
ax.grid(True)
fig.tight_layout()
plt.show()
```

输出经四舍五入后为 `50 Hz: 1.000` 和 `120 Hz: 0.500`。`rfft` 默认的正变换没有除以 $N$，所以显示振幅时使用上面的归一化。将实信号的正负频率配对合并时，只把内部格点的值乘以2，不包括直流成分，以及偶数长度时的奈奎斯特成分。这是在本例中读取未加窗、与格点对齐的正弦波振幅的方法。对于任意信号或加窗后的数据，不能只靠同一个公式就保证得到准确的振幅。

## 5. 总结

傅里叶级数和傅里叶变换帮助我们将复杂现象分解为简单成分。从频域观察信号，可以发现隐藏的模式并进行有效处理。

使用时应指定周期性、收敛条件、频率单位和归一化约定。区分DFT与计算它的FFT算法，也能使数学公式与实际程序的联系更加清楚。

## 参考资料

- [MIT ES.1803 Topic 22：系数、收敛、吉布斯现象和正交性（§22.5–22.7）](https://ocw.mit.edu/courses/es-1803-differential-equations-spring-2024/mites_1803_s24_topic22.pdf)
- [MIT 18.330：傅里叶变换与逆变换（第6章，Definition 14）](https://math.mit.edu/icg/resources/teaching/18.330/18.330-Apr29.pdf)
- [NIST DLMF §1.14(i)：定义和反演条件；符号与归一化和本文不同](https://dlmf.nist.gov/1.14#i)
- [MIT 6.341 Lecture 19：DFT与FFT的运算量](https://ocw.mit.edu/courses/6-341-discrete-time-signal-processing-fall-2005/4ee39a5e74c9f5099ac516ce57215c96_lec19.pdf)
- [NumPy 2.3：FFT](https://numpy.org/doc/2.3/reference/generated/numpy.fft.fft.html)、[实数输入的rfft](https://numpy.org/doc/2.3/reference/generated/numpy.fft.rfft.html)、[频率格点的rfftfreq](https://numpy.org/doc/2.3/reference/generated/numpy.fft.rfftfreq.html)
- [ITU-T T.81：JPEG有损DCT方式（§4.2–4.3）](https://www.w3.org/Graphics/JPEG/itu-t81.pdf)
