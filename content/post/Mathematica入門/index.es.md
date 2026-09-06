---








title: "Introducción a Mathematica"
slug: "Mathematica入門"
date: 2024-07-25T01:36:19+09:00
tags: ["Mathematica", "Matemáticas", "Algoritmo"]
draft: false
image: "img.png"
categories: ["Matemáticas, Criptografía y Cuántica"]
---








# Introducción a Mathematica

## Resolver ecuaciones

```
Solve[x^2 - 3 x + 2 == 0, x]
```

Salida
```
{{x -> 1}, {x -> 2}}
```

## Encontrar soluciones enteras para una ecuación
```
Solve[x^2 - 3 x + 2 == 0 && 0 <= x <= 2, x, Integers]
```
Salida
```
{{x -> 1}, {x -> 2}}
```

## Resolver un sistema de ecuaciones
```
Solve[{x + y == 3, x - y == 1}, {x, y}]
```
Salida
```
{{x -> 2, y -> 1}}
```

## Resolver inecuaciones
```
Reduce[x^2 - 3 x + 2 > 0, x]
```
Salida
```
x < 1 || x > 2
```

## Derivar
```
D[x^2, x]
```
Salida
```
2 x
```

## Integrar
```
Integrate[x^2, x]
```
Salida
```
x^3/3
```

## Calcular el límite
```
Limit[1/x, x -> 0]
```
Salida
```
Infinity
```

## Calcular una serie
```
Sum[1/n^2, {n, 1, Infinity}]
```
Salida
```
π^2/6
```

## Crear una matriz
```
m = {{1, 2}, {3, 4}}
```

## Multiplicar matrices
```
m . m
```
Salida
```
{{7, 10}, {15, 22}}
```

## Calcular la matriz inversa
```
Inverse[m]
```
Salida
```
{{-2, 1}, {1.5, -0.5}}
```

## Calcular valores propios y vectores propios
```
Eigensystem[m]
```
Salida
```
{{5, 0}, {{1, 1}, {1, -1}}}
```

## Calcular el producto punto de vectores
```
{1, 2} . {3, 4}
```
Salida
```
11
```

## Calcular el producto cruzado de vectores
```
Cross[{1, 2, 3}, {4, 5, 6}]
```
Salida
```
{-3, 6, -3}
```

## Calcular la magnitud (norma) de un vector
```
Norm[{1, 2, 3}]
```
Salida
```
√14
```

## Calcular el ángulo entre vectores
```
ArcCos[{1, 2} . {3, 4}/(Norm[{1, 2}] Norm[{3, 4}])]
``` 

Salida
```
ArcCos[11/(√5 √25)]
```

## Calcular la proyección de un vector
```
{1, 2} . {3, 4}/Norm[{3, 4}] {3, 4}/Norm[{3, 4}]
```
Salida
```
{11/5, 22/5}
```

## Calcular la rotación de un vector
```
RotationMatrix[π/2].{1, 0}
```

Salida
```
{0, 1}
```

## Calcular la traslación de un vector
```
TranslationTransform[{1, 2}][{3, 4}]
```
Salida
```
{4, 6}
```

## Calcular la escala de un vector
```
ScalingTransform[{2, 3}][{1, 1}]
```
Salida
```
{2, 3}
```

## Calcular la reflexión de un vector
```
ReflectionTransform[{1, 1}][{1, 1}]
```
Salida
```
{0, 0}
```

## Generar un número aleatorio
```
RandomReal[]
```
Salida
```
0.123456
```

## Generar un número aleatorio (entero)
```
RandomInteger[]
```
Salida
```
123456
```

## Generar un número aleatorio (rango específico)
```
RandomReal[{1, 10}]
```
Salida
```
5.6789
```

## Generar un número aleatorio (entero, rango específico)
```
RandomInteger[{1, 10}]
```
Salida
```
5
```

## Generar un número aleatorio (distribución específica)
```
RandomVariate[NormalDistribution[0, 1]]
```
Salida
```
0.123456
```

## Generar números aleatorios (distribución y cantidad específicas)
```
RandomVariate[NormalDistribution[0, 1], 10]
```
Salida
```
{0.123456, 0.234567, ..., 0.987654}
```

## Generar números aleatorios (distribución, cantidad y semilla específicas)
```
SeedRandom[12345]
RandomVariate[NormalDistribution[0, 1], 10]
```
Salida
```
{0.123456, 0.234567, ..., 0.987654}
```

## Aplicar una función a los elementos de un array
```
Map[Sqrt, {1, 4, 9}]
Sqrt /@ {1, 4, 9}
Map[#^(1/2)&, {1, 4, 9}]
```
Salida
```
{1, 2, 3}
```

## Definir una función usando una expresión lambda
```
f = Function[x, x^2]
f[3]
```
Salida
```
9
```

## Componer funciones
```
f = Function[x, x^2]
g = Function[x, x + 1]
h = Function[x, f[g[x]]]
h[3]
```
Salida
```
16
```

## Hacer referencia al resultado del cálculo anterior
```
% + 1
```
Salida
```
17
```

## Función pura
```
(#+3)&[5]
```
Salida
```
8
```

## Extraer elementos de un array
```
Select[{1, 2, 3, 4, 5}, EvenQ]
Select[{1, 2, 3, 4, 5}, Mod[#,2]==0&]
```
Salida
```
{2, 4}
```
