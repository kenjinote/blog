---
title: 'Einfacher C-Code zur Generierung und Bestimmung von Primzahlen innerhalb eines bestimmten Bereichs'
slug: "Primzahlを生成するC言語コード"
tags: ["C", "Primzahlen", "Algorithmus", "Mathematik"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "Primzahlen mit Probedivision in C17 auflisten: Eingabeprüfung mit fgets und strtol, Vermeidung von Ganzzahlüberläufen, Beispiele und Einsatzgrenzen."
date: 2024-08-24T09:38:10+09:00
lastmod: 2026-10-28
---

Dieses C17-Programm prüft Zahlen durch Probedivision und listet die Primzahlen von 1 bis zu einer oberen Grenze `n` einschließlich auf. Eine Primzahl ist eine ganze Zahl ab 2; bei einer Grenze von 0 oder 1 werden daher keine Primzahlen ausgegeben. Geben Sie genau eine ganze Dezimalzahl zwischen 0 und `INT_MAX` ein.

## Code

```c
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <errno.h>
#include <limits.h>
#include <ctype.h>
#include <string.h>

bool isPrime(int num) {
    if (num <= 1) return false;
    if (num <= 3) return true;
    if (num % 2 == 0 || num % 3 == 0) return false;

    for (int i = 5; i <= num / i; i += 6) {
        if (num % i == 0 || num % (i + 2) == 0) return false;
    }
    return true;
}

void printPrimes(int n) {
    if (n < 2) {
        putchar('\n');
        return;
    }
    printf("2");
    for (int i = 3; i <= n; ) {
        if (isPrime(i)) printf(" %d", i);
        if (i > n - 2) break;
        i += 2;
    }
    putchar('\n');
}

bool readLimit(int *n) {
    char line[128];
    if (fgets(line, sizeof line, stdin) == NULL) return false;
    if (strchr(line, '\n') == NULL) {
        int next = getchar();
        if (next != '\n' && next != EOF) return false;
        if (ferror(stdin)) return false;
    }

    errno = 0;
    char *end;
    long value = strtol(line, &end, 10);
    if (end == line || errno == ERANGE || value < 0 || value > INT_MAX)
        return false;
    while (isspace((unsigned char)*end)) ++end;
    if (*end != '\0') return false;
    *n = (int)value;
    return true;
}

int main(void) {
    int n;
    printf("Obere Grenze eingeben (0 bis %d): ", INT_MAX);
    fflush(stdout);
    if (!readLimit(&n)) {
        fprintf(stderr, "Ungültige Eingabe. Eine ganze Zahl von 0 bis %d eingeben.\n", INT_MAX);
        return EXIT_FAILURE;
    }
    printf("Primzahlen von 1 bis %d:\n", n);
    printPrimes(n);
    return EXIT_SUCCESS;
}
```

## Kompilieren und Ausführungsbeispiel

Speichern Sie das Programm als `primes.c`. Führen Sie in einer Umgebung mit GCC zunächst `gcc -std=c17 -Wall -Wextra -O2 primes.c -o primes` und dann `./primes` aus. Bei der Eingabe `30` erscheint nach einer Überschrift diese Zeile:

```text
2 3 5 7 11 13 17 19 23 29
```

Die Grenze 2 ergibt `2`; 0 oder 1 ergibt eine leere Zeile. Eingelesen wird eine Textzeile mit höchstens 127 Bytes ohne das Zeilenumbruchzeichen. Leerraum am Anfang und Ende sowie ein führendes `+` sind erlaubt. Negative Werte, leere Zeilen, Text ohne gültige ganze Zahl, Werte außerhalb des Bereichs, zu lange Zeilen und Lesefehler führen zu einer Fehlermeldung und beenden das Programm. Nur die erste Zeile wird verarbeitet; weitere Zeilen werden nicht verwendet.

## Funktionsweise von Test und Eingabeverarbeitung

1. `isPrime` liefert für Werte bis einschließlich 1 falsch und für 2 und 3 wahr. Für andere Vielfache von 2 oder 3 liefert die Funktion falsch. Danach prüft sie `i` und `i + 2` für `i = 5, 11, 17, ...`. Die möglichen Teiler haben die Form `6k - 1` oder `6k + 1`; sie sind keine Vielfachen von 6. Auch ist nicht jede Zahl dieser Formen eine Primzahl.
2. Jede zusammengesetzte Zahl hat einen Primteiler, der höchstens ihrer Quadratwurzel entspricht. Daher genügt die Prüfung, solange `i <= num / i` gilt. Bei positiven ganzen Zahlen erfasst dies denselben Bereich wie `i * i <= num`, vermeidet aber einen Überlauf der Multiplikation im Typ `int`. Eine Quadratwurzelberechnung mit Gleitkommazahlen ist nicht nötig.
3. `printPrimes` gibt bei einer Grenze unter 2 nur eine leere Zeile aus. Andernfalls gibt die Funktion zuerst 2 aus und prüft dann ungerade Kandidaten. Wenn `i > n - 2` gilt, endet die Schleife vor der Addition. So läuft auch bei der Grenze `INT_MAX` das letzte `i += 2` nicht über.
4. `readLimit` liest mit `fgets`, prüft den Zeiger auf das Konvertierungsende und `ERANGE` von `strtol` sowie den Bereich von 0 bis `INT_MAX`. Erst danach wird in `int` umgewandelt. Das Argument von `isspace` wird zuvor in `unsigned char` umgewandelt. Wer den Rückgabewert von `scanf("%d", &n)` ignoriert, riskiert nach fehlgeschlagener Eingabe die Verwendung eines nicht initialisierten `n`. Man darf ebenfalls nicht voraussetzen, dass ein Konvertierungsergebnis außerhalb des `int`-Bereichs lediglich zu einem gewöhnlichen Konvertierungsfehler führt.

## Einsatzbereich

`INT_MAX` hängt von der Implementierung ab. Bei einem 32-Bit-`int` beträgt der Wert 2,147,483,647; C schreibt ihn jedoch nicht für alle Implementierungen vor. Dass sich eine Grenze darstellen lässt, bedeutet nicht, dass sich alle Primzahlen bis dorthin schnell ausgeben lassen.

Diese Implementierung dient zum Lernen der Probedivision. Für eine einzelne Zahl ist die Anzahl der Divisionen nach oben durch einen zur Quadratwurzel proportionalen Wert beschränkt. Für die Auflistung aller Kandidaten ergibt sich als grobe obere Schranke `O(n sqrt(n))` Divisionen. Dabei zählt eine Division als eine Operation; gemeint sind weder Bitkomplexität noch gemessene Laufzeit. Für große Intervalle bietet sich das Sieb des Eratosthenes an. Dies ist kein kryptografischer Primzahlgenerator. Zum Testen großer ganzer Zahlen siehe den [Artikel zu Miller–Rabin](https://kenji.blog/de/p/cpp-fast-prime-testing-miller-rabin/).

Die Regeln zu Eingabefunktionen und Ganzzahlarithmetik stehen in den Abschnitten 6.5, 7.4, 7.21.6.2, 7.21.7.2 und 7.22.1.4 des [C11-Komiteeentwurfs N1570 von WG14](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf).
