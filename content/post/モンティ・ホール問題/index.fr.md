---
title: "Le Problème de Monty Hall"
slug: "モンティ・ホール問題"
date: 2024-03-31T23:41:51+09:00
tags: ["Mathématiques", "Probabilité", "Problème de Monty Hall"]
draft: false
image: "img_1.png"
categories: ["Mathématiques, Cryptographie et Quantique"]
---

## Qu'est-ce que le problème de Monty Hall ?
Le problème de Monty Hall est l'un des jeux présentés dans l'émission de télévision américaine "Let's Make a Deal", et se présente comme suit :

Prérequis : Derrière l'une des 3 portes se trouve un prix, et les 2 autres sont perdantes.

1. Le participant choisit l'une des 3 portes.
2. Le présentateur ouvre une des 2 portes non choisies par le participant, révélant qu'elle est perdante.
3. On demande alors au participant s'il souhaite changer la porte qu'il a choisie.

Le problème est de déterminer s'il est préférable pour le participant de changer de porte ou non.

## Solution
La solution au problème de Monty Hall est la suivante :

1. Si le participant ne change pas la porte initialement choisie
   - Probabilité de gagner : 1/3
   - Probabilité de perdre : 2/3

2. Après que le présentateur a ouvert une porte perdante
    - S'il ne change pas, probabilité de gagner : 1/3 (la même qu'à l'étape 1)
    - S'il change, probabilité de gagner : 2/3 (la probabilité restante de l'étape 1)

Par conséquent, la probabilité de gagner est plus élevée si le participant change de porte.

## Référence
- Wikipédia [Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem)
