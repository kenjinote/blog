---
title: "Le théorème des quatre couleurs et la révolution des mathématiques assistées par ordinateur : Un problème centenaire et la philosophie de la preuve par machine"
description: "L'histoire mathématique autour du problème de coloriage de cartes planes. De la fausse preuve de Kempe à la première preuve informatique de l'histoire par Appel & Haken, jusqu'à la redéfinition de la « beauté » mathématique."
slug: "four-color-theorem-computer-assisted-proof"
date: "2026-10-03T05:00:00+09:00"
categories: ["mathematics", "computer-science"]
tags: ["graph-theory", "combinatorics", "formal-proof", "mathematics-history"]
image: "eyecatch.jpg"
---

Dans l'histoire des mathématiques, l'un des théorèmes les plus célèbres et les plus controversés à la fois est le « Théorème des quatre couleurs » (Four Color Theorem). L'affirmation, assez simple pour être comprise par un élève d'école primaire, selon laquelle « pour colorier n'importe quelle carte plane de sorte que les régions adjacentes soient de couleurs différentes, quatre couleurs suffisent », a nécessité plus d'un siècle pour être prouvée, ainsi qu'un changement de paradigme fondamental pour les mathématiques : la « preuve par ordinateur ».

Dans cet article, nous explorerons de manière approfondie le théorème des quatre couleurs d'un point de vue mathématique, historique et philosophique, depuis la question naïve de 1852 jusqu'au sommet des mathématiques modernes avec l'ordinateur comme nouvelle intelligence alliée, en passant par les défis et les échecs des génies. En particulier, nous aborderons des sujets mathématiques profonds tels que la fausse preuve de Kempe et la structure géométrique du contre-exemple de Heawood, la preuve complète du théorème des cinq couleurs, les mathématiques de la méthode de déchargement, l'algorithme d'Appel et Haken, les détails de la preuve formelle par Coq et son lien avec la NP-complétude.

## Chapitre 1 : 1852, la question naïve de Francis Guthrie et son élévation à la théorie des graphes

### L'énoncé du problème de coloration de cartes
L'histoire commence en 1852 avec Francis Guthrie, un jeune homme qui venait d'obtenir son diplôme à l'University College de Londres. En coloriant une carte des comtés d'Angleterre, il a remarqué un fait curieux : « Quelle que soit la complexité d'une carte, quatre couleurs ne suffiraient-elles pas pour que les comtés voisins soient de couleurs différentes ? »

Francis a fait part de cette question à son frère, Frederick Guthrie, qui étudiait alors les mathématiques à l'University College. Frederick présenta ce problème à son directeur de thèse, Augustus De Morgan, l'un des mathématiciens les plus éminents de l'époque. De Morgan fut immédiatement attiré par l'intérêt du problème et le partagea dans une lettre avec son ami William Rowan Hamilton et d'autres. C'est à ce moment-là qu'est né le « Problème des quatre couleurs », brillant dans l'histoire des mathématiques.

### Le théorème des polyèdres d'Euler et la dualité des graphes planaires
Pour traiter mathématiquement et rigoureusement le problème de la coloration des cartes, sa formulation en théorie des graphes est indispensable. En considérant chaque région (pays ou comté) sur la carte comme un « Sommet » (Vertex) et en reliant les régions adjacentes par une « Arête » (Edge), on obtient un « Graphe planaire » (Planar Graph) où les arêtes ne se croisent pas sur le plan. Cette transformation est connue sous le nom de construction du « Graphe dual » (Dual Graph). Les frontières de la carte d'origine correspondent aux arêtes du graphe, et les faces aux sommets.

Le problème des quatre couleurs se réduit alors au Problème de coloration des sommets d'un graphe (Vertex Coloring Problem) : « Est-il possible de colorier les sommets d'un graphe planaire arbitraire avec 4 couleurs de sorte que les sommets adjacents soient de couleurs différentes ? »

Ici, le théorème des polyèdres découvert par Leonhard Euler joue un rôle extrêmement important. Dans un graphe planaire connexe, si le nombre de sommets est $V$, le nombre d'arêtes est $E$ et le nombre de faces est $F$, la relation invariante suivante est vérifiée :

$$V - E + F = 2$$

En combinant ce théorème avec les propriétés fondamentales des graphes planaires, nous pouvons en déduire de fortes contraintes sur la structure des graphes planaires. Supposons qu'il s'agisse d'un graphe simple sans arêtes multiples ni boucles, et considérons un « Graphe planaire maximal » (Maximal Planar Graph) où toutes les faces sont des triangles. Tout graphe planaire arbitraire peut être transformé en un graphe planaire maximal en ajoutant des arêtes sans augmenter son nombre chromatique, il suffit donc de prouver le théorème des quatre couleurs pour les graphes planaires maximaux.

Dans un graphe planaire maximal, chaque face est délimitée par exactement 3 arêtes. Étant donné qu'une arête délimite exactement deux faces, la relation suivante entre le nombre de faces et le nombre d'arêtes est strictement établie :

$$3F = 2E$$

En substituant cela dans la formule d'Euler pour éliminer $F$. En substituant $F = \frac{2}{3}E$ dans $V - E + F = 2$, on obtient :

$$V - E + \frac{2}{3}E = 2 \implies V - \frac{1}{3}E = 2 \implies 3V - E = 6 \implies E = 3V - 6$$

Dans un graphe planaire simple général, comme les faces sont limitées par 3 arêtes ou plus, on a $3F \leq 2E$, ce qui conduit à l'inégalité suivante :

$$E \leq 3V - 6$$

Cette inégalité montre qu'il existe une limite supérieure stricte à la densité des arêtes d'un graphe planaire. À partir de là, considérons le degré (Degree, $\deg(v)$) de chaque sommet. La somme des degrés de tous les sommets du graphe est exactement le double du nombre d'arêtes (Lemme des poignées de main).

$$\sum_{v \in V} \deg(v) = 2E$$

En utilisant l'inégalité précédente $2E \leq 6V - 12$,

$$\sum_{v \in V} \deg(v) \leq 6V - 12$$

En divisant les deux côtés par le nombre de sommets $V$, on obtient le degré moyen des sommets.

$$\frac{1}{V} \sum_{v \in V} \deg(v) \leq 6 - \frac{12}{V} < 6$$

Le fait que le degré moyen soit strictement inférieur à 6 prouve mathématiquement de manière complète qu'« au moins un sommet doit avoir un degré inférieur ou égal à 5 ». En d'autres termes, tout graphe planaire simple contient au moins un sommet dont le degré est 1, 2, 3, 4 ou 5. Ce fait est le point de départ le plus fondamental du concept de « configuration inévitable » décrit plus loin, et constitue la clé de voûte absolue de la preuve du théorème des quatre couleurs.

## Chapitre 2 : La « preuve » d'Alfred Kempe et son effondrement 11 ans plus tard

### Le concept des chaînes de Kempe et la brillante « preuve »
En 1879, Alfred Bray Kempe, un avocat et mathématicien britannique, publia enfin une « preuve » du problème des quatre couleurs dans les revues *Nature* et *American Journal of Mathematics*. Sa preuve était extrêmement originale et fut acceptée comme correcte par la communauté mathématique mondiale pendant 11 ans.

Le cœur de la preuve de Kempe reposait sur une idée révolutionnaire appelée aujourd'hui « Chaîne de Kempe » (Kempe Chain). Il a utilisé le raisonnement par récurrence mathématique. Il a supposé que le théorème des quatre couleurs était vrai pour tous les graphes planaires à $k$ sommets, et a tenté de montrer qu'il restait vrai pour les graphes à $k+1$ sommets.

D'après le théorème d'Euler mentionné précédemment, un graphe planaire $G$ à $k+1$ sommets possède toujours un sommet $v$ de degré inférieur ou égal à 5. Considérons le graphe $G'$ obtenu en retirant de $G$ le sommet $v$ et les arêtes qui y sont connectées. Puisque $G'$ a $k$ sommets, il peut être colorié avec 4 couleurs (disons rouge, bleu, vert et jaune) par hypothèse de récurrence. Ensuite, nous tentons de colorier $v$ après l'avoir réintégré.

1. **Cas où le degré de $v$ est inférieur ou égal à 3 :** $v$ a au plus 3 sommets adjacents. Par conséquent, au moins une des 4 couleurs n'est pas utilisée pour les sommets adjacents. Il suffit d'attribuer cette couleur inutilisée à $v$ pour achever la preuve.
2. **Cas où le degré de $v$ est 4 :** Supposons que les 4 sommets adjacents à $v$ (nommés $v_1, v_2, v_3, v_4$ dans le sens des aiguilles d'une montre) soient coloriés avec 4 couleurs différentes (rouge, bleu, vert, jaune). Considérons alors le sous-graphe obtenu en n'extrayant de l'ensemble du graphe que les sommets coloriés en « rouge » et en « vert » et les arêtes qui les relient. Si $v_1$ (rouge) et $v_3$ (vert) ne sont pas connectés au sein de ce sous-graphe rouge-vert (c'est-à-dire qu'il n'y a pas de chemin reliant $v_1$ à $v_3$ en passant par des sommets rouges et verts), nous pouvons inverser les couleurs (rouge en vert, vert en rouge) de la composante connexe contenant $v_1$. C'est ce qu'on appelle « l'inversion de la chaîne de Kempe ». Après l'inversion, $v_1$ devient vert, et les couleurs autour de $v$ sont réduites à 3 : bleu, vert, vert, jaune. Il est alors possible de peindre $v$ en rouge. Si $v_1$ et $v_3$ sont connectés, alors en vertu des propriétés topologiques des graphes planaires (théorème de Jordan sur les courbes fermées), le chemin rouge-vert reliant $v_1$ et $v_3$ sépare $v_2$ (bleu) et $v_4$ (jaune). Par conséquent, $v_2$ et $v_4$ ne peuvent absolument pas être reliés par une chaîne bleue-jaune, et nous pouvons inverser la composante bleu-jaune contenant $v_2$. Dans les deux cas, le nombre de couleurs autour de $v$ peut être réduit à 3, et $v$ peut être colorié.
3. **Cas où le degré de $v$ est 5 :** Supposons que les 5 sommets $v_1, v_2, v_3, v_4, v_5$ autour de $v$ soient coloriés respectivement en rouge, bleu, vert, jaune, rouge (puisqu'il y a 5 sommets, une couleur est doublée). Kempe a étendu l'argument du cas de degré 4 et a affirmé qu'en combinant habilement l'inversion de deux chaînes de Kempe différentes (par exemple, une chaîne rouge-vert et une chaîne rouge-jaune), il est toujours possible de réduire les couleurs autour de $v$ à 3 ou moins. Sa méthode consistait à appliquer doublement la logique selon laquelle si l'une est connectée, l'autre est séparée.

Cette preuve était intuitive et élégante, et semblait exempte de toute faille logique. Les mathématiciens de l'époque étaient convaincus que le problème des quatre couleurs était complètement résolu.

### Le graphe contre-exemple de Heawood : La faille fatale du « croisement de la double chaîne de Kempe »
Cependant, en 1890, un mathématicien alors âgé de 29 ans, Percy John Heawood, lut attentivement l'article de Kempe et découvrit une faille logique fatale dans l'argument concernant les sommets de degré 5.

Kempe avait implicitement supposé que lors de l'inversion séparée de deux chaînes de Kempe (par exemple, une chaîne bleu-vert et une chaîne bleu-jaune), elles pouvaient être inversées indépendamment l'une de l'autre. Mais Heawood prouva géométriquement et rigoureusement que si ces deux chaînes partagent certains sommets, inverser la première chaîne modifie l'état de coloration du graphe, ce qui altère la connectivité de la seconde chaîne.

Heawood a construit un graphe contre-exemple spécifique (connu aujourd'hui sous le nom de « Graphe de Heawood » (Heawood graph) ou ses dérivés, un graphe planaire maximal de 25 sommets). Il a montré que si l'on applique l'algorithme de Kempe pour réduire les couleurs autour d'un sommet $v$ de degré 5 dans ce graphe, au moment où la chaîne bleu-vert est inversée, la chaîne bleu-jaune (qui n'était pas connectée à l'origine) devient connectée. Si l'on essaie ensuite d'inverser la chaîne bleu-jaune, le sommet vert qui vient d'être inversé retrouve sa couleur d'origine, conduisant à une boucle où le nombre de couleurs ne diminue pas.

L'« inversion simultanée d'une double chaîne de Kempe » de Kempe était une erreur résultant d'une sous-estimation de l'enchevêtrement complexe des graphes planaires, qui ne permettait pas de maintenir globalement la relation de séparation topologique locale. À cause de cette découverte, la preuve du théorème des quatre couleurs de Kempe s'est complètement effondrée.

### La preuve mathématique complète du théorème des cinq couleurs
La preuve de Kempe s'était effondrée, mais Heawood ne s'est pas contenté de la détruire. Il a reconnu que l'idée même de Kempe (la chaîne de Kempe) était extrêmement utile, et l'a utilisée pour prouver rigoureusement le « Théorème des cinq couleurs » (Five Color Theorem) : « tout graphe planaire peut toujours être colorié avec 5 couleurs ». Le processus complet de preuve du théorème des cinq couleurs est le suivant :

**Théorème :** Tout graphe planaire arbitraire $G$ est coloriable avec 5 couleurs.
**Preuve :** Utilisons le raisonnement par récurrence sur le nombre de sommets $n$.
Pour $n \leq 5$, c'est trivial. Supposons que tous les graphes planaires pour $n=k$ soient coloriables avec 5 couleurs, et considérons un graphe planaire $G$ pour $n=k+1$.
D'après un fait déduit de la formule d'Euler, il existe toujours un sommet $v$ de degré inférieur ou égal à 5 dans $G$.
Puisque le graphe $G' = G - \{v\}$ obtenu en supprimant $v$ de $G$ a $k$ sommets, il peut être colorié avec 5 couleurs (couleur 1, couleur 2, couleur 3, couleur 4, couleur 5) par hypothèse de récurrence.
Considérons le fait de remettre $v$ en conservant le coloriage de $G'$.
- **Cas 1 : $\deg(v) < 5$.** Les sommets adjacents à $v$ sont au plus 4, donc au moins une des 5 couleurs n'est pas utilisée pour les sommets adjacents. Il suffit de colorier $v$ avec cette couleur.
- **Cas 2 : $\deg(v) = 5$.** Supposons que les 5 sommets $v_1, v_2, v_3, v_4, v_5$ adjacents à $v$ (disposés dans le sens des aiguilles d'une montre) soient tous de couleurs différentes (couleur 1, couleur 2, couleur 3, couleur 4, couleur 5 respectivement). (Si la même couleur est utilisée plus d'une fois, il restera au moins une couleur inutilisée qui pourra être appliquée à $v$).
Dans le graphe $G'$, considérons le sous-graphe induit composé uniquement de sommets coloriés de la couleur 1 et de la couleur 3, et soit $C_{13}$ la composante connexe contenant $v_1$ dans ce sous-graphe (c'est une chaîne de Kempe).
  - **Sous-cas 2a : $v_3 \notin C_{13}$.** C'est-à-dire qu'il n'existe pas de chemin de $v_1$ à $v_3$ passant uniquement par des sommets de couleur 1 et de couleur 3. Dans ce cas, même si toutes les couleurs des sommets dans $C_{13}$ sont inversées (couleur 1 $\leftrightarrow$ couleur 3), la validité de la coloration est conservée. Après l'inversion, $v_1$ devient de couleur 3, et $v_3$ est aussi de couleur 3, la couleur 1 n'est donc plus présente autour de $v$. Ainsi, on peut peindre $v$ avec la couleur 1.
  - **Sous-cas 2b : $v_3 \in C_{13}$.** C'est-à-dire qu'il existe un chemin $P_{13}$ reliant $v_1$ et $v_3$ composé de sommets de couleur 1 et de couleur 3. Si l'on combine ce chemin $P_{13}$ avec le sommet $v$ et les arêtes $(v, v_1), (v, v_3)$, on forme une courbe fermée (cycle) sur le plan. Par les propriétés des graphes planaires (théorème de Jordan sur les courbes fermées), ce cycle sépare le plan en un intérieur et un extérieur.
  Les sommets $v_2$ et $v_4$ sont situés de part et d'autre de ce cycle (l'un à l'intérieur, l'autre à l'extérieur).
  Considérons maintenant la chaîne de Kempe $C_{24}$ composée de sommets coloriés de la couleur 2 et de la couleur 4. Si l'on suppose que $v_2$ et $v_4$ sont reliés par cette chaîne, il doit exister un chemin $P_{24}$ reliant $v_2$ et $v_4$. Cependant, bien que $P_{24}$ doive parcourir le graphe planaire sans se croiser, il ne peut pas traverser le cycle formé par $P_{13}$ (cela contredirait la définition d'un graphe planaire).
  Par conséquent, il n'existe absolument aucun chemin de couleurs 2 et 4 reliant $v_2$ et $v_4$. Autrement dit, la chaîne de Kempe couleur 2-couleur 4 $C_{24}$ contenant $v_2$ ne contient pas $v_4$.
  Ainsi, si l'on inverse les couleurs dans $C_{24}$ (couleur 2 $\leftrightarrow$ couleur 4), $v_2$ devient de couleur 4, et la couleur 2 disparaît du contour de $v$. Finalement, on peut peindre $v$ avec la couleur 2.

À travers cela, $v$ peut être colorié dans tous les cas, et le théorème des cinq couleurs a été complètement prouvé par récurrence mathématique. $\blacksquare$

Cette preuve utilise de manière extrêmement élégante la topologie des graphes planaires (le théorème des courbes fermées de Jordan) et montre à quel point le concept de « chaîne de Kempe » introduit par Kempe est robuste lorsqu'il est appliqué à une seule chaîne non sécante. Cependant, le chemin vers les « 4 couleurs » passera d'ici par un nouveau paradigme de « réductibilité » et d'« ensemble inévitable », plongeant dans un océan de calculs vertigineux.

## Chapitre 3 : Les mathématiques de la méthode de déchargement (Discharging Method) et la dérivation des configurations inévitables

Après Heawood, les mathématiciens ont supposé l'existence d'un « plus petit contre-exemple (Minimum Counterexample) non coloriable en 4 couleurs », et ont commencé à explorer, par l'absurde, la structure qu'il devrait (ou ne devrait pas) avoir. C'est ici que deux concepts puissants entrent en jeu : la « Configuration réductible (Reducible Configuration) » et l'« Ensemble inévitable (Unavoidable Set) ».

### Réductibilité (Reducibility)
Une configuration réductible est une sous-configuration locale (un motif) de sommets telle que « si le graphe entier n'est pas coloriable avec quatre couleurs (c'est le plus petit contre-exemple), il est absolument impossible qu'elle existe au sein de ce graphe ».
Par exemple, un « sommet de degré 3 ou moins » ou un « sommet de degré 4 » est une configuration réductible. En effet, comme mentionné précédemment, si l'on utilise la réduction par les chaînes de Kempe, leur présence permettrait de réduire le problème à un graphe plus petit, contredisant ainsi l'hypothèse selon laquelle il s'agit du « plus petit contre-exemple ».
En 1913, George David Birkhoff a prouvé qu'une configuration spécifique de 6 sommets, connue sous le nom de « Diamant de Birkhoff », était également réductible. La découverte de configurations réductibles a progressé, mais tant qu'on ne pouvait pas garantir qu'elles « doivent exister » dans le graphe, la preuve ne pouvait être aboutie.

### Structure mathématique de la méthode de déchargement (Discharging Method)
La stratégie finale pour prouver le théorème des quatre couleurs se résume à **« trouver un ensemble inévitable dont tous les éléments sont des configurations réductibles »**.
Un ensemble inévitable est une liste de configurations telle que « tout graphe planaire (ou plus précisément, un graphe planaire maximal) contient toujours au moins l'une des configurations de cet ensemble ».

Une arme extrêmement puissante pour construire et prouver l'existence de cet ensemble inévitable est la « Méthode de déchargement (Discharging Method) », raffinée par Heinrich Heesch. La méthode de déchargement est une technique magique pour prouver des théorèmes structurels dans la théorie des graphes, utilisant le concept de charge de l'électromagnétisme comme analogie.

Le processus mathématique de la méthode de déchargement est le suivant :
1. **Attribution de la charge initiale :**
   Pour chaque sommet $v$ d'un graphe planaire maximal, on attribue une charge initiale (Initial Charge) $ch(v)$ de la façon suivante :
   $$ch(v) = 6 - \deg(v)$$
   D'après l'équation $\sum_{v} (6 - \deg(v)) = 12$ déduite de la formule d'Euler, la somme totale des charges initiales du graphe entier est strictement de 12 (valeur positive).
   Ainsi, les sommets de degré 5 ont une charge de $+1$, les sommets de degré 6 de $0$, et les sommets de degré 7 ou plus ont une charge négative. (Étant donné qu'on peut supposer qu'il n'y a pas de sommets de degré inférieur ou égal à 4 dans le plus petit contre-exemple, le degré minimum est considéré comme étant 5).

2. **Définition des règles de transfert de charge (Discharging Rules) :**
   Ensuite, nous définissons des règles pour déplacer les charges entre les sommets adjacents. L'idée de base est de « faire couler (décharger) la charge des sommets avec une charge positive (c'est-à-dire les sommets de degré 5) vers les sommets avec une charge négative (sommets de haut degré, de degré 7 ou plus) ».
   Par exemple, des dizaines ou des centaines de règles spécifiques sont établies, telles que : « Si un sommet $v$ de degré 5 est adjacent à un sommet $u$ de degré 7, déplacer une charge de $\frac{1}{5}$ de $v$ vers $u$ ».

3. **Déduction d'une contradiction et identification des configurations inévitables :**
   Conformément aux règles définies, on effectue tous les déplacements de charges (Discharging). Étant donné que le mouvement des charges n'est qu'un transfert à l'intérieur du graphe, la somme totale de la charge reste à 12 (positive) même après les transferts.
   $$ \sum_{v \in V} ch'(v) = 12 > 0 $$
   ($ch'(v)$ est la charge du sommet $v$ après transfert)
   Le fait que la somme totale soit positive signifie que **« même après le transfert de charge, il doit y avoir au moins un sommet avec une charge positive »**.

   On analyse alors la charge finale $ch'(v)$ de chaque sommet en fonction de sa structure locale (le motif des degrés de ce sommet et des sommets qui lui sont adjacents). Si on peut prouver que « tout sommet qui ne possède pas une certaine configuration spécifique aura toujours une charge finale inférieure ou égale à zéro selon les règles de déchargement établies », alors pour que la charge finale soit positive, cette « configuration spécifique » doit obligatoirement exister quelque part dans le graphe.
   C'est ainsi qu'une liste exhaustive de modèles de configuration locale conduisant à une charge finale positive constitue un « ensemble inévitable ».

Heesch était convaincu qu'en utilisant cette méthode de déchargement, un ensemble inévitable composé d'un nombre fini (probablement quelques milliers) de configurations réductibles pourrait être construit. Cependant, la complexité de calcul pour déterminer si une configuration est « réductible » explose de manière exponentielle par rapport à la longueur de sa frontière. Il était impossible pour un être humain de vérifier la réductibilité de milliers de configurations à la main, même en y consacrant toute sa vie.

## Chapitre 4 : 1976, l'algorithme de vérification informatique d'Appel et Haken

### Définition de la D-réduction et de la C-réduction
Dans les années 1970, Kenneth Appel et Wolfgang Haken de l'Université de l'Illinois ont lancé un projet historique visant à fusionner la méthode de déchargement de Heesch avec la puissance de calcul des ordinateurs.

La tâche la plus lourde en termes de calcul à laquelle ils se sont attaqués était la « détermination de la réductibilité » des configurations. Il existe principalement deux types de réductibilité :
- **D-réductibilité (D-reducibility / Direct reducibility) :** Pour tous les motifs de coloration possibles en 4 couleurs sur la limite annulaire (Ring) entourant une configuration, on vérifie si la coloration peut s'étendre à l'intérieur de la configuration, ou s'il est possible de la transformer en un motif extensible à l'intérieur en inversant des chaînes de Kempe des couleurs de la limite. Si cela est confirmé, on peut immédiatement affirmer que la configuration n'est pas incluse dans le plus petit contre-exemple.
- **C-réductibilité (C-reducibility / Contracting reducibility) :** S'il y a des motifs qui échouent au test de D-réductibilité, on envisage un graphe plus petit où une partie de la configuration est « contractée (plusieurs sommets sont réduits en un seul) », et on montre que si le graphe contracté est coloriable en 4 couleurs, le graphe d'origine l'est également.

### Algorithme de vérification de la colorabilité de la frontière annulaire
L'ordinateur (un IBM 360) a été chargé d'exécuter des algorithmes pour déterminer la D-réductibilité et la C-réductibilité sur un grand nombre de configurations candidates.

Supposons qu'une configuration $C$ ait un anneau frontière $R$ (de longueur $k$). Le nombre de combinaisons pour colorier les sommets de l'anneau avec 4 couleurs est au maximum de $4^k$, mais même en tenant compte de la symétrie, ce nombre est énorme. Par exemple, pour une longueur d'anneau $k=14$, il faut vérifier la validité d'environ 200 000 colorations de frontières.
L'algorithme se déroule comme suit :
1. Générer l'ensemble de tous les motifs de coloration valides en 4 couleurs pour l'anneau frontière $R$.
2. Essayer toutes les façons de colorier l'intérieur de la configuration $C$ avec 4 couleurs, et enregistrer avec quels motifs de frontière elles sont compatibles (si elles sont extensibles à l'intérieur).
3. Pour les motifs de frontière non extensibles à l'intérieur, simuler l'inversion de chaînes de Kempe. Si l'inversion permet de passer à un motif déjà identifié comme « extensible à l'intérieur », le motif initial est également considéré comme « résolu ».
4. Répéter cette recherche de transitions d'inversion, et si tous les motifs de frontière peuvent être résolus, déclarer la configuration $C$ comme « D-réductible ».

Comme le temps de calcul explose avec la longueur de la frontière, Appel et Haken se sont limités aux configurations avec un anneau de longueur maximale de 14, et ont ajusté de manière exhaustive les règles de déchargement pour construire un ensemble inévitable. Ce processus de réglage en soi fut une suite d'essais et d'erreurs colossaux impliquant des humains et un ordinateur. Le processus interactif « les humains modifient les règles de déchargement, l'ordinateur propose des candidats d'ensemble inévitable, teste la réductibilité, et face aux configurations ayant échoué, les humains modifient à nouveau les règles » s'est poursuivi pendant plusieurs années.

### 1200 heures de calcul et le « Q.E.D. »
En 1976, ils ont finalement découvert un ensemble inévitable composé de **1 936 configurations**, dérivé de règles de déchargement finement construites. Puis, après plus de 1200 heures de fonctionnement sur le mainframe de l'Université de l'Illinois, l'ordinateur a confirmé que les 1 936 configurations étaient toutes D-réductibles ou C-réductibles.

Ils ont brièvement écrit dans le résumé de leur article :
*"Every planar map is four colorable."*

Le tampon postal du département de mathématiques de l'Université de l'Illinois arborait fièrement l'inscription « FOUR COLORS SUFFICE (4 couleurs suffisent) ». Ce fut le premier événement monumental dans l'histoire des mathématiques où un ordinateur assumait l'étape de déduction centrale de la preuve d'un théorème.

## Chapitre 5 : Le choc dans la communauté mathématique et la philosophie de la « preuve »

L'annonce d'Appel et Haken a suscité plus de profonde perplexité et de vives controverses au sein de la communauté mathématique que de joie.

### Une preuve illisible par l'homme est-elle des mathématiques ?
Dans la tradition mathématique remontant à la Grèce antique, une « preuve » était quelque chose que les mathématiciens humains pouvaient suivre étape par étape, comprendre du fond du cœur et dont ils pouvaient se convaincre de la validité. On croyait que le processus de preuve abritait un discernement profond quant à « pourquoi le théorème est vrai » et à la beauté de sa structure.

Cependant, la preuve du théorème des quatre couleurs était d'une autre nature. L'article contenait seulement une liste de 1 936 configurations et une explication de l'algorithme informatique. La trace réelle (enregistrement de l'exécution) de la détermination de la réductibilité était si énorme qu'il était même difficile de l'imprimer sur papier. Aucun génie mathématique, même en y consacrant toute sa vie, ne pourrait suivre ces calculs à la main et vérifier qu'il n'y avait aucune faille logique.

Il est apparu une situation inédite : « pour croire en la justesse de la preuve, il fallait croire que le matériel informatique n'était pas défectueux et qu'il n'y avait pas de bugs dans le programme en langage assembleur écrit par Appel et Haken ».

Le philosophe des sciences Thomas Tymoczko a critiqué le fait que cette preuve pourrait représenter une dégradation des mathématiques pures, passant d'une quête aprioriste de la vérité à une démarche empirique et expérimentale similaire à celle de la physique. La définition même de l'acte de « prouver » a été confrontée à une crise épistémologique.

### Réfutations et simplification par le groupe RSST
Appel et Haken ont répondu aux critiques en affirmant : « Les mathématiques ne se limitent pas à de belles preuves. S'il existe des problèmes intrinsèquement complexes nécessitant une catégorisation massive qui dépasse les limites du cerveau humain, recourir à la machine est une évolution inévitable. »

Afin de dissiper ce malaise, de nombreux mathématiciens ont tenté de simplifier et de vérifier à nouveau la preuve. En 1997, quatre personnes, Neil Robertson, Daniel P. Sanders, Paul Seymour et Robin Thomas (connus sous l'acronyme RSST), ont publié une nouvelle preuve dans laquelle la méthode de déchargement a été améliorée pour devenir plus systématique et plus facile à vérifier par l'homme, réduisant la taille de l'ensemble inévitable de 1 936 à 633 configurations. Leur algorithme était raffiné et ne nécessitait que quelques heures de calcul.

Cependant, cette approche reste fondamentalement tributaire du « calcul de la réductibilité par ordinateur ». Une « belle preuve sur papier et au stylo », entièrement compréhensible par l'intuition humaine, reste encore à trouver (et de nombreux experts en théorie des graphes pensent qu'une telle preuve n'existe pas en principe).

## Chapitre 6 : La preuve formelle complète de Georges Gonthier avec Coq

Comment faire pour dissiper complètement, d'un point de vue mathématique, la crainte qu'« il pourrait y avoir des bugs dans le programme » ? La réponse ultime à cela est la Formalisation complète (Formalization) en utilisant un « Assistant de preuve » (Proof Assistant).

En 2005, Georges Gonthier de l'Institut National de Recherche en Informatique et en Automatique (INRIA) et de Microsoft Research, en collaboration avec Benjamin Werner, a réussi à formaliser de fond en comble la preuve du théorème des quatre couleurs à l'aide de l'assistant de preuve « Coq ».

### Cartes finies non standard (Hypermap) et formalisation de la topologie combinatoire
Coq est un système qui part des axiomes mathématiques pour décrire et vérifier mécaniquement les preuves en suivant un système de règles logiques extrêmement strict (Calculus of Inductive Constructions : Calcul des Constructions Inductives).

L'un des plus grands accomplissements de Gonthier a été de traduire l'objet intuitif et géométrique qu'est un graphe planaire en une structure entièrement algébrique et combinatoire que l'ordinateur peut manipuler. Pour exprimer les relations entre les sommets, les arêtes et les faces d'un graphe, il a défini une structure de données appelée « Hypermap ». C'est une méthode permettant de représenter un graphe comme un ensemble de « fléchettes » (demi-arêtes) et un groupe de permutations sur celles-ci. Ainsi, les théorèmes de topologie tels que la formule d'Euler et le théorème des courbes fermées de Jordan ont été entièrement formalisés en tant que logique combinatoire de la théorie des groupes et des ensembles finis.

### La preuve d'exactitude du programme de preuve lui-même
De plus, Gonthier a écarté le « programme de vérification écrit en C » utilisé par Appel-Haken et RSST, et a implémenté l'algorithme de détermination de réductibilité lui-même en utilisant le langage interne de Coq (Gallina). Ensuite, **il a prouvé mathématiquement dans Coq la justesse même de l'algorithme en affirmant que « si cet algorithme de détermination renvoie "True", alors la configuration est véritablement réductible »**.

Grâce à cela, la fiabilité de la preuve a été radicalement modifiée. Il n'y avait plus besoin de s'inquiéter des « bugs dans l'algorithme ». En effet, tant que le noyau de vérification logique au cœur de Coq (qui est un code extrêmement simple et robuste de quelques centaines de lignes, implémenté à l'aide d'indices de De Bruijn) traite correctement les règles d'inférence logique, l'énorme arbre de preuve construit par Gonthier est mathématiquement garanti comme étant absolument correct.

Il s'agit là d'un nouveau sommet pour les « preuves » mathématiques. C'est l'évolution d'une « preuve lue et comprise par l'homme (Informal Proof) » vers une « preuve formelle dont la complétude logique est garantie par la machine (Formal Proof) ». Le théorème des quatre couleurs est devenu le premier théorème majeur non trivial de l'histoire à atteindre ce niveau de rigueur ultime.

## Chapitre 7 : Le problème de coloration en 4 couleurs des graphes planaires et le paradoxe de la NP-complétude

Enfin, examinons le théorème des quatre couleurs du point de vue de la théorie de la complexité algorithmique (Computational Complexity Theory). Il existe ici un phénomène extrêmement intéressant qui ressemble à un paradoxe.

Le problème de la coloration pour un graphe général (problème de décision consistant à déterminer si un graphe donné peut être colorié avec $k$ couleurs) est l'un des problèmes les plus célèbres de « NP-complet » (NP-complete) en informatique. En particulier, le « Problème de coloration en 3 couleurs des graphes planaires (Planar 3-Colorability) » a été prouvé NP-complet. Cela signifie qu'à moins que $\text{P} = \text{NP}$, il n'existe pas d'algorithme capable de déterminer en temps polynomial si un graphe planaire donné est coloriable en 3 couleurs.

Alors, qu'en est-il du « Problème de coloration en 4 couleurs des graphes planaires (Planar 4-Colorability) » ? On pourrait intuitivement penser que si 3 couleurs sont NP-complet, 4 couleurs doivent également être difficiles (NP-complet).

Cependant, de manière surprenante, **la complexité algorithmique du problème de coloration en 4 couleurs pour les graphes planaires (problème de décision) est de $O(1)$, c'est-à-dire en « temps constant (trivial) ».**
La raison en est que le théorème des quatre couleurs garantit que « tous les graphes planaires peuvent être coloriés avec 4 couleurs » ; par conséquent, l'algorithme n'a même pas besoin de regarder le graphe en entrée et peut simplement renvoyer « Oui » pour avoir toujours raison à 100 %. C'est un bel exemple où la garantie puissante de l'existence issue d'un théorème réduit la complexité du problème de décision à sa limite absolue.

Cependant, cela ne concerne que le problème de décision (Decision Problem) : « peut-on le colorier ? ». **Construire un algorithme de coloration (Search Problem)** qui indique « comment le colorier concrètement avec 4 couleurs » est une autre histoire.
Si l'on implémente la procédure de preuve d'Appel-Haken ou de RSST sous forme d'algorithme, on obtient un algorithme capable de trouver concrètement une coloration en 4 couleurs pour un graphe planaire de $N$ sommets donné. L'algorithme basé sur la preuve RSST s'exécute en un temps polynomial avec une complexité dans le pire des cas de $O(N^2)$.

Autrement dit, alors que tenter de colorier un graphe planaire avec 3 couleurs pourrait nécessiter un temps comparable à la durée de vie de l'univers (NP-complet), dès l'instant où l'on ajoute une quatrième couleur, grâce à la structure mathématique sous-jacente au théorème des quatre couleurs, un algorithme rapide (en $O(N^2)$) existe. C'est un fait extrêmement mystérieux et fascinant qui se situe à l'intersection des mathématiques et de l'informatique.

## Conclusion : L'héritage du théorème des quatre couleurs

Le problème naïf de coloration de carte soulevé par un jeune Anglais en 1852 n'était au départ qu'un simple puzzle. Cependant, plus d'un siècle plus tard, il a ouvert la voie à un vaste nouveau domaine mathématique qu'est la théorie des graphes, a contribué au développement de la théorie des algorithmes, et a finalement confronté l'humanité à des questions philosophiques fondamentales : « Les ordinateurs peuvent-ils faire des preuves mathématiques ? » et « Qu'est-ce que la vérité mathématique ? ».

L'histoire du théorème des quatre couleurs est celle d'un croisement intense entre les limites de l'intuition humaine et les possibilités d'un nouveau moteur logique, la machine. Aujourd'hui, d'autres problèmes majeurs et colossaux, tels que la conjecture de Kepler (projet Flyspeck par Thomas Hales en 2014) et le théorème de Feit-Thompson, ont également été entièrement prouvés par vérification formelle à l'aide d'assistants de preuve.

Lorsque nous colorions nonchalamment une carte avec 4 couleurs, on y retrouve, superposés les uns aux autres, l'esthétique des polyèdres d'Euler, l'échec brillant de Kempe, la réfutation rigoureuse de Heawood, les mathématiques du déchargement de Heesch, la trace des calculs de superordinateurs clignotant sans relâche pendant des milliers d'heures, et la logique des hypermaps de Coq. Le théorème des quatre couleurs continuera d'être raconté comme la meilleure étude de cas illustrant comment les mathématiques s'étendent au-delà des limites de la pensée humaine.
