---
title: 'Conjecture de Collatz'
slug: "コラッツ予想"
date: 2025-07-15T18:03:03+09:00
tags: ["Conjecture de Collatz", "Mathématiques", "Programmation", "Algorithme"]
draft: false
image: "img.webp"
categories: ["Mathématiques, Cryptographie et Quantique"]
---

# Est-il vrai que « n'importe quel nombre finit par devenir 1 » ? ── J'ai joué avec la conjecture de Collatz

Bonjour ! C'est kenji.

Soudainement, si on vous parle d'une « règle où n'importe quel nombre finit par devenir 1 »,
ne trouvez-vous pas cela un peu étrange ?

> Par exemple, même 19, 87 ou 1 000 000.
> Si vous manipulez les nombres en suivant une règle simple, pour une raison quelconque, cela converge finalement vers « 1 ».

Cette histoire qui ressemble à un rêve, c'est la **conjecture de Collatz (Collatz Conjecture)**.

---

## D'abord, qu'est-ce que la conjecture de Collatz ?

Commençons par présenter les règles.

* Départ : Choisissez un **entier positif** arbitraire
* Opération :

    * S'il est pair → le diviser par deux (n → n / 2)
    * S'il est impair → le multiplier par 3 et ajouter 1 (n → 3n + 1)

Si vous répétez cela encore et encore, c'est la conjecture selon laquelle **n'importe quel nombre atteindra finalement 1**.

Par exemple, si on commence par `6` :

```
6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
```

Il est bien devenu « 1 ». Bon retour !

---

## Essayons avec du code : Collatz en Python

Eh bien, dans ces cas-là, le plus rapide est d'essayer avec du code !
Affichons une « suite de Collatz » en Python.

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

Lorsqu'on l'exécute :

```
[19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
```

Il atteint magnifiquement 1.
Il fait pas mal de détours, mais à la fin, il atteint bien la ligne d'arrivée !


D'ailleurs, même si on commence par **27**, il atteindra 1 de la même manière.

```
print(collatz(27))
```

Lorsqu'on l'exécute

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

Incroyable, cela prend 111 étapes !

De plus, il y a des moments où il gonfle jusqu'à plus de 9000 en cours de route.
C'est un modèle où il fait énormément de détours avant d'atteindre l'objectif.

---

## Alors, qu'est-ce qui est si incroyable finalement ?

Ce qui est incroyable avec cette conjecture, c'est que

> **Bien que ce ne soit pas prouvé, on dirait que n'importe quel nombre finira par devenir 1**

Voilà ce qui est fou.

Hein ? Et pour 1 billion, ou 10 billiards... ?

Si vous avez pensé à ça, vous êtes perspicace.
En fait, des ordinateurs ont été utilisés pour vérifier jusqu'à environ « 2 à la puissance 68 »,
et **ils atteignent tous 1**. C'est incroyable...

Cependant, **il n'a pas été théoriquement prouvé que « cela se passera toujours ainsi »**.
C'est ce qu'on appelle un « problème non résolu » dans le monde des mathématiques.

---

## Pourquoi devient-il « 1 » ? Approche probabiliste (contexte mathématique)

Le fait que n'importe quel nombre devienne finalement 1 semble magique, mais d'un **point de vue probabiliste**, il existe une raison logique de se dire « eh bien, c'est assez logique que cela se passe ainsi ».

Si vous appliquez `3n + 1` à un nombre impair $n$, la réponse sera toujours un **nombre pair**.
Par conséquent, à l'étape suivante, il sera certainement divisé par 2, devenant effectivement $\frac{3n + 1}{2} \approx 1.5n$.

Ensuite, la probabilité que ce nombre soit à nouveau pair est de $\frac{1}{2}$.
S'il est pair, il sera encore divisé par 2 pour devenir $0.75n$, ce qui est plus petit que le nombre d'origine.

Bien que ce ne soit pas mathématiquement rigoureux, il est connu que si vous prenez la moyenne géométrique du « multiplicateur » lors du saut d'un nombre impair au nombre impair suivant, il est d'**environ $\frac{3}{4}$ fois** (modèle probabiliste heuristique).
En d'autres termes, **la valeur a tendance à diminuer en moyenne**, et est donc finalement aspirée vers le bas pour atteindre 1.

## Que se passe-t-il si on modifie un peu les règles ? (Comparaison avec d'autres conjectures)

Vous avez sans doute envie de vous dire : « Et si on multipliait par 5 au lieu de 3 ? »
En fait, cela est connu sous le nom de **problème $5n + 1$**, et dans ce cas, tous les nombres ne convergent pas vers 1.

Dans le cas de $5n + 1$, il a été confirmé qu'il existe plusieurs boucles (cycles) différentes, et il a également été souligné qu'il pourrait exister des nombres qui continuent de croître à l'infini (divergence).
De plus, dans le cas du **problème $3n - 1$**, en plus de la boucle « $1 \to 2 \to 1$ », il existe une autre boucle comme « $5 \to 14 \to 7 \to 20 \to 10 \to 5$ ».

On peut voir à quel point la propriété de la conjecture de Collatz selon laquelle « tout converge vers 1 (la boucle $4 \to 2 \to 1$) » repose sur un équilibre très délicat.

---

## Le point d'arrivée de l'humanité ① : Les limites de la force brute par ordinateur

Actuellement, les mathématiciens et les passionnés d'informatique du monde entier utilisent le calcul distribué (des projets qui combinent la puissance de calcul des PC du monde entier) et les GPU pour calculer sans relâche la conjecture de Collatz.

En 2020, il a été confirmé par ordinateur que la conjecture de Collatz est correcte (qu'elle atteint finalement 1) pour toutes les valeurs initiales allant jusqu'à un incroyable **$2^{68}$ (environ 295 millions de milliards)**.

Cependant, dans le monde des mathématiques, on ne peut pas dire « on a vérifié jusqu'à 295 millions de milliards, donc ce doit être tout à fait correct ». Dans l'océan infini des nombres, même $2^{68}$ n'est qu'une « première goutte ».

---

## Le point d'arrivée de l'humanité ② : Indécidabilité et la percée de Terence Tao

À la question « Pourquoi personne ne peut-il le prouver ? », le brillant mathématicien britannique John Conway a prouvé en 1972 qu'un problème légèrement étendu de la conjecture de Collatz est **« indécidable (Turing complete) »**.
C'est un fait terrifiant qui touche aux fondements de l'informatique : selon les règles, « il n'existe en principe aucun algorithme permettant de déterminer si l'on atteindra 1 ou non ». La conjecture de Collatz elle-même pourrait même être une proposition indémontrable dans le cadre des mathématiques modernes.

Cependant, en 2019, une percée majeure a enfin eu lieu.
L'un des plus grands mathématiciens de notre époque, **Terence Tao**, a prouvé, en utilisant des équations aux dérivées partielles et la théorie des probabilités, que « (bien que l'on ne puisse pas dire que ce soit strictement vrai pour tous) **pour presque toutes les valeurs initiales, la suite de Collatz atteint finalement une valeur beaucoup plus petite que le nombre d'origine** ».

Bien que ce ne soit pas une preuve complète que « tout devient 1 », cela a stupéfié le monde mathématique comme **le point d'arrivée historique où l'humanité s'est le plus rapprochée de la vérité de la conjecture de Collatz**.

---

## Qui est M. Collatz ?

Et là, en lisant jusqu'ici, vous vous demandez peut-être : « D'ailleurs, qui est Collatz ? »
Je vais vous le présenter proprement !

* Nom : **Lothar Collatz**
* Nationalité : Allemande
* Années de vie : 1910-1990
* Titre : Mathématicien (actif dans les domaines de l'analyse fonctionnelle et de la théorie des nombres)

Il a proposé cette conjecture en 1937, et
depuis, pendant plus de 80 ans, **personne n'a pu la prouver ou la réfuter**.

À propos, ce problème est tellement simple et pourtant si profond que
même Paul Erdős (un mathématicien super célèbre) aurait dit ceci :

> « Les mathématiques ne sont pas encore prêtes pour aborder Collatz. »

En d'autres termes, c'est la théorie selon laquelle les mathématiques de l'humanité n'ont pas encore rattrapé ce mystère...

---

## Pas besoin de « formules mathématiques compliquées »

Ce qui est bien avec la conjecture de Collatz, c'est que **tout le monde peut jouer avec**.

Si vous avez du papier et un stylo, vous pouvez le faire.
Si vous écrivez du code en Python, vous pouvez le tester automatiquement.
Et pourtant, **les mathématiciens de pointe s'y attaquent sérieusement**.

C'est plutôt excitant, non ?

---

## En bonus : Code pour tester tout d'un coup

Je vais également vous donner un code pour tester plein de nombres en une seule fois.

```python
for n in range(1, 21):
    steps = collatz(n)
    print(f"{n}: {steps} (Nombre d'étapes : {len(steps)-1})")
```

Cela génère les suites de Collatz de « 1 à 20 » d'un seul coup.

---

## Conclusion : Ce monde est quand même bien mystérieux

Voilà, c'était la conjecture de Collatz.

* C'est super simple mais
* Personne n'arrive à la prouver
* C'est un énorme problème dans le monde mathématique

C'était une entité qui ressemble à un concentré de mystère.

Même les débutants en programmation peuvent essayer, alors n'hésitez pas à jouer avec !

---

## Liens recommandés (pour les personnes intéressées)

* [Wikipédia : Conjecture de Syracuse (Collatz)](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse)
* [Article de Terence Tao (en anglais)](https://arxiv.org/abs/1909.03562)
* Créer une version visualisée en Python est aussi très amusant ! (Je le ferai si on me le demande)

---

Si vous voulez en savoir plus sur ce genre de sujet « mathématiques mystérieuses × programmation »,
n'hésitez pas à me demander « dis-m'en plus ».
Plus tard, je vous présenterai l'hypothèse de Riemann, des histoires de nombres premiers et bien d'autres choses encore !

---

📮 Fin !

---
