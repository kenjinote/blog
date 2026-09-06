---
title: "C-Code zur Generierung von Primzahlen"
slug: "c-code-zur-generierung-von-primzahlen"
date: 2024-08-24T09:38:10+09:00
tags: ["C", "Primzahlen", "Algorithmus", "Mathematik"]
draft: false
image: "img.png"
categories: ["Mathematik, Kryptographie und Quanten"]
---

Nachfolgend finden Sie einen einfachen C-Code, der Primzahlen innerhalb eines bestimmten Bereichs generiert. In diesem Beispiel zählen wir Primzahlen von 1 bis n auf.

```cpp
#include <stdio.h>
#include <stdbool.h>

bool isPrime(int num) {
    if (num <= 1) return false;
    if (num <= 3) return true;
    if (num % 2 == 0 || num % 3 == 0) return false;
    
    for (int i = 5; i * i <= num; i += 6) {
        if (num % i == 0 || num % (i + 2) == 0) return false;
    }
    return true;
}

void printPrimes(int n) {
    printf("2 ");
    for (int i = 3; i <= n; i += 2) {
        if (isPrime(i)) {
            printf("%d ", i);
        }
    }
    printf("\n");
}

int main() {
    int n;
    printf("Bitte geben Sie den Maximalwert des Bereichs ein, um Primzahlen zu generieren: ");
    scanf("%d", &n);
    printf("Die Primzahlen von 1 bis %d sind wie folgt:\n", n);
    printPrimes(n);
    return 0;
}
```

Dieser Code funktioniert wie folgt:

1. Funktion isPrime: Bestimmt, ob eine gegebene Zahl eine Primzahl ist. Aus Effizienzgründen wird zunächst geprüft, ob sie durch 2 und 3 teilbar ist, und dann in Vielfachen von 6 weitergeprüft.
2. Funktion printPrimes: Gibt die Primzahlen innerhalb eines bestimmten Bereichs aus. Die 2 wird zuerst ausgegeben, und dann werden nur ungerade Zahlen überprüft.
3. Funktion main: Fordert den Benutzer auf, den Maximalwert des Bereichs einzugeben, und gibt die Primzahlen innerhalb dieses Bereichs aus.

Wenn Sie diesen Code kompilieren und ausführen, werden die Primzahlen innerhalb des angegebenen Bereichs angezeigt.
