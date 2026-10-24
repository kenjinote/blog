---
title: "푸리에 급수와 푸리에 변환: 사인과 코사인 성분으로 파동 이해하기"
description: "복잡한 파형을 단순한 사인파와 코사인파의 중첩으로 표현하는 '푸리에 급수'와 이를 비주기 함수로 확장한 '푸리에 변환'에 대해 자세히 설명합니다."
slug: "fourier-series-and-transform"
date: "2026-09-20T14:30:00+09:00"
lastmod: 2026-10-24
image: "eyecatch.jpg"
categories: ["mathematics"]
tags:
  - "푸리에"
  - "수학"
  - "물리학"
---

## 1. 들어가며: 파동의 합으로 생각하기

우리 주변에는 소리, 빛, 전자기파 등 여러 **파동**이 있습니다. 복잡하고 불규칙해 보이는 파형도 단순한 파동의 조합으로 이해할 수 있을까요? 조제프 푸리에와 관련된 **푸리에 급수**와 연속적인 주파수를 다루는 **푸리에 변환**은 이 생각을 수학으로 표현합니다. 다만 함수를 다룰 조건과 수렴의 의미를 지정해야 합니다.

이 글에서는 기본 공식과 직관적인 해석, 현대 신호 처리에 활용하는 예제를 설명합니다.

## 2. 푸리에 급수: 주기적인 파동 분해하기

푸리에 급수는 기본 주파수의 정수배 주파수를 가진 삼각함수 성분으로 주기함수를 나타내는 방법입니다. 계수를 계산할 수 있다는 사실만으로 급수가 모든 점에서 원래 함수값에 수렴하는 것은 아닙니다. 여기서는 조각별로 매끄러운 주기함수를 생각합니다. 한 주기를 유한 개의 구간으로 나눌 수 있고, 각 구간 내부에서 함수가 연속 미분 가능하며, 구간 끝에서 함수와 도함수가 유한한 좌극한과 우극한을 갖는 경우입니다. 이 충분조건 아래에서 급수는 연속점에서는 원래 함수값에, 도약 불연속점에서는 좌우 극한의 평균에 수렴합니다.

$$
\lim_{M\to\infty} S_M(x)=\frac{f(x-)+f(x+)}{2}
$$

$S_M$은 제 $M$ 고조파까지의 부분합입니다. 주기와 주기가 이어지는 곳에서도 주기적으로 확장한 함수의 좌우 극한을 사용합니다. 도약 부근에는 깁스 현상에 따른 오버슈트가 남습니다. 따라서 항 수를 늘린다고 해서 전체 구간의 오차가 균등하게 0으로 수렴하는 것은 아닙니다.

### 2.1 실수 형태의 푸리에 급수

위 조건을 만족하고 주기가 $2\pi$인 실숫값 함수에서는 다음 등식이 연속점에서 성립합니다. 각도는 라디안으로 나타냅니다. 도약 불연속점에서는 왼쪽을 좌우 극한의 평균으로 바꾸어 읽습니다.

$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n \cos(nx) + b_n \sin(nx) \right)
$$

$a_0,a_n,b_n$은 **푸리에 계수**입니다. 상수항, 즉 직류 성분이자 한 주기의 평균은 $a_0/2$이며 $a_0$ 자체가 아닙니다. $n\ge1$에서 $a_n,b_n$은 각각 코사인 성분과 사인 성분의 가중치입니다. 삼각함수의 직교성을 이용하면 다음 계수 공식을 얻습니다.

$$
a_0 = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) dx
$$

$$
a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos(nx) dx
$$

$$
b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin(nx) dx
$$

### 2.2 복소 형태의 푸리에 급수

[오일러 공식](/ko/p/eulers-identity/) $e^{i\theta}=\cos\theta+i\sin\theta$를 이용하면 같은 급수를 복소지수함수로 나타낼 수 있습니다. 다음 양방향 합은 $n=-M$부터 $M$까지의 대칭 부분합의 극한으로 해석합니다. 연속점의 등식과 도약점에서의 주의사항은 실수 형태와 같습니다.

$$
f(x) = \sum_{n=-\infty}^{\infty} c_n e^{inx}
$$

$$
c_n = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(x) e^{-inx} dx
$$

$f$가 실숫값 함수이면 $c_0=a_0/2$, $c_n=(a_n-ib_n)/2$, $c_{-n}=(a_n+ib_n)/2$입니다($n\ge1$). 실수 파형을 복소지수함수로 표현할 때도 음의 주파수가 나타납니다. 복소 형태는 푸리에 변환과의 관계를 이해하는 데도 도움이 됩니다.

## 3. 푸리에 변환: 비주기 함수로의 확장

푸리에 급수는 주기적으로 확장한 함수에도 사용할 수 있습니다. 하지만 하나의 펄스와 같은 신호를 실수축 전체에서 다루려면 주파수가 연속적으로 변하는 **푸리에 변환**이 적합합니다. 주기를 길게 하여 주파수 간격을 좁히는 생각은 직관적인 연결을 제공합니다. 다만 극한과 적분을 교환하려면 조건이 필요하므로, 이 직관만으로 일반적인 증명이 되지는 않습니다.

### 3.1 정의와 역변환

이 글에서는 순변환 지수에 음의 부호를 쓰고 역변환에는 $1/(2\pi)$를 곱하는 규약을 사용합니다. $\int_{-\infty}^{\infty}|f(t)|\,dt<\infty$이면 다음 순변환은 모든 실수 $\omega$에서 절대수렴합니다.

$$
F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt
$$

예를 들어 $f$가 연속이고 $f$와 $F$가 모두 절대적분 가능하면, 다음 역변환으로 $f$를 복원할 수 있습니다. 이 공식을 임의의 함수에 조건 없이 적용할 수는 없습니다.

$$
f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i\omega t} d\omega
$$

여기서는 $t$의 단위를 초로, $\omega$를 각주파수로 두며 단위는 rad/s입니다. Hz로 나타낸 주파수 $\nu$와는 $\omega=2\pi\nu$의 관계가 있습니다. 복솟값 함수 $F(\omega)$는 연속 스펙트럼의 가중치를 나타내고, $F\ne0$인 곳에서는 절댓값과 편각으로 크기와 위상을 읽을 수 있습니다. 연속 스펙트럼의 가중치를 주기신호의 단일 성분 진폭과 그대로 동일시해서는 안 됩니다.

도약이 있는 함수에서는 추가적인 정칙성 조건과 대칭적인 이상적분을 통해 좌우 극한의 평균을 복원하는 경우도 있습니다. 제곱적분 가능 함수와 주기신호는 각각 $L^2$의 의미와 분포의 의미에서 확장이 필요할 수 있습니다. 이 글에서는 그 이론까지 다루지 않습니다. 문헌에 따라 부호와 정규화 규약이 다르므로 순변환과 역변환을 한 쌍으로 확인해야 합니다.

### 3.2 신호 처리의 흐름

다음 그림은 입력 신호를 주파수 영역에서 처리하는 흐름입니다.

```mermaid
flowchart LR
    A["입력 신호의 시간 파형"] -->|"푸리에 변환"| B["주파수 스펙트럼"]
    B -->|"필터링"| C["수정된 스펙트럼"]
    C -->|"역푸리에 변환"| D["출력 신호의 시간 파형"]

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bbf,stroke:#333,stroke-width:2px
    style D fill:#f9f,stroke:#333,stroke-width:2px
```

## 4. 이산 푸리에 변환(DFT)과 고속 푸리에 변환(FFT)

**이산 푸리에 변환(DFT)**은 유한한 수열 $x_0,\ldots,x_{N-1}$을 같은 개수의 주파수 성분으로 옮기는 변환입니다. 연속 푸리에 변환의 적분을 단순히 유한합으로 바꾸는 설명과는 구분해야 합니다. 시간 신호를 다룰 때는 먼저 표본화하고 유한한 관측 구간을 선택합니다. 순변환과 역변환은 다음 한 쌍입니다.

$$
X_k = \sum_{n=0}^{N-1} x_n e^{-i \frac{2\pi}{N} k n} \quad \text{for } k = 0, 1, \dots, N-1
$$

$$
x_n=\frac{1}{N}\sum_{k=0}^{N-1}X_k e^{i\frac{2\pi}{N}kn} \quad \text{for } n=0,1,\dots,N-1
$$

표본화 주파수를 $f_s$라고 하면 주파수 빈(bin) 사이의 간격은 $f_s/N$ Hz입니다. DFT는 유한 수열을 주기적으로 반복한다고 보는 관점에 대응합니다. 표본화 전의 신호에 $f_s/2$ 이상의 주파수 성분이 있으면 에일리어싱 또는 모호성 문제가 생기므로, 연속 신호를 복원하려면 대역 제한 등의 가정이 필요합니다. 관측 구간 안에 정수 개의 주기가 들어맞지 않는 정현파에서는 에너지가 여러 빈으로 퍼지는 스펙트럼 누설도 발생합니다.

DFT의 $N$개 성분을 정의대로 직접 계산하면 $O(N^2)$번의 연산이 필요합니다. [고속 푸리에 변환(FFT)](/ko/p/fast-fourier-transform-algorithm/)은 같은 DFT를 효율적으로 계산하는 알고리즘의 총칭입니다. 예를 들어 길이가 2의 거듭제곱이면 분할 정복으로 $O(N\log N)$에 계산할 수 있습니다. FFT는 다른 변환이거나 그 자체로 근사를 뜻하는 명칭이 아닙니다. 오디오 등 디지털 신호 처리에 널리 쓰입니다. 한편, 일반적인 손실 JPEG의 기본 방식은 이산 코사인 변환(DCT)을 사용합니다. 관련된 변환이라 해도 JPEG를 곧바로 FFT의 사용 사례로 설명해서는 안 됩니다.

### 4.1 Python으로 두 주파수와 진폭 확인하기

다음 예제는 NumPy와 Matplotlib을 사용합니다. 1초 동안 1,000 Hz로 표본화하고, 주파수 50 Hz·진폭 1인 정현파와 주파수 120 Hz·진폭 0.5인 정현파를 합성합니다. 실수 입력이므로 `rfft`와 `rfftfreq`를 사용합니다. 두 주파수 모두 1 Hz 간격의 빈에 정확히 대응하고 500 Hz보다 낮습니다.

```python
import numpy as np
import matplotlib.pyplot as plt

# 1초 동안 1000 Hz로 표본화하며 끝점 1초는 포함하지 않는다
fs = 1000.0
N = 1000
t = np.arange(N) / fs
signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

# 실수 신호의 음이 아닌 주파수 쪽 DFT
fft_result = np.fft.rfft(signal)
frequencies = np.fft.rfftfreq(N, d=1 / fs)

# 단측 진폭: 직류와 짝수 길이의 나이퀴스트 성분은 2배로 하지 않는다
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

반올림한 출력은 `50 Hz: 1.000`과 `120 Hz: 0.500`입니다. `rfft`의 기본 순변환은 $N$으로 나누지 않으므로 진폭을 표시할 때 위와 같이 정규화합니다. 실수 신호의 양·음 주파수 쌍을 합치기 위해 내부 빈만 2배로 하고, 직류와 짝수 길이의 나이퀴스트 성분은 제외합니다. 이는 이 예제처럼 창 함수를 적용하지 않고 빈에 맞춘 정현파의 진폭을 읽는 방법입니다. 임의의 신호나 창 함수를 적용한 데이터에서 같은 공식만으로 정확한 진폭을 보장할 수는 없습니다.

## 5. 맺음말

푸리에 급수와 푸리에 변환은 복잡한 현상을 간단한 성분으로 나누어 이해하게 해 줍니다. 신호를 주파수 영역에서 보면 숨겨진 패턴을 발견하고 정보를 효과적으로 처리할 수 있습니다.

주기성, 수렴 조건, 주파수 단위와 정규화 규약을 지정하는 것이 중요합니다. DFT와 이를 계산하는 FFT 알고리즘을 구분하면 수학 공식과 실제 프로그램의 관계도 명확해집니다.

## 참고 자료

- [MIT ES.1803 Topic 22: 계수, 수렴, 깁스 현상과 직교성(§22.5–22.7)](https://ocw.mit.edu/courses/es-1803-differential-equations-spring-2024/mites_1803_s24_topic22.pdf)
- [MIT 18.330: 푸리에 변환과 역변환(6장, Definition 14)](https://math.mit.edu/icg/resources/teaching/18.330/18.330-Apr29.pdf)
- [NIST DLMF §1.14(i): 정의와 역변환 조건. 부호와 정규화는 이 글과 다름](https://dlmf.nist.gov/1.14#i)
- [MIT 6.341 Lecture 19: DFT와 FFT의 연산량](https://ocw.mit.edu/courses/6-341-discrete-time-signal-processing-fall-2005/4ee39a5e74c9f5099ac516ce57215c96_lec19.pdf)
- [NumPy 2.3: FFT](https://numpy.org/doc/2.3/reference/generated/numpy.fft.fft.html), [실수 입력용 rfft](https://numpy.org/doc/2.3/reference/generated/numpy.fft.rfft.html), [rfftfreq의 주파수 빈](https://numpy.org/doc/2.3/reference/generated/numpy.fft.rfftfreq.html)
- [ITU-T T.81: JPEG의 손실 DCT 방식(§4.2–4.3)](https://www.w3.org/Graphics/JPEG/itu-t81.pdf)
