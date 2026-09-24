---
title: "Théorie de Ramsey : l'ordre émerge inévitablement du désordre — Démonstration par coloriage des relations entre 6 personnes"
description: "Dans un groupe de 6 personnes, il existe toujours 3 personnes qui se connaissent toutes mutuellement ou 3 personnes qui ne se connaissent pas du tout. Démonstration du nombre de Ramsey R(3,3) = 6 par les graphes bicolores, contre-exemple à 5 personnes, vérification des 32 768 configurations, et applications aux suites et aux réseaux."
date: "2026-09-24T16:08:36+09:00"
image: "eyecatch.jpg"
categories: ["mathematics"]
tags: ["Théorie de Ramsey", "Théorie des graphes", "Combinatoire", "Principe des tiroirs", "Python"]
slug: "ramsey-theory"
math: true
---

## 1. Dès que 6 personnes se réunissent, un trio remarquable apparaît obligatoirement

Imaginons que 6 personnes se réunissent lors d'une soirée. Certaines se connaissent depuis longtemps, d'autres se rencontrent pour la première fois. La configuration des relations peut être aussi complexe et désordonnée que l'on veut. Pourtant, l'une des deux situations suivantes se produit obligatoirement :

- **Il existe 3 personnes qui se connaissent toutes mutuellement deux à deux.**
- **Il existe 3 personnes qui ne se connaissent absolument pas deux à deux (chacune ignore les deux autres).**

Il ne s'agit pas d'un phénomène qui se produit « la plupart du temps ». Quelle que soit la manière dont les relations sont tissées, cela se produit sans aucune exception. De plus, le nombre de 6 personnes est minimal : avec 5 personnes, il est tout à fait possible de concevoir une configuration où aucun de ces deux types de trios n'apparaît.

Cette surprenante observation constitue la porte d'entrée de la **théorie de Ramsey**. Quelle que soit la complexité avec laquelle on partitionne une vaste structure, si celle-ci est suffisamment grande, il devient impossible d'éviter l'apparition d'une sous-structure régulière vérifiant certaines conditions. C'est l'étude de cette « régularité inévitable ».

Cela ne signifie pas pour autant que n'importe quelle règle arbitraire surgit du désordre. Pour formuler un énoncé mathématique rigoureux, il faut définir précisément les objets considérés, le nombre de catégories de classification et le motif recherché. Commençons par un exemple concret que l'on peut tracer sur une feuille de papier avec 6 points.

## 2. Modéliser les relations humaines par des arêtes rouges et bleues

### Les conventions du modèle

Dans cet article, nous considérons la relation « se connaître » comme symétrique : si A connaît B, alors B connaît également A. Chaque paire d'individus est obligatoirement classée dans l'une de ces deux catégories : « se connaissent » ou « ne se connaissent pas ».

Les relations asymétriques (par exemple, connaître quelqu'un de réputation sans réciprocité) ou incertaines sont exclues de ce modèle. De plus, « ne pas se connaître » ne signifie aucunement « se détester » ou « être hostile ».

Représentons chaque personne par un point et la relation entre deux personnes par un segment (une arête).

| Élément du schéma | Signification |
|---|---|
| Point (sommet) | Un participant |
| Ligne continue rouge | Les deux personnes se connaissent mutuellement |
| Ligne pointillée bleue | Les deux personnes ne se connaissent pas |
| Triangle formé de 3 arêtes de même couleur | Le trio recherché |

Comme chaque paire possible de personnes est reliée par une arête, il s'agit d'un **graphe complet**. On note $K_n$ le graphe complet à $n$ sommets, dont le nombre d'arêtes est donné par :

$$
\binom{n}{2}=\frac{n(n-1)}{2}
$$

Pour 6 personnes, il y a 15 arêtes. Le fait que « A connaisse B et C » ne suffit pas pour que les 3 personnes se connaissent toutes mutuellement : il faut aussi que l'arête entre B et C soit rouge. N'oubliez pas cette condition essentielle : **les 3 arêtes** du triangle doivent avoir la même couleur.

Dans la suite de cet article, nous appellerons **triangle monochromatique** un triangle dont toutes les arêtes sont entièrement rouges ou entièrement bleues. Afin de faciliter la lecture même en cas de difficulté à distinguer les couleurs, les arêtes rouges sont représentées par des traits continus et les arêtes bleues par des traits pointillés dans les figures.

## 3. Démonstration de l'existence inévitable pour 6 personnes

Le seul outil nécessaire à cette démonstration est le [principe des tiroirs](../pigeonhole-principle-hash-collision/). Nous nous appuyons sur une vérité élémentaire : « si l'on répartit 5 objets en 2 catégories, au moins l'une des catégories en contient au moins 3 ».

### Étape 1 : Se concentrer sur une seule personne

Prenons une personne quelconque parmi les 6, appelons-la A. Du sommet A partent 5 arêtes vers les 5 autres personnes. Comme chaque arête est soit rouge soit bleue, il y a nécessairement au moins 3 arêtes de la même couleur :

$$
\left\lceil\frac{5}{2}\right\rceil=3
$$

Ici, $\lceil x\rceil$ désigne la fonction partie entière par excès (le plus petit entier supérieur ou égal à $x$). On peut également raisonner ainsi : si le nombre d'arêtes rouges et le nombre d'arêtes bleues étaient tous deux inférieurs ou égaux à 2, leur somme ne dépasserait pas 4, ce qui ne permettrait pas de colorier 5 arêtes.

Supposons qu'il y ait au moins 3 arêtes rouges, et appelons B, C et D les trois personnes situées à leurs extrémités. Les arêtes A–B, A–C et A–D sont donc toutes rouges. Si, au départ, nous avions obtenu au moins 3 arêtes bleues, le raisonnement serait exactement le même en échangeant simplement les rôles du rouge et du bleu.

### Étape 2 : Examiner les relations entre B, C et D

Considérons à présent les 3 arêtes reliant B, C et D entre eux : B–C, B–D et C–D. Deux cas seulement sont possibles :

**Cas 1 : Il y a au moins une arête rouge.** Par exemple, si B–C est rouge, comme A–B et A–C sont également rouges, le triplet A, B, C forme un triangle entièrement rouge. Peu importe alors la couleur des deux autres arêtes.

**Cas 2 : Il n'y a aucune arête rouge.** Alors B–C, B–D et C–D sont toutes les trois bleues. Dès lors, le triplet B, C, D forme un triangle entièrement bleu.

![Schéma de démonstration : en partant de 3 arêtes de même couleur issues de A, la présence d'une arête rouge entre les 3 voisins forme un triangle rouge, et son absence forme un triangle bleu](six-person-proof.svg)

Dans ce schéma, les arêtes grises et les arêtes omises correspondent à celles dont la couleur n'a pas besoin d'être fixée pour la démonstration. Dans un véritable graphe complet, chacune d'entre elles est bel et bien rouge ou bleue.

Nous venons ainsi de démontrer que, quel que soit le coloriage, il existe toujours un triangle monochromatique. Il n'est nullement nécessaire d'examiner l'ensemble des 15 arêtes : **les 5 arêtes issues d'un seul sommet et les relations entre les 3 voisins associés suffisent à couvrir l'intégralité des possibilités**. [Support pédagogique universitaire (en anglais)](https://ximera.osu.edu/math/combinatorics/combinatoricsBook/combinatoricsBook/combinatorics/ramseyTheory/ramseyTheory)

## 4. Pourquoi 5 personnes ne suffisent-elles pas ?

Affirmer que « 6 personnes suffisent » et que « 6 est le minimum » sont deux propositions distinctes. Pour prouver que 6 est le minimum, il est nécessaire de construire un contre-exemple avec 5 personnes ne satisfaisant pas la condition (aucun triangle monochromatique).

Plaçons 5 personnes aux sommets d'un pentagone régulier. Colorions en rouge les arêtes reliant les personnes adjacentes, c'est-à-dire les 5 arêtes du pourtour du pentagone. Colorions en bleu les 5 diagonales restantes.

![Contre-exemple à 5 personnes : le pourtour du pentagone est colorié en rouge et les diagonales en bleu. Aucune des deux couleurs ne forme de triangle](five-person-counterexample.svg)

Si l'on n'observe que le sous-graphe rouge, il s'agit d'un cycle qui parcourt le pentagone. Si l'on choisit 3 sommets quelconques, il est impossible de former un triangle fermé uniquement avec des arêtes rouges. Si l'on n'observe que le sous-graphe bleu, il forme une étoile (un pentagramme) ; mais si l'on réordonne l'ordre des sommets, il s'agit également d'un cycle de longueur 5 passant par tous les sommets. Il n'existe donc aucun triangle bleu non plus.

Attention : les points d'intersection des lignes du pentagramme ne constituent pas de nouveaux sommets. Les personnes ne correspondent qu'aux 5 sommets de A à E. Les petits triangles visuels créés par le croisement géométrique des lignes ne sont pas des triangles au sens de la théorie des graphes.

Puisqu'il est possible d'éviter simultanément tout trio rouge et tout trio bleu, 5 personnes ne permettent pas de garantir la propriété. En combinant ce résultat avec la certitude pour 6 personnes, nous établissons formellement que le nombre minimal requis est 6.

## 5. Cette « taille minimale » est appelée nombre de Ramsey

Lorsque l'on colorie les arêtes d'un graphe complet en rouge et en bleu, le nombre minimal de sommets garantissant l'apparition d'un sous-graphe complet rouge $K_s$ ou d'un sous-graphe complet bleu $K_t$ est appelé **nombre de Ramsey** et se note $R(s,t)$.

Un $K_s$ rouge signifie que toutes les arêtes reliant les $s$ sommets choisis sont rouges. Il ne suffit pas qu'ils soient simplement reliés par un chemin rouge : toutes les paires doivent être connectées par du rouge. Comme $K_3$ représente un triangle, la conclusion de nos sections précédentes se résume en une ligne :

$$
R(3,3)=6
$$

Le théorème de Ramsey affirme que pour tous entiers finis $s, t$, un tel nombre fini existe toujours. Cependant, « savoir qu'il existe » et « calculer facilement sa valeur minimale » sont deux choses très différentes. Même si la démonstration pour les triangles est brève, dès que l'on recherche des sous-graphes monochromatiques plus grands, la complexité calculatoire explose de façon vertigineuse.

Une borne supérieure fondamentale est donnée par la relation suivante :

$$
R(s,t)\leq R(s-1,t)+R(s,t-1)
\qquad(s,t\geq3)
$$

En posant $N$ égal au membre de droite, considérons un sommet parmi ces $N$ sommets. Si le nombre de sommets reliés à celui-ci par des arêtes rouges est au moins égal à $R(s-1,t)$, alors ce groupe contient soit un $K_{s-1}$ rouge, soit un $K_t$ bleu. Dans le premier cas, en lui ajoutant le sommet initial, on obtient un $K_s$ rouge. Dans le second cas, la condition est déjà remplie.

S'il n'y a pas autant d'arêtes rouges, il y a nécessairement au moins $R(s,t-1)$ sommets reliés par des arêtes bleues. Le même raisonnement s'applique alors symétriquement pour la couleur bleue. Cela constitue une généralisation directe de la démonstration précédente (« isoler un sommet et regrouper ses voisins de même couleur »).

En partant des valeurs limites triviales $R(2,t)=t$ et $R(s,2)=s$, cette relation permet d'établir successivement des bornes supérieures finies. Toutefois, s'agissant d'une inégalité, la valeur obtenue n'est pas nécessairement minimale. Il est crucial de faire la distinction entre la « taille suffisante garantie » et le « minimum strictement nécessaire ».

## 6. « Presque toujours » et « Toujours sans exception » sont deux réalités distinctes

À titre d'expérience, imaginons maintenant que chaque arête soit coloriée en rouge ou en bleu de manière indépendante avec une probabilité de $1/2$. Ce modèle probabiliste n'est pas nécessaire pour la démonstration, mais il aide à appréhender la différence entre haute probabilité et certitude absolue.

En conservant les étiquettes des sommets (A, B, C, etc.), le nombre total de coloriages distincts s'exprime ainsi (deux configurations identiques par rotation ou permutation des noms de sommets sont comptées séparément) :

$$
2^{\binom{n}{2}}
$$

Pour 6 personnes, il existe $2^{15}=32\,768$ configurations possibles. En examinant exhaustivement les cas de 3 à 6 personnes, on obtient les résultats suivants :

| Nombre de personnes | Nombre total de coloriages | Coloriages sans aucun triangle monochromatique | Proportion avec au moins un triangle monochromatique |
|---|---:|---:|---:|
| 3 personnes | 8 | 6 | 25,00 % |
| 4 personnes | 64 | 18 | 71,88 % |
| 5 personnes | 1024 | 12 | 98,83 % |
| 6 personnes | 32768 | 0 | 100,00 % |

![Comparaison de la proportion de présence d'un triangle monochromatique pour 3 à 6 personnes. À 5 personnes, la proportion atteint 98,83 % mais il subsiste 12 contre-exemples, tandis qu'à 6 personnes, elle atteint 100 %](coloring-probability.svg)

Même avec 5 personnes, un coloriage aléatoire produit un triangle monochromatique dans environ 98,83 % des cas. Si l'on ne réalisait que quelques essais manuels, on pourrait être tenté de croire que « cela fonctionne toujours dès 5 personnes ». Pourtant, sur les 1 024 configurations possibles, 12 contre-exemples subsistent bel et bien. Il existe une différence fondamentale entre une probabilité très élevée et l'absence totale de contre-exemple.

Ce tableau présente les proportions sous l'hypothèse d'un coloriage indépendant et équiprobable. Il ne prétend nullement que les relations humaines réelles soient distribuées à pile ou face. En revanche, le théorème pour 6 personnes ne dépend aucunement des probabilités : il est valable quelle que soit la structure, même la plus biaisée, des relations.

### En moyenne, combien en trouve-t-on ?

Pour 3 sommets fixés, il y a 3 arêtes et donc 8 façons de les colorier. Parmi elles, 2 configurations sont monochromatiques (tout rouge ou tout bleu), soit une probabilité de $1/4$. Si l'on note $T$ le nombre de triangles monochromatiques, la linéarité de l'espérance donne :

$$
E[T]=\binom{n}{3}\frac14
$$

Pour 6 personnes, la moyenne est de 5 triangles. Bien que les triangles puissent partager des arêtes et ne soient donc pas indépendants, la linéarité de l'espérance ne requiert aucune hypothèse d'indépendance.

Néanmoins, le simple fait que la moyenne soit strictement positive ne garantit pas l'existence d'un triangle dans chaque coloriage individuel. Pour 5 personnes, l'espérance est de 2,5 triangles, et pourtant il existe des contre-exemples contenant exactement 0 triangle. Ne pas confondre « valeur moyenne » et « pire des cas » est un autre enseignement précieux de la théorie de Ramsey.

## 7. Vérification des 32 768 configurations en Python

Le code suivant fonctionne uniquement avec la bibliothèque standard de Python. En associant le rouge à 0 et le bleu à 1, la couleur de chaque arête correspond à un bit d'un entier binaire. On sélectionne chaque triplet de sommets et l'on vérifie si les 3 arêtes reliant ces sommets sont toutes de même couleur.

```python
from itertools import combinations

def check_all(n):
    edges = list(combinations(range(n), 2))
    edge_index = {edge: i for i, edge in enumerate(edges)}
    triples = [
        [edge_index[e] for e in combinations(vertices, 2)]
        for vertices in combinations(range(n), 3)
    ]
    total = 1 << len(edges)
    without_triangle = 0
    minimum = len(triples)

    for coloring in range(total):
        count = 0
        for i, j, k in triples:
            if ((coloring >> i) & 1) == ((coloring >> j) & 1) == ((coloring >> k) & 1):
                count += 1
        without_triangle += (count == 0)
        minimum = min(minimum, count)

    return total, without_triangle, minimum

for n in range(3, 7):
    total, missing, minimum = check_all(n)
    print(f"{n} personnes : total {total} configurations, sans triangle {missing} configurations, minimum {minimum}")
```

```text
3 personnes : total 8 configurations, sans triangle 6 configurations, minimum 0
4 personnes : total 64 configurations, sans triangle 18 configurations, minimum 0
5 personnes : total 1024 configurations, sans triangle 12 configurations, minimum 0
6 personnes : total 32768 configurations, sans triangle 0 configurations, minimum 2
```

La découverte de ce « minimum de 2 » pour 6 personnes est un résultat encore plus fort que notre première démonstration. En effet, si l'on note $r_v$ le nombre d'arêtes rouges incidentes au sommet $v$, et $b_v$ le nombre d'arêtes bleues, on a $r_v+b_v=5$, ce qui entraîne $r_vb_v\leq6$.

Dans un triangle non monochromatique, il y a exactement deux sommets où se rencontrent une arête rouge et une arête bleue. Ainsi, en comptant pour chaque sommet le nombre de paires « une arête rouge, une arête bleue », chaque triangle bicolore est compté exactement deux fois. Comme le nombre total de triangles est $\binom{6}{3}=20$, on a :

$$
T=\binom63-\frac12\sum_{v=1}^{6}r_vb_v
\geq20-\frac12\cdot6\cdot6=2
$$

Cette formule démontre l'existence d'au moins 2 triangles. De plus, si l'on divise les 6 sommets en deux groupes de 3, en coloriant en rouge les arêtes internes à chaque groupe et en bleu les arêtes reliant les deux groupes, on obtient exactement 2 triangles rouges et aucun triangle bleu. Par conséquent, la valeur minimale de 2 est rigoureusement exacte.

Cette énumération exhaustive est efficace pour de petites valeurs, mais le nombre total de coloriages croît selon $2^{n(n-1)/2}$. Si l'on augmente le nombre de personnes, le temps d'exécution devient rapidement prohibitif, c'est pourquoi nous nous limitons ici aux valeurs de 3 à 6. Les schémas et distributions détaillées peuvent être consultés dans le [script de reproduction](generate_graphs.py) et le [fichier JSON des résultats de calcul](calculation-results.json).

## 8. Application 1 : Réseaux — Connectivité totale ou déconnexion totale

Remplaçons la notion de « connaissances » par celle de « connexions directes » entre équipements réseau. Imaginons 6 appareils, où chaque paire est soit « connectée directement », soit « sans connexion directe ». S'il s'agit de liaisons bidirectionnelles non orientées, le même théorème s'applique directement.

Dès lors, il existe obligatoirement soit un sous-groupe de 3 appareils où chaque paire possède une connexion directe, soit un sous-groupe de 3 appareils où aucune paire ne possède de connexion directe. Le premier cas correspond à une **clique** à 3 sommets, et le second à un **ensemble indépendant** (ou stable) à 3 sommets. Soulignons que « sans connexion directe » ne signifie pas l'impossibilité de communiquer en passant par d'autres nœuds intermédiaires.

Cette perspective est également applicable à la planification de tâches avec contraintes de compatibilité par paires, ou à la validation de conception de petits réseaux. Si un cahier des charges impose d'« éviter à la fois tout ensemble de 3 tâches mutuellement compatibles et tout ensemble de 3 tâches mutuellement incompatibles », on sait d'emblée, sans le moindre calcul de recherche, que c'est mathématiquement impossible dès lors qu'il y a 6 éléments.

Cependant, le théorème ne permet pas de choisir laquelle des deux structures apparaîtra. Vous pourriez espérer 3 tâches compatibles et n'obtenir que 3 tâches incompatibles. De plus, le fait que des éléments soient compatibles deux à deux ne garantit pas que les ressources suffisent pour les exécuter simultanément à 3. Le théorème ne garantit strictement que les propriétés de la relation binaire fournie.

## 9. Application 2 : Extraire une sous-suite croissante ou décroissante d'une séquence quelconque

Prenons 6 nombres réels deux à deux distincts ordonnés dans une séquence. Pour deux positions $i < j$, relions-les par une arête rouge si $a_i\lt a_j$, et par une arête bleue si $a_i\gt a_j$.

Cette construction équivaut à un 2-coloriage du graphe complet à 6 sommets. Il existe donc nécessairement un triangle monochromatique. En désignant ces 3 positions ordonnées par $i\lt j\lt k$, s'il s'agit d'un triangle rouge, on a :

$$
a_i\lt a_j\lt a_k
$$

Et s'il s'agit d'un triangle bleu :

$$
a_i\gt a_j\gt a_k
$$

Cela signifie qu'**en préservant l'ordre d'apparition initial, il est toujours possible d'extraire une sous-suite de 3 termes qui soit strictement croissante ou strictement décroissante**. Les termes n'ont pas besoin d'être consécutifs. Une telle séquence obtenue sans modifier l'ordre relatif s'appelle une sous-suite.

![Schéma illustrant l'extraction d'une sous-suite croissante 1, 2, 3 aux positions 2, 4 et 6 à partir de la suite 4, 1, 5, 2, 6, 3](monotone-subsequence.svg)

Dans la suite $4, 1, 5, 2, 6, 3$ illustrée, le choix des positions 2, 4 et 6 fournit la sous-suite $1, 2, 3$. On n'a pas réordonné les valeurs par ordre croissant après coup : leur ordre d'apparition dans la suite d'origine a été scrupuleusement respecté.

Ce concept s'étend à la détection de sous-structures régulières au sein de flux de données. Cependant, extraire ainsi 3 valeurs croissantes ne prouve nullement que la série globale suit une tendance haussière : si une forme donnée apparaît inévitablement dans n'importe quel arrangement, sa simple présence ne traduit aucun phénomène spécifique.

Notons qu'ici, 6 termes ne constituent pas le minimum absolu : en réalité, 5 termes distincts suffisent déjà à garantir une sous-suite monotone (croissante ou décroissante) de longueur 3. Il s'agit d'un cas particulier du théorème d'Erdős-Szekeres. Les coloriages induits par une relation d'ordre sur une suite vérifient en effet des contraintes de transitivité, ce qui permet d'obtenir un résultat plus fort qu'un coloriage arbitraire. [Support de cours sur les sous-suites monotones (en anglais)](https://ywigderson.math.ethz.ch/math/static/pcmi2025/Notes10.pdf)

## 10. Conclusion : Même dans le désordre, certaines structures sont inévitables

En modélisant les relations de 6 personnes par des arêtes rouges et bleues et en isolant simplement les 5 arêtes issues d'un sommet, nous avons démontré l'existence inévitable d'un triangle monochromatique. Comme la configuration pentagonale à 5 personnes fournit un contre-exemple, le nombre de Ramsey correspondant est précisément $R(3,3)=6$.

Voici les trois enseignements fondamentaux à retenir :

- **« Toujours » ne signifie pas « avec une très forte probabilité ».** À 5 personnes, même avec 98,83 % de présence, il subsiste des contre-exemples ; à 6 personnes, il n'en reste aucun.
- **L'existence d'une régularité ne dicte pas la signification globale.** La présence d'un triangle monochromatique ou d'une sous-suite monotone ne renseigne en rien sur la dynamique globale ou les relations causales de l'ensemble.
- **Toute garantie mathématique repose sur un cadre précis.** Il convient de clarifier si la relation est symétrique, si chaque paire peut être catégorisée de façon binaire et quelle est la sous-structure exacte recherchée.

L'élégance de la théorie de Ramsey ne réside pas dans une simplification magique de la complexité globale. Le système peut demeurer éminemment complexe, mais il est rigoureusement impossible d'en éliminer toute parcelle de régularité locale. Quelques traits tracés sur une feuille de papier suffisent à nous en convaincre.

### Références et lectures complémentaires

- Ohio [State](https://kenji.blog/fr/p/iac-infrastructure-as-code-terraform/) University, [Ramsey Theory](https://ximera.osu.edu/math/combinatorics/combinatoricsBook/combinatoricsBook/combinatorics/ramseyTheory/ramseyTheory) : Introduction au 2-coloriage des arêtes et aux petits nombres de Ramsey (en anglais).
- Yuval Wigderson, PCMI 2025, [Extremal graph theory and Ramsey theory: Lecture 10](https://ywigderson.math.ethz.ch/math/static/pcmi2025/Notes10.pdf) : Support de cours sur la combinatoire extrémale et les approches de type Ramsey, incluant les sous-suites monotones (en anglais).

Les graphiques, les tableaux d'énumération exhaustive et les distributions de probabilités présentés dans cet article ont été générés à l'aide du script Python fourni.

