---
title: "La physique de l'antimatière et le mystère de l'asymétrie cosmique : de l'équation de Dirac à la violation de CP"
description: "Les solutions d'énergie négative prédites par l'équation de Dirac. La découverte du positron, la production et l'annihilation de paires, et la cosmologie de 'pourquoi seule la matière est restée'."
slug: "antimatter-physics-cp-violation-asymmetry"
date: "2026-10-03T05:00:00+09:00"
categories: ["physics", "quantum"]
tags: ["particle-physics", "antimatter", "dirac-equation", "cosmology"]
image: "eyecatch.jpg"
---

# La physique de l'antimatière et le mystère de l'asymétrie cosmique : de l'équation de Dirac à la violation de CP

L'un des plus grands mystères de la physique moderne est le problème de l'asymétrie baryonique : "Pourquoi notre univers contient-il de la matière, et presque pas d'antimatière ?". Dans cet article, en partant de l'équation de Dirac — née de la synthèse de la mécanique quantique et de la relativité restreinte — nous expliquerons de manière extrêmement détaillée la découverte de l'antimatière, les mécanismes de brisure de symétrie, et l'avant-garde des défis cosmologiques.

## Chapitre 1 : Les luttes et les prédictions de Paul Dirac

### Contexte historique et difficultés théoriques dans l'unification de la relativité restreinte et de la mécanique quantique
À la fin des années 1920, la physique faisait face à un défi extrêmement ardu : comment unifier ses deux piliers massifs, à savoir la théorie de la relativité restreinte proposée par Albert Einstein en 1905, et la mécanique quantique, construite par la mécanique matricielle de Heisenberg et la mécanique ondulatoire de Schrödinger. L'équation de Schrödinger est non relativiste et peut être obtenue en remplaçant l'énergie $E$ et la quantité de mouvement $p$ dans la relation $E = \frac{p^2}{2m}$ par les opérateurs $E \to i\hbar \frac{\partial}{\partial t}$ et $\mathbf{p} \to -i\hbar \nabla$, en se basant sur le principe de correspondance fondamental de la mécanique quantique. Bien que cette équation ait magnifiquement expliqué le spectre de l'atome d'hydrogène, elle ne pouvait pas décrire de manière auto-cohérente les effets relativistes tels que le spin de l'électron et la structure fine.

Pour surmonter cela, les physiciens sont partis de la relation relativiste énergie-quantité de mouvement $E^2 = \mathbf{p}^2c^2 + m^2c^4$. L'application des substitutions d'opérateurs mentionnées ci-dessus à cette relation donne la fameuse équation de Klein-Gordon (désormais, en suivant la convention de la physique des particules moderne, nous utiliserons le système d'unités naturelles $\hbar=c=1$) :
$$ (\partial^\mu \partial_\mu + m^2)\phi = 0 $$
Ou, en utilisant le d'alembertien $\Box = \partial^\mu \partial_\mu = \frac{\partial^2}{\partial t^2} - \nabla^2$, elle peut s'écrire :
$$ (\Box + m^2)\phi = 0 $$
Cependant, l'équation de Klein-Gordon présentait deux problèmes fatals qui n'existaient pas dans l'équation de Schrödinger.

Premièrement, comme il s'agit d'une équation différentielle du second ordre par rapport au temps, on peut assigner arbitrairement comme conditions initiales non seulement $\phi(t=0, \mathbf{x})$ mais aussi $\partial_t \phi(t=0, \mathbf{x})$. Par conséquent, la densité de probabilité $\rho = j^0 = i(\phi^* \partial_t \phi - \phi \partial_t \phi^*)$, définie à partir du courant conservé satisfaisant l'équation de continuité $\partial_\mu j^\mu = 0$, peut prendre non seulement des valeurs positives mais aussi négatives. Le concept de "probabilité négative" était en totale contradiction avec l'interprétation probabiliste de la mécanique quantique de l'époque (la règle de Born).

Deuxièmement, en substituant une solution d'onde plane $\phi(x) = e^{-ip \cdot x}$, on obtient $E^2 = \mathbf{p}^2 + m^2$, ce qui introduit inévitablement des solutions d'énergie négative $E = -\sqrt{\mathbf{p}^2 + m^2}$ en plus des solutions d'énergie positive $E = +\sqrt{\mathbf{p}^2 + m^2}$. Si les états d'énergie négative existaient, toutes les particules dans la nature tomberaient sans fin (désintégration en cascade) vers des états d'énergie de plus en plus bas en émettant des photons (rayons gamma), entraînant l'effondrement de la stabilité de la matière.

### Dérivation rigoureuse de l'équation de Dirac et structure algébrique des matrices Gamma
En 1928, le jeune génie de la physique britannique Paul Dirac a conçu une idée originale pour résoudre ce "problème de la densité de probabilité négative" : construire une équation différentielle qui soit du premier ordre non seulement dans ses dérivées spatiales mais aussi dans ses dérivées temporelles. Pour que les coordonnées de temps et d'espace soient traitées de manière relativiste sur un pied d'égalité, les dérivées spatiales devaient également être du premier ordre. Il a donc postulé le hamiltonien linéaire suivant :
$$ H = \alpha_1 p_1 + \alpha_2 p_2 + \alpha_3 p_3 + \beta m = \boldsymbol{\alpha} \cdot \mathbf{p} + \beta m $$
L'équation $i\frac{\partial \psi}{\partial t} = H\psi$, obtenue en appliquant le principe de correspondance $E \to i\frac{\partial}{\partial t}$, doit être connectée de manière cohérente à la relation relativiste $H^2 = \mathbf{p}^2 + m^2$. En d'autres termes, le carré du hamiltonien doit correspondre à l'équation de Klein-Gordon.
$$ H^2 = (\sum_{i=1}^3 \alpha_i p_i + \beta m)^2 = \sum_{i=1}^3 \alpha_i^2 p_i^2 + \sum_{i < j} (\alpha_i \alpha_j + \alpha_j \alpha_i)p_i p_j + \sum_{i=1}^3 (\alpha_i \beta + \beta \alpha_i)p_i m + \beta^2 m^2 $$
Pour que ceci soit identiquement égal à $\mathbf{p}^2 + m^2$, il est inévitable de déduire que les coefficients $\alpha_i$ et $\beta$ ne peuvent pas être des nombres réels ou complexes commutatifs ordinaires, mais doivent être des objets mathématiques non commutatifs (matrices) satisfaisant aux relations d'anticommutation suivantes :
$$ \alpha_i^2 = I, \quad \beta^2 = I $$
$$ \{\alpha_i, \alpha_j\} \equiv \alpha_i \alpha_j + \alpha_j \alpha_i = 0 \quad (i \neq j) $$
$$ \{\alpha_i, \beta\} \equiv \alpha_i \beta + \beta \alpha_i = 0 $$
Toutes ces matrices doivent être hermitiennes ($\alpha_i^\dagger = \alpha_i, \beta^\dagger = \beta$) et de trace nulle ($\mathrm{Tr}(\alpha_i) = 0$). Comme elles ne prennent que les valeurs propres $+1$ et $-1$ et ont une trace nulle, il est prouvé que la dimension des matrices doit être paire. En dimension $2 \times 2$, seules les matrices de Pauli (trois types) peuvent être construites pour anticommuter mutuellement, de sorte que pour former quatre matrices indépendantes $\alpha_1, \alpha_2, \alpha_3, \beta$, il faut au moins des matrices de dimension $4 \times 4$.

Dirac a réécrit cette équation sous une forme où la covariance de Lorentz de l'espace-temps à quatre dimensions devient plus évidente. En multipliant l'équation entière par $\beta$ par la gauche, il a défini les matrices gamma $\gamma^\mu$ comme suit :
$$ \gamma^0 = \beta, \quad \gamma^i = \beta \alpha_i \quad (i=1,2,3) $$
Ensuite, l'équation de Dirac est écrite de manière concise comme l'une des plus belles équations symbolisant la profondeur de la nature :
$$ (i\gamma^\mu \partial_\mu - m)\psi = 0 $$
Ou, en utilisant la notation slash de Feynman ($\not{\partial} \equiv \gamma^\mu \partial_\mu$) :
$$ (i\not{\partial} - m)\psi = 0 $$
Ici, les matrices gamma $\gamma^\mu$ satisfont aux relations d'anticommutation, qui sont les relations fondamentales de l'algèbre de Clifford associées au tenseur métrique $g^{\mu\nu} = \mathrm{diag}(1, -1, -1, -1)$ :
$$ \{ \gamma^\mu, \gamma^\nu \} = \gamma^\mu \gamma^\nu + \gamma^\nu \gamma^\mu = 2g^{\mu\nu}I_4 $$
Avec l'introduction de cette structure algébrique, on a découvert que la fonction d'onde $\psi$ n'était pas seulement une fonction scalaire, mais un "spineur de Dirac" comportant quatre composantes complexes. En raison de leurs propriétés de transformation sous les rotations spatiales, ces quatre composantes possédaient une structure extrêmement riche décrivant simultanément deux degrés de liberté de spin (spin vers le haut et spin vers le bas) et deux degrés de liberté pour les particules et les antiparticules.

De plus, en tant que représentations spécifiques des matrices gamma (liberté de représentation), il existe la "représentation de Dirac", utile dans la région des basses énergies, et la "représentation de Weyl (chirale)", qui démontre sa puissance dans les régions d'ultra-haute énergie et dans les discussions sur la chiralité (droitier et gaucher). Les matrices gamma dans la représentation de Weyl sont écrites en utilisant les matrices de Pauli $\sigma^i$ comme suit :
$$ \gamma^0 = \begin{pmatrix} 0 & I_2 \\ I_2 & 0 \end{pmatrix}, \quad \gamma^i = \begin{pmatrix} 0 & \sigma^i \\ -\sigma^i & 0 \end{pmatrix} $$

### Les solutions d'énergie négative et la "mer de Dirac"
Bien que l'équation de Dirac décrivît parfaitement les fermions de spin $1/2$, les solutions d'énergie négative $E = -\sqrt{p^2 + m^2}$ subsistaient. Pour résoudre ce problème, Dirac a proposé l'hypothèse de la "mer de Dirac" : "le vide est un état où tous les états d'énergie négative sont complètement remplis par des électrons". En raison du principe d'exclusion de Pauli, un électron ne peut pas tomber dans un état d'énergie négative déjà rempli. Si un rayon gamma ou un phénomène similaire donne suffisamment d'énergie (plus de $2mc^2$) à un électron dans un état d'énergie négative, l'électron saute vers un état d'énergie positive (création d'un électron normal), laissant un "trou" dans la mer. Ce trou se comporte comme une particule avec une charge positive et une énergie positive. C'était la prédiction théorique de "l'antiparticule (positron)".

## Chapitre 2 : La découverte expérimentale du positron et des antiparticules

### La découverte du positron et la physique de la chambre à brouillard
En 1932, quatre ans seulement après la prédiction de Dirac, le physicien américain Carl Anderson a découvert les traces d'une particule inconnue à l'aide d'une chambre à brouillard lors de son observation des rayons cosmiques au California Institute of Technology. Une chambre à brouillard est un appareil rempli de vapeur d'alcool sursaturée ; lorsqu'une particule chargée la traverse, elle ionise la vapeur, formant de minuscules gouttelettes le long de sa trajectoire et visualisant ainsi son parcours. Anderson a placé la chambre à brouillard entre de puissants électroaimants (champ magnétique $B$) et a installé une plaque de plomb de 6 millimètres d'épaisseur en son centre.
Lorsqu'une particule chargée se déplace dans un champ magnétique, elle subit la force de Lorentz $\mathbf{F} = q(\mathbf{v} \times \mathbf{B})$ et trace un arc de cercle. Le rayon de courbure $R$ dépend de la quantité de mouvement $p$ de la particule et de sa charge $q$, satisfaisant la relation $p = qBR$. Les traces observées par Anderson avaient un plus petit rayon de courbure après avoir traversé la plaque de plomb (car la particule avait perdu de l'énergie et ralenti), confirmant que la particule voyageait du bas vers le haut. D'après sa direction de déplacement et sa façon de se courber, il a été déterminé que cette particule portait une "charge positive". De plus, d'après l'épaisseur de la trace (perte d'ionisation, selon la formule de Bethe-Bloch), il est apparu clairement que sa masse était beaucoup plus légère que celle d'un proton et à peu près égale à celle d'un électron. Ce fut la découverte historique du "positron", le moment où la théorie des "trous" de Dirac s'est avérée être une réalité physique. Pour cette réalisation, Anderson a reçu le prix Nobel de physique en 1936.

### Génération d'antiprotons et d'atomes d'antihydrogène : l'ère des accélérateurs à haute énergie
Les physiciens étaient convaincus que si une antiparticule pour l'électron existait, une antiparticule pour le proton — un "antiproton" — devait également exister. Cependant, parce que la masse d'un proton (environ 938 MeV/$c^2$) est d'environ 1836 fois celle d'un électron, provoquer la production de paires $p + p \to p + p + p + \bar{p}$ nécessite une énorme quantité d'énergie : au moins $4m_p c^2$ dans le référentiel du centre de masse, ce qui correspond à environ 5,6 GeV dans le référentiel du laboratoire (avec un proton cible stationnaire).
En 1955, Emilio Segrè et Owen Chamberlain ont finalement découvert l'antiproton en faisant entrer en collision des protons de haute énergie accélérés à 6,2 GeV dans une cible en cuivre et en mesurant précisément leur quantité de mouvement et leur temps de vol, en utilisant le "Bevatron" du laboratoire national Lawrence Berkeley, qui était à l'époque l'un des plus grands accélérateurs synchrotrons à protons au monde.
Plus tard, en 1995, à l'Anneau d'Antiprotons de Basse Énergie (LEAR) du CERN (Organisation européenne pour la recherche nucléaire), le tout premier "antiatome" — l'atome d'antihydrogène — a été créé en combinant des antiprotons et des positrons. Cela a permis de réaliser des vérifications précises comparant le comportement électromagnétique, la constante de structure fine et la constante de Rydberg de l'antimatière à ceux de la matière normale.

## Chapitre 3 : Production de paires, annihilation de paires, et la loi de conservation de l'énergie

### Le zénith de $E=mc^2$ : production de paires et annihilation de paires
Lorsque l'antimatière et la matière se rencontrent, les deux s'annihilent complètement, et la totalité de leur masse est convertie en énergie. On appelle cela "l'annihilation de paires". Lorsqu'un électron et un positron s'annihilent au repos, une énergie d'exactement $2m_ec^2 \approx 1,022 \text{ MeV}$ est libérée, conformément à la formule d'équivalence masse-énergie d'Einstein $E=mc^2$. Pour satisfaire à la loi de conservation de la quantité de mouvement, deux rayons gamma (511 keV chacun) sont généralement émis dans des directions opposées.
$$ e^- + e^+ \to \gamma + \gamma $$
Inversement, lorsqu'un rayon gamma de haute énergie passe près d'un noyau atomique, une "production de paires" se produit, où une paire électron-positron est créée à partir de l'énergie du rayon gamma.

### Applications médicales pour les diagnostics TEP
Ce rayon gamma d'annihilation de 511 keV forme la base de la "TEP (Tomographie par Émission de Positons)", un puissant outil de diagnostic dans la médecine moderne. Lorsqu'un médicament radioactif incorporant une infime quantité d'un nucléide émetteur de positons (comme le fluor 18) est administré à un patient, il s'accumule dans les zones du corps où le métabolisme est actif (comme les cellules cancéreuses). Les positons émis parcourent quelques millimètres avant de subir une annihilation de paires avec les électrons environnants, libérant deux rayons gamma à exactement 180 degrés l'un de l'autre. Un anneau de détecteurs placé autour du corps mesure simultanément ces rayons gamma (mesure de coïncidence), permettant une imagerie tridimensionnelle de haute précision de l'endroit exact où l'annihilation s'est produite. Le phénomène physique ultime de l'antimatière est aujourd'hui couramment utilisé en première ligne pour sauver des vies.

## Chapitre 4 : Brisures de symétrie : C, P, CP, et le théorème CPT

### Les symétries discrètes (C, P, T)
Les trois symétries fondamentales suivantes en physique sont importantes :
- **Symétrie C (Conjugaison de charge)** : L'opération d'échange des particules avec les antiparticules. Les signes de la charge et du moment magnétique sont inversés.
- **Symétrie P (Parité)** : L'opération d'inversion des coordonnées spatiales ($\mathbf{x} \to -\mathbf{x}$). Le fameux reflet dans le miroir.
- **Symétrie T (Renversement du temps)** : L'opération d'inversion de l'écoulement du temps ($t \to -t$).

Pendant longtemps, on a cru que les interactions fondamentales de la nature étaient invariantes (symétriques) sous ces opérations. Cependant, en 1956, C.N. Yang et T.D. Lee ont proposé que "la symétrie de parité pourrait être brisée dans l'interaction faible".

### L'expérience de Wu et la brisure de la symétrie P
En 1957, Madame Wu (Chien-Shiung Wu) a observé la désintégration bêta de noyaux de cobalt-60 refroidis à des températures cryogéniques. En alignant les spins des noyaux avec un champ magnétique et en examinant la direction de l'émission d'électrons, elle a découvert que les électrons étaient principalement émis dans la direction opposée au spin. Cela signifiait que les lois physiques sont différentes dans un monde miroir (un monde à parité inversée), démontrant une brisure définitive de la symétrie P. La nature chirale de l'interaction faible — le fait qu'elle n'agit que sur les particules "gauchères" — a été révélée.
Même si P est brisée, on pensait que l'application d'une "transformation CP" — c'est-à-dire l'échange de particules avec des antiparticules (C) tout en effectuant simultanément une réflexion spéculaire (P) — préserverait la symétrie.

### Violation de CP par Cronin et Fitch
Cependant, en 1964, James Cronin et Val Fitch ont découvert dans une expérience de désintégration de mésons K neutres (kaons) que la symétrie CP est brisée avec une probabilité extrêmement rare (environ 0,2 %). Le méson K neutre à longue durée de vie ($K_L$), qui devrait être un état propre de CP, s'est désintégré en deux pions, qui ont une valeur propre de CP différente. Cette découverte a été choquante car la violation de CP implique qu'il existe une loi physique capable de distinguer la "matière" de l'"antimatière" de manière absolue.

Notez que le "théorème CPT" est considéré comme le théorème le plus robuste de la théorie quantique des champs. Toute théorie quantique des champs locale et invariante de Lorentz doit être complètement invariante sous l'inversion simultanée de C, P et T. Ainsi, en supposant le théorème CPT, le fait que la symétrie CP soit brisée implique que la symétrie T (symétrie de renversement du temps) est également brisée.

## Chapitre 5 : Les trois conditions de Sakharov et le mystère de l'asymétrie baryonique

### "Pourquoi l'Univers est-il rempli uniquement de matière ?"
Selon les observations actuelles, notre univers ne contient ni galaxies ni étoiles faites d'antimatière ; il est presque entièrement composé de matière. Immédiatement après le Big Bang, dans l'univers primordial, la matière et l'antimatière ont dû être créées en quantités égales à partir d'une immense énergie thermique. S'il y avait eu une symétrie parfaite, toutes les paires particule-antiparticule se seraient annihilées au fur et à mesure que l'univers se refroidissait, laissant l'univers actuel comme un espace vide rempli uniquement de lumière (photons). Le fait que la matière ait survécu au rythme d'à peine une sur environ dix milliards de paires particule-antiparticule a formé les étoiles actuelles et nous-mêmes. C'est ce qu'on appelle "l'asymétrie baryonique". Le rapport de la densité numérique baryonique sur la densité numérique des photons dans l'univers, $\eta = n_B / n_\gamma$, est connu grâce aux observations du fond diffus cosmologique (CMB) par les satellites WMAP et Planck pour être une valeur extrêmement faible mais d'une importance cruciale de $\eta \approx 6 \times 10^{-10}$.

### Les trois conditions de Sakharov et leur contexte physique et mathématique
En 1967, le physicien soviétique Andreï Sakharov a formulé trois conditions essentielles pour qu'un univers dominé par la matière ($B > 0$) émerge d'un état où la matière et l'antimatière étaient égales ($B=0$) dans l'univers primordial. Celles-ci sont maintenant connues sous le nom de "conditions de Sakharov" et forment la base de la cosmologie.

1. **Violation du nombre baryonique ($B$)** :
Il doit y avoir des processus où le nombre de baryons (protons, neutrons, etc.) moins le nombre d'antibaryons change. Exprimé mathématiquement, si l'état initial est $|i\rangle$ et l'état final est $|f\rangle$, il doit y avoir des réactions dans la probabilité de transition $\Gamma(i \to f)$ telles que $B_i \neq B_f$. Dans le modèle standard, le nombre baryonique est conservé dans le cadre de la théorie des perturbations, mais il existe le "processus du sphaléron", qui brise la somme des nombres baryonique et leptonique $B+L$ à travers des anomalies quantiques non perturbatives. Dans les Théories de Grande Unification (GUT), des processus comme la désintégration du proton violent naturellement le nombre baryonique, médiés par le boson $X$, etc.

2. **Violation de la symétrie C et de la symétrie CP** :
Il doit y avoir une différence dans les taux de réaction entre les particules et les antiparticules. Même s'il existait une réaction violant le nombre baryonique $X \to Y + B$, si la symétrie C était conservée, l'antiréaction de ses antiparticules $\bar{X} \to \bar{Y} + \bar{B}$ se produirait exactement avec la même probabilité, entraînant une augmentation nette nulle du nombre baryonique total de l'univers. Ainsi, $\Gamma(X \to Y + B) \neq \Gamma(\bar{X} \to \bar{Y} + \bar{B})$ est requise. De plus, pour moyenner l'asymétrie par rapport aux directions spatiales, la violation non seulement de la symétrie P, mais aussi de la symétrie CP est essentielle.

3. **Départ de l'équilibre thermique (réalisation d'un état hors équilibre)** :
Si le système est en équilibre thermique, même si la CP est brisée, le principe du bilan détaillé (une conséquence de l'hypothèse ergodique et du théorème CPT) garantit que les masses des particules et des antiparticules sont égales, et que le nombre baryonique s'annule en moyenne dans les distributions de Fermi-Dirac ou de Bose-Einstein. Par conséquent, un état hors équilibre thermique doit être réalisé, que ce soit par l'expansion rapide de l'univers primordial (un état où le taux d'expansion de Hubble $H$ dépasse le taux d'interaction $\Gamma$, $H > \Gamma$) ou à travers une transition de phase du premier ordre comme la transition de phase électrofaible.

### La théorie de Kobayashi-Maskawa et l'expansion mathématique du modèle à six quarks
C'est un article monumental de 1973 de Makoto Kobayashi et Toshihide Maskawa qui a expliqué théoriquement la deuxième condition de Sakharov, la "violation de la symétrie CP". Ils ont mathématiquement prouvé que si au moins trois générations (six types) de quarks existent, une phase complexe irréductible apparaît dans la matrice unitaire représentant le mélange intergénérationnel entre les états propres de l'interaction faible et les états propres de masse des quarks, et que cela induit naturellement la violation de CP.

La matrice de Cabibbo-Kobayashi-Maskawa (CKM) $V$ est une matrice unitaire $3 \times 3$ satisfaisant à $V^\dagger V = I$. Une matrice unitaire générale $N \times N$ a $N^2$ paramètres réels, mais la redéfinition des phases des champs de quarks (absorption des phases non physiques) permet d'éliminer $2N-1$ paramètres. Ainsi, le nombre de paramètres physiques est $N^2 - (2N-1) = (N-1)^2$.
- Pour $N=2$ (deux générations), il y a $(2-1)^2 = 1$ paramètre, correspondant à l'angle de Cabibbo $\theta_c$. Aucune phase complexe n'existe, et la symétrie CP n'est pas brisée.
- Pour $N=3$ (trois générations), il y a $(3-1)^2 = 4$ paramètres : trois angles d'Euler (angles de mélange) $\theta_{12}, \theta_{23}, \theta_{13}$ et un "angle de phase de violation CP" $\delta$. Ce $\delta$ est la source même de la violation de CP.

Dans la représentation standard (convention PDG), la matrice CKM s'écrit comme suit :
$$ V_{CKM} = \begin{pmatrix} c_{12}c_{13} & s_{12}c_{13} & s_{13}e^{-i\delta} \\ -s_{12}c_{23} - c_{12}s_{23}s_{13}e^{i\delta} & c_{12}c_{23} - s_{12}s_{23}s_{13}e^{i\delta} & s_{23}c_{13} \\ s_{12}s_{23} - c_{12}c_{23}s_{13}e^{i\delta} & -c_{12}s_{23} - s_{12}c_{23}s_{13}e^{i\delta} & c_{23}c_{13} \end{pmatrix} $$
Où $c_{ij} = \cos\theta_{ij}$ et $s_{ij} = \sin\theta_{ij}$. L'ampleur de la violation de CP est proportionnelle à "l'invariant de Jarlskog" $J$, construit à partir des éléments de cette matrice.
$$ \mathrm{Im}(V_{us} V_{cb} V_{ub}^* V_{cs}^*) = J = c_{12}c_{23}c_{13}^2 s_{12}s_{23}s_{13}\sin\delta $$
Les valeurs expérimentales actuelles donnent $J \approx 3 \times 10^{-5}$. Ce mécanisme de violation de CP dans le Modèle Standard a été prouvé avec une précision remarquablement élevée en tant qu'asymétrie dans les désintégrations de mésons B lors des expériences des usines à mésons B (l'expérience Belle au KEK et l'expérience BaBar au SLAC), ce qui a valu à Kobayashi et Maskawa le prix Nobel de physique en 2008.

Cependant, d'un point de vue cosmologique, un problème définitif existe. Le paramètre d'asymétrie baryonique prédit à partir de cet invariant de Jarlskog n'est que d'environ $\eta \sim \frac{J \cdot \Delta m^2}{T^{12}} \sim 10^{-20}$ à une échelle de température de l'univers de $T \sim 100 \text{ GeV}$, ce qui est inférieur de plus de dix ordres de grandeur à la valeur réelle observée de $\eta \approx 6 \times 10^{-10}$. En d'autres termes, bien que la théorie de Kobayashi-Maskawa ait magnifiquement expliqué la violation de CP dans le cadre de la physique des particules, on sait qu'elle est largement insuffisante pour expliquer la disparition de l'antimatière dans l'univers. Ce fait suggère fortement l'existence inévitable d'une "Nouvelle Physique" au-delà du Modèle Standard, telle que la "leptogénèse" issue de la phase CP des neutrinos, ou des théories de supersymétrie.

## Chapitre 6 : La frontière de l'antimatière

### Le décélérateur d'antiprotons (AD) du CERN et l'expérience ALPHA
La recherche sur l'antimatière se poursuit aujourd'hui à la pointe du progrès. Le décélérateur d'antiprotons (AD) du CERN "décélère" les antiprotons de haute énergie et les mélange avec des positrons cryogéniques pour synthétiser des atomes d'antihydrogène. Des groupes de recherche collaboratifs internationaux comme l'expérience ALPHA utilisent des bouteilles magnétiques (pièges de Penning et pièges de Ioffe-Pritchard) pour piéger des atomes d'antihydrogène neutres et étudier leurs propriétés spectroscopiques.
Depuis 2018, il a été confirmé avec une précision d'un billionième que la fréquence de la transition 1S-2S dans les atomes d'antihydrogène correspond parfaitement à celle des atomes d'hydrogène, soumettant le théorème CPT à des tests rigoureux.

### Mesure directe de la chute gravitationnelle de la Terre sur l'antimatière
Une autre grande question en physique est : "Comment l'antimatière se comporte-t-elle face à la gravité ?". Il y avait autrefois une hypothèse digne de la science-fiction selon laquelle l'antimatière pourrait subir une antigravité et tomber vers le haut. En 2023, le groupe expérimental ALPHA-g a piégé des atomes d'antihydrogène dans un piège vertical et a progressivement relâché le champ magnétique pour observer de quel côté ils tomberaient. Les résultats ont fourni la preuve directe que l'antimatière, tout comme la matière normale, est attirée vers le bas par la gravité terrestre. Cela a fortement suggéré que la relativité générale d'Einstein (le principe d'équivalence) s'applique également à l'antimatière.

### L'exploration spatiale de l'antimatière (AMS-02) et la future exploration spatiale
Dans l'espace extra-atmosphérique, le spectromètre magnétique alpha (AMS-02) à bord de la Station spatiale internationale (ISS) continue de rechercher des antiprotons, des positrons et même de l'antihélium dans les rayons cosmiques. Si la matière noire subit une annihilation de paires, un excès de positrons devrait être observé dans des régions d'énergie spécifiques, et de féroces débats sont toujours en cours sur l'interprétation de ces données.

En se tournant vers l'avenir, l'antimatière est anticipée comme la source d'énergie ultime pour l'expansion de l'humanité dans l'espace. Les fusées à propulsion à antimatière sont un concept qui utilise l'énergie générée par l'annihilation de paires de matière et d'antimatière comme poussée. Bénéficiant d'une efficacité de conversion masse-énergie (100 %) bien supérieure à celle de la fusion nucléaire, elle est considérée comme la seule source d'énergie qui rendrait possible le vol interstellaire au-delà de notre système solaire dans des délais réalistes. Bien que les obstacles techniques (production de masse et stockage stable de l'antimatière) soient incroyablement élevés, c'est théoriquement le meilleur moteur de fusée possible.

## Conclusion

L'histoire de l'antimatière, qui a commencé avec une seule équation dérivée par Dirac avec un stylo et du papier, est devenue aujourd'hui la clé pour percer les origines de l'univers, se situant au carrefour de la physique des particules et de la cosmologie. Le fait même que nous existions ici aujourd'hui est le cadeau d'une légère "asymétrie" de l'enfance de l'univers. La recherche sur l'antimatière est la quête de l'humanité pour les lois ultimes de la nature et continuera de nous fasciner comme un grand défi ouvrant les portes à la science et à la technologie de demain.
