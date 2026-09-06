---
title: "Tour de Hanoï"
slug: "tour-de-hanoi"
date: 2025-04-17T22:23:14+09:00
tags: ["Tour de Hanoï", "Algorithme", "Python"]
draft: false
image: "img.png"
categories: ["Programmation"]
---

# Tour de Hanoï

Bonjour !

Aujourd'hui, j'aimerais vous expliquer la "Tour de Hanoï", à l'aide d'un exemple de programme en Python.

---

## Qu'est-ce que la Tour de Hanoï ?

La Tour de Hanoï est un puzzle qui utilise 3 tiges et plusieurs disques. Les disques sont de tailles différentes et, au début, ils sont empilés sur une tige par ordre décroissant de taille. Les règles sont les suivantes :

1. Un seul disque peut être déplacé à la fois.
2. Un grand disque ne peut pas être placé sur un petit disque.

Ce puzzle est considéré comme un excellent matériel pédagogique pour apprendre la pensée récursive. La récursivité est une méthode de résolution d'un problème en le décomposant en problèmes plus petits du même type. Dans la Tour de Hanoï, pour déplacer n disques, nous répétons l'opération de déplacement de n-1 disques.

---

## Résolvons la Tour de Hanoï avec Python

Voici un exemple de code pour résoudre la Tour de Hanoï en Python.

```python
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)

# Exemple : Déplacer 3 disques de A vers C
hanoi(3, 'A', 'C', 'B')
```

Dans ce code, la fonction `hanoi` est appelée de manière récursive, et les étapes pour déplacer les disques sont affichées. Par exemple, dans le cas de 3 disques, on obtient le résultat suivant :

```
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
```

De cette façon, en utilisant une approche récursive, les problèmes complexes peuvent être résolus simplement.

---

## Combien de temps faut-il pour déplacer 64 disques ?

Le nombre de mouvements dans la Tour de Hanoï nécessite un minimum de 2^n - 1 fois. En d'autres termes, pour déplacer 64 disques, 2^64 - 1 mouvements, soit environ 1,84×10^19 mouvements sont nécessaires. Même si vous pouviez effectuer un mouvement par seconde, cela prendrait environ 584,9 milliards d'années. C'est environ 42 fois l'âge de l'univers (environ 13,7 milliards d'années).

Ainsi, au fur et à mesure que le nombre de disques augmente, le nombre de mouvements nécessaires augmente de manière exponentielle. Par conséquent, déplacer 64 disques dans la pratique n'est pas réaliste.

---

## Résumé

La Tour de Hanoï est un puzzle parfait pour apprendre la pensée récursive. Avec Python, vous pouvez facilement implémenter sa solution. Cependant, soyez prudent, car au fur et à mesure que le nombre de disques augmente, le nombre de mouvements nécessaires augmente considérablement.

En comprenant l'approche récursive et en essayant d'écrire du code, vous pouvez améliorer vos compétences en programmation. N'hésitez pas à relever le défi de la Tour de Hanoï.

--- 
