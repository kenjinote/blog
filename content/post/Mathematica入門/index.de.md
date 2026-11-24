---
title: 'Einführung in Mathematica: Verwendung grundlegender Befehle für Gleichungen, Differential- und Integralrechnung usw.'
slug: "Mathematica入門"
date: 2024-07-25T01:36:19+09:00
tags: ["Mathematica", "Mathematik", "Algorithmus"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: 'Erklärt die grundlegende Verwendung und Berechnungsbefehle von Mathematica für Anfänger. Fasst konkrete Beispiele häufig verwendeter Funktionen zusammen, wie das Lösen von Gleichungen und Gleichungssystemen (Solve), Ungleichungen (Reduce), Differenziation (D), Integration (Integrate) und Matrixberechnungen.'
lastmod: "2026-11-24T00:00:00+09:00"
mermaid: true
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
Limit[1/x, x -> 0, Direction -> "FromAbove"]
```
Ausgabe
```
Infinity
```

Der rechtsseitige Grenzwert für x gegen 0 ist Infinity. Der zweiseitige reelle Grenzwert existiert nicht. Direction legt die Annäherungsrichtung fest.

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
{{-2, 1}, {3/2, -1/2}}
```

## [Eigenwerte und Eigenvektoren](https://kenji.blog/de/p/eigenvalues-and-eigenvectors/) berechnen
```
Eigensystem[m]
```
Ausgabe
```
{{(5 + Sqrt[33])/2, (5 - Sqrt[33])/2}, {{2, (3 + Sqrt[33])/2}, {2, (3 - Sqrt[33])/2}}}
```

Die Eigenwerte dieser Matrix sind (5 ± √33)/2. Reihenfolge und Skalierung der Eigenvektoren können abweichen; jedes Paar erfüllt m.v = λv.

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
Projection[{1, 2}, {3, 4}]
```
Ausgabe
```
{33/25, 44/25}
```

Die orthogonale Projektion von {1,2} auf {3,4} verwendet das Skalarproduktverhältnis 11/25 und ergibt {33/25,44/25}.







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
ReflectionTransform[{0, 1}][{1, 1}]
```
Ausgabe
```
{1, -1}
```

Das erste Argument von ReflectionTransform ist die Normale der Spiegelebene. Die Normale {0,1} definiert die x-Achse und bildet {1,1} auf {1,-1} ab.

Die folgenden Zufallswerte dienen nur als Beispiel und ändern sich bei jeder Auswertung. RandomInteger[] liefert 0 oder 1. SeedRandom reproduziert eine Folge mit demselben Generator und derselben Version.









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
0
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
{0.123456, 0.234567, 0.345678, 0.456789, 0.567890, 0.678901, 0.789012, 0.890123, 0.901234, 0.012345}
```

## Zufallszahlen generieren (Verteilung, Menge, Seed angegeben)
```
SeedRandom[12345]
RandomVariate[NormalDistribution[0, 1], 10]
```
Ausgabe
```
(* Output intentionally omitted: exact sequence depends on the Wolfram Language version. *)
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

## Funktion mit [Lambda](https://kenji.blog/de/p/serverless-architecture-aws-lambda-cold-start/)-Ausdrücken definieren
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


## Offizielle Funktionsdokumentation

[Solve](https://reference.wolfram.com/language/ref/Solve.html) · [Reduce](https://reference.wolfram.com/language/ref/Reduce.html) · [D](https://reference.wolfram.com/language/ref/D.html) · [Integrate](https://reference.wolfram.com/language/ref/Integrate.html) · [Limit](https://reference.wolfram.com/language/ref/Limit.html) · [Sum](https://reference.wolfram.com/language/ref/Sum.html) · [Inverse](https://reference.wolfram.com/language/ref/Inverse.html) · [Eigensystem](https://reference.wolfram.com/language/ref/Eigensystem.html) · [Projection](https://reference.wolfram.com/language/ref/Projection.html) · [RotationMatrix](https://reference.wolfram.com/language/ref/RotationMatrix.html) · [ReflectionTransform](https://reference.wolfram.com/language/ref/ReflectionTransform.html) · [RandomReal](https://reference.wolfram.com/language/ref/RandomReal.html) · [RandomInteger](https://reference.wolfram.com/language/ref/RandomInteger.html) · [RandomVariate](https://reference.wolfram.com/language/ref/RandomVariate.html)
