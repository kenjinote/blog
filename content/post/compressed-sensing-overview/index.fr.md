---
slug: compressed-sensing-overview
title: "L'acquisition comprimée : pourquoi nous pouvons reconstruire le signal original à partir de peu d'observations"
description: "Un thème moderne menant à l'imagerie médicale, l'astronomie et la compression d'images."
categories: ["mathematics", "computer-science"]
tags: ["math", "signal-processing", "algorithm", "science"]
date: "2026-09-25T11:25:00+09:00"
image: eyecatch.jpg
---

# Qu'est-ce que l'acquisition comprimée (Compressed Sensing) ?

Dans la science des données et le traitement du signal modernes, l'un des changements de paradigme les plus révolutionnaires est l'« acquisition comprimée » (Compressed Sensing / Compressive Sensing). Traditionnellement, lors de la conversion de signaux analogiques tels que l'audio, les images et les ondes électromagnétiques en données numériques pour les ordinateurs, nous avons suivi la loi absolue du « théorème d'échantillonnage de Nyquist-Shannon ». Cependant, l'acquisition comprimée bouleverse cette sagesse conventionnelle en offrant une garantie mathématique étonnante : « Si le signal satisfait une certaine condition (parcimonie), le signal original peut être parfaitement reconstruit à partir d'un nombre de données d'observation bien inférieur à ce qu'exige le théorème d'échantillonnage. »

Dans cet article, nous expliquerons en profondeur, à l'aide de formules mathématiques, les fondements du théorème d'échantillonnage, la définition mathématique de la parcimonie, sa relaxation vers un problème d'optimisation $L_1$, ainsi que le cœur des percées théoriques réalisées par Emmanuel Candès, Terence Tao et d'autres. De plus, nous révélerons la vue d'ensemble de l'acquisition comprimée, en couvrant des exemples d'application tels que l'accélération de l'IRM et la construction d'images de trous noirs, jusqu'à l'implémentation de code concret en Python.

## 1. Le théorème d'échantillonnage de Nyquist-Shannon et ses limites

### Les bases du théorème d'échantillonnage
Au milieu du 20e siècle, Claude Shannon et Harry Nyquist ont établi le « théorème d'échantillonnage » comme fondement de la théorie de l'information. Ce théorème définit les conditions de conversion d'un signal analogique continu en un signal numérique discret comme suit :

> **Théorème d'échantillonnage de Nyquist-Shannon**
> Pour reconstruire parfaitement un signal dont la bande passante est limitée à $f_{\max}$, le signal doit être échantillonné à une fréquence d'échantillonnage (fréquence de Nyquist) d'au moins $2f_{\max}$.

Par exemple, la limite supérieure de la plage audible par l'oreille humaine est d'environ 20 kHz. Par conséquent, sur un CD audio, l'échantillonnage est effectué à 44,1 kHz, soit plus du double. Exprimé sous forme mathématique, si un signal continu $x(t)$ possède une transformée de Fourier $X(f)$ et que $X(f) = 0$ pour $|f| > f_{\max}$, $x(t)$ peut être parfaitement restauré par la formule d'interpolation suivante utilisant la fonction sinus cardinal (fonction sinc) :

$$ x(t) = \sum_{n=-\infty}^{\infty} x\left(\frac{n}{2f_{\max}}\right) \operatorname{sinc}\left(2f_{\max}t - n\right) $$

### L'explosion des données et les limites du théorème
Le théorème d'échantillonnage est extrêmement puissant et constitue la pierre angulaire des communications numériques modernes. Cependant, avec les progrès technologiques, la quantité d'informations captées par les capteurs a explosé. Dans l'imagerie médicale à haute résolution (IRM et scanner), les réseaux de radiotélescopes en astronomie et les systèmes radar à ultra-large bande, un échantillonnage selon la fréquence de Nyquist entraînerait un volume de données à observer beaucoup trop important.

En conséquence, les problèmes suivants surviennent :
1. **Augmentation du temps de balayage** : En IRM, par exemple, la collecte des données prend beaucoup de temps, ce qui impose une charge physique aux patients.
2. **Limites matérielles** : La fabrication de convertisseurs A/N pour échantillonner des signaux à très haute fréquence devient techniquement difficile ou extrêmement coûteuse.
3. **Pression sur le stockage des données et les communications** : Les coûts de stockage et de transmission de quantités massives de données d'échantillonnage montent en flèche.

Le paradigme conventionnel consistait à « échantillonner massivement, puis compresser par logiciel (comme JPEG ou MP3) pour éliminer les données inutiles ». Cependant, une question se pose : « S'il s'agit de les jeter finalement, ne pourrions-nous pas capter (acquérir) directement uniquement les informations nécessaires dès le départ ? » L'acquisition comprimée a rendu cela possible.

## 2. Définition mathématique de la parcimonie (Sparsity)

La condition absolue pour que l'acquisition comprimée fonctionne est la **parcimonie (Sparsity)**. La parcimonie désigne la propriété selon laquelle, « lorsqu'un signal est transformé avec une base (représentation) appropriée, la plupart de ses composantes deviennent nulles (ou des valeurs très proches de zéro) ».

### Formulation d'un vecteur parcimonieux
Considérons un signal discret (vecteur) de longueur $N$, $\mathbf{x} \in \mathbb{R}^N$. Supposons que ce signal puisse être exprimé à l'aide d'une matrice de base orthogonale $\mathbf{\Psi} \in \mathbb{R}^{N \times N}$ (par exemple, la matrice de transformée de Fourier ou la matrice de transformée en ondelettes) comme suit :

$$ \mathbf{x} = \mathbf{\Psi} \mathbf{s} $$

Ici, $\mathbf{s} \in \mathbb{R}^N$ est le vecteur de coefficients sur la base $\mathbf{\Psi}$.
Si le nombre d'éléments non nuls de ce vecteur $\mathbf{s}$ est $K$ ($K \ll N$), on dit que $\mathbf{x}$ est **$K$-parcimonieux ($K$-sparse)**. Mathématiquement, cela est défini en utilisant la pseudo-norme $L_0$ (une fonction qui compte le nombre d'éléments non nuls) :

$$ \|\mathbf{s}\|_0 = K $$

### La parcimonie dans le monde réel
Étonnamment, de nombreux signaux existant dans la nature deviennent parcimonieux en choisissant une base appropriée.
- **Images** : Les images naturelles ne sont pas parcimonieuses dans l'espace des pixels, mais lorsqu'on applique une transformée en ondelettes ou une transformée en cosinus discrète (DCT), la plupart des composantes à haute fréquence s'approchent de zéro, rendant le signal parcimonieux (c'est le principe de la compression JPEG).
- **Audio** : Les signaux audio sont continus dans le domaine temporel, mais dans le domaine fréquentiel (après transformée de Fourier), seules quelques composantes de fréquence principales (fréquence fondamentale et harmoniques) ont des valeurs importantes.

L'acquisition comprimée est une technologie qui tire parti de cette « redondance inhérente aux signaux » pour effectuer la compression des données simultanément lors de la phase d'échantillonnage.

## 3. Formulation de l'acquisition comprimée et matrice d'observation

En supposant qu'un signal est parcimonieux, comment pouvons-nous restaurer le signal à partir de peu de données ?
Pour un signal inconnu $\mathbf{x} \in \mathbb{R}^N$, supposons que nous fassions $M$ observations linéaires ($M < N$). Le processus d'observation est exprimé à l'aide de la matrice d'observation $\mathbf{\Phi} \in \mathbb{R}^{M \times N}$ comme suit :

$$ \mathbf{y} = \mathbf{\Phi} \mathbf{x} = \mathbf{\Phi} \mathbf{\Psi} \mathbf{s} = \mathbf{A} \mathbf{s} $$

Ici,
- $\mathbf{y} \in \mathbb{R}^M$ : Vecteur de données d'observation
- $\mathbf{A} = \mathbf{\Phi} \mathbf{\Psi} \in \mathbb{R}^{M \times N}$ : Matrice d'acquisition (Sensing matrix)

Notre objectif est de restaurer le vecteur de coefficients inconnu $\mathbf{s}$ (et finalement $\mathbf{x}$) à partir des données d'observation données $\mathbf{y}$ et de la matrice $\mathbf{A}$.

### Le problème du système sous-déterminé
Cependant, nous faisons face ici à un mur mathématique. Étant donné que $M < N$ (il y a plus d'inconnues que d'équations), ce système d'équations simultanées $\mathbf{y} = \mathbf{A} \mathbf{s}$ devient un **système sous-déterminé (underdetermined system)**, ce qui entraîne une infinité de solutions. Il est impossible de trouver une solution unique avec l'algèbre linéaire classique.

C'est ici que nous utilisons la connaissance préalable selon laquelle « $\mathbf{s}$ est parcimonieux (les composantes non nulles sont extrêmement rares) ». Si nous cherchons la solution la plus parcimonieuse (celle avec le moins de composantes non nulles) parmi l'infinité de solutions candidates, il est très probable qu'il s'agisse du vrai signal. Formulé comme un problème d'optimisation, cela donne ce qui suit :

$$ (P_0) \quad \min_{\mathbf{s} \in \mathbb{R}^N} \|\mathbf{s}\|_0 \quad \text{subject to} \quad \mathbf{y} = \mathbf{A} \mathbf{s} $$

### La difficulté de l'optimisation $L_0$
Idéalement, nous devrions résoudre le problème $(P_0)$ ci-dessus, mais mathématiquement, le problème de minimisation de $\|\mathbf{s}\|_0$ est connu pour être **NP-difficile (NP-hard)**. Il est nécessaire de vérifier par force brute les combinaisons des composantes non nulles, et lorsque la dimension $N$ augmente, cela prendrait plus de temps que la durée de vie de l'univers, même avec les superordinateurs modernes.

## 4. Relaxation vers le problème d'optimisation $L_1$ : La percée de Candès et Tao

La raison pour laquelle l'acquisition comprimée s'est répandue de manière explosive en tant que technologie pratique est la preuve mathématique stupéfiante que même si ce problème insoluble d'optimisation $L_0$ est remplacé par un **problème d'optimisation $L_1$ calculable**, on aboutit exactement à la **même réponse correcte** sous certaines conditions.

Entre 2004 et 2006, Emmanuel Candès, Terence Tao et David Donoho ont posé des fondations solides pour cette théorie.

### Minimisation de la norme $L_1$
Au lieu de la pseudo-norme $L_0$, nous utilisons la norme $L_1$, qui est la somme des valeurs absolues de chaque élément du vecteur.

$$ \|\mathbf{s}\|_1 = \sum_{i=1}^N |s_i| $$

Grâce à cela, le problème est relaxé (relaxation) comme suit :

$$ (P_1) \quad \min_{\mathbf{s} \in \mathbb{R}^N} \|\mathbf{s}\|_1 \quad \text{subject to} \quad \mathbf{y} = \mathbf{A} \mathbf{s} $$

Le problème de minimisation $L_1$ est un type de problème d'optimisation convexe, et une solution exacte peut être calculée en temps polynomial en utilisant des algorithmes existants très efficaces tels que la programmation linéaire (Linear Programming).

### Pourquoi $L_1$ ? (Intuition géométrique)
Pourquoi utiliser la norme $L_1$ plutôt que la norme $L_2$ (méthode des moindres carrés) ? Cela peut être compris de manière géométrique.
La contrainte $\mathbf{y} = \mathbf{A}\mathbf{s}$ forme un hyperplan dans un espace de grande dimension. La minimisation de la norme équivaut à étendre des surfaces de niveau (boules) centrées sur l'origine et à trouver le premier point de contact avec cet hyperplan.

- **Boule $L_2$ ($\|\mathbf{s}\|_2 \le R$)** : La forme est une sphère lisse. Le point de contact avec l'hyperplan se situe, dans la plupart des cas, à l'écart de tous les axes de coordonnées, de sorte que la solution obtenue est un vecteur « dense » dont tous les éléments sont non nuls.
- **Boule $L_1$ ($\|\mathbf{s}\|_1 \le R$)** : La forme est un polyèdre (losange, octaèdre, etc.) et possède de nombreux « coins (sommets) ». Ces coins sont situés sur les axes de coordonnées. Lorsqu'on presse l'hyperplan contre elle, la probabilité est élevée qu'ils se touchent sur un de ces « coins ». Toucher à un coin signifie que les valeurs des autres axes de coordonnées deviennent nulles, et par conséquent, une solution parcimonieuse est obtenue.

### RIP (Restricted Isometry Property : Propriété d'isométrie restreinte)
Candès et Tao ont introduit le concept de **RIP (Propriété d'isométrie restreinte)** comme condition suffisante pour que la minimisation $L_1$ coïncide avec la minimisation $L_0$.
La matrice d'acquisition $\mathbf{A}$ satisfait la RIP d'ordre $K$ s'il existe une petite constante $\delta_K \in (0,1)$ telle que, pour tout vecteur $K$-parcimonieux $\mathbf{s}$, l'inégalité suivante soit vraie :

$$ (1 - \delta_K) \|\mathbf{s}\|_2^2 \le \|\mathbf{A}\mathbf{s}\|_2^2 \le (1 + \delta_K) \|\mathbf{s}\|_2^2 $$

Intuitivement, il s'agit de la propriété selon laquelle « la matrice $\mathbf{A}$ préserve (presque) la longueur de n'importe quel vecteur parcimonieux sans la modifier ». Candès et Tao ont brillamment prouvé que si $\mathbf{A}$ satisfait une condition RIP spécifique, la solution de $(P_1)$ correspondra parfaitement à la solution de $(P_0)$ dans une situation sans bruit.

De plus, d'un point de vue pratique, il a été démontré que l'utilisation d'une **matrice aléatoire (une matrice de nombres aléatoires suivant une distribution gaussienne ou de Bernoulli)** comme matrice d'observation $\mathbf{\Phi}$ satisfait la RIP avec une forte probabilité. En d'autres termes, « observer de manière aléatoire » devient la stratégie d'échantillonnage la plus efficace et universelle dans l'acquisition comprimée.

Il a été prouvé que le nombre d'observations nécessaires $M$ par rapport à la longueur du signal $N$ et au degré de parcimonie $K$ est suffisant dans l'ordre suivant :

$$ M \ge C \cdot K \log\left(\frac{N}{K}\right) $$
(où $C$ est une constante)

Cela signifie que par rapport aux $N$ observations exigées par le théorème d'échantillonnage, un nombre beaucoup plus petit (dépendant de $K$) est suffisant.

## 5. Exemples d'application de l'acquisition comprimée

La théorie de l'acquisition comprimée a révolutionné tous les domaines de l'ingénierie de l'information et de la physique.

### 1. Accélération de l'IRM (Imagerie par Résonance Magnétique)
L'un des exemples d'applications commerciales les plus réussis est l'IRM. L'IRM utilise de puissants champs magnétiques pour obtenir des images en coupe du corps humain, mais la collecte de données (données du domaine fréquentiel appelées espace k) présente des limites physiques et prend du temps.
Lors de l'imagerie de patients pédiatriques ou d'organes en mouvement comme le cœur, une immobilité prolongée est difficile. En appliquant l'acquisition comprimée à l'IRM, l'échantillonnage des données de l'espace k est aléatoirement sous-échantillonné, réussissant à réduire le temps de balayage à une fraction de ce qu'il était. Aujourd'hui, les principaux fabricants d'équipements médicaux tels que Siemens et GE vendent des IRM équipés de série de la technologie d'acquisition comprimée.

### 2. Imagerie des trous noirs (Event Horizon Telescope)
En 2019, l'équipe de recherche internationale « Event Horizon Telescope (EHT) » a réussi à capturer la première image de l'ombre d'un trou noir dans l'histoire de l'humanité. Pour construire un télescope virtuel géant de la taille de la Terre, les données des radiotélescopes répartis dans le monde entier ont été intégrées (Interférométrie à très longue base : VLBI), mais le placement des télescopes sur Terre présentait des limites, et les données d'observation comportaient d'énormes « vides (données manquantes) ».
Afin de restaurer l'image du trou noir à partir de ces données lacunaires, un algorithme appelé CHIRP (Continuous High-resolution Image Reconstruction using Patch priors) a été développé. On peut dire qu'il s'agit également d'une application de l'acquisition comprimée tirant parti de la parcimonie et des connaissances structurelles préalables inhérentes aux images de l'espace.

### 3. Caméra à pixel unique (Single-Pixel Camera)
Une équipe de recherche de l'Université Rice a développé une caméra ne possédant qu'un seul élément récepteur de lumière (pixel).
En utilisant un DMD (Digital Micromirror Device), la lumière de l'objet cible est réfléchie dans un motif aléatoire et sa somme est mesurée par un seul capteur. En répétant cela des milliers de fois, une image de plusieurs millions de pixels est reconstruite. Cette technologie est extrêmement utile pour l'imagerie dans des bandes de fréquences telles que l'infrarouge ou les ondes térahertz, où la fabrication de capteurs multi-pixels est extrêmement coûteuse.

## 6. Exemple d'implémentation de l'acquisition comprimée en Python

Comme il est difficile de saisir la théorie seule, effectuons une simulation de l'acquisition comprimée en utilisant Python.
Ici, nous générons un signal parcimonieux unidimensionnel et restaurons le signal original à partir de quelques observations aléatoires en utilisant l'optimisation $L_1$. Nous utiliserons la bibliothèque `cvxpy` pour l'optimisation.

### Installation des bibliothèques nécessaires
```bash
pip install numpy matplotlib cvxpy
```

### Code d'implémentation

```python
import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cp

# Fixer la graine aléatoire
np.random.seed(42)

# --- 1. Paramètres du problème ---
N = 1000  # Dimension du signal (nombre qui devrait idéalement être échantillonné)
K = 50    # Degré de parcimonie (nombre d'éléments non nuls)
M = 250   # Nombre d'observations (seulement 25% de N)

# --- 2. Génération du vrai signal parcimonieux ---
# Créer le vrai signal x_true (valeurs initiales toutes nulles)
x_true = np.zeros(N)
# Choisir aléatoirement K indices et leur attribuer des valeurs non nulles (distribution gaussienne)
nonzero_indices = np.random.choice(N, K, replace=False)
x_true[nonzero_indices] = np.random.randn(K)

# --- 3. Simulation du processus d'observation ---
# Générer une matrice d'observation gaussienne aléatoire A (M x N)
A = np.random.randn(M, N)
# Normaliser par colonne (rendre la norme égale à 1)
A = A / np.linalg.norm(A, axis=0)

# Données observées y = A * x_true
y = A @ x_true

# --- 4. Reconstruction du signal par acquisition comprimée (optimisation L1) ---
# Définir le problème d'optimisation avec cvxpy
x_reconstruct = cp.Variable(N)
# Fonction objectif : minimisation de la norme L1
objective = cp.Minimize(cp.norm(x_reconstruct, 1))
# Contrainte : y = A * x (correspondance avec les données observées)
constraints = [A @ x_reconstruct == y]

# Définir et résoudre le problème
prob = cp.Problem(objective, constraints)
print("Calcul d'optimisation en cours...")
prob.solve(solver=cp.ECOS)

# Signal reconstruit
x_rec = x_reconstruct.value

# --- 5. Visualisation des résultats ---
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(x_true, label='Vrai signal', alpha=0.7)
plt.title(f'Signal parcimonieux original (N={N}, K={K})')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(x_rec, color='red', label='Signal reconstruit', alpha=0.7)
plt.title(f'Reconstruit par minimisation L1 (M={M} mesures)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Vérification de la précision de la reconstruction
error = np.linalg.norm(x_true - x_rec)
print(f"Erreur de reconstruction (norme L2) : {error:.6e}")
```

### Explication du code
1. **Génération du signal** : Parmi la dimension $N=1000$, seules $K=50$ positions ont des valeurs (le reste est zéro), ce qui permet de créer un vecteur parcimonieux `x_true`.
2. **Observation** : Si nous suivions le théorème d'échantillonnage, 1000 mesures seraient nécessaires, mais ici nous utilisons une matrice d'observation aléatoire `A` avec seulement $M=250$ (25%) observations pour obtenir les données `y`.
3. **Reconstruction** : En utilisant uniquement les données d'observation `y` et la matrice `A` comme entrées, nous utilisons `cvxpy` pour trouver « le $\mathbf{x}$ avec la plus petite norme $L_1$ parmi ceux qui satisfont $\mathbf{y} = \mathbf{A}\mathbf{x}$ ».
4. **Résultats** : Une fois le calcul terminé, l'erreur de reconstruction est d'une valeur extrêmement faible de l'ordre de `1e-9` ou moins, confirmant que le vrai signal a été **parfaitement (Exact) restauré** à partir de seulement 25% des données d'observation.

```mermaid
flowchart LR
    X["Signal parcimonieux inconnu\nx (Dimension N)"] -->|Matrice d'observation\naléatoire A| Y["Données d'observation\ny (Dimension M, M < N)"]
    Y -->|Optimisation L1\n(Algorithme d'optimisation convexe)| X_hat["Signal reconstruit\nx^"]
    X -. "Garantie de correspondance parfaite" .-> X_hat
```

## 7. Conclusion et perspectives futures

L'acquisition comprimée a fondamentalement changé le paradigme dans l'histoire du traitement du signal. L'approche consistant à « mesurer intelligemment uniquement la quantité nécessaire dès le départ », plutôt que de « mesurer massivement pour ensuite jeter », s'appuie sur des théories mathématiques profondes (optimisation convexe, [théorie des matrices aléatoires](/fr/p/random-matrix-theory/), géométrie en haute dimension).

Actuellement, les recherches combinant l'apprentissage profond (Deep Learning) et l'acquisition comprimée sont très actives. Au lieu des algorithmes d'optimisation $L_1$ conventionnels, les approches utilisant des réseaux neuronaux pour résoudre des problèmes inverses de manière plus rapide et plus précise (Deep Unfolding / Algorithm Unrolling) deviennent la norme. Cela permet d'apprendre la conception même de la matrice d'observation à partir des données, ce qui fait progresser des applications telles qu'une accélération supplémentaire de l'IRM et une reconstruction d'images robuste au bruit.

La magie mathématique de l'acquisition comprimée, qui permet de voir la vue d'ensemble avec précision à partir de peu d'informations, continuera de nous fournir de « nouveaux yeux » dans tous les domaines où l'explosion des données est un défi, tels que la conduite autonome, les réseaux de capteurs IoT et l'exploration spatiale.
