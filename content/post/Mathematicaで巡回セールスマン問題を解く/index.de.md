---
title: "Lösung des Problems des Handlungsreisenden mit Mathematica"
slug: "loesung-des-problems-des-handlungsreisenden-mit-mathematica"
date: 2022-10-12T19:05:58+09:00
tags: ["Mathematica", "Problem des Handlungsreisenden", "Algorithmus", "Mathematik"]
draft: false
image: "img.png"
categories: ["Mathematik, Kryptographie, Quanten"]
---
# Lösung des Problems des Handlungsreisenden mit Mathematica

## Problem
{{<twitter user="hayamizu_lab" id="1579806418982825984">}}

## Lösung

```
d=SparseArray[{{1,2}->10,{2,1}->10,{1,5}->15,{5,1}->15,{1,4}->12,{4,1}->12,{1,3}->20,{3,1}->20,{2,5}->10,{5,2}->10,{3,4}->10,{4,3}->10,{3,8}->30,{8,3}->30,{3,7}->20,{7,3}->20,{3,6}->25,{6,3}->25,{4,5}->15,{5,4}->15,{4,8}->20,{8,4}->20,{5,9}->18,{9,5}->18,{5,8}->15,{8,5}->15,{6,7}->5,{7,6}->5,{7,8}->35,{8,7}->35,{8,9}->12,{9,8}->12},{9,9},Infinity];
```

Erstellen Sie eine Matrix mit der Funktion SparseArray. Jedes Element repräsentiert die Entfernung zwischen den Städten in seiner Zeile und Spalte. Das erste Element `{1,2}->10` bedeutet beispielsweise, dass die Entfernung zwischen 1 und 2 gleich 10 ist. Das vorletzte Element `{9,9}` gibt die Größe der Matrix an, und das letzte Element `Infinity` bedeutet, dass die Weglänge zwischen nicht angegebenen Städten unendlich ist, das heißt, es gibt keinen Weg.

```
{len,tour}=FindShortestTour[{1,2,3,4,5,6,7,8,9},DistanceFunction->(d[[#1,#2]]&)]
```

Mit der Funktion FindShortestTour können Sie das Problem des Handlungsreisenden ganz einfach lösen. `{1,2,3,4,5,6,7,8,9}` repräsentiert die Stadtnummern. `DistanceFunction->(d[[#1,#2]]&)` übergibt die Matrix d, die die Entfernung zwischen den Städten darstellt.

## Ausgabe

```
{137, {1, 2, 5, 9, 8, 7, 6, 3, 4}}
```

Die Ausgabe ist die kürzeste Entfernung und die Tourroute zu diesem Zeitpunkt. Die kürzeste Entfernung ist `137`, und die Tourroute ist `1→2→5→9→8→7→6→3→4→1`. Bei der Konvertierung in die alphabetische ABC-Reihenfolge wird es zu `A, B, E, I, H, G, F, C, D`.
