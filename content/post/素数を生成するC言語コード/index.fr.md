---
title: 'Code source simple en langage C pour générer et déterminer les nombres premiers dans une plage spécifiée'
slug: "Nombre premierを生成するC言語コード"
tags: ["C", "Nombres premiers", "Algorithme", "Mathématiques"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "Énumérez les nombres premiers par division d’essai en C17, avec prévention des débordements, validation de l’entrée, exemples et limites d’application."
date: 2024-08-24T09:38:10+09:00
lastmod: 2026-10-28
---

Ce programme en C17 utilise la division d’essai pour tester les nombres et énumérer les nombres premiers de 1 à une borne supérieure `n`, incluse. Un nombre premier est un entier supérieur ou égal à 2 : une borne de 0 ou de 1 ne produit donc aucun nombre premier. Saisissez un seul entier décimal compris entre 0 et `INT_MAX`.

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
    printf("Saisissez une borne supérieure (0 à %d) : ", INT_MAX);
    fflush(stdout);
    if (!readLimit(&n)) {
        fprintf(stderr, "Entrée invalide. Saisissez un entier de 0 à %d.\n", INT_MAX);
        return EXIT_FAILURE;
    }
    printf("Nombres premiers de 1 à %d :\n", n);
    printPrimes(n);
    return EXIT_SUCCESS;
}
```

## Compilation et exemple d’exécution

Enregistrez le programme dans `primes.c`. Dans un environnement disposant de GCC, exécutez `gcc -std=c17 -Wall -Wextra -O2 primes.c -o primes`, puis `./primes`. La saisie de `30` affiche un en-tête suivi de cette ligne :

```text
2 3 5 7 11 13 17 19 23 29
```

La borne 2 produit `2` ; les bornes 0 et 1 produisent une ligne vide. L’entrée est une ligne de texte limitée à 127 octets, sans compter le saut de ligne. Les caractères d’espacement en début et en fin de ligne, ainsi qu’un `+` initial, sont autorisés. Les valeurs négatives, les lignes vides, les textes qui ne représentent pas un entier, les valeurs hors plage, les lignes trop longues et les échecs de lecture provoquent une erreur et l’arrêt du programme. Seule la première ligne est traitée ; les suivantes ne sont pas utilisées.

## Fonctionnement du test et de la lecture

1. `isPrime` renvoie faux pour les valeurs inférieures ou égales à 1, et vrai pour 2 et 3. Pour les autres multiples de 2 ou de 3, elle renvoie faux. Elle teste ensuite `i` et `i + 2` pour `i = 5, 11, 17, ...`. Les diviseurs candidats sont de la forme `6k - 1` ou `6k + 1` : ce ne sont pas des multiples de 6, et tous les nombres de ces formes ne sont pas premiers.
2. Tout entier composé possède un diviseur premier inférieur ou égal à sa racine carrée. Il suffit donc de poursuivre tant que `i <= num / i`. Pour les entiers positifs, cette condition couvre le même intervalle que `i * i <= num`, tout en évitant le débordement de la multiplication en `int`. Aucun calcul de racine carrée en virgule flottante n’est nécessaire.
3. `printPrimes` n’affiche qu’une ligne vide si la borne est inférieure à 2. Sinon, elle affiche 2, puis teste les candidats impairs. Si `i > n - 2`, elle quitte la boucle avant l’addition, ce qui évite un débordement lors du dernier `i += 2`, même avec une borne égale à `INT_MAX`.
4. `readLimit` lit avec `fgets`, vérifie le pointeur de fin de conversion et `ERANGE` de `strtol`, puis contrôle que la valeur est comprise entre 0 et `INT_MAX` avant de la convertir en `int`. L’argument de `isspace` est converti en `unsigned char`. Ignorer la valeur de retour de `scanf("%d", &n)` risque de conduire à l’utilisation d’un `n` non initialisé après un échec de lecture. On ne peut pas non plus supposer qu’un résultat hors de la plage de `int` sera traité comme un simple échec de conversion.

## Domaine d’application

`INT_MAX` dépend de l’implémentation. Pour un `int` de 32 bits, sa valeur est 2,147,483,647, mais C n’impose pas cette valeur partout. Pouvoir représenter une borne ne signifie pas que l’énumération de tous les nombres premiers jusqu’à cette borne sera rapide.

Cette implémentation sert à apprendre la division d’essai. Le test d’un nombre effectue au plus un nombre de divisions proportionnel à sa racine carrée ; pour énumérer tous les candidats, une borne supérieure grossière est `O(n sqrt(n))` divisions. Une division compte ici pour une opération : ce n’est ni une complexité en bits ni un temps mesuré. Pour énumérer les nombres premiers sur un grand intervalle, envisagez le crible d’Ératosthène. Ce programme n’est pas un générateur de nombres premiers cryptographiques. Pour tester de grands entiers, consultez l’[article sur Miller–Rabin](https://kenji.blog/fr/p/cpp-fast-prime-testing-miller-rabin/).

Les règles des fonctions d’entrée et de l’arithmétique entière de C figurent aux sections 6.5, 7.4, 7.21.6.2, 7.21.7.2 et 7.22.1.4 du [projet de comité C11 N1570 du WG14](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf).
