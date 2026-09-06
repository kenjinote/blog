---
title: 'Introduction to Mathematica'
slug: "Mathematica入門"
date: 2024-07-25T01:36:19+09:00
tags: ["Mathematica", "Math", "Algorithm"]
draft: false
image: "img.png"
categories: ["Math/Cryptography/Quantum"]
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
Limit[1/x, x -> 0]
```
Output
```
Infinity
```

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
{{-2, 1}, {1.5, -0.5}}
```

## Find eigenvalues and eigenvectors
```
Eigensystem[m]
```
Output
```
{{5, 0}, {{1, 1}, {1, -1}}}
```

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
{1, 2} . {3, 4}/Norm[{3, 4}] {3, 4}/Norm[{3, 4}]
```
Output
```
{11/5, 22/5}
```

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
ReflectionTransform[{1, 1}][{1, 1}]
```
Output
```
{0, 0}
```

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
123456
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
{0.123456, 0.234567, ..., 0.987654}
```

## Generate random numbers (distribution specified, number specified, seed specified)
```
SeedRandom[12345]
RandomVariate[NormalDistribution[0, 1], 10]
```
Output
```
{0.123456, 0.234567, ..., 0.987654}
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
