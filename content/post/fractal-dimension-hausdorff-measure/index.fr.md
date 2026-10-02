---
title: "Dimension fractale et mesure de Hausdorff : les dimensions décimales au-delà du mur des entiers et la science de l'autosimilarité"
description: "L'ensemble de Mandelbrot, le paradoxe du littoral et les dimensions fractionnaires entre 1D et 2D. L'ordre naturel révélé par la géométrie et la théorie de la mesure."
slug: "fractal-dimension-hausdorff-measure"
date: "2026-10-03T05:00:00+09:00"
categories: ["mathematics", "physics"]
tags: ["fractal", "hausdorff-dimension", "mandelbrot", "measure-theory"]
image: "eyecatch.jpg"
---

## Introduction : repenser le concept de dimension

L'espace que nous expérimentons au quotidien est perçu comme un espace euclidien en 3 dimensions. Une ligne sur du papier est en 1 dimension, un plan en 2 dimensions et un solide en 3 dimensions. Il s'agit d'une intuition solide qui sert de fondement à la perception spatiale humaine depuis des milliers d'années, depuis Euclide dans la Grèce antique. Cependant, lorsque l'on observe les formes complexes de la nature, ce paradigme de « dimension entière » fait face à une limite décisive. Les nuages ne sont pas des sphères, les montagnes ne sont pas des cônes, les côtes ne sont pas des arcs de cercle. Les branches des arbres, les réseaux sanguins, les trajectoires de la foudre et bien d'autres formes trouvées dans la nature possèdent une « rugosité » fondamentalement différente des objets de la géométrie euclidienne lisse.

La « géométrie fractale » est née comme un nouveau langage pour décrire mathématiquement cette complexité de la nature. Ses fondements théoriques reposent sur la « mesure de Hausdorff » et la « dimension de Hausdorff » associée, des concepts issus des profondeurs de l'analyse réelle et de la théorie de la mesure. Dans cet article, nous expliquerons en profondeur comment la dimension fractale est définie, calculée et appliquée à la compréhension des phénomènes naturels, de la géométrie intuitive à la théorie de la mesure rigoureuse.

---

## Chapitre 1 : Les limites de la géométrie euclidienne et la « rugosité de la nature »

### La question de Benoît Mandelbrot : « Quelle est la longueur de la côte de la Grande-Bretagne ? »

Il existe une question célèbre symbolisant l'aube de la géométrie fractale : « Quelle est la longueur de la côte de la Grande-Bretagne ? (How Long Is the Coast of Britain?) », qui est le titre d'un article publié par Benoît Mandelbrot (Benoit Mandelbrot) dans la revue scientifique "Science" en 1967.

À première vue, cette question semble n'être qu'un problème d'arpentage. Cependant, un profond paradoxe s'y cachait. Supposons que nous voulions mesurer la longueur du littoral en l'approchant avec une règle d'une certaine longueur (par exemple, une longueur de $\eta = 100 \text{ km}$). Que se passe-t-il avec la longueur totale mesurée si nous réduisons la longueur de la règle ($\eta = 10 \text{ km}, 1 \text{ km}, 1 \text{ m}, \dots$) ? S'il s'agit d'une courbe lisse (comme un cercle ou une parabole), la mesure converge vers une certaine valeur finie au fur et à mesure que la règle devient plus petite. C'est la définition classique de la longueur d'une courbe (longueur d'arc).

Cependant, ce n'est pas le cas pour un véritable littoral. Plus la règle est petite, plus on prend en compte les petites criques et les irrégularités des rochers qui passaient auparavant inaperçues, et la longueur du littoral augmente indéfiniment. En d'autres termes, à la limite où l'échelle de mesure $\eta$ s'approche de $0$, la longueur de la côte $L(\eta)$ diverge vers l'infini.

### L'effet Richardson

Ce phénomène avait été découvert de manière empirique par le météorologue Lewis Fry Richardson. Richardson a mesuré les longueurs des frontières et des côtes de divers pays à différentes échelles et a découvert que la loi de puissance suivante était vérifiée entre l'échelle de mesure $\eta$ et la longueur mesurée $L(\eta)$ :

$$ L(\eta) \propto \eta^{1-D} $$

Ici, $D$ est une constante et plus le littoral est complexe, plus la valeur de $D$ est grande. Bien que Richardson lui-même ait traité ce $D$ comme une constante empirique, Mandelbrot lui a donné une interprétation mathématique profonde. Il a considéré que ce $D$ représentait la « dimension » de l'objet.

Dans le cas d'une courbe lisse en 1 dimension, on a $D=1$, et $L(\eta) \propto \eta^0 = 1$, la longueur converge vers une valeur constante. Cependant, dans le cas d'une frontière extrêmement complexe comme la côte de la Grande-Bretagne, on a $D \approx 1.25$, et comme $1 - D = -0.25 < 0$, alors $L(\eta) \to \infty$ lorsque $\eta \to 0$. Cette dimension réelle supérieure à $1$ et inférieure à $2$ fut la première ébauche de la « dimension fractale ».

---

## Chapitre 2 : Autosimilarité et dimension de similitude

Le mot fractale (fractal) vient du latin « fractus » (brisé, fragmenté) et a été inventé par Mandelbrot. L'une des caractéristiques les plus fondamentales des fractales est l'« autosimilarité » (self-similarity). Cela fait référence à la propriété où, si vous agrandissez le tout, vous y trouvez la même structure que l'ensemble.

En utilisant cette autosimilarité, nous pouvons dériver une définition intuitive de la dimension appelée « dimension de similitude » (Similarity Dimension).

### Dérivation intuitive de la dimension de similitude $D$

Considérons les propriétés des figures euclidiennes lisses.
- Si on réduit un segment de droite en 1 dimension à l'échelle $1/r$, il faut $r^1$ de ces segments réduits pour reconstituer le segment de droite d'origine.
- Si on réduit un carré en 2 dimensions de $1/r$ sur chaque côté, il faut $r^2$ petits carrés pour reconstituer le carré d'origine.
- Si on réduit un cube en 3 dimensions de $1/r$ sur chaque côté, il faut $r^3$ petits cubes pour reconstituer le cube d'origine.

En général, lorsqu'une figure dans un espace de dimension $d$ est réduite de $1/r$, le nombre de copies $N$ nécessaires pour reconstruire la figure d'origine satisfait la relation :
$$ N = r^d $$
En prenant le logarithme des deux côtés de cette équation, on obtient :
$$ \log N = d \log r $$
et en résolvant pour la dimension $d$, nous pouvons la définir comme suit :

$$ d = \frac{\log N}{\log r} $$

Cette définition étendue aux figures autosimilaires qui n'ont pas de dimension entière est la « dimension de similitude ».

$$ D_s = \frac{\log N}{\log(1/r)} $$

Ici, $r$ est le taux de réduction ($0 < r < 1$), et $N$ est le nombre de pièces nécessaires pour recouvrir entièrement la figure d'origine en utilisant cette figure réduite. (Si $r$ est le taux de réduction, le dénominateur est $\log(1/r)$. Dans l'exemple précédent, $r$ était utilisé comme multiplicateur, faites donc attention à la définition des symboles).

### L'ensemble de Cantor (Cantor Set)

Introduit par Georg Cantor en 1883, cet ensemble est l'un des contre-exemples les plus importants de la théorie de la mesure.
La méthode de construction est la suivante :
1. Commencer avec l'intervalle $[0, 1]$ (Étape 0).
2. Retirer le tiers central $(1/3, 2/3)$ (Étape 1 : les intervalles sont $[0, 1/3] \cup [2/3, 1]$).
3. Retirer le tiers central de chaque intervalle restant.
4. Répéter cela à l'infini.

L'ensemble obtenu à la limite (l'ensemble triadique de Cantor) a une propriété d'autosimilarité. Il est composé de $2$ copies de l'ensemble réduit de $1/3$.
Par conséquent, la dimension de similitude est
$$ D = \frac{\log 2}{\log 3} \approx 0.6309 $$
Il s'agit d'un ensemble plus grand que 0 dimension (un point) et plus petit qu'une dimension (une ligne). Étonnamment, la mesure de Lebesgue (la longueur) de cet ensemble est de $0$, tout en contenant un nombre infini indénombrable de points.

### La courbe de Koch (Koch Curve)

C'est une courbe continue mais non dérivable partout inventée par Helge von Koch en 1904.
1. Diviser un segment en trois parties égales.
2. Remplacer le segment central par les deux côtés d'un triangle équilatéral ayant ce segment pour base.
3. Répéter cette opération pour tous les segments de droite.

En une seule opération, la longueur du segment est multipliée par $4/3$. Si on répète à l'infini, la longueur devient $(4/3)^\infty \to \infty$ (longueur infinie). D'un autre côté, la surface délimitée par ceci (le flocon de Koch) est finie. La dimension de similitude de cette courbe avec une surface nulle et une longueur infinie est obtenue par l'assemblage de $N = 4$ copies réduites au taux $r = 1/3$, donc :
$$ D = \frac{\log 4}{\log 3} \approx 1.2618 $$

### Le triangle de Sierpiński (Sierpinski Gasket)

C'est une figure obtenue en creusant répétitivement un triangle inversé au centre d'un triangle équilatéral.
Étant donné qu'il est composé de $N = 3$ copies au taux de réduction $r = 1/2$, la dimension de similitude est
$$ D = \frac{\log 3}{\log 2} \approx 1.5849 $$
La surface (mesure de Lebesgue en 2D) est de 0, mais la longueur 1D est infinie.

---

## Chapitre 3 : Définitions rigoureuses de la mesure extérieure de Hausdorff et de la dimension de Hausdorff

La dimension de similitude est intuitive et facile à calculer, mais elle ne s'applique qu'aux figures ayant une « autosimilarité stricte ». Pour déterminer la dimension des fractales naturelles ou d'ensembles mathématiquement complexes (ensembles où l'autosimilarité est brisée), nous avons besoin d'une définition stricte et universelle basée sur l'analyse réelle et la théorie de la mesure. C'est la « dimension de Hausdorff » (Hausdorff Dimension).

En 1918, Felix Hausdorff a étendu la méthode de la théorie de la mesure de Carathéodory et a défini la mesure extérieure de dimension $d$ pour tout nombre réel non négatif $d$.

### $\delta$-recouvrement ($\delta$-cover)

Considérons un sous-ensemble $E$ de $\mathbb{R}^n$. Pour tout $\delta > 0$, une famille de sous-ensembles $\{U_i\}_{i=1}^\infty$ de $E$ telle que
$$ E \subset \bigcup_{i=1}^\infty U_i \quad \text{et} \quad \operatorname{diam}(U_i) \leq \delta $$
est appelée un **$\delta$-recouvrement** de $E$. Ici, $\operatorname{diam}(U_i)$ est le diamètre de $U_i$ (la borne supérieure des distances) $\sup_{x,y \in U_i} \|x - y\|$.

### Mesure extérieure de Hausdorff $\mathcal{H}^d(E)$

Fixons un nombre réel non négatif $d \geq 0$. Pour tout $\delta$-recouvrement $\{U_i\}$ de $E$, considérons la somme des diamètres à la puissance $d$, et prenons son infimum.

$$ \mathcal{H}_\delta^d(E) = \inf \left\{ \sum_{i=1}^\infty (\operatorname{diam} U_i)^d \mathrel{\Big|} \{U_i\} \text{ est un } \delta\text{-recouvrement de } E \right\} $$

À mesure que $\delta$ diminue, les conditions de recouvrement deviennent plus strictes, l'ensemble des infimums se rétrécit et $\mathcal{H}_\delta^d(E)$ devient monotone croissante. Par conséquent, la limite lorsque $\delta \to 0$ existe (y compris $\infty$).

$$ \mathcal{H}^d(E) = \lim_{\delta \to 0} \mathcal{H}_\delta^d(E) = \sup_{\delta > 0} \mathcal{H}_\delta^d(E) $$

Ce $\mathcal{H}^d(E)$ est appelé la **mesure de Hausdorff de dimension $d$**. Du point de vue de la théorie de la mesure, il s'agit d'une mesure extérieure complète de Borel (satisfaisant la condition de Carathéodory), qui devient une véritable mesure satisfaisant l'additivité dénombrable sur la famille des ensembles de Borel.

Dans le cas où la dimension est un entier $d = n$, $\mathcal{H}^n(E)$ diffère de la mesure de Lebesgue classique de dimension $n$ seulement par un multiple constant (elles correspondent parfaitement si la constante de normalisation est ajustée).

### La dimension de Hausdorff $\dim_H(E)$ en tant que valeur critique de saut

La propriété la plus importante de la mesure de Hausdorff est le comportement de $\mathcal{H}^d(E)$ lorsqu'on modifie la valeur de $d$.
Si nous supposons que pour un certain $d$, $\mathcal{H}^d(E) < \infty$. Alors, pour tout $s > d$,
$$ \sum (\operatorname{diam} U_i)^s = \sum (\operatorname{diam} U_i)^{s-d} (\operatorname{diam} U_i)^d \leq \delta^{s-d} \sum (\operatorname{diam} U_i)^d $$
Lorsque $\delta \to 0$, $\delta^{s-d} \to 0$, de sorte que $\mathcal{H}^s(E) = 0$.
Inversement, si $\mathcal{H}^s(E) > 0$, alors pour tout $d < s$, $\mathcal{H}^d(E) = \infty$.

En d'autres termes, à mesure que l'on augmente $d$ depuis $0$, $\mathcal{H}^d(E)$ est toujours de $\infty$ jusqu'à un certain point critique, après quoi il devient toujours $0$, montrant un « saut » extrême. Cette valeur critique de $d$ est définie comme la **dimension de Hausdorff** (Hausdorff Dimension).

$$ \dim_H(E) = \inf \{ d \geq 0 \mid \mathcal{H}^d(E) = 0 \} = \sup \{ d \geq 0 \mid \mathcal{H}^d(E) = \infty \} $$

La beauté écrasante de cette définition réside dans le fait que la dimension est strictement et uniquement déterminée pour n'importe quel sous-ensemble de n'importe quel espace métrique, même si l'ensemble cible $E$ n'a pas d'autosimilarité ou s'il s'agit d'un ensemble pathologique. Les dimensions de Hausdorff de l'ensemble de Cantor ou de la courbe de Koch correspondent exactement à la dimension de similitude mentionnée précédemment.

---

## Chapitre 4 : Dimension de comptage de boîtes (dimension de capacité), dimension d'information et dimension d'emballage

Bien que la dimension de Hausdorff soit le concept mathématiquement le plus sophistiqué, il n'est pas adapté aux calculs numériques ou à l'analyse de données expérimentales (car il nécessite de trouver la limite inférieure à partir d'un nombre infini de modèles de recouvrement, puis de prendre la limite). Par conséquent, des définitions de dimension fractale plus calculables sont utilisées en mathématiques appliquées et en physique.

### Dimension de comptage de boîtes (dimension de capacité, Box-counting Dimension)

Divisons l'espace en une grille avec des côtés de longueur $\varepsilon$, et soit $N(\varepsilon)$ le nombre de boîtes (points de grille) qui coupent l'ensemble cible $E$. Alors, la dimension de comptage de boîtes $\dim_B(E)$ est définie comme suit :

$$ \dim_B(E) = \lim_{\varepsilon \to 0} \frac{\log N(\varepsilon)}{-\log \varepsilon} $$

Cette définition est très pratique et constitue la base des algorithmes (méthode de couverture) pour estimer la dimension fractale dans l'analyse d'images. Cependant, elle présente également des défauts mathématiques. Par exemple, la dimension de comptage de boîtes de l'ensemble des nombres rationnels $\mathbb{Q} \cap [0,1]$ est de $1$, mais la dimension de Hausdorff est de $0$ puisqu'il s'agit d'un ensemble dénombrable. En général, on a $\dim_H(E) \leq \dim_B(E)$.

### Dimension d'information (Information Dimension) et dimensions généralisées

Si l'ensemble fractal a une distribution non uniforme, il ne suffit pas de simplement compter les boîtes. Soit $P_i$ la mesure (probabilité) contenue dans chaque boîte $i$. En utilisant l'entropie de Shannon $I(\varepsilon) = - \sum P_i \log P_i$, la dimension d'information $D_1$ est définie :

$$ D_1 = \lim_{\varepsilon \to 0} \frac{\sum P_i \log P_i}{\log \varepsilon} $$

De plus, la théorie des « multifractales » (fractales multiples) basée sur l'entropie étendue d'Alfréd Rényi conduit au concept de dimensions généralisées (dimensions de Rényi) $D_q$.

### Dimension d'emballage (Packing Dimension)

Introduite par Tricot dans les années 1980, la dimension d'emballage $\dim_P(E)$ est un concept dual à la dimension de Hausdorff. Alors que la dimension de Hausdorff adopte une approche de « recouvrement de l'ensemble », la dimension d'emballage adopte une approche « d'emballage de sphères dans l'ensemble ».
Strictement parlant, la relation $\dim_H(E) \leq \dim_P(E) \leq \dim_{\overline{B}}(E)$ (dimension supérieure de comptage de boîtes) est vérifiée, et c'est un outil très puissant dans l'analyse probabiliste des ensembles.

---

## Chapitre 5 : L'ensemble de Mandelbrot et l'ensemble de Julia en dynamique complexe

En discutant de la géométrie fractale, il est impossible d'éviter le monde de la dynamique complexe (Complex Dynamics). En particulier, l'« ensemble de Mandelbrot » (Mandelbrot set), généré à partir d'applications quadratiques extrêmement simples sur le plan complexe, est considéré comme l'une des figures les plus complexes et les plus belles de l'histoire des mathématiques.

### Application quadratique complexe $z_{n+1} = z_n^2 + c$

Considérons un système dynamique paramétré par un nombre complexe $c \in \mathbb{C}$. En partant de la valeur initiale $z_0 = 0$, nous générons une suite $\{z_n\}$ avec la relation de récurrence suivante :

$$ z_{n+1} = z_n^2 + c $$

L'ensemble des paramètres $c$ pour lesquels cette suite ne diverge pas lorsque $n \to \infty$ et reste bornée est appelé l'**ensemble de Mandelbrot $\mathcal{M}$**.

$$ \mathcal{M} = \left\{ c \in \mathbb{C} \mathrel{\Big|} \sup_{n} |z_n| < \infty, \text{ avec } z_0 = 0 \right\} $$

D'autre part, en fixant $c$ et en modifiant la valeur initiale $z_0$, la frontière de l'ensemble des valeurs initiales pour lesquelles la suite reste bornée est appelée l'**ensemble de Julia** (Julia set). L'ensemble de Mandelbrot fonctionne comme un catalogue d'un nombre infini d'ensembles de Julia (l'espace des paramètres de connexité).

### Le théorème de Shishikura sur la dimension de Hausdorff de la frontière

La frontière de l'ensemble de Mandelbrot $\partial \mathcal{M}$ possède une structure fractale d'une complexité inimaginable. Quel que soit le grossissement, des copies infiniment petites de l'ensemble de Mandelbrot (mini-Mandelbrot) continuent d'apparaître, reliées par d'innombrables filaments.

Quelle est la « complexité » de cette frontière mathématiquement ? En 1998, le mathématicien japonais Mitsuhiro Shishikura a prouvé un théorème monumental en dynamique complexe.

**Théorème (Shishikura, 1998)**
La dimension de Hausdorff de la frontière de l'ensemble de Mandelbrot $\partial \mathcal{M}$ est exactement de $2$.
$$ \dim_H(\partial \mathcal{M}) = 2 $$

Malgré le fait qu'il s'agisse d'une simple « ligne » de frontière (unidimensionnelle) sur un plan (bidimensionnel), le fait que sa dimension de Hausdorff atteigne $2$, c'est-à-dire la dimension de l'espace lui-même, signifie que $\partial \mathcal{M}$ ondule, se plie et possède d'innombrables structures microscopiques remplissant l'espace à l'extrême sur le plan complexe. Cependant, la question de savoir si sa mesure de Lebesgue bidimensionnelle (surface) est positive reste un problème d'une grande difficulté non résolu dans les mathématiques modernes.

---

## Chapitre 6 : Les fractales dans la physique et la nature

La géométrie fractale et la dimension de Hausdorff ont dépassé le cadre des mathématiques pures et ont eu un impact perturbateur sur toutes les sciences naturelles telles que la physique, la biologie et la cosmologie. Il semble que la nature ait choisi la géométrie fractale plutôt que la géométrie euclidienne.

### Turbulence et dynamique des fluides

La « turbulence », phénomène le plus difficile en dynamique des fluides, a une structure fractale. Selon la théorie de la cascade d'énergie (par Richardson et Kolmogorov), les grands tourbillons dans les turbulences s'effondrent en tourbillons plus petits, qui s'effondrent à leur tour, répétant ce processus de manière autosimilaire. Le calcul de la dimension fractale de la région où se produit la dissipation d'énergie (structure de dissipation) est l'une des approches pour résoudre mathématiquement les équations de Navier-Stokes.

### Trajectoire du mouvement brownien $D=2$

Le « mouvement brownien » (processus de Wiener) est le phénomène par lequel des particules microscopiques se déplacent de manière irrégulière dans un liquide ou un gaz. Lorsque la trajectoire de cette particule est tracée dans l'espace, elle est infiniment dentelée et non dérivable partout.
Étonnamment, la dimension de Hausdorff de la trajectoire du mouvement brownien standard dans un espace à $n \geq 2$ dimensions est strictement de $2$ avec une probabilité de 1.
$$ \dim_H(\text{Brownian path}) = 2 \quad \text{almost surely} $$
Cela montre que bien qu'il s'agisse d'une courbe générée par un paramètre temporel unidimensionnel, elle explore l'espace de manière si dense qu'elle s'étend sur une zone d'espace bidimensionnel.

### La structure à grande échelle des galaxies (Cosmologie)

En regardant le ciel nocturne, les étoiles semblent dispersées au hasard, mais la cartographie tridimensionnelle de la distribution des galaxies à grande échelle dans l'univers (comme le Sloan Digital Sky Survey) révèle la « structure à grande échelle de l'univers » composée de superamas filamenteux et de vides immenses. L'analyse de la fonction de corrélation de cette distribution de la matière suggère qu'elle a une autosimilarité avec une dimension fractale $D \approx 1.2$ à $2.0$ à certaines échelles. L'auto-organisation de la matière due à la gravité crée des fractales.

### Réseaux de transport optimaux des alvéoles et des vaisseaux sanguins

Les fractales sont également omniprésentes dans le domaine de la biologie. Les poumons humains (structure de ramification des bronches), le système cardiovasculaire et le réseau neuronal du cerveau ont tous une structure fractale.
Pourquoi la sélection naturelle a-t-elle choisi les fractales ? Parce que c'est la solution optimale pour « emballer une surface infinie dans un volume fini (espace) ». En se ramifiant de manière fractale, les bronches maximisent la surface d'échange d'oxygène tout en maintenant constant le volume pulmonaire, et minimisent la perte d'énergie nécessaire pour acheminer le sang dans les moindres recoins des cellules du corps. Le mécanisme d'optimisation de la vie correspond parfaitement aux lois de la dimension fractale mathématique.

## Conclusion : Continuité des dimensions et nouvelle vision de la nature

Les « dimensions entières » que nous a données la géométrie euclidienne constituaient un modèle approximatif extrêmement utile pour que le cerveau humain simplifie et comprenne le monde. Cependant, les « fractales » et les « dimensions de Hausdorff » nées du développement de la théorie de la mesure et de l'intuition de Mandelbrot ont prouvé que la dimension ne prend pas des valeurs discrètes de $0, 1, 2, 3$, mais peut exister sous forme d'un continuum de nombres réels.

La dimension de Hausdorff est la jauge ultime pour quantifier la « rugosité », les « détails infinis » et « l'ordre caché dans le chaos » sous-jacents dans la nature. Des côtes, des arbres, de la foudre, de la structure de l'univers à la structure de notre propre corps, on peut dire que la fractale est le langage de conception universel de l'univers.

Le fait que la théorie de la mesure (mesure extérieure de Hausdorff), summum de l'abstraction mathématique, décrive avec autant de précision la réalité du monde physique, nous donne une forte impression de la correspondance mystérieuse qui existe entre les mathématiques et les sciences naturelles. La géométrie fractale a fondamentalement changé notre façon de voir le monde.
