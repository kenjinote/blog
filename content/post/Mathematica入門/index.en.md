---
title: 'Mathematica Introduction: How to Use Basic Commands for Equations, Calculus, etc.'
slug: "Mathematica入門"
date: 2024-07-25T01:36:19+09:00
tags: ["Mathematica", "Math", "Algorithm"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: 'Explains the basic usage and calculation commands of Mathematica for beginners. Summarizes specific examples of frequently used functions such as solving equations and simultaneous equations (Solve), inequalities (Reduce), differentiation (D), integration (Integrate), and matrix calculations.'
lastmod: "2026-11-24T00:00:00+09:00"
mermaid: true
---
# Introduction to Mathematica

## Solve an equation

```
Solve[x^2 - 3 x + 2 == 0, x]
```

Output
```
{{x -> 1}, {x -> 2}}
```

## Solve an equation within integers
```
Solve[x^2 - 3 x + 2 == 0 && 0 <= x <= 2, x, Integers]
```
Output
```
{{x -> 1}, {x -> 2}}
```

## Solve simultaneous equations
```
Solve[{x + y == 3, x - y == 1}, {x, y}]
```
Output
```
{{x -> 2, y -> 1}}
```

## Solve an inequality
```
Reduce[x^2 - 3 x + 2 > 0, x]
```
Output
```
x < 1 || x > 2
```

## Differentiate
```
D[x^2, x]
```
Output
```
2 x
```

## Integrate
```
Integrate[x^2, x]
```
Output
```
x^3/3
```

## Find a limit
```
Limit[1/x, x -> 0, Direction -> "FromAbove"]
```
Output
```
Infinity
```

The limit as x approaches 0 from the right is Infinity. The two-sided real limit does not exist. Use Direction to choose a one-sided approach.

## Find a series
```
Sum[1/n^2, {n, 1, Infinity}]
```
Output
```
π^2/6
```

## Create a matrix
```
m = {{1, 2}, {3, 4}}
```

## Find the product of matrices
```
m . m
```
Output
```
{{7, 10}, {15, 22}}
```

## Find the inverse matrix
```
Inverse[m]
```
Output
```
{{-2, 1}, {3/2, -1/2}}
```

## Find eigenvalues and eigenvectors
```
Eigensystem[m]
```
Output
```
{{(5 + Sqrt[33])/2, (5 - Sqrt[33])/2}, {{2, (3 + Sqrt[33])/2}, {2, (3 - Sqrt[33])/2}}}
```

The eigenvalues of this matrix are (5 ± √33)/2. Eigenvectors may be returned in a different order or scaled; each value-vector pair satisfies m.v = λv.

## Find the inner product of vectors
```
{1, 2} . {3, 4}
```
Output
```
11
```

## Find the cross product of vectors
```
Cross[{1, 2, 3}, {4, 5, 6}]
```
Output
```
{-3, 6, -3}
```

## Find the magnitude of a vector
```
Norm[{1, 2, 3}]
```
Output
```
√14
```

## Find the angle between vectors
```
ArcCos[{1, 2} . {3, 4}/(Norm[{1, 2}] Norm[{3, 4}])]
```

Output
```
ArcCos[11/(√5 √25)]
```

## Find the projection of a vector
```
Projection[{1, 2}, {3, 4}]
```
Output
```
{33/25, 44/25}
```

Projecting {1,2} onto {3,4} uses the dot-product ratio 11/25, giving {33/25,44/25}.







## Find the rotation of a vector
```
RotationMatrix[π/2].{1, 0}
```

Output
```
{0, 1}
```

## Find the translation of a vector
```
TranslationTransform[{1, 2}][{3, 4}]
```
Output
```
{4, 6}
```

## Find the scaling of a vector
```
ScalingTransform[{2, 3}][{1, 1}]
```
Output
```
{2, 3}
```

## Find the reflection of a vector
```
ReflectionTransform[{0, 1}][{1, 1}]
```
Output
```
{1, -1}
```

ReflectionTransform takes the mirror's normal as its first argument. The normal {0,1} defines the x-axis, which maps {1,1} to {1,-1}.

The random outputs below are illustrative and change on each evaluation. RandomInteger[] returns 0 or 1. SeedRandom can reproduce a sequence with the same generator and version.









## Generate random numbers
```
RandomReal[]
```


Output
```
0.123456
```

## Generate random numbers (integers)
```
RandomInteger[]
```
Output
```
0
```

## Generate random numbers (range specified)
```
RandomReal[{1, 10}]
```
Output
```
5.6789
```

## Generate random numbers (integers, range specified)
```
RandomInteger[{1, 10}]
```
Output
```
5
```

## Generate random numbers (distribution specified)
```
RandomVariate[NormalDistribution[0, 1]]
```
Output
```
0.123456
```

## Generate random numbers (distribution specified, number specified)
```
RandomVariate[NormalDistribution[0, 1], 10]
```
Output
```
{0.123456, 0.234567, 0.345678, 0.456789, 0.567890, 0.678901, 0.789012, 0.890123, 0.901234, 0.012345}
```

## Generate random numbers (distribution specified, number specified, seed specified)
```
SeedRandom[12345]
RandomVariate[NormalDistribution[0, 1], 10]
```
Output
```
(* Output intentionally omitted: exact sequence depends on the Wolfram Language version. *)
```

## Apply a function to array elements
```
Map[Sqrt, {1, 4, 9}]
Sqrt /@ {1, 4, 9}
Map[#^(1/2)&, {1, 4, 9}]
```
Output
```
{1, 2, 3}
```

## Define a function using lambda expressions
```
f = Function[x, x^2]
f[3]
```
Output
```
9
```

## Compose functions
```
f = Function[x, x^2]
g = Function[x, x + 1]
h = Function[x, f[g[x]]]
h[3]
```
Output
```
16
```

## Reference the previous calculation result
```
% + 1
```
Output
```
17
```

## Pure functions
```
(#+3)&[5]
```
Output
```
8
```

## Extract from an array
```
Select[{1, 2, 3, 4, 5}, EvenQ]
Select[{1, 2, 3, 4, 5}, Mod[#,2]==0&]
```
Output
```
{2, 4}
```


## Official function documentation

[Solve](https://reference.wolfram.com/language/ref/Solve.html) · [Reduce](https://reference.wolfram.com/language/ref/Reduce.html) · [D](https://reference.wolfram.com/language/ref/D.html) · [Integrate](https://reference.wolfram.com/language/ref/Integrate.html) · [Limit](https://reference.wolfram.com/language/ref/Limit.html) · [Sum](https://reference.wolfram.com/language/ref/Sum.html) · [Inverse](https://reference.wolfram.com/language/ref/Inverse.html) · [Eigensystem](https://reference.wolfram.com/language/ref/Eigensystem.html) · [Projection](https://reference.wolfram.com/language/ref/Projection.html) · [RotationMatrix](https://reference.wolfram.com/language/ref/RotationMatrix.html) · [ReflectionTransform](https://reference.wolfram.com/language/ref/ReflectionTransform.html) · [RandomReal](https://reference.wolfram.com/language/ref/RandomReal.html) · [RandomInteger](https://reference.wolfram.com/language/ref/RandomInteger.html) · [RandomVariate](https://reference.wolfram.com/language/ref/RandomVariate.html)
