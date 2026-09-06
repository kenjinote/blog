---
title: "Connaissances de Base sur les Ordinateurs"
slug: "コンピュータの基本知識"
date: 2024-09-19T01:10:20+09:00
tags: ["Ordinateur", "Connaissances de base"]
draft: false
image: "img.png"
categories: ["Informatique et Technologie"]
---

# Connaissances de Base sur les Ordinateurs

Cette page explique ce qu'est un ordinateur.

## Définition d'un ordinateur
Un ordinateur est une machine composée des 5 unités suivantes :

1. Périphérique d'entrée
2. Périphérique de sortie
3. Périphérique de stockage
4. Unité de contrôle
5. Unité arithmétique et logique

En gros, un ordinateur est une machine qui effectue un `traitement` spécifique pour une `entrée` donnée et `produit` le résultat.
Il peut `stocker` les données saisies, effectuer des `opérations` et `produire` des sorties. Le `contrôle` a pour rôle de contrôler les 4 unités mentionnées ci-dessus.

## Ce qui est nécessaire pour faire fonctionner un ordinateur
Pour faire fonctionner un ordinateur, des programmes (logiciels) sont nécessaires en plus des dispositifs (matériel).

Dans un programme, nous indiquons à l'ordinateur le type de traitement à effectuer. Les programmes sont écrits dans un format que l'ordinateur peut comprendre.

Un exemple de programme est présenté ci-dessous :
Un programme qui calcule la somme de 1 à un entier saisi.
```
#include <iostream>
using namespace std;

int main() {
    // Allocation de l'espace mémoire nécessaire
    int n, sum = 0;
    
    // Sortie
    cout << "Veuillez entrer un entier : ";
    
    // Entrée 
    cin >> n;
    
    // Opération
    for (int i = 1; i <= n; i++) { // Opération
        sum += i;
    }
    
    // Sortie
    cout << "La somme de 1 à " << n << " est " << sum << "." << endl;
    
    // Fin
    return 0;
}
```

Le programme est converti en code machine par un compilateur, dans un format que l'ordinateur peut exécuter.
