---
title: "Microscopie électronique (TEM/SEM) de l'imagerie ultramicroscopique : La physique des faisceaux d'électrons pour dépasser la limite de diffraction de la lumière"
description: "De la théorie des ondes de matière à la conception des lentilles électromagnétiques, le monde de la très haute résolution qui permet de visualiser « un seul atome » grâce aux correcteurs d'aberration sphérique."
slug: "electron-microscopy-tem-sem-imaging-physics"
date: "2026-10-03T05:00:00+09:00"
categories: ["engineering", "physics"]
tags: ["microscopy", "electron-microscopy", "nanotechnology", "quantum-physics"]
image: "eyecatch.jpg"
---

# Introduction : Ouvrir la porte au monde ultramicroscopique, physique des faisceaux d'électrons et exploration des faisceaux quantiques

Le désir fondamental de l'humanité de « voir l'invisible » a évolué de pair avec l'histoire des instruments optiques tels que les microscopes. Depuis qu'Antonie van Leeuwenhoek a découvert des micro-organismes avec un microscope monoculaire de sa propre fabrication au 17e siècle, le microscope optique a apporté une immense révolution à la biologie, à la science des matériaux et plus généralement aux sciences naturelles. Cependant, au 20e siècle, alors que la frontière de la science s'est miniaturisée passant des cellules aux molécules, puis aux atomes, l'observation par la lumière s'est heurtée à un mur physique. C'est la « limite de diffraction d'Abbe ».

Dans cet article, nous expliquerons en profondeur, en y associant une approche mathématique, les technologies d'imagerie ultramicroscopique du microscope électronique (microscope électronique à balayage : SEM, microscope électronique en transmission : TEM) qui ont franchi les limites du microscope optique jusqu'à permettre la visualisation des atomes un par un, incluant la mécanique quantique sous-jacente, l'électromagnétisme, et les technologies de pointe de correction d'aberration sphérique. Le processus qui consiste à traiter une particule élémentaire comme l'électron en tant qu'onde de mécanique quantique et à la contrôler par un champ électromagnétique pour former une image peut être considéré comme l'un des plus beaux aboutissements de la physique appliquée jamais atteints par l'humanité.

## Chapitre 1 : Limites des microscopes optiques et le saut de de Broglie : L'aube de la nature ondulatoire et de la mécanique quantique

### 1.1 Limite de diffraction d'Abbe : Nature ondulatoire de la lumière et contraintes physiques de la fréquence spatiale
En imagerie optique, l'acte de « voir un objet » implique un processus de transformée de Fourier spatiale dans lequel un système de lentilles est utilisé pour reconstruire le front d'onde de la lumière diffusée et diffractée par l'objet. En 1873, le physicien allemand Ernst Abbe a formulé le mécanisme de formation d'image du microscope comme un phénomène de diffraction. Lorsqu'une onde plane de longueur d'onde $\lambda$ frappe un objet (par exemple un réseau de diffraction de période $d$), la lumière est diffractée à différents angles $\theta$. La condition minimale de formation de l'image est que, outre l'onde d'ordre zéro qui se propage en ligne droite, au moins l'onde de diffraction du premier ordre soit captée par la pupille (ouverture) de l'objectif et produise une interférence.

Dans l'équation fondamentale de diffraction $d \sin \theta = n\lambda$, si l'on considère la diffraction du premier ordre ($n=1$), la résolution est déterminée par l'angle maximal que la lentille peut capter (lié à l'ouverture numérique $NA = n \sin \theta$). La formule de la limite de diffraction d'Abbe est la suivante :

$$ d = \frac{\lambda}{2NA} $$

Ici, $d$ est la résolution (la distance minimale permettant de distinguer deux points), $\lambda$ est la longueur d'onde de la lumière utilisée, et $NA$ est l'ouverture numérique de l'objectif (Numerical Aperture). Plus rigoureusement, la résolution $\delta$, en tant que rayon du disque d'Airy d'une ouverture circulaire basée sur le critère de Rayleigh, est exprimée par $\delta = 0.61 \frac{\lambda}{NA}$. Dans les deux formulations, la limite montre une loi absolue de la nature : elle est proportionnelle à la longueur d'onde $\lambda$ et inversement proportionnelle à l'ouverture numérique $NA$.

Dans l'air normal (indice de réfraction du milieu $n \approx 1$), $NA$ est au maximum inférieur à 1, et même avec un objectif à immersion dans l'huile ($n \approx 1.5$), la limite se situe autour de 1,4. Puisque la longueur d'onde $\lambda$ de la lumière visible est d'environ 400 nm (violet) à 700 nm (rouge), même en utilisant la lumière de la longueur d'onde la plus courte de 400 nm et l'objectif à immersion dans l'huile le plus performant (NA = 1,4), la résolution $d$ n'est que d'environ 200 nm. Des virus de la taille de plusieurs milliers d'angströms (1 $\text{\AA} = 0,1 \text{nm}$), des molécules protéiques encore plus petites (quelques nm), et les atomes (environ 0,1 nm à 0,3 nm) ne pourront jamais être « vus » en lumière visible, peu importe le polissage de la lentille. Bien que des tentatives pour augmenter à l'extrême l'indice de réfraction du milieu $n$ (comme les lentilles à immersion liquide ou les lentilles à immersion solide) aient été faites, il est en principe impossible de franchir le mur des milliers d'angströms en raison de la nature même des ondes électromagnétiques.

### 1.2 Onde de matière de de Broglie et approche de la mécanique quantique
La clé pour briser ce mur désespérant est venue d'une direction totalement inattendue. En 1924, le physicien français Louis de Broglie a proposé l'hypothèse de l'« onde de matière (onde de de Broglie) », postulant que si la lumière possède la dualité onde-particule, alors les particules de matière dotées d'une masse, telles que les électrons, doivent également posséder une nature ondulatoire. Par analogie avec l'hypothèse des quanta de lumière d'Einstein $E = h\nu$ et la relativité restreinte $E = mc^2$, la longueur d'onde $\lambda$ de l'onde de de Broglie est inversement proportionnelle à la quantité de mouvement $p$ de la particule (le produit de sa masse $m$ par sa vitesse $v$) et s'exprime avec la constante de Planck $h$ de la façon suivante :

$$ \lambda = \frac{h}{p} = \frac{h}{mv} $$

Lorsqu'un électron est accéléré dans un champ électrique avec une différence de potentiel $V$ (tension d'accélération), l'énergie cinétique $E_k$ acquise par l'électron, avec la charge de l'électron $e$, est $E_k = eV$. Dans le domaine non relativiste, la relation entre l'énergie cinétique et la quantité de mouvement est $E_k = \frac{p^2}{2m}$, par conséquent, la quantité de mouvement $p$ est $p = \sqrt{2meV}$. En substituant cela dans l'équation de la longueur d'onde de de Broglie, on peut calculer la longueur d'onde de l'électron comme suit :

$$ \lambda = \frac{h}{\sqrt{2meV}} $$

### 1.3 Dérivation stricte de la tension d'accélération avec correction relativiste et de la longueur d'onde électronique
Dans les microscopes électroniques en transmission (TEM) réels, on utilise des tensions d'accélération extrêmement élevées, allant de dizaines de kV à plusieurs milliers de kV. Par exemple, la vitesse d'un électron accéléré à 200 kV atteint environ 70 % de la vitesse de la lumière, et environ 78 % à 300 kV. Dans de tels domaines à ultra-haute vitesse, l'effet d'augmentation de masse selon la théorie de la relativité restreinte (facteur de Lorentz $\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}$) ne peut être ignoré, et de graves erreurs surviennent avec les formules de la mécanique classique.

L'énergie totale $E$ s'exprime comme la somme de l'énergie cinétique $E_k$ et de l'énergie de masse au repos $m_0 c^2$.
$$ E = E_k + m_0 c^2 = eV + m_0 c^2 $$

D'autre part, la relation entre l'énergie relativiste et la quantité de mouvement $p$ est donnée par :
$$ E^2 = (pc)^2 + (m_0 c^2)^2 $$

En éliminant l'énergie $E$ de ces deux équations, on résout pour la quantité de mouvement $p$.
$$ (eV + m_0 c^2)^2 = (pc)^2 + (m_0 c^2)^2 $$
$$ (eV)^2 + 2eV m_0 c^2 + (m_0 c^2)^2 = (pc)^2 + (m_0 c^2)^2 $$
$$ (pc)^2 = (eV)^2 + 2eV m_0 c^2 $$
$$ p = \frac{1}{c} \sqrt{(eV)^2 + 2eV m_0 c^2} = \sqrt{2m_0 eV \left(1 + \frac{eV}{2m_0 c^2}\right)} $$

En substituant cette quantité de mouvement relativiste $p$ dans l'équation de de Broglie $\lambda = \frac{h}{p}$, on dérive la formule de la longueur d'onde du faisceau d'électrons avec la correction relativiste.
$$ \lambda = \frac{h}{\sqrt{2m_0 eV \left(1 + \frac{eV}{2m_0 c^2}\right)}} $$

En substituant les constantes physiques (constante de Planck $h \approx 6,626 \times 10^{-34} \text{ J s}$, masse au repos de l'électron $m_0 \approx 9,109 \times 10^{-31} \text{ kg}$, charge élémentaire $e \approx 1,602 \times 10^{-19} \text{ C}$, vitesse de la lumière $c \approx 2,998 \times 10^8 \text{ m/s}$), on peut calculer de manière approchée la longueur d'onde $\lambda$ [nm] par rapport à la tension d'accélération $V$ [volts] comme suit :

$$ \lambda \approx \frac{1,226}{\sqrt{V \left(1 + 0,978 \times 10^{-6} V\right)}} \text{ [nm]} $$

Utilisons cette formule pour calculer la longueur d'onde électronique pour une tension d'accélération commune dans les TEM de 200 kV ($V = 200 000$ V).
Le terme de correction entre parenthèses est $\left(1 + 0,978 \times 10^{-6} \times 200 000\right) = 1 + 0,1956 = 1,1956$.
Le calcul non relativiste (sans le terme de correction) donne $\lambda \approx 0,00274 \text{ nm}$, mais en incluant la correction relativiste, on obtient $\lambda \approx 0,00251 \text{ nm}$ (soit environ 2,5 pm). Puisqu'il y a un écart d'environ 10 %, la correction relativiste est un processus indispensable pour l'imagerie ultramicroscopique.
Cette longueur d'onde de 2,5 pm est incroyablement courte, soit environ 200 000 fois plus courte en comparaison de la longueur d'onde de la lumière visible (environ 500 nm). Selon la formule de la limite de diffraction d'Abbe, utiliser une longueur d'onde aussi courte permet de résoudre et de visualiser facilement même la distance interatomique dans un cristal (environ 0,1 à 0,3 nm). C'est le fondement théorique de la microscopie électronique, et l'une des plus grandes avancées en physique.


## Chapitre 2 : La physique des canons à électrons et des sources de faisceaux d'électrons : Comment créer une onde parfaite

Dans un microscope électronique permettant une ultra-haute résolution, il est d'une importance vitale de savoir « comment produire un faisceau d'électrons qui soit à la fois brillant, doté d'une longueur d'onde uniforme et capable d'être focalisé très finement ». Pour évaluer les performances d'une source de faisceau d'électrons (source lumineuse), les trois indicateurs physiques suivants ont une signification cruciale.

1. **Brillance (Brightness, $\beta$)**
La brillance est définie comme la densité de courant par unité de surface et par unité d'angle solide. Lors de la focalisation d'un faisceau par un système de lentilles de focalisation, la brillance est un invariant conservé dans un système de lentilles idéal, en vertu du théorème de Liouville (loi de conservation du volume dans l'espace des phases).
$$ \beta = \frac{I}{\pi r^2 \cdot \pi \alpha^2} = \frac{J}{\pi \alpha^2} $$
(Ici, $I$ est le courant du faisceau, $r$ le rayon effectif de la source, $\alpha$ le demi-angle d'ouverture du faisceau, $J$ la densité de courant)
Dans les STEM et SEM à haute résolution, étant donné qu'il est nécessaire d'obtenir un signal suffisant (un grand $I$) avec une sonde microscopique ($r$ extrêmement petit), la brillance de la source elle-même affecte directement les performances.

2. **Étalement en énergie (Energy spread, $\Delta E$)**
Les électrons émis par le canon à électrons ne possèdent pas tous une énergie unique, mais ont une distribution d'énergie due à l'énergie thermique ou aux caractéristiques de l'effet tunnel. Si cette dispersion $\Delta E$ est importante, elle provoque l'aberration chromatique (Chromatic Aberration) des lentilles électromagnétiques, dont nous parlerons plus tard, dégradant significativement la résolution.

3. **Cohérence spatiale (Spatial coherence)**
Plus la taille de la source est petite, plus la cohérence spatiale (interférence) est élevée. Pour former des franges d'interférence claires de l'onde électronique dans un TEM à haute résolution (HRTEM) ou en holographie électronique, une source de faisceau d'électrons avec une cohérence spatiale élevée (proche d'une source ponctuelle) est indispensable.

Les mécanismes des « canons à électrons » qui émettent des électrons dans le vide sont largement classés en deux types selon la manière dont les électrons franchissent la barrière de potentiel appelée travail de sortie (work function) du matériau : le type « à émission thermoïonique » et le type « à émission de champ ».

### 2.1 Les limites de l'émission thermoïonique (Thermionic Emission)
Lorsqu'une substance est chauffée à haute température, les électrons proches du niveau de Fermi acquièrent une énergie thermique $kT$ élevée ($k$ est la constante de Boltzmann, $T$ est la température absolue). Lorsque cette énergie dépasse le travail de sortie (Work function, $\Phi$) du matériau, les électrons peuvent s'échapper dans le vide. C'est ce qu'on appelle l'effet Richardson-Dushman, et la densité de courant émis $J$ est décrite par l'équation suivante :

$$ J = A T^2 \exp\left( -\frac{\Phi}{kT} \right) $$
Où $A$ est la constante de Richardson (environ $1,2 \times 10^6 \text{ A/m}^2\text{K}^2$).

Les premiers microscopes électroniques utilisaient des filaments en épingle à cheveux en tungstène (W). Le tungstène a un point de fusion élevé (environ 3400 K) et est utilisé chauffé à environ 2800 K, mais comme son travail de sortie est élevé (environ 4,5 eV), une température ultra-haute est requise pour obtenir un courant suffisant. Par conséquent, la dispersion de l'énergie thermique des électrons devient l'étalement énergétique du faisceau d'électrons, ce qui donne un étalement important d'environ 1,5 à 3,0 eV.
Cela a été amélioré par le monocristal d'hexaborure de lanthane (LaB6). Étant donné que le LaB6 a un travail de sortie nettement plus faible, d'environ 2,4 eV, il permet d'atteindre une brillance plus de 10 fois supérieure à celle du tungstène ($10^6 \text{ A/cm}^2\cdot\text{sr}$) à une température plus basse (environ 1800 K). Cependant, le type à émission thermoïonique a intrinsèquement un grand diamètre de croisement (taille de la source lumineuse virtuelle) de plusieurs dizaines de $\mu\text{m}$, avec une faible cohérence spatiale, ce qui le rend insuffisant pour l'imagerie ultramicroscopique à l'échelle nanométrique.

### 2.2 Percée de la mécanique quantique de l'émission à effet de champ (Field Emission Gun : FEG)
Le canon à électrons à émission de champ (FEG), qui utilise l'effet tunnel de la mécanique quantique, a permis d'améliorer de manière spectaculaire la brillance, la monochromaticité en énergie et la cohérence spatiale.
L'extrémité (pointe) d'un monocristal de tungstène extrêmement acérée, avec un rayon de courbure allant de quelques nm à plusieurs dizaines de nm, est maintenue à un potentiel fortement négatif par rapport à l'anode, et un champ électrique intense (de l'ordre de $10^9 \text{ V/m}$) est appliqué. La barrière de potentiel de la surface devient alors extrêmement mince, et les électrons sont directement émis dans le vide par effet tunnel quantique, sans emprunter d'énergie thermique. C'est ce qu'on appelle l'effet Fowler-Nordheim.

Il existe principalement deux méthodes pour l'émission à effet de champ.

**① Émission à effet de champ par cathode froide (Cold FEG, C-FEG)**
Les électrons sont extraits uniquement par le champ électrique intense tandis que la pointe est maintenue à température ambiante. L'énergie des électrons étant limitée à une zone extrêmement étroite autour du niveau de Fermi, l'étalement énergétique est étonnamment étroit (environ 0,25 à 0,3 eV), minimisant l'impact de l'aberration chromatique. De plus, comme la taille de la source est minuscule (quelques nm), elle se vante d'une ultra-haute brillance (plus de $10^8 \text{ A/cm}^2\cdot\text{sr}$) et d'une cohérence spatiale extrêmement élevée. Ces caractéristiques la rendent idéale pour l'holographie électronique et le STEM ultra-haute résolution avec une sonde microscopique. Cependant, lorsque des molécules de gaz résiduel s'adsorbent sur la pointe, le travail de sortie change et le courant d'émission devient instable. Il est donc difficile de l'opérer, nécessitant un ultra-vide (de l'ordre de $10^{-9}$ Pa) et un flash régulier (nettoyage de la surface par un chauffage instantané).

**② Type Schottky (Schottky FEG, émission à effet de champ thermique)**
La surface d'une pointe de monocristal de tungstène (100) est recouverte d'oxyde de zirconium (ZrO2), ce qui réduit considérablement le travail de sortie (environ 2,7 eV). La pointe est alors chauffée à environ 1800 K et simultanément, un champ électrique intense est appliqué pour extraire les électrons. Rigoureusement, ce n'est pas un effet tunnel, mais une extension de l'émission thermoïonique utilisant l'« effet Schottky », où le travail de sortie diminue de façon apparente sous l'effet du champ électrique.
Bien que l'étalement énergétique soit légèrement plus large (environ 0,7 eV) que le C-FEG, la pointe étant constamment chauffée, l'adsorption des gaz résiduels est empêchée, rendant le courant d'émission extrêmement stable sur une longue période. De plus, comme le courant total pouvant être émis à la fois est élevé, ce type de canon est largement répandu dans le monde comme source principale pour les fonctions d'analyse telles que l'EDS (spectroscopie de rayons X à dispersion d'énergie) et l'EELS (spectroscopie de perte d'énergie des électrons), ainsi que pour les SEM/TEM polyvalents à haute résolution.


## Chapitre 3 : Optique de formation d'image des lentilles électromagnétiques et le mur des aberrations : Le théorème désespérant de Scherzer

De même que la lumière est réfractée par des lentilles en verre, le rôle de dévier le faisceau d'électrons pour former une image incombe à la « lentille électromagnétique (Electromagnetic Lens) ». Dans l'optique électronique, il existe des lentilles électrostatiques utilisant des champs électriques, et des lentilles magnétiques utilisant des champs magnétiques, mais pour l'objectif et les lentilles de focalisation des microscopes électroniques, on utilise principalement des lentilles magnétiques, car elles présentent moins d'aberrations et une force de focalisation extrêmement puissante (courte distance focale).

### 3.1 Contrôle des trajectoires d'électrons par la force de Lorentz et dérivation de la distance focale
La structure de base d'une lentille magnétique est une bobine de fil de cuivre (solénoïde) recouverte d'un matériau magnétique doux tel que le fer pur (pièce polaire). Un entrefer de quelques millimètres est prévu dans la pièce polaire près de l'axe optique, et lorsqu'un courant continu traverse la bobine, un champ magnétique de fuite $B_z$ puissant et symétrique axialement se forme le long de l'axe optique (axe Z). Dans les objectifs les plus performants, un champ magnétique intense de 2 à 3 Tesla est concentré dans l'entrefer.

Lorsqu'un électron (charge $-e$, vitesse $\mathbf{v}$) entre dans ce champ magnétique $\mathbf{B}$, il subit la force de Lorentz $\mathbf{F} = -e(\mathbf{v} \times \mathbf{B})$ selon la règle de la main gauche de Fleming.
Un électron entrant avec un angle faible par rapport à l'axe optique possède une composante de vitesse $v_z$ dans la direction de l'axe optique et une composante de vitesse $v_r$ dans la direction radiale.
1. Près de l'entrée de la lentille, la vitesse radiale $v_r$ de l'électron interagit avec le champ magnétique radial de fuite $B_r$, générant une force dans la direction azimutale (direction $\theta$). Par conséquent, l'électron commence à tourner en spirale autour de l'axe optique (vitesse de rotation $v_\theta$).
2. Ensuite, cette vitesse de rotation $v_\theta$ interagit avec le puissant champ magnétique axial $B_z$ au centre de la lentille, générant une force centripète (force de convergence) $F_r = -e v_\theta B_z$ qui attire en permanence l'électron vers l'axe optique.

En résolvant l'équation du mouvement avec l'approximation paraxiale (Paraxial approximation), qui suppose que l'orbite de l'électron est proche de l'axe optique, la distance focale $f$ d'une lentille mince est dérivée comme suit :

$$ \frac{1}{f} = \frac{e}{8m_0 V_r} \int_{-\infty}^{\infty} B_z^2(z) dz $$

Ici, $V_r$ est la tension d'accélération corrigée par la relativité ($V_r = V(1 + \frac{eV}{2m_0 c^2})$).
Cette formule mathématique révèle une conséquence physique extrêmement importante. Le champ magnétique $B_z$ à l'intérieur de l'intégrale étant au carré, l'intégrale est toujours positive même si le sens du courant de la bobine est inversé pour changer la direction du champ magnétique. En d'autres termes, les lentilles électromagnétiques symétriques sur un axe n'agissent que comme des « lentilles toujours convergentes (convexes) ». Il est en principe impossible de créer une lentille divergente (concave) telle qu'on en trouve dans les lentilles optiques.

### 3.2 Classification des aberrations géométriques, aberrations sphériques et aberrations chromatiques
Tout comme les lentilles optiques, les lentilles électromagnétiques ne peuvent pas réaliser une formation d'image ponctuelle idéale et s'accompagnent inévitablement d'« aberrations (Aberrations) ». Les principales aberrations sont les suivantes :

**Aberration sphérique (Spherical Aberration, $C_s$)**
C'est un phénomène où les électrons qui entrent dans la lentille à une certaine distance de l'axe optique (électrons avec un grand angle d'incidence) sont déviés plus fortement que les électrons proches de l'axe optique, et forment une image en avant du foyer idéal. Le rayon du cercle de confusion $\Delta r_s$ dans le plan focal augmente de manière exponentielle, proportionnellement au cube de l'angle d'incidence $\alpha$.
$$ \Delta r_s = C_s \alpha^3 $$
Le coefficient d'aberration sphérique $C_s$ a généralement une valeur (quelques mm) comparable à la distance focale $f$ de la lentille. Pour augmenter la résolution, on tente de raccourcir la longueur d'onde en augmentant l'angle d'ouverture $\alpha$, mais on se heurte alors au dilemme de voir l'aberration sphérique s'accroître de façon explosive avec l'augmentation de $\alpha$.

**Aberration chromatique (Chromatic Aberration, $C_c$)**
Comme mentionné au chapitre précédent, la dispersion d'énergie de la source d'électrons $\Delta E$, ainsi que les fluctuations de la tension d'accélération $\Delta V$ et du courant de la lentille $\Delta I$, entraînent une variation de la quantité de mouvement (longueur d'onde) des électrons. Les électrons de plus faible énergie (plus lents) sont plus fortement courbés, tandis que les électrons de haute énergie (plus rapides) le sont moins, ce qui crée un décalage de la distance focale.
$$ \Delta r_c = C_c \alpha \sqrt{\left(\frac{\Delta V}{V}\right)^2 + \left(\frac{2\Delta I}{I}\right)^2 + \left(\frac{\Delta E}{E}\right)^2} $$

### 3.3 Théorème de Scherzer (Scherzer's Theorem) : Le mur infranchissable
En 1936, le physicien allemand Otto Scherzer a prouvé mathématiquement un théorème désespérant pour l'optique électronique.
« Dans toutes les lentilles électroniques sans charge d'espace et constituées de champs électromagnétiques stationnaires et symétriques de révolution, l'aberration sphérique $C_s$ et l'aberration chromatique $C_c$ sont toujours positives, et il est impossible de les réduire à zéro. »

Dans un microscope optique combinant des lentilles en verre, il est possible d'annuler complètement les aberrations en combinant habilement une lentille convexe (aberration sphérique positive) et une lentille concave (aberration sphérique négative) (ex : objectifs apochromatiques). Cependant, le théorème de Scherzer signifiait que, dans un système optique électronique où il n'existe que des lentilles convexes, peu importe le nombre de lentilles à symétrie de révolution placées en série, les aberrations ne font que s'accumuler et ne peuvent jamais être compensées.
En raison de cette malédiction, bien que la longueur d'onde de de Broglie soit de 0,002 nm, la résolution réelle des microscopes électroniques est restée d'environ 0,2 nm pendant des décennies. La manière dont ce mur a été brisé sera expliquée en détail au chapitre 6.


## Chapitre 4 : Principe de fonctionnement et observation de surface du microscope électronique à balayage (SEM)

Les microscopes électroniques se divisent en gros en SEM (Scanning Electron Microscope), qui observe la structure de surface des matériaux, et TEM (Transmission Electron Microscope), qui regarde à travers l'intérieur. Nous allons d'abord expliquer la physique et les mécanismes d'extraction d'informations du SEM, qui est le plus répandu, allant de la science des matériaux à la biologie, et à l'industrie des semi-conducteurs.

Le principe de formation d'image du SEM est d'utiliser un faisceau d'électrons extrêmement focalisé (diamètre de sonde : de quelques nm à quelques dizaines de nm) pour balayer (scanner) bidimensionnellement (directions X-Y) la surface de l'échantillon, de détecter les divers signaux générés par l'interaction entre les électrons et la matière, et de synchroniser leur intensité avec la luminosité des pixels correspondants sur un écran pour former une image. Le « grossissement $M$ » du SEM est déterminé uniquement par le rapport entre la largeur de balayage sur l'écran $W_d$ et la largeur de balayage réelle du faisceau d'électrons sur l'échantillon $W_s$ ($M = W_d / W_s$). En d'autres termes, le concept est fondamentalement différent du TEM, qui agrandit et forme une image réelle avec des lentilles.

### 4.1 Volume d'interaction (Interaction Volume) entre les électrons et la matière
Lorsque les électrons primaires accélérés (de l'ordre de quelques kV à 30 kV) pénètrent dans un échantillon solide, ils subissent un nombre infini de collisions (dispersions élastiques et inélastiques) avec les noyaux atomiques et les électrons des atomes constituant l'échantillon, diffusant progressivement vers l'intérieur tout en perdant de l'énergie. Cette zone en forme de goutte d'eau où les électrons se dispersent et s'étalent est appelée « volume d'interaction ». La profondeur et l'étendue du volume d'interaction augmentent avec une tension d'accélération plus élevée et une densité d'échantillon plus faible, atteignant jusqu'à plusieurs $\mu\text{m}$.
Au cours de ce processus, différents types de signaux sont émis depuis diverses profondeurs.

### 4.2 Électrons secondaires (Secondary Electrons : SE) et contraste topographique
Les électrons primaires subissent des dispersions inélastiques avec les électrons de valence et les électrons libres des atomes de l'échantillon, leur transférant de l'énergie et éjectant des électrons à l'extérieur. Ceux-ci sont appelés électrons secondaires. Ces électrons ont une énergie extrêmement faible (généralement moins de 50 eV) et ceux générés au plus profond de l'échantillon sont réabsorbés avant d'atteindre la surface. Par conséquent, seuls les électrons secondaires générés à la surface très peu profonde de l'échantillon (profondeur d'environ 1 à 10 nm) peuvent s'échapper dans le vide.
La quantité d'électrons secondaires émis (efficacité d'émission) dépend fortement de l'angle d'inclinaison $\theta$ de la surface de l'échantillon par rapport au faisceau incident et augmente proportionnellement à peu près à $\sec \theta$. En particulier sur les arêtes (bords) ou les surfaces inclinées, le volume d'interaction se formant juste en dessous de la surface, la probabilité d'échappement fait un bond (effet de bord). De ce fait, on obtient un contraste topographique tridimensionnel et intuitif, propre au SEM, donnant l'impression qu'une lumière oblique projette des ombres.

### 4.3 Électrons rétrodiffusés (Backscattered Electrons : BSE) et contraste de composition
Les électrons de haute énergie qui subissent une dispersion élastique (rétrodiffusion) en raison du champ coulombien puissant des noyaux atomiques de l'échantillon et qui rebondissent hors de l'échantillon presque sans perdre d'énergie, sont appelés électrons rétrodiffusés. La profondeur de génération va de quelques dizaines de nm à quelques $\mu\text{m}$.
Comme le suggère la section efficace de diffusion quantique de Rutherford, le coefficient d'émission $\eta$ des électrons rétrodiffusés augmente de façon monotone avec le numéro atomique $Z$ de l'échantillon. En d'autres termes, une grande quantité de BSE est reflétée par les régions d'éléments lourds (comme l'or ou le plomb), et moins par les régions d'éléments légers (comme le carbone ou l'aluminium). Par conséquent, l'observation de l'image BSE affiche les zones composées d'éléments lourds de façon brillante et les zones d'éléments légers de façon sombre, rendant le « contraste de composition (contraste Z) » de la surface de l'échantillon clairement visible.

### 4.4 Rayons X caractéristiques et cartographie élémentaire par analyse EDS
Lorsque des électrons primaires éjectent des électrons des couches internes d'un atome (comme la couche K) créant une vacance, l'atome passe dans un état excité. Pour résoudre cet état instable, un électron d'une couche externe (comme la couche L ou M) effectue une transition vers la lacune. À ce moment-là, une énergie correspondant à la différence de niveau d'énergie entre les deux orbites est émise sous forme d'ondes électromagnétiques (rayons X). L'énergie (ou longueur d'onde) de ces rayons X ayant une valeur spécifique pour chaque élément, ils sont appelés « rayons X caractéristiques ».
En détectant et en dispersant ces rayons X avec un spectromètre de rayons X à dispersion d'énergie (EDS : Energy Dispersive X-ray Spectrometer), on peut identifier quels éléments sont présents à quelle concentration dans une zone microscopique (analyse qualitative et quantitative). De plus, en balayant le faisceau, on peut obtenir une « image de cartographie élémentaire » montrant la distribution spatiale des éléments.


## Chapitre 5 : Le summum du microscope électronique en transmission (TEM) et du STEM : Interférence des ondes et mathématiques de la phase

Tandis que le SEM permet d'observer la surface de la matière, le microscope électronique en transmission (TEM) est l'appareil d'imagerie ultime permettant de regarder à travers la structure atomique elle-même à « l'intérieur » de la matière. Pour transmettre les électrons, l'échantillon doit être préparé sous la forme d'un film ultra-mince (utilisant des méthodes comme le FIB ou le fraisage ionique) d'une épaisseur inférieure à plusieurs dizaines de nm.

### 5.1 Mécanismes de formation d'image : Image en champ clair et image en champ sombre
Dans le TEM, le faisceau d'électrons qui traverse l'échantillon passe par l'objectif pour former d'abord un motif de diffraction (image de transformée de Fourier spatiale) dans le plan focal arrière (Back Focal Plane), et se recombine dans le plan d'image pour former une image agrandie (transformée de Fourier inverse).
En insérant un « diaphragme d'objectif » dans le plan focal arrière, on peut sélectionner uniquement des faisceaux spécifiques pour former l'image, et obtenir un contraste puissant basé sur le phénomène de diffraction.

- **Image en champ clair (Bright Field Image : image BF)**
Seule l'onde transmise (onde d'ordre 0) se propageant en ligne droite sans diffraction est sélectionnée par le diaphragme pour la formation de l'image. Les zones où l'échantillon est épais, celles composées d'éléments lourds où la diffusion est forte, ou les plans cristallins qui répondent aux conditions de réflexion de Bragg et diffractent fortement le faisceau d'électrons, apparaîtront « sombres » parce que l'intensité de l'onde transmise diminue. C'est ce qu'on appelle le contraste d'amplitude ou le contraste de diffraction.

- **Image en champ sombre (Dark Field Image : image DF)**
L'onde se propageant en ligne droite est bloquée, et seule une onde de diffraction spécifique (une onde réfléchie par un plan cristallin particulier) est sélectionnée pour former l'image. Seuls les grains cristallins ou précipités spécifiques qui génèrent cette onde de diffraction apparaissent alors « brillants » sur un fond noir, ce qui rend cette méthode extrêmement puissante pour l'identification de minuscules défauts et de champs de contrainte.

### 5.2 Mathématiques du TEM à haute résolution (HRTEM) et fonction de transfert de contraste (CTF)
La méthode qui repousse les limites de la résolution pour observer directement les réseaux cristallins et les arrangements atomiques est le HRTEM (High Resolution TEM). Ici, l'onde transmise et de nombreuses ondes de diffraction passent simultanément par le diaphragme, pour interférer les unes avec les autres sur le plan d'image.
L'onde électronique traversant l'échantillon mince subit un décalage de phase causé par le potentiel atomique (approximation de l'objet de phase faible). Cependant, le détecteur d'électrons ou l'œil humain ne peut percevoir que l'« intensité (amplitude au carré) » de l'onde, et les minuscules variations de phase n'apparaissent pas telles quelles en tant que contraste (problème de phase).

Ceci est résolu par la combinaison exquise de l'aberration sphérique de l'objectif $C_s$ et d'une quantité de défocalisation intentionnelle (défocalisation) $\Delta f$. L'aberration de la lentille et la défocalisation imposent un décalage de phase artificiel $\chi(k)$ par rapport à la fréquence spatiale $k$ de l'onde électronique (l'inverse de la longueur d'onde spatiale, $k = 1/d$). L'équation décrivant les caractéristiques de cette modulation de phase s'appelle la « fonction de transfert de contraste (Contrast Transfer Function : CTF) ».

La fonction de décalage de phase $\chi(k)$ de la CTF est strictement donnée par l'équation suivante :
$$ \chi(k) = \pi \Delta f \lambda k^2 + \frac{1}{2} \pi C_s \lambda^3 k^4 $$

La composante de contraste de l'intensité de l'image, due à l'interférence entre l'onde transmise et l'onde dispersée, est proportionnelle au sinus de ce décalage de phase, $\sin(\chi(k))$. Ainsi, dans la bande de fréquences spatiales où $\sin(\chi(k)) \approx \pm 1$, le déphasage est converti en différence d'amplitude, et un contraste élevé est obtenu.
Les termes de défocalisation $\Delta f$ et d'aberration sphérique $C_s$ peuvent être configurés pour avoir des signes opposés (par exemple, adopter une sous-focalisation $\Delta f < 0$ pour un $C_s > 0$). Il existe alors une condition de défocalisation optimale où la CTF maintient un décalage de phase constant ($\sin(\chi(k)) \approx -1$) sur une large bande de fréquences spatiales. C'est ce qu'on appelle la « défocalisation de Scherzer (Scherzer defocus) », donnée par l'équation suivante :

$$ \Delta f_S = -1,2 \sqrt{C_s \lambda} $$

En appliquant cette condition, il est possible d'observer des franges d'interférence périodiques (image du réseau) qui correspondent un à un à la disposition réelle des atomes dans le cristal sans artéfact (fausse image). La résolution ponctuelle (Scherzer resolution) dans ce cas sera $d = 0,66 C_s^{1/4} \lambda^{3/4}$.

### 5.3 Microscope électronique à balayage en transmission (STEM) et contraste Z par HAADF
En tant que dérivé du TEM, le STEM (Scanning Transmission Electron Microscope) balaie en deux dimensions l'échantillon à couche mince à l'aide d'un faisceau d'électrons extrêmement focalisé (diamètre de la sonde inférieur à 0,1 nm), puis trace et convertit l'intensité des électrons transmis et dispersés en une image.
En particulier, la technique permettant de capturer uniquement les électrons dispersés à un très grand angle (diffusion aux grands angles, au-delà de 50 à 200 milliradians) au moyen d'un détecteur annulaire s'appelle HAADF-STEM (High-Angle Annular Dark-Field STEM).

La diffusion à des angles élevés est dominée non pas par la diffraction de Bragg, mais par la diffusion inélastique (diffusion par phonons) ou la diffusion de Rutherford due aux vibrations thermiques lorsque les électrons passent près du noyau atomique. Son intensité de diffusion (section transversale) est proportionnelle à une puissance d'environ 1,7 à 2,0 du numéro atomique $Z$ ($Z^{1,7 \sim 2,0}$). C'est pourquoi l'image HAADF, presque non affectée par le contraste de diffraction ou d'interférence, fournit une « image de contraste Z pure » où les positions des éléments lourds brillent intensément.
Puisqu'il s'agit d'une imagerie incohérente, aucun phénomène d'inversion de phase (oscillation de la CTF) ne se produit. On peut ainsi interpréter intuitivement que « là où ça brille, il y a un atome ». Cela en fait un outil d'analyse superpuissant et aujourd'hui indispensable en science des matériaux pour des opérations comme la détection d'atomes dopants individuels.


## Chapitre 6 : Le miracle des technologies de correction d'aberration et la révolution digne d'un prix Nobel

### 6.1 Réalisation du correcteur d'aberration sphérique (Correcteur Cs) avec lentilles multipolaires
Comme expliqué dans le théorème de Scherzer au chapitre 3, il était considéré comme impossible de corriger l'aberration sphérique $C_s$ uniquement avec des lentilles magnétiques à symétrie de rotation. Pour surmonter cette limitation physique, il fallait concevoir habilement un champ électromagnétique non symétrique de rotation afin de créer artificiellement une « aberration sphérique négative » destinée à compenser l'aberration sphérique positive inhérente à l'objectif.
Cependant, un tel exploit nécessitait des technologies de traitement de précision extrêmement avancées et des capacités informatiques permettant de contrôler de manière indépendante et ultra-stable des dizaines d'électroaimants, ce qui fut longtemps considéré comme un « défi impossible ».

À la fin des années 1990, sur la base de la conception théorique de Harald Rose, Maximilian Haider et Knut Urban ont finalement réussi à rendre pratique un « correcteur d'aberration sphérique (Correcteur Cs) » utilisant des lentilles multipolaires (multipôles).
Le correcteur de type Rose-Haider le plus standard adopte une configuration avec deux étages de lentilles hexapolaires (Hexapole) en série, séparées par une lentille de transfert. La première lentille hexapolaire distord fortement la trajectoire des électrons avec une symétrie d'ordre trois (en forme de triangle arrondi) par rapport à l'axe optique. La deuxième lentille hexapolaire annule ensuite parfaitement cette distorsion pour la ramener à une orbite parfaitement circulaire. C'est durant ce processus global de « distorsion puis retour à la normale » qu'une « aberration sphérique négative » est générée mathématiquement, sous forme d'un effet secondaire touchant l'ensemble de la trajectoire.

En ajoutant cette aberration sphérique négative à l'aberration sphérique positive inhérente à l'objectif, il est devenu possible de régler l'aberration sphérique de tout le système sur zéro ou sur n'importe quelle valeur infime souhaitée.
L'accomplissement de cette technologie a permis à la résolution spatiale des TEM et STEM de franchir aisément le mur de 0,1 nm, et d'atteindre aujourd'hui le domaine époustouflant du sous-angström de 0,04 nm (40 pm). Ainsi, que ce soit les réseaux de liaisons covalentes des éléments légers tels que le silicium ou le carbone, les atomes dopants isolés cachés dans un réseau cristallin, ou même les positions d'éléments ultraminces à faible dispersion comme le lithium et l'hydrogène, tout peut être visualisé directement à l'échelle d'« un seul atome » au sens propre du terme.

### 6.2 Cryomicroscopie électronique (Cryo-EM) et analyse de la structure tridimensionnelle des biomolécules
Parallèlement à la révolution de la correction des aberrations matérielles, c'est la technologie de la « cryomicroscopie électronique (Cryo-EM) » qui a apporté le plus grand changement de paradigme à la microscopie électronique du 21e siècle, particulièrement en sciences de la vie. Pour leurs brillantes réalisations, Jacques Dubochet, Joachim Frank et Richard Henderson ont reçu le prix Nobel de chimie 2017.

Les macromolécules biologiques, telles que les protéines et les acides nucléiques, fonctionnent dans un état riche en eau. Placés dans le vide élevé d'un microscope électronique, ils se déshydratent instantanément et leur structure s'effondre. De plus, exposés à un faisceau d'électrons, ils se carbonisent immédiatement à cause des dommages radiatifs (Radiation damage). Il était donc considéré comme impossible en principe d'observer directement des échantillons biologiques dans leur état natif (Native state) en TEM.

Dans les années 1980, Dubochet et son équipe ont mis au point une méthode de congélation rapide (taux de refroidissement de $10^5 \text{ K/s}$ ou plus) des biomolécules en suspension aqueuse, en utilisant de l'éthane liquide, empêchant les molécules d'eau d'avoir le temps de former des cristaux de glace, figeant ainsi les molécules dans de la « glace amorphe (glace vitreuse) » (méthode de cryofixation). Cela a permis de préserver intacte la structure de l'échantillon sous vide tout en bénéficiant de l'effet d'atténuation des dommages radiatifs lié à la basse température (cryoprotection).

De son côté, Frank et ses collaborateurs ont développé un algorithme mathématique d'« analyse de particules isolées (Single Particle Analysis : SPA) » pour reconstruire en 3D la structure tridimensionnelle. Ce procédé s'appuie sur la classification, l'alignement et le calcul de la moyenne, par ordinateur, d'innombrables images 2D en transmission bruitées, de la même molécule prise à l'état cryogénique (les molécules pointant selon des angles aléatoires dans la glace).

Récemment, l'émergence d'une nouvelle technologie de caméra appelée détecteur direct d'électrons (Direct Electron Detector) a amélioré drastiquement l'efficacité quantique tout en permettant l'enregistrement de vidéos par de multiples prises espacées de l'ordre de la milliseconde. Il est ainsi devenu possible de corriger par logiciel les légères dérives de l'échantillon dues à l'irradiation du faisceau d'électrons. La résolution de l'analyse de particules individuelles en Cryo-EM a atteint environ 1,5 $\text{\AA}$. Cela surpasse la cristallographie aux rayons X, permettant de cartographier la structure atomique des protéines membranaires et des complexes gigantesques. C'est grâce à cette technologie que la structure 3D de la protéine Spike du nouveau coronavirus a pu être élucidée si rapidement. Les technologies d'imagerie ultramicroscopique se trouvent ainsi aux avant-postes de la découverte de médicaments, intimement liés à la santé de l'humanité.

# Conclusion : Les « yeux » du futur tissés par la physique

Depuis la prise de conscience de la limite d'Abbe face au mur immense qu'est la longueur d'onde de la lumière, l'étincelle de génie de la mécanique quantique avec l'onde de matière de de Broglie, jusqu'au contrôle minutieux de la force de Lorentz par des lentilles électromagnétiques, et enfin le miracle de la technologie de correction d'aberration sphérique triomphant du théorème de Scherzer. L'histoire du microscope électronique n'est rien de moins que l'histoire d'un formidable défi relevé par l'intellect humain et l'ingénierie face aux contraintes physiques du monde naturel.
Les ondes d'électrons, prédites par les équations de la mécanique quantique, servent aujourd'hui d'« œil du futur révélant directement la forme des atomes » dans tous les domaines scientifiques, de la science des matériaux à la biologie structurale.
À l'avenir, avec les avancées des microscopes électroniques ultrarapides (4D-EM : Ultrafast Electron Microscopy), qui poussent la résolution temporelle à l'extrême (picoseconde/femtoseconde), et avec les progrès de la reconstruction d'images par l'IA, nous deviendrons capables d'assister de nos propres yeux au moment même où « les atomes bougent, se lient et où les réactions chimiques progressent ». L'exploration du monde de l'ultramicroscopique ne connaît pas de limites et continuera, sans nul doute, à éclairer de nouveaux mondes inconnus.
