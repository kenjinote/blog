---
title: "Was ist das Geburtstagsparadoxon?"
slug: "バースデイパラドックスとは"
date: 2024-04-02T01:20:50+09:00
tags: ["Mathematik", "Paradoxon"]
draft: false
math: true
image: "img.png"
categories: ["Mathematik, Kryptographie, Quanten"]
---

## Kennen Sie das Geburtstagsparadoxon?

Ich werde Ihnen eine etwas seltsame Geschichte erzählen.
Wie viele Personen müssen Ihrer Meinung nach zusammenkommen, damit "die Wahrscheinlichkeit, dass Personen am selben Tag Geburtstag haben", hoch ist?

Ein Jahr hat zum Beispiel 365 Tage. Wenn man Ihnen also sagt: "Wenn 23 Personen zusammenkommen, liegt die Wahrscheinlichkeit, dass jemand denselben Geburtstag hat, bei über 50 %"... dann scheint das irgendwie gegen die Intuition zu verstoßen.

Aber es sind **tatsächlich über 50 %.** 

---

## Warum passiert das?

Dieses Phänomen wird als "Geburtstagsparadoxon" bezeichnet.
Der Name lautet "Paradoxon", aber es gibt einen fundierten mathematischen Grund.

Wenn die Anzahl der Personen "n" ist, wird **die Wahrscheinlichkeit, dass niemand denselben Geburtstag hat** , durch die folgende Formel berechnet:

```
P(niemand hat am selben Tag Geburtstag) = 365/365 × 364/365 × 363/365 × ... × (365 - n + 1)/365
```

Indem man dies von 1 abzieht, erhält man "die Wahrscheinlichkeit, denselben Geburtstag wie jemand anderes zu haben".

---

## Wenn wir uns die Ergebnisse ansehen...

| Anzahl der Personen | Wahrscheinlichkeit, denselben Geburtstag zu haben |
| ------------------- | ------------------------------------------------- |
| 10 Personen         | Etwa 11.7%                                        |
| 20 Personen         | Etwa 41.1%                                        |
| 23 Personen         | **Etwa 50.7% (Hierauf achten!)** |
| 30 Personen         | Etwa 70.6%                                        |
| 70 Personen         | **Erstaunliche 99.9%!** |

Das heißt, bei nur **23 Personen** besteht eine Wahrscheinlichkeit von mehr als der Hälfte, dass jemand denselben Geburtstag hat.
Dies lässt sich durchaus auch auf Schulklassen oder Besprechungen am Arbeitsplatz übertragen.

---

## Zusammenfassung: Die Diskrepanz zwischen Intuition und Mathematik ist faszinierend

Das "Geburtstagsparadoxon" ist ein interessantes Beispiel dafür, wie unsere Intuition und die tatsächliche mathematische Wahrscheinlichkeit voneinander abweichen.
Solche Dinge zu wissen, kann eine nette Unterhaltung oder ein Quiz auflockern!

---

## Referenz-Links

* [Geburtstagsparadoxon (Wikipedia)](https://ja.wikipedia.org/wiki/%E8%AA%95%E7%94%9F%E6%97%A5%E3%81%AE%E3%83%91%E3%83%A9%E3%83%89%E3%83%83%E3%82%AF%E3%82%B9)
