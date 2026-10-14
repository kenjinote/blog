---
title: "Wie teilt man einen Kuchen 'gerecht'? Die Mathematik neidfreier Aufteilungen"
date: 2026-10-14T01:00:00+09:00
draft: false
slug: "fair-division-cake-cutting-envy-free-proportionality-mathematics"
tags:
  - Mathematik
  - Spieltheorie
  - Entscheidungstheorie
  - Algorithmen
  - Wirtschaftswissenschaften
categories:
  - Mathematik
image: "eyecatch.jpg"
math: true
---

Wenn Geschwister einen Geburtstagskuchen teilen, Erben einen Nachlass aufteilen oder Mitbewohner Zimmer und Miete verteilen, stoßen wir auf das fundamentale Problem der <strong>Gerechtigkeit (Fairness)</strong>.

Die älteste intuitive Lösung für zwei Personen lautet: *„Einer teilt, der andere wählt (Cut and Choose)“*. Der Teilende bemüht sich um exakte Gleichheit, um sich selbst abzusichern, während der Wählende das bevorzugte Stück nimmt.

Doch was geschieht bei <strong>drei oder mehr Personen</strong>?
Und was passiert, wenn der Kuchen ungleichmäßig belegt ist – links Schokolade, rechts Erdbeeren – und die Vorlieben der Teilnehmer stark asymmetrisch sind? Teilt man den Kuchen nach reinem geometrischem Volumen in drei gleiche Teile, fühlt sich der Erdbeer-Allergiker betrogen.

Gibt es ein mathematisches Verfahren, das garantiert, dass jeder Teilnehmer nach seinen ganz eigenen Maßstäben zufrieden ist und <strong>niemand das Stück eines anderen beneidet</strong>?

Dies ist das zentrale Forschungsgebiet der <strong>fairen Aufteilung (Fair Division)</strong>, bekannt als <strong>Kuchenteilungs-Problem (Cake-Cutting Problem)</strong>. Seit seiner mathematischen Formulierung durch Hugo Steinhaus in den 1940er Jahren hat es sich zu einer hochentwickelten Disziplin entwickelt, die Maßtheorie, Topologie (Fixpunktsätze und Sperners Lemma), Spieltheorie und Algorithmen vereint. 2016 gelang Haris Aziz und Simon Mackenzie ein historischer Durchbruch: der erste beschränkte, endliche neidfreie Algorithmus für beliebig viele Teilnehmer.

---

## 1. Mathematische Modellierung: Maßtheorie des Geschmacks

### 1.1 Der Kuchen als metrischer Raum
Der Kuchen wird als reelles Intervall $X = [0, 1]$ modelliert. Jedes Teilstück ist eine messbare Borel-Menge $A \in \mathcal{B}(X)$.

### 1.2 Subjektive Wertmaße
Jeder Teilnehmer $i \in \{1, \dots, n\}$ besitzt ein privates Wertmaß $V_i: \mathcal{B}(X) \to [0, 1]$, das folgenden Axiomen genügt:
1. <strong>Normierung</strong>: $V_i(X) = 1, V_i(\emptyset) = 0$.
2. <strong>Nicht-Negativität</strong>: $V_i(A) \ge 0$.
3. <strong>Additivität</strong>: Für disjunkte Stücke gilt $V_i(A \cup B) = V_i(A) + V_i(B)$.
4. <strong>Nicht-Atomarität (Teilbarkeit)</strong>: Zu jedem Stück $A$ und Skalar $\alpha \in [0, 1]$ existiert ein Teilstück $B \subset A$ mit $V_i(B) = \alpha V_i(A)$.

Das Geniale an diesem Modell: <strong>Die Teilnehmer müssen sich in ihren Präferenzen keineswegs einig sein</strong>. Jeder bewertet den Kuchen ausschließlich nach seiner inneren Dichtefunktion $v_i(x)$.

---

## 2. Vier Kriterien der Gerechtigkeit: Proportionalität vs. Neidfreiheit

Bei einer Partition $(X_1, \dots, X_n)$ unterscheidet die Mathematik vier Stufen der Fairness:

| Kriterium | Formale Definition | Bedeutung |
| :---: | :---: | :---: |
| <strong>Proportionalität (PROP)</strong> | $\forall i, \quad V_i(X_i) \ge \frac{1}{n}$ | Jeder erhält nach eigenem Maßstab mindestens $1/n$ des Gesamtwerts |
| <strong>Neidfreiheit (EF)</strong> | $\forall i, j, \quad V_i(X_i) \ge V_i(X_j)$ | Niemand bevorzugt das Stück eines anderen gegenüber dem eigenen |
| <strong>Gleichheit (Equitability)</strong> | $\forall i, j, \quad V_i(X_i) = V_j(X_j)$ | Alle verspüren denselben numerischen subjektiven Nutzen |
| <strong>Pareto-Effizienz (PE)</strong> | Keine Umverteilung nützt jemandem, ohne einem anderen zu schaden | Perfekte Ressourcen-Nutzung ohne Verschwendung |

### Warum Neidfreiheit viel stärker ist als Proportionalität
Bei zwei Personen ($n=2$) fallen beide Kriterien zusammen. Bei drei Personen jedoch reicht Proportionalität nicht aus, um Neid zu verhindern!
Angenommen, Alice schätzt drei Stücke wie folgt ein:
- Eigenes Stück $X_1$: $0.35$ ($> 1/3$, proportional!)
- Bobs Stück $X_2$: $0.50$
- Charlies Stück $X_3$: $0.15$

Alice hat mehr als ihr zustehendes Drittel erhalten, doch sie empfindet brennenden Neid auf Bob, der in ihren Augen $50\%$ des Kuchens besitzt. <strong>Neidfreiheit (Envy-Freeness)</strong> ist das Goldstandard-Kriterium für echten sozialen Frieden.

---

## 3. Das 2-Personen-Verfahren: "Cut and Choose"

```mermaid
sequenceDiagram
    autonumber
    actor A as Spieler 1 (Teilender / Cutter)
    actor B as Spieler 2 (Wählender / Chooser)
    Note over A: Teilt den Kuchen bei c, sodass<br/>V1([0, c]) = 1/2 und V1([c, 1]) = 1/2
    A->>B: Präsentiert Stücke X1 und X2
    Note over B: Bewertet beide Stücke unter V2
    alt V2(X1) >= V2(X2)
        B->>B: Wählt Stück X1
        A->>A: Erhält restliches Stück X2
    else V2(X2) > V2(X1)
        B->>B: Wählt Stück X2
        A->>A: Erhält restliches Stück X1
    end
    Note over A,B: Beide erhalten >= 1/2; Neid = 0!
```

Spieltheoretisch hat der <strong>Wählende (Chooser)</strong> einen massiven strategischen Vorteil (Informationsrente): Der Teilende muss exakt $50:50$ teilen und bleibt bei $50\%$ Nutzen stehen. Weichen die Geschmäcker ab, kann der Wählende $80\%$ oder $100\%$ des subjektiven Nutzens für sich beanspruchen.

---

## 4. Das Selfridge-Conway-Verfahren für 3 Personen

Um 1960 entdeckten John Selfridge und John Horton Conway ein diskretes Protokoll mit maximal 5 Schnitten für 3 Personen:

1. <strong>Stufe 1 (Hauptkuchen und Trimmen)</strong>:
   - $P_1$ teilt den Kuchen in drei für ihn exakt gleichwertige Teile $A, B, C$.
   - $P_2$ begutachtet die Stücke. Wenn ein Stück (z. B. $A$) eindeutig das größte ist, schneidet $P_2$ einen Randstreifen (Abschnitt $T$) ab, sodass der Rest $A'$ mit dem zweitgrößten Stück gleichwertig ist.
   - Auswahl: $P_3$ wählt zuerst. Dann wählt $P_2$ (muss $A'$ nehmen, falls $P_3$ es nicht nahm). Zuletzt nimmt $P_1$ das verbleibende Stück.
   - Da $P_1$ ein unversehrtes Stück mit Wert $1/3$ erhält, beneidet $P_1$ niemanden!
2. <strong>Stufe 2 (Neidfreie Verteilung des Rests $T$)</strong>:
   - Sei $T_{\text{in}}$ der Spieler, der $A'$ erhalten hat, und $T_{\text{out}}$ der andere aus $\{P_2, P_3\}$.
   - $T_{\text{out}}$ teilt $T$ in drei gleiche Stücke.
   - Auswahlreihenfolge: $T_{\text{in}} \to P_1 \to T_{\text{out}}$.
   - <strong>Clou</strong>: $P_1$ beneidet $T_{\text{in}}$ niemals, denn selbst mit ganz $T$ erreicht $A'$ in den Augen von $P_1$ höchstens den Wert $1/3$, den $P_1$ bereits besitzt!

---

## 5. Topologie und Mieten-Harmonie: Sperners Lemma

Francis Su bewies 1999 mithilfe von <strong>Sperners Lemma</strong> (einem kombinatorischen Äquivalent des Brouwerschen Fixpunktsatzes), dass sich Zimmer und Gesamtmiete in einer WG stets so aufteilen lassen, dass jeder Mitbewohner ein anderes Zimmer wählt und vollkommen neidfrei bleibt (*Rental Harmony*).

---

## 6. Fazit

Gerechtigkeit bedeutet nicht mechanische Gleichmacherei, sondern die Achtung individueller Werte. Durch mathematisches Mechanismusdesign verwandelt die Spieltheorie menschlichen Neid in harmonische Kooperation.
