---
title: "Sekretärinnenproblem / Problem des optimalen Stoppens (Secretary Problem) - Die \"1/e-Regel\" zur Einstellung der besten Person"
description: "Was ist das Sekretärinnenproblem (Secretary Problem)? Anhand dieses repräsentativen Beispiels für das Problem des optimalen Stoppens erläutern wir detailliert den mathematischen Ansatz \"1/e-Regel (ca. 37%-Regel)\", um unter unsicheren Bedingungen die beste Wahl zu treffen. Mit mathematischen Beweisen und Simulationen untersuchen wir, wie dies bei der Personalbeschaffung und bei alltäglichen Entscheidungen genutzt werden kann."
slug: "secretary-problem"
date: "2026-09-14T13:20:00+09:00"
image: "eyecatch.jpg"
categories: ["mathematics", "algorithms", "decision-making"]
tags:
  - "Optimales Stoppen"
  - "Sekretärinnenproblem"
  - "Wahrscheinlichkeitstheorie"
  - "Mathe"
---

## Was ist das Sekretärinnenproblem (Secretary Problem)?

Das **Sekretärinnenproblem** (Secretary Problem) ist eines der bekanntesten und klassischsten Beispiele für das **Problem des optimalen Stoppens** (Optimal Stopping Problem) in der angewandten Wahrscheinlichkeitstheorie. Dieses Problem, das auch als Heiratsproblem (Marriage Problem) oder Mitgiftproblem des Sultans (Sultan's Dowry Problem) bezeichnet wird, modelliert hervorragend das Dilemma der Entscheidungsfindung, wie man unter Unsicherheit die **beste Wahl** treffen sollte.

Alle möglichen Alltagssituationen, wie "Wann sollte man ein Haus kaufen", "Wann sollte man sich für einen Parkplatz entscheiden" oder "Wann sollte man sich für einen Partner entscheiden", können letztendlich auf dieses Problem zurückgeführt werden.

### Grundeinstellungen des Problems

Das Sekretärinnenproblem wird unter den folgenden strengen Regeln betrachtet.

1. **Eine offene Stelle**: Man möchte eine einzelne Sekretärin einstellen.
2. **Anzahl der Kandidaten ist bekannt**: Die Gesamtzahl der Bewerber $N$ ist im Voraus bekannt.
3. **Sequentielle Interviews**: Die Kandidaten werden in zufälliger Reihenfolge einzeln interviewt, und die Entscheidung für oder gegen eine Einstellung muss auf der Stelle getroffen werden.
4. **Nur relative Bewertung**: Man kann Kandidaten mit früheren vergleichen, aber keine absolute Punktzahl vergeben (d. h. man weiß nur, ob der aktuelle Kandidat der bisher beste ist).
5. **Kein Zurück**: Ein einmal abgelehnter Kandidat kann nicht später eingestellt werden.
6. **Ziel**: Die Maximierung der Wahrscheinlichkeit, den **besten Kandidaten** (den Kandidaten mit dem wahren Rang 1) einzustellen. Die Einstellung jedes anderen Kandidaten (z. B. des zweitbesten) gilt als Misserfolg.

Wie kann man unter diesen strengen Bedingungen die Wahrscheinlichkeit maximieren, die "beste Person" zu finden?

---

## Intuition vs. Mathematik

Intuitiv besteht bei einer zu frühen Entscheidung das Risiko, bessere Kandidaten zu verpassen, die vielleicht noch übrig sind. Wenn man andererseits zu vorsichtig ist und bis zum Ende wartet, steigt das Risiko, dass man den besten Kandidaten bereits abgelehnt hat.

Die optimale Strategie, die von der Mathematik abgeleitet wurde, ist eine einfache Regel wie folgt.

> **Die ersten $r-1$ Kandidaten werden bedingungslos abgelehnt (sie dienen als "Maßstab"), und bei den nachfolgenden Kandidaten wird sofort die Person eingestellt, die besser ist als alle bisherigen.**

Wie groß sollte nun diese Maßstabsgröße $r-1$ (oder Beobachtungszeitraum) eingestellt werden, um die Erfolgswahrscheinlichkeit zu maximieren?

---

## Die 1/e-Regel (ca. 37%-Regel)

Um gleich zum Ergebnis zu kommen: Wenn die Anzahl der Kandidaten $N$ ausreichend groß ist, lautet die optimale Strategie: **"Verbringe die ersten ca. 37% der Kandidaten mit der Beobachtung (Erstellung eines Maßstabs) und stelle dann den ersten Kandidaten ein, der diesen Maßstab übertrifft."**

Diese Zahl "37%" wird als $1/e$ ausgedrückt, wobei die Basis des natürlichen Logarithmus $e \approx 2.718$ verwendet wird.
$$ \frac{1}{e} \approx 0.367879 \dots $$

Erstaunlicherweise beträgt bei Anwendung dieser Strategie die Wahrscheinlichkeit, den besten Kandidaten erfolgreich einzustellen, ebenfalls **$1/e$ (ca. 37%)**. Egal, ob es 100 oder 1 Million Kandidaten gibt, wenn man dieser Regel folgt, hat man eine Wahrscheinlichkeit von etwa 37%, den Besten zu treffen.

### Flussdiagramm: Algorithmus des optimalen Stoppens

Das folgende Diagramm visualisiert den Algorithmus dieses Prozesses.

```mermaid
graph TD
    A["Interview-Start (Gesamtzahl Kandidaten N)"] --> B{"Kandidat n <= N/e (ca. 37%)?"}
    B -->|"Ja"| C["Bedingungslos ablehnen und Bestbewertung aktualisieren"]
    C --> D["Zum nächsten Kandidaten"]
    D --> B
    B -->|"Nein"| E{"Besser als alle bisherigen?"}
    E -->|"Ja"| F["Eingestellt! (Ende)"]
    E -->|"Nein"| G{"n == N?"}
    G -->|"Nein"| H["Ablehnen und zum nächsten Kandidaten"]
    H --> E
    G -->|"Ja"| I["Den letzten Kandidaten notgedrungen einstellen (Hohe Wahrscheinlichkeit für Misserfolg)"]
```

---

## Mathematischer Beweis: Warum 1/e?

Hier erklären wir den wahrscheinlichkeitstheoretischen Hintergrund, warum sich das Ergebnis $1/e$ ergibt.

Nehmen wir eine Maßstabsgröße von $r-1$ Personen an. Das heißt, die Einstellungsaktivität beginnt ab dem $r$-ten Kandidaten.
Wir nehmen an, dass sich unter $N$ Kandidaten der wahrlich beste Kandidat an $i$-ter Stelle befindet ($i \ge r$).

Die Bedingungen für eine erfolgreiche Einstellung dieses $i$-ten Kandidaten sind wie folgt:
- Der wahre beste Kandidat befindet sich an $i$-ter Stelle. Die Wahrscheinlichkeit dafür ist $1/N$.
- Der beste Kandidat unter den Kandidaten von $1$ bis $i-1$ befindet sich unter den ersten $r-1$ Personen. Dadurch können die Kandidaten von $r$ bis $i-1$ den Maßstab nicht übertreffen und werden abgelehnt. Diese Wahrscheinlichkeit ist $\frac{r-1}{i-1}$.

Daher wird die Wahrscheinlichkeit $P(r)$ für einen Erfolg bei der Festlegung des Maßstabs $r$ wie folgt ausgedrückt:

$$ P(r) = \sum_{i=r}^{N} \frac{1}{N} \times \frac{r-1}{i-1} = \frac{r-1}{N} \sum_{i=r}^{N} \frac{1}{i-1} $$

Wenn $N$ sehr groß ist, kann diese Summe mit einem Integral angenähert werden.
Wenn wir $x = \lim_{N \to \infty} \frac{r}{N}$ (welcher Anteil der Gesamtheit als Beobachtungszeitraum dienen soll) setzen, ergibt sich:

$$ P(x) \approx x \int_{x}^{1} \frac{1}{t} dt = -x \ln(x) $$

Um die Erfolgswahrscheinlichkeit $P(x)$ zu maximieren, differenzieren wir nach $x$ und suchen den Punkt, an dem sie $0$ wird.

$$ \frac{d P(x)}{dx} = - \ln(x) - x \cdot \frac{1}{x} = - \ln(x) - 1 = 0 $$

Wenn wir dies auflösen, erhalten wir:
$$ \ln(x) = -1 \implies x = e^{-1} = \frac{1}{e} $$

Und die Wahrscheinlichkeit bei diesem Maximalwert ist:
$$ P(1/e) = -\left(\frac{1}{e}\right) \ln\left(\frac{1}{e}\right) = \frac{1}{e} $$

Auf diese Weise lässt sich wunderbar ableiten, dass sowohl der zu beobachtende Anteil als auch die Erfolgswahrscheinlichkeit **$1/e \approx 0.37$** betragen.

---

## Anwendungen außerhalb der Personalbeschaffung

Diese **1/e-Regel** ist über die Einstellung von Sekretärinnen hinaus weit anwendbar.

1. **Haus- oder Wohnungssuche**
   Wenn man innerhalb eines bestimmten Zeitraums (z. B. 1 Monat) ein neues Zuhause finden muss. Man widmet die ersten ca. 11 Tage (37%) ausschließlich der Besichtigung, ohne einen Vertrag zu unterschreiben, und nutzt das Niveau der besten Immobilie, die man in dieser Zeit gesehen hat, als Maßstab. Danach unterschreibt man sofort einen Vertrag, wenn eine Immobilie auftaucht, die diesen Maßstab übertrifft.

2. **Parkplatzsuche**
   Wenn man sich einem Ziel nähert und nach einem Parkplatz sucht. Man fährt die ersten 37% der Gesamtstrecke einfach vorbei, um ein Gefühl für die Verfügbarkeit zu bekommen, und parkt dann auf dem ersten freien Platz, der näher am Ziel liegt als jeder andere Platz, den man in den ersten 37% gesehen hat.

3. **Partnersuche**
   Ein oft im Scherz genanntes Beispiel: Angenommen, man sucht in den 22 Jahren zwischen dem 18. und 40. Lebensjahr nach einem Ehepartner. 37% von 22 Jahren sind etwa 8 Jahre. Das heißt, von 18 bis 26 Jahren (18+8) trifft man verschiedene Personen, um einen Maßstab zu bilden, und heiratet dann die erste Person, die man ab 26 Jahren trifft und die man für besser hält als jeden anderen in der Vergangenheit. Das ist die mathematisch optimale Lösung.

---

## Zusammenfassung

Das **Sekretärinnenproblem** ist ein leistungsstarkes Werkzeug zur mathematischen Lösung des Dilemmas, die beste Wahl treffen zu müssen, ohne alle Informationen zu haben, was in der realen Welt häufig vorkommt.

Dem intuitiven Unbehagen "Der entkommene Fisch ist vielleicht groß, aber wenn man zu lange wartet, gibt es keine Fische mehr" begegnet die Mathematik mit der klaren Antwort: **"Schau dir 37% an, bevor du entscheidest."**

Natürlich gibt es bei realen Entscheidungen verschiedene Variablen wie "Neben einer relativen Bewertung ist auch eine absolute Bewertung möglich", "Frühere Kandidaten können später kontaktiert werden" oder "Selbst wenn es nicht das Beste ist, kann das Zweitbeste ein Kompromiss sein". Aber die Kenntnis der **1/e-Regel** als Maßstab wird ein starker Kompass sein, um in einer unsicheren Welt zu navigieren.
