---
title: 'Newcombs Paradoxon: Kannst du ein superintelligentes Wesen besiegen, das die Zukunft vorhersieht?'
slug: 'newcombs-paradox'
description: '"Eine durchsichtige Box mit 100.000 Yen" und "eine undurchsichtige Box mit 100 Millionen Yen oder leer". Welches würdest du in einem Spiel wählen, das von einem Wesen vorbereitet wurde, das die Zukunft perfekt vorhersagt? Wir erklären das größte Rätsel der modernen Philosophie, bei dem der freie Wille und der Determinismus aufeinanderprallen.'
date: '2026-09-10T08:00:00+09:00'
image: 'img/newcombs_paradox.jpg'
math: true
mermaid: true
categories:
  - 'Mathematische Paradoxien'
  - 'Spieltheorie'
tags:
  - 'Paradoxon'
  - 'Determinismus'
  - 'Freier Wille'
  - 'Philosophie'
---

## 1. Das ultimative Entscheidungsspiel

Vor dir erscheint ein außerirdisches Wesen mit Superintelligenz, das sich selbst "Omega" nennt.
Omega ist ein Meister darin, menschliches Verhalten zu analysieren, und besitzt die erschreckende Fähigkeit, **"mit fast 100%iger Genauigkeit vorherzusagen, welche Entscheidung die Zielperson als nächstes treffen wird"**. Auch in vergangenen Experimenten haben sich Omegas Vorhersagen nie als falsch erwiesen.

Omega stellt zwei Boxen vor dich hin.
- **Box A**: Eine transparente Box. Darin befinden sich mit Sicherheit **"100.000 Yen"**.
- **Box B**: Eine undurchsichtige Box. Darin befinden sich entweder **"100 Millionen Yen"** oder sie ist **"leer (0 Yen)"**.

Omega fordert dich auf, eine der folgenden zwei Handlungen zu wählen.

- **Wahl 1 "Beide Boxen nehmen"**: Du erhältst sowohl die 100.000 Yen aus Box A als auch den Inhalt von Box B.
- **Wahl 2 "Nur Box B nehmen"**: Du erhältst nur den Inhalt von Box B. Auf die 100.000 Yen aus Box A musst du verzichten.

Wenn man nur das hört, würde sich natürlich jeder für "Beide Boxen nehmen" entscheiden.
Aber Omega hat eine schreckliche "Regel" hinzugefügt.

**【Omegas Regel】**
> "Ich habe bereits gestern vorhergesagt, 'welche Wahl' du heute treffen wirst, und den Inhalt von Box B entsprechend vorbereitet.
> Wenn ich vorhergesagt habe, dass du gierig bist und 'beide Boxen nehmen' wirst, habe ich Box B **leer** gelassen.
> Wenn ich vorhergesagt habe, dass du nicht gierig bist und 'nur Box B nehmen' wirst, habe ich **100 Millionen Yen** in Box B gelegt."

Nun musst du von jetzt an deine Wahl treffen.
**Solltest du "beide Boxen nehmen"? Oder solltest du "nur Box B nehmen"?**

```mermaid
graph TD
    Omega["Omegas Vorhersage<br>(Gestern bereits abgeschlossen)"]
    
    Omega -->|Sagt voraus: "Nimmt beide"| BoxB_Empty["Box B ist leer (0 Yen)"]
    Omega -->|Sagt voraus: "Nimmt nur Box B"| BoxB_100M["Box B enthält 100 Millionen Yen"]
    
    You["Deine Wahl<br>(Heute)"]
    
    You -->|Wahl 1: Beide nehmen| Result1["Box A (100.000) + Inhalt von Box B"]
    You -->|Wahl 2: Nur Box B nehmen| Result2["Box A (0) + Inhalt von Box B"]
    
    BoxB_Empty -.-> Result1
    BoxB_100M -.-> Result2
```

---

## 2. Zwei "perfekte Logiken" prallen aufeinander

Dieses Problem wurde 1969 vom Physiker William Newcomb erdacht und vom Philosophen Robert Nozick veröffentlicht.
Sobald es veröffentlicht wurde, spaltete es die Meinungen brillanter Mathematiker und Philosophen weltweit in "zwei Hälften" und löste eine große Debatte aus.

Der Grund dafür ist, dass **für beide Wahlmöglichkeiten eine "absolut unwiderlegbare, perfekte Logik" existiert**.

### Logik 1: Das Argument der "Nur Box B nehmen"-Fraktion (Erwartungswertmaximierung)

> "Omegas Vorhersagegenauigkeit liegt doch bei fast 100%, oder? Dann sollte man gemäß den vergangenen Daten an Omega glauben.
> Wenn ich mich für 'beide nehmen' entscheide, hat Omega das durchschaut und das Ergebnis sind läppische 100.000 Yen.
> Wenn ich mich für 'nur Box B nehmen' entscheide, hat Omega das durchschaut und das Ergebnis sind 100 Millionen Yen.
> Selbst ein Narr weiß, ob er 100.000 Yen oder 100 Millionen Yen haben möchte. Deshalb sollte man **unbedingt 'nur Box B nehmen'**!"

Diese Denkweise basiert auf der "Erwartungsnutzentheorie", die vergangenen statistischen Daten und Erwartungswerten blind vertraut.

### Logik 2: Das Argument der "Beide Boxen nehmen"-Fraktion (Dominante Strategie)

> "Moment mal. Dass Omega die Vorhersage getroffen und den Inhalt in Box B gelegt hat, war doch **'gestern'**, richtig?
> Das bedeutet, dass zum jetzigen Zeitpunkt der Inhalt von Box B auf entweder '100 Millionen Yen sind drin' oder 'leer' festgelegt ist und sich **absolut nicht mehr ändern** kann.
> 
> Szenario 1: Wenn Box B bereits 100 Millionen Yen enthält, bekommt man mit 'beide nehmen' 100,1 Millionen Yen, und mit 'nur B' 100 Millionen Yen.
> Szenario 2: Wenn Box B bereits leer ist, bekommt man mit 'beide nehmen' 100.000 Yen, und mit 'nur B' 0 Yen.
> 
> In beiden Szenarien **erhält man doch definitiv 100.000 Yen mehr, wenn man 'beide nehmen' wählt**!
> Egal, wofür ich mich jetzt entscheide, Omegas gestrige Handlung kann nicht durch eine Zeitmaschine umgeschrieben werden. Deshalb sollte man **unbedingt 'beide Boxen nehmen'**!"

Diese Denkweise basiert auf der "Dominanten Strategie" (Dominant Strategy) in der Spieltheorie, die besagt, dass man "die für sich selbst vorteilhafte Wahl trifft, unabhängig davon, welche Aktion der Gegner ausführt".

---

## 3. Glaubst du an den "freien Willen"?

Die "Nur Box B nehmen"-Fraktion und die "Beide nehmen"-Fraktion.
Nachdem du beide Argumente gehört hast, welche hältst du für richtig?

Tatsächlich gibt es bis heute keine "mathematisch perfekte, einzige richtige Antwort" für dieses Paradoxon.
Der Grund dafür ist, dass sich an der Wurzel dieses Problems die größte philosophische Frage der Menschheit verbirgt: **"Determinismus vs. Freier Wille"**.

### Jene, die "Nur Box B nehmen" geantwortet haben (Deterministen)
Diejenigen, die diese Wahl getroffen haben, akzeptieren unbewusst den **"Determinismus (die Zukunft dieser Welt ist von Anfang an vorherbestimmt)"**.
Dass Omega die Zukunft zu 100% vorhersagen kann, bedeutet, dass deine jetzige Entscheidung nicht durch "deinen freien Willen" getroffen wurde, sondern dass du "durch die physikalischen Gesetze des Universums und die Bewegung der Neuronen im Gehirn bereits seit gestern dazu bestimmt warst, diese Wahl zu treffen".
Da die Zukunft nicht geändert werden kann, ist es am rationalsten, sich dem von Omega vorhergesagten "Schicksal, nur Box B zu nehmen" zu fügen, so diese Denkweise.

### Jene, die "Beide Boxen nehmen" geantwortet haben (Anhänger des freien Willens)
Diejenigen, die diese Wahl getroffen haben, glauben unbewusst an den **"freien Willen (die Zukunft kann durch eigene Entscheidungen gestaltet werden)"**.
Gerade weil sie glauben, dass sie "ihre Wahl durch ihren jetzigen Willen ändern können, unabhängig von Omegas gestriger Vorhersage", "unternehmen sie in diesem Moment die Aktion, 100.000 Yen hinzuzufügen, unabhängig vom bereits festgelegten Inhalt der Box".
Selbst wenn Omega dies im Endeffekt vorhergesagt hat und die Box leer war, besitzen sie die Logik, es als "unvermeidliches Ergebnis einer logisch richtigen Handlung" zu akzeptieren.

---

## 4. Zeitreisen und der Zusammenbruch der Kausalität

Was Newcombs Paradoxon noch komplizierter macht, ist die Umkehrung der "Kausalität (es gibt eine Ursache und eine Wirkung)".

In der uns vertrauten Welt des gesunden Menschenverstands,
schafft "meine heutige Wahl (Ursache)" "das morgige Ergebnis".

Aber in Omegas Spiel,
scheint "meine heutige Wahl (Ursache)" "**Omegas gestrige** Handlung (Wirkung)" zu bestimmen.
Es entsteht eine "Rückwärtskausalität" (Backward Causality), bei der zukünftige Handlungen vergangene Tatsachen bestimmen.

Wenn ein "perfekter Vorhersager" wie Omega im Universum existieren würde, würde sogar unser gesunder Menschenverstand, dass "die Zeit von der Vergangenheit in die Zukunft fließt", zusammenbrechen.

---

## 5. Fazit: Ein Gedankenexperiment enthüllt die menschliche "Rationalität"

Welche Box öffnest du?

Obwohl seit der Präsentation dieses Paradoxons mehr als ein halbes Jahrhundert vergangen ist, spalten sich in Umfragen aus Philosophie und Wirtschaftswissenschaften die Befragten interessanterweise etwa zur Hälfte in die "Beide nehmen"-Fraktion und die "Nur B nehmen"-Fraktion.
Und das Interessante daran ist, dass beide Lager ernsthaft glauben: "Die Logik der anderen Seite ist völlig fehlerhaft und dumm."

"Was ist eine rationale Entscheidung?"
Egal wie weit sich Wirtschaftswissenschaften und Mathematik entwickeln, am Ende landet man immer bei der Philosophie: "Wie der Mensch diese Welt wahrnimmt". Newcombs Paradoxon ist ein höchst bösartiges und wunderschönes Gedankenexperiment, das uns die Grenzen der Logik aufzeigt.
