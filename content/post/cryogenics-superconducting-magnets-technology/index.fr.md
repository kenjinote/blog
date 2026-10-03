---
title: "Ingénierie cryogénique et technologie des électroaimants supraconducteurs : Le monde du cycle de réfrigération et des champs magnétiques intenses à l'approche du zéro absolu"
description: "Liquéfaction de l'hélium, réfrigération à dilution et circuits de protection contre les transitions résistives (quench). L'ingénierie extrême des aimants supraconducteurs qui soutient le Maglev, l'IRM et les accélérateurs géants."
slug: "cryogenics-superconducting-magnets-technology"
date: "2026-10-03T05:00:00+09:00"
categories: ["engineering", "physics"]
tags: ["cryogenics", "superconductivity", "magnets", "materials-science"]
image: "eyecatch.jpg"
---

# Ingénierie cryogénique et technologie des électroaimants supraconducteurs : Le monde du cycle de réfrigération et des champs magnétiques intenses à l'approche du zéro absolu

Dans les sciences de pointe et les infrastructures modernes, la « cryogénie » (Cryogenics) et la « supraconductivité » (Superconductivity) sont devenues des technologies fondamentales indissociables. L'IRM en médecine, les accélérateurs de particules géants qui font avancer la physique des hautes énergies, ainsi que le train à lévitation magnétique supraconducteur (Maglev), moyen de transport à grande vitesse de nouvelle génération. Tous ces éléments sont le fruit de l'« ingénierie cryogénique » pour maintenir l'état supraconducteur à résistance électrique nulle, et de l'« ingénierie des électroaimants supraconducteurs » pour générer et maintenir de manière stable des champs magnétiques puissants.

Dans cet article, nous explorerons en profondeur l'ingénierie cryogénique et la technologie des aimants supraconducteurs : depuis la thermodynamique des cycles de réfrigération qui s'approchent à l'extrême du zéro absolu (0 K = -273,15 °C), en passant par les propriétés physiques microscopiques des matériaux supraconducteurs pratiques, la conception de bobines capables de résister à d'immenses forces électromagnétiques, jusqu'aux mécanismes physiques des systèmes de protection qui préviennent le « quench », une rupture destructrice de l'état supraconducteur.

## Chapitre 1 : Thermodynamique de la cryogénie (Cryogenics)

La porte d'entrée vers le monde des températures cryogéniques s'ouvre par le cycle thermodynamique qui liquéfie les gaz. À pression atmosphérique, le point d'ébullition de l'azote est de 77,3 K, celui de l'hydrogène de 20,3 K, et celui de l'hélium (He-4) de 4,2 K. Pour produire ces réfrigérants cryogéniques, ou pour refroidir des systèmes sans réfrigérant, l'humanité a mis au point de nombreux cycles de réfrigération sophistiqués.

### Effet Joule-Thomson et liquéfaction de l'hélium
Le phénomène par lequel la température d'un gaz change lors de son expansion adiabatique s'appelle l'effet Joule-Thomson (Joule-Thomson effect). Dans un processus isenthalpique où l'enthalpie $h$ est constante, le coefficient de Joule-Thomson $\mu_{JT}$, qui indique le taux de changement de la température $T$ par rapport à la pression $P$, est défini comme suit :

$$ \mu_{JT} = \left( \frac{\partial T}{\partial P} \right)_h = \frac{1}{C_p} \left[ T \left( \frac{\partial v}{\partial T} \right)_P - v \right] $$

Où $C_p$ est la chaleur massique à pression constante, et $v$ est le volume massique. Ce n'est que dans la région où $\mu_{JT} > 0$ (en dessous de la température d'inversion) qu'une baisse de pression ($\Delta P < 0$) s'accompagne d'une baisse de température ($\Delta T < 0$). La température d'inversion de l'hélium étant très basse (environ 40 K), une simple expansion à partir de la température ambiante ferait monter sa température. Par conséquent, pour liquéfier l'hélium, on utilise le cycle de Claude (Claude cycle) : on commence par un prérefroidissement avec de l'azote liquide, ou une expansion isentropique (expansion adiabatique qui extrait un travail vers l'extérieur) à l'aide d'un turbo-détendeur (turbine d'expansion) pour refroidir en dessous de la température d'inversion, puis dans l'étape finale de liquéfaction, on effectue une expansion isenthalpique à travers une vanne J-T. Sur un diagramme T-s (température-entropie), ce processus illustre le passage de la ligne à haute pression avec une chute verticale isentropique dans la turbine, combinée à une chute suivant une courbe isenthalpique dans la vanne J-T, pour pénétrer dans la région de coexistence liquide-vapeur.

### Réfrigérateurs Gifford-McMahon (GM) et réfrigérateurs à tube à gaz pulsé
Pour les IRM et les cryostats de recherche, le réfrigérateur GM (Gifford-McMahon) à cycle fermé est largement utilisé. Le réfrigérateur GM réalise l'expansion de Simon (un cycle de compression isotherme et d'expansion adiabatique) en commutant l'alimentation et l'échappement de gaz hélium à haute pression provenant d'un compresseur à l'aide d'une vanne rotative, ce qui fait osciller un déplaceur (un piston contenant un matériau régénérateur) dans un cylindre. Bien qu'il soit similaire à un cycle de Stirling inversé, en contrôlant le déphasage entre la vanne et le piston, il offre une plus grande capacité de réfrigération à plus basse fréquence.

Pour le matériau régénérateur (Regenerator), la dépendance en température de la capacité thermique joue un rôle décisif. Aux températures cryogéniques (en dessous de 10 K), la chaleur massique du réseau cristallin des solides chute fortement en suivant la loi en $T^3$ de Debye, et les métaux ordinaires (cuivre ou plomb) ne peuvent plus emmagasiner de chaleur. Ainsi, pour le matériau régénérateur du deuxième étage des réfrigérateurs GM de classe 4 K, on adopte des matériaux régénérateurs magnétiques (comme $Er_3Ni$ ou $HoCu_2$) qui exploitent la chaleur massique magnétique géante associée à une transition de phase magnétique, ce qui a permis la production directe de 4,2 K (sans ajout de fluide frigorigène).

De plus, le réfrigérateur à tube à gaz pulsé (Pulse Tube Cryocooler) a considérablement augmenté la fiabilité en éliminant les pièces mobiles. En remplaçant le déplaceur par un déphaseur (orifice et réservoir tampon) et en optimisant acoustiquement la différence de phase entre l'onde acoustique (onde de pression) et le déplacement du gaz, il permet de pomper la chaleur vers l'extrémité chaude sans aucune pièce mobile.

### Vers la région du millikelvin : Réfrigération à dilution et désaimantation adiabatique
Si l'on fait bouillir de l'hélium liquide à 4,2 K sous pression réduite, on descend le long de la courbe de pression de vapeur et on peut atteindre environ 1 K. Cependant, pour s'approcher encore du zéro absolu dans la région du millikelvin (mK), il faut utiliser un « réfrigérateur à dilution (Dilution Refrigerator) » qui exploite le phénomène de séparation de phase d'un mélange isotopique d'hélium-3 (He-3) et d'hélium-4 (He-4).
En dessous de 0,87 K, le mélange $He^3-He^4$ se sépare en deux phases : une phase riche en $He^3$ (proche de l'$He^3$ pur) et une phase diluée en $He^3$ (où environ 6,6 % de $He^3$ est dissous dans l'$He^4$ superfluide). Lorsque les atomes de $He^3$ « s'évaporent (se dissolvent) » de la phase riche vers la phase diluée, un phénomène d'absorption de chaleur dû à la différence d'enthalpie se produit. En faisant circuler cela continuellement, on maintient de manière stable des températures extrêmement basses, de quelques dizaines de mK à moins de 10 mK.

En outre, en utilisant la technologie de désaimantation adiabatique (Adiabatic Demagnetization), qui exploite l'entropie des dipôles magnétiques, il est possible d'atteindre le domaine du microkelvin ($\mu K$).

## Chapitre 2 : Propriétés physiques des matériaux supraconducteurs pratiques et techniques de fabrication

Pour générer des champs magnétiques intenses, le conducteur utilisé pour l'enroulement doit maintenir son état supraconducteur sous des champs magnétiques élevés et pouvoir transporter un courant énorme (courant critique). L'état supraconducteur n'est maintenu qu'à l'intérieur d'une surface critique tridimensionnelle délimitée par trois valeurs critiques : la température $T$, le champ magnétique $H$ et la densité de courant $J$ ($T_c, H_c, J_c$).

### Supraconducteurs de type II et effet d'ancrage (Pinning)
Les matériaux utilisés pour les aimants à champ intense sont tous des supraconducteurs de type II (Type-II Superconductors). Au-delà du champ magnétique critique inférieur $H_{c1}$, le flux magnétique pénètre à l'intérieur du supraconducteur sous la forme de « quantons de flux (Flux quantum, $\Phi_0 = h/2e \approx 2,07 \times 10^{-15} \text{ Wb}$) » (état mixte). L'état supraconducteur est macroscopiquement maintenu jusqu'à ce que le champ magnétique externe atteigne le champ magnétique critique supérieur $H_{c2}$.
Cependant, si un flux magnétique $\vec{B}$ est présent alors qu'un courant $\vec{J}$ circule, une force de Lorentz ($\vec{F}_L = \vec{J} \times \vec{B}$) agit sur le quantum de flux. Si le flux magnétique se déplace (fluage), une tension est générée par induction électromagnétique, ce qui produit une chaleur de Joule et détruit la supraconductivité. Pour éviter cela, il est indispensable d'introduire des défauts artificiels (précipités normaux, joints de grains, dislocations, etc.) à l'intérieur du matériau pour y piéger le flux magnétique, ce que l'on appelle l'« ancrage (Flux Pinning) ». La condition pour que la force d'ancrage $\vec{F}_p$ surmonte la force de Lorentz ($\vec{F}_L \le \vec{F}_p$) détermine la densité de courant critique macroscopique $J_c$ de ce matériau.

### Fils multifilamentaires en NbTi (Niobium-Titane) et matrice de cuivre
L'alliage le plus largement utilisé dans les IRM et les accélérateurs est le NbTi ($T_c \approx 9,2 \text{ K}, H_{c2} \approx 11 \text{ T}$ (à 4,2 K)). Le NbTi est très ductile et facile à travailler par déformation plastique.
Le fil pratique n'est pas un fil monobloc, mais possède une « structure multifilamentaire ultrafine » dans laquelle des dizaines de milliers de filaments de NbTi de l'ordre du micron sont noyés dans une matrice en cuivre pur exempt d'oxygène (OFC). Ceci est fait pour éviter l'« instabilité magnétique (saut de flux) ». Si le flux magnétique pénètre soudainement dans le supraconducteur, cela génère de la chaleur, l'élévation de température abaisse le courant critique, ce qui entraîne une pénétration supplémentaire du flux magnétique, conduisant à un emballement thermique (quench). Pour satisfaire aux critères de stabilisation (critère de stabilité adiabatique et critère de stabilité dynamique) visant à prévenir cela, il est essentiel d'amincir les filaments supraconducteurs à quelques dizaines de $\mu m$ ou moins, et de les envelopper de cuivre, qui présente une excellente conductivité thermique et électrique.

### Nb3Sn (Niobium-Étain) et technologie de traitement thermique des composés fragiles
Pour les champs magnétiques intenses dépassant 10 T (RMN, ITER, recherche sur les champs intenses), on utilise le Nb3Sn, un composé intermétallique de type A15 ($T_c \approx 18,3 \text{ K}, H_{c2} \approx 23 \text{ T}$ (à 4,2 K)). Cependant, le Nb3Sn est extrêmement fragile et ne peut pas être plié tel quel (la contrainte dégrade considérablement ses propriétés critiques).
C'est pourquoi des techniques de fabrication ingénieuses telles que le « procédé bronze » (Bronze Method) et le « procédé à l'étain interne » (Internal Tin Process) ont été développées. Au moment de l'enroulement de la bobine, on usine et on enroule le matériau à l'état de filaments de Nb (niobium) n'ayant pas encore réagi et d'une matrice contenant du Sn (étain) (bronze, etc.) (méthode Wind & React). Après lui avoir donné la forme d'une bobine, on applique un traitement thermique à 600-700 °C pendant des dizaines d'heures. Par une réaction de diffusion à l'état solide, le Nb et le Sn se combinent, formant une couche de Nb3Sn dans la partie des filaments.

### L'essor des fils supraconducteurs à haute température (REBCO / BSCCO)
Les supraconducteurs à haute température (HTS) à base d'oxydes de cuivre, qui présentent une supraconductivité au-dessus de la température de l'azote liquide (77 K), affichent une résistance remarquable aux champs magnétiques avec un $H_{c2}$ dépassant 100 T lorsqu'ils sont utilisés à des températures cryogéniques comme $20 \text{ K}$ ou $4,2 \text{ K}$.
Une attention particulière est portée sur les fils minces en bande de REBCO (Terre Rare-Baryum-Oxyde de Cuivre, $RE Ba_2 Cu_3 O_{7-\delta}$). Sur un substrat métallique à haute résistance tel que l'Hastelloy, on dépose une couche tampon orientée par la méthode IBAD (Ion Beam Assisted Deposition), sur laquelle la couche de REBCO fait l'objet d'une croissance épitaxiale. Une couche de REBCO d'à peine 1 à 2 $\mu m$ d'épaisseur permet le passage de plusieurs centaines d'ampères. Avec l'apparition des HTS, la faisabilité des RMN à ultra-haut champ magnétique dépassant les 25 T, et des réacteurs à fusion compacts (comme le SPARC) a soudainement émergé.

## Chapitre 3 : Conception d'électroaimants supraconducteurs et ingénierie des champs intenses

La conception d'un aimant supraconducteur est une trinité d'ingénierie impliquant l'électromagnétisme, la thermodynamique cryogénique et la mécanique des structures solides de l'extrême.

### Forme de la bobine et force électromagnétique géante (Force de Lorentz)
La bobine solénoïdale la plus fondamentale génère un champ magnétique puissant le long de son axe central. En revanche, dans les aimants dipolaires qui courbent les faisceaux dans les accélérateurs de particules, on combine des bobines spéciales en forme de piste de course appelées en forme de selle, en cosinus thêta ($\cos \theta$), ou bobines en blocs pour former un champ magnétique dipolaire uniforme.
Le plus grand obstacle dans la conception des aimants est l'immense force électromagnétique (Force de Lorentz $\vec{f} = \vec{J} \times \vec{B}$) agissant sur le fil supraconducteur lui-même. Par exemple, dans un grand aimant dont le champ magnétique central dépasse 10 T, la contrainte circonférentielle (Hoop stress) qui tend à élargir la bobine vers l'extérieur atteint des centaines de MPa (des centaines d'atmosphères).
Pour y résister, la circonférence de la bobine est pourvue d'anneaux de frettage (Shrink rings) en acier inoxydable non magnétique ou en alliage d'aluminium très résistants, ou bien de solides structures de renforcement mécanique composées de plastique renforcé de fibres de carbone (CFRP) ou de résine époxy renforcée de fibres de verre (GFRP). L'enroulement est imprégné sous vide (VPI) de résine époxy, l'intégrant dans un corps rigide qui ne permet même pas le moindre échauffement par friction (déplacement dynamique du fil).

### Mode de courant persistant (Persistent Current Mode)
Une technologie extrêmement importante pour l'IRM et la RMN est le mode de courant persistant. Si le circuit de l'aimant supraconducteur peut être fermé en boucle entièrement avec des matériaux supraconducteurs, même si l'alimentation externe est déconnectée, comme la résistance $R = 0$, le courant $I$ ne s'atténue théoriquement jamais de façon semi-permanente (constante de temps $\tau = L/R \to \infty$).
Cela est rendu possible par le « commutateur à courant persistant (PCS: Persistent Current Switch) ». Le PCS est un circuit de dérivation en fil supraconducteur connecté en parallèle avec l'aimant. Un élément chauffant est enroulé autour du PCS. En le chauffant pour amener la partie du PCS à un état normal (avec résistance) au-dessus de la température $T_c$, le commutateur est « désactivé (ouvert) », et un courant est excité depuis l'alimentation externe vers le corps de l'aimant (inductance $L$). Une fois la valeur de courant souhaitée atteinte, le chauffage est coupé et le PCS revient à l'état supraconducteur (commutateur activé, résistance nulle). Ensuite, lorsque le courant de l'alimentation externe est progressivement réduit, le courant commence à circuler dans la boucle fermée entre le PCS (résistance nulle) et l'aimant, plutôt que dans le circuit externe. C'est l'accomplissement du mode de courant persistant. Grâce à cette technologie, le champ magnétique est maintenu pendant des années avec une stabilité extrêmement élevée, inférieure à 0,01 ppm/h.

## Chapitre 4 : La physique du phénomène de « Quench » et le système de protection

Le phénomène le plus redoutable dans un aimant supraconducteur est le « quench » (transition résistive). Le quench est un phénomène où une partie de la bobine subit une augmentation de température due à une perturbation thermique quelconque (chaleur de friction due au mouvement microscopique d'un fil, fissure dans la résine, irradiation, etc.) et transite vers un état normal (état avec résistance) en dépassant $T_c$.

### Mécanisme physique du quench et propagation rapide
Lorsqu'une zone normale (non supraconductrice) apparaît, un fort courant la traverse, générant de la chaleur de Joule ($I^2 R$). Cette chaleur est transmise à la partie supraconductrice environnante par conduction thermique, et la zone normale s'étend en trois dimensions à une vitesse explosive. C'est ce qu'on appelle la « propagation de la zone normale (Normal Zone Propagation) ».
Lorsqu'un quench se produit, l'énorme énergie magnétique ($E = \frac{1}{2} L I^2$) accumulée à l'intérieur de l'aimant tente d'être entièrement dissipée sous forme de chaleur de Joule dans la bobine elle-même. Par exemple, un seul aimant dipolaire du LHC stocke une énergie de 7 MJ, ce qui équivaut à plusieurs kilogrammes d'explosif TNT. Sans mesure de protection, la température du « point chaud » local devenu normal dépassera la température de fusion (1085 °C pour le cuivre), et la bobine fondra littéralement et sera détruite.
De plus, si la bobine est immergée dans un bain d'hélium liquide, le dégagement rapide de chaleur provoque une vaporisation explosive de l'hélium liquide (dont le volume se dilate d'environ 700 fois), entraînant une augmentation soudaine de la pression à l'intérieur du cryostat.

### Équation de la chaleur adiabatique et calcul du circuit de décharge
Le modèle thermodynamique fondamental pour protéger la bobine d'un quench est basé sur le calcul de l'élévation de température par une approximation adiabatique. La température du point chaud $T_m$ à un instant $t$ après le début du quench est décrite par l'équation de chaleur adiabatique suivante :

$$ \int_{0}^{\infty} I(t)^2 \, dt = S^2 \int_{T_{op}}^{T_{m}} \frac{\gamma C_p(T)}{\rho(T)} \, dT $$

Le côté gauche est l'intégrale temporelle du carré du courant, un indicateur de la gravité du quench appelé « MIITs (Mega Amps Squared Seconds) ». Le côté droit est l'intégrale en température des propriétés intrinsèques du matériau (section transversale $S$, densité $\gamma$, chaleur massique $C_p$, résistivité électrique $\rho$). Pour limiter la température du point chaud $T_m$ à une plage sûre (par exemple, en dessous de 150 K, température où la déformation thermique ne coupe pas le fil), il faut minimiser l'intégrale $\int I^2 dt$ du côté gauche.

### Système de protection : Décharge d'énergie et déclenchement de chauffage
Un système de protection contre le quench (Quench Protection System, QPS) est indispensable pour prévenir les dommages liés au quench.
1. **Détecteur de quench (Quench Detector)** : Il utilise un circuit en pont pour surveiller la différence entre la tension aux bornes de la bobine et la tension depuis une prise centrale, annulant la tension induite $L(di/dt)$ pour détecter rapidement la minuscule tension (quelques dizaines de mV) due à l'apparition d'une résistance.
2. **Résistance de décharge d'énergie (Energy Dump Resistor)** : Au moment où le quench est détecté, un disjoncteur externe s'ouvre, insérant dans le circuit une énorme « résistance de décharge (Dump Resistor, $R_d$) » normale en série avec la bobine. Cela permet de dissiper sous forme de chaleur la majeure partie de l'énergie magnétique dans la résistance de décharge à l'extérieur du cryostat. La constante de temps de décroissance du courant devient $\tau = L / (R_{coil} + R_d)$, ce qui permet de faire chuter le courant rapidement.
3. **Dispositifs de chauffage de protection (Quench Heaters)** : Si la bobine est extrêmement grande, l'utilisation de la seule résistance de décharge entraînerait une tension trop élevée ($V = I \times R_d$), avec un risque de claquage diélectrique (décharge en arc). Par conséquent, dès la détection du quench, une méthode consistant à faire passer un courant pulsé dans des éléments chauffants collés à la surface de la bobine est employée pour chauffer de force l'ensemble de la bobine et « provoquer intentionnellement un quench sur toute sa surface ». Ainsi, le dégagement de chaleur de Joule est réparti sur toute la bobine, évitant l'élévation de température d'un point chaud localisé.

## Chapitre 5 : Des systèmes géants soutenant les infrastructures de pointe

Les électroaimants supraconducteurs ont franchi les limites du laboratoire pour fonctionner comme des infrastructures massives qui soutiennent la société moderne.

### Le Maglev Chuo Shinkansen de JR Tokai (Aimants supraconducteurs de la série L0)
Le SC MAGLEV, projet de fierté du Japon, est équipé d'aimants supraconducteurs en NbTi à bord des véhicules, générant une puissante force de répulsion et d'attraction avec les bobines de propulsion et de lévitation au sol, réalisant ainsi une circulation en lévitation à une vitesse de 500 km/h.
Étant donné que les aimants à bord du véhicule sont soumis à un environnement vibratoire sévère, une structure de support de charge est adoptée pour offrir une grande rigidité mécanique tout en minimisant la pénétration de chaleur. Alors que les premiers véhicules expérimentaux utilisaient un système de refroidissement à base d'hélium liquide et d'azote liquide, la dernière série L0 est équipée de réfrigérateurs GM-JT à cycle fermé embarqués haute performance, rendant l'apport extérieur d'hélium inutile sur de longues périodes.

### Vulgarisation des IRM médicales (3T à 7T)
Le système supraconducteur le plus largement opérationnel au monde est l'IRM (Imagerie par Résonance Magnétique). Pour aligner les spins des noyaux d'hydrogène du corps humain, elle nécessite un espace à champ magnétique puissant et uniforme (l'alésage) allant de 1,5 T à 3,0 T, et jusqu'à 7,0 T pour les derniers modèles de recherche et d'usage clinique.
L'aimant de l'IRM est constitué d'une bobine solénoïdale faite de fils en NbTi et est piloté de manière stable en mode de courant persistant. Grâce aux progrès de la technologie « Zero-Boil-Off » (zéro évaporation de l'hélium), les systèmes qui ne nécessitent pas de réapprovisionnement régulier en réfrigérant sont devenus la norme.

### Grand collisionneur de hadrons (LHC) du CERN et réacteur expérimental de fusion ITER
Au sommet de la physique des hautes énergies, le LHC de Genève abrite 1 232 aimants dipolaires supraconducteurs alignés dans un tunnel circulaire de 27 km. Pour générer le champ magnétique de 8,3 T nécessaire pour courber les faisceaux de protons, les bobines en NbTi sont refroidies par de l'hélium superfluide (Superfluid Helium, He-II) à 1,9 K. L'hélium à l'état superfluide, de viscosité nulle et d'une conductivité thermique des milliers de fois supérieure à celle du cuivre pur, s'infiltre dans les moindres interstices à l'intérieur de la bobine pour évacuer la chaleur de manière extrêmement efficace, agissant comme le « réfrigérant ultime ».
D'autre part, dans le réacteur thermonucléaire expérimental international ITER en construction dans le sud de la France, de gigantesques bobines de champ toroïdal et une bobine solénoïdale centrale sont en cours de fabrication pour confiner le plasma. Le solénoïde central, haut de 13 m et pesant 1 000 tonnes, génère un champ magnétique variable de 13 T, ce qui a nécessité l'utilisation d'un conducteur en Nb3Sn à structure spéciale appelé CICC (Cable-in-Conduit Conductor). C'est le conducteur ultime qui combine la résistance à une force électromagnétique colossale et de hautes performances de refroidissement, en forçant la circulation d'hélium supercritique (Supercritical Helium) dans les interstices de centaines de brins supraconducteurs torsadés à l'intérieur d'un tuyau en acier inoxydable.

## Chapitre 6 : Les frontières de l'ingénierie cryogénique

Les innovations technologiques en matière de cryogénie et de supraconductivité continuent de s'accélérer aujourd'hui.

### Réfrigérateurs à dilution pour ordinateurs quantiques
Le développement des ordinateurs quantiques utilisant des qubits supraconducteurs (tels que les Transmons) fait actuellement l'objet d'une compétition mondiale. Pour protéger la cohérence des états quantiques (superposition) contre le bruit thermique, il est nécessaire de placer la puce dans un environnement aux températures de l'extrême limite du zéro absolu, soit de 10 à 15 mK. Pour ce faire, de grands réfrigérateurs à dilution sans liquide réfrigérant sont utilisés. Ils refroidissent depuis la température ambiante jusqu'à 4 K avec un réfrigérateur à tube à gaz pulsé, puis utilisent un cycle de circulation He-3/He-4 pour descendre dans la région du millikelvin. Le secret de la conception matérielle réside dans la conception de boucliers thermiques multi-étagés qui bloquent l'afflux de chaleur tout en tirant un grand nombre de câbles coaxiaux vers la région cryogénique.

### Aimants supraconducteurs sans fluide frigorigène (Cryogen-Free Magnets) et technologie de refroidissement par conduction
Pendant de nombreuses années, le fonctionnement des aimants supraconducteurs nécessitait de l'hélium liquide, un produit coûteux et difficile à manipuler. Cependant, avec l'amélioration des performances des fils supraconducteurs à haute température et la puissance accrue des petits réfrigérateurs tels que les réfrigérateurs GM, les aimants à refroidissement par conduction (Conduction Cooled) se sont rapidement répandus. Ces aimants n'utilisent aucun réfrigérant liquide et refroidissent la bobine en la connectant directement à l'étage de refroidissement du réfrigérateur par une liaison thermique en cuivre. Cela a rendu possible la génération de champs magnétiques intenses d'une simple pression sur un bouton, ce qui a élargi de façon explosive le champ de leurs applications à la science des matériaux, à la physique de la matière condensée et au domaine médical.

### Fusion avec la société de l'hydrogène : Infrastructures d'hydrogène liquide et MgB2
L'hydrogène liquide (point d'ébullition 20,3 K) suscite l'intérêt en tant que vecteur énergétique vers une future société neutre en carbone. Cette plage de températures de 20 K est suffisamment basse pour faire fonctionner le diborure de magnésium ($MgB_2$, $T_c \approx 39 \text{ K}$), un composé supraconducteur intermétallique découvert au Japon en 2001, ainsi que les supraconducteurs à haute température susmentionnés (REBCO / BSCCO).
Un changement de paradigme pour les infrastructures énergétiques cryogéniques a été proposé, et des expériences de démonstration ont déjà commencé : « utiliser l'hydrogène liquide comme liquide de refroidissement pour refroidir les câbles de transmission supraconducteurs et les systèmes de stockage d'énergie supraconductrice (SMES), tout en transportant et en utilisant l'hydrogène lui-même comme carburant ».



## Annexe A : Thermodynamique du cycle de réfrigération et analyse détaillée sur le diagramme T-s

Pour mieux comprendre l'essence du cycle de réfrigération cryogénique, nous allons suivre rigoureusement le comportement du cycle de Claude (Claude cycle) lors de la liquéfaction de l'hélium sur le diagramme T-s (température-entropie).
Le gaz hélium, à l'état de 1 atm (environ 0,1 MPa) à température ambiante (300 K), est comprimé de manière isotherme à environ 2 MPa (20 atm) par un compresseur. La chaleur de compression générée au cours de ce processus est rejetée vers l'extérieur par un échangeur de chaleur refroidi à l'eau (processus de diminution de l'entropie le long d'une courbe isotherme sur le diagramme T-s).
Ensuite, le gaz à haute pression est envoyé à un échangeur de chaleur à contre-courant multi-étagé (Counter-flow heat exchangers). Ici, il échange de la chaleur avec le gaz froid à basse pression qui revient sans être liquéfié, et subit un refroidissement isobare (un processus où la température et l'entropie baissent le long d'une courbe isobare sur le diagramme T-s).
Toutefois, l'effet Joule-Thomson seul ne pouvant liquéfier l'hélium, la majorité du gaz (environ 60 à 80 %) est déviée à mi-chemin vers un turbo-détendeur (turbine d'expansion). Dans la turbine, le gaz subit une expansion adiabatique tout en faisant tourner une roue pour produire un travail externe. Idéalement, ce processus est une expansion isentropique (chute verticale le long d'une ligne d'isentropie), entraînant une baisse brutale de la température (par exemple jusqu'à environ 15 K).
Le gaz à basse pression refroidi par cette turbine retourne à l'échangeur de chaleur et sert à pré-refroidir le reste du gaz à haute pression qui a continué sans être dévié. Grâce à ce pré-refroidissement, le gaz à haute pression est refroidi à environ 6 K, bien en dessous de la température d'inversion de l'hélium (environ 40 K).
Enfin, ce gaz à haute pression à 6 K traverse la vanne Joule-Thomson (vanne J-T). L'expansion à travers la vanne J-T n'impliquant pas de travail externe, elle devient une expansion isenthalpique (Isenthalpic expansion) où l'enthalpie est conservée. Sur le diagramme T-s, l'état change le long d'une courbe isenthalpique (une courbe descendante vers la droite) pour pénétrer dans la région de coexistence liquide-gaz (dôme de saturation). Par conséquent, une partie du gaz se liquéfie (température de 4,2 K, pression de 1 atm) et est récupérée sous forme d'hélium liquide. Le gaz non liquéfié retourne dans l'échangeur de chaleur pour refroidir le système.

## Annexe B : Structure transversale des fils multifilamentaires supraconducteurs en NbTi et critère de stabilité dynamique

Comme mentionné précédemment, les fils supraconducteurs pratiques adoptent une structure multifilamentaire (Multifilamentary structure) dans laquelle de nombreux filaments supraconducteurs sont disposés au sein d'une matrice de cuivre. Nous allons expliquer quantitativement la nécessité de cette structure du point de vue de l'instabilité magnétique (Flux jump).
Lorsque le champ magnétique pénètre dans le supraconducteur, un courant d'écrantage (courant d'ancrage) se met à circuler. Si le champ magnétique externe fluctue, les flux magnétiques se déplacent, générant une chaleur de Joule. Si la capacité thermique du supraconducteur est faible et sa conductivité thermique basse, cette chaleur provoque une élévation locale de la température, ce qui diminue la densité de courant critique $J_c$. La baisse de $J_c$ entraîne une pénétration accrue des flux magnétiques, générant encore plus de chaleur. Le phénomène où cette boucle de rétroaction positive conduit à un quench catastrophique est appelé « saut de flux » (Flux jump).

Le premier critère pour éviter cela est le « critère de stabilité adiabatique » (Adiabatic stability criterion). En posant $d$ le rayon du filament, $C$ la chaleur massique, et $-(dJ_c/dT)$ la dérivée en température de la densité de courant critique, la dimension maximale $d_{max}$ pour éviter le saut de flux est proportionnelle à l'expression suivante :

$$ d_{max} \propto \sqrt{ \frac{C}{\mu_0 J_c |dJ_c/dT|} } $$

À des températures cryogéniques, la chaleur massique $C$ est si faible que $d_{max}$ est généralement de quelques dizaines de $\mu m$ au maximum. Par conséquent, le supraconducteur doit être divisé en fils fins (filaments) de l'ordre du micron.

Cependant, les amincir n'est pas suffisant. Si l'on regroupe de nombreux filaments, un couplage électromagnétique (courants de couplage) se produit entre eux, et l'ensemble se comporte comme un seul gros supraconducteur. Pour pallier cela, les filaments sont enveloppés dans un métal normal (comme le cuivre), et l'ensemble du fil est ensuite « torsadé » dans le sens de la longueur. En raccourcissant le pas de torsion $L_p$, on réduit la surface de boucle des courants de couplage et on rompt la liaison magnétique.
De plus, en cas de perturbation thermique, pour dissiper rapidement la chaleur générée vers l'environnement et pour dériver le courant en cas de transition vers l'état normal, on utilise comme matrice du cuivre pur exempt d'oxygène à haute conductivité thermique et électrique (cuivre avec un RRR (Residual Resistivity Ratio) élevé). C'est ce qu'on appelle le « critère de stabilité dynamique » (Dynamic stability criterion). Le rapport volumique entre les filaments supraconducteurs et la matrice de cuivre (ratio Cu/SC) se situe généralement entre 1,0 et 10,0, et est soigneusement conçu en fonction de l'application de l'aimant et des exigences de stabilité.

## Annexe C : Circuit de décharge lors d'un quench et conception quantitative de la tension maximale

Dans la conception de la protection d'un aimant, le choix de la résistance de décharge $R_d$ est un processus extrêmement important pour trouver le compromis entre la sécurité de l'aimant et l'isolation électrique.
Lorsqu'un aimant d'inductance $L$ et de courant nominal initial $I_0$ subit un quench, l'atténuation du courant dans le circuit où une résistance de décharge $R_d$ a été insérée obéit à l'équation suivante, compte tenu de la résistance normale $R_c(t)$ de la bobine elle-même :

$$ L \frac{dI}{dt} + (R_c(t) + R_d) I = 0 $$

Pour simplifier, si l'on suppose que $R_d$ est inséré immédiatement après le quench et que $R_c(t)$ est suffisamment petit par rapport à $R_d$, le courant s'atténue de manière exponentielle :

$$ I(t) = I_0 \exp\left(-\frac{R_d}{L} t\right) $$

Dans ce cas, l'intégrale MIITs est calculée comme suit :

$$ \int_0^\infty I^2 dt = \int_0^\infty I_0^2 \exp\left(-\frac{2R_d}{L} t\right) dt = \frac{L I_0^2}{2 R_d} $$

D'après l'équation de la chaleur adiabatique mentionnée plus haut, pour maintenir la température du point chaud sous une valeur tolérable (ex : 150 K), cette intégrale MIITs doit être inférieure à une certaine valeur critique $U_{max}$ (une constante déterminée par les propriétés du conducteur).

$$ \frac{L I_0^2}{2 R_d} \le U_{max} \implies R_d \ge \frac{L I_0^2}{2 U_{max}} $$

En d'autres termes, du point de vue de la protection thermique, la résistance de décharge $R_d$ doit être **suffisamment grande**.

D'un autre côté, au moment où la résistance de décharge est insérée, une tension induite élevée $V_{max}$ apparaît aux bornes de l'aimant.

$$ V_{max} = I_0 R_d $$

Cette tension est appliquée entre la bobine et la masse (la terre), ou entre les couches (inter-couches) de la bobine. Si $V_{ins}$ est la tension de tenue maximale que le revêtement isolant de l'aimant (Kapton ou résine époxy) peut supporter, alors

$$ I_0 R_d \le V_{ins} \implies R_d \le \frac{V_{ins}}{I_0} $$

En d'autres termes, du point de vue de l'isolation électrique, la résistance de décharge $R_d$ doit être **suffisamment petite**.

La valeur de la résistance de décharge, l'inductance de l'aimant $L$ (et donc l'équilibre entre le nombre de spires et la valeur du courant), ainsi que la structure isolante, sont conçues de manière à satisfaire ces deux conditions contradictoires. Dans les aimants géants (comme le LHC ou ITER), l'inductance $L$ étant très élevée, il devient impossible de satisfaire les deux conditions avec la seule résistance de décharge. Par conséquent, il est indispensable de recourir à un système de protection active plus sophistiqué, en utilisant les « dispositifs de chauffage de protection » (Quench Heaters) mentionnés plus haut pour augmenter de force et rapidement la résistance $R_c(t)$, de façon à obtenir la résistance effective tout en évitant les concentrations thermiques localisées.

La fusion de ces calculs minutieux et de l'approche de la science des matériaux dans un environnement cryogénique est sans doute le miracle de l'ingénierie que représente la technologie moderne des aimants supraconducteurs.

## Conclusion : L'ingénierie de l'extrême en constante recherche de repousser les limites

L'ingénierie cryogénique, qui s'approche des limites des lois de la physique au zéro absolu, et la technologie des aimants supraconducteurs, qui manipule une énergie colossale. Ces technologies forment un pont exceptionnel reliant un phénomène physique microscopique tel que la mécanique quantique à des infrastructures géantes de l'ordre du mètre, telles que les trains à lévitation magnétique et les accélérateurs géants.

Face au risque d'emballement thermique causé par les quench, les aimants, conçus en repoussant les limites du calcul des contraintes, de l'analyse de la conduction thermique et de l'ingénierie des propriétés des matériaux supraconducteurs, représentent le summum de la sagesse humaine. À l'avenir, grâce à la poursuite de l'évolution des matériaux supraconducteurs à haute température et à l'innovation des technologies de réfrigération, nous parviendrons à maîtriser les environnements cryogéniques et les champs magnétiques intenses inexplorés en les rendant plus accessibles. La frontière ouverte par la cryogénie et la supraconductivité n'en est qu'à ses balbutiements.
