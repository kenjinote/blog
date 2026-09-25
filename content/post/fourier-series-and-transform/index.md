---
title: "フーリエ級数とフーリエ変換：あらゆる複雑な波をサインとコサインの足し算に分解する"
description: "複雑な波形を単純なサイン波とコサイン波の重ね合わせとして表現する「フーリエ級数」と、それを非周期関数に拡張した「フーリエ変換」について詳しく解説します。"
slug: "fourier-series-and-transform"
date: "2026-09-20T14:30:00+09:00"
image: "eyecatch.jpg"
categories:
  - "mathematics"
tags:
  - "Fourier"
  - "Math"
  - "Physics"
---

## 1. はじめに：波の足し算という魔法

私たちの身の回りには、音、光、電磁波など、さまざまな **「波」** が溢れています。一見すると非常に複雑で不規則に見える波形でも、実は単純な波の組み合わせでできているとしたらどうでしょうか。この驚くべき事実を数学的に表現したのが、ジョゼフ・フーリエによって提唱された **「フーリエ級数」** と、それをさらに発展させた **「フーリエ変換」** です。

本記事では、この魅力的な数学の手法について、基礎から直感的な理解、そして現代のテクノロジーにおける応用までを深く掘り下げていきます。

## 2. フーリエ級数：周期的な波を分解する

フーリエ級数（Fourier series）の基本的なアイデアは、「どのような周期関数であっても、異なる周波数を持つサイン波（正弦波）とコサイン波（余弦波）の無限の足し合わせで表現できる」というものです。

### 2.1 実数形式のフーリエ級数

周期 $2\pi$ を持つ関数 $f(x)$ は、以下のように展開できます。

$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n \cos(nx) + b_n \sin(nx) \right)
$$

ここで、$a_0$、$a_n$、$b_n$ は **「フーリエ係数」** と呼ばれ、それぞれの波がどの程度の強さで含まれているかを表します。これらの係数は以下の積分で計算されます。

$$
a_0 = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) dx \quad (\text{直流成分})
$$
$$
a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos(nx) dx \quad (\text{コサイン成分の重み})
$$
$$
b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin(nx) dx \quad (\text{サイン成分の重み})
$$

### 2.2 複素フーリエ級数

[オイラー](https://kenji.blog/p/euler/)の公式 $e^{i\theta} = \cos\theta + i\sin\theta$ を用いると、フーリエ級数はよりエレガントな複素指数関数の形で書き表すことができます。

$$
f(x) = \sum_{n=-\infty}^{\infty} c_n e^{inx}
$$

$$
c_n = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(x) e^{-inx} dx \quad (\text{複素フーリエ係数})
$$

複素形式は、後述するフーリエ変換への橋渡しとして非常に重要な役割を果たします。

## 3. フーリエ変換：非周期関数への拡張

フーリエ級数は周期的な関数にしか適用できません。しかし、現実世界の多くの信号（たとえば音声の短い発声や、一度きりのパルス信号）は非周期的です。そこで、周期を無限大（$T \to \infty$）に飛ばす極限を考えることで、 **「フーリエ変換」** が導かれます。

### 3.1 フーリエ変換の定義

関数 $f(t)$ に対するフーリエ変換 $\mathcal{F}\{f(t)\}$ および逆フーリエ変換は、以下のように定義されます。

$$
F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt \quad (\text{時間領域から周波数領域への変換})
$$

$$
f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i\omega t} d\omega \quad (\text{周波数領域から時間領域への逆変換})
$$

ここで、$t$ は時間、$\omega$ は角周波数を表します。$F(\omega)$ は、元の信号 $f(t)$ の中に周波数 $\omega$ の成分がどれだけ含まれているか（振幅と位相）を示す関数となります。

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

コンピュータで信号を処理するためには、連続的な時間と無限の長さを持つ積分を、有限個の離散的なデータポイントの和に置き換える必要があります。これが **離散フーリエ変換 (DFT)** です。

$$
X_k = \sum_{n=0}^{N-1} x_n e^{-i \frac{2\pi}{N} k n} \quad \text{for } k = 0, 1, \dots, N-1
$$

さらに、この DFT の計算量を $O(N^2)$ から $O(N \log N)$ へと劇的に削減するアルゴリズムが **[高速フーリエ変換](/p/fast-fourier-transform-algorithm/) ([FFT](/p/fast-fourier-transform-algorithm/))** です。[FFT](/p/fast-fourier-transform-algorithm/) の登場により、デジタル信号処理（DSP）の分野は飛躍的な発展を遂げました。スマートフォンでの音声認識や、JPEG 画像の圧縮など、私たちの身近な技術の多くが [FFT](/p/fast-fourier-transform-algorithm/) の恩恵を受けています。

```python
import numpy as np
import matplotlib.pyplot as plt

# 時間軸の作成（0から1秒まで、サンプリング周波数1000Hz）
t = np.linspace(0, 1, 1000, endpoint=False)

# 50Hzと120Hzのサイン波を合成した信号
signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

# FFTの実行
fft_result = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(t), 1/1000)

# 正の周波数領域のみをプロットするためのインデックス
positive_freqs = frequencies > 0
```

## 5. まとめ

[フーリエ級数とフーリエ変換](https://kenji.blog/p/fourier-series-and-transform/)は、複雑な現象をシンプルな要素に分解するという、科学と工学における最も強力なツールの1つです。時間を周波数に変換するこの数学的な「レンズ」を通して世界を見ることで、私たちは隠されたパターンを発見し、情報を効率的に処理することができるのです。

波の足し算という魔法は、今もなお現代技術の基盤として活躍し続けています。
