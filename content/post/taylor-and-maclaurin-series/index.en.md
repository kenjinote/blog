---
title: "Taylor and Maclaurin Series: The Magic of Approximating Complex Functions with Polynomials"
description: "A detailed explanation of Taylor and Maclaurin series, the secrets of calculus, from intuitive meanings to mathematical derivations and applications in programming and physics."
slug: "taylor-and-maclaurin-series"
date: "2026-09-20T14:30:00+09:00"
image: "eyecatch.jpg"
categories:
  - "Mathematics"
tags:
  - "Calculus"
  - "Taylor Series"
  - "Maclaurin Series"
  - "Function Approximation"
---

## Introduction

In the worlds of mathematics, physics, and even computer science, **Taylor series** and **Maclaurin series** are incredibly powerful tools. They are methods for expressing "complex functions that are hard to calculate," such as exponential and trigonometric functions, as infinite sums of "simple polynomials that can be calculated using only addition and multiplication."

The reason calculators and computers can instantly compute values like $\sin(37^\circ)$ or $e^{2.5}$ is because they internally perform approximation calculations applying these expansions. In this article, we will explain this magical mathematical technique in detail, from its intuitive meaning to its rigorous formulas, and its actual applications.

## Why Approximate Functions with Polynomials?

To begin with, why is it necessary to represent a function as a polynomial ( $a + bx + cx^2 + \dots$ )?

```mermaid
flowchart LR
    A["Complex function"] -->|"Taylor expansion"| B["Infinite sum of polynomials"]
    B -->|"Truncate at finite terms"| C["Polynomial approximation"]
    C -->|"Basic arithmetic only"| D["High-speed computer calculation"]
```

Many functions describing natural phenomena are non-linear, making them difficult to calculate directly by hand or solely with a computer's CPU instructions. However, because polynomials consist only of **addition** and **multiplication**, they have the advantage of being extremely easy for computers to handle.

## Intuitive Understanding of Maclaurin Series

First, let's consider the **Maclaurin series**, which approximates a function around a specific point $x = 0$.
Suppose we have an unknown function $f(x)$. We want to approximate this function near $x = 0$ with a polynomial $P(x)$ like the following:

$$ P(x) = c_0 + c_1 x + c_2 x^2 + c_3 x^3 + \dots $$

The conditions for improving the accuracy of the approximation are as follows:

1.  **0th-order approximation** : The value of the function at $x=0$ matches ( $P(0) = f(0)$ ).
    This results in $c_0 = f(0)$.
2.  **1st-order approximation** : The slope (first derivative) at $x=0$ matches ( $P'(0) = f'(0)$ ).
    This results in $c_1 = f'(0)$. On a graph, this is the tangent line of the function $f(x)$ at $x=0$.
3.  **2nd-order approximation** : The curvature (second derivative) at $x=0$ matches ( $P''(0) = f''(0)$ ).
    Since $P''(x) = 2 c_2$, we have $c_2 = \frac{f''(0)}{2}$.
4.  **$n$th-order approximation** : In general, by matching up to the $n$-th derivative, we can more accurately mimic the behavior around $x=0$.

## Formula and Derivation of Maclaurin Series

By repeating the above intuitive conditions infinitely, we obtain a beautiful series using the derivative coefficients of each order of the function. This is called the **Maclaurin series**.

$$ f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f^{(3)}(0)}{3!}x^3 + \dots $$

Written using sigma notation, it looks like this:

$$ f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!} x^n $$

Here, $f^{(n)}(0)$ is the value obtained by differentiating the function $f(x)$ $n$ times and substituting $x=0$, and $n!$ represents the factorial of $n$ ( $n \times (n-1) \times \dots \times 1$ ).

## Maclaurin Series of Typical Functions

Here, we introduce the Maclaurin series of important functions that appear frequently.

### 1. Exponential function $e^x$

The exponential function $f(x) = e^x$ remains $e^x$ no matter how many times it is differentiated. Therefore, when $x=0$ is substituted, the derivative coefficients of all orders become $1$ ( $f^{(n)}(0) = 1$ ).

$$ e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots = \sum_{n=0}^{\infty} \frac{x^n}{n!} $$

### 2. Trigonometric functions $\sin x$ and $\cos x$

When $\sin x$ is repeatedly differentiated, it changes cyclically: $\cos x, -\sin x, -\cos x, \sin x, \dots$. By substituting $x=0$, only the derivative coefficients of odd orders remain, and the even orders become $0$.

$$ \sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} x^{2n+1} $$

Similarly, for $\cos x$, only the terms of even orders remain.

$$ \cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \dots = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n)!} x^{2n} $$

## Extension to Taylor Series

While the Maclaurin series is an approximation around $x=0$, generalizing this to an approximation around an arbitrary point $x=a$ yields the **Taylor series**.

$$ f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \dots = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x-a)^n $$

This formula demonstrates its power when you want to predict the value of a function at a location slightly away from $x=a$ ( $x = a + \Delta x$ ).

## Applications of Taylor Series

### Linear Approximation in Physics

In physics, approximation using Taylor series is frequently used to make equations of motion easier to solve. For example, in the motion of a pendulum, if the swing angle $\theta$ is sufficiently small, we extract only the 1st-order term of the Maclaurin series for $\sin \theta$ and approximate it as follows:

$$ \sin \theta \approx \theta \quad (\text{when } \theta \text{ is sufficiently small}) $$

This transforms a complex non-linear differential equation into an easily solvable linear differential equation, deriving the isochronism of a simple pendulum.

### Programming and Numerical Computation

Inside the standard libraries of computers (such as the `math` module), Taylor series (or its improved versions like Chebyshev approximation) are utilized to calculate functions. Below is a simple example of approximating $\sin x$ in Python.

```python
import math

def approx_sin(x, terms=10):
    """
    Function to approximate sin(x) using Maclaurin series
    x: Angle in radians
    terms: Number of terms to calculate
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
print(f"True value: {math.sin(x_val)}")
```

## Radius of Convergence and Taylor's Theorem

Not all functions can be accurately represented by a Taylor series at every $x$. The range within which the infinite series converges to a finite value is called the **radius of convergence**. For example, the Maclaurin series for $\ln(1+x)$ is only valid in the range $-1 < x \le 1$.

Furthermore, **Taylor's theorem** (evaluation of the remainder term) is a theorem for estimating how much error there will be between the true value and the approximated value when truncated at finite terms (up to the $n$-th order). This allows us to mathematically guarantee "up to what order we should expand based on the required accuracy."

## Conclusion

Taylor series and Maclaurin series are, so to speak, "mathematical translators" for translating the complex world into an easily manageable form called polynomials. The process of starting from the concept of differentiation and completely restoring the original function through infinite additions symbolizes the beauty of mathematics. From approximations in physics to optimization algorithms in AI, their range of applications is immeasurable. By all means, utilize this powerful tool to deepen your understanding of mathematics and programming.
