---le: 'Introdução ao Mathematica: Como usar comandos básicos como equações, cálculo diferencial e integral'
slug: "Mathematica入門"
date: 2024-07-25T01:36:19+09:00
tags: ["Mathematica", "Matemática", "Algoritmos"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: 'Explicamos o uso básico e os comandos de cálculo do Mathematica para iniciantes. Reunimos exemplos práticos de funções frequentemente usadas, como resolução de equações e sistemas de equações (Solve), inequações (Reduce), derivadas (D), integrais (Integrate), cálculos de matrizes, entre outros.'
lastmod: "2026-11-24T00:00:00+09:00"

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
Limit[1/x, x -> 0, Direction -> "FromAbove"]
```
Saída
```
Infinity
```

O limite quando x tende a 0 pela direita é Infinity. O limite real bilateral não existe. Direction permite indicar o lado de aproximação.

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
{{-2, 1}, {3/2, -1/2}}
```

## Encontrar autovalores e autovetores
```
Eigensystem[m]
```
Saída
```
{{(5 + Sqrt[33])/2, (5 - Sqrt[33])/2}, {{2, (3 + Sqrt[33])/2}, {2, (3 - Sqrt[33])/2}}}
```

Os autovalores desta matriz são (5 ± √33)/2. A ordem ou a escala dos autovetores pode variar; cada par satisfaz m.v = λv.

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
Projection[{1, 2}, {3, 4}]
```
Saída
```
{33/25, 44/25}
```

A projeção ortogonal de {1,2} sobre {3,4} usa a razão dos produtos escalares 11/25 e resulta em {33/25,44/25}.







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
ReflectionTransform[{0, 1}][{1, 1}]
```
Saída
```
{1, -1}
```

O primeiro argumento de ReflectionTransform é a normal do espelho. A normal {0,1} define o eixo x e transforma {1,1} em {1,-1}.

Os resultados aleatórios abaixo são ilustrativos e mudam a cada avaliação. RandomInteger[] retorna 0 ou 1. SeedRandom pode reproduzir uma sequência com o mesmo gerador e versão.









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
0
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
{0.123456, 0.234567, 0.345678, 0.456789, 0.567890, 0.678901, 0.789012, 0.890123, 0.901234, 0.012345}
```

## Gerar números aleatórios (distribuição, quantidade, semente)
```
SeedRandom[12345]
RandomVariate[NormalDistribution[0, 1], 10]
```
Saída
```
(* Output intentionally omitted: exact sequence depends on the Wolfram Language version. *)
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


## Documentação oficial das funções

[Solve](https://reference.wolfram.com/language/ref/Solve.html) · [Reduce](https://reference.wolfram.com/language/ref/Reduce.html) · [D](https://reference.wolfram.com/language/ref/D.html) · [Integrate](https://reference.wolfram.com/language/ref/Integrate.html) · [Limit](https://reference.wolfram.com/language/ref/Limit.html) · [Sum](https://reference.wolfram.com/language/ref/Sum.html) · [Inverse](https://reference.wolfram.com/language/ref/Inverse.html) · [Eigensystem](https://reference.wolfram.com/language/ref/Eigensystem.html) · [Projection](https://reference.wolfram.com/language/ref/Projection.html) · [RotationMatrix](https://reference.wolfram.com/language/ref/RotationMatrix.html) · [ReflectionTransform](https://reference.wolfram.com/language/ref/ReflectionTransform.html) · [RandomReal](https://reference.wolfram.com/language/ref/RandomReal.html) · [RandomInteger](https://reference.wolfram.com/language/ref/RandomInteger.html) · [RandomVariate](https://reference.wolfram.com/language/ref/RandomVariate.html)
