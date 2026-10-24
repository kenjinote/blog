---
title: "傅立葉級數與傅立葉轉換：用正弦與餘弦成分理解波形"
description: "詳細解釋將複雜波形表示為簡單正弦波和餘弦波疊加的「傅立葉級數」，以及其向非週期函數擴展的「傅立葉轉換」。"
slug: "fourier-series-and-transform"
date: "2026-09-20T14:30:00+09:00"
lastmod: 2026-10-24
image: "eyecatch.jpg"
categories: ["mathematics"]
tags:
  - "傅立葉"
  - "數學"
  - "物理"
---

## 1. 引言：從波的疊加來思考

聲音、光、電磁波等各種**波**存在於我們周圍。看起來複雜而不規則的波形，能否理解為簡單波形的組合？與約瑟夫·傅立葉相關的**傅立葉級數**，以及使用連續頻率的**傅立葉轉換**，為這種想法提供了數學表達。不過，使用時需要說明函數滿足的條件，以及收斂的意義。

本文從基本公式與直觀理解出發，介紹它們在現代訊號處理中的應用。

## 2. 傅立葉級數：分解週期波形

傅立葉級數以頻率為基本頻率整數倍的三角函數成分來表示週期函數。能夠算出係數，並不代表級數在每一點都收斂到原函數的值。這裡考慮分段光滑的週期函數：一個週期可以分成有限個區間，函數在各區間內部連續可微，而且函數及其導函數在端點都有有限的單側極限。在這個充分條件下，級數在連續點收斂到原函數的值，在跳躍不連續點則收斂到左右極限的平均值。

$$
\lim_{M\to\infty} S_M(x)=\frac{f(x-)+f(x+)}{2}
$$

$S_M$ 表示保留到第 $M$ 次諧波的部分和。在兩個週期的接合處，也要使用週期延拓後的左右極限。跳躍附近會出現吉布斯現象造成的過衝；增加項數時，這種過衝並不會消失。因此，不能認為增加項數就會使整個區間的誤差一致趨近於零。

### 2.1 實數形式的傅立葉級數

對於滿足上述條件、週期為 $2\pi$ 的實值函數，下列等式在連續點成立。角度以弧度表示。在跳躍不連續點，左邊應改為左右極限的平均值。

$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n \cos(nx) + b_n \sin(nx) \right)
$$

$a_0,a_n,b_n$ 稱為**傅立葉係數**。常數項，也就是直流成分與一個週期的平均值，是 $a_0/2$，而不是 $a_0$。對於 $n\ge1$，$a_n,b_n$ 分別是餘弦與正弦的權重。利用三角函數的正交性，可以得到下列係數公式。

$$
a_0 = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) dx
$$

$$
a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos(nx) dx
$$

$$
b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin(nx) dx
$$

### 2.2 複數形式的傅立葉級數

利用[尤拉公式](/zh-tw/p/eulers-identity/) $e^{i\theta}=\cos\theta+i\sin\theta$，同一個級數可以寫成複指數函數的形式。下列雙邊求和，應理解為從 $n=-M$ 到 $M$ 的對稱部分和之極限。連續點的等式與跳躍處的注意事項和實數形式相同。

$$
f(x) = \sum_{n=-\infty}^{\infty} c_n e^{inx}
$$

$$
c_n = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(x) e^{-inx} dx
$$

當 $f$ 為實值函數時，$c_0=a_0/2$，$c_n=(a_n-ib_n)/2$，$c_{-n}=(a_n+ib_n)/2$（$n\ge1$）。所以，即使原波形是實值的，以複指數函數表示時也會出現負頻率。複數形式也讓級數與傅立葉轉換的聯繫更容易理解。

## 3. 傅立葉轉換：擴展到非週期函數

傅立葉級數也可以用於週期延拓後的函數。但若要在整個實數軸上描述單一脈衝等訊號，具有連續頻率的**傅立葉轉換**就很合適。逐漸拉長週期，使頻率間隔縮小，能提供直觀的聯繫。不過，交換極限與積分需要滿足條件，這種直觀說明本身並不是一般性的證明。

### 3.1 定義與反轉換

本文採用正轉換指數帶負號、反轉換乘上 $1/(2\pi)$ 的慣例。若 $\int_{-\infty}^{\infty}|f(t)|\,dt<\infty$，下列正轉換對所有實數 $\omega$ 都絕對收斂。

$$
F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt
$$

例如，若 $f$ 連續，而且 $f$ 與 $F$ 都絕對可積，就可以用下列反轉換還原 $f$。不能對任意函數無條件套用這個公式。

$$
f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i\omega t} d\omega
$$

這裡取 $t$ 的單位為秒，$\omega$ 為角頻率，單位是 rad/s。以 Hz 表示的頻率 $\nu$ 與它的關係為 $\omega=2\pi\nu$。複值函數 $F(\omega)$ 表示連續頻譜中的權重；在 $F\ne0$ 處，可以由絕對值與幅角讀取大小及相位。連續頻譜的權重，不能直接等同於週期訊號中單一成分的振幅。

對於有跳躍的函數，在附加的正則性條件下，以對稱的瑕積分處理，有時可以還原左右極限的平均值。平方可積函數與週期訊號，則可能分別需要 $L^2$ 意義與廣義函數意義下的擴展。本文不展開這些理論。不同文獻可能使用不同的符號與正規化慣例，因此應把正轉換和反轉換配對核對。

### 3.2 訊號處理流程

下圖展示了在頻域處理輸入訊號的流程。

```mermaid
flowchart LR
    A["輸入訊號的時間波形"] -->|"傅立葉轉換"| B["頻譜"]
    B -->|"濾波處理"| C["處理後的頻譜"]
    C -->|"反傅立葉轉換"| D["輸出訊號的時間波形"]

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bbf,stroke:#333,stroke-width:2px
    style D fill:#f9f,stroke:#333,stroke-width:2px
```

## 4. 離散傅立葉轉換（DFT）與快速傅立葉轉換（FFT）

**離散傅立葉轉換（DFT）**將有限序列 $x_0,\ldots,x_{N-1}$ 映射為相同數量的頻率成分。它和單純把連續傅立葉轉換的積分換成有限和並不相同。處理時間訊號時，應先取樣，並截取有限的觀測時間。正轉換與反轉換成對如下：

$$
X_k = \sum_{n=0}^{N-1} x_n e^{-i \frac{2\pi}{N} k n} \quad \text{for } k = 0, 1, \dots, N-1
$$

$$
x_n=\frac{1}{N}\sum_{k=0}^{N-1}X_k e^{i\frac{2\pi}{N}kn} \quad \text{for } n=0,1,\dots,N-1
$$

若取樣頻率為 $f_s$，頻率格點（bin）的間隔就是 $f_s/N$ Hz。DFT對應於將有限序列週期重複的觀點。取樣前的訊號若含有 $f_s/2$ 或更高頻率的成分，就會發生混疊或歧義問題；要還原連續訊號，需要帶限等假設。若正弦波在觀測區間內未恰好完成整數個週期，也會有頻譜洩漏，能量散布到多個頻率格點。

依照定義直接計算全部 $N$ 個DFT成分，需要 $O(N^2)$ 次運算。[快速傅立葉轉換（FFT）](/zh-tw/p/fast-fourier-transform-algorithm/)是有效率地計算相同DFT的一類演算法。例如，當長度是2的冪次時，可以用分治法達到 $O(N\log N)$。FFT並不是另一種轉換，也不代表它本身是一種近似。它廣泛應用於音訊等數位訊號處理。另一方面，一般有損JPEG的基本編碼方式採用離散餘弦轉換（DCT）。這些轉換雖然相關，卻不應直接把JPEG當作使用FFT的例子。

### 4.1 用Python檢查兩種頻率及其振幅

下例使用NumPy與Matplotlib，以1,000 Hz取樣1秒，合成50 Hz、振幅1與120 Hz、振幅0.5的正弦波。輸入為實數，因此採用 `rfft` 和 `rfftfreq`。兩種頻率都對齊間隔1 Hz的頻率格點，且都低於500 Hz。

```python
import numpy as np
import matplotlib.pyplot as plt

# 以1000 Hz取樣1秒，不包含終點1秒
fs = 1000.0
N = 1000
t = np.arange(N) / fs
signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

# 實數訊號非負頻率部分的DFT
fft_result = np.fft.rfft(signal)
frequencies = np.fft.rfftfreq(N, d=1 / fs)

# 單邊振幅：直流成分與偶數長度的奈奎斯特成分不乘以2
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

輸出四捨五入後為 `50 Hz: 1.000` 與 `120 Hz: 0.500`。`rfft` 預設的正轉換未除以 $N$，所以顯示振幅時使用上述正規化。將實數訊號的正負頻率成對合併時，只把內部格點乘以2，不包含直流成分，以及偶數長度時的奈奎斯特成分。這是在本例中讀取未加窗、對齊格點之正弦波振幅的方法。對於任意訊號或加窗後的資料，不能只靠同一個公式就保證得到準確的振幅。

## 5. 結語

傅立葉級數與傅立葉轉換可以幫助我們將複雜現象分解為簡單成分。從頻域觀察訊號，能發現隱藏的模式並進行有效處理。

使用時應指定週期性、收斂條件、頻率單位與正規化慣例。區分DFT和計算它的FFT演算法，也能使數學公式與實際程式的聯繫更加清楚。

## 參考資料

- [MIT ES.1803 Topic 22：係數、收斂、吉布斯現象與正交性（§22.5–22.7）](https://ocw.mit.edu/courses/es-1803-differential-equations-spring-2024/mites_1803_s24_topic22.pdf)
- [MIT 18.330：傅立葉轉換與反轉換（第6章，Definition 14）](https://math.mit.edu/icg/resources/teaching/18.330/18.330-Apr29.pdf)
- [NIST DLMF §1.14(i)：定義與反演條件；符號和正規化與本文不同](https://dlmf.nist.gov/1.14#i)
- [MIT 6.341 Lecture 19：DFT與FFT的運算量](https://ocw.mit.edu/courses/6-341-discrete-time-signal-processing-fall-2005/4ee39a5e74c9f5099ac516ce57215c96_lec19.pdf)
- [NumPy 2.3：FFT](https://numpy.org/doc/2.3/reference/generated/numpy.fft.fft.html)、[實數輸入的rfft](https://numpy.org/doc/2.3/reference/generated/numpy.fft.rfft.html)、[頻率格點的rfftfreq](https://numpy.org/doc/2.3/reference/generated/numpy.fft.rfftfreq.html)
- [ITU-T T.81：JPEG有損DCT方式（§4.2–4.3）](https://www.w3.org/Graphics/JPEG/itu-t81.pdf)
