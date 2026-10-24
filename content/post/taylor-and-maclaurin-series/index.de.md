---
title: "Taylor- und Maclaurin-Reihen: Die Magie der Approximation komplexer Funktionen mit Polynomen"
description: "Eine detaillierte Erklärung der Taylor- und Maclaurin-Reihen, der Geheimnisse der Infinitesimalrechnung, von intuitiven Bedeutungen über mathematische Herleitungen bis hin zu Anwendungen in Programmierung und Physik."
slug: "taylor-and-maclaurin-series"
date: "2026-09-20T14:30:00+09:00"
lastmod: 2026-10-24
image: "eyecatch.jpg"
categories: ["mathematics"]
tags:
  - "Infinitesimalrechnung"
  - "Taylorreihe"
  - "Maclaurin-Reihe"
  - "Funktionsapproximation"
---

## Einführung

Ein **Taylorpolynom** nähert eine Funktion in der Umgebung eines Punktes an, indem es dort mit ihrem Wert und endlich vielen Ableitungen übereinstimmt. Die aus diesen Koeffizienten gebildete unendliche Summe heißt **Taylorreihe**; liegt der Entwicklungspunkt bei null, spricht man von einer **Maclaurin-Reihe**. Ob die Reihe konvergiert und ob ihre Summe mit der ursprünglichen Funktion übereinstimmt, muss getrennt geprüft werden.

Anhand der Exponentialfunktion und trigonometrischer Funktionen erklären wir die Bestimmung der Koeffizienten, die Voraussetzungen für die Gleichheiten und die Abschätzung des Fehlers beim Abbrechen der Reihe. Ein Python-Beispiel veranschaulicht anschließend die Näherung von $\sin x$ nahe null.

## Warum Funktionen mit Polynomen approximieren?

Warum ist es überhaupt notwendig, eine Funktion als Polynom ( $a + bx + cx^2 + \dots$ ) darzustellen?

```mermaid
flowchart LR
    A["Nahe dem Entwicklungspunkt analytische Funktion"] -->|"Taylorentwicklung im Konvergenzbereich"| B["Potenzreihe"]
    B -->|"Abbruch bei endlichen Termen"| C["Polynom-Approximation"]
    C -->|"Nur Grundrechenarten"| D["Hochgeschwindigkeits-Computerberechnung"]
```

Die Annäherung einer nichtlinearen Funktion durch ein Polynom kann Auswertung, Differentiation und Integration vereinfachen. Sobald die Koeffizienten feststehen, lässt sich das Polynom durch Addition und Multiplikation auswerten. Restglied und numerische Fehler bestimmen, in welchem Bereich die Näherung brauchbar und wie genau sie ist.

## Intuitives Verständnis der Maclaurin-Reihe

Betrachten wir zunächst die **Maclaurin-Entwicklung**, die eine Funktion nahe $x=0$ annähert.
Die Funktion $f$ besitze nahe null die benötigten Ableitungen. Wir wählen einen endlichen Grad $n$ und bestimmen die Koeffizienten des folgenden Polynoms $P_n$:

$$ P_n(x) = c_0 + c_1 x + c_2 x^2 + \dots + c_n x^n $$

Die Koeffizienten werden so gewählt, dass Funktionswert und Ableitungen bei null übereinstimmen. Die folgende Bedingung an die zweite Ableitung gilt für $n\ge2$.

1. **Bedingung an den Funktionswert**: Aus $P_n(0)=f(0)$ folgt $c_0=f(0)$. Der konstante Term gleicht den Funktionswert bei null an.
2. **Bedingung an die erste Ableitung**: Aus $P_n'(0)=f'(0)$ folgt $c_1=f'(0)$. Das Polynom $P_1(x)=f(0)+f'(0)x$ ist die Tangentennäherung bei null.
3. **Bedingung an die zweite Ableitung**: Wir verlangen $P_n''(0)=f''(0)$. Wegen $P_n''(0)=2c_2$ erhalten wir $c_2=f''(0)/2!$. Bei zusätzlichen Termen höheren Grades ist die gesamte Ableitung $P_n''(x)$ im Allgemeinen nicht die Konstante $2c_2$.
4. **Allgemeine Bedingung**: Für $k\le n$ bestimmt $P_n^{(k)}(0)=f^{(k)}(0)$ den Koeffizienten $c_k=f^{(k)}(0)/k!$. Das weiter unten behandelte Restglied schätzt den Fehler nahe dem Entwicklungspunkt ab.

## Formel und Herleitung der Maclaurin-Reihe

Ist $f$ unendlich oft differenzierbar, definieren diese Koeffizienten ihre Maclaurin-Reihe. Um wie im Folgenden eine Gleichheit mit $f(x)$ zu schreiben, muss die Reihe am betrachteten Punkt jedoch gegen $f(x)$ konvergieren. Das gilt in einer geeigneten Umgebung von null, wenn $f$ dort analytisch ist. Unendlich häufige Differenzierbarkeit allein reicht nicht aus.

$$ f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f^{(3)}(0)}{3!}x^3 + \dots $$

Mit der Sigma-Notation geschrieben sieht das so aus:

$$ f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!} x^n $$

Hierbei ist $f^{(n)}(0)$ der Wert, den man erhält, indem man die Funktion $f(x)$ $n$-mal ableitet und $x=0$ einsetzt, und $n!$ stellt die Fakultät von $n$ dar ( $n \times (n-1) \times \dots \times 1$ ).

## Maclaurin-Reihe typischer Funktionen

Die folgenden Reihen der Exponentialfunktion sowie von Sinus und Kosinus konvergieren für jedes reelle $x$ gegen die jeweilige Funktion. Die trigonometrischen Argumente werden im Bogenmaß angegeben.

### 1. Exponentialfunktion $e^x$

Die Exponentialfunktion $f(x)=e^x$ bleibt nach beliebig vielen Ableitungen $e^x$. Daher haben alle ihre Ableitungen bei null den Wert $1$ ($f^{(n)}(0)=1$).

$$ e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots = \sum_{n=0}^{\infty} \frac{x^n}{n!} $$

### 2. Trigonometrische Funktionen $\sin x$ und $\cos x$

Die aufeinanderfolgenden Ableitungen von $\sin x$ durchlaufen den Zyklus $\cos x, -\sin x, -\cos x, \sin x, \dots$. Bei $x=0$ sind nur die Ableitungen ungerader Ordnung ungleich null; die gerader Ordnung haben den Wert $0$.

$$ \sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} x^{2n+1} $$

Ebenso bleiben für $\cos x$ nur die Terme gerader Ordnungen übrig.

$$ \cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \dots = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n)!} x^{2n} $$

## Erweiterung zur Taylorreihe

Verschiebt man den Entwicklungspunkt von null nach $a$, erhält man die Taylorreihe. Ist $f$ nahe $a$ analytisch, gilt die folgende Gleichheit dort, wo die Reihe die ursprüngliche Funktion darstellt. Näherungen, die nur endlich viele Ableitungen voraussetzen, behandelt man mit einem endlichen Taylorpolynom und seinem Restglied, wie weiter unten beschrieben.

$$ f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \dots = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x-a)^n $$

Diese Formel zeigt ihre Stärke, wenn Sie den Wert einer Funktion an einem Ort vorhersagen möchten, der leicht von $x=a$ ( $x = a + \Delta x$ ) abweicht.

## Anwendungen der Taylorreihen

### Lineare Approximation in der Physik

In der Physik werden lineare Näherungen durch Taylorpolynome häufig verwendet. Beim Pendel messen wir den Winkel $\theta$ im Bogenmaß und setzen $|\theta|\ll1$ voraus. Dann verwenden wir die Näherung ersten Grades des Sinus:

$$ \sin \theta \approx \theta \quad (\text{wenn } \theta \text{ ausreichend klein ist}) $$

Diese Näherung linearisiert die Pendelgleichung und liefert innerhalb der Näherung für kleine Amplituden eine von der Amplitude unabhängige Periode. Die tatsächliche Periode eines einfachen Pendels hängt von der Amplitude ab; für große Schwingungen ist dieselbe Näherung nicht anwendbar.

### Programmierung und Numerische Berechnung

Zur numerischen Auswertung von Funktionen werden verschiedene Verfahren eingesetzt, darunter Polynomnäherungen. Das Modul `math` von CPython ruft hauptsächlich die C-Mathematikbibliothek der Plattform auf; die konkreten Algorithmen hängen von dieser Implementierung ab. Das folgende Lernbeispiel summiert wenige Terme nahe null, etwa für $|x|\le1$, und bildet nicht die interne Implementierung der Standardbibliothek nach.

```python
import math

def approx_sin(x, terms=10):
    """
    Lernbeispiel: endliche Maclaurin-Summe für sin(x) nahe null
    x: Winkel im Bogenmaß
    terms: Anzahl der summierten Terme (positive ganze Zahl; hier 10)
    """
    result = 0.0
    for n in range(terms):
        # Berechne jeden Term: (-1)^n * x^(2n+1) / (2n+1)!
        sign = (-1) ** n
        numerator = x ** (2 * n + 1)
        denominator = math.factorial(2 * n + 1)
        result += sign * (numerator / denominator)
    return result

# Test: x = 1.0 Bogenmaß (ca. 57.3 Grad)
x_val = 1.0
print(f"Näherungswert: {approx_sin(x_val)}")
print(f"Wert von math.sin (zum Vergleich): {math.sin(x_val)}")
```

## Konvergenzradius und Satz von Taylor

Der **Konvergenzradius** $R$ ist eine Zahl, die den Abstand vom Entwicklungspunkt $a$ angibt, innerhalb dessen eine Potenzreihe konvergiert, also $|x-a|<R$; er ist nicht die Bezeichnung des Intervalls selbst. Auch $R=0$ und $R=\infty$ sind möglich. Randpunkte mit $|x-a|=R$ müssen gesondert untersucht werden. Beispielsweise hat die Maclaurin-Reihe von $\ln(1+x)$ den Radius 1 und stimmt für reelle $-1<x\le1$ mit der Funktion überein. Bei $x=1$ konvergiert sie bedingt, bei $x=-1$ divergiert sie.

Für eine endliche Näherung sei $f$ auf dem Intervall zwischen $a$ und $x$ von der Klasse $C^{n+1}$. Der Satz von Taylor liefert dann:

$$
f(x)=P_{n,a}(x)+R_n(x),\qquad P_{n,a}(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k
$$

$$
R_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}
$$

Dabei liegt $\xi$ zwischen $a$ und $x$. Gilt auf dem Intervall $|f^{(n+1)}|\le M$, so ist $|R_n(x)|\le M|x-a|^{n+1}/(n+1)!$. Um die Gleichheit einer Funktion mit ihrer unendlichen Taylorreihe nachzuweisen, kann man zeigen, dass dieses Restglied für $n\to\infty$ gegen null geht.

Der obige Code summiert 10 Terme, also bis $x^{19}$. Da der Koeffizient des Sinus vom Grad 20 null ist, beschränkt der Satz von Taylor den Abbruchfehler bei $x=1$ durch $1/21!$, ungefähr $1.96\times10^{-20}$. Diese Schranke gilt für die exakt über den reellen Zahlen berechnete endliche Summe; die Rundungsfehler der Gleitkommarechnung in Python sind davon zu unterscheiden. Auch die Ausgabe von `math.sin` ist ein Gleitkommawert zum Vergleich und nicht der exakte mathematische Wert.

### Eine glatte Funktion, die nicht durch ihre Taylorreihe dargestellt wird

$$
g(x)=\begin{cases}e^{-1/x},&x>0,\\0,&x\le0.\end{cases}
$$

Diese Funktion ist unendlich oft differenzierbar, und alle ihre Ableitungen bei null sind null. Ihre Taylorreihe bei null ist daher identisch null und konvergiert für jedes $x$. Für $x>0$ gilt jedoch $g(x)>0$, sodass die Summe der Reihe nicht mit der ursprünglichen Funktion übereinstimmt. Das Beispiel unterscheidet die Konvergenz einer Reihe von der Gleichheit ihrer Summe mit der Funktion.

## Fazit

Taylorpolynome liefern lokale Näherungen, und Restglieder schätzen deren Fehler ab. Wird eine Taylorreihe als Gleichheit verwendet, müssen ihr Konvergenzbereich und die Übereinstimmung ihrer Summe mit der ursprünglichen Funktion geprüft werden. Diese Unterscheidungen helfen, Genauigkeit und Anwendungsbereich von Näherungen in Physik und numerischer Berechnung zu beurteilen.

## Quellen

- [NIST DLMF §1.4(vi): Satz von Taylor und Restglieder für eine reelle Variable](https://dlmf.nist.gov/1.4#vi)
- [MIT 18.100A: Basic Analysis §§4.3 und 5.4 (Analytizität, Glattheit, Logarithmusreihe und nichtanalytisches Beispiel)](https://ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/mit18_100af20_basic_analysis.pdf)
- [MIT 16.07 Lecture 24: Pendelnäherung für kleine Amplituden und Amplitudenabhängigkeit](https://ocw.mit.edu/courses/16-07-dynamics-fall-2009/c0c881f96f4ff4e21f082c88e8b015d6_MIT16_07F09_Lec24.pdf)
- [Python 3.12 math: Mathematische Funktionen und Implementierungsdetails von CPython](https://docs.python.org/3.12/library/math.html)
