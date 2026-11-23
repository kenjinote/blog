---
title: 'Gibt es einen Algorithmus, der das GNFS (Allgemeines Zahlkörpersieb) übertrifft?'
slug: "beyond-gnfs-integer-factorization-algorithms"
date: "2026-09-11T09:00:00+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["mathematics", "cryptography"]
tags: ["GNFS", "Integer Factorization", "RSA", "Algorithms"]
---

## 1. Einführung: Primfaktorzerlegung und die Grundlage der modernen Kryptographie

RSA ist eines von mehreren Public-Key-Systemen; seine Sicherheit hängt unter anderem von der Schwierigkeit der Faktorisierung großer Zahlen ab. Die Internetsicherheit insgesamt beruht jedoch nicht allein auf RSA. Eine effiziente Faktorisierung würde RSA-Anwendungen bedrohen, aber nicht automatisch die gesamte Kommunikationsinfrastruktur außer Kraft setzen.

Für die Faktorisierung allgemeiner großer Zahlen gehört GNFS zu den bekanntesten klassischen Verfahren. Damit wurden unter anderem RSA-768 und RSA-250 faktorisiert; für Zahlen besonderer Form können Verfahren wie SNFS geeigneter sein. [Bericht zu RSA-250](https://eprint.iacr.org/2020/697)

Kryptographen und Mathematiker stellen sich jedoch stets folgende Fragen: "Gibt es einen klassischen Algorithmus, der das GNFS übertrifft?", "Wo liegen die Grenzen klassischer Computer?" und "Wie werden Quantencomputer diese Situation überwinden?".

In diesem Artikel analysieren wir gründlich die tiefgründige mathematische Struktur hinter dem GNFS und führen detaillierte technische Analysen der Polynomauswahl, des Siebprozesses und des linearen Algebraschritts mithilfe der Block-Wiedemann-Methode durch. Darüber hinaus betrachten wir GNFS-Erweiterungsmethoden, wie die Coppersmith-Modifikation, und vergleichen sowie erklären wir die entscheidenden Unterschiede zwischen klassischen Algorithmen in subexponentieller Zeit (Sub-exponential time) und Quantenalgorithmen in polynomieller Zeit aus einer mathematischen Perspektive.

---

## 2. Asymptotische Komplexität und L-Notation (L-notation)

Bei der Bewertung der Komplexität von Faktorisierungsalgorithmen wird anstelle der Standard-Polynomzeit-Notation (wie $O(n^k)$) die **L-Notation (L-notation)** verwendet, um die subexponentielle Zeit relativ zur Anzahl der Stellen der Eingabe $n$ auszudrücken. Die L-Notation ist wie folgt definiert:

$$
L_n[\alpha, c] = \exp \left( (c + o(1)) (\ln n)^\alpha (\ln \ln n)^{1-\alpha} \right)
$$

Hierbei ist $n$ die zu faktorisierende ganze Zahl und $\ln n$ der natürliche Logarithmus, der proportional zur Bitlänge von $n$ ist.
- Wenn $\alpha = 0$: $L_n[0, c] = \exp(c \ln \ln n) = (\ln n)^c$, was die **Polynomzeit (Polynomial time)** bezogen auf die Bitlänge darstellt.
- Wenn $\alpha = 1$: $L_n[1, c] = \exp(c \ln n) = n^c$, was die **Exponentialzeit (Exponential time)** bezogen auf die Bitlänge darstellt.
- Wenn $0 < \alpha < 1$: Es handelt sich um eine **subexponentielle Zeit (Sub-exponential time)**, die zwischen der Polynomzeit und der Exponentialzeit liegt.

Die Geschichte der Entwicklung vergangener Faktorisierungsalgorithmen war auch eine Geschichte der allmählichen Verringerung dieses $\alpha$-Wertes.
- **CFRAC**: heuristische erwartete Laufzeit $L_n[1/2,\sqrt{2}]$ ([Referenz](https://cacr.uwaterloo.ca/hac/about/chap3.pdf)).
- **MPQS/QS**: heuristische erwartete Laufzeit $L_n[1/2,1]$ ([FLINT-Dokumentation](https://flintlib.org/doc/algorithms/number-theory/quadratic-sieve.html)).
- **GNFS**: die übliche heuristische Schätzung lautet $L_n[1/3,(64/9)^{1/3}]$; dies ist weder eine bewiesene Schranke noch eine direkte praktische Laufzeit ([NFS-Analyse](https://arxiv.org/abs/2007.02730)).

---

## 3. Der gesamte GNFS-Algorithmus und seine mathematische Struktur

GNFS und QS nutzen die Idee einer Kongruenz von Quadraten: Gesucht werden $X,Y$ mit $X^2\equiv Y^2\pmod n$ und $X\not\equiv\pm Y\pmod n$; dann kann $\gcd(X-Y,n)$ einen nicht-trivialen Faktor liefern.

Der Kern des GNFS liegt jedoch darin, dies nicht nur im Körper der rationalen Zahlen $\mathbb{Q}$ zu tun, sondern gleichzeitig "glatte Zahlen (Smooth numbers)" in einem Erweiterungskörper $\mathbb{Q}(\alpha)$, der als algebraischer Zahlkörper (Algebraic Number Field) bezeichnet wird, und im Körper der rationalen Zahlen zu suchen und durch einen Homomorphismus eine Kongruenzbeziehung herzustellen.

Der GNFS-Prozess ist grob in fünf Phasen unterteilt.

```mermaid
graph TD
  A["Faktorisierungsproblem (Eingabe n)"] --> B["1. Polynomauswahl (Polynomial Selection)"]
  B --> C["2. Siebphase (Sieving Phase)"]
  C --> D["3. Filterphase (Filtering Phase)"]
  D --> E["4. Lineare Algebra Phase (Linear Algebra Phase)"]
  E --> F["5. Quadratwurzelphase (Square Root Phase)"]
  F --> G["Ausgabe der Primfaktoren p, q"]```

### 3.1 Phase 1: Polynomauswahl (Polynomial Selection)

Der Erfolg des GNFS hängt stark von der Auswahl geeigneter Polynome ab. Das Ziel ist es, zwei irreduzible Polynome, $f_1(x)$ (rationale Seite) und $f_2(x)$ (algebraische Seite), zu finden, die eine gemeinsame Wurzel $m$ haben. Das heißt, sie erfüllen:
$f_1(m) \equiv f_2(m) \equiv 0 \pmod n$

Normalerweise wird für die rationale Seite ein lineares Polynom $f_1(x) = x - m$ gewählt, und für das Polynom der algebraischen Seite $f_2(x)$ wird ein normiertes Polynom vom Grad $d$ (typischerweise 5 oder 6) gewählt. Der klassischste Ansatz ist die **Base-$m$-Methode**.
Man wählt eine ganze Zahl $m = \lfloor n^{1/(d+1)} \rfloor$, die nahe an der $1/(d+1)$-ten Potenz von $n$ liegt, und entwickelt $n$ im $m$-adischen System.
$n = c_d m^d + c_{d-1} m^{d-1} + \dots + c_1 m + c_0$
Dadurch erhält man das Polynom $f_2(x) = c_d x^d + c_{d-1} x^{d-1} + \dots + c_0$. Offensichtlich gilt $f_2(m) = n \equiv 0 \pmod n$.

In modernen Implementierungen wird jedoch der **Kleinjung-Algorithmus** verwendet. Dieser optimiert algebraische Eigenschaften (wie Murphys $E$-Wert und $\alpha$-Wert), während er verhindert, dass die Koeffizienten der Polynome extrem groß werden (Optimierung der Skewness), und sucht nach Polynomen, die bei der Siebverarbeitung leicht glatte Zahlen erzeugen. Allein in diesen Schritt werden enorme Rechenressourcen investiert.

### 3.2 Phase 2: Siebphase (Sieving Phase)

Sobald die Polynome bestimmt sind, tritt der Algorithmus in die "Sieb"-Phase (Sieving) ein, die den höchsten Rechenaufwand aufweist. Hier suchen wir nach Paaren $(a, b)$. Dieses Paar ist teilerfremd, und es wird gefordert, dass die folgenden zwei Werte gleichzeitig "glatt" (Smooth) sind:

1. **Norm auf der rationalen Seite**: $F_1(a, b) = b \cdot f_1(a/b) = a - bm$
2. **Norm auf der algebraischen Seite**: $F_2(a, b) = b^d \cdot f_2(a/b)$

Im Grundmodell hat eine glatte Zahl nur Primfaktoren bis zur Siebgrenze. Praktische Varianten lassen teils zusätzliche große Primfaktoren zu; die genauen Kriterien hängen von der Implementierung ab.
Heutzutage ist eine Methode namens **Gittersieb (Lattice Sieving)** der Mainstream. Indem eine bestimmte Primzahl $q$ fixiert wird und nur $(a, b)$-Paare auf einem Teilgitter gesiebt werden, bei denen sowohl die rationale als auch die algebraische Seite ein Vielfaches von $q$ sind, wird eine extrem hohe Effizienz erreicht.

### 3.3 Phase 3: Filterphase (Filtering Phase)

Die Anzahl der glatten Relationen (Gleichungen), die bei der Siebverarbeitung gefunden werden, geht in die Hunderte von Millionen oder Milliarden. Diese enthalten jedoch auch viele nutzlose Informationen.
Das Ziel der Filterung ist es, eine riesige dünnbesetzte Matrix (Sparse Matrix) zu konstruieren und gleichzeitig deren Dimension so gering wie möglich zu halten.

Konkret werden die folgenden Operationen durchgeführt:
- **Singleton removal**: Entfernen von Relationen, die einen Primfaktor enthalten, der nur einmal vorkommt.
- **Clique removal / Merging**: Multiplizieren von Relationen, die Primfaktoren haben, die zweimal oder öfter vorkommen, um Variablen zu eliminieren und sie auf ein Gleichungssystem mit höherer Dichte, aber kleinerer Dimension zu reduzieren.

Dadurch wird eine Matrix mit Milliarden von Zeilen zu einer riesigen dünnbesetzten Matrix $\mathbf{A}$ (mit Elementen 0 und 1 über dem Körper $\mathbb{F}_2$) auf dem Niveau von zig Millionen Zeilen komprimiert.

### 3.4 Phase 4: Lineare Algebra Phase (Linear Algebra Phase)

Hier suchen wir einen von null verschiedenen Vektor $\mathbf{x}$ mit $\mathbf{A}\mathbf{x}=\mathbf{0}$ über $\mathbb{F}_2$, also einen Vektor im Kern (Nullraum) der dünn besetzten Matrix.

Für dünn besetzte Matrizen werden iterative Krylow-Verfahren wie Block Lanczos und Block Wiedemann eingesetzt. Der Bericht zur Faktorisierung von RSA-250 dokumentiert den Einsatz von Block Wiedemann; Auswahl und Leistung hängen von Matrix, Implementierung und Rechnerarchitektur ab. [RSA-250-Bericht](https://eprint.iacr.org/2020/697)


### 3.5 Phase 5: Quadratwurzel Phase (Square Root Phase)

Aus der Lösung der linearen Algebra werden Produkte konstruiert, die auf der rationalen bzw. der algebraischen Seite zu "vollständigen Quadraten" werden.
Auf der rationalen Seite wird $\prod (a-bm)$ zum Quadrat $X^2$ einer ganzen Zahl $X$, und auf der algebraischen Seite wird das Produkt der entsprechenden Ideale zu einem vollständigen Quadrat $\gamma^2$ über dem algebraischen Zahlkörper.
Indem man dieses $\gamma$ über dem algebraischen Zahlkörper berechnet und den Homomorphismus zum Ring der rationalen ganzen Zahlen $\phi: \alpha \mapsto m \pmod n$ anwendet, erhält man die Kongruenz:
$X^2 \equiv \phi(\gamma)^2 \equiv Y^2 \pmod n$

Für die Berechnung der Quadratwurzel über dem algebraischen Zahlkörper werden komplexe Algorithmen wie die **Montgomery-Methode (Montgomery's Method)** verwendet, was tiefe Kenntnisse der algebraischen Zahlentheorie erfordert. Schließlich wird $\gcd(X-Y, n)$ berechnet, und wenn ein nicht-trivialer Faktor erhalten wird, ist die Primfaktorzerlegung abgeschlossen.

---

## 4. Gibt es einen klassischen Algorithmus, der das GNFS übertrifft?

Bisher wurde für die Primfaktorzerlegung allgemeiner ganzer Zahlen kein klassischer Algorithmus entdeckt, dessen asymptotische Komplexität unter $L_n[1/3, c]$ fällt. Es gibt jedoch einige Versuche und abgeleitete Algorithmen, um theoretische und praktische Grenzen zu durchbrechen.

### 4.1 Vielfaches Zahlkörpersieb (MNFS: Multiple Number Field Sieve)

Als Ansatz zur Erweiterung des GNFS gibt es das **Vielfache Zahlkörpersieb (MNFS)** von D. Coppersmith. Während das GNFS zwei Polynome (rationale und algebraische Seite) verwendet, verwendet das MNFS gleichzeitig mehrere verschiedene algebraische Polynome für ein einzelnes Polynom auf der rationalen Seite.

$$ f_1(x), f_{2,1}(x), f_{2,2}(x), \dots, f_{2,V}(x) $$

Durch die Verwendung mehrerer algebraischer Körper kann die Wahrscheinlichkeit, dass die Zahl in jedem Siebschritt "in einem der algebraischen Körper glatt wird", drastisch erhöht werden. Mit diesem Ansatz ist es Coppersmith gelungen, die Konstante $c$ in der Komplexität $L_n[1/3, c]$ leicht zu reduzieren.

In der Praxis ist jedoch der Overhead durch die Verwaltung mehrerer Körper groß, und es hat nicht zu einem entscheidenden Durchbruch bei [RSA](https://kenji.blog/de/p/modern-cryptography-public-key-hash-signature/)-Modulen in praktischer Größe geführt.

### 4.2 Sind Algorithmen der Klasse $L_n[1/4]$ möglich?

Derzeit ist kein klassischer allgemeiner Faktorisierungsalgorithmus mit geringerer asymptotischer Komplexität als die übliche GNFS-Form bekannt. Das beweist nicht, dass ein besserer Algorithmus unmöglich ist. Analysen glatter Zahlen beschreiben bekannte Siebverfahren, aber keine untere Schranke für alle Algorithmen; die Frage bleibt offen.
---

## 5. Durchbruch durch Quantencomputer: Shors Algorithmus

Während klassische Computer an der $L_n[1/3]$-Wand stehen, zerschmetterte der 1994 von Peter Shor vorgestellte **Shor-Algorithmus ([Shor's Algorithm](https://kenji.blog/de/p/quantum-computing-shors-algorithm/))** diese Wand, indem er das Berechnungsmodell grundlegend veränderte.

### 5.1 Der Schock der quantenmechanischen Polynomzeit

Shors Algorithmus reduziert das Faktorisierungsproblem auf ein "Ordnungsfindungsproblem (Order Finding Problem)". Es geht darum, die Periode (Ordnung) $r$ der Funktion $f(x) = a^x \pmod n$ für eine bestimmte ganze Zahl $a$ zu finden.
Shor nutzt Quanteninterferenz, um Information über die Periode der Funktion zu gewinnen; das bedeutet nicht, dass alle überlagerten Zustände parallel ausgelesen werden.

In Bezug auf die Komplexität ist die Ausführungszeit von Shors Algorithmus eine **quantenmechanische Polynomzeit**, konkret:
$$ O((\log n)^3) $$

```mermaid
graph LR
  A["Klassischer Algorithmus (GNFS)"] -->|"Grenze"| B["Subexponentielle Zeit L_n[1/3]"]
  C["Quantenalgorithmus (Shor)"] -->|"Durchbruch"| D["Polynomzeit O((log n)^3)"]
  B --> E["Fortgesetzte Nutzung von RSA (Längere Schlüssel)"]
  D --> F["RSA gefährdet, falls ein ausreichend leistungsfähiger fehlertoleranter Quantencomputer existiert"]
```

### 5.2 Klassische subexponentielle Zeit vs Quantenmechanische Polynomzeit

Shor faktorisiert im idealisierten Quantenmodell in Polynomialzeit, doch daraus folgt keine praktische Kostenschätzung für ein fehlertolerantes Gerät. Gidney und Ekerå schätzten 2021 etwa 20 Millionen physische Qubits und 8 Stunden; Gidney schätzte 2025 für einen anderen Entwurf und andere Annahmen weniger als eine Million verrauschte physische Qubits und weniger als eine Woche. Das sind bedingte Schätzungen, keine Demonstrationen eines Angriffs auf RSA-2048; bisher hat kein Quantencomputer eine Zahl dieser Größe faktorisiert. Aus $2048^3$ allein lassen sich weder Gatterzahl noch Laufzeit ableiten. [2021](https://doi.org/10.22331/q-2021-04-15-433) · [2025](https://arxiv.org/abs/2505.15917)

Auch die asymptotische GNFS-Formel ergibt nicht direkt eine Operationszahl oder Laufzeit; dafür braucht man ein explizites Kostenmodell und Parameter.
## 6. Zusammenfassung: Ausblick auf die nächste Generation

GNFS ist das beste bekannte allgemeine Verfahren, aber keine bewiesene Grenze. Es ist kein klassischer allgemeiner Algorithmus mit besserer asymptotischer Komplexität bekannt, doch ein Unmöglichkeitsbeweis existiert nicht. Praktische Verbesserungen rechtfertigen weder Zeitgarantien noch die Prognose, RSA bleibe jahrzehntelang sicher. Shor-Ressourcenschätzungen sind bedingt und beschreiben nicht heutige Geräte. Die Umstellung auf Post-Quanten-Kryptographie folgt einschlägigen Standards und Empfehlungen.
