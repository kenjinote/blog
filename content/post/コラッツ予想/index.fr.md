---
title: "コラッツ予想"
slug: "コラッツ予想"
date: 2025-07-15T18:03:03+09:00
tags: ["コラッツ予想", "数学", "プログラミング", "アルゴリズム"]
draft: false
image: "img.png"
categories: ["数学・暗号・量子"]
---

# "Est-il vrai que n'importe quel nombre finit par devenir 1 ?" ── Jouer avec la Conjecture de Collatz

Bonjour ! C'est kenji.

Soudain, si vous entendez "une règle où n'importe quel nombre devient finalement 1",
cela ne semble-t-il pas un peu étrange ?

> Par exemple, 19, 87 ou même 1000000.
> Si vous manipulez les nombres selon une règle simple, pour une raison quelconque, cela converge vers "1" à la fin.

Cette histoire de rêve est la ** Conjecture de Collatz (Collatz Conjecture) **.

---

## Après tout, qu'est-ce que la Conjecture de Collatz ?

Tout d'abord, je vais présenter les règles.

* Début : Choisissez n'importe quel ** entier positif **.
* Opération :

    * Si c'est pair → divisez par deux (n → n / 2)
    * Si c'est impair → multipliez par 3 et ajoutez 1 (n → 3n + 1)

En répétant cela encore et encore, c'est une conjecture selon laquelle ** n'importe quel nombre finira par atteindre 1 **.

Par exemple, en commençant par `6` :

```
6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
```

Il est devenu "1" proprement. Bon retour !

---

## Faisons-le avec du code : Collatz en Python

Eh bien, dans ces moments-là, il est plus rapide de tester avec du code !
Imprimons la "Séquence de Collatz" en Python.

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

# Exemple : commencer par 19
print(collatz(19))
```

Lors de l'exécution :

```
[19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
```

Il atteint 1 brillamment.
Même s'il fait beaucoup de détours, il atteint finalement son but !


Au fait, si vous commencez avec 29, vous atteindrez également 1 de la même manière.

```python
print(collatz(29))
```

Lors de l'exécution

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

Waouh, ça prend 111 étapes !

Et aussi, il y a des scènes où ça gonfle à plus de 9000 en cours de route.
C'est un modèle où l'on fait un détour fou avant d'atteindre le but.

---

## Et donc, qu'est-ce qui est si incroyable à ce sujet ?

Ce qui est incroyable avec cette conjecture, c'est que,

> ** Bien que cela n'ait pas été prouvé, il semble que n'importe quel nombre que vous essayez deviendra 1 **

C'est ça.

Hein ? Et qu'en est-il de 1 billion, ou 10 billiards... ?

Pour ceux qui pensaient cela, très perspicace.
En fait, à l'aide d'ordinateurs, cela a été confirmé jusqu'à environ "2 à la puissance 68",
et ** tous ont atteint 1 **. Incroyable...

Mais, ** il n'a pas été théoriquement prouvé que "tous seront comme ça" **.
C'est ce qu'on appelle un "problème non résolu" dans le monde des mathématiques.

---

## Qui est M. Collatz ?

Donc, en lisant jusqu'ici, vous vous demandez probablement "Qui est Collatz, après tout ?".
Je vais vous le présenter correctement !

* Nom : ** Lothar Collatz (Lothar Collatz) **
* Nationalité : Allemagne
* Année de naissance : 1910 à 1990
* Titre : Mathématicien (actif dans les domaines de l'analyse fonctionnelle et de la théorie des nombres)

Il a proposé cette conjecture en 1937,
et depuis lors, pendant plus de 80 ans, ** personne n'a été capable de la prouver ou de la réfuter **.

Au fait, ce problème est si simple mais si profond que
même Paul Erdős (mathématicien super célèbre) a dit quelque chose comme ça.

> "Les mathématiques sont encore trop immatures pour traiter la conjecture de Collatz"

En d'autres termes, la théorie selon laquelle les mathématiques de l'humanité n'ont pas encore rattrapé ce mystère...

---

## "Des formules mathématiques difficiles" ne sont pas nécessaires

La bonne chose à propos de la Conjecture de Collatz est que ** tout le monde peut jouer **.

Vous pouvez le faire avec du papier et un stylo.
Si vous écrivez le code en Python, vous pouvez le tester automatiquement.
Et pourtant, ** les meilleurs mathématiciens s'y attaquent sérieusement **.

D'une manière ou d'une autre, n'est-ce pas excitant ?

---

## Bonus : Code pour tout tester à la fois

Je vais également publier un code pour tester plusieurs nombres en même temps.

```python
for n in range(1, 21):
    steps = collatz(n)
    print(f"{n} : {steps} (Étapes : {len(steps)-1})")
```

Cela nous donnera les séquences de Collatz de "1 à 20" d'un seul coup.

---

## Conclusion : Ce monde est, après tout, mystérieux

Donc, c'est la Conjecture de Collatz.

* Même si c'est super simple
* Personne ne peut la prouver
* Un gros problème dans le monde des mathématiques

C'était une existence comme une masse de mystères.

Même les débutants en programmation peuvent l'essayer, alors n'hésitez pas à jouer avec !

---

## Liens recommandés (pour ceux qui sont intéressés)

* [Wikipedia : Conjecture de Collatz](https://ja.wikipedia.org/wiki/コラッツ予想)
* [Article de Terence Tao (Anglais)](https://arxiv.org/abs/1909.03562)
* C'est aussi amusant de créer une version visualisée en Python ! (J'en ferai une s'il y a de la demande)

---

Si vous voulez en savoir plus sur ce genre de matériel "Mathématiques mystérieuses x Programmation",
n'hésitez pas à demander et à dire "Apprenez-m'en plus".
Finalement, j'introduirai diverses choses comme l'Hypothèse de Riemann et les nombres premiers !

---

📮Fin !

---
