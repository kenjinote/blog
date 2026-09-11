---
title: "Voir une pomme bleue prouve-t-il que « les corbeaux sont noirs » ? : Les corbeaux de Hempel"
description: "Peut-on prouver l'hypothèse selon laquelle « les corbeaux sont noirs » sans jamais voir de corbeau ? Le paradoxe de l'induction créé par l'équivalence logique."
date: 2026-09-10T21:00:00+09:00
draft: false
slug: "hempels-ravens"
image: "img/hempels_ravens.jpg"
math: true
mermaid: true
categories: ["Paradoxes mathématiques", "Logique"]
tags: ["Paradoxe", "Induction", "Équivalence logique", "Contraposée"]
---

Comment les scientifiques prouvent-ils une théorie ? En général, ils utilisent l'« induction », qui consiste à observer le monde et à recueillir des données.
Par exemple, si vous voulez prouver l'hypothèse selon laquelle « tous les corbeaux sont noirs », vous observerez les corbeaux du monde entier et confirmerez un par un qu'ils sont noirs.

Cependant, dans les années 1940, le logicien Carl Hempel a souligné une étrange faille logique cachée dans cette méthode scientifique évidente.
Il s'agit du paradoxe des **corbeaux de Hempel (Hempel's Ravens)**, selon lequel **« le simple fait de voir une pomme bleue ou des chaussures rouges devient une preuve que 'les corbeaux sont noirs' »**.

## Substitution logique : la magie de la contraposée

Pour comprendre l'argument de Hempel, il faut se rappeler du concept de **« contraposée »** appris au lycée en mathématiques.

En logique, si une proposition « Si A, alors B » est vraie, sa contraposée « Si non B, alors non A » est obligatoirement vraie (c'est ce qu'on appelle l'équivalence logique).

Hypothèse $H_1$ : **« Tous les corbeaux sont noirs (Si c'est un corbeau, alors c'est noir) »**

Prenons la contraposée de cette hypothèse $H_1$.
Cela devient « Si ce n'est pas noir, alors ce n'est pas un corbeau ».

Hypothèse $H_2$ : **« Tout ce qui n'est pas noir n'est pas un corbeau »**

Selon les règles de la logique, $H_1$ et $H_2$ ont **exactement la même signification (équivalence)**. Si l'une est prouvée, l'autre est automatiquement prouvée.

## Prouver les corbeaux sans voir de corbeaux

Or, pour vérifier l'hypothèse $H_1$ (les corbeaux sont noirs), chaque fois que l'on trouve un corbeau noir, la probabilité (la preuve) de l'hypothèse se renforce un peu.
C'est quelque chose que tout le monde accepte.

Cependant, puisque $H_1$ et $H_2$ ont la même signification, trouver une preuve pour l'hypothèse $H_2$ (ce qui n'est pas noir n'est pas un corbeau) devrait être directement une preuve pour l'hypothèse $H_1$.

Alors, quelle est la preuve de $H_2$ ?
Il suffit de trouver « quelque chose qui n'est ni noir, ni un corbeau ».

- Supposons qu'il y ait une **« pomme bleue »** sur la table. Ce n'est ni noir, ni un corbeau. C'est donc une preuve à l'appui de $H_2$.
- Il y avait des **« chaussures rouges »** dans le placard. Celles-ci ne sont ni noires, ni des corbeaux. C'est une preuve de $H_2$.
- Des **« nuages blancs »** flottent dans le ciel. C'est aussi une preuve de $H_2$.

Puisque la preuve de $H_2$ a la même valeur que la preuve de $H_1$, la conclusion étrange suivante est logiquement déduite :

**« Plus vous observez de pommes bleues ou de chaussures rouges dans une pièce, plus vous prouvez que l'hypothèse 'tous les corbeaux sont noirs' est correcte. »**

```mermaid
graph TD
    A["Proposition H1 : Tous les corbeaux sont noirs"] <-->|Équivalence logique (Contraposée)| B["Proposition H2 : Ce qui n'est pas noir n'est pas un corbeau"]
    
    C["Observation : Corbeau noir"] -->|Sert de preuve| A
    D["Observation : Pomme bleue"] -->|Sert de preuve| B
    
    D -.->|Par conséquent, cela devrait aussi être une preuve ?| A
    
    style A fill:#4CAF50,stroke:#333,stroke-width:2px,color:#fff
    style B fill:#4CAF50,stroke:#333,stroke-width:2px,color:#fff
    style C fill:#2196F3,stroke:#333,color:#fff
    style D fill:#FF9800,stroke:#333,color:#fff
```

## Pourquoi cela va-t-il à l'encontre de l'intuition ?

Il n'y a aucun ornithologue au monde dont la conviction que « les corbeaux sont noirs » se renforce en voyant une pomme bleue. Bien que cela soit parfaitement correct d'un point de vue logique, pourquoi notre bon sens le rejette-t-il ?

Dans le monde de la philosophie et de la statistique, plusieurs approches ont été proposées pour résoudre ce paradoxe.

### 1. La solution bayésienne (différence de quantité d'information)

La contre-argumentation la plus puissante du point de vue des statistiques modernes (probabilités bayésiennes) se concentre sur la différence de « force de la preuve (quantité d'information) ».

Il y a infiniment plus de « choses qui ne sont pas noires » dans le monde que de « choses noires », et il y a astronomiquement plus de « choses qui ne sont pas des corbeaux » que de « corbeaux ».

Lorsque vous voyez une pomme bleue, c'est certes une preuve que « tous les corbeaux sont noirs », mais sa **valeur en tant que preuve (l'augmentation de la probabilité) est infiniment proche de zéro**.
Le fait de confirmer l'existence d'une des innombrables « choses qui ne sont pas noires » dans le vaste univers n'augmente la probabilité que « les corbeaux soient noirs » que de l'ordre d'un grain de sable retiré d'un désert. D'un autre côté, trouver directement un corbeau noir a une valeur de preuve écrasante.

En d'autres termes, la solution bayésienne est que logiquement « une pomme bleue est une preuve », mais en pratique « sa valeur en tant que preuve est égale à zéro, donc elle peut être ignorée ».

### 2. Les limites de l'« ornithologie de salon »

Ce paradoxe met en évidence à quel point le fondement même de la science, « l'induction (déduire des lois générales à partir d'observations) », repose sur des prémisses fragiles. Si l'on ne se fie qu'à l'équivalence logique, une « ornithologie de salon » devient possible, où l'on pourrait vérifier n'importe quelle loi de l'univers (« tous les cygnes sont blancs », « tous les extraterrestres ne sont pas verts », etc.) simplement en observant les objets hétéroclites dans sa chambre sans jamais sortir.

Les corbeaux de Hempel est un paradoxe fascinant qui montre que les mots « preuve » et « prouver » que nous utilisons inconsciemment ne peuvent pas être pleinement appréhendés uniquement par les règles de la logique symbolique pure.
