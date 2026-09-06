---
title: 'Solving the Traveling Salesperson Problem with Mathematica'
slug: "Mathematicaで巡回セールスマン問題を解く"
date: 2022-10-12T19:05:58+09:00
tags: ["Mathematica", "Traveling Salesperson Problem", "Algorithm", "Mathematics"]
draft: false
image: "img.png"
categories: ["Mathematics/Cryptography/Quantum"]
---
# Solving the Traveling Salesperson Problem with Mathematica

## Problem
{{<twitter user="hayamizu_lab" id="1579806418982825984">}}

## Solution

```
d=SparseArray[{{1,2}->10,{2,1}->10,{1,5}->15,{5,1}->15,{1,4}->12,{4,1}->12,{1,3}->20,{3,1}->20,{2,5}->10,{5,2}->10,{3,4}->10,{4,3}->10,{3,8}->30,{8,3}->30,{3,7}->20,{7,3}->20,{3,6}->25,{6,3}->25,{4,5}->15,{5,4}->15,{4,8}->20,{8,4}->20,{5,9}->18,{9,5}->18,{5,8}->15,{8,5}->15,{6,7}->5,{7,6}->5,{7,8}->35,{8,7}->35,{8,9}->12,{9,8}->12},{9,9},Infinity];
```

We create a matrix using the SparseArray function. Each element represents the distance between cities at the row and column of that element. For example, the first element `{1,2}->10` means the distance between 1 and 2 is 10. The second to last element `{9,9}` indicates the size of the matrix, and the final element `Infinity` means the length of paths between unspecified cities is infinite, meaning there is no path.

```
{len,tour}=FindShortestTour[{1,2,3,4,5,6,7,8,9},DistanceFunction->(d[[#1,#2]]&)]
```

You can easily solve the traveling salesperson problem with the FindShortestTour function. `{1,2,3,4,5,6,7,8,9}` represents the city numbers. `DistanceFunction->(d[[#1,#2]]&)` passes the matrix d which represents the distance between cities.

## Output

```
{137, {1, 2, 5, 9, 8, 7, 6, 3, 4}}
```

The output gives the shortest distance and the tour route for it. The shortest distance is `137`, and the route is `1→2→5→9→8→7→6→3→4→1`. Converting this to ABC order gives `A, B, E, I, H, G, F, C, D`.
