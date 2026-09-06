---
title: "Introdução ao Mathematica"
slug: "Mathematica入門"
date: 2024-07-25T01:36:19+09:00
tags: ["Mathematica", "Matemática", "Algoritmos"]
draft: false
image: "img.png"
categories: ["Matemática・Criptografia・Quântica"]
---
# Introdução ao Mathematica

## Resolver equações

```
Solve[x^2 - 3 x + 2 == 0, x]
```

Saída
```
{{x -> 1}, {x -> 2}}
```

## Encontrar raízes de equações no intervalo de inteiros
```
Solve[x^2 - 3 x + 2 == 0 && 0 <= x <= 2, x, Integers]
```
Saída
```
{{x -> 1}, {x -> 2}}
```

## Resolver sistema de equações
```
Solve[{x + y == 3, x - y == 1}, {x, y}]
```
Saída
```
{{x -> 2, y -> 1}}
```

## Resolver desigualdades
```
Reduce[x^2 - 3 x + 2 > 0, x]
```
Saída
```
x < 1 || x > 2
```

## Derivar
```
D[x^2, x]
```
Saída
```
2 x
```

## Integrar
```
Integrate[x^2, x]
```
Saída
```
x^3/3
```

## Encontrar limites
```
Limit[1/x, x -> 0]
```
Saída
```
Infinity
```

## Encontrar séries
```
Sum[1/n^2, {n, 1, Infinity}]
```
Saída
```
π^2/6
```

## Criar matriz
```
m = {{1, 2}, {3, 4}}
```

## Encontrar produto de matrizes
```
m . m
```
Saída
```
{{7, 10}, {15, 22}}
```

## Encontrar matriz inversa
```
Inverse[m]
```
Saída
```
{{-2, 1}, {1.5, -0.5}}
```

## Encontrar autovalores e autovetores
```
Eigensystem[m]
```
Saída
```
{{5, 0}, {{1, 1}, {1, -1}}}
```

## Encontrar produto escalar de vetores
```
{1, 2} . {3, 4}
```
Saída
```
11
```

## Encontrar produto vetorial
```
Cross[{1, 2, 3}, {4, 5, 6}]
```
Saída
```
{-3, 6, -3}
```

## Encontrar magnitude de um vetor
```
Norm[{1, 2, 3}]
```
Saída
```
√14
```

## Encontrar o ângulo de vetores
```
ArcCos[{1, 2} . {3, 4}/(Norm[{1, 2}] Norm[{3, 4}])]
``` 

Saída
```
ArcCos[11/(√5 √25)]
```

## Encontrar projeção de vetor
```
{1, 2} . {3, 4}/Norm[{3, 4}] {3, 4}/Norm[{3, 4}]
```
Saída
```
{11/5, 22/5}
```

## Encontrar rotação de vetor
```
RotationMatrix[π/2].{1, 0}
```

Saída
```
{0, 1}
```

## Encontrar translação de vetor
```
TranslationTransform[{1, 2}][{3, 4}]
```
Saída
```
{4, 6}
```

## Encontrar escala de vetor
```
ScalingTransform[{2, 3}][{1, 1}]
```
Saída
```
{2, 3}
```

## Encontrar reflexão de vetor
```
ReflectionTransform[{1, 1}][{1, 1}]
```
Saída
```
{0, 0}
```

## Gerar números aleatórios
```
RandomReal[]
```
Saída
```
0.123456
```

## Gerar números aleatórios (inteiros)
```
RandomInteger[]
```
Saída
```
123456
```

## Gerar números aleatórios (com intervalo)
```
RandomReal[{1, 10}]
```
Saída
```
5.6789
```

## Gerar números aleatórios (inteiros, com intervalo)
```
RandomInteger[{1, 10}]
```
Saída
```
5
```

## Gerar números aleatórios (com distribuição)
```
RandomVariate[NormalDistribution[0, 1]]
```
Saída
```
0.123456
```

## Gerar números aleatórios (distribuição, quantidade)
```
RandomVariate[NormalDistribution[0, 1], 10]
```
Saída
```
{0.123456, 0.234567, ..., 0.987654}
```

## Gerar números aleatórios (distribuição, quantidade, semente)
```
SeedRandom[12345]
RandomVariate[NormalDistribution[0, 1], 10]
```
Saída
```
{0.123456, 0.234567, ..., 0.987654}
```

## Aplicar função aos elementos do array
```
Map[Sqrt, {1, 4, 9}]
Sqrt /@ {1, 4, 9}
Map[#^(1/2)&, {1, 4, 9}]
```
Saída
```
{1, 2, 3}
```

## Definir função com expressões lambda
```
f = Function[x, x^2]
f[3]
```
Saída
```
9
```

## Compor funções
```
f = Function[x, x^2]
g = Function[x, x + 1]
h = Function[x, f[g[x]]]
h[3]
```
Saída
```
16
```

## Referenciar o resultado do cálculo anterior
```
% + 1
```
Saída
```
17
```

## Funções puras
```
(#+3)&[5]
```
Saída
```
8
```

## Extrair arrays
```
Select[{1, 2, 3, 4, 5}, EvenQ]
Select[{1, 2, 3, 4, 5}, Mod[#,2]==0&]
```
Saída
```
{2, 4}
```
