---
title: "Comment partager un gâteau de manière 'juste' ? Les mathématiques du partage sans envie"
date: 2026-10-14T01:00:00+09:00
draft: false
slug: "fair-division-cake-cutting-envy-free-proportionality-mathematics"
tags:
  - Mathématiques
  - Théorie des jeux
  - Théorie de la décision
  - Algorithmes
  - Économie
categories:
  - Mathématiques
image: "eyecatch.jpg"
math: true
---

Partager un héritage, diviser les biens lors d'un divorce ou répartir les chambres et le loyer entre colocataires confronte l'être humain à la notion de <strong>justice (équité)</strong>.

La méthode intuitive ancestrale à deux personnes est : *« L'un coupe, l'autre choisit (Cut and Choose) »*. Celui qui coupe s'assure de faire deux parts d'égale valeur, et celui qui choisit prend sa part préférée.

Mais comment procéder avec <strong>trois participants ou plus</strong> ?
Et si le gâteau n'est pas homogène (chocolat d'un côté, fraises de l'autre) et que les goûts divergent ? Une découpe géométrique égale en volume frustrera inévitablement celui qui déteste les fraises.

Existe-t-il une règle mathématique garantissant que chacun estime avoir reçu une part équitable et que <strong>personne n'envie la part d'autrui</strong> ?

C'est l'objet de la <strong>théorie du partage équitable (Fair Division)</strong>, ou <strong>problème de découpe du gâteau (Cake-Cutting Problem)</strong>. Formalisé dans les années 1940 par Hugo Steinhaus, ce domaine allie théorie de la mesure, topologie (lemme de Sperner), théorie des jeux et algorithmique. En 2016, Haris Aziz et Simon Mackenzie ont résolu une énigme cinquantenaire en publiant le premier algorithme fini et borné pour un nombre arbitraire $n$ de personnes.

---

## 1. Modélisation mathématique par la théorie de la mesure

### 1.1 Le gâteau comme continuum
Le gâteau est représenté par l'intervalle réel $X = [0, 1]$. Toute part correspond à un sous-ensemble borélien mesurable $A \in \mathcal{B}(X)$.

### 1.2 Mesures de valeur subjectives
Chaque participant $i \in \{1, \dots, n\}$ possède une mesure de valeur privée non négative et non atomique $V_i: \mathcal{B}(X) \to [0, 1]$ :
1. <strong>Normalisation</strong> : $V_i(X) = 1, V_i(\emptyset) = 0$.
2. <strong>Additivité</strong> : $A \cap B = \emptyset \implies V_i(A \cup B) = V_i(A) + V_i(B)$.
3. <strong>Divisibilité</strong> : la lame du couteau peut trancher continûment en tout point.

---

## 2. Quatre critères de justice : Proportionnalité vs Absence d'envie

Pour une partition $(X_1, \dots, X_n)$ :

| Critère | Définition formelle | Signification |
| :---: | :---: | :---: |
| <strong>Proportionnalité (PROP)</strong> | $\forall i, \quad V_i(X_i) \ge \frac{1}{n}$ | Chacun reçoit au moins $1/n$ de la valeur totale selon son propre étalon |
| <strong>Absence d'envie (EF)</strong> | $\forall i, j, \quad V_i(X_i) \ge V_i(X_j)$ | Nul ne préfère la part d'un autre à la sienne |
| <strong>Équité (EQ)</strong> | $\forall i, j, \quad V_i(X_i) = V_j(X_j)$ | Utilités subjectives strictement identiques |
| <strong>Optimalité de Pareto (PE)</strong> | Aucune réallocation n'améliore le sort de l'un sans léser autrui | Efficacité maximale des ressources |

### Pourquoi l'absence d'envie est supérieure
Pour $n=2$, proportionnalité et absence d'envie coïncident. Dès $n=3$, la proportionnalité n'exclut pas l'envie : si Alice reçoit $35\%$ ($> 33.3\%$), mais que Bob reçoit $50\%$ à ses yeux, Alice éprouvera une jalousie intense. L'absence d'envie (<strong>Envy-Freeness</strong>) est le véritable standard de paix sociale.

---

## 3. Le protocole Selfridge-Conway pour 3 personnes

Découvert vers 1960 par Selfridge et Conway, ce protocole élégant requiert au plus 5 coupes :

1. <strong>Étape 1 (Tranchage et rognage)</strong> :
   - $P_1$ découpe le gâteau en 3 parts égales à ses yeux ($A, B, C$).
   - $P_2$ rogne la plus grande part ($A$) d'une lamelle $T$ pour créer une égalité avec la deuxième plus grande part ($A'$).
   - Ordre de choix : $P_3$ choisit en premier, puis $P_2$ (qui doit prendre $A'$ si $P_3$ ne l'a pas prise), puis $P_1$.
   - $P_1$ recevant une part intacte valant $1/3$, personne n'est envié !
2. <strong>Étape 2 (Partage des rognures $T$)</strong> :
   - Le joueur ayant reçu $A'$ est noté $T_{\text{in}}$, l'autre joueur parmi $\{P_2, P_3\}$ est noté $T_{\text{out}}$.
   - $T_{\text{out}}$ divise $T$ en 3 parts égales.
   - Choix dans l'ordre : $T_{\text{in}} \to P_1 \to T_{\text{out}}$.
   - <strong>Génie du mécanisme</strong> : même si $T_{\text{in}}$ recevait la totalité de $T$, la part $A' \cup T$ vaudrait exactement $1/3$ pour $P_1$. Donc $P_1$ n'envie jamais $T_{\text{in}}$ !

---

## 4. Lemme de Sperner et partage des loyers

Francis Su a démontré en 1999, grâce au <strong>lemme de Sperner</strong> en topologie combinatoire, qu'il existe toujours un vecteur de loyers équilibrant la colocation de manière totalement sans envie (*Rental Harmony*).

---

## 5. Conclusion

La justice ne réside pas dans une uniformité géométrique aveugle, mais dans le respect des préférences subjectives. Les mathématiques nous enseignent comment transformer les désaccords en harmonie collective.
