---
title: "Fourier Series and Fourier Transform: Understanding Waves Through Sine and Cosine Components"
description: "A detailed explanation of 'Fourier Series', which expresses complex waveforms as a superposition of simple sine and cosine waves, and its extension to non-periodic functions, the 'Fourier Transform'."
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

## 1. Introduction: Thinking in Terms of Waves

Sound, light, and electromagnetic waves surround us. Could even an apparently complicated waveform be understood as a combination of simple waves? **Fourier series**, associated with Joseph Fourier, and the **Fourier transform**, which uses a continuous range of frequencies, give a mathematical form to this idea. To use them correctly, we must specify conditions on the functions and what convergence means.

This article introduces the underlying ideas, the formulas, and an example connecting them to modern signal processing.

## 2. Fourier Series: Decomposing Periodic Waves

A Fourier series represents a periodic function using trigonometric components at integer multiples of a fundamental frequency. Being able to calculate coefficients does not by itself imply that the series converges to the original function at every point. Here we consider piecewise smooth periodic functions: one period can be divided into finitely many intervals on which the function is continuously differentiable, with finite one-sided limits of both the function and its derivative at the endpoints. Under this sufficient condition, the series converges to the function at continuity points and to the average of the one-sided limits at a jump.

$$
\lim_{M\to\infty} S_M(x)=\frac{f(x-)+f(x+)}{2}
$$

Here $S_M$ is the partial sum through the $M$th harmonic. At the join between periods, use the limits of the periodic extension. Near a jump, the overshoot known as the Gibbs phenomenon persists as more terms are added. Thus increasing the number of terms does not make the error tend uniformly to zero over the entire interval.

### 2.1 Real Fourier Series

For a real-valued function of period $2\pi$ satisfying the conditions above, the following equality holds at continuity points. Angles are in radians. At a jump, replace the left side by the average of the one-sided limits.

$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n \cos(nx) + b_n \sin(nx) \right)
$$

The numbers $a_0,a_n,b_n$ are **Fourier coefficients**. The constant term, or DC component, is the mean over one period, $a_0/2$, rather than $a_0$. For $n\ge1$, $a_n$ and $b_n$ are the weights of the cosine and sine components. Orthogonality of the trigonometric functions gives the coefficient formulas:

$$
a_0 = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) dx
$$

$$
a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos(nx) dx
$$

$$
b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin(nx) dx
$$

### 2.2 Complex Fourier Series

Using [Euler's formula](/en/p/eulers-identity/), $e^{i\theta}=\cos\theta+i\sin\theta$, we can express the same series using complex exponentials. Interpret the two-sided sum below as the limit of symmetric partial sums from $n=-M$ to $M$. The equality at continuity points and the qualification at jumps are the same as for the real form.

$$
f(x) = \sum_{n=-\infty}^{\infty} c_n e^{inx}
$$

$$
c_n = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(x) e^{-inx} dx
$$

For real-valued $f$, we have $c_0=a_0/2$, $c_n=(a_n-ib_n)/2$ and $c_{-n}=(a_n+ib_n)/2$ for $n\ge1$. Negative frequencies appear even when representing a real waveform with complex exponentials. The complex form also makes the connection to the Fourier transform easier to see.

## 3. Fourier Transform: Beyond Periodic Functions

Fourier series can be applied to periodically extended functions. To describe a single pulse or another signal on the whole real line, however, a **Fourier transform** with continuously varying frequency is useful. Increasing the period so that the frequency spacing becomes smaller gives an intuitive connection. Interchanging limits and integrals requires conditions, so this intuition alone is not a general proof.

### 3.1 Definition and Inversion

We use a minus sign in the forward transform's exponent and a factor $1/(2\pi)$ in the inverse transform. If $\int_{-\infty}^{\infty}|f(t)|\,dt<\infty$, the forward transform below converges absolutely for every real $\omega$.

$$
F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt
$$

For example, if $f$ is continuous and both $f$ and $F$ are absolutely integrable, the inverse transform recovers $f$ as follows. This formula cannot be applied to an arbitrary function without conditions.

$$
f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i\omega t} d\omega
$$

Take $t$ in seconds and $\omega$ as angular frequency in radians per second. Ordinary frequency $\nu$ in hertz is related by $\omega=2\pi\nu$. The complex-valued $F(\omega)$ describes the weights of a continuous spectrum; where $F\ne0$, its modulus and argument describe magnitude and phase. A weight in a continuous spectrum is not directly the amplitude of a single component of a periodic signal.

For functions with jumps, additional regularity and a symmetric improper integral can give the average of the one-sided limits instead. Square-integrable functions and periodic signals may require extensions in $L^2$ and in the sense of distributions, respectively. Those theories are outside this introduction. Signs and normalizations vary between references, so always check the forward and inverse transforms as a pair.

### 3.2 Signal Processing Flow

This diagram illustrates processing an input signal in the frequency domain.

```mermaid
flowchart LR
    A["Input signal in time"] -->|"Fourier transform"| B["Frequency spectrum"]
    B -->|"Filtering"| C["Modified spectrum"]
    C -->|"Inverse Fourier transform"| D["Output signal in time"]

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bbf,stroke:#333,stroke-width:2px
    style D fill:#f9f,stroke:#333,stroke-width:2px
```

## 4. Discrete Fourier Transform (DFT) and Fast Fourier Transform (FFT)

The **discrete Fourier transform (DFT)** maps a finite sequence $x_0,\ldots,x_{N-1}$ to the same number of frequency components. Distinguish this finite transform from simply replacing an integral in the continuous Fourier transform. For a time signal, sampling and selecting a finite observation interval come first. The forward and inverse DFT form the pair:

$$
X_k = \sum_{n=0}^{N-1} x_n e^{-i \frac{2\pi}{N} k n} \quad \text{for } k = 0, 1, \dots, N-1
$$

$$
x_n=\frac{1}{N}\sum_{k=0}^{N-1}X_k e^{i\frac{2\pi}{N}kn} \quad \text{for } n=0,1,\dots,N-1
$$

For a sampling rate $f_s$, frequency bins are spaced $f_s/N$ Hz apart. The DFT corresponds to viewing the finite sequence as periodically repeated. Components at or above $f_s/2$ in the signal before sampling cause aliasing or ambiguity, so recovering a continuous signal requires assumptions such as band limitation. A sinusoid that does not complete an integer number of cycles within the observation interval also produces spectral leakage: its energy spreads over multiple bins.

Evaluating all $N$ DFT components directly requires $O(N^2)$ operations. The [fast Fourier transform (FFT)](/en/p/fast-fourier-transform-algorithm/) is a family of algorithms for computing the same DFT efficiently. For example, a divide-and-conquer algorithm for a power-of-two length needs $O(N\log N)$ operations. FFT denotes a method of computation, not a different transform or an approximation in itself. It is widely used in digital signal processing, including audio. The baseline method of ordinary lossy JPEG compression, however, uses a discrete cosine transform (DCT). These transforms are related, but JPEG should not simply be presented as a direct use of FFT.

### 4.1 Checking Two Frequencies and Their Amplitudes in Python

This example uses NumPy and Matplotlib. We sample one second at 1,000 Hz and combine a 50 Hz sinusoid of amplitude 1 with a 120 Hz sinusoid of amplitude 0.5. Because the input is real, we use `rfft` and `rfftfreq`. Both frequencies match bins spaced 1 Hz apart and are below 500 Hz.

```python
import numpy as np
import matplotlib.pyplot as plt

# Sample one second at 1000 Hz; exclude the endpoint at one second
fs = 1000.0
N = 1000
t = np.arange(N) / fs
signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

# Nonnegative-frequency DFT for real input
fft_result = np.fft.rfft(signal)
frequencies = np.fft.rfftfreq(N, d=1 / fs)

# One-sided amplitude: do not double DC or the even-length Nyquist bin
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

Rounded output is `50 Hz: 1.000` and `120 Hz: 0.500`. The default forward `rfft` is not divided by $N$, so we normalize as shown to display amplitudes. Combining the positive- and negative-frequency pair of a real signal requires doubling only interior bins, excluding DC and, for even lengths, the Nyquist component. This reads the amplitudes of the unwindowed, bin-centered sinusoids in this example. The same formula alone does not guarantee exact amplitude estimates for arbitrary signals or windowed data.

## 5. Conclusion

Fourier series and Fourier transforms help break complicated phenomena into simpler components. Viewing a signal in the frequency domain can reveal patterns and enable useful processing.

Specify periodicity, convergence conditions, frequency units, and normalization. Distinguishing the DFT from its FFT algorithms also makes the connection between the mathematics and practical programs clearer.

## References

- [MIT ES.1803 Topic 22: coefficients, convergence, Gibbs phenomenon and orthogonality (§22.5–22.7)](https://ocw.mit.edu/courses/es-1803-differential-equations-spring-2024/mites_1803_s24_topic22.pdf)
- [MIT 18.330: Fourier transform and inversion (Chapter 6, Definition 14)](https://math.mit.edu/icg/resources/teaching/18.330/18.330-Apr29.pdf)
- [NIST DLMF §1.14(i): transform and inversion conditions; its signs and normalization differ from ours](https://dlmf.nist.gov/1.14#i)
- [MIT 6.341 Lecture 19: DFT and FFT operation counts](https://ocw.mit.edu/courses/6-341-discrete-time-signal-processing-fall-2005/4ee39a5e74c9f5099ac516ce57215c96_lec19.pdf)
- [NumPy 2.3: FFT](https://numpy.org/doc/2.3/reference/generated/numpy.fft.fft.html), [rfft for real input](https://numpy.org/doc/2.3/reference/generated/numpy.fft.rfft.html), and [rfftfreq frequency bins](https://numpy.org/doc/2.3/reference/generated/numpy.fft.rfftfreq.html)
- [ITU-T T.81: JPEG lossy DCT processes (§4.2–4.3)](https://www.w3.org/Graphics/JPEG/itu-t81.pdf)
