---
title: "Introduction à Mathematica"
slug: "Mathematica入門"
date: 2024-07-25T01:36:19+09:00
tags: ["Mathematica", "Mathématiques", "Algorithme"]
draft: false
image: "img.png"
categories: ["Mathématiques・Cryptographie・Quantique"]
---
# Introduction à Mathematica

## Résoudre des équations

```
Solve[x^2 - 3 x + 2 == 0, x]
```

Sortie
```
{{x -> 1}, {x -> 2}}
```

## Trouver les solutions d'une équation dans les entiers
```
Solve[x^2 - 3 x + 2 == 0 && 0 <= x <= 2, x, Integers]
```
Sortie
```
{{x -> 1}, {x -> 2}}
```

## Résoudre un système d'équations
```
Solve[{x + y == 3, x - y == 1}, {x, y}]
```
Sortie
```
{{x -> 2, y -> 1}}
```

## Résoudre des inéquations
```
Reduce[x^2 - 3 x + 2 > 0, x]
```
Sortie
```
x < 1 || x > 2
```

## Dériver
```
D[x^2, x]
```
Sortie
```
2 x
```

## Intégrer
```
Integrate[x^2, x]
```
Sortie
```
x^3/3
```

## Calculer une limite
```
Limit[1/x, x -> 0]
```
Sortie
```
Infinity
```

## Calculer une série
```
Sum[1/n^2, {n, 1, Infinity}]
```
Sortie
```
π^2/6
```

## Créer une matrice
```
m = {{1, 2}, {3, 4}}
```

## Calculer le produit de matrices
```
m . m
```
Sortie
```
{{7, 10}, {15, 22}}
```

## Calculer la matrice inverse
```
Inverse[m]
```
Sortie
```
{{-2, 1}, {1.5, -0.5}}
```

## Calculer les valeurs propres et les vecteurs propres
```
Eigensystem[m]
```
Sortie
```
{{5, 0}, {{1, 1}, {1, -1}}}
```

## Calculer le produit scalaire de vecteurs
```
{1, 2} . {3, 4}
```
Sortie
```
11
```

## Calculer le produit vectoriel
```
Cross[{1, 2, 3}, {4, 5, 6}]
```
Sortie
```
{-3, 6, -3}
```

## Calculer la norme d'un vecteur
```
Norm[{1, 2, 3}]
```
Sortie
```
√14
```

## Calculer l'angle entre des vecteurs
```
ArcCos[{1, 2} . {3, 4}/(Norm[{1, 2}] Norm[{3, 4}])]
``` 

Sortie
```
ArcCos[11/(√5 √25)]
```

## Calculer la projection d'un vecteur
```
{1, 2} . {3, 4}/Norm[{3, 4}] {3, 4}/Norm[{3, 4}]
```
Sortie
```
{11/5, 22/5}
```

## Calculer la rotation d'un vecteur
```
RotationMatrix[π/2].{1, 0}
```

Sortie
```
{0, 1}
```

## Calculer la translation d'un vecteur
```
TranslationTransform[{1, 2}][{3, 4}]
```
Sortie
```
{4, 6}
```

## Calculer la mise à l'échelle d'un vecteur
```
ScalingTransform[{2, 3}][{1, 1}]
```
Sortie
```
{2, 3}
```

## Calculer la réflexion d'un vecteur
```
ReflectionTransform[{1, 1}][{1, 1}]
```
Sortie
```
{0, 0}
```

## Générer des nombres aléatoires
```
RandomReal[]
```
Sortie
```
0.123456
```

## Générer des nombres aléatoires (entiers)
```
RandomInteger[]
```
Sortie
```
123456
```

## Générer des nombres aléatoires (plage spécifiée)
```
RandomReal[{1, 10}]
```
Sortie
```
5.6789
```

## Générer des nombres aléatoires (entiers, plage spécifiée)
```
RandomInteger[{1, 10}]
```
Sortie
```
5
```

## Générer des nombres aléatoires (distribution spécifiée)
```
RandomVariate[NormalDistribution[0, 1]]
```
Sortie
```
0.123456
```

## Générer des nombres aléatoires (distribution, quantité spécifiées)
```
RandomVariate[NormalDistribution[0, 1], 10]
```
Sortie
```
{0.123456, 0.234567, ..., 0.987654}
```

## Générer des nombres aléatoires (distribution, quantité, graine spécifiées)
```
SeedRandom[12345]
RandomVariate[NormalDistribution[0, 1], 10]
```
Sortie
```
{0.123456, 0.234567, ..., 0.987654}
```

## Appliquer une fonction aux éléments d'un tableau
```
Map[Sqrt, {1, 4, 9}]
Sqrt /@ {1, 4, 9}
Map[#^(1/2)&, {1, 4, 9}]
```
Sortie
```
{1, 2, 3}
```

## Définir une fonction avec des expressions lambda
```
f = Function[x, x^2]
f[3]
```
Sortie
```
9
```

## Composer des fonctions
```
f = Function[x, x^2]
g = Function[x, x + 1]
h = Function[x, f[g[x]]]
h[3]
```
Sortie
```
16
```

## Faire référence au résultat du calcul précédent
```
% + 1
```
Sortie
```
17
```

## Fonction pure
```
(#+3)&[5]
```
Sortie
```
8
```

## Extraction de tableau
```
Select[{1, 2, 3, 4, 5}, EvenQ]
Select[{1, 2, 3, 4, 5}, Mod[#,2]==0&]
```
Sortie
```
{2, 4}
```
