---



title: "Resolver el problema del viajante con Mathematica"
slug: "Mathematicaで巡回セールスマン問題を解く"
date: 2022-10-12T19:05:58+09:00
tags: ["Mathematica", "Problema del viajante", "Algoritmos", "Matemáticas"]
draft: false
image: "img.png"
categories: ["Matemáticas, Criptografía, Cuántica"]
---



# Resolver el problema del viajante con Mathematica

## Problema
{{<twitter user="hayamizu_lab" id="1579806418982825984">}}

## Solución

```
d=SparseArray[{{1,2}->10,{2,1}->10,{1,5}->15,{5,1}->15,{1,4}->12,{4,1}->12,{1,3}->20,{3,1}->20,{2,5}->10,{5,2}->10,{3,4}->10,{4,3}->10,{3,8}->30,{8,3}->30,{3,7}->20,{7,3}->20,{3,6}->25,{6,3}->25,{4,5}->15,{5,4}->15,{4,8}->20,{8,4}->20,{5,9}->18,{9,5}->18,{5,8}->15,{8,5}->15,{6,7}->5,{7,6}->5,{7,8}->35,{8,7}->35,{8,9}->12,{9,8}->12},{9,9},Infinity];
```

La función SparseArray crea una matriz. Cada elemento representa la distancia entre las ciudades de la fila y columna de ese elemento. Por ejemplo, el primer elemento `{1,2}->10` significa que la distancia entre 1 y 2 es 10. El penúltimo elemento `{9,9}` indica el tamaño de la matriz, y el último elemento `Infinity` significa que la longitud del camino entre ciudades no especificadas es infinita. Es decir, significa que no hay camino.

```
{len,tour}=FindShortestTour[{1,2,3,4,5,6,7,8,9},DistanceFunction->(d[[#1,#2]]&)]
```

Con la función FindShortestTour, puedes resolver fácilmente el problema del viajante. `{1,2,3,4,5,6,7,8,9}` representa los números de las ciudades. `DistanceFunction->(d[[#1,#2]]&)` pasa la matriz d que representa la distancia entre las ciudades.

## Salida

```
{137, {1, 2, 5, 9, 8, 7, 6, 3, 4}}
```

La salida es la distancia más corta y el recorrido en ese momento. La distancia más corta es `137`, y el recorrido es `1→2→5→9→8→7→6→3→4→1`. Convertido al orden ABC, es `A, B, E, I, H, G, F, C, D`.
