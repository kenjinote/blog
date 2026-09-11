---
title: 'Was ist die Collatz-Vermutung? Wir untersuchen ein ungelöstes mathematisches Problem in Python, bei dem jede Zahl am Ende bei 1 landet'
slug: "コラッツ予想"
date: 2025-07-15T18:03:03+09:00
tags: ["Collatz-Problem", "Mathematik", "Programmieren", "Algorithmus"]
draft: false
image: "img.webp"
categories: ["Mathematik, Kryptographie & Quanten"]
description: 'Ergibt „Gerade Zahlen halbieren, ungerade Zahlen verdreifachen und 1 addieren“ immer 1? Wir erklären leicht verständlich die mysteriösen Regeln der „Collatz-Vermutung“, einem berühmten ungelösten mathematischen Problem. Zusätzlich schreiben wir ein Python-Programm, um zu simulieren, ob die Folge wirklich gegen 1 konvergiert.'
---

# Stimmt es, dass „jede Zahl am Ende zu 1 wird“? ── Mit dem Collatz-Problem gespielt

Hallo! Ich bin kenji.

Ganz unvermittelt: Wenn man von einer „Regel hört, nach der jede Zahl am Ende zu 1 wird“,
klingt das nicht ein bisschen wundersam?

> Zum Beispiel bei 19, oder 87, oder sogar bei 1000000.
> Wenn man die Zahl nach einer bestimmten Regel verändert, konvergiert sie am Ende aus irgendeinem Grund auf „1“.

So eine traumhafte Geschichte ist das **Collatz-Problem (Collatz Conjecture)**.

---

## Was genau ist das Collatz-Problem?

Zuerst stelle ich die Regel vor.

* Start: Wähle eine beliebige **positive ganze Zahl**.
* Operation:

    * Wenn gerade → halbieren (n → n / 2)
    * Wenn ungerade → verdreifachen und 1 addieren (n → 3n + 1)

Wenn man dies immer weiter wiederholt, lautet die Vermutung, dass **jede Zahl letztendlich die 1 erreicht**.

Wenn wir zum Beispiel mit `6` beginnen:

```
6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
```

Sie ist brav zur „1“ geworden. Willkommen zurück!

---

## Lass es uns im Code ausprobieren: Collatz in Python

Nun, in solchen Fällen ist es am schnellsten, es im Code auszuprobieren!
Lass uns die „Collatz-Folge“ in Python ausgeben.

```python
def collatz(n):
    steps = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps.append(n)
    return steps

# Beispiel: Wir beginnen mit 19
print(collatz(19))
```

Wenn man es ausführt:

```
[19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
```

Es erreicht wunderbar die 1.
Obwohl es ziemlich viele Umwege gemacht hat, ist es am Ende sicher im Ziel gelandet!


Übrigens, selbst wenn wir mit **27** beginnen, erreicht es auf die gleiche Weise die 1.

```
print(collatz(27))
```

Wenn man es ausführt:

```
[27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242,
121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350,
175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167,
502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479,
1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911,
2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732,
866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35,
106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
```

Unglaublich, es dauert 111 Schritte!

Und zwischendurch gibt es sogar Phasen, in denen die Zahl auf über 9000 anwächst.
Ein Muster, bei dem es extrem viele Umwege macht, bevor es ins Ziel kommt.

---

## Und was ist nun das Besondere daran?

Das Besondere an dieser Vermutung ist Folgendes:

> **Obwohl sie nicht bewiesen ist, scheint sie bei jeder Zahl zur 1 zu führen.**

Das ist der Punkt.

Häh? Was ist dann mit 1 Billion oder 1 Billiarde...?

Wer so denkt, ist scharfsinnig.
Tatsächlich wurde dies mithilfe von Computern bis etwa „2 hoch 68“ überprüft,
und **alle haben die 1 erreicht**. Unglaublich...

Aber **es wurde theoretisch nicht bewiesen, dass „alle das tun“**.
Das ist das, was man in der Mathematikwelt ein „ungelöstes Problem“ nennt.

---

## Warum wird es „1“? Ein Ansatz aus der Wahrscheinlichkeitstheorie (Mathematischer Hintergrund)

Dass jede Zahl letztendlich 1 wird, scheint wie Magie zu sein, aber aus einer **wahrscheinlichkeitstheoretischen Perspektive** gibt es einen rationalen Grund, zu sagen: „Nun, es sieht so aus, als würde es passieren.“

Wenn wir `3n + 1` auf eine ungerade Zahl $n$ anwenden, ist die Antwort immer eine **gerade Zahl**.
Daher wird sie im nächsten Schritt immer durch 2 geteilt, was praktisch $\frac{3n + 1}{2} \approx 1.5n$ ergibt.

Und die Wahrscheinlichkeit, dass diese Zahl wieder gerade ist, beträgt $\frac{1}{2}$.
Wenn sie gerade ist, wird sie weiter durch 2 geteilt und wird zu $0.75n$, was kleiner als die ursprüngliche Zahl ist.

Auch wenn es mathematisch nicht streng ist, ist bekannt, dass das geometrische Mittel des „Multiplikators“ beim Sprung von einer ungeraden zur nächsten ungeraden Zahl **ungefähr das $\frac{3}{4}$-Fache** beträgt (heuristisches Wahrscheinlichkeitsmodell).
Das heißt, **im Durchschnitt tendiert der Wert dazu, zu schrumpfen**, sodass er letztendlich quasi in die 1 hineingezogen wird.

## Was passiert, wenn man die Regeln ein wenig ändert? (Vergleich mit anderen Vermutungen)

Man möchte vielleicht denken: „Nun, was ist, wenn man es mit 5 statt mit 3 multipliziert?“
Tatsächlich ist dies als das **$5n + 1$-Problem** bekannt, und in diesem Fall konvergieren nicht alle Zahlen gegen 1.

Beim $5n + 1$-Problem wurde bestätigt, dass mehrere verschiedene Schleifen (Zyklen) existieren, und es wurde auch auf die Möglichkeit hingewiesen, dass Zahlen existieren, die unendlich weiter wachsen (Divergenz).
Auch beim **$3n - 1$-Problem** gibt es neben der Schleife „$1 \to 2 \to 1$“ eine weitere Schleife wie „$5 \to 14 \to 7 \to 20 \to 10 \to 5$“.

Wir können sehen, welch feine Balance der Eigenschaft des Collatz-Problems zugrunde liegt, dass „alles gegen 1 (die $4 \to 2 \to 1$-Schleife) konvergiert“.

---

## Der Stand der Menschheit ①: Die Grenzen der Brute-Force durch Computer

Gegenwärtig berechnen Mathematiker und Informatik-Enthusiasten auf der ganzen Welt unermüdlich das Collatz-Problem und nutzen dabei verteiltes Rechnen (Projekte, die die Rechenleistung von PCs weltweit bündeln) und GPUs.

Stand 2020 haben Computer bestätigt, dass das Collatz-Problem für alle Startwerte bis unglaublichen **$2^{68}$ (etwa 295 Trilliarden)** richtig ist (also letztendlich 1 erreicht).

In der Mathematikwelt kann man jedoch nicht sagen: „Wir haben es bis 295 Trilliarden überprüft, also wird es für alle richtig sein.“ Denn angesichts des endlosen Ozeans an Zahlen ist selbst $2^{68}$ nur „der erste Tropfen“.

---

## Der Stand der Menschheit ②: Unentscheidbarkeit und der Durchbruch von Terence Tao

Auf die Frage „Warum kann es niemand beweisen?“ bewies der geniale britische Mathematiker John Conway 1972, dass ein leicht erweitertes Problem des Collatz-Problems **„unentscheidbar“ (Turing-vollständig)** ist.
Dies ist eine erschreckende Tatsache, die das Fundament der Informatik betrifft: Je nach Regel „existiert im Prinzip kein Algorithmus, um zu entscheiden, ob es 1 erreicht oder nicht“. Es ist sogar möglich, dass das Collatz-Problem selbst eine im Rahmen der modernen Mathematik unbeweisbare Aussage ist.

Doch 2019 gab es endlich einen großen Durchbruch.
**Terence Tao**, einer der größten Mathematikgenies der modernen Zeit, bewies mit Methoden der partiellen Differentialgleichungen und der Wahrscheinlichkeitstheorie, dass „(obwohl man nicht streng sagen kann, dass es für alle gilt) **die Collatz-Folge bei fast allen Startwerten letztendlich einen viel kleineren Wert als die ursprüngliche Zahl erreicht**“.

Dies ist zwar kein vollständiger Beweis dafür, dass „alles zu 1 wird“, aber es sorgte in der mathematischen Welt für Aufsehen als der **historische Meilenstein, an dem die Menschheit der Wahrheit des Collatz-Problems am nächsten kam**.

---

## Wer ist Herr Collatz?

Wer bis hierhin gelesen hat, denkt sich bestimmt: „Wer ist eigentlich dieser Collatz?“
Ich werde ihn kurz vorstellen!

* Name: **Lothar Collatz**
* Nationalität: Deutschland
* Geburts-/Todesjahr: 1910–1990
* Titel: Mathematiker (aktiv in den Bereichen Funktionalanalysis und Zahlentheorie)

Er schlug diese Vermutung 1937 vor,
und seitdem, über mehr als 80 Jahre hinweg, **konnte niemand sie beweisen oder widerlegen**.

Übrigens ist dieses Problem so simpel und doch so tiefgründig, dass sogar Paul Erdős (ein superberühmter Mathematiker) einmal sagte:

> „Die Mathematik ist noch nicht reif genug, um mit solchen Problemen umzugehen.“

Das heißt, es gibt die Theorie, dass die menschliche Mathematik dieses Rätsel noch nicht eingeholt hat...

---

## „Komplizierte Formeln“ sind nicht nötig

Das Schöne am Collatz-Problem ist, dass **jeder damit spielen kann**.

Man kann es mit Papier und Stift machen.
Wenn man Code in Python schreibt, kann man es automatisch ausprobieren.
Und trotzdem **stellen sich die führenden Mathematiker diesem Problem ernsthaft**.

Ist das nicht irgendwie aufregend?

---

## Bonus: Code, um alles auf einmal zu testen

Ich füge auch einen Code bei, um viele Zahlen auf einmal auszuprobieren.

```python
for n in range(1, 21):
    steps = collatz(n)
    print(f"{n}: {steps} (Anzahl der Schritte: {len(steps)-1})")
```

Dies gibt uns die Collatz-Folgen für „1 bis 20“ auf einen Schlag aus.

---

## Fazit: Diese Welt ist wirklich wundersam

Das war also das Collatz-Problem.

* Obwohl es extrem simpel ist
* Kann es niemand beweisen
* Und es ist ein riesiges Problem in der Mathematikwelt

Es ist wie ein massives Bündel an Wundersamkeit.

Auch Programmier-Anfänger können es ausprobieren, also spielt auf jeden Fall mal damit herum!

---

## Empfohlene Links (für Interessierte)

* [Wikipedia: Collatz-Problem](https://de.wikipedia.org/wiki/Collatz-Problem)
* [Paper von Terence Tao (Englisch)](https://arxiv.org/abs/1909.03562)
* Es macht auch Spaß, eine visualisierte Version in Python zu erstellen! (Wenn es Nachfrage gibt, werde ich eine machen)

---

Wer mehr über solche „wundersame Mathematik × Programmierung“-Themen wissen möchte,
kann gerne ungeniert „Erzähl mir mehr“ anfragen.
Irgendwann werde ich auch über die Riemannsche Vermutung, Primzahlen und vieles mehr berichten!

---

📮 Ende!

---
