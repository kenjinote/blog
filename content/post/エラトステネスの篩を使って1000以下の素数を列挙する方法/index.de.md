---
title: "Wie man Primzahlen unter 1000 mit dem Sieb des Eratosthenes auflistet"
slug: "Wie man Primzahlen unter 1000 mit dem Sieb des Eratosthenes auflistet"
date: 2023-04-09T12:54:24+09:00
tags: ["Sieb des Eratosthenes", "Primzahlen", "Mathematik", "Rust"]
draft: false
math: true
image: "img.png"
categories: ["Mathematik, Kryptografie, Quanten"]
---

## Was ist das Sieb des Eratosthenes?

Das Sieb des Eratosthenes ist ein Algorithmus, mit dem alle Primzahlen bis zu einem bestimmten Grenzwert gefunden werden können.
Der Algorithmus ist einfach und kann durch die folgenden Schritte implementiert werden:

1. Erstellen Sie ein boolesches Array mit N Elementen und initialisieren Sie alle Elemente auf wahr (true).
2. Setzen Sie das nullte und das erste Element des Arrays auf falsch (false) (da 0 und 1 keine Primzahlen sind).
3. Wenn das 2. Element des Arrays wahr ist, geben Sie 2 als Primzahl aus.
4. Setzen Sie alle Vielfachen von 2 ab $2^2$ auf falsch (*).
5. Wenn das 3. Element des Arrays wahr ist, geben Sie 3 als Primzahl aus.
6. Setzen Sie alle Vielfachen von 3 ab $3^2$ auf falsch.
7. Wiederholen Sie den gleichen Vorgang für das 4., 5., ..., und N-te Element.

* Der Grund, warum die Elemente ab dem Quadrat des Wertes auf falsch gesetzt werden, liegt daran, dass Zahlen, die kleiner als das Quadrat sind, bereits in vorherigen Schritten verarbeitet wurden.

![](Animation_Sieb_des_Eratosthenes.gif)


## Implementierung in Rust

```
fn main() {
    let n = 1000;
    let mut is_prime = vec![true; n+1];
    is_prime[0] = false;
    is_prime[1] = false;
    for i in 2..=n {
        if is_prime[i] {
            println!("{}", i);
            let mut j = i * i;
            while j <= n {
                is_prime[j] = false;
                j += i;
            }
        }
    }
}
```

## Leicht optimierte Version

Wir können die Implementierung unter Berücksichtigung der folgenden Punkte leicht optimieren:

- Initialisieren Sie das Array mit falsch (false) statt mit wahr (true) (das ist schneller).
- Da Vielfache von 2 keine Primzahlen sind, überspringen Sie den Schritt, bei dem die Vielfachen von 2 auf falsch gesetzt werden.
- Es ist nicht notwendig, bis n zu iterieren; es reicht aus, die Primzahlen bis zur Quadratwurzel von n zu berechnen, um alle Primzahlen zu finden, die kleiner oder gleich n sind.

```
fn main() {
    let n = 1000;
    let mut is_prime = vec![false; n+1];
    is_prime[2] = true;
    for i in (3..=n).step_by(2) {
        is_prime[i] = true;
    }
    for i in 3..=((n as f64).sqrt() as usize) {
        if is_prime[i] {
            let mut j = i * i;
            while j <= n {
                is_prime[j] = false;
                j += i * 2;
            }
        }
    }
    for i in (2..=n).filter(|&x| is_prime[x]) {
        println!("{}", i);
    }
}
```

## Referenz
- [Sieb des Eratosthenes (Wikipedia)](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE%E7%AF%A9)
