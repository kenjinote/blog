---
title: 'Le problème de la Belle au bois dormant : La probabilité de la pièce est-elle de 1/2 ou 1/3 ? Le casse-tête qui divise la théorie des probabilités'
slug: 'sleeping-beauty-paradox'
description: '"Maintenant que vous êtes réveillé, quelle est la probabilité que le résultat du tirage au sort soit pile ?" Malgré une configuration très simple, nous expliquons ce récent paradoxe sur lequel les mathématiciens et philosophes du monde entier, divisés en "partisans de 1/2" et "partisans de 1/3", continuent de débattre.'
date: '2026-09-10T09:00:00+09:00'
image: 'img/sleeping_beauty.jpg'
math: true
mermaid: true
categories:
  - 'Paradoxe mathématique'
  - 'Théorie des probabilités'
tags:
  - 'Paradoxe'
  - 'Probabilité conditionnelle'
  - 'Théorème de Bayes'
  - 'Philosophie'
---

## 1. Les règles d'une étrange expérience

Vous (la Belle au bois dormant) avez été choisie comme sujet d'une expérience scientifique.
L'expérience se déroule de dimanche à mercredi. Le dimanche soir, on vous fait prendre un somnifère et vous vous endormez.

Après votre endormissement, l'expérimentateur lance **une pièce de monnaie équitable** (une pièce dont la probabilité d'obtenir pile ou face est exactement de 1/2). Ensuite, selon le résultat, il vous réveillera selon le programme suivant.

**[Si le résultat du tirage au sort est "Pile"]**
- Vous serez réveillée une seule fois le lundi pour qu'on vous pose une question. Ensuite, vous serez endormie à nouveau et ne vous réveillerez plus jusqu'à la fin de l'expérience (mercredi).

**[Si le résultat du tirage au sort est "Face"]**
- Vous serez réveillée le lundi pour qu'on vous pose une question. Ensuite, on vous fera prendre un médicament spécial (un médicament qui efface la mémoire) et vous vous rendormirez.
- Vous serez réveillée une seconde fois le mardi pour qu'on vous pose la même question. Ensuite, vous serez endormie à nouveau, ce qui marquera la fin de l'expérience (mercredi).

※ En raison des effets du médicament effaçant la mémoire, à votre réveil, vous ne pourrez absolument pas vous rappeler "quel jour on est" ni "si vous avez déjà été réveillée auparavant".

```mermaid
graph TD
    Sunday["Dimanche : La Belle s'endort"] --> Toss{"Tirage au sort"}
    
    Toss -->|Pile (1/2)| Mon_Heads["Lundi : Réveil + Question<br>（Puis fin de l'expérience）"]
    Toss -->|Face (1/2)| Mon_Tails["Lundi : Réveil + Question<br>（Puis effacement de la mémoire）"]
    
    Mon_Tails --> Tue_Tails["Mardi : Réveil + Question<br>（Puis fin de l'expérience）"]
    
    style Toss fill:#ff9999,stroke:#333
    style Mon_Heads fill:#aaffaa,stroke:#333
    style Mon_Tails fill:#aaffaa,stroke:#333
    style Tue_Tails fill:#aaffaa,stroke:#333
```

Eh bien, c'est lundi (ou mardi), et vous vous êtes réveillée.
Il n'y a ni horloge ni calendrier dans la pièce, et vous ne savez pas quel jour on est.

L'expérimentateur entre alors et vous pose cette question :
**"Dans votre état d'éveil actuel, à votre avis, quelle est la probabilité que la pièce lancée soit tombée sur 'Pile' ?"**

Vous êtes une belle femme douée en mathématiques. Alors, que répondez-vous ?

---

## 2. Le choc de deux factions : 1/2 ou 1/3

Ce problème a été conçu dans les années 1990 et publié dans une revue universitaire par le philosophe Adam Elga en 2000.
La probabilité de la pièce semble évidente, mais en fait, autour de ce problème, les mathématiciens, statisticiens et philosophes du monde entier se sont scindés en deux camps : les **"partisans de 1/2 (Halfers)"** et les **"partisans de 1/3 (Thirders)"**, et ils continuent de se livrer à des débats passionnés jusqu'à aujourd'hui.

Écoutons la "logique parfaite" de chaque camp.

### Les arguments des "partisans de 1/2 (Halfers)"
> "Puisque la pièce est équitable et non truquée, la probabilité d'obtenir pile est évidemment de 1/2.
> Peu importe le nombre de fois que l'expérimentateur me réveille après que je me sois endormie ou qu'il efface ma mémoire, cela **n'affecte en rien le résultat physique de la pièce**.
> Au moment où la pièce a été lancée, la probabilité était de 1/2, et le fait que je me sois réveillée ne m'a apporté aucune nouvelle information (aucun indice pour deviner s'il s'agit de pile ou face). Par conséquent, la probabilité reste de 1/2."

Il s'agit d'une opinion tout à fait légitime qui met l'accent sur le phénomène physique objectif et la non-actualisation de l'information.

### Les arguments des "partisans de 1/3 (Thirders)"
> "Le fait même que vous soyez 'réveillée' est une information qui modifie la probabilité.
> Supposons que cette expérience soit répétée 100 fois (100 semaines).
> La pièce devrait tomber 50 fois sur 'Pile' et 50 fois sur 'Face'.
> 
> - Pendant les 50 semaines où c'est pile, vous vous réveillez une seule fois le lundi $\rightarrow$ **Le nombre de réveils avec 'Pile' est de 50 fois**
> - Pendant les 50 semaines où c'est face, vous vous réveillez deux fois, le lundi et le mardi $\rightarrow$ **Le nombre de réveils avec 'Face' est de 100 fois**
> 
> En d'autres termes, pour la situation du moment où vous vous réveillez, sur un total de 150 fois, il y a 50 fois le 'modèle réveillé avec pile' et 100 fois le 'modèle réveillé avec face'.
> C'est pourquoi la probabilité que le réveil que vous vivez actuellement soit 'Pile' est de 50 / 150 = **1/3** !"

Il s'agit d'une opinion puissante basée sur le "fréquentisme" et le "principe anthropique", qui intègre la situation même d'"exister (être observée) maintenant" comme élément de l'espace de probabilité dans le calcul.

---

## 3. Calculons avec le théorème de Bayes

Certains tentent également de résoudre ce problème en utilisant le "théorème de Bayes", un outil mathématique de mise à jour des probabilités.
Organisons la logique des "partisans de 1/3" du point de vue de la probabilité conditionnelle.

L'état au moment du réveil correspond à l'un de ces 3 cas :
1. $E_1$ : La pièce est sur "Pile", et on est "Lundi"
2. $E_2$ : La pièce est sur "Face", et on est "Lundi"
3. $E_3$ : La pièce est sur "Face", et on est "Mardi"

La probabilité d'obtenir "Pile" est de $1/2$, et celle d'obtenir "Face" est de $1/2$.
Cependant, dans le cas de "Face", comme "Lundi" et "Mardi" sont parfaitement symétriques (indiscernables à cause de l'absence de mémoire), on peut considérer que la probabilité d'occurrence de $E_2$ et de $E_3$ est égale.

Puisque la somme de toutes les probabilités doit être égale à $1$, en attribuant à chaque réveil une probabilité égale en tant qu'"événement (point d'observation)" indépendant, nous obtenons :
$P(E_1) = 1/3$
$P(E_2) = 1/3$
$P(E_3) = 1/3$
Par conséquent, la conclusion est que "la probabilité que ce soit pile ($P(E_1)$)" est de $1/3$.

D'un autre côté, les "partisans de 1/2" réfutent cela en affirmant que "le lundi et le mardi quand la pièce est face ($E_2$ et $E_3$) ne sont, à l'origine, que des événements dépendants dérivés du résultat de la même unique pièce, et qu'il est erroné de les compter comme des probabilités indépendantes".

---

## 4. Pourquoi ce problème reste-t-il non résolu ?

La raison pour laquelle "le problème de la Belle au bois dormant" tourmente autant les chercheurs ne relève pas d'une simple erreur de calcul ou d'une illusion.
C'est parce que ce problème touche à la question fondamentale la plus profonde de la théorie des probabilités, à savoir la question philosophique : **"Qu'est-ce que la probabilité, au juste ?"**

- Pour les **partisans de 1/2**, la probabilité est "une propriété physique de la pièce" ou "un fait objectif".
- Pour les **partisans de 1/3**, la probabilité est le "degré de croyance de l'observateur (la Belle)" ou "la fréquence observée".

Des thèmes profonds, faisant écho au "problème de la mesure" en mécanique quantique ou au "principe anthropique" en cosmologie (l'idée de rétrocalculer les probabilités de l'univers à partir du fait que nous existons), sont condensés dans cette simple expérience de tirage au sort.

## 5. Conclusion

Si vous deveniez le sujet de cette expérience, répondriez-vous "1/2" ou "1/3" à votre réveil ?

Quelle que soit votre réponse, des mathématiciens de renommée mondiale se tiendront derrière vous pour vous défendre.
Comment une définition mathématique apparemment simple peut-elle s'effondrer dès qu'elle est liée aux concepts épineux de "subjectivité" et d'"existence" humaine. Aujourd'hui encore, le paradoxe continue d'ébranler notre bon sens.
