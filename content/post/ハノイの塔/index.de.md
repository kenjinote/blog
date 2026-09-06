---
title: "Türme von Hanoi"
slug: "tuerme-von-hanoi"
date: 2025-04-17T22:23:14+09:00
tags: ["Türme von Hanoi", "Algorithmus", "Python"]
draft: false
image: "img.png"
categories: ["Programmierung"]
---

# Türme von Hanoi

Hallo!

Heute möchte ich Ihnen die "Türme von Hanoi" anhand eines Python-Beispielprogramms erklären.

---

## Was sind die Türme von Hanoi?

Die Türme von Hanoi sind ein Puzzle, das 3 Stäbe und mehrere Scheiben verwendet. Die Scheiben sind unterschiedlich groß und liegen zu Beginn der Größe nach absteigend auf einem Stab. Die Regeln lauten wie folgt:

1. Es kann immer nur eine Scheibe bewegt werden.
2. Eine größere Scheibe darf nicht auf eine kleinere Scheibe gelegt werden.

Dieses Puzzle gilt als hervorragendes Lehrmaterial, um rekursives Denken zu erlernen. Rekursion ist eine Methode zur Lösung eines Problems, indem man es in kleinere Probleme derselben Art zerlegt. Bei den Türmen von Hanoi wiederholen wir die Operation, n-1 Scheiben zu bewegen, um n Scheiben zu bewegen.

---

## Lösen wir die Türme von Hanoi mit Python

Unten sehen Sie einen Beispielcode zur Lösung der Türme von Hanoi in Python.

```python
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)

# Beispiel: 3 Scheiben von A nach C bewegen
hanoi(3, 'A', 'C', 'B')
```

In diesem Code wird die Funktion `hanoi` rekursiv aufgerufen, und die Schritte zum Bewegen der Scheiben werden angezeigt. Bei 3 Scheiben erhält man beispielsweise die folgende Ausgabe:

```
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
```

Auf diese Weise lassen sich komplexe Probleme durch einen rekursiven Ansatz einfach lösen.

---

## Wie lange dauert es, 64 Scheiben zu bewegen?

Die Anzahl der Züge bei den Türmen von Hanoi erfordert mindestens 2^n - 1 mal. Um 64 Scheiben zu bewegen, sind also 2^64 - 1 Züge, etwa 1,84×10^19 Züge erforderlich. Selbst wenn Sie einen Zug pro Sekunde machen könnten, würde es etwa 584,9 Milliarden Jahre dauern. Das ist etwa das 42-fache des Alters des Universums (etwa 13,7 Milliarden Jahre).

Mit zunehmender Anzahl von Scheiben steigt also die Anzahl der erforderlichen Züge exponentiell an. Daher ist es unrealistisch, in der Praxis 64 Scheiben zu bewegen.

---

## Zusammenfassung

Die Türme von Hanoi sind ein perfektes Puzzle, um rekursives Denken zu lernen. Mit Python können Sie die Lösung leicht implementieren. Seien Sie jedoch vorsichtig, da die Anzahl der erforderlichen Züge drastisch ansteigt, wenn die Anzahl der Scheiben zunimmt.

Indem Sie den rekursiven Ansatz verstehen und versuchen, tatsächlich Code zu schreiben, können Sie Ihre Programmierfähigkeiten verbessern. Bitte versuchen Sie sich an der Herausforderung der Türme von Hanoi.

--- 
