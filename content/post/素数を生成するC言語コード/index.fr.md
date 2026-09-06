---
title: "Code C pour générer des nombres premiers"
slug: "code-c-pour-generer-des-nombres-premiers"
date: 2024-08-24T09:38:10+09:00
tags: ["C", "Nombres premiers", "Algorithme", "Mathématiques"]
draft: false
image: "img.png"
categories: ["Mathématiques, Cryptographie et Quantique"]
---

Voici un code C simple qui génère des nombres premiers dans une plage spécifiée. Dans cet exemple, nous énumérons les nombres premiers de 1 à n.

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
    printf("Veuillez entrer la valeur maximale de la plage pour générer des nombres premiers : ");
    scanf("%d", &n);
    printf("Les nombres premiers de 1 à %d sont les suivants :\n", n);
    printPrimes(n);
    return 0;
}
```

Ce code fonctionne de la manière suivante :

1. Fonction isPrime : Détermine si un nombre donné est premier. Par souci d'efficacité, on vérifie d'abord s'il est divisible par 2 et 3, puis on procède à la vérification par multiples de 6.
2. Fonction printPrimes : Produit les nombres premiers dans une plage spécifiée. Le 2 est affiché en premier, puis seuls les nombres impairs sont vérifiés.
3. Fonction main : Demande à l'utilisateur de saisir la valeur maximale de la plage et affiche les nombres premiers dans cette plage.

Si vous compilez et exécutez ce code, les nombres premiers dans la plage spécifiée seront affichés.
