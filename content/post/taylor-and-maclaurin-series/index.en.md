---
title: "Taylor and Maclaurin Series: The Magic of Approximating Complex Functions with Polynomials"
description: "A detailed explanation of Taylor and Maclaurin series, the secrets of calculus, from intuitive meanings to mathematical derivations and applications in programming and physics."
slug: "taylor-and-maclaurin-series"
date: "2026-09-20T14:30:00+09:00"
lastmod: 2026-10-24
image: "eyecatch.jpg"
categories: ["mathematics"]
tags:
  - "Calculus"
  - "Taylor Series"
  - "Maclaurin Series"
  - "Function Approximation"
---

## Introduction

A **Taylor polynomial** approximates a function near a point by matching its value and a finite number of derivatives there. Extending these derivative coefficients to an infinite sum gives the **Taylor series**; when the center is zero, it is called the **Maclaurin series**. Convergence of the series and equality of its sum to the original function are separate questions.

Using exponential and trigonometric functions as examples, we will explain how to determine the coefficients, when the resulting equalities hold, and how to bound the error from truncating the series. A short Python example illustrates approximating $\sin x$ near zero.

## Why Approximate Functions with Polynomials?

To begin with, why is it necessary to represent a function as a polynomial ( $a + bx + cx^2 + \dots$ )?

```mermaid
flowchart LR
    A["Function analytic near the center"] -->|"Taylor expansion within its convergence range"| B["Power series"]
    B -->|"Truncate at finite terms"| C["Polynomial approximation"]
    C -->|"Basic arithmetic only"| D["High-speed computer calculation"]
```

Approximating a nonlinear function with a polynomial can simplify evaluation, differentiation, and integration. Once its coefficients are known, a polynomial can be evaluated with addition and multiplication. The remainder and numerical errors determine where the approximation is useful and how accurate it is.

## Intuitive Understanding of Maclaurin Series

First, let's consider the **Maclaurin series**, which approximates a function around a specific point $x = 0$.
Suppose $f$ has the required derivatives near zero. Choose a finite degree $n$ and determine the coefficients of the polynomial $P_n$:

$$ P_n(x) = c_0 + c_1 x + c_2 x^2 + \dots + c_n x^n $$

Match the function value and derivatives at zero. The second-derivative condition below applies when $n\ge2$.

1. **Value condition**: $P_n(0)=f(0)$ gives $c_0=f(0)$. The constant term matches the function value at zero.
2. **First-derivative condition**: $P_n'(0)=f'(0)$ gives $c_1=f'(0)$. The first-degree polynomial $P_1(x)=f(0)+f'(0)x$ is the tangent-line approximation at zero.
3. **Second-derivative condition**: Require $P_n''(0)=f''(0)$. Since $P_n''(0)=2c_2$, we obtain $c_2=f''(0)/2!$. When higher-degree terms are present, the full derivative $P_n''(x)$ is not generally the constant $2c_2$.
4. **General condition**: For $k\le n$, requiring $P_n^{(k)}(0)=f^{(k)}(0)$ gives $c_k=f^{(k)}(0)/k!$. The remainder discussed below bounds the error near the center.

## Formula and Derivation of Maclaurin Series

If $f$ is infinitely differentiable, these coefficients define its Maclaurin series. To write an equality with $f(x)$ as below, the series must converge to $f(x)$ at the point in question. This holds in a suitable neighborhood of zero when $f$ is analytic there. Infinite differentiability alone is not sufficient.

$$ f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f^{(3)}(0)}{3!}x^3 + \dots $$

Written using sigma notation, it looks like this:

$$ f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!} x^n $$

Here, $f^{(n)}(0)$ is the value obtained by differentiating the function $f(x)$ $n$ times and substituting $x=0$, and $n!$ represents the factorial of $n$ ( $n \times (n-1) \times \dots \times 1$ ).

## Maclaurin Series of Typical Functions

The following exponential, sine, and cosine series converge to their respective functions for every real $x$. Trigonometric arguments are measured in radians.

### 1. Exponential function $e^x$

The exponential function $f(x) = e^x$ remains $e^x$ no matter how many times it is differentiated. Therefore, when $x=0$ is substituted, the derivative coefficients of all orders become $1$ ( $f^{(n)}(0) = 1$ ).

$$ e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots = \sum_{n=0}^{\infty} \frac{x^n}{n!} $$

### 2. Trigonometric functions $\sin x$ and $\cos x$

When $\sin x$ is repeatedly differentiated, it changes cyclically: $\cos x, -\sin x, -\cos x, \sin x, \dots$. By substituting $x=0$, only the derivative coefficients of odd orders remain, and the even orders become $0$.

$$ \sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} x^{2n+1} $$

Similarly, for $\cos x$, only the terms of even orders remain.

$$ \cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \dots = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n)!} x^{2n} $$

## Extension to Taylor Series

Moving the center from zero to $a$ gives the Taylor series. If $f$ is analytic near $a$, the following equality holds where the series represents $f$. Approximation assuming only finitely many derivatives uses a finite Taylor polynomial and a remainder, as discussed below.

$$ f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \dots = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x-a)^n $$

This formula demonstrates its power when you want to predict the value of a function at a location slightly away from $x=a$ ( $x = a + \Delta x$ ).

## Applications of Taylor Series

### Linear Approximation in Physics

Linear approximation with Taylor polynomials is common in physics. For a pendulum, measure the angle $\theta$ in radians and assume $|\theta|\ll1$. The first-degree approximation to sine is:

$$ \sin \theta \approx \theta \quad (\text{when } \theta \text{ is sufficiently small}) $$

This linearizes the pendulum equation and gives a period independent of amplitude within the small-amplitude approximation. The actual period of a simple pendulum depends on amplitude; the same approximation does not apply to large oscillations.

### Programming and Numerical Computation

Numerical evaluation of functions uses various methods, including polynomial approximation. CPython's `math` module mostly wraps the platform's C mathematics library, and the algorithms depend on that implementation. The following educational example sums a few terms near zero, for example for $|x|\le1$; it does not reproduce the standard library's implementation.

```python
import math

def approx_sin(x, terms=10):
    """
    Educational finite Maclaurin sum for sin(x) near zero
    x: Angle in radians
    terms: Number of terms to add (a positive integer; 10 in this example)
    """
    result = 0.0
    for n in range(terms):
        # Calculate each term: (-1)^n * x^(2n+1) / (2n+1)!
        sign = (-1) ** n
        numerator = x ** (2 * n + 1)
        denominator = math.factorial(2 * n + 1)
        result += sign * (numerator / denominator)
    return result

# Test: x = 1.0 radian (approx 57.3 degrees)
x_val = 1.0
print(f"Approximated value: {approx_sin(x_val)}")
print(f"math.sin value (for comparison): {math.sin(x_val)}")
```

## Radius of Convergence and Taylor's Theorem

The **radius of convergence** $R$ is a number specifying the distance from the center $a$ within which a power series converges, $|x-a|<R$; it is not the name of the interval itself. The cases $R=0$ and $R=\infty$ are possible. Boundary points with $|x-a|=R$ must be checked separately. For example, the Maclaurin series for $\ln(1+x)$ has radius 1 and equals the function for real $-1<x\le1$. It converges conditionally at $x=1$ and diverges at $x=-1$.

For a finite approximation, assume $f$ is $C^{n+1}$ on the interval joining $a$ and $x$. Taylor's theorem then gives:

$$
f(x)=P_{n,a}(x)+R_n(x),\qquad P_{n,a}(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k
$$

$$
R_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}
$$

Here $\xi$ lies between $a$ and $x$. If $|f^{(n+1)}|\le M$ throughout the interval, then $|R_n(x)|\le M|x-a|^{n+1}/(n+1)!$. To establish equality between a function and its infinite Taylor series, one can show that this remainder tends to zero as $n\to\infty$.

The code above adds 10 terms, through $x^{19}$. Since the coefficient of degree 20 in the sine series is zero, Taylor's theorem bounds the truncation error at $x=1$ by $1/21!$, approximately $1.96\times10^{-20}$. This bound applies to the finite sum computed exactly over the real numbers; Python's floating-point rounding error is separate. The output of `math.sin` is also a floating-point comparison value, not the exact mathematical value.

### A Smooth Function Not Represented by Its Taylor Series

$$
g(x)=\begin{cases}e^{-1/x},&x>0,\\0,&x\le0.\end{cases}
$$

This function is infinitely differentiable, and all its derivatives at zero are zero. Its Taylor series at zero is therefore identically zero and converges for every $x$. However, $g(x)>0$ for $x>0$, so the sum of the series does not equal the original function there. This example distinguishes convergence of a series from equality to the function that generated its coefficients.

## Conclusion

Taylor polynomials provide local approximations, and remainder terms bound their errors. When using a Taylor series as an equality, check its convergence range and whether its sum equals the original function. These distinctions help determine the accuracy and applicability of approximations in physics and numerical computation.

## References

- [NIST DLMF §1.4(vi): Taylor's theorem and remainders for a real variable](https://dlmf.nist.gov/1.4#vi)
- [MIT 18.100A: Basic Analysis §§4.3 and 5.4 (analyticity, smoothness, the logarithmic series, and a nonanalytic example)](https://ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/mit18_100af20_basic_analysis.pdf)
- [MIT 16.07 Lecture 24: Small-amplitude pendulum approximation and amplitude dependence](https://ocw.mit.edu/courses/16-07-dynamics-fall-2009/c0c881f96f4ff4e21f082c88e8b015d6_MIT16_07F09_Lec24.pdf)
- [Python 3.12 math: Mathematical functions and CPython implementation details](https://docs.python.org/3.12/library/math.html)
