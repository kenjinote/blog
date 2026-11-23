---
title: 'Existe-t-il un algorithme surpassant GNFS (Crible général du corps de nombres) ?'
slug: "beyond-gnfs-integer-factorization-algorithms"
date: "2026-09-11T09:00:00+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["mathematics", "cryptography"]
tags: ["GNFS", "Factorisation d'entiers", "RSA", "Algorithmes"]
---

## 1. Introduction : La factorisation d'entiers et le fondement de la cryptographie moderne

RSA est l’un des systèmes à clé publique existants ; sa sécurité repose en partie sur la difficulté de factoriser de grands entiers. La sécurité d’Internet dans son ensemble ne dépend toutefois pas uniquement de RSA. Une méthode de factorisation efficace menacerait les usages fondés sur RSA, sans provoquer automatiquement l’effondrement de toutes les communications.

Pour factoriser de grands entiers généraux, le GNFS fait partie des méthodes classiques les mieux connues. Il a servi à factoriser notamment RSA-768 et RSA-250 ; les nombres de forme particulière peuvent mieux se prêter à des méthodes comme le SNFS. [Rapport RSA-250](https://eprint.iacr.org/2020/697)

Cependant, les cryptographes et les mathématiciens se posent constamment les questions suivantes : « Existe-t-il un algorithme classique surpassant GNFS ? », « Où se situent les limites des ordinateurs classiques ? » et « Comment les ordinateurs quantiques vont-ils surmonter cette situation ? »

Cet article dissèque de manière approfondie la structure mathématique profonde derrière GNFS, et fournit une analyse technique détaillée de la sélection de polynômes, du processus de criblage et de l'étape d'algèbre linéaire via la méthode par blocs de Wiedemann. En outre, il examine les méthodes d'extension de GNFS, comme l'amélioration de Coppersmith, et compare et explique les différences cruciales entre les algorithmes classiques en temps sous-exponentiel (Sub-exponential time) et les algorithmes quantiques en temps polynomial d'un point de vue mathématique.

---

## 2. Complexité asymptotique et notation L (L-notation)

Lors de l'évaluation de la complexité des algorithmes de factorisation, au lieu de la notation standard en temps polynomial (comme $O(n^k)$), on utilise la **notation L (L-notation)** pour exprimer le temps sous-exponentiel par rapport au nombre de chiffres de l'entrée $n$. La notation L est définie comme suit :

$$
L_n[\alpha, c] = \exp \left( (c + o(1)) (\ln n)^\alpha (\ln \ln n)^{1-\alpha} \right)
$$

Où $n$ est l'entier à factoriser, et $\ln n$ est le logarithme népérien, qui est proportionnel à la longueur en bits de $n$.
- Lorsque $\alpha = 0$ : $L_n[0, c] = \exp(c \ln \ln n) = (\ln n)^c$, ce qui représente un **temps polynomial (Polynomial time)** par rapport à la longueur en bits.
- Lorsque $\alpha = 1$ : $L_n[1, c] = \exp(c \ln n) = n^c$, ce qui représente un **temps exponentiel (Exponential time)** par rapport à la longueur en bits.
- Lorsque $0 < \alpha < 1$ : Cela devient un **temps sous-exponentiel (Sub-exponential time)**, situé entre le temps polynomial et le temps exponentiel.

L'histoire de l'évolution des algorithmes de factorisation du passé a également été l'histoire de la réduction progressive de la valeur de cet $\alpha$.
- **CFRAC** : temps d’exécution attendu heuristique $L_n[1/2,\sqrt{2}]$ ([référence](https://cacr.uwaterloo.ca/hac/about/chap3.pdf)).
- **MPQS/QS** : temps d’exécution attendu heuristique $L_n[1/2,1]$ ([documentation FLINT](https://flintlib.org/doc/algorithms/number-theory/quadratic-sieve.html)).
- **GNFS** : l’estimation heuristique usuelle est $L_n[1/3,(64/9)^{1/3}]$ ; ce n’est ni une borne démontrée ni un temps pratique directement obtenu ([analyse du NFS](https://arxiv.org/abs/2007.02730)).

---

## 3. L'algorithme complet et la structure mathématique de GNFS

GNFS et QS reposent sur la recherche d’une congruence de carrés : trouver $X,Y$ tels que $X^2\equiv Y^2\pmod n$ et $X\not\equiv\pm Y\pmod n$ ; alors $\gcd(X-Y,n)$ peut fournir un facteur non trivial.

Cependant, l'essence de GNFS réside dans le fait qu'il n'effectue pas cela uniquement dans le corps des nombres rationnels $\mathbb{Q}$, mais qu'il recherche simultanément des « nombres friables (Smooth numbers) » à la fois dans un corps d'extension $\mathbb{Q}(\alpha)$ appelé corps de nombres algébriques (Algebraic Number Field) et dans le corps des rationnels, et construit des relations de congruence par le biais d'homomorphismes.

Le processus de GNFS est divisé en 5 phases principales.

```mermaid
graph TD
  A["Problème de factorisation d'entiers (entrée n)"] --> B["1. Sélection de polynômes (Polynomial Selection)"]
  B --> C["2. Processus de criblage (Sieving Phase)"]
  C --> D["3. Filtrage (Filtering Phase)"]
  D --> E["4. Algèbre linéaire (Linear Algebra Phase)"]
  E --> F["5. Extraction de racine carrée (Square Root Phase)"]
  F --> G["Sortie des facteurs premiers p, q"]```

### 3.1 Phase 1 : Sélection de polynômes (Polynomial Selection)

Le succès de GNFS dépend fortement de la sélection de polynômes appropriés. L'objectif est de trouver deux polynômes irréductibles ayant une racine commune $m$ : $f_1(x)$ (côté rationnel) et $f_2(x)$ (côté algébrique). C'est-à-dire qu'ils satisfont :
$f_1(m) \equiv f_2(m) \equiv 0 \pmod n$

Généralement, on choisit un polynôme de degré 1, $f_1(x) = x - m$, pour le côté rationnel, et un polynôme unitaire de degré $d$ (typiquement 5 ou 6) pour le polynôme côté algébrique $f_2(x)$. L'approche la plus classique est la **méthode de la Base-$m$**.
On choisit un entier $m = \lfloor n^{1/(d+1)} \rfloor$ proche de la puissance $1/(d+1)$ de $n$, et on développe $n$ en base $m$.
$n = c_d m^d + c_{d-1} m^{d-1} + \dots + c_1 m + c_0$
On obtient ainsi le polynôme $f_2(x) = c_d x^d + c_{d-1} x^{d-1} + \dots + c_0$. Évidemment, on a $f_2(m) = n \equiv 0 \pmod n$.

Cependant, dans les implémentations modernes, on utilise l'**algorithme de Kleinjung**. Celui-ci évite que les coefficients des polynômes ne deviennent trop grands (optimisation du Skewness) tout en optimisant les propriétés algébriques (valeur $E$ de Murphy et valeur $\alpha$), cherchant ainsi des polynômes susceptibles de générer facilement des nombres friables lors de la phase de criblage. Rien que pour cette étape, d'importantes ressources de calcul sont mobilisées.

### 3.2 Phase 2 : Processus de criblage (Sieving Phase)

Une fois les polynômes déterminés, l'algorithme entre dans la phase de « criblage (Sieving) », qui est la plus gourmande en calculs. Ici, on recherche des paires $(a, b)$. Ces paires doivent être premières entre elles, et il est requis que les deux valeurs suivantes soient simultanément « friables (Smooth) » :

1. **Norme du côté rationnel** : $F_1(a, b) = b \cdot f_1(a/b) = a - bm$
2. **Norme du côté algébrique** : $F_2(a, b) = b^d \cdot f_2(a/b)$

Dans la définition de base, un nombre friable n’a pas de facteur premier supérieur à la borne de criblage. Certaines variantes pratiques acceptent aussi de grands facteurs premiers ; les critères dépendent de l’implémentation.
Aujourd'hui, une méthode appelée **crible par réseaux (Lattice Sieving)** est dominante. En fixant un certain nombre premier $q$, et en ne criblant que les paires $(a, b)$ sur un sous-réseau où les côtés rationnel et algébrique sont tous deux des multiples de $q$, on atteint une efficacité extrêmement élevée.

### 3.3 Phase 3 : Filtrage (Filtering Phase)

Le nombre de relations (relations) friables trouvées lors du processus de criblage s'élève à des centaines de millions, voire des milliards. Cependant, celles-ci contiennent également beaucoup d'informations inutiles.
Le but du filtrage est de construire une énorme matrice creuse (Sparse Matrix) tout en réduisant ses dimensions autant que possible.

Plus précisément, les opérations suivantes sont effectuées :
- **Suppression des singletons (Singleton removal)** : Suppression des relations contenant un facteur premier qui n'apparaît qu'une seule fois.
- **Suppression/Fusion de cliques (Clique removal / Merging)** : Multiplication entre elles de relations ayant des facteurs premiers apparaissant deux fois ou plus, afin d'éliminer des variables et de réduire à un système d'équations plus dense, mais de dimension plus petite.

Grâce à cela, une matrice de milliards de lignes est compressée en une énorme matrice creuse $\mathbf{A}$ de dizaines de millions de lignes (dont les éléments sont des 0 et des 1 sur le corps $\mathbb{F}_2$).

### 3.4 Phase 4 : Algèbre linéaire (Linear Algebra Phase)

On cherche ici un vecteur non nul $\mathbf{x}$ tel que $\mathbf{A}\mathbf{x}=\mathbf{0}$ sur $\mathbb{F}_2$ ; autrement dit, un vecteur du noyau de la matrice creuse.

Pour les matrices creuses, on utilise des méthodes itératives de Krylov comme Block Lanczos et Block Wiedemann. Le rapport sur la factorisation de RSA-250 documente un calcul avec Block Wiedemann ; le choix et les performances dépendent de la matrice, de l’implémentation et de l’architecture de calcul. [Rapport RSA-250](https://eprint.iacr.org/2020/697)


### 3.5 Phase 5 : Racine carrée (Square Root Phase)

À partir des solutions de l'algèbre linéaire, on construit des produits qui sont des « carrés parfaits » pour chacun des côtés rationnel et algébrique.
Du côté rationnel, $\prod (a-bm)$ devient le carré $X^2$ d'un certain entier $X$, et du côté algébrique, le produit des idéaux correspondants devient un carré parfait $\gamma^2$ sur le corps de nombres algébriques.
En calculant ce $\gamma$ sur le corps de nombres algébriques et en appliquant l'homomorphisme $\phi: \alpha \mapsto m \pmod n$ vers l'anneau des entiers rationnels, on obtient la congruence :
$X^2 \equiv \phi(\gamma)^2 \equiv Y^2 \pmod n$

Pour calculer la racine carrée sur le corps de nombres algébriques, des algorithmes complexes tels que la **méthode de Montgomery (Montgomery's Method)** sont utilisés, ce qui nécessite des connaissances approfondies en théorie algébrique des nombres. Enfin, en calculant $\gcd(X-Y, n)$, et si un facteur non trivial est obtenu, la factorisation est terminée.

---

## 4. Existe-t-il un algorithme classique surpassant GNFS ?

À ce jour, aucun algorithme classique avec une complexité asymptotique inférieure à $L_n[1/3, c]$ pour la factorisation d'entiers généraux n'a été découvert. Cependant, il existe plusieurs tentatives et algorithmes dérivés pour franchir les limites théoriques et pratiques.

### 4.1 Crible multiple du corps de nombres (MNFS: Multiple Number Field Sieve)

Comme approche étendant GNFS, on trouve le **crible multiple du corps de nombres (MNFS)** par D. Coppersmith. Alors que GNFS utilise deux polynômes (côté rationnel et côté algébrique), MNFS utilise simultanément plusieurs polynômes différents du côté algébrique pour un seul polynôme du côté rationnel.

$$ f_1(x), f_{2,1}(x), f_{2,2}(x), \dots, f_{2,V}(x) $$

En utilisant plusieurs corps algébriques, la probabilité de devenir « friable dans l'un des corps algébriques » à chaque étape de criblage peut être considérablement augmentée. Avec cette approche, Coppersmith a réussi à réduire légèrement la constante $c$ de la complexité $L_n[1/3, c]$.

Cependant, dans la pratique, la surcharge due à la gestion de corps multiples est importante, et cela n'a pas conduit à une percée décisive pour les modules [RSA](https://kenji.blog/fr/p/modern-cryptography-public-key-hash-signature/) à l'échelle pratique.

### 4.2 Des algorithmes de la classe $L_n[1/4]$ sont-ils possibles ?

Aucun algorithme classique général de factorisation de complexité asymptotique inférieure à la forme usuelle du GNFS n’est connu, mais cela ne prouve pas qu’un meilleur algorithme soit impossible. Les analyses des nombres friables décrivent les méthodes de criblage connues, sans établir de borne inférieure pour tous les algorithmes ; la question reste ouverte.
---

## 5. La percée par les ordinateurs quantiques : l'algorithme de Shor

Alors que les ordinateurs classiques font face au mur du $L_n[1/3]$, c'est l'**algorithme de Shor ([Shor's Algorithm](https://kenji.blog/fr/p/quantum-computing-shors-algorithm/))**, publié en 1994 par Peter Shor, qui a brisé ce mur en changeant fondamentalement le modèle de calcul lui-même.

### 5.1 Le choc du temps quantique polynomial

L'algorithme de Shor réduit le problème de la factorisation d'entiers au « problème de la recherche de l'ordre (Order Finding Problem) ». Pour un entier donné $a$, il s'agit de trouver la période (ordre) $r$ de la fonction $f(x) = a^x \pmod n$.
Shor exploite l’interférence quantique pour extraire des informations sur la période de la fonction ; cela ne signifie pas que tous les états en superposition sont lus en parallèle.

En termes de complexité, le temps d'exécution de l'algorithme de Shor est un **temps quantique polynomial**, plus précisément comme suit :
$$ O((\log n)^3) $$

```mermaid
graph LR
  A["Algorithme classique (GNFS)"] -->|"Limite"| B["Temps sous-exponentiel L_n[1/3]"]
  C["Algorithme quantique (Shor)"] -->|"Percée"| D["Temps polynomial O((log n)^3)"]
  B --> E["Utilisation continue de RSA (augmentation de la longueur des clés)"]
  D --> F["RSA vulnérable si un ordinateur quantique tolérant aux fautes assez puissant existe"]
```

### 5.2 Temps sous-exponentiel classique vs Temps polynomial quantique

Shor factorise en temps polynomial dans un modèle quantique idéalisé, mais cela ne donne pas à lui seul le coût pratique d’une machine tolérante aux fautes. Gidney et Ekerå estimaient en 2021 environ 20 millions de qubits physiques et 8 heures ; en 2025, Gidney estimait moins d’un million de qubits physiques bruités et moins d’une semaine avec une autre conception et d’autres hypothèses. Ce sont des estimations conditionnelles, pas des démonstrations de rupture de RSA-2048 ; aucun ordinateur quantique n’a factorisé un entier de cette taille. On ne peut déduire portes ou durée de $2048^3$ seulement. [2021](https://doi.org/10.22331/q-2021-04-15-433) · [2025](https://arxiv.org/abs/2505.15917)

La formule asymptotique du GNFS ne donne pas directement un nombre d’opérations ni une durée ; il faut un modèle de coût et des paramètres explicites.
## 6. Conclusion : Perspectives pour la prochaine génération

Le GNFS est la meilleure méthode générale connue, pas une limite démontrée. Aucun algorithme classique général de meilleure complexité asymptotique n’est connu, mais aucune preuve ne l’exclut. Les améliorations pratiques ne justifient ni garantie de durée ni affirmation selon laquelle RSA resterait sûr pendant des décennies. Les estimations de Shor sont conditionnelles et ne décrivent pas le matériel actuel. La transition post-quantique suit les normes et recommandations officielles applicables.
