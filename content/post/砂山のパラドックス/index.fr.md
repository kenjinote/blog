---
title: "Si l'on retire un grain de sable, quand un tas de sable cesse-t-il d'être un tas ? : Le paradoxe sorite"
description: "Où se situe la frontière entre un « tas de sable » et « ce qui n'est pas un tas » ? Un paradoxe philosophique hérité de la Grèce antique qui interroge l'essence même de l'ambiguïté."
date: 2026-09-10T21:00:00+09:00
draft: false
slug: "sorites-paradox"
image: "img/sorites_paradox.jpg"
math: true
mermaid: true
categories: ["Paradoxes mathématiques", "Philosophie", "Logique"]
tags: ["Paradoxe", "Ambiguïté", "Sorite", "Logique floue"]
---

Imaginons un beau tas constitué de 10 000 grains de sable. Tout le monde s'accorde à dire qu'il s'agit bien d'un « tas de sable ».
Retirons-en un seul grain. 9 999 grains. C'est toujours un tas, n'est-ce pas ?
Retirons-en encore un. 9 998 grains. C'est encore un tas.

Poursuivons cette opération.
Le simple retrait d'un grain ne devrait pas transformer un « tas de sable » en « quelque chose qui n'est pas un tas ». Pourtant, si l'on répète indéfiniment ce raisonnement, on finit par ne plus avoir qu'un seul grain de sable.

**Un seul grain de sable est-il un « tas » ?**

Bien sûr, personne n'appellerait un seul grain de sable un « tas ». Et pourtant, nous n'avons jamais réfuté la prémisse selon laquelle « retirer un grain ne change pas le fait qu'un tas reste un tas ». Le raisonnement se brise quelque part, mais **à partir de combien de grains le tas cesse-t-il d'être un tas ?**

C'est le **« paradoxe sorite » (ou paradoxe du tas de sable)**, qui remonte au philosophe grec Eubulide, au IVᵉ siècle avant J.-C.

## Structure logique

Ce paradoxe peut être formulé sous la forme d'un syllogisme :

**Prémisse 1** : Un ensemble de 10 000 grains de sable constitue un « tas ».
**Prémisse 2** : Si l'on retire un grain d'un tas de sable, celui-ci reste un « tas ».
**Conclusion** : Par conséquent, un seul grain de sable est aussi un « tas ».

Prises individuellement, les prémisses 1 et 2 semblent parfaitement raisonnables. Cependant, l'application répétée de la prémisse 2 conduit à une conclusion manifestement fausse.

```mermaid
graph LR
    A["10 000 grains = tas"] -->|Retrait d'1 grain| B["9 999 grains = tas"]
    B -->|Retrait d'1 grain| C["9 998 grains = tas"]
    C -->|...répétition...| D["100 grains = tas ?"]
    D -->|Retrait d'1 grain| E["10 grains = tas ?"]
    E -->|Retrait d'1 grain| F["1 grain = tas ?"]
    
    style A fill:#4CAF50,color:#fff
    style D fill:#FF9800,color:#fff
    style E fill:#FF5722,color:#fff
    style F fill:#F44336,color:#fff,stroke-width:3px
```

## Pourquoi ce paradoxe est-il insoluble ?

Le cœur du paradoxe du tas de sable réside dans le fait que **le mot « tas » est intrinsèquement ambigu**.
Il n'existe pas de définition précise (de seuil) indiquant « à partir de combien de grains on a un tas ». Ce type de concept est appelé **« prédicat vague » (vague predicate)**.

Notre langage quotidien regorge de tels mots ambigus.

- **« Grand »** : à partir de combien de centimètres ? Une personne de 180 cm est « grande ». Et si on lui retire 1 mm ? Encore 1 mm ?
- **« Riche »** : à partir de quel patrimoine ? Avec 10 milliards de yens, on est « riche ». Et si on retire 1 yen ?
- **« Chauve »** : en dessous de combien de cheveux ? Avec 0 cheveu, on est « chauve ». Et si un cheveu repousse ?

Tous ces exemples possèdent exactement la même structure que le paradoxe du tas de sable.

## Les approches des philosophes

### 1. L'approche épistémique (la frontière existe)

Selon cette approche, « il existe en réalité une frontière nette entre le tas et le non-tas, mais l'être humain n'a tout simplement pas la capacité de la percevoir ».
Par exemple, il existerait une limite précise telle que « 5 837 grains forment un tas, mais 5 836 grains n'en forment pas », que nous serions incapables de connaître.

Du point de vue de la logique formelle, cette position est satisfaisante, mais beaucoup de gens la trouvent intuitivement insatisfaisante.

### 2. La logique floue (valeurs de vérité graduées)

En logique classique, une proposition est soit « vraie » soit « fausse ». En logique floue, elle peut prendre **une valeur comprise entre 0 et 1**.

Par exemple :
- 10 000 grains de sable → « degré de tas = 1,0 (parfaitement un tas) »
- 5 000 grains → « degré de tas = 0,7 »
- 100 grains → « degré de tas = 0,1 »
- 1 grain → « degré de tas = 0,0 (parfaitement non-tas) »

Cette méthode est pragmatique, mais elle ne résout pas entièrement le paradoxe. En effet, une nouvelle ambiguïté surgit : « quelle est la différence entre un degré de tas de 0,7 et de 0,699 ? »

### 3. Le supervaluationnisme (Supervaluationism)

Selon cette conception, on considère simultanément toutes les frontières raisonnables possibles pour le mot « tas ». Si toutes les frontières classent l'ensemble comme « tas », alors c'est « assurément un tas ». Si toutes le classent comme « non-tas », alors c'est « assurément un non-tas ». Le domaine où les avis divergent est qualifié d'« indéterminé ».

## Impact sur la société contemporaine

Le paradoxe du tas de sable n'est pas un simple jeu de mots : il soulève des problèmes graves dans le monde réel du droit et des politiques publiques.

- **L'âge de la majorité** : à 17 ans et 364 jours, on est « enfant » ; à 18 ans et 0 jour, on est « adulte ». Qu'est-ce qui change fondamentalement en une journée ?
- **Le seuil de pauvreté** : si le revenu annuel est inférieur de 1 yen au montant de référence, on est « pauvre » ; s'il est supérieur de 1 yen, on ne l'est pas.
- **Les réglementations environnementales** : si les émissions de polluants dépassent la valeur limite de 0,001 mg, c'est illégal. Si elles sont exactement à la limite, c'est légal.

Le langage et la pensée humaine comportent une part intrinsèque d'ambiguïté, et tenter de découper le monde en dichotomies nettes est peut-être en soi une entreprise vouée à l'échec. Le paradoxe du tas de sable est un paradoxe qui, depuis plus de 2 400 ans, continue de tourmenter les philosophes et met en lumière les limites fondamentales de l'intelligence humaine.
