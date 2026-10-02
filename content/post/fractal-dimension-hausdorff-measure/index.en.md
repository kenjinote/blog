---
title: "Fractal Dimension and Hausdorff Measure: Fractional Dimensions Beyond the Wall of Integers and the Science of Self-Similarity"
description: "The Mandelbrot set, the coastline paradox, and the fractional dimensions between 1D and 2D. The order of nature unraveled by geometry and measure theory."
slug: "fractal-dimension-hausdorff-measure"
date: "2026-10-03T05:00:00+09:00"
categories: ["mathematics", "physics"]
tags: ["fractal", "hausdorff-dimension", "mandelbrot", "measure-theory"]
image: "eyecatch.jpg"
---

## Introduction: Rethinking the Concept of Dimension

The space we experience daily is recognized as a 3-dimensional Euclidean space. A line on paper is 1-dimensional, a plane is 2-dimensional, and a solid is 3-dimensional. This has been the firm intuition underlying humanity's spatial awareness for thousands of years since Euclid of ancient Greece. However, when observing the complex shapes of the natural world, this paradigm of "integer dimensions" faces a definitive limitation. Clouds are not spheres, mountains are not cones, and coastlines are not circular arcs. Many of the forms found in nature, such as the branching of trees, networks of blood vessels, and trajectories of lightning, possess a "roughness" that is fundamentally different from the subjects of smooth Euclidean geometry.

"Fractal geometry" was born as a new language to mathematically describe this complexity of the natural world. And supporting its theoretical foundation are the concepts of "Hausdorff measure" and the accompanying "Hausdorff dimension," born from the depths of real analysis and measure theory. In this article, we will thoroughly explain how fractal dimensions are defined, calculated, and applied to the understanding of natural phenomena, from intuitive geometry to rigorous measure theory.

---

## Chapter 1: The Limits of Euclidean Geometry and the "Roughness of Nature"

### Benoit Mandelbrot's Question "How Long Is the Coast of Britain?"

There is a famous question that symbolizes the dawn of fractal geometry. "How Long Is the Coast of Britain?" is the title of a paper published in the scientific journal *Science* by Benoit Mandelbrot in 1967.

At first glance, this question seems like a simple measurement problem. However, a deep paradox lay hidden within it. Suppose we approximate the coastline using a ruler of a certain fixed length (for example, length $\eta = 100 \text{ km}$) to measure it. As we make the length of the ruler smaller ($\eta = 10 \text{ km}, 1 \text{ km}, 1 \text{ m}, \dots$), what will happen to the total measured length? If it were a smooth curve (like a circle or parabola), it would converge to a certain finite value as the ruler gets smaller. This is the classical definition of the length (arc length) of a curve.

However, this is not the case for actual coastlines. The smaller the ruler, the more it captures the tiny inlets and unevenness of rocks that were previously hidden and overlooked between the rulers, causing the length of the coastline to increase infinitely. In other words, in the limit as the measurement scale $\eta$ approaches $0$, the length of the coastline $L(\eta)$ diverges to infinity.

### The Richardson Effect

This phenomenon was empirically discovered by the meteorologist Lewis Fry Richardson. Richardson measured the lengths of borders and coastlines of various countries at different scales and discovered that the following power law holds between the measurement scale $\eta$ and the measured length $L(\eta)$:

$$ L(\eta) \propto \eta^{1-D} $$

Here, $D$ is a constant, and the more complex the coastline, the larger the value of $D$. While Richardson himself treated this $D$ as an empirical constant, Mandelbrot gave it a profound mathematical interpretation. Namely, he considered that this $D$ represents the "dimension" of the object.

For a smooth 1-dimensional curve, $D=1$, and the length converges to a constant value as $L(\eta) \propto \eta^0 = 1$. However, for extremely complex boundaries like the coast of Britain, $D \approx 1.25$, and since $1 - D = -0.25 < 0$, $L(\eta) \to \infty$ as $\eta \to 0$. This real number dimension, greater than $1$ and less than $2$, was the very first sprout of the "fractal dimension."

---

## Chapter 2: Self-Similarity and Similarity Dimension

The word fractal is derived from the Latin "fractus" (broken, fragmented) and was coined by Mandelbrot. One of the most fundamental characteristics of a fractal is "self-similarity." It refers to the property where magnifying the whole reveals the same structure as the whole contained within it.

By utilizing this self-similarity, we can derive an intuitive definition of dimension called "Similarity Dimension."

### Intuitive Derivation of Similarity Dimension $D$

Let's consider the properties of smooth Euclidean figures.
- When a 1-dimensional line segment is reduced to a scale of $1/r$, $r^1$ of those reduced segments are needed to construct the original line segment.
- When a 2-dimensional square is reduced to $1/r$ on each side, $r^2$ small squares are needed to construct the original square.
- When a 3-dimensional cube is reduced to $1/r$ on each side, $r^3$ small cubes are needed to construct the original cube.

In general, when a figure in a $d$-dimensional space is reduced to $1/r$, the number of copies $N$ required to reconstruct the original figure satisfies the relationship:
$$ N = r^d $$
Taking the logarithm of both sides of this equation,
$$ \log N = d \log r $$
Solving for the dimension $d$, it can be defined as follows:

$$ d = \frac{\log N}{\log r} $$

The "Similarity Dimension" extends this definition to self-similar figures that do not have integer dimensions.

$$ D_s = \frac{\log N}{\log(1/r)} $$

Here, $r$ is the reduction ratio ($0 < r < 1$), and $N$ is the number of reduced figures needed to completely cover the original figure. (Note that when $r$ is the reduction ratio, the denominator becomes $\log(1/r)$. In the previous example, $r$ was the magnification factor, so be careful with the definition of the symbols).

### Cantor Set

Introduced by Georg Cantor in 1883, this set is one of the most important counterexamples in measure theory.
The construction method is as follows:
1. Start with the interval $[0, 1]$ (Step 0).
2. Remove the middle 1/3, which is $(1/3, 2/3)$ (Step 1: the intervals are $[0, 1/3] \cup [2/3, 1]$).
3. Remove the middle 1/3 of each remaining interval.
4. Repeat this infinitely.

The set obtained as the limit (Cantor ternary set) possesses self-similarity. The whole is composed of $2$ copies of the whole reduced to $1/3$.
Therefore, the similarity dimension is
$$ D = \frac{\log 2}{\log 3} \approx 0.6309 $$
This is a set larger than 0-dimensional (a point) and smaller than 1-dimensional (a line). Surprisingly, the Lebesgue measure (length) of this set is $0$, yet it contains an uncountably infinite number of points.

### Koch Curve

This is a continuous but nowhere differentiable curve devised by Helge von Koch in 1904.
1. Divide a line segment into three equal parts.
2. Replace the middle segment with two sides of an equilateral triangle having that segment as its base.
3. Repeat this for all line segments.

With one operation, the length of the line segment becomes $4/3$ times longer. Repeated infinitely, the length becomes $(4/3)^\infty \to \infty$ (infinite length). On the other hand, the area enclosed by it (Koch snowflake) is finite. The similarity dimension of this curve, which has zero area and infinite length, is composed of $N = 4$ copies with a reduction ratio of $r = 1/3$, so
$$ D = \frac{\log 4}{\log 3} \approx 1.2618 $$

### Sierpinski Gasket

This is a figure obtained by repeatedly hollowing out a central inverted triangle from an equilateral triangle.
Since it is composed of $N = 3$ copies with a reduction ratio of $r = 1/2$, the similarity dimension is
$$ D = \frac{\log 3}{\log 2} \approx 1.5849 $$
Its area (2-dimensional Lebesgue measure) is 0, but its 1-dimensional length is infinite.

---

## Chapter 3: Rigorous Definitions of Hausdorff Outer Measure and Hausdorff Dimension

While the similarity dimension is intuitive and easy to calculate, it can only be applied to figures with "strict self-similarity." To determine the dimension of fractals in nature or mathematically complex sets (sets where self-similarity is broken), a rigorous and universal definition of dimension based on real analysis and measure theory is needed. That is the "Hausdorff Dimension."

In 1918, Felix Hausdorff extended Carathéodory's measure-theoretic method and defined the $d$-dimensional outer measure for any non-negative real number $d$.

### $\delta$-cover

Consider a subset $E$ of $\mathbb{R}^n$. For any $\delta > 0$, a collection of subsets $\{U_i\}_{i=1}^\infty$ of $E$ is called a **$\delta$-cover** of $E$ if it satisfies
$$ E \subset \bigcup_{i=1}^\infty U_i \quad \text{and} \quad \operatorname{diam}(U_i) \leq \delta $$
Here, $\operatorname{diam}(U_i)$ is the diameter (supremum distance) of $U_i$, defined as $\sup_{x,y \in U_i} \|x - y\|$.

### Hausdorff Outer Measure $\mathcal{H}^d(E)$

Fix a non-negative real number $d \geq 0$. For any $\delta$-cover $\{U_i\}$ of $E$, consider the sum of the $d$-th powers of their respective diameters, and take its infimum.

$$ \mathcal{H}_\delta^d(E) = \inf \left\{ \sum_{i=1}^\infty (\operatorname{diam} U_i)^d \mathrel{\Big|} \{U_i\} \text{ is a } \delta\text{-cover of } E \right\} $$

As $\delta$ is made smaller, the condition for the cover becomes stricter, so the set for the infimum narrows, making $\mathcal{H}_\delta^d(E)$ monotonically non-decreasing. Therefore, the limit as $\delta \to 0$ exists (including $\infty$).

$$ \mathcal{H}^d(E) = \lim_{\delta \to 0} \mathcal{H}_\delta^d(E) = \sup_{\delta > 0} \mathcal{H}_\delta^d(E) $$

This $\mathcal{H}^d(E)$ is called the **$d$-dimensional Hausdorff measure**. In measure-theoretic terms, this is an outer measure with Borel regularity (satisfying Carathéodory's criterion) and becomes a true measure satisfying countable additivity over the Borel $\sigma$-algebra.

For an integer dimension $d = n$, $\mathcal{H}^n(E)$ differs from the usual $n$-dimensional Lebesgue measure only by a constant multiple (it perfectly matches if the normalization constant is adjusted).

### Hausdorff Dimension $\dim_H(E)$ as a Jumping Critical Value

The most important property of the Hausdorff measure is the behavior of $\mathcal{H}^d(E)$ when the value of $d$ is changed.
Suppose that for a certain $d$, $\mathcal{H}^d(E) < \infty$. Then, for any $s > d$,
$$ \sum (\operatorname{diam} U_i)^s = \sum (\operatorname{diam} U_i)^{s-d} (\operatorname{diam} U_i)^d \leq \delta^{s-d} \sum (\operatorname{diam} U_i)^d $$
Taking $\delta \to 0$, we have $\delta^{s-d} \to 0$, so $\mathcal{H}^s(E) = 0$.
Conversely, if $\mathcal{H}^s(E) > 0$, then for any $d < s$, $\mathcal{H}^d(E) = \infty$.

In other words, as $d$ increases from $0$, $\mathcal{H}^d(E)$ exhibits an extreme "jump": it is always $\infty$ up to a certain critical point, and beyond that critical point, it is always $0$. The value of $d$ at this critical point is defined as the **Hausdorff Dimension**.

$$ \dim_H(E) = \inf \{ d \geq 0 \mid \mathcal{H}^d(E) = 0 \} = \sup \{ d \geq 0 \mid \mathcal{H}^d(E) = \infty \} $$

The overwhelming beauty of this definition is that the dimension is rigorously and uniquely determined for subsets of any metric space, even if the target set $E$ has no self-similarity, or is any pathological set. The Hausdorff dimensions of the Cantor set and the Koch curve correspond exactly to the similarity dimensions mentioned earlier.

---

## Chapter 4: Box-Counting Dimension (Capacity Dimension), Information Dimension, and Packing Dimension

While the Hausdorff dimension is the most mathematically refined concept, it is not suitable for numerical calculations or experimental data analysis (because it requires finding an infimum from infinite covering patterns and then taking a limit). Therefore, in applied mathematics and physics, more computable definitions of fractal dimension are used.

### Box-counting Dimension (Capacity Dimension)

Divide the space into a grid with a side length of $\varepsilon$, and let $N(\varepsilon)$ be the number of boxes (grid cells) intersecting the target set $E$. Then, the box-counting dimension $\dim_B(E)$ is defined as follows:

$$ \dim_B(E) = \lim_{\varepsilon \to 0} \frac{\log N(\varepsilon)}{-\log \varepsilon} $$

This definition is extremely practical and forms the basis for algorithms (like the coverage method) used to estimate fractal dimensions in image analysis. However, it also has mathematical flaws. For example, the box-counting dimension of the set of rational numbers $\mathbb{Q} \cap [0,1]$ is $1$, but its Hausdorff dimension is $0$ because it is a countable set. In general, $\dim_H(E) \leq \dim_B(E)$ holds.

### Information Dimension and Generalized Dimensions

When a fractal set has a non-uniform distribution, simply counting the boxes is insufficient. Letting $P_i$ be the measure (probability) contained in each box $i$, the information dimension $D_1$ is defined using the Shannon entropy $I(\varepsilon) = - \sum P_i \log P_i$:

$$ D_1 = \lim_{\varepsilon \to 0} \frac{\sum P_i \log P_i}{\log \varepsilon} $$

Furthermore, in the "multifractal" theory based on Alfréd Rényi's extended entropy, this develops into the concept of generalized dimensions (Rényi dimensions) $D_q$.

### Packing Dimension

The packing dimension $\dim_P(E)$, introduced by Tricot in the 1980s, is a dual concept to the Hausdorff dimension. While the Hausdorff dimension takes the approach of "covering the set," the packing dimension takes the approach of "packing spheres inside the set."
Strictly speaking, the relationship $\dim_H(E) \leq \dim_P(E) \leq \dim_{\overline{B}}(E)$ (upper box-counting dimension) holds, making it a very powerful tool in the probabilistic analysis of sets.

---

## Chapter 5: Complex Dynamics of the Mandelbrot Set and Julia Sets

When talking about fractal geometry, one cannot avoid the world of Complex Dynamics. In particular, the "Mandelbrot set," generated from an extremely simple quadratic map on the complex plane, is considered one of the most complex and beautiful figures in the history of mathematics.

### Complex Quadratic Map $z_{n+1} = z_n^2 + c$

Consider a dynamical system parameterized by a complex number $c \in \mathbb{C}$. Starting from the initial value $z_0 = 0$, the sequence $\{z_n\}$ is generated by the following recurrence relation:

$$ z_{n+1} = z_n^2 + c $$

The set of parameters $c$ for which this sequence does not diverge to infinity as $n \to \infty$ but remains bounded is called the **Mandelbrot set $\mathcal{M}$**.

$$ \mathcal{M} = \left\{ c \in \mathbb{C} \mathrel{\Big|} \sup_{n} |z_n| < \infty, \text{ where } z_0 = 0 \right\} $$

On the other hand, when $c$ is fixed and the initial value $z_0$ is varied, the (boundary of the) set of initial values for which the sequence remains bounded is called the **Julia set**. The Mandelbrot set essentially functions as a catalog (parameter space of connectedness) for the infinitely many Julia sets.

### Shishikura's Theorem on the Hausdorff Dimension of the Boundary

The boundary of the Mandelbrot set, $\partial \mathcal{M}$, has a fractal structure of unimaginable complexity. No matter how much it is magnified, infinitely scaled-down copies of the Mandelbrot set (mini-Mandelbrots) continue to appear, connected by countless filaments.

Mathematically, how great is the "complexity" of this boundary line? In 1998, the Japanese mathematician Mitsuhiro Shishikura proved a monumental theorem in complex dynamics.

**Theorem (Shishikura, 1998)**
The Hausdorff dimension of the boundary of the Mandelbrot set, $\partial \mathcal{M}$, is exactly $2$.
$$ \dim_H(\partial \mathcal{M}) = 2 $$

Despite being merely a boundary "line" (a 1-dimensional entity) on a plane (2 dimensions), the fact that its Hausdorff dimension reaches $2$, the dimension of the space itself, means that $\partial \mathcal{M}$ undulates, folds, and possesses countless minute structures to the extent that it fills the space on the complex plane to the limit. However, whether its 2-dimensional Lebesgue measure (area) is positive or not remains an unsolved super-hard problem in modern mathematics.

---

## Chapter 6: Fractals in Physics and the Natural World

Fractal geometry and the Hausdorff dimension have transcended the boundaries of pure mathematics, exerting a disruptive impact on natural sciences in general, including physics, biology, and cosmology. It is as if the natural world chose fractal geometry over Euclidean geometry.

### Turbulence and Fluid Dynamics

"Turbulence," the most intractable phenomenon in fluid dynamics, has a fractal structure. According to the energy cascade theory (by Richardson and Kolmogorov), large eddies in turbulence break down into smaller eddies, which then break down further, repeating this process in a self-similar manner. Calculating the fractal dimension of the region where energy dissipation occurs (dissipative structure) is one approach toward mathematically elucidating the Navier-Stokes equations.

### Trajectory of Brownian Motion $D=2$

"Brownian motion (Wiener process)" is the phenomenon where microscopic particles move irregularly in a liquid or gas. When the trajectory of such a particle is drawn in space, it is infinitely jagged and nowhere differentiable.
Surprisingly, the Hausdorff dimension of the trajectory of standard Brownian motion in an $n \geq 2$ dimensional space is rigorously $2$ with probability 1.
$$ \dim_H(\text{Brownian path}) = 2 \quad \text{almost surely} $$
This indicates that although it is a curve generated from a 1-dimensional time parameter, it explores the space so densely that it possesses the areal extent of a 2-dimensional space.

### Large-scale Structure of the Universe (Cosmology)

Looking up at the night sky, stars seem to be scattered randomly, but when mapping the distribution of galaxies on a large cosmological scale in 3D (such as the Sloan Digital Sky Survey), the "large-scale structure of the universe," consisting of filamentary superclusters and giant voids, emerges. Analyzing the correlation function of this matter distribution suggests that it possesses self-similarity with a fractal dimension of $D \approx 1.2$ to $2.0$ at certain scales. The self-organization of matter by gravity generates fractals.

### Optimal Transport Networks of Alveoli and Blood Vessels

Fractals are also universal in the realm of biology. The human lungs (branching structure of the bronchi), the cardiovascular system, and the neural networks of the brain all have fractal structures.
Why did natural selection choose fractals? It is because they are the optimal solution for "packing an infinite surface area into a finite volume (space)." By branching the bronchi fractally, the surface area for oxygen exchange is maximized while maintaining a constant lung volume, and the energy loss for delivering blood to cells in every corner of the body is minimized. The optimization mechanisms of life perfectly conform to the mathematical laws of fractal dimension.

## Conclusion: The Continuity of Dimensions and a New View of Nature

The "integer dimensions" given to us by Euclidean geometry were extremely useful approximation models for the human brain to simplify and understand the world. However, "fractals" and "Hausdorff dimensions," born from the development of measure theory and Mandelbrot's intuition, proved that dimensions do not just take discrete values of $0, 1, 2, 3$, but can exist as a continuum of real numbers.

The Hausdorff dimension is the ultimate yardstick for quantifying the "roughness," "infinite detail," and "order hidden within chaos" lurking in the natural world. From coastlines, trees, and lightning to the structure of the universe and our own bodies, fractals can be said to be the universal design language of the cosmos.

The fact that measure theory (Hausdorff outer measure), the pinnacle of mathematical abstraction, accurately describes the reality of the physical world to such an extent strongly impresses upon us the mysterious correspondence that exists between mathematics and natural science. Fractal geometry has fundamentally changed the way we view the world.
