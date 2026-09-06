---
title: "Qu'est-ce que le paradoxe des anniversaires ?"
slug: "バースデイパラドックスとは"
date: 2024-04-02T01:20:50+09:00
tags: ["Mathématiques", "Paradoxe"]
draft: false
math: true
image: "img.png"
categories: ["Mathématiques, Cryptographie, Quantique"]
---

## Connaissez-vous le paradoxe des anniversaires ?

Je vais vous raconter une histoire un peu étrange.
À votre avis, combien de personnes faut-il réunir pour que "la probabilité d'avoir des personnes nées le même jour" soit élevée ?

Par exemple, il y a 365 jours dans une année, donc quand on vous dit que "si 23 personnes se réunissent, la probabilité que quelqu'un partage le même anniversaire est de plus de 50 %"... cela semble un peu contre-intuitif, n'est-ce pas ?

Mais c'est **réellement plus de 50 %.** 

---

## Pourquoi cela se produit-il ?

Ce phénomène s'appelle le "paradoxe des anniversaires".
Le nom contient "paradoxe", mais il y a une raison mathématique tout à fait valable.

Lorsque le nombre de personnes est "n", **la probabilité que personne ne partage le même anniversaire** est calculée par la formule suivante :

```
P(personne ne partage) = 365/365 × 364/365 × 363/365 × ... × (365 - n + 1)/365
```

En soustrayant cela de 1, on obtient "la probabilité de partager avec quelqu'un".

---

## En regardant les résultats...

| Nombre de personnes | Probabilité d'avoir la même date d'anniversaire |
| ------------------- | ----------------------------------------------- |
| 10 personnes        | Environ 11.7%                                   |
| 20 personnes        | Environ 41.1%                                   |
| 23 personnes        | **Environ 50.7% (C'est le point clé !)** |
| 30 personnes        | Environ 70.6%                                   |
| 70 personnes        | **Incroyable : environ 99.9% !** |

En d'autres termes, avec seulement **23 personnes** , il y a plus d'une chance sur deux que quelqu'un partage le même anniversaire.
Cela s'applique tout à fait à une salle de classe ou à une réunion de travail.

---

## Résumé : Le décalage entre l'intuition et les mathématiques est fascinant

Le "paradoxe des anniversaires" est un exemple intéressant où notre intuition s'écarte de la probabilité mathématique réelle.
Connaître ce genre d'anecdote peut animer vos petites discussions et vos quiz !

---

## Liens de référence

* [Paradoxe des anniversaires (Wikipedia)](https://ja.wikipedia.org/wiki/%E8%AA%95%E7%94%9F%E6%97%A5%E3%81%AE%E3%83%91%E3%83%A9%E3%83%89%E3%83%83%E3%82%AF%E3%82%B9)
