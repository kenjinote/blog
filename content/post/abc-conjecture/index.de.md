---
title: "Die abc-Vermutung und IUT: ein beanspruchter Beweis und eine offene Debatte"
date: "2026-09-14T13:00:00+09:00"
lastmod: 2026-11-23
slug: "abc-conjecture"
image: "eyecatch.jpg"
categories: ["mathematics", "science"]
tags: ["ABC Conjecture", "Number Theory", "IUT Theory", "Shinichi Mochizuki"]
draft: false
description: "Ein Überblick über die abc-Vermutung, Mochizukis behaupteten Beweis mit IUT, die Veröffentlichung in PRIMS und die weiterhin ungelöste mathematische Kontroverse."
---

## Aussage der abc-Vermutung

Seien $a,b,c$ paarweise teilerfremde positive ganze Zahlen mit $a+b=c$. Das **Radikal** einer positiven ganzen Zahl $n$ ist das Produkt ihrer verschiedenen Primteiler:

$$\operatorname{rad}(n)=\prod_{p\mid n}p$$

Zum Beispiel gilt $\operatorname{rad}(2^3\cdot3^2)=6$. Das Radikal ignoriert die Exponenten der Primfaktoren und kann daher deutlich kleiner als die Zahl selbst sein.

Die abc-Vermutung besagt: Für jedes $\varepsilon>0$ gibt es eine Konstante $K_\varepsilon$, sodass für jedes solche Tripel

$$c\le K_\varepsilon\operatorname{rad}(abc)^{1+\varepsilon}$$

gilt. Die Konstante darf von $\varepsilon$ abhängen. Joseph Oesterlé und David Masser formulierten die Vermutung 1985. Sie beschreibt eine starke Einschränkung zwischen Addition und Primfaktorzerlegung; sie ist keine einfache Regel, nach der kleine Primfaktoren von $a$ und $b$ zwangsläufig einen großen Primfaktor von $c$ erzeugen.

## Mochizukis behaupteter Beweis mit IUT

2012 veröffentlichte Shinichi Mochizuki von der Universität Kyoto Arbeiten zur inter-universellen Teichmüller-Theorie (IUT) als neuem Rahmen für Probleme der diophantischen Geometrie, darunter die abc-Vermutung. IUT ist eine hoch technische Theorie über arithmetische Objekte wie elliptische Kurven über Zahlkörpern und verbindet Ideen aus der Teichmüller-Theorie, der Hodge-Arakelov-Theorie und der anabelschen Geometrie. Begriffe wie Hodge-Theater und Log-Theta-Gitter dienen dazu, arithmetische Daten zwischen Strukturen zu vergleichen. Eine bloße Beschreibung als „Addition und Multiplikation in getrennte Universen legen“ wäre irreführend.

Mochizuki behauptet, dass die abc-Vermutung aus IUT folgt. Die vier Arbeiten durchliefen ein langes Begutachtungsverfahren und erschienen 2021 in einer Sonderausgabe von *Publications of the Research Institute for Mathematical Sciences* (PRIMS). Die Veröffentlichung ist ein wichtiger Fakt, beweist aber für sich allein weder einen Konsens in der Mathematik noch das Ende der Debatte.

## Was umstritten bleibt

Peter Scholze und Jakob Stix argumentierten 2018 in einem Bericht, dass ein entscheidender Schritt – der Übergang von Satz 3.11 zu Korollar 3.12 in IUT III, der auf dem Weg zur abc-Ungleichung verwendet wird – eine Lücke enthalte. Mochizuki weist die Kritik als Missverständnis der Theorie zurück und erläuterte seine Position erneut in einem Bericht vom Oktober 2025. Dieser Abschnitt fasst die erklärten Positionen der Autoren zusammen; er ist keine unabhängige Prüfung des IUT-Beweises.

Eine sorgfältige Darstellung unterscheidet daher drei Punkte: Die IUT-Arbeiten erschienen in PRIMS; Mochizuki beansprucht, damit abc zu beweisen; und die Meinungsverschiedenheit über das zentrale Argument ist unter Mathematikern nicht beigelegt. Es wäre irreführend, die abc-Vermutung als allgemein anerkannten Satz darzustellen.

## Zusammenhang mit Fermats letztem Satz

Aus der abc-Vermutung würde Fermats letzter Satz folgen: Für $n\ge3$ gibt es keine positiven ganzzahligen Lösungen von $x^n+y^n=z^n$. Das ist eine bedingte Folgerung und bedeutet nicht, dass Fermats Satz noch unbewiesen wäre; Andrew Wiles und andere haben ihn bereits bewiesen.

Angenommen, es gäbe eine paarweise teilerfremde Lösung $x,y,z$. Dann wäre für jede positive ganze Zahl $k$ auch $(x^{nk},y^{nk},z^{nk})$ ein teilerfremdes Additionstripel. Sein Radikal bliebe gleich, $\operatorname{rad}(x^{nk}y^{nk}z^{nk})=\operatorname{rad}(xyz)$, während $z^{nk}$ unbegrenzt wüchse. Damit gäbe es unendlich viele Tripel, die für jedes feste $\varepsilon>0$ die abc-Schranke verletzen – ein Widerspruch.

## Quellen

- [Standardformulierung von abc (Jordan S. Ellenberg)](https://arxiv.org/abs/math/9909098)
- [PRIMS-Sonderausgabe zu IUT von 2021](https://ems.press/journals/prims/issues/1507)
- [Bericht von Scholze und Stix (2018)](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf)
- [IUT-Bericht von Mochizuki (Oktober 2025)](https://www.kurims.kyoto-u.ac.jp/~motizuki/IUT-report-2025-10.pdf)
- [Überblick über IUT (Mochizuki, 2012)](https://www.kurims.kyoto-u.ac.jp/~motizuki/Panoramic%20Overview%20of%20Inter-universal%20Teichmuller%20Theory.pdf)

Dies ist eine kurze Einführung in die Vermutung und die öffentlich ausgetragene Kontroverse, keine Rekonstruktion oder Bewertung des IUT-Beweises.
