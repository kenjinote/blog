---
title: "FizzBuzz"
slug: "FizzBuzz"
date: 2025-04-18T00:58:11+09:00
tags: ["FizzBuzz", "Python", "Algorithmus"]
draft: false
image: "img.png"
categories: ["Programmierung"]
---

## Was genau ist eigentlich FizzBuzz?

Hallo!

Heute möchte ich über „FizzBuzz“ schreiben.

Egal, ob du denkst „Ah, das kenne ich!“, oder ob du sagst „Ich habe davon gehört, es aber nicht wirklich verstanden“, bitte bleib einen Moment bei mir. Es dauert nur wenige Minuten, es zu lesen, und vielleicht denkst du danach: „Das ergibt Sinn.“

---

### Stimmt es, dass man „als Programmierer versagt hat, wenn man FizzBuzz nicht schreiben kann“?

FizzBuzz ist kurz gesagt so etwas.

```python
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

Ja, das ist das berühmte „FizzBuzz-Problem“.

Man betrachtet nacheinander die Zahlen von 1 bis 100,  
wenn es ein Vielfaches von 3 ist, gibt man „Fizz“ aus, wenn es ein Vielfaches von 5 ist, „Buzz“,  
wenn es ein Vielfaches von beiden ist, gibt man „FizzBuzz“ aus – es ist wirklich sehr einfach.

Und dennoch wird es aus irgendeinem Grund oft als „der minimale Test für einen Programmierer“ behandelt. Es taucht in Vorstellungsgesprächen auf, und in den sozialen Medien sieht man Kommentare wie „Jemand, der nicht einmal FizzBuzz schreiben kann...“.

Aber Moment mal.

Können wir wirklich behaupten, dass „FizzBuzz nicht schreiben können = nicht programmieren können“ bedeutet?

---

### Es geht nicht um das Können, sondern darum, ob man den „Zustand“ dafür hat

Es stimmt, dass FizzBuzz das Verständnis von Syntax und grundlegendem logischem Denken erfordert. Daher ist es nachvollziehbar, dass es zur „Überprüfung der Grundlagen“ verwendet wird.

Aber hier ist der Punkt.

Wenn die Umgebung anders ist, sind auch die Ergebnisse anders.

Zum Beispiel,

- Wenn man vor einem Interviewer nervös ist, den man gerade erst kennengelernt hat
- Wenn einem plötzlich ein Whiteboard übergeben wird und man keinen Editor zur Hand hat
- Wenn einem nicht sofort einfällt: „Warte, was ist noch mal Modulo?“

...Kommt das nicht vor? Wir sind Menschen. Ich denke, das passiert.

Deshalb glaube ich, dass die Frage, „ob man sich in einen Zustand versetzen kann, in dem man FizzBuzz schreiben kann“, eigentlich viel wichtiger ist, als einfach nur „ob man FizzBuzz schreiben kann“.

---

### Die Falle des üblichen Ratschlags „Einfach üben, dann wird alles gut“

Wenn dieses Thema aufkommt, neigen die Leute oft zu dem Ratschlag: „Dann übe jeden Tag!“.

Es ist wahr, dass wiederholte Übung dazu führt, dass man es fließend schreiben kann, und das ist an sich eine gute Sache. Aber wenn wir von der Prämisse ausgehen, dass „man disqualifiziert ist, wenn man FizzBuzz nicht schreiben kann“, kann sich das leicht in bloße Angst verwandeln.

Mit anderen Worten, es neigt dazu, eine Struktur zu schaffen, in der man das Gefühl hat: „Ich habe einen Fehler gemacht = ich bin nutzlos.“

Zum Beispiel, wenn man an einem Tag verschläft, neigt man dann nicht dazu zu denken: „Ich bin faul...“? Aber es könnte einfach sein, dass der Körper in diesem Moment erschöpft war.

Bei FizzBuzz ist es genauso.

---

### Abgesehen davon ist FizzBuzz immer noch eine gute Frage

Trotzdem ist FizzBuzz nichts Schlechtes.

Vielmehr denke ich, dass es eine sehr gut durchdachte Frage ist. Die Regeln sind einfach und es lässt sich leicht erweitern. Wenn man es zum Beispiel so ändert, wird das Denken vertieft.

```python
for i in range(1, 101):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    print(output or i)
```

Dies ist ein Beispiel dafür, dass „man es auch ohne if-elif-else schreiben kann“. Das ist ziemlich smart, oder?

Mit anderen Worten, bei FizzBuzz geht es nicht nur darum, „ob man es geschafft hat“, sondern es dient auch als Einstiegspunkt, um zu sehen, „wie man es schreibt“ und „wie viel man versteht“.

---

### Zusammenfassend

Ich denke, wir sollten der Frage, ob man FizzBuzz programmieren kann oder nicht, zu viel Bedeutung beimessen.

Selbst wenn man es nicht schreiben konnte, könnte es einfach daran liegen, dass „man sich gerade nicht wohlgefühlt hat“, und oft kann man es später tun, wenn man sorgfältig darüber nachdenkt.

Keine Eile, lass uns langsam vorankommen.

Code wird von Menschen geschrieben. Weil wir Menschen sind, vergessen wir manchmal Dinge und sind nervös. Wenn wir das akzeptieren, reicht es meiner Meinung nach aus, wenn wir Stück für Stück vorankommen können.

Lass uns also auch heute wieder ganz entspannt Code schreiben.
