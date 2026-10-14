---
title: "Kann Papierfalten die Grenzen von Zirkel und Lineal sprengen? Die tiefe Mathematik des Origami"
date: 2026-10-14T01:00:00+09:00
draft: false
slug: "origami-mathematics-axioms-geometric-constructions-angle-trisection"
tags:
  - Mathematik
  - Geometrie
  - Abstrakte Algebra
  - Origami-Ingenieurwesen
  - Wissenschaftsgeschichte
categories:
  - Mathematik
image: "eyecatch.jpg"
math: true
---

Über zwei Jahrtausende lang bissen sich die Mathematiker der Antike an den <strong>drei klassischen Problemen der antiken Geometrie</strong> die Zähne aus:
1. <strong>Die Dreiteilung des Winkels</strong>: Einen beliebigen Winkel nur mit Zirkel und unmarkiertem Lineal in drei gleiche Teile zu teilen.
2. <strong>Die Verdoppelung des Würfels (Delisches Problem)</strong>: Die Kantenlänge eines Würfels mit doppeltem Volumen zu konstruieren ($\sqrt[3]{2}$).
3. <strong>Die Quadratur des Kreises</strong>: Ein Quadrat mit demselben Flächeninhalt wie ein gegebener Kreis zu konstruieren ($\sqrt{\pi}$).

1837 bewies Pierre Wantzel mit Mitteln der Körpertheorie, dass Zirkel und Lineal algebraisch strikt auf Ketten quadratischer Körpererweiterungen ($[K : \mathbb{Q}] = 2^k$) beschränkt sind. Da die Dreiteilung des Winkels und die Verdoppelung des Würfels irreduzible kubische Polynome ($x^3 - 3x - 1 = 0$ und $x^3 - 2 = 0$) vom Grad 3 erfordern, ist ihre Konstruktion mit euklidischen Werkzeugen <strong>vollkommen unmöglich</strong>.

Doch im 20. Jahrhundert ereignete sich eine wissenschaftliche Sensation:
<strong>Durch das einfache, physikalische Falten eines quadratischen Blattes Papier lassen sich sowohl die Dreiteilung des Winkels als auch $\sqrt[3]{2}$ in Sekundenschnelle präzise und elegant konstruieren!</strong>

Origami ist nicht bloß Kunst oder Spielerei, sondern ein <strong>mächtiger analoger geometrischer Computer zur Lösung kubischer Gleichungen</strong>.

---

## 1. Das Huzita-Hatori-Axiomensystem

Papierfalten entspricht der Spiegelung an einer Geraden (der Faltkante). Zwischen 1989 und 2001 formulierten Humiaki Huzita, Jacques Justin und Koshiro Hatori die <strong>sieben Axiome des Origami</strong>:

```mermaid
flowchart TD
    A1["Axiom 1: Gerade durch 2 Punkte falten (Grad 1)"]
    A2["Axiom 2: Punkt auf Punkt falten (Mittelsenkrechte: Grad 1)"]
    A3["Axiom 3: Gerade auf Gerade falten (Winkelhalbierende: Grad 1)"]
    A4["Axiom 4: Lot durch Punkt auf Gerade falten (Grad 1)"]
    A5["Axiom 5: Punkt auf Gerade durch einen anderen Punkt falten (Grad 2)"]
    A7["Axiom 7: Punkt auf Gerade senkrecht zu anderer Gerade falten (Grad 2)"]
    A6["Axiom 6: Zwei Punkte P1, P2 SIMULTAN auf zwei Geraden L1, L2 falten!<br/>【Gemeinsame Tangente zweier Parabeln: Kubische Gleichung!】"]
end
```

Während die Axiome 1 bis 5 und 7 nur lineare und quadratische Probleme lösen, sprengt <strong>Axiom 6</strong> alle euklidischen Grenzen.

---

## 2. Wie Axiom 6 kubische Gleichungen löst

Faltet man einen Punkt $P$ auf eine Gerade $L$, ist die Faltlinie die Mittelsenkrechte. Geometrisch ist jede solche Faltlinie eine <strong>Tangente an die Parabel</strong> mit Brennpunkt $P$ und Leitlinie $L$!

Axiom 6 verlangt, zwei Punkte $P_1, P_2$ gleichzeitig auf zwei Geraden $L_1, L_2$ zu falten.
Die Faltlinie ist daher nichts anderes als die <strong>gemeinsame Tangente zweier verschiedener Parabeln</strong>.
In Koordinaten führt der Koeffizientenvergleich der Tangentensteigung $m$ unweigerlich zu einer <strong>kubischen Gleichung 3. Grades</strong>:

$$
A m^3 + B m^2 + C m + D = 0
$$

Das gleichzeitige Anlegen zweier Punkte an zwei Linien beim Falten ist eine physikalische Gradientensuche, die eine reelle Nullstelle des kubischen Polynoms exakt bestimmt.

---

## 3. Abes Winkeldreiteilung und Messers Würfelverdoppelung

### 3.1 Die Winkeldreiteilung nach Hisashi Abe (1980)
Der japanische Geometer Hisashi Abe zeigte, wie man jeden spitzen Winkel $\angle ABC$ dreiteilt:
1. Man faltet zwei Parallelen $L_1, L_2$ zur Grundlinie $BC$ im gleichen Abstand $d$.
2. Man errichtet das Lot in $B$ mit Punkten $P \in L_1, Q \in L_2$ ($BP = PQ = d$).
3. <strong>Axiom 6</strong>: Man faltet das Papier so, dass Punkt $B$ auf $L_2$ und Punkt $P$ auf dem Schenkel $BA$ zu liegen kommt!
4. Beim Entfalten schneidet die entstehende Linie exakt $\frac{1}{3} \angle ABC$ ab.

### 3.2 Die Konstruktion von $\sqrt[3]{2}$ nach Peter Messer (1986)
Faltet man ein Einheitsquadrat in drei Streifen und wendet Axiom 6 geschickt an, entsteht an der Kante eine Strecke der Länge $\sqrt[3]{2} - 1$. Addiert man 1, ist das Delische Problem gelöst! Der Körper der <strong>Origami-Zahlen $\mathcal{O}$</strong> besitzt Erweiterungsgrade der Form:
$$
[\mathbb{Q}(\alpha) : \mathbb{Q}] = 2^a \cdot 3^b
$$
Daher sind auch regelmäßige 7-Ecke und 9-Ecke mit Origami exakt konstruierbar!

---

## 4. Flache Faltbarkeit: Kawasakis und Maekawas Theoreme

- <strong>Satz von Kawasaki</strong>: Ein Faltmuster mit einem Knotenpunkt ist genau dann flach faltbar, wenn die alternierende Summe der Zwischenwinkel $180^\circ$ beträgt ($\theta_1 + \theta_3 + \dots = 180^\circ$).
- <strong>Satz von Maekawa</strong>: An jedem flach gefalteten inneren Knotenpunkt differiert die Zahl der Bergfalten ($M$) und Talfalten ($V$) stets um genau $\pm 2$ ($M - V = \pm 2$).
- <strong>NP-Vollständigkeit</strong>: Die Frage, ob ein beliebiges Faltmuster mit vielen Knoten flach faltbar ist, ist NP-vollständig (Bern & Demaine, 1996).

---

## 5. Origami-Ingenieurwesen: Von der Raumfahrt zur Nanomedizin

- <strong>Miura-Faltung (Miura-ori)</strong>: 1970 von Koryo Miura erfunden; starre Flächen entfalten sich synchron mit nur einem Freiheitsgrad. Erfolgreich im All (SFU-Satellit 1995, James-Webb-Weltraumteleskop).
- <strong>Medizinische Stents</strong>: Im Katheter ultrakompakt gefaltet, entfalten sich Origami-Röhrchen im verengten Blutgefäß selbstständig.
- <strong>Auxetische Metamaterialien</strong>: Materialien mit negativer Querkontraktionszahl (dehnen sich bei Längszug auch quer aus) revolutionieren den Leichtbau.

---

## 6. Fazit

Indem Origami die künstlichen Fesseln von Zirkel und Lineal durch die reiche Physik eines gefalteten Blattes ersetzte, eröffnete es der Mathematik ein neues Universum.
