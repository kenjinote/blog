---
title: "傅立葉級數與傅立葉轉換：將任何複雜波形分解為正弦和餘弦之和"
description: "詳細解釋將複雜波形表示為簡單正弦波和餘弦波疊加的「傅立葉級數」，以及其向非週期函數擴展的「傅立葉轉換」。"
slug: "fourier-series-and-transform"
date: "2026-09-24T16:08:36+09:00"
image: "eyecatch.jpg"
categories:
  - "數學"
tags:
  - "傅立葉"
  - "數學"
  - "物理"
---

## 1. 簡介：波相加的魔法

我們的周圍充滿了各種 **「波」**，如聲音、光和電磁波。如果乍看之下非常複雜和不規則的波形實際上是由簡單的波組合而成的呢？這一驚人事實的數學表示就是約瑟夫·傅立葉提出的 **「傅立葉級數」**，以及其進一步的發展 **「傅立葉轉換」**。

在本文中，我們將深入探討這種迷人的數學方法，從其基礎到直觀的理解，以及在現代技術中的應用。

## 2. 傅立葉級數：分解週期波

傅立葉級數的基本思想是「任何週期函數都可以表示為具有不同頻率的正弦波和餘弦波的無限總和」。

### 2.1 實數形式的傅立葉級數

週期為 $2\pi$ 的函數 $f(x)$ 可以展開如下。

$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n \cos(nx) + b_n \sin(nx) \right)
$$

這裡，$a_0$、$a_n$ 和 $b_n$ 被稱為 **「傅立葉係數」**，它們表示每種波包含的強度。這些係數由以下積分計算。

$$
a_0 = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) dx \quad (\text{直流分量})
$$
$$
a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos(nx) dx \quad (\text{餘弦分量的權重})
$$
$$
b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin(nx) dx \quad (\text{正弦分量的權重})
$$

### 2.2 複數傅立葉級數

使用歐拉公式 $e^{i\theta} = \cos\theta + i\sin\theta$，傅立葉級數可以更優雅地寫成複指數函數的形式。

$$
f(x) = \sum_{n=-\infty}^{\infty} c_n e^{inx}
$$

$$
c_n = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(x) e^{-inx} dx \quad (\text{複傅立葉係數})
$$

複數形式作為通往後文所述的傅立葉轉換的橋樑，起著非常重要的作用。

## 3. 傅立葉轉換：向非週期函數的擴展

傅立葉級數只能應用於週期函數。然而，現實世界中的許多信號（如簡短的聲音或一次性脈衝信號）是非週期的。因此，透過考慮週期趨於無窮大（$T \to \infty$）的極限，推導出了 **「傅立葉轉換」**。

### 3.1 傅立葉轉換的定義

函數 $f(t)$ 的傅立葉轉換 $\mathcal{F}\{f(t)\}$ 和逆傅立葉轉換定義如下。

$$
F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt \quad (\text{從時域到頻域的轉換})
$$

$$
f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i\omega t} d\omega \quad (\text{從頻域到時域的逆轉換})
$$

這裡，$t$ 表示時間，$\omega$ 表示角頻率。$F(\omega)$ 是一個函數，指示原始信號 $f(t)$ 中包含了多少頻率為 $\omega$ 的分量（振幅和相位）。

### 3.2 信號處理流程

下圖展示了如何使用傅立葉轉換處理輸入信號。

```mermaid
flowchart LR
    A["輸入信號的時間波形"] -->|"傅立葉轉換"| B["頻譜"]
    B -->|"濾波處理"| C["處理後的頻譜"]
    C -->|"逆傅立葉轉換"| D["輸出信號的時間波形"]
    
    %% 節點樣式
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bbf,stroke:#333,stroke-width:2px
    style D fill:#f9f,stroke:#333,stroke-width:2px
```

## 4. 離散傅立葉轉換（DFT）和快速傅立葉轉換（FFT）

為了用電腦處理信號，連續時間和具有無限長度的積分必須被有限數量的離散資料點之和所取代。這就是 **離散傅立葉轉換（DFT）**。

$$
X_k = \sum_{n=0}^{N-1} x_n e^{-i \frac{2\pi}{N} k n} \quad \text{對於 } k = 0, 1, \dots, N-1
$$

此外，將此 DFT 的計算複雜度從 $O(N^2)$ 顯著降低到 $O(N \log N)$ 的演算法是 **快速傅立葉轉換（FFT）**。隨著 FFT 的出現，數位信號處理（DSP）領域經歷了爆炸性的發展。我們熟悉的許多技術，例如智慧型手機上的語音辨識和 JPEG 影像壓縮，都得益於 FFT。

```python
import numpy as np
import matplotlib.pyplot as plt

# 建立時間軸（從0到1秒，取樣頻率1000Hz）
t = np.linspace(0, 1, 1000, endpoint=False)

# 合成50Hz和120Hz正弦波的信號
signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

# 執行FFT
fft_result = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(t), 1/1000)

# 僅繪製正頻率域的索引
positive_freqs = frequencies > 0
```

## 5. 結論

傅立葉級數和傅立葉轉換是科學和工程中最強大的工具之一，將複雜的現象分解為簡單的元素。透過將時間轉換為頻率的這種數學「鏡頭」來看待世界，我們可以發現隱藏的模式並高效地處理資訊。

今天，波相加的魔法繼續作為現代技術的基礎發揮著積極作用。
