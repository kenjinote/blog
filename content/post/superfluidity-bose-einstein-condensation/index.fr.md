---
title: "Superfluidité et condensation de Bose-Einstein : la physique des phénomènes quantiques macroscopiques près du zéro absolu"
description: "L'hélium liquide qui grimpe aux murs avec une viscosité nulle, l'effet fontaine, la topologie des vortex quantiques. Les merveilles de la BEC, où les bosons dégénèrent en une fonction d'onde unique."
slug: "superfluidity-bose-einstein-condensation"
date: "2026-10-03T05:00:00+09:00"
categories: ["physics", "quantum"]
tags: ["quantum-mechanics", "condensed-matter", "superfluidity", "thermodynamics"]
image: "eyecatch.jpg"
---

# Superfluidité et condensation de Bose-Einstein : la physique des phénomènes quantiques macroscopiques près du zéro absolu

Dans la physique moderne, le monde cryogénique près du zéro absolu (0 K = -273,15 °C) est un trésor de phénomènes étonnants qui défient largement notre intuition quotidienne. Parmi eux, la « Superfluidité » (Superfluidity) et la « Condensation de Bose-Einstein » (Bose-Einstein Condensation, BEC) sont des représentants typiques des « phénomènes quantiques macroscopiques », où les propriétés de la mécanique quantique microscopique sont observées directement à l'échelle macroscopique, continuant de fasciner de nombreux physiciens.

L'hélium liquide, dont la viscosité devient complètement nulle et qui grimpe spontanément sur les parois d'un récipient. L'effet thermomécanique (effet fontaine) où le liquide jaillit d'une buse étroite lorsqu'il est éclairé. Et la BEC, où des billions d'atomes tombent exactement dans le même état quantique et se comportent comme une seule onde de matière géante. Cet article explore en profondeur, d'un point de vue très détaillé et académique, comment ces phénomènes ont été découverts et théoriquement élucidés, de leur contexte historique jusqu'à leur cadre théorique avancé.

---

## Chapitre 1 : Le défi du zéro absolu et l'histoire de la liquéfaction de l'hélium

### 1.1 L'aube de la physique des basses températures et la liquéfaction des gaz permanents
À la fin du 19ème siècle, l'un des grands thèmes de la physique était de savoir si « tous les gaz pouvaient être liquéfiés par refroidissement et pressurisation ». Grâce aux efforts de Michael Faraday et d'autres, de nombreux gaz ont été liquéfiés, mais l'oxygène, l'azote, l'hydrogène et l'hélium étaient appelés « gaz permanents » et leur liquéfaction était considérée comme extrêmement difficile.

Cependant, avec le développement de la thermodynamique et les progrès de la technologie de refroidissement utilisant l'effet Joule-Thomson, l'oxygène a été liquéfié en 1877, et en 1898, James Dewar a réussi à liquéfier l'hydrogène (point d'ébullition d'environ 20 K). Le dernier gaz inexploré était l'hélium.

### 1.2 La liquéfaction de l'hélium et la gloire de Kamerlingh Onnes
Heike Kamerlingh Onnes, qui a fondé le laboratoire de cryogénie à l'Université de Leyde aux Pays-Bas, a procédé à des préparatifs minutieux et à la construction d'un immense appareil de liquéfaction. Le 10 juillet 1908, en utilisant de l'hydrogène liquide pour le pré-refroidissement et en répétant l'expansion de Joule-Thomson, il a finalement réussi à liquéfier l'hélium. Le point d'ébullition de l'hélium liquide étant de 4,2 K, l'humanité a ouvert la porte au monde des températures extrêmement basses, à seulement 4 degrés du zéro absolu. Pour cette réalisation, Kamerlingh Onnes a reçu le prix Nobel de physique en 1913.

La production d'hélium liquide a directement conduit à la découverte de la supraconductivité en 1911 (le phénomène où la résistance électrique du mercure tombe à zéro à 4,2 K), mais il a fallu plusieurs décennies de plus avant que les propriétés anormales de l'hélium liquide lui-même ne soient révélées.

### 1.3 La transition lambda et la découverte de la superfluidité
Des années 1920 aux années 1930, Willem Hendrik Keesom et d'autres ont découvert que lorsque l'hélium liquide était refroidi davantage, la chaleur spécifique présentait une divergence logarithmique à environ 2,17 K. Le graphique de cette variation de température de la chaleur spécifique ressemblant à la lettre grecque « $\lambda$ (lambda) », cette transition de phase a été nommée « transition $\lambda$ (lambda) ». La phase au-dessus de 2,17 K ($T_\lambda$) est appelée « Hélium I » et la phase en dessous est appelée « Hélium II ».

L'Hélium II a montré un comportement anormal, totalement différent des liquides ordinaires. Les découvertes les plus spectaculaires ont été rapportées l'une après l'autre en 1938. Pyotr Kapitza à Moscou, et John F. Allen et Don Misener de l'Université de Cambridge, ont découvert indépendamment que l'Hélium II s'écoulait à travers des tubes capillaires extrêmement fins sans résistance (avec une viscosité nulle).

Kapitza a nommé cette fluidité anormale « Superfluidité » par analogie avec la supraconductivité (Superconductivity). Dans l'expérience menée par Kapitza, deux disques de verre ont été placés face à face pour créer un très petit espace (quelques microns), et la viscosité de l'hélium liquide s'y écoulant a été mesurée. Alors que l'Hélium I montrait une résistance en tant que fluide visqueux normal, la vitesse d'écoulement a augmenté de façon spectaculaire dès que la température est descendue en dessous de $T_\lambda$, et il a été confirmé que le coefficient de viscosité apparent chutait brusquement à au moins moins d'un dix-millième ($10^{-4}$) de sa valeur normale.

Plus curieusement, des mesures effectuées à l'aide d'un viscosimètre rotatif (une expérience dans laquelle un cylindre est mis en rotation dans le liquide) ont donné des résultats contradictoires, suggérant que l'Hélium II se comportait comme s'il avait encore une viscosité finie. Ce phénomène apparemment inexplicable, « une viscosité nulle dans un tube capillaire, mais qui exerce une résistance visqueuse sur un corps en rotation », a été brillamment résolu par le « modèle à deux fluides » ultérieur.

---

## Chapitre 2 : Le cadre théorique de la condensation de Bose-Einstein (BEC)

La clé pour comprendre la superfluidité de l'hélium liquide d'un point de vue microscopique réside dans la mécanique statistique quantique. Un atome d'hélium 4 est composé de deux protons, deux neutrons et deux électrons, et la somme totale de leurs spins est un nombre entier (0). En d'autres termes, l'hélium 4 est un « boson ». Nous déduirons ici le cadre théorique de ce qui se passe lorsqu'un ensemble de bosons est refroidi vers le zéro absolu.

### 2.1 Statistiques de Bose et statistiques de Fermi
En mécanique quantique, des particules identiques sont, par principe, indiscernables. En raison de la symétrie de la fonction d'onde par rapport à l'échange de particules, les particules sont divisées en deux grandes catégories.
- **Bosons** : Particules à spin entier. La fonction d'onde est symétrique par rapport à l'échange de particules (le signe ne change pas). Ils ne suivent pas le principe d'exclusion de Pauli, et plusieurs particules peuvent occuper le même état quantique simultanément.
- **Fermions** : Particules à spin demi-entier. La fonction d'onde est antisymétrique par rapport à l'échange de particules (le signe change). Ils suivent le principe d'exclusion de Pauli, et une seule particule peut occuper un état quantique donné.

Considérons la mécanique statistique d'un gaz de Bose idéal. Soit $\Xi$ la grande fonction de partition, $\mu$ le potentiel chimique, et $\beta = 1 / (k_B T)$ la température inverse. Le nombre moyen de particules $\langle n_i \rangle$ dans l'état d'énergie $\epsilon_i$ est donné par la fonction de distribution de Bose-Einstein :
$$ \langle n_i \rangle = \frac{1}{e^{\beta(\epsilon_i - \mu)} - 1} $$
Ici, pour que le nombre de particules soit non négatif, il faut que $\epsilon_i - \mu > 0$ dans tous les états $i$. En posant l'énergie de l'état fondamental $\epsilon_0 = 0$, le potentiel chimique doit toujours satisfaire $\mu \leq 0$.

### 2.2 La longueur d'onde thermique de de Broglie et l'émergence de la fonction d'onde macroscopique
La « longueur d'onde thermique de de Broglie » $\lambda_{dB}$ est un indicateur de l'étendue spatiale d'une particule en tant qu'onde. À partir de la moyenne thermique de l'énergie cinétique $p^2 / 2m \sim k_B T$, l'impulsion est $p \sim \sqrt{m k_B T}$, donc la longueur d'onde de de Broglie $\lambda = h/p$ est approximativement donnée par :
$$ \lambda_{dB} = \sqrt{\frac{2\pi \hbar^2}{m k_B T}} $$

À haute température, $\lambda_{dB}$ est très courte, bien plus petite que la distance moyenne entre les particules $d = (V/N)^{1/3}$. À ce moment-là, les particules se comportent comme des boules de billard classiques et peuvent être bien approximées par la statistique de Maxwell-Boltzmann.
Cependant, à mesure que la température $T$ diminue, $\lambda_{dB}$ s'allonge progressivement. Ensuite, à une certaine température critique $T_c$, la longueur d'onde $\lambda_{dB}$ devient comparable à la distance inter-particulaire $d$ ($\lambda_{dB} \sim d$). À ce moment, les fonctions d'onde des particules individuelles commencent à se chevaucher spatialement, et les effets d'interférence quantique deviennent évidents à l'échelle macroscopique.

Lorsque la température est encore abaissée, un grand nombre de bosons tombent comme une avalanche dans l'état de plus basse énergie (l'état fondamental). Dans cet état, d'innombrables particules se comportent comme une seule onde de matière géante avec exactement la même phase, c'est-à-dire une « fonction d'onde macroscopique » (Macroscopic Wavefunction) $\Psi(\mathbf{r}) = \sqrt{n_0(\mathbf{r})} e^{i\theta(\mathbf{r})}$. C'est la condensation de Bose-Einstein (BEC).

### 2.3 Dérivation mathématique de la température de transition de condensation $T_c$
Considérons un système de gaz de Bose idéal dans un volume $V$ de l'espace tridimensionnel. Le nombre total de particules $N$ dans le système est exprimé comme la somme du nombre moyen de particules dans chaque état :
$$ N = \sum_i \frac{1}{e^{\beta(\epsilon_i - \mu)} - 1} $$

Dans un système macroscopique ($V \to \infty$), la somme sur les états peut être remplacée par une intégrale sur l'énergie. La densité d'états $D(\epsilon)$, en posant les degrés de liberté de spin à 1, est :
$$ D(\epsilon) = \frac{V}{(2\pi)^2} \left( \frac{2m}{\hbar^2} \right)^{3/2} \sqrt{\epsilon} $$
En évaluant le nombre de particules à l'aide de l'intégrale, nous avons :
$$ N_{ex} = \int_0^\infty D(\epsilon) \frac{1}{e^{\beta(\epsilon - \mu)} - 1} d\epsilon $$
Ceci représente le nombre de particules dans des états excités $N_{ex}$.
Lorsque la température diminue ($\beta$ augmente), le potentiel chimique $\mu$ s'approche de 0 pour maintenir $N_{ex}$. Cependant, il existe une limite supérieure à la valeur de l'intégrale lorsque l'on pose $\mu = 0$ :
$$ N_{max} = \frac{V}{(2\pi)^2} \left( \frac{2m}{\hbar^2} \right)^{3/2} \int_0^\infty \frac{\sqrt{\epsilon}}{e^{\beta \epsilon} - 1} d\epsilon $$
En effectuant le changement de variable $x = \beta \epsilon$, la partie intégrale peut être calculée en utilisant la fonction gamma $\Gamma(z)$ et la fonction zêta de Riemann $\zeta(z)$ comme suit :
$$ \int_0^\infty \frac{\sqrt{\epsilon}}{e^{\beta \epsilon} - 1} d\epsilon = (k_B T)^{3/2} \int_0^\infty \frac{x^{1/2}}{e^x - 1} dx = (k_B T)^{3/2} \Gamma(3/2) \zeta(3/2) $$
Puisque $\Gamma(3/2) = \sqrt{\pi}/2$ et $\zeta(3/2) \approx 2,612$, le nombre maximum de particules pouvant être accueillies par les états excités est :
$$ N_{max} = V \left( \frac{m k_B T}{2\pi \hbar^2} \right)^{3/2} \zeta(3/2) = \frac{V}{\lambda_{dB}^3} \zeta(3/2) $$
Que se passe-t-il si le nombre total de particules $N$ dépasse $N_{max}$ ? Les particules en excès $N_0 = N - N_{max}$ n'ont d'autre choix que de se condenser dans l'état fondamental d'énergie $\epsilon = 0$, qui n'est pas inclus dans l'intégrale ($\epsilon > 0$). C'est le mécanisme mathématique de la BEC.

La température critique $T_c$ à laquelle la condensation commence est définie comme la température à laquelle $N = N_{max}(T_c)$. En résolvant cette équation pour $T_c$, nous obtenons :
$$ T_c = \frac{2\pi \hbar^2}{m k_B} \left( \frac{n}{\zeta(3/2)} \right)^{2/3} $$
(où $n = N/V$ est la densité numérique)
Cette formule donne la température de transition BEC exacte pour un gaz idéal sans interactions. La substitution de la densité de l'hélium liquide donne $T_c \approx 3,1 K$, ce qui est proche de la température réelle de la transition $\lambda$, 2,17 K. Cet accord suggère fortement que la superfluidité de l'Hélium II est fondamentalement un phénomène lié à la BEC. Cependant, parce que l'hélium liquide est un « liquide quantique fortement corrélé » avec des interactions inter-particulaires très fortes, il y a un écart par rapport au modèle des gaz parfaits.
---

## Chapitre 3 : Le modèle à deux fluides de Tisza et Landau

Pour expliquer l'étrange propriété de l'hélium superfluide selon laquelle il « s'écoule avec une viscosité nulle dans un capillaire mais présente une résistance visqueuse à un corps en rotation », László Tisza a proposé en 1938 une phénoménologie novatrice. Plus tard, en 1941, Lev Landau l'a perfectionné en tant que théorie plus raffinée basée sur les fondements microscopiques de la mécanique quantique : c'est le « modèle à deux fluides » (Two-Fluid Model).

### 3.1 Coexistence de la composante fluide normale et de la composante superfluide
Le cœur du modèle à deux fluides est de considérer l'Hélium II comme un système dans lequel deux composantes fluides ayant des propriétés physiques complètement différentes sont mélangées de manière indépendante.
La densité $\rho$ et la vitesse d'écoulement $\mathbf{v}$ de l'ensemble du système s'expriment comme la somme des deux composantes :
$$ \rho = \rho_n + \rho_s $$
$$ \mathbf{j} = \rho_n \mathbf{v}_n + \rho_s \mathbf{v}_s $$
Où,
- **Composante fluide normale ($\rho_n$)** : La composante qui a une viscosité finie et transporte de l'entropie. Elle correspond à la population de particules dans des états thermiquement excités.
- **Composante superfluide ($\rho_s$)** : La composante qui a une viscosité complètement nulle et aucune entropie (dans le même état qu'au zéro absolu). Elle correspond à la population de particules dans un état quantique macroscopique (état BEC).

Au zéro absolu ($T = 0$), tout est composé de la composante superfluide ($\rho_s = \rho, \rho_n = 0$), mais à mesure que la température augmente, la proportion de la composante normale augmente, et à $T_\lambda$, la composante superfluide disparaît ($\rho_s = 0, \rho_n = \rho$).

L'utilisation de ce modèle permet de résoudre brillamment la contradiction précédente sur la viscosité. Dans une expérience de passage à travers un tube capillaire ultra-fin, la composante normale visqueuse est arrêtée par le frottement avec les parois du tube, mais seule la composante superfluide non visqueuse s'échappe par le tube, de sorte que la viscosité apparente devient nulle. D'autre part, dans une expérience de rotation d'un cylindre dans le liquide massif, le cylindre subit un frottement avec la composante normale, de sorte qu'une viscosité finie est observée.

### 3.2 L'effet thermomécanique (effet fontaine) et l'effet mécanocalorique
La propriété de la composante superfluide de n'avoir « aucune entropie » conduit à des phénomènes étonnants où les flux de chaleur et de matière sont directement couplés. Un exemple représentatif est l'« effet thermomécanique » (Thermomechanical effect) ou « effet fontaine » (Fountain effect).

Au milieu d'un tube en forme de U, on place un filtre ultra-poreux (superfuite) rempli de poudre très fine, et on remplit les deux côtés d'Hélium II. Si on chauffe un côté du filtre avec un radiateur, le niveau de liquide du côté chauffé s'élève, et si les conditions sont réunies, l'hélium jaillit violemment d'une buse.
Le mécanisme de ce phénomène est le suivant. Lorsque la température du côté chauffé augmente, selon le modèle à deux fluides, la proportion de la composante normale $\rho_n$ dans cette région augmente, et la composante superfluide $\rho_s$ diminue. Ensuite, un gradient de potentiel chimique (similaire à la pression osmotique) se produit pour tenter d'éliminer le gradient de concentration de la composante superfluide à travers la superfuite. Comme la composante normale ne peut pas passer à travers le filtre, seule une grande quantité de la composante superfluide s'écoule du côté froid vers le côté chaud, repoussant le niveau de liquide vers le haut.
Thermodynamiquement, l'équation de London s'applique entre la différence de pression $\Delta P$ et la différence de température $\Delta T$ :
$$ \Delta P = \rho S \Delta T $$
($S$ est l'entropie par unité de masse)

Inversement, lorsque l'Hélium II est forcé à travers une superfuite, ce qui s'écoule n'est que la composante superfluide sans entropie, provoquant ainsi l'augmentation de la température du liquide restant. C'est ce qu'on appelle l'effet mécanocalorique.

### 3.3 Physique du deuxième son (Second Sound)
Dans un fluide normal, une « onde sonore » est une onde de densité de compression et de dilatation (onde de pression). Cependant, dans l'Hélium II, parce que deux champs de vitesse indépendants $\mathbf{v}_n$ et $\mathbf{v}_s$ existent, deux types d'ondes peuvent se propager.
- **Premier son (First Sound)** : Une onde dans laquelle la composante normale et la composante superfluide oscillent en phase. Cela correspond à une onde de densité normale (onde de pression).
- **Deuxième son (Second Sound)** : Une onde dans laquelle la composante normale et la composante superfluide oscillent en opposition de phase (dans des directions opposées). La densité est maintenue constante, tandis que la proportion de la composante normale (masse d'entropie) et de la composante superfluide oscille spatialement ; cela se propage donc de fait comme une « onde de température (onde thermique) ».

Dans les matériaux ordinaires, la chaleur est transférée comme un phénomène de diffusion, mais dans l'Hélium II, la chaleur se propage comme une « onde » sans atténuation à la vitesse du son (la vitesse du deuxième son). Ce phénomène a également été prédit par Landau, et sa validation expérimentale ultérieure a prouvé de manière décisive l'exactitude du modèle à deux fluides.

---

## Chapitre 4 : La vitesse critique superfluide de Landau et le spectre d'excitation élémentaire

La théorie de la condensation de Bose-Einstein était basée sur l'hypothèse d'un gaz parfait et ne pouvait donc pas expliquer les fortes interactions entre les atomes d'hélium. En fait, la superfluidité n'apparaît pas dans un gaz de Bose idéal sans interactions (elle est facilement excitée par la diffusion des impuretés). Lev Landau a formulé l'hélium liquide comme un « liquide de fond dans l'état fondamental au zéro absolu » avec un « gaz d'excitations élémentaires (Elementary Excitations) » au-dessus.

### 4.1 Phonons et rotons : Courbe de dispersion énergie-impulsion
Afin d'expliquer les propriétés thermiques de l'Hélium II, Landau a supposé la relation suivante entre l'énergie $\epsilon$ et l'impulsion $p$ des excitations élémentaires (relation de dispersion $\epsilon(p)$).

1. **Région des phonons (Région de faible impulsion)**
   Les excitations de grande longueur d'onde sont des fluctuations de la densité globale du fluide, c'est-à-dire des ondes sonores quantifiées (phonons). L'énergie est proportionnelle à l'impulsion :
   $$ \epsilon(p) = c p $$
   ($c$ est la vitesse du premier son)

2. **Région des rotons (Région de grande impulsion)**
   Lorsque l'impulsion augmente, la courbe de dispersion passe par un maximum puis possède un minimum local. Landau a nommé l'excitation autour de ce minimum un « roton ». La relation de dispersion du roton est approximée par une parabole :
   $$ \epsilon(p) = \Delta + \frac{(p - p_0)^2}{2\mu} $$
   Où $\Delta$ est l'énergie du gap du roton, $p_0$ est l'impulsion au point minimum, et $\mu$ est la masse effective du roton.

Cette étrange courbe de dispersion a été mesurée avec une grande précision par la suite lors d'expériences de diffusion inélastique de neutrons, démontrant de manière spectaculaire l'intuition géniale de Landau.

### 4.2 La preuve de l'impossibilité de diffusion sans frottement due à la vitesse critique $v_c$
La plus grande réussite de Landau a été d'utiliser cette relation de dispersion pour prouver mécaniquement le mécanisme fondamental de la superfluidité : « pourquoi l'Hélium II peut s'écouler sans frottement contre les parois » (le théorème de la vitesse critique de Landau).

Supposons qu'un objet massif de masse $M$ (par exemple, une minuscule saillie sur la paroi d'un capillaire) se déplace à une vitesse constante $v$ à travers de l'hélium liquide au zéro absolu. Pour que cet objet décélère en raison du frottement avec l'hélium, il doit transférer une partie de son énergie cinétique à l'hélium, générant une « excitation élémentaire » dans l'hélium.
Supposons qu'une excitation élémentaire d'impulsion $p$ et d'énergie $\epsilon(p)$ soit générée. D'après les lois de conservation de l'énergie et de l'impulsion, en supposant que la variation de la vitesse de l'objet soit infinitésimale, la relation suivante est vérifiée :
$$ \Delta E = \mathbf{v} \cdot \mathbf{p} = \epsilon(p) $$
Puisque $\mathbf{v} \cdot \mathbf{p} = v p \cos\theta \leq v p$, la condition pour générer une excitation élémentaire est :
$$ v \geq \frac{\epsilon(p)}{p} $$
En d'autres termes, si la vitesse de l'objet $v$ est inférieure à la valeur minimale de $\epsilon(p)/p$ pour toutes les impulsions $p$ possibles, aucune excitation élémentaire ne peut être générée, et aucune dissipation d'énergie (frottement) ne se produit. Cette vitesse limite est appelée vitesse critique de Landau $v_c$ :
$$ v_c = \min \left[ \frac{\epsilon(p)}{p} \right] $$

Si l'hélium liquide était un gaz de Bose idéal, il aurait la relation de dispersion d'une particule libre $\epsilon(p) = p^2 / 2m$, donc $v_c = \min [p/2m] = 0$, ce qui signifie que peu importe la lenteur avec laquelle il se déplace, l'excitation se produirait et ce ne serait pas un superfluide.
Cependant, dans l'hélium liquide réel, la courbe de dispersion commence linéairement ($\epsilon = c p$) en raison des interactions, de sorte que la pente près de l'origine est $c$ (vitesse du son, environ 240 m/s). En trouvant la valeur minimale sur toute la forme de la courbe de dispersion, la pente de la tangente allant vers le minimum du roton donne $v_c$, et sa valeur est d'environ 60 m/s.
(*La vitesse critique observée dans les expériences réelles est beaucoup plus petite, de l'ordre de quelques cm/s, ce qui sera expliqué plus tard par Richard Feynman et d'autres comme le mécanisme de génération de « vortex quantiques ».)

Ainsi, la présence d'un « gap » ou d'une « pente finie » dans la relation de dispersion d'énergie du système est la condition absolue qui garantit la superfluidité (écoulement sans frottement).
---

## Chapitre 5 : Vortex quantiques (Quantized Vortex) et défauts topologiques

La théorie de la vitesse critique de Landau expliquait l'origine microscopique de la superfluidité, mais la raison pour laquelle la vitesse critique observée expérimentalement était bien inférieure à la valeur théorique restait un mystère. Ce mystère a été résolu par Lars Onsager et Richard Feynman à travers la théorie des « vortex quantiques », qui a relié le problème à la phase (topologie) de la fonction d'onde macroscopique du superfluide.

### 5.1 Phase de la fonction d'onde macroscopique et quantification de la circulation
Un superfluide ayant subi une BEC est décrit par une seule fonction d'onde macroscopique $\Psi(\mathbf{r}) = \sqrt{n_0(\mathbf{r})} e^{i\theta(\mathbf{r})}$. Ici $n_0(\mathbf{r})$ est la densité numérique du condensat et $\theta(\mathbf{r})$ est la phase.
Le champ de vitesse $\mathbf{v}_s$ du superfluide est dérivé de la densité de courant de probabilité en mécanique quantique comme étant proportionnel au gradient spatial de la phase :
$$ \mathbf{v}_s = \frac{\hbar}{m} \nabla \theta $$

En dynamique des fluides, la « circulation » $\kappa$ est un indicateur du degré de rotation d'un fluide. Elle est définie comme l'intégrale de ligne du vecteur vitesse $\mathbf{v}_s$ le long d'une courbe fermée $C$.
$$ \kappa = \oint_C \mathbf{v}_s \cdot d\mathbf{r} = \frac{\hbar}{m} \oint_C \nabla \theta \cdot d\mathbf{r} $$
La partie intégrale représente la variation de phase $\Delta\theta$ après avoir fait un tour complet de la courbe fermée $C$.
Ici, il y a une exigence de la mécanique quantique que la fonction d'onde $\Psi(\mathbf{r})$ doit avoir une valeur unique en chaque point de l'espace. Par conséquent, lors du retour au point de départ après un tour le long d'une courbe fermée, la phase doit revenir à sa valeur d'origine ou être décalée d'un multiple entier de $2\pi$ :
$$ \Delta\theta = 2\pi n \quad (n = 0, \pm 1, \pm 2, \dots) $$
En substituant cela dans l'équation de la circulation, on obtient un résultat surprenant.
$$ \kappa = \frac{\hbar}{m} (2\pi n) = n \frac{h}{m} $$
C'est-à-dire que la circulation dans un superfluide ne peut pas prendre de valeurs continues, mais est complètement « quantifiée » en unités de $h/m$ (la constante de Planck $h$ divisée par la masse d'un atome d'hélium $m$). C'est ce qu'on appelle la « quantification de la circulation ».

### 5.2 Réseau de vortex dans l'hélium liquide en rotation et défauts topologiques
Lorsqu'un récipient contenant un fluide visqueux normal est mis en rotation, le fluide tout entier tourne comme un corps rigide et forme une surface parabolique. Cependant, l'hélium superfluide (sa composante superfluide) possède la propriété $\nabla \times \mathbf{v}_s = (\hbar/m) \nabla \times \nabla \theta = 0$, c'est-à-dire qu'il est irrotationnel (sans tourbillon) ; donc, même si l'on tourne lentement le récipient, le contenu ne tourne pas avec lui.
Cependant, à mesure que la vitesse de rotation augmente progressivement, au moment où elle dépasse une certaine vitesse angulaire critique, d'innombrables lignes de « vortex quantiques » (Quantized Vortex) (lignes de tourbillons) pénètrent dans le superfluide.

Au centre (cœur) d'un vortex quantique, la phase devient une singularité et ne peut pas être définie, de sorte que la densité superfluide $n_0$ tombe à zéro (c'est-à-dire qu'il devient un fluide normal ou un vide). Autour du cœur, le fluide tourne avec une circulation quantifiée $\kappa = h/m$ (généralement, l'état minimum $n=1$ est énergétiquement stable).
Si l'on augmente encore la vitesse de rotation, le nombre de vortex quantiques augmente, ils se repoussent et forment un réseau triangulaire régulier (un réseau de vortex semblable au réseau d'Abrikosov). Macroscopiquement, cette collection d'innombrables vortex quantiques se comporte comme si le fluide entier tournait comme un corps rigide.

L'écart avec la vitesse critique de Landau a également été expliqué par ces vortex quantiques. Lors de l'écoulement le long des parois d'un capillaire, même à des vitesses d'écoulement très faibles, des vortex quantiques sont générés par de microscopiques irrégularités de la paroi. L'énergie nécessaire pour créer ce vortex quantique étant bien inférieure à celle de l'excitation d'un roton, la vitesse critique expérimentale s'est avérée extrêmement faible par rapport à la valeur théorique de Landau. Les vortex quantiques agissent comme des « défauts topologiques » qui détruisent la superfluidité.

---

## Chapitre 6 : Réalisation d'une BEC gazeuse par refroidissement laser et développements vers la physique moderne

L'hélium liquide ayant des interactions inter-particulaires extrêmement fortes, le taux de condensation reste d'environ 10 % même au zéro absolu, ce qui est loin de la BEC d'un gaz parfait pur. Pour réaliser une véritable « BEC dans un gaz dilué », il était nécessaire de refroidir un gaz si dilué que les interactions interatomiques étaient négligeables, presque jusqu'au zéro absolu.

### 6.1 L'obtention de la BEC d'un gaz d'atomes alcalins
Des années 1980 aux années 1990, des technologies innovantes telles que le refroidissement par laser (refroidissement Doppler, refroidissement Sisyphe), les pièges magnétiques et le refroidissement par évaporation ont été développées, permettant de refroidir les gaz atomiques au niveau du nanokelvin ($10^{-9}$ K).
Puis, en 1995, Eric Cornell et Carl Wieman de l'Université du Colorado (JILA), en utilisant un gaz d'atomes de rubidium ($^{87}$Rb), et la même année, Wolfgang Ketterle du MIT, en utilisant un gaz d'atomes de sodium ($^{23}$Na), ont réussi, pour la première fois dans l'histoire humaine, l'observation directe de la condensation de Bose-Einstein dans des gaz dilués d'atomes alcalins. Pour cette réalisation, ils ont reçu le prix Nobel de physique en 2001.

Dans l'expérience réalisée par le groupe de Ketterle, des « franges d'interférence » claires ont été observées en faisant interférer spatialement deux BEC indépendants. C'était la preuve définitive que des masses de matière à une échelle macroscopique se comportent comme une onde de matière unique.

### 6.2 Superfluidité et transition isolant de Mott dans les réseaux optiques
La recherche moderne sur la BEC a dépassé la simple confirmation du phénomène et a évolué vers des applications en tant que « simulateurs quantiques ». Lorsqu'une BEC est introduite dans un potentiel périodique (réseau optique, Optical Lattice) créé par l'interférence de faisceaux laser opposés, les atomes se comportent comme des électrons dans le réseau cristallin d'un solide.
En ajustant l'intensité du laser, le rapport entre l'interaction entre atomes et le saut (effet tunnel vers le site adjacent) peut être contrôlé à volonté. Lorsque l'interaction est faible, les atomes se déplacent librement dans tout le système avec une phase alignée (état superfluide), mais au fur et à mesure que l'interaction se renforce, les atomes se localisent un par un sur chaque site du réseau, et la cohérence de phase macroscopique est complètement détruite, provoquant une transition de phase quantique vers l'« état isolant de Mott » (Mott Insulator).
Cette transition superfluide-isolant de Mott (observée par Greiner et al. en 2002) a ouvert la voie à un test précis du modèle de Hubbard pour les systèmes d'électrons fortement corrélés (tels que les supraconducteurs à haute température) dans un système artificiel idéal.

### 6.3 Compréhension unifiée avec la supraconductivité (BEC des paires de Cooper)
Enfin, évoquons la relation profonde entre la superfluidité et la supraconductivité. La supraconductivité peut s'interpréter comme le phénomène dans lequel les électrons de conduction (fermions) dans un métal forment des paires (paires de Cooper) par l'intermédiaire d'une force d'attraction médiée par les phonons (vibrations du réseau), et ces paires se comportent comme des bosons et subissent une BEC (théorie BCS).
Ces dernières années, la recherche sur le « crossover BCS-BEC » s'est intensifiée ; elle utilise un gaz atomique de Fermi dont on contrôle l'interaction interatomique par un champ magnétique (résonance de Feshbach) pour modifier continuellement l'état de la BEC des molécules (limite BEC) à l'état BCS des paires de Cooper (limite BCS).

La superfluidité et la BEC sont des phénomènes physiques ultimes où les lois régissant la mécanique quantique microscopique sont étendues à notre échelle macroscopique quotidienne. L'écoulement avec une viscosité nulle, la quantification de la circulation, et l'interférence des ondes de matière. Tout cela n'est rien de moins que l'aspect le plus fondamental et le plus pur de l'univers, révélé par la nature dans les conditions extrêmes du zéro absolu.
