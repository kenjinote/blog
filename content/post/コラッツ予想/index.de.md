---
title: "コラッツ予想"
slug: "コラッツ予想"
date: 2025-07-15T18:03:03+09:00
tags: ["コラッツ予想", "数学", "プログラミング", "アルゴリズム"]
draft: false
image: "img.png"
categories: ["数学・暗号・量子"]
---

# "Stimmt es, dass jede Zahl am Ende zu 1 wird?" ── Spielen mit der Collatz-Vermutung

Hallo! Hier ist kenji.

Wenn man plötzlich hört "eine Regel, bei der jede Zahl schließlich zu 1 wird",
klingt das nicht ein bisschen seltsam?

> Zum Beispiel 19, 87 oder auch 1000000.
> Wenn man die Zahlen nach einer bestimmten Regel manipuliert, konvergieren sie aus irgendeinem Grund am Ende gegen "1".

Diese traumhafte Geschichte ist die ** Collatz-Vermutung (Collatz Conjecture) **.

---

## Was ist die Collatz-Vermutung eigentlich?

Zuerst stelle ich die Regeln vor.

* Start: Wähle eine beliebige ** positive ganze Zahl **.
* Operation:

    * Wenn sie gerade ist → halbiere sie (n → n / 2)
    * Wenn sie ungerade ist → multipliziere mit 3 und addiere 1 (n → 3n + 1)

Wenn man dies immer wieder wiederholt, ist es eine Vermutung, dass ** jede Zahl schließlich 1 erreicht **.

Zum Beispiel, beginnend mit `6`:

```
6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
```

Es wurde ordentlich "1". Willkommen zurück!

---

## Machen wir es mit Code: Collatz in Python

Nun, in solchen Zeiten ist es schneller, mit Code zu testen!
Lassen Sie uns die "Collatz-Folge" in Python ausgeben.

```python
def collatz(n):
    steps = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps.append(n)
    return steps

# Beispiel: beginnend mit 19
print(collatz(19))
```

Bei Ausführung:

```
[19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
```

Es erreicht brillant die 1.
Obwohl es viele Umwege macht, erreicht es am Ende das Ziel!


Übrigens, wenn Sie mit 29 beginnen, werden Sie auf die gleiche Weise 1 erreichen.

```python
print(collatz(29))
```

Bei Ausführung

```
[27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242,
121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350,
175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167,
502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479,
1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911,
2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732,
866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35,
106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
```

Wow, es dauert 111 Schritte!

Und es gibt auch Szenen, in denen es unterwegs auf über 9000 anschwillt.
Es ist ein Muster, bei dem man einen verrückten Umweg macht, bevor man das Ziel erreicht.

---

## Und, was ist daran so toll?

Das Tolle an dieser Vermutung ist,

> ** Obwohl es nicht bewiesen ist, scheint es, dass jede Zahl, die man versucht, zu 1 wird **

Das ist es.

Äh? Und was ist mit 1 Billion oder 10 Billiarden...?

Für diejenigen, die so dachten: sehr scharfsinnig.
Tatsächlich wurde es mit Computern bis zu etwa "2 hoch 68",
und ** alle haben 1 erreicht **. Unglaublich...

Aber ** es wurde nicht theoretisch bewiesen, dass "alle so sein werden" **.
Das ist ein sogenanntes "ungelöstes Problem" in der Welt der Mathematik.

---

## Wer ist Herr Collatz?

Wenn Sie bis hierher gelesen haben, fragen Sie sich wahrscheinlich: "Wer ist Collatz eigentlich?".
Ich werde ihn richtig vorstellen!

* Name: ** Lothar Collatz (Lothar Collatz) **
* Nationalität: Deutschland
* Geburtsjahr: 1910 bis 1990
* Titel: Mathematiker (aktiv in den Bereichen Funktionalanalysis und Zahlentheorie)

Er schlug diese Vermutung 1937 vor,
und seither, seit über 80 Jahren, ** konnte niemand sie beweisen oder widerlegen **.

Übrigens ist dieses Problem so einfach und doch so tiefgründig, dass
selbst Paul Erdős (super berühmter Mathematiker) so etwas sagte.

> "Die Mathematik ist noch nicht reif für die Collatz-Vermutung"

Mit anderen Worten, die Theorie, dass die Mathematik der Menschheit dieses Mysterium noch nicht eingeholt hat...

---

## "Schwierige mathematische Formeln" sind nicht erforderlich

Das Gute an der Collatz-Vermutung ist, dass ** jeder mitspielen kann **.

Man kann es mit Papier und Stift machen.
Wenn man den Code in Python schreibt, kann man ihn automatisch testen.
Und dennoch ** nehmen ihn Spitzenmathematiker ernst **.

Irgendwie aufregend, nicht wahr?

---

## Bonus: Code, um alles auf einmal zu testen

Ich werde auch einen Code posten, um verschiedene Zahlen gleichzeitig zu testen.

```python
for n in range(1, 21):
    steps = collatz(n)
    print(f"{n}: {steps} (Schritte: {len(steps)-1})")
```

Dadurch erhalten wir die Collatz-Folgen von "1 bis 20" auf einmal.

---

## Fazit: Diese Welt ist doch mysteriös

Das ist also die Collatz-Vermutung.

* Obwohl es super einfach ist
* Niemand kann es beweisen
* Ein großes Problem in der Welt der Mathematik

Es war eine Existenz wie eine Masse von Mysterien.

Sogar Programmieranfänger können es versuchen, also spielen Sie bitte damit!

---

## Empfohlene Links (für Interessierte)

* [Wikipedia: Collatz-Vermutung](https://ja.wikipedia.org/wiki/コラッツ予想)
* [Terence Tao Paper (Englisch)](https://arxiv.org/abs/1909.03562)
* Es macht auch Spaß, eine visualisierte Version in Python zu erstellen! (Ich werde eine machen, wenn es gewünscht wird)

---

Wenn Sie mehr über dieses Material "Mysteriöse Mathematik x Programmierung" erfahren möchten,
zögern Sie nicht, anzufragen und zu sagen: "Bring mir mehr bei".
Schließlich werde ich verschiedene Dinge wie die Riemann-Vermutung und Primzahlen vorstellen!

---

📮Ende!

---
