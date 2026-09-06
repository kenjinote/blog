---
title: "Die wahre mathematische Struktur des allgemeinen Zahlkörpersiebs (GNFS)"
date: 2026-09-05T02:26:13+09:00
tags: ["Mathematik", "Kryptographie", "RSA", "GNFS"]
draft: false
image: "rsa_encryption_break_1788542156523.jpg"
categories: ["Mathematik, Kryptographie und Quanten"]
---

# Die wahre mathematische Struktur des allgemeinen Zahlkörpersiebs (GNFS)

Das ultimative Ziel des GNFS ist es, $X, Y$ so zu finden, dass $X^2 \equiv Y^2 \pmod N$ gilt.
Um dies zu erreichen, bauten Mathematiker eine Brücke zwischen der **"Welt der reellen ganzen Zahlen"** und der **"Welt der algebraischen Zahlkörper"** . Diese Brücke ist der sogenannte "Homomorphismus".

## Phase 1: Die Welten mit "Homomorphismus" verbinden

### 1. Auswahl des Polynoms und Definition der Wurzeln
Für eine riesige zusammengesetzte Zahl $N$ wählen wir eine ganze Zahl $m$ und ein Polynom $f(x)$ so, dass $f(m) \equiv 0 \pmod N$ gilt.
(Beispiel: Wir entwickeln $N$ zur Basis $m$ und bilden $f(x)$ aus den Koeffizienten. Dabei nehmen wir an, dass $f(x)$ über dem Körper der rationalen Zahlen $\mathbb{Q}$ irreduzibel ist (nicht weiter faktorisiert werden kann)).

Als Nächstes definieren wir eine der "komplexen Wurzeln" der Gleichung $f(x) = 0$ als $\alpha$.
Natürlich ist $f(\alpha) = 0$. $\alpha$ ist keine ganze Zahl, sondern eine komplexe Zahl, die Wurzeln und imaginäre Zahlen enthält (eine algebraische Zahl).

### 2. Konstruktion von Ringen und Homomorphismus
Hier bereiten wir zwei mathematische "Ringe" vor (Welten, in denen Addition und Multiplikation definiert sind).

*   **Welt A: $\mathbb{Z}[\alpha]$** (Der Ring der algebraischen ganzen Zahlen, der $\alpha$ enthält)
    Eine Zahlenwelt in der Form $a + b\alpha + c\alpha^2 + \dots$.
*   **Welt B: $\mathbb{Z}/N\mathbb{Z}$** (Der Ring der Reste modulo $N$)
    Eine Kongruenzwelt (Modulo), die nur aus den ganzen Zahlen von $0$ bis $N-1$ besteht.

Hier definieren wir eine Abbildung $\phi$ von Welt A nach Welt B wie folgt:
**$$\phi : \mathbb{Z}[\alpha] \to \mathbb{Z}/N\mathbb{Z}$$**
**$$\phi(\alpha) = m \pmod N$$**

Diese Abbildung $\phi$ ist eine magische Operation, die exakt die Variable $\alpha$ in Welt A durch die ganze Zahl $m$ in Welt B ersetzt.
Dieses $\phi$ besitzt eine extrem mächtige Eigenschaft, die **"Ringhomomorphismus"** genannt wird.
Homomorphismus ist die Eigenschaft, **"in eine andere Welt zu teleportieren, ohne die Struktur von Addition und Multiplikation zu zerstören"** . Das heißt, die folgenden Gleichungen sind gültig:
*   $\phi(X \times Y) = \phi(X) \times \phi(Y)$
*   $\phi(X^2) = \phi(X)^2$

Was bedeutet das? Wenn wir das **"Quadrat ($\gamma^2$)"** eines komplexen Elements $\gamma$ in "Welt A (der Welt von $\alpha$)" erzeugen und es mithilfe von $\phi$ nach "Welt B (der Restewelt)" teleportieren können, **bleibt die quadratische Form $\phi(\gamma)^2$ perfekt erhalten** .

---

## Phase 2: Der Zusammenbruch der Primfaktorzerlegung und die Geburt der "Ideale"

In Welt A ($\mathbb{Z}[\alpha]$) wollen wir viele geeignete Elemente $(a - b\alpha)$ sammeln und sie multiplizieren, um ein "perfektes Quadrat (Quadratelement)" zu erzeugen.
Normalerweise würden wir jedes gesammelte $(a - b\alpha)$ in Primfaktoren zerlegen und sie so kombinieren, dass die Exponenten der Primzahlen alle gerade sind (durch Lösen mit Matrizen), um ein Quadrat zu bilden.

**Jedoch stellt sich hier die verzweifelte Mauer der Algebra in den Weg.**
In algebraischen Welten wie $\mathbb{Z}[\alpha]$ **bricht die "Eindeutigkeit der Primfaktorzerlegung (jede Zahl kann eindeutig als Produkt von Primzahlen ausgedrückt werden)", die in der Schule gelehrt wird, zusammen** .

(Beispiel: In einer bestimmten algebraischen Welt ist $6 = 2 \times 3$, aber gleichzeitig auch $6 = (1+\sqrt{-5}) \times (1-\sqrt{-5})$, und wir wissen nicht mehr, welche die wahren Primzahlen sind)

Wenn die Faktorzerlegung nicht eindeutig ist, ist das Rätsel "Primzahlen zählen, um sie gerade zu machen" (die Siebmethode) im Prinzip unmöglich auszuführen.

### Die Rettung durch Kummer und Dedekind: "Ideale"
Was diesen Zusammenbruch rettete, war das Konzept des **"Ideals (Ideal: ideale Zahl)"** , das von Mathematikern des 19. Jahrhunderts geschaffen wurde.
Indem man nicht an das Element selbst dachte, sondern an die "Menge der Vielfachen (Ideal)", die von diesem Element erzeugt wird, wurde die Primfaktorzerlegung wieder möglich.

Im Ganzheitsring eines algebraischen Zahlkörpers $\mathcal{O}_K$ (ein vollständigerer Ring, der $\mathbb{Z}[\alpha]$ enthält) ist bewiesen, dass selbst wenn ein Element nicht eindeutig faktorisiert werden kann, **"ein Ideal immer eindeutig als Produkt von 'Primidealen ($\mathfrak{p}$)' faktorisiert werden kann"** .

Daher faktorisieren wir im GNFS nicht das Element $(a - b\alpha)$ selbst, sondern das **von ihm erzeugte Hauptideal $\langle a - b\alpha \rangle$ in Primideale** .

---

## Phase 3: Die Norm und die zwei Siebe

Woher wissen wir also, in welche Primideale das Ideal $\langle a - b\alpha \rangle$ zerfällt?
Hier verwenden wir eine Funktion namens **"Norm"** . Die Norm ist eine Funktion, die komplexe Elemente algebraischer Körper in "normale reelle ganze Zahlen $\mathbb{Z}$" umwandelt.

Die Norm des Elements $(a - b\alpha)$ wird durch eine einfache Polynomrechnung $b^d f(a/b)$ gefunden ($d$ ist der Grad von $f(x)$).

Durch einen algebraischen Satz wissen wir: **"Wenn die Norm eines bestimmten Ideals vollständig in kleine Primzahlen zerlegt werden kann (glatt ist), dann kann das ursprüngliche Ideal auch vollständig in kleine Primideale zerlegt werden"** .

Daher berechnet GNFS für eine große Anzahl von Ganzzahlpaaren $(a, b)$ gleichzeitig die folgenden zwei Werte und sammelt nur die Paare, bei denen beide zu "glatten Zahlen (smooth numbers)" werden:
1. **Rationales Sieb (Rational Sieve)** : $a - bm$ (der Wert in der realen Welt)
2. **Algebraisches Sieb (Algebraic Sieve)** : $b^d f(a/b)$ (die Norm in der algebraischen Welt)

Indem wir zig Millionen Paare $(a, b)$ sammeln, bei denen beide glatt sind, lösen wir die Daten der Primidealzerlegung (wie viele Primideale enthalten sind) als riesige Matrix (lineare Algebra über GF(2)), um eine Menge $S$ von Paaren zu finden, sodass "beim Multiplizieren die Exponenten aller Primideale gerade werden".

---

## Phase 4: Die zwei "Hindernisse" und die Idealklassengruppe

Aus der Matrixberechnung haben wir herausgefunden, dass das Multiplizieren aller Ideale von $(a - b\alpha)$, die zur Menge $S$ gehören, zum Quadrat eines bestimmten Ideals $I$ führt.
$$\prod_{S} \langle a - b\alpha \rangle = I^2$$

**Es ist jedoch noch nicht vorbei. Die tiefste und schwierigste mathematische Mauer des GNFS befindet sich hier.**

Was wir am Ende wollen, ist nicht das "Quadrat eines Ideals", sondern das **"Quadrat eines Elements ($\gamma^2$)"** , das wir in die Abbildung $\phi$ einsetzen können.
Nur weil es zum Quadrat eines Ideals wurde, heißt das nicht zwangsläufig, dass das Element selbst ein Quadrat ist. Hier gibt es **zwei starke mathematische Hindernisse (Obstructions)** .

### Hindernis ①: Die Barriere der Idealklassengruppe (Ideal Class Group)
Das Ideal $I$ ist nicht immer ein "Ideal, das von einem einzigen Element erzeugt wird (Hauptideal)".
Es ist unmöglich, ein spezifisches Element $\gamma$ aus einem Ideal zu extrahieren, das kein Hauptideal ist.

Hier kommt das Konzept der **"Idealklassengruppe (Class Group, $Cl_K$)"** ins Spiel. Die Idealklassengruppe ist eine Gruppe, die misst, "wie viele Ideale in dieser algebraischen Welt existieren, die keine Hauptideale sind (wie sehr die Eindeutigkeit der Primfaktorzerlegung gebrochen ist)".
Selbst wenn $\prod \langle a - b\alpha \rangle$ zu $I^2$ wird, kann es nicht auf das Quadrat eines Elements zurückgeführt werden, wenn $I$ nicht das Identitätselement (Hauptideal) in der Idealklassengruppe ist.

### Hindernis ②: Die Barriere der Einheitengruppe (Unit Group)
Angenommen, durch Glück wäre $I$ das Hauptideal $\langle \gamma \rangle$.
Dann hätten wir $\prod \langle a - b\alpha \rangle = \langle \gamma^2 \rangle$.
Man könnte denken: "Großartig, das Element ist auch ein Quadrat!", aber das ist ein großer Irrtum.

Dass Ideale (Mengen von Vielfachen) gleich sind, bedeutet nicht, dass die Elemente perfekt gleich sind. Es wird immer eine Abweichung durch eine **"Einheit (Unit: eine Zahl, deren Kehrwert ebenfalls eine ganze Zahl ist. Wie 1 oder -1)"** geben.
Mit anderen Worten, die eigentliche Elementgleichung sieht so aus:
$$\prod_{S} (a - b\alpha) = u \cdot \gamma^2$$
($u$ ist ein Element der Einheitengruppe $U_K$)

Wenn diese Einheit $u$ nicht selbst das Quadrat von etwas ist, kann die linke Seite niemals ein "perfektes Quadrat eines Elements" werden.

---

## Phase 5: Adlemans Magie "Quadratische Charaktere" (Quadratic Characters)

Das Hindernis der Idealklassengruppe und das Hindernis der Einheitengruppe. Wie können wir diese beiden überwinden?
Hier kommt die brillante Methode der **"Quadratischen Charaktere (Quadratic Characters)"** ins Spiel, die von dem Kryptographen Leonard Adleman (das "A" von RSA) und anderen eingeführt wurde.

Um festzustellen, "ob ein bestimmtes Element ein perfektes Quadrat im algebraischen Körper ist", verwenden wir die Zahlkörper-Version des Legendre-Symbols (quadratischer Rest).
In dieser riesigen Matrix (dem Rätsel, um die Primidealzählungen gerade zu machen), **fügen wir heimlich ein paar Dutzend zusätzliche Bedingungen (Spalten) hinzu, die besagen: "Die quadratischen Charaktere für einige spezielle Primideale $\mathfrak{q}$ müssen ebenfalls alle $1$ (gerade) sein"** .

Wenn wir eine Menge $S$ finden, die durch die Matrixberechnung sogar diese zusätzliche Bedingungen erfüllt, garantieren tiefe Sätze aus der algebraischen Zahlentheorie, dass **"sowohl das Hindernis der Idealklassengruppe als auch das Hindernis der Einheitengruppe mit überwältigender Wahrscheinlichkeit natürlich verschwinden werden"** .

Damit erhalten wir endlich die wahre Gleichung.
$$\prod_{S} (a - b\alpha) = \gamma^2$$

---

## Letzte Phase: Die Verschmelzung der Welten und der Zusammenbruch der Kryptographie

Endlich sind alle Puzzleteile an ihrem Platz.

**[Elemente in der Welt der algebraischen Körper (Welt A)]**
$\gamma^2 = \prod (a - b\alpha)$
(Wir verwenden einen Quadratwurzel-Algorithmus, um $\gamma$ zu finden)

**[Elemente in der realen Welt (Welt der rationalen Zahlen)]**
$V^2 = \prod (a - bm)$
(Da dies eine einfache Ganzzahlmultiplikation ist, $V$ normal gefunden werden kann)

Nun ist es Zeit für die magische Brücke, die wir zu Beginn gebaut haben, den **Homomorphismus $\phi$** .
Wir teleportieren das Element $\gamma$ aus Welt A nach Welt B (die Welt der Reste von $N$) mithilfe von $\phi$ (die Abbildung, bei der wir $\alpha$ durch $m$ ersetzen).
$$Y = \phi(\gamma) \pmod N$$

Andererseits bringen wir das in der realen Welt gebaute $V$ direkt in die Restewelt und nennen es $X$.
$$X = V \pmod N$$

Aufgrund der "strukturerhaltenden" Eigenschaft des Homomorphismus bleibt die quadratische Beziehung, die in Welt A galt, in Welt B (der Welt modulo $N$) perfekt erhalten.
Da die ursprünglichen Paare $(a, b)$ außerdem in Entsprechung in den Formen $a - b\alpha$ und $a - bm$ erzeugt wurden, kollidieren diese $X$ und $Y$ in der Welt modulo $N$ und erzeugen die folgende absolute Gleichung:

**$$X^2 \equiv Y^2 \pmod N$$**

Alles, was bleibt, ist zu beten, dass diese $X$ und $Y$ keine trivialen Lösungen ($X \equiv \pm Y$) sind, und
**$\gcd(X - Y, N)$** zu berechnen.

Wenn es sich um eine nicht-triviale Lösung handelt, durchläuft der Euklidische Algorithmus sie in 0,001 Sekunden, und die geheimen Primzahlen $p$ und $q$, die das Herzstück der RSA-Kryptographie bilden, werden auf dem Ausgabebildschirm gedruckt.

---

Dies ist das vollständige Bild des **"Allgemeinen Zahlkörpersiebs (GNFS)"** , der Essenz der modernen Mathematik.
