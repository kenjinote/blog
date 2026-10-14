---
title: "Le pliage de papier peut-il surpasser la règle et le compas ? Les mathématiques de l'origami"
date: 2026-10-14T01:00:00+09:00
draft: false
slug: "origami-mathematics-axioms-geometric-constructions-angle-trisection"
tags:
  - Mathématiques
  - Géométrie
  - Algèbre abstraite
  - Ingénierie de l'origami
  - Histoire des sciences
categories:
  - Mathématiques
image: "eyecatch.jpg"
math: true
---

Pendant plus de deux millénaires, les géomètres ont buté sur les <strong>trois grands problèmes de l'Antiquité grecque</strong> :
1. <strong>La trisection de l'angle</strong> : diviser un angle quelconque en trois parties égales avec une règle et un compas.
2. <strong>La duplication du cube (problème de Délos)</strong> : construire le côté d'un cube de volume double ($\sqrt[3]{2}$).
3. <strong>La quadrature du cercle</strong> : construire un carré de même aire qu'un cercle ($\sqrt{\pi}$).

En 1837, Pierre Wantzel prouva que la règle et le compas ne permettent que des extensions de corps de degré $2^k$. Comme la trisection et la duplication du cube requièrent des racines de polynômes irréductibles de degré 3 ($x^3 - 3x - 1 = 0$ et $x^3 - 2 = 0$), ces constructions sont <strong>absolument impossibles</strong> dans le cadre euclidien.

Pourtant, au XXe siècle, une découverte stupéfiante bouleversa la géométrie :
<strong>En pliant simplement une feuille de papier carrée, la trisection de l'angle et la construction de $\sqrt[3]{2}$ s'accomplissent en quelques secondes avec une rigueur absolue !</strong>

L'art traditionnel de l'<strong>origami</strong> est en réalité un <strong>calculateur analogique capable de résoudre des équations du troisième degré</strong>.

---

## 1. Les axiomes de Huzita-Hatori

Le pliage est une réflexion par rapport à une droite. Entre 1989 et 2001, Huzita, Justin et Hatori ont codifié les sept axiomes universels de l'origami :

```mermaid
flowchart TD
    A1["Axiome 1: Plier une droite passant par 2 points (degré 1)"]
    A2["Axiome 2: Plier un point sur un autre (médiatrice: degré 1)"]
    A3["Axiome 3: Plier une droite sur une autre (bissectrice: degré 1)"]
    A4["Axiome 4: Plier une perpendiculaire à une droite en un point (degré 1)"]
    A5["Axiome 5: Plier un point sur une droite passant par un autre point (degré 2)"]
    A7["Axiome 7: Plier un point sur une droite perpendiculairement à une autre (degré 2)"]
    A6["Axiome 6: Plier DEUX points simultanément sur DEUX droites !<br/>【Tangente commune à 2 paraboles : Équation du 3e degré !】"]
end
```

L'<strong>Axiome 6</strong> est la clé de voûte qui transcende la géométrie classique.

---

## 2. Pourquoi l'Axiome 6 résout-il les équations cubiques ?

Tout pli amenant un point $P$ sur une droite $L$ est la médiatrice du segment reliant $P$ à son image. Géométriquement, cette droite est une <strong>tangente à la parabole</strong> de foyer $P$ et de directrice $L$.

L'Axiome 6 consiste à trouver un pli tangent à la fois à la parabole $\mathcal{P}_1$ et à la parabole $\mathcal{P}_2$.
C'est la recherche de la <strong>tangente commune à deux coniques</strong>. L'équation de la pente $m$ de cette tangente est un <strong>polynôme cubique général</strong> :

$$
A m^3 + B m^2 + C m + D = 0
$$

---

## 3. Trisection de l'angle et duplication du cube

- <strong>Trisection d'Abe (1980)</strong> : Hisashi Abe a conçu un protocole utilisant l'Axiome 6 pour diviser un angle quelconque en trois angles rigoureusement isométriques.
- <strong>Duplication du cube de Messer (1986)</strong> : Peter Messer a montré comment construire $\sqrt[3]{2}$ sur un carré unitaire.
- <strong>Corps des nombres origamiques $\mathcal{O}$</strong> : Le degré d'extension est de la forme $[\mathbb{Q}(\alpha) : \mathbb{Q}] = 2^a 3^b$, ce qui rend constructibles l'heptagone régulier (7 côtés) et l'ennéagone régulier (9 côtés) !

---

## 4. Pliabilité à plat : théorèmes de Kawasaki et Maekawa

- <strong>Théorème de Kawasaki</strong> : Un sommet est pliable à plat si et seulement si la somme des angles alternés vaut $180^\circ$ ($\theta_1 + \theta_3 + \dots = 180^\circ$).
- <strong>Théorème de Maekawa</strong> : La différence entre plis montagne ($M$) et plis vallée ($V$) vaut toujours $\pm 2$ ($M - V = \pm 2$).

---

## 5. Ingénierie de l'origami : de l'espace à la médecine

- <strong>Pliage Miura (Miura-ori)</strong> : Déploiement rigide à un seul degré de liberté pour les panneaux solaires spatiaux (télescope James Webb).
- <strong>Stents biomédicaux</strong> : Tubes auto-déployables insérés dans les vaisseaux sanguins.
- <strong>Métamatériaux auxétiques</strong> : Structures à coefficient de Poisson négatif s'élargissant sous traction.

---

## 6. Conclusion

L'origami démontre que les limites mathématiques dépendent des outils physiques autorisés. La feuille de papier libère la pensée géométrique du carcan euclidien.
