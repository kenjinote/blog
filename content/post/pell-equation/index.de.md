---
title: "Pellsche Gleichung: Der Reiz der Diophantischen Gleichung mit Unendlichen Lösungen und Kettenbrüchen"
description: "Ein detaillierter Leitfaden zur Pellschen Gleichung, ihrer Lösung mittels Kettenbrüchen und der Generierung unendlich vieler Lösungen."
slug: "pell-equation"
date: "2026-09-24T16:08:36+09:00"
image: "eyecatch.jpg"
categories:
  - "mathematik"
tags:
  - "pellsche-gleichung"
  - "diophantische-gleichung"
  - "kettenbruch"
  - "zahlentheorie"
---

# Einführung

Im Gebiet der Zahlentheorie ist die **[Pellsche Gleichung](https://kenji.blog/de/p/pell-equation/)** (Pell's equation) als eine der schönsten diophantischen Gleichungen mit einem tiefgreifenden theoretischen Hintergrund bekannt. In diesem Artikel werden wir eine sehr detaillierte Erklärung geben, beginnend mit der grundlegenden Definition und den Eigenschaften dieser Gleichung, bis hin zu einer eleganten und effizienten Lösungsmethode mithilfe von Kettenbrüchen (Continued fractions) und dem Mechanismus zur Generierung ihrer unendlich vielen Lösungen. Für alle, die die Mathematik lieben, haben wir alles abgedeckt, von der Herleitung von Formeln bis zur Visualisierung von Algorithmen und der Implementierung mit einer Programmiersprache.

## 1. Was ist die [Pellsche Gleichung](https://kenji.blog/de/p/pell-equation/)?

Die [Pellsche Gleichung](https://kenji.blog/de/p/pell-equation/) bezeichnet eine quadratische diophantische Gleichung in zwei Variablen mit der folgenden Form:

$$ x^2 - ny^2 = 1 $$

Hierbei ist $n$ eine positive ganze Zahl, die keine Quadratzahl ist (quadratfrei oder zumindest kein perfektes Quadrat). Unser Ziel ist es, Paare unbekannter ganzer Zahlen $x$ und $y$ zu finden, die diese Gleichung erfüllen. Nehmen wir für einen Moment an, dass $n$ ein perfektes Quadrat ist, d.h. $n = k^2$ (wobei $k$ eine ganze Zahl ist). Dann kann die Gleichung wie folgt umgeformt werden:

$$ x^2 - k^2y^2 = 1 $$
$$ (x - ky)(x + ky) = 1 $$

Da $x$, $y$ und $k$ alle ganze Zahlen sind, müssen $(x - ky)$ und $(x + ky)$ ebenfalls ganze Zahlen sein. Die einzigen Kombinationen ganzer Zahlen, deren Produkt 1 ergibt, sind $(1, 1)$ oder $(-1, -1)$. Die Lösung hierfür ergibt $y = 0$, was bedeutet, dass die einzigen Lösungen die sehr einfachen $(x, y) = (\pm 1, 0)$ sind. Daher ist in der Pellschen Gleichung die Bedingung, dass $n$ kein perfektes Quadrat ist, eine wesentliche Voraussetzung, um sinnvolle Lösungen zu finden.

## 2. Historischer Hintergrund: Pell, [Fermat](https://kenji.blog/de/p/fermat/) und alte indische Mathematiker

Obwohl diese Gleichung den Namen "Pell" trägt, offenbart die Erforschung der historischen Fakten einen etwas seltsamen Hintergrund. Tatsächlich war die erste Person im modernen Europa, die eine allgemeine Lösung für diese Gleichung studierte und nachdrücklich behauptete, dass immer eine Lösung existiert, der große französische Mathematiker **[Pierre de Fermat](https://kenji.blog/de/p/fermat/)**.

Später brachte **[Leonhard Euler](https://kenji.blog/de/p/euler/)** fälschlicherweise den Namen des englischen Mathematikers **John Pell** mit dieser Gleichung in Verbindung, und seitdem ist sie weithin als "[Pellsche Gleichung](https://kenji.blog/de/p/pell-equation/)" bekannt. Pell selbst spielte keine zentrale Rolle bei der Lösungsmethode für diese Gleichung.

Wenn man weiter in die Vergangenheit zurückgeht, so berechneten die indischen Mathematiker **Brahmagupta** und **Bhāskara II** hunderte Jahre vor [Fermat](https://kenji.blog/de/p/fermat/) Lösungen für Gleichungen dieser Art unter Verwendung eines ausgeklügelten Algorithmus, der als Chakravala-Methode bezeichnet wird. Die Geschichte der Erforschung durch Mathematiker von der Antike über das Mittelalter bis in die Neuzeit ist in dieser Gleichung eingeschrieben.

## 3. Der Unterschied zwischen trivialen und nicht-trivialen Lösungen

Für die [Pellsche Gleichung](https://kenji.blog/de/p/pell-equation/) $x^2 - ny^2 = 1$ gibt es unabhängig vom Wert von $n$ immer die Lösung $(x, y) = (\pm 1, 0)$. Setzt man diese in die Gleichung ein, so erhält man $1^2 - n \cdot 0^2 = 1$, was offensichtlich wahr ist. Dies wird als **triviale Lösung** (trivial solution) bezeichnet.

Was Mathematiker jedoch wirklich interessiert, ist eine **nicht-triviale Lösung** (non-trivial solution), bei der $y \neq 0$ ist. Erstaunlicherweise wurde mathematisch bewiesen, dass die [Pellsche Gleichung](https://kenji.blog/de/p/pell-equation/) **unendlich viele nicht-triviale Lösungen** besitzt, wenn $n$ eine positive ganze Zahl ist, die kein perfektes Quadrat ist. Unter diesen unendlichen Lösungen wird außerdem die kleinste Lösung, bei der sowohl $x$ als auch $y$ positive ganze Zahlen sind, als **Fundamentallösung** (fundamental solution) bezeichnet, und sobald diese gefunden ist, können alle anderen Lösungen leicht durch algebraische Operationen generiert werden.

## 4. Die tiefe Verbindung zwischen Kettenbrüchen und der Pellschen Gleichung

Das leistungsfähigste und standardmäßigste Werkzeug, um die Fundamentallösung effizient zu finden, ist der **Kettenbruch** (Continued fraction). Da die irrationale Zahl $\sqrt{n}$ nicht durch einen endlichen Bruch dargestellt werden kann, kann sie wunderbar als ein unendlich fortdauernder periodischer regulärer Kettenbruch ausgedrückt werden.

$$ \sqrt{n} = [a_0; \overline{a_1, a_2, \dots, a_k, 2a_0}] $$

Hierbei ist $a_0$ der ganzzahlige Teil von $\sqrt{n}$ (d.h. $\lfloor \sqrt{n} \rfloor$), und der Teil unter dem Überstrich stellt den periodischen Teil des Kettenbruchs dar. Sei $m$ die Länge dieser Periode.

Die rationale Zahl $\frac{p_i}{q_i}$, die durch Abbrechen des Kettenbruchs an einem bestimmten Glied erhalten wird, wird als **Näherungsbruch** (convergent) bezeichnet. Näherungsbrüche liefern die besten rationalen Approximationen für die irrationale Zahl $\sqrt{n}$. Erstaunlicherweise wird die Fundamentallösung $(x_1, y_1)$ der Pellschen Gleichung direkt aus dem Zähler $p$ und dem Nenner $q$ eines bestimmten Näherungsbruchs in der Kettenbruchentwicklung von $\sqrt{n}$ gewonnen. Genauer gesagt wird sie wie folgt durch die Länge der Periode $m$ bestimmt:

- Wenn die Periode $m$ gerade ist: Die Fundamentallösung ist $(p_{m-1}, q_{m-1})$.
- Wenn die Periode $m$ ungerade ist: Die Fundamentallösung ist $(p_{2m-1}, q_{2m-1})$.

## 5. Finden der Fundamentallösung: Eine gründliche Erklärung des Algorithmus

Die Näherungsbrüche $\frac{p_i}{q_i}$ können mit Hilfe der folgenden Rekursionsformeln auf einem Computer sehr schnell berechnet werden.

$$ p_i = a_i p_{i-1} + p_{i-2} $$
$$ q_i = a_i q_{i-1} + q_{i-2} $$

Die Anfangsbedingungen werden wie folgt festgelegt, damit der Algorithmus reibungslos starten kann:
- $p_{-1} = 1, \quad p_{-2} = 0$
- $q_{-1} = 0, \quad q_{-2} = 1$

Jedes Glied $a_i$ des Kettenbruchs kann auch sequentiell nur unter Verwendung ganzzahliger arithmetischer Operationen gefunden werden. Dies ermöglicht genaue ganzzahlige Berechnungen, die Gleitkommafehler vollständig ausschließen.

Um die Reihe von Prozessen bei der Suche nach einer Lösung zu visualisieren, haben wir das folgende [Zustand](https://kenji.blog/de/p/state-management-history-redux-context-recoil-zustand/)sübergangsdiagramm vorbereitet.

```mermaid
flowchart TD
    Start["Start: Ganzzahl n eingeben"] --> CheckSquare["Bestimmen, ob n ein perfektes Quadrat ist"]
    CheckSquare --|"Ja"| Trivial["Nur triviale Lösungen existieren (Ende)"] --> End["Ende"]
    CheckSquare --|"Nein"| InitContFrac["Rekursion für Kettenbruch initialisieren"]
    InitContFrac --> CalcNext["Nächstes Glied a_i und Näherungsbruch (p_i, q_i) berechnen"]
    CalcNext --> CheckEq["Bedingung: p_i^2 - n * q_i^2 == 1 auswerten"]
    CheckEq --|"Falsch"| CalcNext
    CheckEq --|"Wahr"| Found["Fundamentallösung (x_1, y_1) = (p_i, q_i) gefunden"] --> End
```

## 6. Konkretes Beispiel: Kettenbruchentwicklung und Fundamentallösung für n = 7

Anstatt nur bei abstrakter Theorie zu bleiben, wollen wir die Berechnungen für den konkreten Fall $n = 7$ nachvollziehen. Die [Pellsche Gleichung](https://kenji.blog/de/p/pell-equation/) wird zu $x^2 - 7y^2 = 1$.

Zuerst ist der ganzzahlige Teil von $\sqrt{7}$ $a_0 = 2$. Durch Wiederholen der Operation, den Kehrwert des verbleibenden Dezimalteils zu nehmen und den ganzzahligen Teil zu extrahieren, ergibt sich die Kettenbruchentwicklung von $\sqrt{7}$ wie folgt:

$$ \sqrt{7} = [2; \overline{1, 1, 1, 4}] $$

Die Periode ist $m = 4$, was gerade ist. Daher sollte die Fundamentallösung aus dem Näherungsbruch $\frac{p_3}{q_3}$ erhalten werden. Berechnen wir die Näherungsbrüche der Reihe nach mithilfe der Rekursionsformeln.

- $i=0$: Wenn $a_0=2$, $\frac{p_0}{q_0} = \frac{2}{1}$
- $i=1$: Wenn $a_1=1$, $p_1 = 1 \times 2 + 1 = 3$, $q_1 = 1 \times 1 + 0 = 1$. Somit $\frac{p_1}{q_1} = \frac{3}{1}$
- $i=2$: Wenn $a_2=1$, $p_2 = 1 \times 3 + 2 = 5$, $q_2 = 1 \times 1 + 1 = 2$. Somit $\frac{p_2}{q_2} = \frac{5}{2}$
- $i=3$: Wenn $a_3=1$, $p_3 = 1 \times 5 + 3 = 8$, $q_3 = 1 \times 2 + 1 = 3$. Somit $\frac{p_3}{q_3} = \frac{8}{3}$

Überprüfen wir durch Einsetzen der erhaltenen $(p_3, q_3) = (8, 3)$ in die Gleichung.
$8^2 - 7 \times 3^2 = 64 - 7 \times 9 = 64 - 63 = 1$.
Es erfüllt die Bedingung perfekt, sodass dies die Fundamentallösung $(x_1, y_1) = (8, 3)$ für $n = 7$ wird.

## 7. Unendliche Lösungen generieren: Ein Ansatz mit Matrizen und Rekursionen

Sobald auch nur eine Fundamentallösung $(x_1, y_1)$ gefunden ist, können alle anderen positiven ganzzahligen Lösungen $(x_k, y_k)$ aus der folgenden algebraischen Beziehung unendlich oft generiert werden.

$$ x_k + y_k \sqrt{n} = (x_1 + y_1 \sqrt{n})^k \quad \text{for} \quad k = 1, 2, 3, \dots $$

Durch Expandieren dieses Ausdrucks und Vergleichen des rationalen Teils und des irrationalen Teils (des Koeffizienten von $\sqrt{n}$) erhalten wir eine Rekursionsformel, um die nächste Lösung $(x_{k+1}, y_{k+1})$ aus der vorherigen Lösung $(x_k, y_k)$ zu berechnen. Drückt man dies im Matrixformat aus, ergibt sich eine sehr saubere Form.

$$
\begin{pmatrix} x_{k+1} \\ y_{k+1} \end{pmatrix} = \begin{pmatrix} x_1 & n y_1 \\ y_1 & x_1 \end{pmatrix} \begin{pmatrix} x_k \\ y_k \end{pmatrix}
$$

Jede $k$-te Lösung kann auch direkt mithilfe der Matrixexponentiation wie folgt berechnet werden:

$$
\begin{pmatrix} x_k \\ y_k \end{pmatrix} = \begin{pmatrix} x_1 & n y_1 \\ y_1 & x_1 \end{pmatrix}^{k-1} \begin{pmatrix} x_1 \\ y_1 \end{pmatrix}
$$

Diese Eigenschaft legt stark nahe, dass die Lösungen der Pellschen Gleichung nicht nur Zahlenfolgen sind, sondern eine algebraische Struktur (eine Gruppenstruktur) besitzen.

## 8. Die Brahmagupta-Identität und die Chakravala-Methode

In der alten indischen Mathematik spielte die **Brahmagupta-Identität** eine zentrale Rolle bei der Lösung der Pellschen Gleichung. Diese Identität nimmt die folgende Form an:

$$ (x_1^2 - ny_1^2)(x_2^2 - ny_2^2) = (x_1 x_2 + n y_1 y_2)^2 - n(x_1 y_2 + x_2 y_1)^2 $$

Das Brillante an dieser Identität ist, dass man durch Kombinieren einer Lösung $(x_1, y_1)$ für $x^2 - ny^2 = k_1$ und einer Lösung $(x_2, y_2)$ für $x^2 - ny^2 = k_2$ direkt eine neue Lösung $(X, Y)$ synthetisieren kann, so dass $X^2 - nY^2 = k_1 k_2$ gilt.

Indische Mathematiker nutzten diese mächtige Identität meisterhaft, um Lösungen mit kleinen Fehlern nacheinander zusammenzusetzen und entwickelten schließlich die **Chakravala-Methode**, um zu einer Lösung mit einem Fehler von $1$, d.h. einer Lösung der Pellschen Gleichung, zu gelangen. Dies ist eine monumentale Leistung in der menschlichen Mathematikgeschichte, die eine Effizienz aufweist, die gleich oder größer als die der Kettenbruchentwicklung ist.

## 9. Python-Implementierungsbeispiel und Erklärung

Da wir den theoretischen Hintergrund nun vollständig verstanden haben, wollen wir tatsächlich ein Programm schreiben. Das folgende Python-Skript führt die Rekursion für den Kettenbruch für ein gegebenes $n$ aus und sucht nach der Fundamentallösung der Pellschen Gleichung. Da es die Verarbeitung vollständig mit Ganzzahlarithmetik durchführt, ohne Gleitkommazahlen zu verwenden, gibt es keine Bedenken hinsichtlich des Verlusts an Genauigkeit.

```python
import math

def is_square(n):
    """
    Eine Funktion, um schnell zu bestimmen, ob eine gegebene Zahl n ein perfektes Quadrat ist.
    """
    s = math.isqrt(n)
    return s * s == n

def solve_pell(n):
    """
    Berechnet die Fundamentallösung der Pellschen Gleichung x^2 - n * y^2 = 1 mit der Kettenbruchmethode.
    Rückgabewert: Ein Tupel der Fundamentallösung (x, y). Gibt None für perfekte Quadrate zurück.
    """
    if is_square(n):
        return None  # Hat keine nicht-trivialen Lösungen für perfekte Quadrate

    # Initialisierung für Kettenbruchberechnungen
    m = 0
    d = 1
    a0 = math.isqrt(n)
    a = a0
    
    # Anfangseinstellung für Näherungsbrüche (p_{-1}=1, p_{-2}=0, q_{-1}=0, q_{-2}=1)
    num1, num2 = 1, 0  # p_{i-1}, p_{i-2}
    den1, den2 = 0, 1  # q_{i-1}, q_{i-2}
    
    # Erster Näherungsbruch (p_0, q_0)
    num = a0
    den = 1
    
    # Schleife, bis die Bedingung x^2 - n*y^2 == 1 erfüllt ist
    while num * num - n * den * den != 1:
        # Berechne das nächste Glied a_i des Kettenbruchs
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        
        # Aktualisiere Näherungsbrüche p_i, q_i
        num2 = num1
        num1 = num
        den2 = den1
        den1 = den
        
        num = a * num1 + num2
        den = a * den1 + den2

    return num, den

# Anwendungsbeispiel: Wenn n = 7
n = 7
solution = solve_pell(n)
if solution:
    x, y = solution
    print(f"Fundamentallösung für n={n}: x={x}, y={y}")
    print(f"Überprüfung: {x}^2 - {n}*{y}^2 = {x**2 - n * y**2}")
```

Wenn dieser Code ausgeführt wird, wird die Fundamentallösung $(x, y) = (8, 3)$ sofort ausgegeben, genau wie wir sie zuvor von Hand berechnet haben. Wenn Sie einen größeren Wert für $n$ ausprobieren, z.B. $61$, können Sie überprüfen, dass die Lösung zu enormen Zahlen wird ($x = 1766319049, y = 226153980$), wodurch Sie die profunde Tiefe der Pellschen Gleichung wirklich spüren können.

## 10. Brücke zur algebraischen Zahlentheorie: Beziehung zum Dirichletschen Einheitensatz

Die [Pellsche Gleichung](https://kenji.blog/de/p/pell-equation/) ist nicht bloß ein Zahlenrätsel. In der modernen Mathematik ist sie als wichtiges Tor zur Theorie der **reell-quadratischen Zahlkörper** $\mathbb{Q}(\sqrt{n})$ positioniert.

Die Lösungen der Pellschen Gleichung entsprechen eng den **Einheiten** (Elemente, deren Inverse ebenfalls algebraische ganze Zahlen sind) im Ring der algebraischen ganzen Zahlen eines reell-quadratischen Zahlkörpers. Die Fundamentallösung entspricht der **Grundeinheit** (fundamental unit), die diese Einheitengruppe erzeugt, und die Tatsache, dass unendlich viele Lösungen für die [Pellsche Gleichung](https://kenji.blog/de/p/pell-equation/) existieren, kann als Sonderfall eines fortgeschritteneren Satzes, des **Dirichletschen Einheitensatzes** (Dirichlet's unit theorem), angesehen werden. Das Verständnis der Eigenschaften der Grundeinheit ist äußerst entscheidend, um Formeln für die Klassenzahl quadratischer Körper und die Struktur von Idealklassen tiefgehend zu erforschen.

## 11. Fazit

In diesem Artikel haben wir eine der faszinierendsten diophantischen Gleichungen, die **[Pellsche Gleichung](https://kenji.blog/de/p/pell-equation/)**, von ihren Grundlagen bis zu ihren Anwendungen im Detail untersucht. Wir haben die überraschende Tatsache erklärt, dass es für jedes nicht quadratische $n$ immer unendliche nicht-triviale Lösungen gibt, einen effizienten Algorithmus zur Suche nach Lösungen mittels Kettenbruchentwicklungen sowie die Dynamik der Synthese neuer Lösungen nacheinander aus der generierten Fundamentallösung unter Verwendung von Matrizen.

Die Tatsache, dass klassische Probleme, die von [Fermat](https://kenji.blog/de/p/fermat/) und Brahmagupta vor Hunderten von Jahren betrachtet wurden, auf wunderbare Weise als moderne Computeralgorithmen implementiert werden können und darüber hinaus eine Verbindung zur fortgeschrittenen algebraischen Zahlentheorie herstellen, ruft eine tiefe und zeitlose mathematische Romantik hervor. Wir hoffen, dass Sie diese Gelegenheit nutzen werden, um mithilfe des Python-Codes die Welt der Pellschen Gleichung für verschiedene Werte von $n$ zu erkunden und die tiefgreifenden Eigenschaften von Zahlen kennenzulernen.
