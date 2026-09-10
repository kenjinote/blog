---
title: 'Das Dornröschen-Problem: Ist die Wahrscheinlichkeit der Münze 1/2 oder 1/3? Ein Paradoxon, das die Wahrscheinlichkeitstheorie spaltet'
slug: 'sleeping-beauty-paradox'
description: '"Wie hoch ist die Wahrscheinlichkeit, dass das Ergebnis des Münzwurfs Kopf war, jetzt, wo Sie aufgewacht sind?" Wir erklären das neueste Paradoxon, bei dem trotz eines sehr einfachen Aufbaus Mathematiker und Philosophen weltweit in "1/2-Anhänger" und "1/3-Anhänger" gespalten sind und weiterhin debattieren.'
date: '2026-09-10T09:00:00+09:00'
image: 'img/sleeping_beauty.jpg'
math: true
mermaid: true
categories:
  - 'Mathematische Paradoxa'
  - 'Wahrscheinlichkeitstheorie'
tags:
  - 'Paradoxon'
  - 'Bedingte Wahrscheinlichkeit'
  - 'Satz von Bayes'
  - 'Philosophie'
---

## 1. Die Regeln des seltsamen Experiments

Sie (Dornröschen) wurden als Versuchsperson für ein wissenschaftliches Experiment ausgewählt.
Das Experiment findet von Sonntag bis Mittwoch statt. Am Sonntagabend bekommen Sie ein Schlafmittel und schlafen ein.

Nachdem Sie eingeschlafen sind, wirft der Versuchsleiter **eine faire Münze** (eine Münze, bei der die Wahrscheinlichkeit für Kopf und Zahl genau 1/2 beträgt). Abhängig vom Ergebnis werden Sie nach folgendem Zeitplan geweckt:

**[Wenn das Ergebnis des Münzwurfs "Kopf" ist]**
- Sie werden am Montag genau einmal geweckt und es wird Ihnen eine Frage gestellt. Danach werden Sie wieder in den Schlaf versetzt und wachen bis zum Ende des Experiments (Mittwoch) nicht mehr auf.

**[Wenn das Ergebnis des Münzwurfs "Zahl" ist]**
- Sie werden am Montag geweckt und es wird Ihnen eine Frage gestellt. Danach wird Ihnen ein spezielles Medikament (ein Medikament, das Erinnerungen löscht) verabreicht und Sie schlafen wieder ein.
- Am Dienstag werden Sie noch einmal geweckt und Ihnen wird dieselbe Frage gestellt. Danach werden Sie wieder in den Schlaf versetzt und das Experiment endet (Mittwoch).

* Aufgrund der Wirkung des Medikaments, das die Erinnerung löscht, können Sie sich beim Aufwachen absolut nicht daran erinnern, "welcher Wochentag heute ist" oder "ob Sie in der Vergangenheit schon einmal geweckt wurden".

```mermaid
graph TD
    Sunday["Sonntag: Dornröschen schläft"] --> Toss{"Münzwurf"}
    
    Toss -->|Kopf (1/2)| Mon_Heads["Montag: Aufwachen + Frage<br>(Danach Ende des Experiments)"]
    Toss -->|Zahl (1/2)| Mon_Tails["Montag: Aufwachen + Frage<br>(Danach Erinnerungslöschung)"]
    
    Mon_Tails --> Tue_Tails["Dienstag: Aufwachen + Frage<br>(Danach Ende des Experiments)"]
    
    style Toss fill:#ff9999,stroke:#333
    style Mon_Heads fill:#aaffaa,stroke:#333
    style Mon_Tails fill:#aaffaa,stroke:#333
    style Tue_Tails fill:#aaffaa,stroke:#333
```

Nun wachen Sie am Montag (oder Dienstag) auf.
In dem Raum gibt es weder eine Uhr noch einen Kalender, und Sie wissen nicht, welcher Wochentag heute ist.

Dann kommt der Versuchsleiter zu Ihnen und stellt Ihnen folgende Frage:
**"Was glauben Sie, wie hoch ist die Wahrscheinlichkeit, dass die geworfene Münze 'Kopf' zeigte, in dem Zustand, in dem Sie jetzt wach sind?"**

Sie sind ein Dornröschen, das sich gut mit Mathematik auskennt. Nun, was antworten Sie?

---

## 2. Zwei kollidierende Fraktionen: 1/2 oder 1/3

Dieses Problem wurde in den 1990er Jahren erdacht und im Jahr 2000 von dem Philosophen Adam Elga in einer Fachzeitschrift veröffentlicht.
Die Wahrscheinlichkeit der Münze erscheint trivial, aber in Wirklichkeit sind Mathematiker, Statistiker und Philosophen auf der ganzen Welt in Bezug auf dieses Problem genau in zwei Lager gespalten: die **"1/2-Fraktion (Halfer)"** und die **"1/3-Fraktion (Thirder)"**, und führen bis heute eine heftige Debatte.

Lassen Sie uns die "perfekte Logik" jedes Lagers anhören.

### Das Argument der "1/2-Fraktion (Halfer)"
> "Da die Münze eine faire Münze ohne Betrug ist, beträgt die Wahrscheinlichkeit, dass sie auf Kopf landet, natürlich 1/2.
> Egal wie oft der Versuchsleiter mich weckt, nachdem ich eingeschlafen bin, oder mein Gedächtnis löscht, das hat **absolut keinen Einfluss auf das physische Ergebnis der Münze**.
> Die Wahrscheinlichkeit zum Zeitpunkt des Münzwurfs beträgt 1/2, und durch mein Aufwachen habe ich keine neuen Informationen (Hinweise, um zu erraten, ob es Kopf oder Zahl ist) erhalten. Daher bleibt die Wahrscheinlichkeit 1/2."

Dies ist eine sehr vernünftige Meinung, die das objektive physikalische Phänomen und die Nicht-Aktualisierung von Informationen betont.

### Das Argument der "1/3-Fraktion (Thirder)"
> "Die Tatsache selbst, dass Sie 'wach sind', ist eine Information, die die Wahrscheinlichkeit verändert.
> Angenommen, wir wiederholen dieses Experiment 100 Mal (100 Wochen).
> Die Münze sollte 50 Mal 'Kopf' und 50 Mal 'Zahl' zeigen.
> 
> - In den 50 Wochen, in denen Kopf geworfen wird, wachen Sie am Montag nur einmal auf $\rightarrow$ **Die Anzahl der Male, die Sie bei 'Kopf' aufwachen, beträgt 50**
> - In den 50 Wochen, in denen Zahl geworfen wird, wachen Sie am Montag und Dienstag zweimal auf $\rightarrow$ **Die Anzahl der Male, die Sie bei 'Zahl' aufwachen, beträgt 100**
> 
> Das bedeutet, dass in den Momenten, in denen Sie aufwachen, aus insgesamt 150 Situationen das 'Muster, bei Kopf aufzuwachen' 50 Mal auftritt und das 'Muster, bei Zahl aufzuwachen' 100 Mal.
> Daher ist die Wahrscheinlichkeit, dass das Aufwachen, das Sie gerade erleben, 'Kopf' ist, 50 / 150 ＝ **1/3**!"

Dies ist eine starke Meinung, die auf dem "Frequentismus" oder dem "Anthropischen Prinzip" basiert und die Situation, dass "man selbst jetzt existiert (beobachtet)", als Element des Wahrscheinlichkeitsraums in die Berechnung einbezieht.

---

## 3. Berechnung mit dem Satz von Bayes

Es gibt auch Versuche, dieses Problem mit dem "Satz von Bayes", einem mathematischen Werkzeug zur Aktualisierung von Wahrscheinlichkeiten, zu lösen.
Lassen Sie uns die Logik der "1/3-Fraktion" unter dem Gesichtspunkt der bedingten Wahrscheinlichkeit ordnen.

Der Zustand beim Aufwachen ist einer der folgenden drei:
1. $E_1$: Die Münze ist "Kopf" und es ist "Montag"
2. $E_2$: Die Münze ist "Zahl" und es ist "Montag"
3. $E_3$: Die Münze ist "Zahl" und es ist "Dienstag"

Die Wahrscheinlichkeit, dass "Kopf" geworfen wird, ist $1/2$, und die Wahrscheinlichkeit, dass "Zahl" geworfen wird, ist $1/2$.
Da jedoch im Falle von Zahl "Montag" und "Dienstag" vollkommen symmetrisch sind (sie können nicht unterschieden werden, da keine Erinnerung vorhanden ist), kann man davon ausgehen, dass die Wahrscheinlichkeit für das Eintreten von $E_2$ und $E_3$ gleich ist.

Da die Summe aller Wahrscheinlichkeiten $1$ ergeben muss, ergibt sich, wenn man jedem Aufwachen als unabhängigem "Ereignis (Beobachtungspunkt)" die gleiche Wahrscheinlichkeit zuordnet:
$P(E_1) = 1/3$
$P(E_2) = 1/3$
$P(E_3) = 1/3$
Daher ist die Schlussfolgerung, dass die "Wahrscheinlichkeit, dass es Kopf war ($P(E_1)$)", $1/3$ wird.

Andererseits widerspricht die "1/2-Fraktion": "Montag und Dienstag, wenn die Münze Zahl zeigt ($E_2$ und $E_3$), sind von vornherein abhängige Ereignisse, die nur vom Ergebnis einer einzigen Münze abgeleitet sind, und es ist falsch, sie als unabhängige Wahrscheinlichkeiten zu zählen."

---

## 4. Warum wird dieses Problem nicht gelöst?

Der Grund, warum das "Dornröschen-Problem" Gelehrte so sehr plagt, liegt nicht an einfachen Berechnungsfehlern oder Illusionen.
Dieses Problem berührt die tiefste und grundlegendste Frage der Wahrscheinlichkeitstheorie, nämlich die philosophische Frage: **"Was genau ist Wahrscheinlichkeit?"**

- Für die **1/2-Fraktion** ist Wahrscheinlichkeit eine "physikalische Eigenschaft der Münze" oder eine "objektive Tatsache".
- Für die **1/3-Fraktion** ist Wahrscheinlichkeit der "Grad der Überzeugung des Beobachters (Dornröschens)" oder die "beobachtete Häufigkeit".

Tiefe Themen, die auch mit dem "Messproblem" in der Quantenmechanik oder dem "Anthropischen Prinzip" in der Kosmologie (der Idee, die Wahrscheinlichkeit des Universums aus der Tatsache, dass wir existieren, zurückzurechnen) verbunden sind, sind in diesem einfachen Münzwurfexperiment verdichtet.

## 5. Zusammenfassung

Wenn Sie eine Versuchsperson in diesem Experiment würden, würden Sie beim Aufwachen "1/2" antworten? Oder würden Sie "1/3" antworten?

Egal, was Sie antworten, Mathematiker von Weltrang werden hinter Ihnen stehen und Sie verteidigen.
Wie scheinbar einfache mathematische Definitionen zusammenbrechen, sobald sie mit so kniffligen Konzepten wie der menschlichen "Subjektivität" oder "Existenz" verknüpft werden. Das Paradoxon erschüttert auch heute noch unseren gesunden Menschenverstand.
