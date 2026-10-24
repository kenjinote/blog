---
title: "フーリエ級数とフーリエ変換：波をサインとコサインの成分で捉える"
description: "複雑な波形を単純なサイン波とコサイン波の重ね合わせとして表現する「フーリエ級数」と、それを非周期関数に拡張した「フーリエ変換」について詳しく解説します。"
slug: "fourier-series-and-transform"
date: "2026-09-20T14:30:00+09:00"
lastmod: 2026-10-24
image: "eyecatch.jpg"
categories:
  - "mathematics"
tags:
  - "Fourier"
  - "Math"
  - "Physics"
---

## 1. はじめに：波の足し算という考え方

私たちの身の回りには、音、光、電磁波など、さまざまな **「波」** が溢れています。一見すると非常に複雑で不規則に見える波形でも、実は単純な波の組み合わせでできているとしたらどうでしょうか。この見方を、関数の条件や収束の意味を定めて数学的に扱うのが、ジョゼフ・フーリエによって提唱された **「フーリエ級数」** と、連続的な周波数を扱う **「フーリエ変換」** です。

本記事では、この魅力的な数学の手法について、基礎から直感的な理解、そして現代のテクノロジーにおける応用までを説明します。

## 2. フーリエ級数：周期的な波を分解する

フーリエ級数（Fourier series）は、周期関数を基本周波数の整数倍の周波数を持つ三角関数の成分で表す方法です。ただし、係数を計算できることと、級数が各点で元の関数に収束することは別です。ここでは、一周期を有限個の区間に分けると各区間で連続微分可能で、端で関数と導関数が有限の片側極限を持つ、区分的に滑らかな周期関数を考えます。この十分条件のもとでは、連続点で元の値に、跳びの点では左右の極限の平均に収束します。

$$
\lim_{M\to\infty} S_M(x)=\frac{f(x-)+f(x+)}{2}
$$

$S_M$ は第 $M$ 高調波までの部分和です。周期の継ぎ目でも周期延長した左右の極限を使います。跳びの近くにはギブズ現象による行き過ぎが残るため、項数を増やせば全区間で一様に誤差が消えるわけではありません。

### 2.1 実数形式のフーリエ級数

上の条件を満たす実数値の周期 $2\pi$ の関数について、連続点では次の等式が成り立ちます。角度はラジアンで表します。跳びの点の左辺は、先ほどの左右の極限の平均に読み替えます。

$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n \cos(nx) + b_n \sin(nx) \right)
$$

ここで、$a_0$、$a_n$、$b_n$ は**フーリエ係数**です。定数項（直流成分・一周期の平均値）は $a_0/2$ であり、$a_0$ そのものではありません。$n\ge1$ に対する $a_n,b_n$ は余弦・正弦の重みです。係数は三角関数の直交性から次の積分で求められます。

$$
a_0 = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) dx
$$
$$
a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos(nx) dx
$$
$$
b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin(nx) dx
$$

### 2.2 複素フーリエ級数

[オイラーの公式](/p/eulers-identity/) $e^{i\theta} = \cos\theta + i\sin\theta$ を用いると、同じ級数を複素指数関数で表せます。以下の両側の和は、$n=-M$ から $M$ までの対称部分和の極限として読みます。連続点での等式と跳びでの注意は実数形式と同じです。

$$
f(x) = \sum_{n=-\infty}^{\infty} c_n e^{inx}
$$

$$
c_n = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(x) e^{-inx} dx
$$

実数値の $f$ では $c_0=a_0/2$、$c_n=(a_n-ib_n)/2$、$c_{-n}=(a_n+ib_n)/2$（$n\ge1$）です。負の周波数は、実数の波形を複素指数関数で表すときにも現れます。複素形式はフーリエ変換とのつながりも見やすくします。

## 3. フーリエ変換：非周期関数への拡張

級数は周期延長した関数にも使えますが、単発のパルスなどを実数軸全体で扱うときには、連続した周波数を持つ**フーリエ変換**が適しています。周期を長くして周波数の間隔を狭める考え方は直感的な橋渡しになりますが、極限と積分の交換には条件が必要で、それだけで一般の証明にはなりません。

### 3.1 フーリエ変換の定義

本記事では順変換の指数に負号、逆変換に $1/(2\pi)$ を置く規約を使います。$\int_{-\infty}^{\infty}|f(t)|\,dt<\infty$ なら、次の順変換はすべての実数 $\omega$ で絶対収束します。

$$
F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt
$$

例えば $f$ が連続で、$f$ と $F$ がともに絶対可積分なら、逆変換は次のように $f$ を復元します。この式を任意の関数に無条件で適用することはできません。

$$
f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i\omega t} d\omega
$$

ここで、$t$ は秒、$\omega$ は角周波数（rad/s）とします。Hzでの周波数 $\nu$ とは $\omega=2\pi\nu$ の関係です。$F(\omega)$ は連続スペクトルの複素数値の重みを表し、$F\ne0$ では絶対値と偏角から大きさと位相を読み取れます。連続スペクトルの重みは、周期信号の単一成分の振幅とそのまま同じものではありません。

跳びのある関数では、追加の正則性の条件と対称な広義積分によって左右の極限の平均を復元する場合もあります。また、二乗可積分関数や周期信号を扱うには、それぞれ $L^2$ や超関数としての拡張が必要になることがあります。本記事ではその理論には立ち入りません。符号や正規化は文献で異なるので、順変換と逆変換を対で確認してください。

### 3.2 信号処理の流れ

以下の図は、入力信号がフーリエ変換を用いてどのように処理されるかを示しています。

```mermaid
flowchart LR
    A["入力信号の時間波形"] -->|"フーリエ変換"| B["周波数スペクトル"]
    B -->|"フィルタリング処理"| C["加工されたスペクトル"]
    C -->|"逆フーリエ変換"| D["出力信号の時間波形"]
    
    %% ノードのスタイリング
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bbf,stroke:#333,stroke-width:2px
    style D fill:#f9f,stroke:#333,stroke-width:2px
```

## 4. 離散フーリエ変換 (DFT) と高速フーリエ変換 (FFT)

**離散フーリエ変換（DFT）**は、有限長の列 $x_0,\ldots,x_{N-1}$ を同じ長さの周波数成分へ写す変換です。連続フーリエ変換の積分をそのまま置き換えたものとは区別します。時間信号を扱う場合は、標本化と有限時間の切り出しを先に行います。順変換と逆変換は次の対です。

$$
X_k = \sum_{n=0}^{N-1} x_n e^{-i \frac{2\pi}{N} k n} \quad \text{for } k = 0, 1, \dots, N-1
$$

$$
x_n=\frac{1}{N}\sum_{k=0}^{N-1}X_k e^{i\frac{2\pi}{N}kn} \quad \text{for } n=0,1,\dots,N-1
$$

標本化周波数を $f_s$ とすると、周波数ビンの間隔は $f_s/N$ Hzです。DFTは有限列を周期的に繰り返す見方と対応します。標本化前の信号に $f_s/2$ 以上の成分があると折り返し（エイリアシング）の問題があるため、連続信号の復元には帯域制限などの仮定が必要です。観測区間に整数周期が収まらない正弦波では、エネルギーが複数のビンに広がるスペクトル漏れも生じます。

DFTを定義どおりに全 $N$ 成分計算すると $O(N^2)$ の演算が必要です。[高速フーリエ変換（FFT）](/p/fast-fourier-transform-algorithm/)は同じDFTを効率よく計算するアルゴリズムの総称で、例えば2のべき乗の長さでは分割によって $O(N\log N)$ にできます。FFTは別の変換や、それ自体が近似の名称なのではありません。音声などのデジタル信号処理に広く使われます。一方、通常の非可逆JPEGの基本方式は離散コサイン変換（DCT）を使います。関連する変換でも、JPEGを直接FFTの利用例とする説明とは区別します。

### 4.1 Pythonで2つの周波数と振幅を確認する

次はNumPyとMatplotlibを使う例です。1秒間を1,000 Hzで標本化し、50 Hz・振幅1と120 Hz・振幅0.5の正弦波を合成します。実数入力なので `rfft` と `rfftfreq` を使います。例では周波数が1 Hz間隔のビンに一致し、両方とも500 Hz未満です。

```python
import numpy as np
import matplotlib.pyplot as plt

# 1秒間、1000 Hzで標本化する（終点1秒は含めない）
fs = 1000.0
N = 1000
t = np.arange(N) / fs
signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

# 実数信号の非負周波数側のDFT
fft_result = np.fft.rfft(signal)
frequencies = np.fft.rfftfreq(N, d=1 / fs)

# 片側の振幅。DCと、Nが偶数のときのナイキスト成分は2倍しない
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

出力は丸めて `50 Hz: 1.000` と `120 Hz: 0.500` になります。`rfft` の既定の順変換は $N$ で割られていないため、振幅表示では上の正規化を行います。実数信号の正負周波数の対をまとめるために内部のビンだけ2倍し、直流と偶数長のナイキスト成分は除きます。これはこの例の、窓を掛けないビンに一致した正弦波の振幅を読む方法です。任意の信号のスペクトルや、窓を掛けたデータから同じ式だけで正確な振幅が読めるわけではありません。


## 5. まとめ

フーリエ級数とフーリエ変換は、複雑な現象をシンプルな要素に分解するという、科学と工学における最も強力なツールの1つです。時間を周波数に変換するこの数学的な「レンズ」を通して世界を見ることで、私たちは隠されたパターンを発見し、情報を効率的に処理することができるのです。

級数と変換では、周期性、収束の条件、周波数の単位、正規化を指定することが大切です。DFTとその計算法であるFFTを区別すると、数式と実際のプログラムのつながりも明確になります。

## 参考資料

- [MIT ES.1803 Topic 22：直交性、係数、級数の収束（§22.5–22.7）](https://ocw.mit.edu/courses/es-1803-differential-equations-spring-2024/mites_1803_s24_topic22.pdf)
- [MIT 18.330：フーリエ変換と逆変換（第6章、Definition 14）](https://math.mit.edu/icg/resources/teaching/18.330/18.330-Apr29.pdf)
- [NIST DLMF §1.14(i)：変換の定義と反転の条件（本記事とは符号・正規化が異なる）](https://dlmf.nist.gov/1.14#i)
- [MIT 6.341 Lecture 19：DFTとFFTの演算量](https://ocw.mit.edu/courses/6-341-discrete-time-signal-processing-fall-2005/4ee39a5e74c9f5099ac516ce57215c96_lec19.pdf)
- [NumPy 2.3：FFT](https://numpy.org/doc/2.3/reference/generated/numpy.fft.fft.html)、[実数入力のrfft](https://numpy.org/doc/2.3/reference/generated/numpy.fft.rfft.html)、[周波数ビンのrfftfreq](https://numpy.org/doc/2.3/reference/generated/numpy.fft.rfftfreq.html)
- [ITU-T T.81：JPEGの非可逆DCT方式（§4.2–4.3）](https://www.w3.org/Graphics/JPEG/itu-t81.pdf)
