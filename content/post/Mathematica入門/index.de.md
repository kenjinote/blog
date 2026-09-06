---
title: "Einführung in Mathematica"
slug: "Mathematica入門"
date: 2024-07-25T01:36:19+09:00
tags: ["Mathematica", "Mathematik", "Algorithmus"]
draft: false
image: "img.png"
categories: ["Mathematik・Kryptographie・Quanten"]
---
# Einführung in Mathematica

## Gleichungen lösen

```
Solve[x^2 - 3 x + 2 == 0, x]
```

Ausgabe
```
{{x -> 1}, {x -> 2}}
```

## Lösungen von Gleichungen im Bereich der ganzen Zahlen finden
```
Solve[x^2 - 3 x + 2 == 0 && 0 <= x <= 2, x, Integers]
```
Ausgabe
```
{{x -> 1}, {x -> 2}}
```

## Gleichungssysteme lösen
```
Solve[{x + y == 3, x - y == 1}, {x, y}]
```
Ausgabe
```
{{x -> 2, y -> 1}}
```

## Ungleichungen lösen
```
Reduce[x^2 - 3 x + 2 > 0, x]
```
Ausgabe
```
x < 1 || x > 2
```

## Ableiten
```
D[x^2, x]
```
Ausgabe
```
2 x
```

## Integrieren
```
Integrate[x^2, x]
```
Ausgabe
```
x^3/3
```

## Grenzwerte berechnen
```
Limit[1/x, x -> 0]
```
Ausgabe
```
Infinity
```

## Reihen berechnen
```
Sum[1/n^2, {n, 1, Infinity}]
```
Ausgabe
```
π^2/6
```

## Matrix erstellen
```
m = {{1, 2}, {3, 4}}
```

## Matrixprodukt berechnen
```
m . m
```
Ausgabe
```
{{7, 10}, {15, 22}}
```

## Inverse Matrix berechnen
```
Inverse[m]
```
Ausgabe
```
{{-2, 1}, {1.5, -0.5}}
```

## Eigenwerte und Eigenvektoren berechnen
```
Eigensystem[m]
```
Ausgabe
```
{{5, 0}, {{1, 1}, {1, -1}}}
```

## Skalarprodukt von Vektoren berechnen
```
{1, 2} . {3, 4}
```
Ausgabe
```
11
```

## Kreuzprodukt von Vektoren berechnen
```
Cross[{1, 2, 3}, {4, 5, 6}]
```
Ausgabe
```
{-3, 6, -3}
```

## Betrag eines Vektors berechnen
```
Norm[{1, 2, 3}]
```
Ausgabe
```
√14
```

## Winkel von Vektoren berechnen
```
ArcCos[{1, 2} . {3, 4}/(Norm[{1, 2}] Norm[{3, 4}])]
``` 

Ausgabe
```
ArcCos[11/(√5 √25)]
```

## Projektion von Vektoren berechnen
```
{1, 2} . {3, 4}/Norm[{3, 4}] {3, 4}/Norm[{3, 4}]
```
Ausgabe
```
{11/5, 22/5}
```

## Rotation von Vektoren berechnen
```
RotationMatrix[π/2].{1, 0}
```

Ausgabe
```
{0, 1}
```

## Translation von Vektoren berechnen
```
TranslationTransform[{1, 2}][{3, 4}]
```
Ausgabe
```
{4, 6}
```

## Skalierung von Vektoren berechnen
```
ScalingTransform[{2, 3}][{1, 1}]
```
Ausgabe
```
{2, 3}
```

## Reflexion von Vektoren berechnen
```
ReflectionTransform[{1, 1}][{1, 1}]
```
Ausgabe
```
{0, 0}
```

## Zufallszahlen generieren
```
RandomReal[]
```
Ausgabe
```
0.123456
```

## Zufallszahlen generieren (ganze Zahlen)
```
RandomInteger[]
```
Ausgabe
```
123456
```

## Zufallszahlen generieren (Bereich angegeben)
```
RandomReal[{1, 10}]
```
Ausgabe
```
5.6789
```

## Zufallszahlen generieren (ganze Zahlen, Bereich angegeben)
```
RandomInteger[{1, 10}]
```
Ausgabe
```
5
```

## Zufallszahlen generieren (Verteilung angegeben)
```
RandomVariate[NormalDistribution[0, 1]]
```
Ausgabe
```
0.123456
```

## Zufallszahlen generieren (Verteilung, Menge angegeben)
```
RandomVariate[NormalDistribution[0, 1], 10]
```
Ausgabe
```
{0.123456, 0.234567, ..., 0.987654}
```

## Zufallszahlen generieren (Verteilung, Menge, Seed angegeben)
```
SeedRandom[12345]
RandomVariate[NormalDistribution[0, 1], 10]
```
Ausgabe
```
{0.123456, 0.234567, ..., 0.987654}
```

## Funktion auf Array-Elemente anwenden
```
Map[Sqrt, {1, 4, 9}]
Sqrt /@ {1, 4, 9}
Map[#^(1/2)&, {1, 4, 9}]
```
Ausgabe
```
{1, 2, 3}
```

## Funktion mit Lambda-Ausdrücken definieren
```
f = Function[x, x^2]
f[3]
```
Ausgabe
```
9
```

## Funktionen komponieren
```
f = Function[x, x^2]
g = Function[x, x + 1]
h = Function[x, f[g[x]]]
h[3]
```
Ausgabe
```
16
```

## Auf vorheriges Berechnungsergebnis verweisen
```
% + 1
```
Ausgabe
```
17
```

## Reine Funktion
```
(#+3)&[5]
```
Ausgabe
```
8
```

## Array extrahieren
```
Select[{1, 2, 3, 4, 5}, EvenQ]
Select[{1, 2, 3, 4, 5}, Mod[#,2]==0&]
```
Ausgabe
```
{2, 4}
```
