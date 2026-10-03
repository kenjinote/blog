---
title: "Mécanique orbitale et méga-constellations de satellites"
description: "Une analyse mathématique détaillée de la mécanique orbitale, de la propagation des ondes, des systèmes de propulsion et des débris spatiaux derrière les méga-constellations comme Starlink."
slug: "satellite-mega-constellation-orbital-mechanics-starlink"
categories: ["Space", "Technology"]
tags: ["Starlink", "Orbital Mechanics", "Mega-Constellation"]
image: "eyecatch.jpg"
date: "2026-10-03T13:00:00+09:00"
---

# Introduction : L'aube des méga-constellations qui recouvrent le ciel de l'humanité
Au 21e siècle, le développement spatial connaît l'une de ses transformations les plus ambitieuses et dramatiques avec l'avènement des « méga-constellations de satellites artificiels ». Sous l'impulsion de SpaceX avec Starlink, mais aussi de OneWeb ou encore du Project Kuiper d'Amazon, des essaims de satellites d'une ampleur inédite, comptant de plusieurs milliers à des dizaines de milliers d'unités, sont en passe de recouvrir entièrement l'orbite terrestre basse. Il ne s'agit pas d'une simple évolution des technologies de communication, mais d'une entreprise grandiose visant à concevoir et à contrôler l'espace — une toile tridimensionnelle — avec une précision mathématique et physique extrême.
Cet article propose une analyse mathématique approfondie pour démystifier la théorie sous-jacente qui rend ces méga-constellations possibles : la « mécanique orbitale », les principes fondamentaux de la propagation des ondes électromagnétiques pour les communications spatiales, les systèmes de propulsion matériels, jusqu'au problème des débris spatiaux qui menace la durabilité de l'environnement spatial.

# Chapitre 1 : Les limites de l'orbite géostationnaire (GEO) et le changement de paradigme vers les méga-constellations en orbite basse (LEO)

## 1.1 Contraintes physiques des communications en orbite géostationnaire (GEO)
Historiquement, les systèmes de communication spatiale ont été dominés par l'orbite géostationnaire (GEO), située à environ 35 786 km au-dessus de l'équateur. Sur l'orbite GEO, la période de révolution du satellite correspond exactement à la période de rotation de la Terre (jour sidéral : environ 23 heures, 56 minutes et 4 secondes), ce qui donne l'impression, depuis le sol, que le satellite reste immobile dans la même direction. Cette caractéristique offre l'immense avantage de permettre à une antenne terrestre fixe de couvrir de vastes zones géographiques avec un seul satellite, sans nécessiter de mécanisme de poursuite.

Cependant, les lois de la physique imposent des limites strictes à l'orbite GEO. La plus importante d'entre elles est le **délai de propagation (latence)**. Même à la vitesse de la lumière $c \approx 3 \times 10^8$ m/s, en tenant compte d'un aller-retour entre le sol et un satellite GEO (liaison montante et liaison descendante) et de la réponse de l'autre partie (aller-retour complet), la distance parcourue par l'onde radio est d'environ $35 786 \times 4 \approx 143 144$ km.
En divisant cette distance par la vitesse de la lumière, on obtient le temps de latence théorique minimum suivant :
$$ t_{delay} = \frac{4 \times 35,786,000}{3 \times 10^8} \approx 0.477 \text{ s} = 477 \text{ ms} $$
Si l'on ajoute les délais de traitement des protocoles de communication, le temps de calcul de la correction d'erreur directe (FEC) et le délai de routage du réseau terrestre, le temps de latence aller-retour atteint facilement 600 ms à 800 ms. C'est une latence fatale pour les applications modernes exigeant du temps réel, telles que les jeux en ligne, le trading à haute fréquence (HFT), la télémédecine, ou même les visioconférences fluides. En raison de la contrainte de taille de fenêtre dans le protocole TCP/IP (BDP : Bandwidth-Delay Product), l'orbite GEO présentait également le problème d'une chute drastique du débit, même avec une large bande passante.

## 1.2 Le changement de paradigme vers l'orbite basse (LEO)
Pour résoudre ce problème de latence à la racine, l'idée de méga-constellations exploitant l'orbite terrestre basse (LEO), à une altitude de 500 km à 1 200 km, a émergé. Dans un réseau de communication LEO comme Starlink, si l'on suppose une altitude de 550 km, le délai aller-retour lié à la vitesse de la lumière est considérablement réduit.
$$ t_{LEO\_delay} = \frac{4 \times 550,000}{3 \times 10^8} \approx 0.0073 \text{ s} = 7.3 \text{ ms} $$
Même en incluant le délai de routage terrestre, on obtient un internet à très faible latence de 20 à 30 ms, comparable à celui des réseaux terrestres en fibre optique, voire supérieur pour les communications à longue distance. L'indice de réfraction de la lumière dans la fibre de verre est d'environ 1,5, ce qui réduit sa vitesse à environ 2/3 de la vitesse de la lumière dans le vide (environ $2 \times 10^8$ m/s). En revanche, la vitesse de la lumière est maintenue dans le vide spatial. Ainsi, pour des distances intercontinentales de plusieurs milliers de kilomètres, les données arrivent physiquement plus vite en passant par l'orbite LEO.

## 1.3 L'équation de transmission de Friis et l'analyse du bilan de liaison
L'avantage de l'orbite LEO ne se limite pas à la latence. Elle offre également une supériorité écrasante en matière de perte de propagation des ondes radio. Selon l'équation de transmission de Friis, fondement de la conception des bilans de liaison, la puissance reçue $P_r$ s'exprime comme suit :
$$ P_r = P_t G_t G_r \left( \frac{\lambda}{4 \pi d} \right)^2 \frac{1}{L_a L_s} $$
Où $L_a$ est l'atténuation atmosphérique et $L_s$ la perte du système.
L'affaiblissement de propagation en espace libre (Free Space Path Loss: FSPL) est défini par l'équation suivante :
$$ L_{FSPL} = \left( \frac{4 \pi d}{\lambda} \right)^2 $$
En décibels (dB), cela donne :
$$ L_{FSPL}(dB) = 20 \log_{10}(d) + 20 \log_{10}(f) + 20 \log_{10}\left(\frac{4 \pi}{c}\right) $$
Prenons pour exemple la fréquence de la liaison descendante en bande Ku, $f = 12$ GHz.
En calculant la différence de perte de propagation $\Delta L$ entre l'orbite GEO ($d \approx 36,000$ km) et l'orbite LEO ($d \approx 550$ km) :
$$ \Delta L = 20 \log_{10}\left(\frac{36000}{550}\right) \approx 20 \log_{10}(65.45) \approx 36.3 \text{ dB} $$
En d'autres termes, par rapport aux satellites GEO, les satellites LEO subissent environ 36,3 dB (soit environ 4 200 fois en termes de ratio de puissance) d'atténuation radio en moins pour la même bande de fréquences. Cela permet de réduire considérablement la puissance d'émission du satellite (EIRP) tout en miniaturisant la surface d'ouverture de l'antenne du terminal utilisateur. C'est ce puissant bilan de liaison qui a rendu possibles les communications à large bande avec des antennes domestiques de seulement 50 cm de diamètre.

# Chapitre 2 : Mathématiques de la mécanique orbitale et théorie des perturbations

Pour que des dizaines de milliers de satellites couvrent l'intégralité du globe terrestre en continu, sans jamais entrer en collision, des modèles mathématiques précis sont indispensables. Nous détaillerons ici du problème à deux corps jusqu'à la théorie des perturbations.

## 2.1 Les lois de Kepler et l'équation du problème à deux corps
La base de la mécanique orbitale repose sur la loi universelle de la gravitation de Newton et sur le problème à deux corps dérivé des équations du mouvement. En notant $M$ la masse de la Terre, $m$ la masse du satellite, et $\mathbf{r}$ le vecteur position allant du centre de la Terre au satellite, l'équation du mouvement s'écrit de la manière suivante :
$$ m \frac{d^2\mathbf{r}}{dt^2} = -G \frac{Mm}{r^3} \mathbf{r} $$
En utilisant le paramètre gravitationnel standard de la Terre $\mu = GM \approx 3.986004418 \times 10^5 \text{ km}^3/\text{s}^2$, l'équation se simplifie pour devenir indépendante de la masse $m$.
$$ \ddot{\mathbf{r}} + \frac{\mu}{r^3} \mathbf{r} = 0 $$
La trajectoire solution de cette équation différentielle non linéaire est une conique. La vitesse $v$ du satellite en n'importe quel point de son orbite est calculée grâce à l'« équation de la force vive (Vis-viva equation) » déduite du principe de conservation de l'énergie.
$$ v^2 = \mu \left( \frac{2}{r} - \frac{1}{a} \right) $$
Dans le cas d'une orbite circulaire à 550 km d'altitude ($a = 6371 + 550 = 6921$ km, $r=a$), la vitesse est $v = \sqrt{\mu/a} \approx 7.59 \text{ km/s}$ (soit environ 27 300 km/h). Cette vitesse vertigineuse est à l'origine du décalage Doppler et de la fréquence extrême des transferts (handovers), dont nous discuterons plus tard.

## 2.2 Les 6 paramètres orbitaux de Kepler (Keplerian Elements)
Afin de déterminer complètement l'orbite et la position d'un satellite dans un espace tridimensionnel, 6 paramètres indépendants sont nécessaires.
1. **Demi-grand axe (Semi-major axis, $a$)** : Détermine l'énergie et la période de l'orbite.
2. **Excentricité (Eccentricity, $e$)** : Forme de l'orbite ($e=0$ pour une orbite circulaire). Pour maintenir une qualité de communication constante, les constellations LEO adoptent des orbites extrêmement proches du cercle parfait avec $e \approx 0.0001$.
3. **Inclinaison orbitale (Inclination, $i$)** : Angle formé par le plan équatorial et le plan orbital. Pour Starlink, des inclinaisons de 53 degrés, 70 degrés, 97,6 degrés, etc., sont adoptées.
4. **Ascension droite du nœud ascendant (Right Ascension of the Ascending Node, $\Omega$)** : Angle sur le plan équatorial entre la direction du point vernal (équinoxe de printemps) et le nœud ascendant (le point où le satellite traverse l'équateur du sud vers le nord).
5. **Argument du périgée (Argument of Perigee, $\omega$)** : Angle dans le plan orbital mesuré depuis le nœud ascendant jusqu'au périgée.
6. **Anomalie vraie (True Anomaly, $\nu$)** : Angle représentant la position actuelle du satellite mesurée à partir du périgée.

## 2.3 Potentiel gravitationnel et perturbation $J_2$ due à l'aplatissement de la Terre
En réalité, la Terre n'est pas une sphère parfaite, mais un sphéroïde oblate (ellipsoïde de révolution) dont la région équatoriale est renflée d'environ 21 km en raison de la force centrifuge liée à sa rotation. Cette répartition inégale de la masse engendre un écart séculaire (perturbation) par rapport au problème idéal à deux corps. Le potentiel gravitationnel $U$ de la Terre s'exprime par le développement en harmoniques sphériques suivant :
$$ U = \frac{\mu}{r} \left[ 1 - \sum_{n=2}^{\infty} J_n \left(\frac{R_e}{r}\right)^n P_n(\sin \phi) \right] $$
Où $R_e$ est le rayon équatorial de la Terre (6 378,137 km), $P_n$ les polynômes de Legendre, et $\phi$ la latitude géocentrique. Le terme le plus influent est le coefficient harmonique zonal d'ordre 2, $J_2 \approx 1.08263 \times 10^{-3}$, qui représente le renflement équatorial.

La perturbation $J_2$ provoque une perturbation séculaire qui fait tourner progressivement l'ensemble du plan orbital. Le taux de variation dans le temps de l'ascension droite du nœud ascendant $\Omega$ et de l'argument du périgée $\omega$ est particulièrement important.
$$ \dot{\Omega} = -\frac{3}{2} J_2 \left(\frac{R_e}{p}\right)^2 n \cos i $$
$$ \dot{\omega} = \frac{3}{4} J_2 \left(\frac{R_e}{p}\right)^2 n (5 \cos^2 i - 1) $$
Où $p = a(1-e^2)$ est le demi-latus rectum, et $n = \sqrt{\mu/a^3}$ le moyen mouvement.

Lorsque l'inclinaison orbitale $i$ est inférieure à 90 degrés (orbite prograde), $\dot{\Omega}$ est négatif, et le plan orbital tourne vers l'ouest dans le sens inverse de la rotation terrestre (régression nodale : Nodal Regression). À une altitude de 550 km et une inclinaison de 53 degrés, $\dot{\Omega}$ est d'environ $-5.2^\circ / \text{jour}$. Dans une méga-constellation, tous les satellites sont contrôlés avec précision pour avoir la même altitude et la même inclinaison. Ainsi, le taux de variation $\dot{\Omega}$ dû à la perturbation $J_2$ est identique pour tous les plans, et la structure en filet de la constellation se maintient sur de longues périodes sans perdre sa forme relative.

## 2.4 Principe de conception de l'orbite héliosynchrone (SSO)
L'orbite héliosynchrone (Sun-Synchronous Orbit: SSO) tire parti de la perturbation $J_2$. La vitesse angulaire moyenne de déplacement du Soleil due à la révolution de la Terre autour de ce dernier est de 360 degrés par an, soit environ $0.9856^\circ/\text{jour}$.
En choisissant des paramètres orbitaux appropriés tels que $\dot{\Omega} = 0.9856^\circ/\text{jour}$, le plan orbital conserve toujours un angle constant par rapport au Soleil.
$$ 0.9856^\circ/\text{jour} = -\frac{3}{2} J_2 \left(\frac{R_e}{a}\right)^2 n \cos i $$
Pour satisfaire cette condition, il faut que $\cos i < 0$, c'est-à-dire une orbite rétrograde avec une inclinaison $i > 90^\circ$. À une altitude de 550 km, cela donne $i \approx 97.6^\circ$. Certaines couches (shells) de Starlink adoptent des orbites polaires proches de la SSO pour couvrir les régions polaires (autour du pôle Nord et du pôle Sud).

# Chapitre 3 : Géométrie des constellations de Walker

La "constellation de Walker" est la solution géométrique optimale pour couvrir toute la surface terrestre sans aucune lacune avec des milliers de satellites.

## 3.1 Définition mathématique de la configuration Walker-Delta $i: T/P/F$
Le modèle Walker-Delta, conçu par John G. Walker, est entièrement défini par la notation $i: T/P/F$.
- $i$ : Inclinaison orbitale (Inclination)
- $T$ : Nombre total de satellites composant la constellation
- $P$ : Nombre de plans orbitaux (Number of orbital Planes)
- $F$ : Paramètre de déphasage des satellites entre les plans orbitaux adjacents (entier compris entre $0 \le F \le P-1$)

Dans chaque plan orbital, $S = T/P$ satellites sont répartis uniformément. L'espacement entre les satellites dans le plan orbital est $\Delta \nu = 360^\circ / S$.
L'ascension droite du nœud ascendant $\Omega$ est divisée uniformément sur l'équateur, et l'espacement avec le plan orbital adjacent est $\Delta \Omega = 360^\circ / P$.
De plus, le décalage (déphasage) de l'anomalie vraie des satellites dans le plan orbital adjacent à l'est est donné par $\Delta \Phi = F \times (360^\circ / T)$.

Par exemple, la couche (Shell) 1 représentative de la première génération de Starlink, située à une altitude de 550 km et avec une inclinaison de 53 degrés, utilise une configuration géante de Walker où $T=1584, P=72$ (avec $S=22$ satellites par plan). En optimisant le déphasage $F$ entre les plans adjacents, il est possible de minimiser le risque de collision entre les satellites aux latitudes les plus élevées (autour de 53 degrés de latitude nord et sud) où les orbites sont les plus denses, tout en garantissant une couverture continue (Continuous Coverage) où au moins un satellite est toujours visible à un angle d'élévation supérieur à 25 degrés depuis le sol.

## 3.2 Réseau maillé spatial via des liaisons optiques inter-satellites (ISL)
La première génération de méga-constellations ne pouvait fournir Internet que dans la zone où un satellite pouvait communiquer simultanément avec un terminal utilisateur terrestre et une station passerelle (station terrienne) (connexion "bent-pipe"). Cela ne permettait pas d'offrir des services au milieu des océans ou dans les régions polaires.

Cette limite a été franchie par la liaison optique inter-satellites (Inter-Satellite Link: ISL) utilisant les communications laser. Dans le vide de l'espace, il n'y a pas d'atténuation de la lumière due à l'atmosphère ni de scintillation (turbulence atmosphérique). Cela permet des communications de haute capacité et à faible latence (de plusieurs Gbps à plusieurs dizaines de Gbps) avec des lasers dans la bande de longueur d'onde de 1,55 $\mu$m (bande C).
Chaque satellite est équipé de quatre terminaux de communication optique et établit des liaisons laser avec les deux satellites qui le précèdent et le suivent dans le même plan orbital (Intra-plane ISL) et avec les deux satellites à sa gauche et à sa droite dans les plans orbitaux adjacents (Inter-plane ISL).

## 3.3 L'algorithme du plus court chemin de Dijkstra et la mise à jour dynamique de la topologie
Dans le réseau formé par les ISL, la topologie du réseau évolue radicalement chaque seconde, car les nœuds (satellites) se déplacent à une vitesse d'environ 7,5 km/s. En particulier, à mesure que l'on se dirige vers les pôles, les plans orbitaux se croisent, et la liaison laser avec les satellites des plans adjacents (Inter-plane ISL) est régulièrement interrompue et rétablie (handover).

Le routage des paquets sur ce réseau graphique dynamique utilise un algorithme de Dijkstra étendu (Dijkstra's Algorithm) ou un routage par graphe de contacts (Contact Graph Routing: CGR). Le coût $C_{ij}$ de l'arête entre les nœuds $i$ et $j$ est évalué comme suit :
$$ C_{ij} = \alpha \cdot d_{ij} + \beta \cdot Q_{ij} + \gamma \cdot L_{ij} $$
Où $d_{ij}$ est la distance physique (latence), $Q_{ij}$ la longueur de la file d'attente (congestion), et $L_{ij}$ le temps restant pour maintenir la liaison.
Les paquets de données font des sauts en ligne droite à la vitesse de la lumière dans l'espace. Par rapport à un réseau terrestre en fibre optique posé le long de la courbure terrestre, la longueur du trajet est plus courte, et il n'y a pas de délai dû à l'indice de réfraction (qui est de $c/1.5$ dans la fibre). Pour les communications à très longue distance comme New York-Londres, le passage par les ISL est donc théoriquement plus rapide.

# Chapitre 4 : Matériel et système de propulsion des satellites Starlink

Les conditions de la réussite des méga-constellations résident dans la production de masse des satellites et dans la réduction drastique des coûts.

## 4.1 Impulsion spécifique des propulseurs à effet Hall au Krypton/Argon et calcul de la masse du propulseur
Après leur injection en orbite, les satellites doivent utiliser leur propre force pour s'élever jusqu'à leur orbite opérationnelle. Pendant leur fonctionnement, ils doivent compenser la traînée atmosphérique et, en fin de vie, ils doivent désorbiter (Deorbit). Pour atteindre l'incrément de vitesse $\Delta V$ nécessaire à ces manœuvres, on utilise un système de propulsion électrique appelé propulseur à effet Hall (Hall-effect Thruster).

D'après l'équation de la fusée de Tsiolkovski, la masse nécessaire de propergol $m_p$ est donnée par la formule suivante :
$$ m_p = m_0 \left( 1 - e^{-\frac{\Delta V}{I_{sp} g_0}} \right) $$
Où $I_{sp}$ est l'impulsion spécifique, $g_0$ l'accélération de la pesanteur standard, et $m_0$ la masse initiale.
Alors que la propulsion électrique traditionnelle utilisait du Xénon, un gaz très coûteux, SpaceX a opté pour le Krypton dans sa première génération et pour l'Argon dans sa deuxième génération (V2 Mini). L'Argon est abondant dans l'atmosphère et extrêmement bon marché, mais il a une énergie d'ionisation plus élevée, ce qui réduit son efficacité de poussée. Cependant, grâce à l'optimisation de la topologie du champ magnétique, le propulseur à effet Hall à l'Argon a atteint une impulsion spécifique de 2500 secondes ≒ 24,5 km/s de vitesse d'éjection, faisant baisser drastiquement le coût en propulseur lors des lancements de masse.

## 4.2 Mathématiques de la formation de faisceaux (Beamforming) des antennes à réseau phasé
Pour la communication avec les terminaux terrestres, on utilise une antenne à réseau phasé (Phased Array Antenna) qui permet de modifier instantanément la direction du faisceau radio sans nécessiter de pièces mécaniques mobiles.
En disposant les éléments de l'antenne sous forme de grille et en contrôlant la phase (Phase) des ondes radio émises par chaque élément, l'effet d'interférence permet de former un faisceau radio puissant dans une direction spécifique.

Dans un réseau plan bidimensionnel, la valeur du déphasage $\Delta \Phi_{mn}$ d'un élément situé aux coordonnées $(x_m, y_n)$ pour orienter le faisceau principal dans la direction souhaitée $(\theta, \phi)$ est calculée par la formule suivante :
$$ \Delta \Phi_{mn} = -\frac{2\pi}{\lambda} (x_m \sin\theta \cos\phi + y_n \sin\theta \sin\phi) $$
Les satellites Starlink et les terminaux utilisateurs sont équipés de circuits intégrés (IC) de formation de faisceau très avancés et recalculent la matrice de pondération de phase des milliers de fois par seconde. Cela permet de suivre électroniquement et en continu les satellites qui se déplacent à grande vitesse dans le ciel.

## 4.3 Algorithme d'évitement automatique des collisions
En LEO, où volent des milliers de satellites, le risque de collision avec des débris ou d'autres satellites est omniprésent. Les satellites Starlink intègrent un système d'évitement autonome des collisions qui utilise les données orbitales (TLE) fournies par le 18e Escadron de contrôle spatial (18 SDS).
La probabilité de collision $P_c$ au moment de l'approche maximale (TCA) s'obtient en projetant la matrice de covariance de l'erreur de position des deux objets sur un plan bidimensionnel, et en l'intégrant sur la section efficace de collision.
$$ P_c = \frac{1}{2\pi |C_p|^{1/2}} \iint_{A} \exp\left( -\frac{1}{2} \mathbf{r}^T C_p^{-1} \mathbf{r} \right) dx dy $$
Où $C_p$ est la matrice de covariance projetée, et $A$ la section efficace de collision. Si $P_c$ dépasse $10^{-5}$ (un pour cent mille), le satellite déclenche de manière autonome son propulseur à effet Hall pour effectuer une manœuvre d'évitement. La fusion de l'intelligence artificielle et du contrôle prédictif (MPC) permet d'assurer la sécurité sans intervention humaine.

# Chapitre 5 : Le problème des débris spatiaux et la crainte du syndrome de Kessler

## 5.1 Modèle de processus de Poisson pour la probabilité de collision
La collision d'objets en orbite peut être modélisée comme un processus de Poisson stochastique (Poisson Process). Si un satellite de section transversale $A$ traverse un espace avec une densité de débris spatiaux $\rho$ à une vitesse relative $v_{rel}$, la valeur attendue des collisions $d\lambda$ en un temps $dt$ est :
$$ d\lambda = \rho \cdot A \cdot v_{rel} \cdot dt $$
Sur une certaine période $T$, la probabilité $P_c$ d'avoir au moins une collision est :
$$ P_c = 1 - e^{-\int_0^T \rho A v_{rel} dt} $$
Dans le cas d'une collision frontale en orbite basse, la vitesse relative atteint environ $10 \sim 15 \text{ km/s}$. Même un fragment d'aluminium de seulement 1 cm possède une énergie cinétique comparable à celle d'une grenade à main, pouvant pulvériser complètement le satellite.

## 5.2 Le mécanisme de retombée naturelle par la traînée atmosphérique
Même en cas de panne du système de propulsion rendant le contrôle impossible, la traînée atmosphérique de la haute atmosphère joue un rôle naturel de nettoyeur. L'accélération de la perturbation causée par la traînée atmosphérique $\mathbf{a}_{drag}$ est exprimée par la formule suivante :
$$ \mathbf{a}_{drag} = -\frac{1}{2} \rho_{atm} \frac{C_D A}{m} v_{rel}^2 \frac{\mathbf{v}_{rel}}{v_{rel}} $$
La densité atmosphérique $\rho_{atm}$ augmente de façon exponentielle lorsque l'altitude diminue, et elle augmente encore plus avec la dilatation de la thermosphère induite par le rayonnement ultraviolet extrême (EUV) de l'activité solaire. C'est la raison principale pour laquelle Starlink a choisi une altitude de 550 km. En cas de perte de contrôle, il s'agit d'une "orbite d'auto-nettoyage" où l'altitude diminuera naturellement grâce à la traînée atmosphérique en quelques années (généralement 1 à 5 ans), avant que le satellite n'entre dans l'atmosphère et ne s'y consume. Au-delà de 1000 km d'altitude, les objets peuvent rester en orbite pendant plusieurs centaines d'années.

## 5.3 Destruction en chaîne par les collisions en orbite : Le syndrome de Kessler
Le "Syndrome de Kessler" (Kessler Syndrome), proposé par Donald Kessler de la NASA en 1978, constitue le scénario du pire.
Lorsqu'un objet massif entre en collision, cela génère un nuage composé de milliers de débris, ce qui augmente considérablement la probabilité que ces derniers percutent d'autres satellites. Des collisions s'ensuivent en chaîne, multipliant les fragments de façon exponentielle.
Une fois la densité critique dépassée, même sans nouveau lancement, l'auto-multiplication des débris devient incontrôlable, rendant des zones orbitales spécifiques (par exemple, à une altitude de 700 à 1 000 km) inutilisables pendant des centaines, voire des milliers d'années. C'est pour prévenir cette spirale désastreuse que la FCC a imposé "une désorbitation dans les 5 ans suivant la fin de l'opération".

# Chapitre 6 : Le problème de la pollution lumineuse en astronomie et la durabilité de l'espace

## 6.1 Réflectance lumineuse des satellites et impact sur les télescopes optiques
Les groupes de satellites juste après leur lancement (les "trains de Starlink") réfléchissent fortement la lumière du soleil, traversant le ciel nocturne.
La magnitude astronomique $m$ est définie par la formule suivante :
$$ m_1 - m_2 = -2.5 \log_{10} \left( \frac{F_1}{F_2} \right) $$
Les premiers satellites Starlink atteignaient une magnitude visuelle de $+3$ à $+5$, saturant les capteurs CCD des télescopes à champ large ultra-sensibles, comme ceux de l'Observatoire Vera C. Rubin, et provoquant une diaphonie (crosstalk) sévère. Cela a eu un impact désastreux sur la recherche des objets géocroiseurs (NEO) et les observations cosmologiques.

## 6.2 Mesures contre l'éblouissement : VisorSat et film miroir diélectrique
SpaceX et la communauté astronomique ont collaboré pour trouver des solutions.
1. **DarkSat** : La surface du satellite a été peinte en noir, mais elle absorbait la chaleur solaire, ruinant la conception thermique.
2. **VisorSat** : Des pare-soleil déployables ont été utilisés pour créer de l'ombre, mais ils interféraient avec l'équipement de communication laser et augmentaient la résistance atmosphérique.
3. **Film miroir diélectrique** : La deuxième génération (V2 Mini) a adopté un contrôle thermique et optique sophistiqué combinant une peinture noire et un film miroir diélectrique (Dielectric Mirror Film) spécial, reflétant la lumière de manière spéculaire vers l'espace plutôt que vers le sol. Cela permet d'assombrir les satellites jusqu'à une magnitude de $+7$ ou moins, les rendant invisibles à l'œil nu.

## 6.3 L'avenir de la gestion du trafic spatial (STM)
La méga-constellation en orbite basse, constituée de dizaines de milliers de satellites artificiels, est une révolution apportant le haut débit à toute l'humanité. Mais cest aussi un test moral pour l'humanité, face aux mathématiques implacables de la mécanique orbitale et aux limites de l'environnement spatial telles qu'illustrées par le syndrome de Kessler.
Actuellement, sous l'égide du COPUOS de l'ONU, la mise en place d'un cadre de Gestion du Trafic Spatial (Space Traffic Management: STM) — l'équivalent de la "liberté de navigation" ou du "COLREG" dans le domaine maritime — progresse à un rythme effréné. La réalisation d'un développement spatial durable (Space Sustainability) est notre plus grande responsabilité envers la prochaine génération.

# Annexe : Modélisation de la capacité de communication d'une méga-constellation

Afin d'évaluer mathématiquement la capacité globale du système (System Capacity) d'une méga-constellation, un modèle de multiplexage spatial prolongeant le théorème de Shannon-Hartley s'avère nécessaire.
La capacité de canal $C_{beam}$ pour un faisceau (beam) unique est donnée par l'équation :
$$ C_{beam} = B \log_2 \left( 1 + \text{SINR} \right) $$
Où $B$ est la bande passante (par exemple, une largeur de canal de 250 MHz en bande Ku) et SINR (Signal-to-Interference-plus-Noise Ratio) est le rapport signal sur interférence plus bruit.

Le SINR est développé de la manière suivante :
$$ \text{SINR} = \frac{P_r}{N_0 B + \sum I_{intra} + \sum I_{inter}} $$
- $P_r$ : Puissance de réception (calculée à partir de l'équation de Friis)
- $N_0$ : Densité spectrale de puissance de bruit ($N_0 = k T_{sys}$, où $k$ est la constante de Boltzmann, $T_{sys}$ la température de bruit du système)
- $\sum I_{intra}$ : Interférence interne (auto-interférence) provenant d'autres faisceaux ou d'autres satellites du même système (Intra-system interference)
- $\sum I_{inter}$ : Interférence provenant d'autres systèmes comme OneWeb, Kuiper ou des satellites GEO (Inter-system interference)

La caractéristique majeure des méga-constellations réside dans la réutilisation spatiale des fréquences (Spatial Frequency Reuse) avancée. La surface terrestre est divisée en cellules hexagonales (zones de couverture), et des canaux de fréquence ou des polarisations (polarisation circulaire droite RHCP et polarisation circulaire gauche LHCP) différents sont utilisés dans les cellules adjacentes. C'est ce qu'on appelle un modèle de réutilisation de fréquence avec une taille de grappe (cluster) $K$.
En notant $N_{beam}$ le nombre de faisceaux ponctuels (spot beams) qu'un satellite peut générer simultanément, le débit $C_{sat}$ par satellite s'établit à :
$$ C_{sat} = \sum_{i=1}^{N_{beam}} B_i \log_2 \left( 1 + \text{SINR}_i \right) $$

La capacité totale du système de la constellation, $C_{total}$, où $N_{active}$ est le nombre de satellites actifs, ne s'obtient pas par une simple multiplication $C_{total} = N_{active} \times C_{sat}$. En effet, environ 70 % des satellites survolent l'océan ou les régions polaires où la demande de communication est faible.
En supposant que le rapport des terres émergées à la surface totale de la Terre est $\eta_{land} \approx 0.29$ et que le facteur de pondération de la couverture démographique est $\eta_{pop}$, la capacité effective du système $C_{eff}$ peut être estimée comme suit :
$$ C_{eff} = C_{total} \times \eta_{land} \times \eta_{pop} \times \eta_{utilization} $$
Où $\eta_{utilization}$ est le taux de disponibilité du réseau et l'efficacité du routage.
Comme le montre clairement cette formule, pour accroître l'autonomie économique d'une méga-constellation, il est essentiel de trouver comment monétiser la « capacité des satellites au-dessus de l'océan » qui, autrement, serait gaspillée. Cela peut passer par la fourniture de services aux avions et aux navires en mer, ou par l'utilisation de l'ISL pour les communications longue distance (backhaul), ce qui constitue un défi crucial pour le modèle économique.
