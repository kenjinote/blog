---
title: "Resolvendo o Problema do Caixeiro Viajante com Mathematica"
slug: "Resolvendo o Problema do Caixeiro Viajante com Mathematica"
date: 2022-10-12T19:05:58+09:00
tags: ["Mathematica", "Problema do Caixeiro Viajante", "Algoritmo", "Matemática"]
draft: false
image: "img.png"
categories: ["Matemática, Criptografia, Quântica"]
---
# Resolvendo o Problema do Caixeiro Viajante com Mathematica

## Problema
{{<twitter user="hayamizu_lab" id="1579806418982825984">}}

## Solução

```
d=SparseArray[{{1,2}->10,{2,1}->10,{1,5}->15,{5,1}->15,{1,4}->12,{4,1}->12,{1,3}->20,{3,1}->20,{2,5}->10,{5,2}->10,{3,4}->10,{4,3}->10,{3,8}->30,{8,3}->30,{3,7}->20,{7,3}->20,{3,6}->25,{6,3}->25,{4,5}->15,{5,4}->15,{4,8}->20,{8,4}->20,{5,9}->18,{9,5}->18,{5,8}->15,{8,5}->15,{6,7}->5,{7,6}->5,{7,8}->35,{8,7}->35,{8,9}->12,{9,8}->12},{9,9},Infinity];
```

Crie uma matriz usando a função SparseArray. Cada elemento representa a distância entre as cidades em sua respectiva linha e coluna. Por exemplo, o primeiro elemento `{1,2}->10` significa que a distância entre 1 e 2 é 10. O penúltimo elemento `{9,9}` indica o tamanho da matriz, e o último elemento `Infinity` significa que o comprimento do caminho entre cidades não especificadas é infinito, ou seja, não há caminho.

```
{len,tour}=FindShortestTour[{1,2,3,4,5,6,7,8,9},DistanceFunction->(d[[#1,#2]]&)]
```

Com a função FindShortestTour, você pode resolver facilmente o problema do caixeiro viajante. `{1,2,3,4,5,6,7,8,9}` representa os números das cidades. `DistanceFunction->(d[[#1,#2]]&)` passa a matriz d que representa a distância entre as cidades.

## Saída

```
{137, {1, 2, 5, 9, 8, 7, 6, 3, 4}}
```

A saída mostra a distância mais curta e a rota correspondente. A distância mais curta é `137`, e a rota é `1→2→5→9→8→7→6→3→4→1`. Convertendo para ordem alfabética ABC, torna-se `A, B, E, I, H, G, F, C, D`.
