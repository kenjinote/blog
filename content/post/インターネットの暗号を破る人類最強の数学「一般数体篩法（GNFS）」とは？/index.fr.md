---
title: 'Qu''est-ce que le "Crible du corps de nombres généralisé (GNFS)", la mathématique la plus puissante de l''humanité qui brise le chiffrement d''Internet ?'
date: 2026-09-05T02:09:08+09:00
tags: ["Mathématiques", "Cryptographie", "RSA", "GNFS"]
draft: false
image: "gnfs_two_worlds_1788542142485.jpg"
categories: ["Mathématiques・Cryptographie・Quantique"]
---

# Qu'est-ce que le « Crible du corps de nombres généralisé (GNFS) », la mathématique la plus puissante de l'humanité qui brise le chiffrement d'Internet ?

L'Internet que nous utilisons tous les jours. Les messages sur LINE, YouTube, les achats sur Amazon, toutes les communications sont protégées par le « chiffrement ».
Actuellement, le chiffrement le plus utilisé dans le monde est le « Chiffrement RSA ».

La clé de la défense du chiffrement RSA est très simple. Elle utilise la propriété mathématique selon laquelle ** « la factorisation en nombres premiers de nombres gigantesques ne peut être résolue, même par des ordinateurs » ** .
Par exemple, pour « 15 », nous savons tout de suite que c'est « 3 × 5 », mais dès que cela devient un « nombre à 270 chiffres », même si tous les superordinateurs du monde étaient combinés, cela prendrait des centaines de millions d'années à résoudre.

Cependant, les mathématiciens ne sont pas restés silencieux. Pour briser ce chiffrement impénétrable, l'humanité a créé un algorithme (procédure de calcul) presque magique appelé ** « Crible du corps de nombres généralisé (GNFS : General Number Field Sieve) » ** .

Dans cet article, sans utiliser de jargon technique, avec seulement les connaissances des ** mathématiques du collège (factorisation, expressions algébriques, plus grand commun diviseur) ** , nous vous expliquerons étape par étape comment « l'algorithme le plus puissant de l'humanité » brise le code !

---

## Chapitre 1 : Le but du déchiffrement est une « formule de 3ème »

Le plus grand coup spécial pour faire face à la gigantesque factorisation en nombres premiers. C'est cette formule apprise en classe de 3ème :

> ** $X^2 - Y^2 = (X + Y)(X - Y)$ ** 

Vous pourriez vous dire : « Sérieusement, une formule aussi basique peut briser le chiffrement ? ». Cependant, c'est la clé maîtresse qui révèle tout.

Le but ultime pour briser le chiffrement, pour un nombre gigantesque $N$, est de trouver ** « des nombres ($X$ et $Y$) dont le reste de la division de $X^2$ et $Y^2$ par $N$ est le même » ** .

### Pourquoi avoir le « même reste » brise-t-il le chiffrement ?
Supposons que deux nombres, $X^2$ et $Y^2$, aient « le même reste lorsqu'ils sont divisés par $N$ ».
Avoir le même reste signifie qu'il y a une règle selon laquelle ** la soustraction « $X^2 - Y^2$ » sera toujours parfaitement divisible par $N$ (sera un multiple de $N$) ** .

Ici, supposons que le nombre géant $N$ utilisé dans le chiffrement soit constitué de la multiplication de deux nombres premiers secrets ($p$ et $q$) ($N = p \times q$).

En factorisant $X^2 - Y^2$, nous obtenons ** $(X - Y)(X + Y)$ ** .
Le fait que ce soit un multiple de $N$ signifie que, quelque part dans cette multiplication, les nombres premiers secrets $p$ et $q$ sont cachés.

Ici, un miracle se produit.
Il y a une probabilité mathématique de ** 50 % (la moitié) ** que les deux nombres premiers $p$ et $q$ se séparent dans des pièces différentes : ** « $p$ va dans la pièce de $(X - Y)$ » et « $q$ va dans la pièce de $(X + Y)$ » ** .

Avec seulement le nombre premier $p$ étant entré dans la pièce de $(X - Y)$, calculons le ** « plus grand commun diviseur (la plus grande partie commune) » ** de $(X - Y)$ et $N$.
* Contenu de $(X - Y)$ = $p \times$ un certain nombre
* Contenu de $N$ = $p \times q$
  La seule partie commune est ** « $p$ » ** !

En d'autres termes, au moment où le plus grand commun diviseur est calculé, le nombre premier caché $p$ est révélé et le chiffrement est complètement décodé. (*Le plus grand commun diviseur peut être calculé instantanément sur un smartphone en utilisant « l'Algorithme d'Euclide »).

** 【Petite Chronique : Pourquoi le carré ? Le cube ou le double ne fonctionnent-ils pas ?】 ** 
> Avec « $2X - 2Y$ », cela devient $2(X - Y)$ et il n'y a qu'une seule pièce, vous ne pouvez donc pas séparer les nombres premiers. Avec « $X^3 - Y^3$ », la taille des pièces devient déséquilibrée et le calcul devient inutilement lourd. Pour séparer les nombres premiers en deux, le « carré » qui se divise parfaitement en deux pièces est le plus rentable.

---

## Chapitre 2 : Comment trouver X et Y ? « Le puzzle de collecte de cartes de nombres premiers »

L'objectif est clair. Cependant, même si nous cherchons aveuglément des « $X^2$ et $Y^2$ qui ont le même reste », la fin de l'univers arriverait avant de les trouver.
Alors, les mathématiciens ont imaginé une méthode géniale appelée ** « le puzzle de collecte de cartes de nombres premiers » ** .

### Étape 1 : Collecter uniquement de la poudre d'or (nombres friables) avec un tamis
Tout d'abord, préparez un nombre approprié $Z$, élevez-le au carré et calculez le reste $W$ en le divisant par $N$.
(Le monde des restes de $Z^2 = W$)

Factorisez le reste obtenu $W$ en nombres premiers. Ici, seulement lorsqu'il apparaît ** « un $W$ composé uniquement de petits nombres premiers tels que 2, 3, 5, 7, etc. » ** , gardez cette équation comme une « carte gagnante » et jetez-la si de grands nombres premiers sont mélangés.
C'est comme jeter de grosses pierres avec un tamis dans une rivière pour ne récolter que de la poudre d'or.

### Étape 2 : Le puzzle pour tout rendre « pair »
Par exemple, supposons que les 3 cartes de poudre d'or suivantes ont été collectées.
* Carte A : $Z_1^2 = 2^3 \times 3^1$
* Carte B : $Z_2^2 = 2^1 \times 5^1$
* Carte C : $Z_3^2 = 3^1 \times 5^1$

Multiplions-les toutes.
Le côté droit devient $(2^3 \times 3^1) \times (2^1 \times 5^1) \times (3^1 \times 5^1)$,
Et en organisant le tout ensemble, cela devient ** « $2^4 \times 3^2 \times 5^2$ » ** .

Étonnamment, la quantité de nombres premiers est devenue « 4, 2, 2 », ** tous étant un nombre pair ** !
Le fait qu'ils soient tous pairs signifie que si vous divisez la quantité totale par deux, ce sera « le carré de quelque chose ».
En d'autres termes, $(2^2 \times 3^1 \times 5^1)^2 = (60)^2$.

Le côté gauche est $(Z_1 \times Z_2 \times Z_3)^2$, donc finalement,
** $X = (Z_1 \times Z_2 \times Z_3)$ ** 
** $Y = 60$ ** 
La paire tant attendue de « $X^2 = Y^2$ » est complète !

Pour les ordinateurs, le puzzle consistant à calculer si la quantité de nombres premiers est « paire ou impaire (0 ou 1) » est quelque chose dans lequel ils sont très doués, donc avec cette méthode, $X$ et $Y$ peuvent être trouvés à grande vitesse.

---

## Chapitre 3 : Le mur du désespoir

Maintenant n'importe quel code peut être brisé ! ... Ou du moins le pensions-nous, mais un problème majeur survient.
Si le nombre du chiffrement $N$ compte jusqu'à « 100 chiffres », cette méthode (appelée Crible Quadratique) peut le résoudre, mais lorsque $N$ atteint « 200 ou 300 chiffres », le $W$ qui apparaît au milieu du calcul devient beaucoup trop grand.

Lorsque les nombres deviennent trop grands, les « nombres composés uniquement de petits nombres premiers (poudre d'or) » cessent purement et simplement d'apparaître. Cela devient plus difficile que de chercher des lentilles de contact dans le désert, et les cartes nécessaires pour résoudre le puzzle ne s'accumuleront plus du tout.

Ici, l'arme ultime de l'humanité, le ** « Crible du corps de nombres généralisé (GNFS) » ** , entre enfin en scène.

---

## Chapitre 4 : L'idée la plus puissante de l'humanité de créer « Deux Mondes »

L'idée géniale du GNFS est : ** « Les nombres deviennent gigantesques car nous calculons uniquement dans le monde réel. Créons donc un 'monde caché' en utilisant des polynômes (formules avec des lettres) pour diviser le poids du calcul en deux. » ** 

### La magie des formules avec des lettres
Le GNFS convertit le nombre géant $N$ en une expression littérale à l'aide d'un nombre de base $m$.
Par exemple si $N=100$, avec $m=4$, alors $100 = 4^3 + 2(4^2) + 4$.
En utilisant la lettre $x$, nous en faisons une formule (le monde caché) : ** $f(x) = x^3 + 2x^2 + x$ ** .

Ce qui est intéressant avec cette formule, c'est qu'elle a la propriété que ** « si vous remplacez $x$ par $m$ (4 dans l'exemple ci-dessus), vous pouvez toujours revenir au nombre réel $N$ » ** .

### Chercher de la poudre d'or dans 2 mondes en même temps
Le GNFS crée de nombreuses paires d'entiers aléatoires $(a, b)$ et effectue les deux calculs suivants simultanément :
1. ** Monde Réel ** : $a - b \times m$
2. ** Monde des Lettres ** : La valeur de $a - b \times x$ calculée selon les règles des polynômes

En séparant le problème en deux mondes, la taille des nombres manipulés diminue (devient plus légère) de manière spectaculaire. C'est comme fendre un rocher géant en deux pierres plus faciles à manipuler.

Ensuite, vous utilisez un crible (tamis) pour séparer et ne collecter que les paires miraculeuses $(a, b)$ où ** « à la fois dans le monde réel et dans le monde des lettres, les deux sont 'composés uniquement de petits nombres premiers (poudre d'or)' » ** . D'où le nom de « Crible du corps de nombres ».

### Le moment où le chiffrement est enfin brisé
Une fois que des dizaines de millions de « cartes de poudre d'or » sont collectées dans les deux mondes, le superordinateur utilise des calculs matriciels gigantesques pour trouver « une combinaison où le nombre de nombres premiers est entièrement pair », tout comme nous l'avons fait au Chapitre 2.

Une fois la combinaison trouvée :
* Que le nombre au carré dans le monde réel soit ** $X^2$ ** 
* Que la formule au carré créée dans le monde des lettres soit ** $Y(x)^2$ ** 

Enfin, remplacez le $x$ dans la formule littérale $Y(x)$ par $m$, en revenant au monde réel et en les rejoignant.
Alors, comme par magie mathématique, la condition où ** « les restes de $X^2$ et $Y^2$ sont les mêmes » ** est strictement remplie !

Le reste, comme au Chapitre 1, consiste simplement à calculer le plus grand commun diviseur de $X - Y$ et $N$, et le chiffrement RSA impénétrable s'effondrera, révélant les nombres premiers secrets.

---

## Conclusion : Les mathématiques ne finissent jamais

Vous pourriez penser : « Super, avec le GNFS n'importe quel chiffrement peut être brisé ! ».
Cependant, le chiffrement RSA ne s'est pas non plus avoué vaincu. Ce qui est utilisé sur l'Internet d'aujourd'hui est un nombre gigantesque et monstrueux appelé « RSA-2048 (environ 617 chiffres) ».

Bien que le GNFS soit l'algorithme le plus puissant de l'humanité, même pour résoudre 270 chiffres (RSA-270), on dit que cela prendrait des milliers ou des dizaines de milliers d'années, même en connectant des ordinateurs du monde entier. Pour l'instant, nos données LINE et bancaires sont en sécurité.

Mais que se passerait-il si ** « une magie capable de trouver instantanément $X$ et $Y$ pour n'importe quel nombre géant » ** apparaissait ?
En fait, la chose qui s'en rapproche le plus est l' ** « Ordinateur Quantique (Algorithme de Shor) » ** , actuellement en développement. En utilisant la nature ondulatoire de la mécanique quantique, il a été prouvé mathématiquement qu'il est possible d'ignorer le fastidieux puzzle de collecte de cartes et de tirer la réponse d'un seul coup.

La bataille d'intelligence sans fin entre ceux qui créent le chiffrement (la défense) et ceux qui créent des algorithmes pour le briser (l'attaque).
Savoir que la « factorisation en nombres premiers » et les « expressions littérales apprises au collège sont en fait les armes qui s'affrontent sur la ligne de front de la sécurité mondiale ne rend-il pas les cours de mathématiques un peu plus intéressants ?

La personne qui découvrira l'algorithme le plus puissant du futur, c'est peut-être vous qui lisez cet article !

--- 
*(※Cet article est une adaptation conceptuelle de l'attrait mathématique du cassage de code pour les collégiens. Le GNFS réel est rigoureusement calculé à l'aide de mathématiques universitaires avancées, telles que les groupes de classes d'idéaux des corps de nombres algébriques et les homomorphismes)*
