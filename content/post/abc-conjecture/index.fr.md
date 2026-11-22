---
title: "La conjecture abc et IUT : une preuve revendiquée et un débat toujours ouvert"
date: "2026-09-14T13:00:00+09:00"
lastmod: 2026-11-23
slug: "abc-conjecture"
image: "eyecatch.jpg"
categories: ["mathematics", "science"]
tags: ["ABC Conjecture", "Number Theory", "IUT Theory", "Shinichi Mochizuki"]
draft: false
description: "Présentation de la conjecture abc, de la preuve que Shinichi Mochizuki affirme obtenir par IUT, de sa publication dans PRIMS et du débat mathématique non résolu."
---

## Énoncé de la conjecture abc

Soient $a,b,c$ des entiers positifs premiers entre eux deux à deux tels que $a+b=c$. Le **radical** d’un entier positif $n$ est le produit de ses diviseurs premiers distincts :

$$\operatorname{rad}(n)=\prod_{p\mid n}p$$

Par exemple, $\operatorname{rad}(2^3\cdot3^2)=6$. Le radical ignore les exposants des facteurs premiers et peut donc être bien inférieur à l’entier lui-même.

La conjecture abc affirme que, pour tout $\varepsilon>0$, il existe une constante $K_\varepsilon$ telle que tout triplet de ce type vérifie

$$c\le K_\varepsilon\operatorname{rad}(abc)^{1+\varepsilon}.$$

La constante peut dépendre de $\varepsilon$. Joseph Oesterlé et David Masser ont formulé la conjecture en 1985. Elle exprime une forte contrainte entre l’addition et la décomposition en facteurs premiers ; ce n’est pas la règle simpliste selon laquelle les petits facteurs premiers de $a$ et de $b$ obligeraient $c$ à avoir un grand facteur premier.

## La preuve revendiquée par Mochizuki au moyen d’IUT

En 2012, Shinichi Mochizuki, de l’Université de Kyoto, a publié des travaux présentant la théorie de Teichmüller inter-universelle (IUT) comme un nouveau cadre pour des problèmes de géométrie diophantienne, dont la conjecture abc. IUT est une théorie très technique portant sur des objets arithmétiques tels que les courbes elliptiques sur des corps de nombres et reliant des idées de la théorie de Teichmüller, de la théorie de Hodge-Arakelov et de la géométrie anabélienne. Des notions comme les théâtres de Hodge et le réseau log-thêta servent à comparer des données arithmétiques entre structures. La résumer à une « séparation de l’addition et de la multiplication dans des univers distincts » serait trompeur.

Mochizuki affirme que la conjecture abc découle d’IUT. Les quatre articles ont fait l’objet d’un long processus d’évaluation et ont paru dans un numéro spécial de 2021 de *Publications of the Research Institute for Mathematical Sciences* (PRIMS). Cette publication est un fait important, mais elle ne suffit pas à établir un consensus mathématique ni à clore le débat.

## Ce qui reste controversé

Dans un rapport de 2018, Peter Scholze et Jakob Stix ont soutenu qu’une étape essentielle — le passage du théorème 3.11 au corollaire 3.12 d’IUT III, utilisé pour parvenir à l’inégalité abc — comportait une lacune. Mochizuki rejette cette critique, qu’il attribue à une mauvaise compréhension de la théorie, et a exposé à nouveau sa position dans un rapport d’octobre 2025. Ce paragraphe résume les positions déclarées des auteurs ; il ne vérifie pas indépendamment la preuve d’IUT.

Une présentation prudente distingue donc trois points : les articles d’IUT ont été publiés dans PRIMS ; Mochizuki affirme qu’ils démontrent abc ; le désaccord des mathématiciens sur l’argument central n’est pas résolu. Il serait trompeur de présenter la conjecture abc comme un théorème largement établi.

## Lien avec le dernier théorème de Fermat

Si elle est vraie, la conjecture abc impliquerait le dernier théorème de Fermat : l’équation $x^n+y^n=z^n$ n’a pas de solution en entiers positifs pour $n\ge3$. C’est une conséquence conditionnelle, et non l’affirmation que le théorème de Fermat n’a pas été démontré : Andrew Wiles et d’autres l’ont déjà prouvé.

Supposons qu’une solution $x,y,z$ première entre eux deux à deux existe. Pour tout entier positif $k$, $(x^{nk},y^{nk},z^{nk})$ serait également un triplet d’addition premier entre eux. Son radical resterait fixe, $\operatorname{rad}(x^{nk}y^{nk}z^{nk})=\operatorname{rad}(xyz)$, tandis que $z^{nk}$ croîtrait sans borne. On obtiendrait ainsi une infinité de triplets qui violeraient la borne abc pour tout $\varepsilon>0$ fixé, ce qui est contradictoire.

## Références

- [Formulation classique d’abc (Jordan S. Ellenberg)](https://arxiv.org/abs/math/9909098)
- [Numéro spécial PRIMS consacré à IUT, 2021](https://ems.press/journals/prims/issues/1507)
- [Rapport de Scholze et Stix (2018)](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf)
- [Rapport IUT de Mochizuki (octobre 2025)](https://www.kurims.kyoto-u.ac.jp/~motizuki/IUT-report-2025-10.pdf)
- [Présentation panoramique d’IUT (Mochizuki, 2012)](https://www.kurims.kyoto-u.ac.jp/~motizuki/Panoramic%20Overview%20of%20Inter-universal%20Teichmuller%20Theory.pdf)

Cette brève introduction présente la conjecture et le débat public ; elle ne reconstitue ni n’évalue la preuve d’IUT.
