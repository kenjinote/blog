---
title: 'Was ist das "General Number Field Sieve (GNFS)", die stärkste Mathematik der Menschheit, die die Internetverschlüsselung knackt?'
slug: "インターネットの暗号を破る人類最強の数学「一般数体篩法（GNFS）」とは？"
date: 2026-09-05T02:09:08+09:00
tags: ["Mathematik", "Kryptographie", "RSA", "GNFS"]
draft: false
image: "gnfs_two_worlds_1788542142485.jpg"
categories: ["Mathematik・Kryptographie・Quanten"]
---

# Was ist das "General Number Field Sieve (GNFS)", die stärkste Mathematik der Menschheit, die die Internetverschlüsselung knackt?

Das Internet, das wir jeden Tag nutzen. LINE-Nachrichten, YouTube, Einkaufen auf Amazon – die gesamte Kommunikation wird durch "Verschlüsselung" geschützt.
Derzeit ist der weltweit am häufigsten verwendete Vertreter die "RSA-Verschlüsselung".

Der Schlüssel zur Verteidigung der RSA-Verschlüsselung ist sehr einfach. Er nutzt die mathematische Eigenschaft, dass ** "die Primfaktorzerlegung gigantischer Zahlen selbst von Computern nicht gelöst werden kann" ** .
Bei "15" wissen wir zum Beispiel sofort, dass es "3 × 5" ist, aber sobald es eine "270-stellige Zahl" wird, würde es Hunderte von Millionen Jahren dauern, selbst wenn man alle Supercomputer der Welt zusammennimmt, um sie zu lösen.

Doch die Mathematiker sind nicht stumm geblieben. Um diese undurchdringliche Verschlüsselung zu knacken, hat die Menschheit einen fast magischen Algorithmus (Berechnungsverfahren) namens ** "General Number Field Sieve (GNFS)" ** erschaffen.

In diesem Artikel werden wir ohne Fachjargon und nur mit dem Wissen der ** Mittelstufenmathematik (Primfaktorzerlegung, algebraische Ausdrücke, größter gemeinsamer Teiler) ** Schritt für Schritt erklären, wie dieser "stärkste Algorithmus der Menschheit" die Verschlüsselung knackt!

---

## Kapitel 1: Das Ziel der Entschlüsselung ist eine "Formel der 9. Klasse"

Der größte Spezialtrick, um der gigantischen Primfaktorzerlegung zu begegnen. Es ist diese Formel, die man in der 9. Klasse lernt:

> ** $X^2 - Y^2 = (X + Y)(X - Y)$ ** 

Sie denken vielleicht: "Ernsthaft, eine so grundlegende Formel kann Verschlüsselung knacken?". Dies ist jedoch der Hauptschlüssel, der alles offenbart.

Das größte Ziel beim Knacken der Verschlüsselung ist es, für eine riesige Zahl $N$, ** "Zahlen ($X$ und $Y$) zu finden, bei denen der Rest bei der Division von $X^2$ und $Y^2$ durch $N$ derselbe ist" ** .

### Warum knackt "derselbe Rest" die Verschlüsselung?
Angenommen, zwei Zahlen, $X^2$ und $Y^2$, haben "denselben Rest, wenn sie durch $N$ geteilt werden".
Denselben Rest zu haben bedeutet, dass es eine Regel nach der ** die Subtraktion "$X^2 - Y^2$" immer genau durch $N$ teilbar ist (ein Vielfaches von $N$ sein wird) ** .

Nehmen wir hier an, dass die gigantische Zahl $N$, die für die Verschlüsselung verwendet wird, aus der Multiplikation zweier geheimer Primzahlen ($p$ und $q$) besteht ($N = p \times q$).

Wenn wir $X^2 - Y^2$ faktorisieren, erhalten wir ** $(X - Y)(X + Y)$ ** .
Die Tatsache, dass dies ein Vielfaches von $N$ ist, bedeutet, dass irgendwo in dieser Multiplikation die geheimen Primzahlen $p$ und $q$ verborgen sind.

Hier geschieht ein Wunder.
Es besteht eine mathematische Wahrscheinlichkeit von ** 50% (der Hälfte) ** , dass die beiden Primzahlen $p$ und $q$ sich in verschiedene Räume trennen: ** "$p$ geht in den Raum von $(X - Y)$" und "$q$ geht in den Raum von $(X + Y)$" ** .

Wenn nur die Primzahl $p$ den Raum von $(X - Y)$ betreten hat, berechnen wir den ** "größten gemeinsamen Teiler (das größte gemeinsame Teil)" ** von $(X - Y)$ und $N$.
* Inhalt von $(X - Y)$ = $p \times$ irgendeine Zahl
* Inhalt von $N$ = $p \times q$
  Das einzige gemeinsame Teil ist ** "$p$" ** !

Mit anderen Worten, in dem Moment, in dem der größte gemeinsame Teiler berechnet wird, wird die verborgene Primzahl $p$ enthüllt und die Verschlüsselung ist vollständig entschlüsselt. (*Der größte gemeinsame Teiler kann sogar auf einem Smartphone sofort mit dem "Euklidischen Algorithmus" berechnet werden).

** 【Kleine Kolumne: Warum das Quadrat? Funktionieren Kubik oder das Doppelte nicht?】 ** 
> Bei "$2X - 2Y$" wird es zu $2(X - Y)$ und es gibt nur einen Raum, sodass Sie die Primzahlen nicht trennen können. Bei "$X^3 - Y^3$" wird die Größe der Räume unausgewogen und die Berechnung wird unnötig schwer. Um die Primzahlen in zwei zu trennen, ist das "Quadrat", das sich wunderbar in zwei Räume aufteilt, am kostengünstigsten.

---

## Kapitel 2: Wie findet man X und Y? "Das Primzahlkarten-Sammelpuzzle"

Das Ziel ist klar. Doch selbst wenn wir blind nach "$X^2$ und $Y^2$ mit demselben Rest" suchen würden, würde das Ende des Universums eintreten, bevor wir sie finden.
Also ließen sich Mathematiker eine geniale Methode namens ** "Primzahlkarten-Sammelpuzzle" ** einfallen.

### Schritt 1: Nur Goldstaub (glatte Zahlen) mit einem Sieb sammeln
Bereiten Sie zunächst eine geeignete Zahl $Z$ vor, quadrieren Sie sie und berechnen Sie den Rest $W$, wenn sie durch $N$ geteilt wird.
(Die Restwelt von $Z^2 = W$)

Faktorisieren Sie den erhaltenen Rest $W$ in Primzahlen. Hier gilt: Nur wenn ** "ein $W$, das nur aus kleinen Primzahlen wie 2, 3, 5, 7 usw. besteht" ** , erscheint, behalten Sie diese Gleichung als "Gewinnerkarte" und werfen Sie sie weg, wenn große Primzahlen beigemischt sind.
Es ist wie das Wegwerfen großer Steine mit einem Sieb in einem Fluss, um nur Goldstaub zu sammeln.

### Schritt 2: Das Puzzle, um alles "gerade" zu machen
Nehmen wir zum Beispiel an, die folgenden 3 Goldstaubkarten wurden gesammelt.
* Karte A: $Z_1^2 = 2^3 \times 3^1$
* Karte B: $Z_2^2 = 2^1 \times 5^1$
* Karte C: $Z_3^2 = 3^1 \times 5^1$

Lassen Sie uns alle multiplizieren.
Die rechte Seite wird zu $(2^3 \times 3^1) \times (2^1 \times 5^1) \times (3^1 \times 5^1)$,
Und wenn man alles ordnet, wird es zu ** "$2^4 \times 3^2 \times 5^2$" ** .

Überraschenderweise wurde die Anzahl der Primzahlen zu "4, 2, 2", ** allesamt eine gerade Zahl ** !
Dass alle gerade sind, bedeutet, dass wenn man die Gesamtmenge halbiert, es "das Quadrat von etwas" sein wird.
Mit anderen Worten, $(2^2 \times 3^1 \times 5^1)^2 = (60)^2$.

Die linke Seite ist $(Z_1 \times Z_2 \times Z_3)^2$, also sind wir endlich am Ziel:
** $X = (Z_1 \times Z_2 \times Z_3)$ ** 
** $Y = 60$ ** 
Das lang ersehnte Paar von "$X^2 = Y^2$" ist komplett!

Für Computer ist das Puzzle, zu berechnen, ob die Anzahl der Primzahlen "gerade oder ungerade (0 oder 1)" ist, etwas, worin sie sehr gut sind, sodass mit dieser Methode $X$ und $Y$ mit hoher Geschwindigkeit gefunden werden können.

---

## Kapitel 3: Die Mauer der Verzweiflung

Jetzt kann jeder Code geknackt werden! ...oder das dachten wir zumindest, aber ein großes Problem tritt auf.
Wenn die Verschlüsselungszahl $N$ bis zu "100 Stellen" umfasst, kann diese Methode (Quadratisches Sieb genannt) sie lösen, aber wenn $N$ zu "200 oder 300 Stellen" wird, wird das in der Mitte der Berechnung auftretende $W$ viel zu groß.

Wenn die Zahlen zu groß werden, tauchen "Zahlen, die nur aus kleinen Primzahlen (Goldstaub) bestehen", einfach nicht mehr auf. Es wird schwieriger, als eine Kontaktlinse in der Wüste zu suchen, und die zum Lösen des Puzzles benötigten Karten sammeln sich gar nicht erst an.

Hier tritt schließlich die ultimative Waffe der Menschheit, das ** "General Number Field Sieve (GNFS)" ** , auf den Plan.

---

## Kapitel 4: Die stärkste Idee der Menschheit, "Zwei Welten" zu erschaffen

Die geniale Idee des GNFS ist: ** "Die Zahlen werden gigantisch, weil wir nur in der realen Welt rechnen. Lassen Sie uns also eine 'Hinterwelt' mit Polynomen (Buchstabenformeln) erschaffen, um das Gewicht der Berechnung in zwei Hälften zu teilen." ** 

### Die Magie der Buchstabenformeln
GNFS wandelt die riesige Zahl $N$ unter Verwendung einer Basiszahl $m$ in einen Buchstabenausdruck um.
Wenn zum Beispiel $N=100$ ist, mit $m=4$, dann ist $100 = 4^3 + 2(4^2) + 4$.
Mit dem Buchstaben $x$ machen wir daraus eine Formel (die Hinterwelt): ** $f(x) = x^3 + 2x^2 + x$ ** .

Das Interessante an dieser Formel ist, dass sie die Eigenschaft hat, ** "wenn Sie $x$ durch $m$ ersetzen (4 im obigen Beispiel), können Sie immer zur realen Zahl $N$ zurückkehren" ** .

### Gleichzeitig in 2 Welten nach Goldstaub suchen
GNFS erzeugt viele Paare von zufälligen Ganzzahlen $(a, b)$ und führt gleichzeitig die folgenden zwei Berechnungen durch:
1. ** Reale Welt ** : $a - b \times m$
2. ** Buchstabenwelt ** : Der Wert von $a - b \times x$, berechnet nach den Regeln der Polynome

Durch die Aufteilung des Problems in zwei Welten verringert sich die Größe (das Gewicht) der verarbeiteten Zahlen drastisch. Es ist, als würde man einen riesigen Felsen in zwei handliche Steine spalten.

Dann trennen und sammeln Sie mit einem Sieb nur die Wunderpaare $(a, b)$, bei denen ** "sowohl in der realen Welt als auch in der Buchstabenwelt beide 'nur aus kleinen Primzahlen (Goldstaub) bestehen'" ** . Daher der Name "Zahlkörpersieb" (Number Field Sieve).

### Der Moment, in dem die Verschlüsselung endlich geknackt wird
Sobald Dutzende Millionen von "Goldstaubkarten" aus beiden Welten gesammelt wurden, verwendet der Supercomputer gigantische Matrixberechnungen, um "eine Kombination zu finden, bei der die Anzahl der Primzahlen alle gerade ist", genau wie wir es in Kapitel 2 getan haben.

Sobald die Kombination gefunden ist:
* Sei die Quadratzahl in der realen Welt ** $X^2$ ** 
* Sei die in der Buchstabenwelt erstellte Quadratformel ** $Y(x)^2$ ** 

Ersetzen Sie schließlich das $x$ in der Buchstabenformel $Y(x)$ durch $m$, springen Sie in die reale Welt zurück und verbinden Sie sie.
Dann ist, wie durch mathematische Magie, die Bedingung erfüllt, dass ** "die Reste von $X^2$ und $Y^2$ gleich sind" ** !

Der Rest besteht, wie in Kapitel 1, lediglich darin, den größten gemeinsamen Teiler von $X - Y$ und $N$ zu berechnen, und die uneinnehmbare RSA-Verschlüsselung wird zusammenbrechen und die geheimen Primzahlen offenbaren.

---

## Fazit: Die Mathematik endet nie

Sie denken vielleicht: "Großartig, mit GNFS kann jede Verschlüsselung geknackt werden!".
Doch auch die RSA-Verschlüsselung hat nicht aufgegeben. Was im heutigen Internet verwendet wird, ist eine monströs gigantische Zahl namens "RSA-2048 (ca. 617 Stellen)".

Obwohl GNFS der stärkste Algorithmus der Menschheit ist, sagt man, dass selbst das Lösen von 270 Stellen (RSA-270) Tausende oder Zehntausende von Jahren dauern würde, selbst wenn man Computer auf der ganzen Welt miteinander verbindet. Vorerst sind unsere LINE- und Bankdaten sicher.

Aber was wäre, wenn eine ** "Magie, um $X$ und $Y$ für jede riesige Zahl sofort zu finden" ** , auftauchen würde?
Tatsächlich kommt der ** "Quantencomputer (Shor-Algorithmus)" ** , der sich derzeit in der Entwicklung befindet, dem am nächsten. Unter Ausnutzung der Wellennatur der Quantenmechanik wurde mathematisch bewiesen, dass es möglich ist, das mühsame Kartensammelpuzzle zu umgehen und die Antwort auf einen Schlag zu finden.

Ein endloser Kampf des Verstandes zwischen denen, die Verschlüsselung erschaffen (Verteidigung), und denen, die Algorithmen entwickeln, um sie zu knacken (Angriff).
Macht das Wissen, dass die in der Mittelstufe erlernte "Primfaktorzerlegung" und "algebraische Ausdrücke" tatsächlich die Waffen sind, die an vorderster Front der globalen Sicherheit kämpfen, den Mathematikunterricht nicht ein wenig interessanter?

Derjenige, der den stärksten Algorithmus der Zukunft entdeckt, könnten Sie sein, der diesen Artikel liest!

--- 
*(※Dieser Artikel ist eine konzeptionelle Adaption der mathematischen Faszination des Codeknackens für Schüler. Das eigentliche GNFS wird streng mit Hilfe der fortgeschrittenen Universitätsmathematik, wie Idealklassengruppen algebraischer Zahlkörper und Homomorphismen, berechnet)*
