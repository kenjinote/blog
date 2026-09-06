---
title: "Résoudre le problème du voyageur de commerce avec Mathematica"
slug: "resoudre-le-probleme-du-voyageur-de-commerce-avec-mathematica"
date: 2022-10-12T19:05:58+09:00
tags: ["Mathematica", "Problème du voyageur de commerce", "Algorithme", "Mathématiques"]
draft: false
image: "img.png"
categories: ["Mathématiques, Cryptographie, Quantique"]
---
# Résoudre le problème du voyageur de commerce avec Mathematica

## Problème
{{<twitter user="hayamizu_lab" id="1579806418982825984">}}

## Solution

```
d=SparseArray[{{1,2}->10,{2,1}->10,{1,5}->15,{5,1}->15,{1,4}->12,{4,1}->12,{1,3}->20,{3,1}->20,{2,5}->10,{5,2}->10,{3,4}->10,{4,3}->10,{3,8}->30,{8,3}->30,{3,7}->20,{7,3}->20,{3,6}->25,{6,3}->25,{4,5}->15,{5,4}->15,{4,8}->20,{8,4}->20,{5,9}->18,{9,5}->18,{5,8}->15,{8,5}->15,{6,7}->5,{7,6}->5,{7,8}->35,{8,7}->35,{8,9}->12,{9,8}->12},{9,9},Infinity];
```

Créez une matrice à l'aide de la fonction SparseArray. Chaque élément représente la distance entre les villes à sa ligne et sa colonne. Par exemple, le premier élément `{1,2}->10` signifie que la distance entre 1 et 2 est de 10. L'avant-dernier élément `{9,9}` indique la taille de la matrice, et le dernier élément `Infinity` signifie que la longueur du chemin entre les villes non spécifiées est infinie, c'est-à-dire qu'il n'y a pas de chemin.

```
{len,tour}=FindShortestTour[{1,2,3,4,5,6,7,8,9},DistanceFunction->(d[[#1,#2]]&)]
```

Avec la fonction FindShortestTour, vous pouvez facilement résoudre le problème du voyageur de commerce. `{1,2,3,4,5,6,7,8,9}` représente les numéros de ville. `DistanceFunction->(d[[#1,#2]]&)` transmet la matrice d qui représente la distance entre les villes.

## Sortie

```
{137, {1, 2, 5, 9, 8, 7, 6, 3, 4}}
```

La sortie correspond à la distance la plus courte et à l'itinéraire de visite à ce moment-là. La distance la plus courte est `137` et l'itinéraire de la visite est `1→2→5→9→8→7→6→3→4→1`. En le convertissant dans l'ordre alphabétique ABC, il devient `A, B, E, I, H, G, F, C, D`.
