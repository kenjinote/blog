---
title: "Wann hört ein Sandhaufen auf, ein Sandhaufen zu sein, wenn man ein Sandkorn entfernt? Das Sorites-Paradoxon"
description: "Wo liegt die Grenze zwischen einem 'Sandhaufen' und 'keinem Sandhaufen'? Ein philosophisches Paradoxon seit dem antiken Griechenland, das sich dem Wesen der Vagheit stellt."
date: 2026-09-10T21:00:00+09:00
draft: false
slug: "sorites-paradox"
image: "img/sorites_paradox.jpg"
math: true
mermaid: true
categories: ["Mathematische Paradoxa", "Philosophie", "Logik"]
tags: ["Paradoxon", "Vagheit", "Sorites", "Fuzzy-Logik"]
---

Stellen Sie sich vor, vor Ihnen steht ein prächtiger Sandhaufen aus 10.000 Körnern. Jeder würde ihn als „Sandhaufen" bezeichnen.
Nun entfernen wir ein einziges Sandkorn. 9.999 Körner. Immer noch ein Sandhaufen, oder?
Wir entfernen ein weiteres Korn. 9.998 Körner. Auch das ist noch ein Sandhaufen.

Wiederholen wir diesen Vorgang.
Durch das Entfernen eines einzigen Korns sollte sich ein „Sandhaufen" nicht in „keinen Sandhaufen" verwandeln. Doch wenn man diese Logik immer weiter fortsetzt, bleibt am Ende nur noch ein einziges Sandkorn übrig.

**Ist ein einzelnes Sandkorn ein „Sandhaufen"?**

Natürlich würde niemand ein einzelnes Sandkorn als „Sandhaufen" bezeichnen. Aber wir haben die Prämisse „Auch nach dem Entfernen eines Korns bleibt ein Sandhaufen ein Sandhaufen" kein einziges Mal verneint. Irgendwo muss die Logik zusammenbrechen – doch **bei welchem Korn genau hörte der Sandhaufen auf, ein Sandhaufen zu sein?**

Dies ist das **„Sorites-Paradoxon" (Paradoxon des Haufens)**, das auf den altgriechischen Philosophen Eubulides aus dem 4. Jahrhundert v. Chr. zurückgeht.

## Logische Struktur

Dieses Paradoxon lässt sich in Form eines Syllogismus ausdrücken:

**Prämisse 1**: Eine Ansammlung von 10.000 Sandkörnern ist ein „Sandhaufen".
**Prämisse 2**: Wenn man von einem Sandhaufen ein Sandkorn entfernt, ist das Ergebnis immer noch ein „Sandhaufen".
**Schlussfolgerung**: Folglich ist auch ein einzelnes Sandkorn ein „Sandhaufen".

Prämisse 1 und Prämisse 2 klingen jeweils für sich genommen sehr plausibel. Doch wenn man Prämisse 2 wiederholt anwendet, führt dies zu einer offensichtlich falschen Schlussfolgerung.

```mermaid
graph LR
    A["10.000 Körner = Sandhaufen"] -->|1 Korn entfernt| B["9.999 Körner = Sandhaufen"]
    B -->|1 Korn entfernt| C["9.998 Körner = Sandhaufen"]
    C -->|...Wiederholung...| D["100 Körner = Sandhaufen?"]
    D -->|1 Korn entfernt| E["10 Körner = Sandhaufen?"]
    E -->|1 Korn entfernt| F["1 Korn = Sandhaufen?"]
    
    style A fill:#4CAF50,color:#fff
    style D fill:#FF9800,color:#fff
    style E fill:#FF5722,color:#fff
    style F fill:#F44336,color:#fff,stroke-width:3px
```

## Warum dieses Paradoxon unlösbar ist

Der Kern des Sorites-Paradoxons liegt darin, dass **das Wort „Sandhaufen" von Natur aus vage ist**.
Für „Sandhaufen" gibt es keine klare Definition (Schwellenwert) wie „ab so-und-so-vielen Körnern ist es ein Sandhaufen". Solche Begriffe werden als **„vage Prädikate" (vague predicates)** bezeichnet.

Unsere Alltagssprache ist voll von solchen vagen Ausdrücken.

- **„Groß"** – ab wie vielen Zentimetern? Eine Person mit 180 cm ist „groß". Was, wenn man 1 mm abzieht? Und noch 1 mm?
- **„Reich"** – ab welchem Vermögen? Bei 10 Milliarden Yen ist man „reich". Was, wenn 1 Yen weniger?
- **„Kahl"** – ab wie wenigen Haaren? Bei 0 Haaren ist man „kahl". Was, wenn ein einziges Haar nachwächst?

All diese Beispiele haben exakt die gleiche Struktur wie das Sorites-Paradoxon.

## Ansätze der Philosophen

### 1. Erkenntnistheoretischer Ansatz (Die Grenze existiert)

Dieser Ansatz behauptet: „Tatsächlich gibt es eine klare Grenze zwischen Sandhaufen und Nicht-Sandhaufen, aber der Mensch ist einfach nicht in der Lage, sie zu erkennen."
Zum Beispiel gäbe es eine exakte Grenze wie „5.837 Körner sind ein Sandhaufen, aber 5.836 Körner sind es nicht" – wir können sie nur nicht wissen.

Logisch betrachtet ist das schlüssig, doch intuitiv empfinden die meisten Menschen ein Unbehagen bei dieser Position.

### 2. Fuzzy-Logik (Graduelle Wahrheitswerte)

In der klassischen Logik gibt es nur „wahr oder falsch", doch in der Fuzzy-Logik kann ein Wert **irgendwo zwischen 0 und 1** liegen.

Zum Beispiel:
- 10.000 Körner Sand: „Sandhaufen-Grad = 1,0 (definitiv ein Sandhaufen)"
- 5.000 Körner: „Sandhaufen-Grad = 0,7"
- 100 Körner: „Sandhaufen-Grad = 0,1"
- 1 Korn: „Sandhaufen-Grad = 0,0 (definitiv kein Sandhaufen)"

Dieser Ansatz ist praktisch, löst das Paradoxon aber nicht vollständig. Denn es entsteht eine neue Vagheit: „Was ist der Unterschied zwischen einem Sandhaufen-Grad von 0,7 und 0,699?"

### 3. Supervaluationismus (Supervaluationism)

Bei diesem Ansatz werden für das Wort „Sandhaufen" alle denkbaren vernünftigen Grenzziehungen gleichzeitig berücksichtigt. Wird etwas bei allen Grenzziehungen als „Sandhaufen" eingestuft, ist es „definitiv ein Sandhaufen". Wird es bei allen als „Nicht-Sandhaufen" eingestuft, ist es „definitiv kein Sandhaufen". Der Bereich, in dem die Meinungen auseinandergehen, gilt als „unbestimmt".

## Auswirkungen auf die moderne Gesellschaft

Das Sorites-Paradoxon ist nicht nur ein Wortspiel, sondern verursacht auch in der realen Welt der Gesetze und Politik ernsthafte Probleme.

- **Volljährigkeitsalter**: Mit 17 Jahren und 364 Tagen ist man ein „Kind", mit 18 Jahren und 0 Tagen ein „Erwachsener". Was ändert sich grundlegend an einem einzigen Tag?
- **Armutsgrenze**: Liegt das Jahreseinkommen 1 Yen unter dem Grenzwert, gilt man als „arm"; liegt es 1 Yen darüber, gilt man als „nicht arm".
- **Umweltvorschriften**: Überschreitet der Schadstoffausstoß den Grenzwert um 0,001 mg, ist es illegal. Genau auf dem Grenzwert ist es legal.

Die menschliche Sprache und das Denken enthalten von Natur aus Vagheit, und der Versuch, die Welt in klare binäre Gegensätze zu unterteilen, stößt möglicherweise an seine Grenzen. Das Sorites-Paradoxon ist ein Paradoxon, das seit über 2.400 Jahren Philosophen beschäftigt und die grundlegenden Grenzen des menschlichen Intellekts aufzeigt.
