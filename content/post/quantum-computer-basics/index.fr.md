---
title: "【Anatomie Complète】 Qu\"est-ce qu\"un ordinateur quantique ? 〜 Le principe de calcul ultime expliqué de zéro 〜"
date: 2026-09-05T22:10:00+09:00
tags: ["Ordinateur quantique", "Physique", "Technologie"]
image: "quantum_basics_eyecatch_1788613712487.jpg"
categories: ["Mathématiques, Cryptographie et Quantique"]
---

## Introduction : Le « changement de paradigme de calcul » apporté par l'ordinateur quantique

Ces dernières années, il ne se passe pas un jour sans que nous voyions les mots « ordinateur quantique » dans les actualités ou les articles technologiques. Des histoires semblables à celles des films de science-fiction, telles que « Des calculs qui prendraient des milliers d'années aux superordinateurs actuels seront terminés en quelques minutes » ou « Toutes les technologies de cryptage actuelles pourraient être brisées », sont racontées avec conviction. Des géants de l'informatique comme Google, IBM et Microsoft aux universités et startups du monde entier, tous se font une concurrence acharnée pour mettre en pratique cette technologie de rêve.

Cependant, lorsqu'on demande « Qu'est-ce qu'un ordinateur quantique après tout ? », peu de personnes peuvent répondre avec précision. Beaucoup de gens ont une image vague d'une « boîte magique capable de calculer toutes les combinaisons en même temps », mais strictement parlant, ce n'est pas correct.

Dans cet article, nous expliquerons en profondeur depuis les bases, de manière experte mais facile à comprendre, en quoi un ordinateur quantique diffère fondamentalement d'un ordinateur classique (les PC et smartphones que nous utilisons habituellement), et comment il utilise des phénomènes étranges de la mécanique quantique tels que la « superposition » (Superposition), l'« intrication quantique » (Entanglement) et les « portes quantiques » (Quantum gates) pour les calculs. Au moment où vous aurez fini de lire cet article, vous devriez comprendre clairement la grandeur essentielle des ordinateurs quantiques et leurs défis actuels.

---

## Chapitre 1 : La différence décisive entre les ordinateurs classiques et les ordinateurs quantiques

Afin de comprendre le fonctionnement des ordinateurs quantiques, nous devons d'abord revoir le fonctionnement des « ordinateurs classiques » que nous utilisons actuellement.

### Tableau comparatif : Ordinateur classique vs Ordinateur quantique

| Élément | Ordinateur classique | Ordinateur quantique |
| --- | --- | --- |
| **Unité de base** | Bit (0 ou 1) | Qubit (superposition de 0 et 1) |
| **Expression de l'état** | Déterministe | Probabiliste (non déterminé jusqu'à l'observation) |
| **Méthode de calcul** | Traitement séquentiel (nécessite des cœurs physiques pour la parallélisation) | Parallélisme quantique (manipulation simultanée d'états exponentiels) |
| **Calculs de prédilection** | Opérations arithmétiques, traitement de données quotidien | Factorisation en nombres premiers, calculs de chimie quantique |
| **Tolérance aux erreurs** | Très forte | Très faible (nécessite des environnements cryogéniques et une correction d'erreurs) |

### Le monde des ordinateurs classiques : Le « Bit » qui vaut 0 ou 1
Les ordinateurs classiques représentent toutes les informations sous forme de « 0 » ou « 1 ». C'est ce qu'on appelle un **bit** (Bit). Physiquement, cela est représenté par la tension élevée (1) ou faible (0) des transistors sur une puce semi-conductrice.
Les photos haute résolution de votre smartphone, le texte que vous lisez actuellement et vos vidéos YouTube préférées sont finalement réduits à un nombre massif de « séquences de 0 et de 1 ». Le calcul n'est rien d'autre que le processus d'application d'opérations à ces séquences de 0 et de 1 en combinant des circuits logiques de base tels que AND (et logique), OR (ou logique) et NOT (non logique).
Il s'agit d'un monde très certain et déterministe. Si l'entrée est la même, la même sortie sera toujours obtenue.

### Le monde des ordinateurs quantiques : Le « Qubit » qui est à la fois 0 et 1
D'autre part, l'unité d'information minimale d'un ordinateur quantique est appelée **qubit** (Qubit : Quantum bit).
La plus grande caractéristique d'un qubit est que, contrairement à un bit classique qui est soit dans l'état « 0 » soit dans l'état « 1 », il peut prendre un état dans lequel « 0 et 1 sont mélangés avec une certaine probabilité ». C'est ce qu'on appelle la **« Superposition »** (Superposition).

Par exemple, si un bit classique est une pièce placée face « pile » ou face « face » vers le haut, un qubit est souvent comparé à une « pièce qui tourne continuellement dans les airs ». Une pièce en rotation ne peut être dite ni pile ni face, et les deux états se chevauchent. Ce n'est qu'au moment où la pièce tombe sur le sol et s'arrête (ce que la mécanique quantique appelle « l'observation ») qu'il est déterminé si c'est « pile » ou « face ».

Un ordinateur quantique intègre cette propriété spécifique au monde microscopique (la mécanique quantique), où « l'état n'est pas déterminé jusqu'à ce qu'il soit observé », directement dans le processus de traitement de l'information.

---

## Chapitre 2 : Trois propriétés quantiques qui changent fondamentalement le calcul

La source de l'incroyable puissance de calcul d'un ordinateur quantique n'est pas simplement une fréquence d'horloge élevée ou de petits composants. Elle réside dans l'utilisation des lois de la physique elles-mêmes comme ressources de calcul. Les trois phénomènes quantiques suivants sont les principaux facteurs clés.

### 1. La superposition (Superposition) et la quantité d'informations exponentielle
Comme mentionné précédemment, un qubit peut conserver les deux états 0 et 1 en même temps. Un qubit est une « superposition de 0 et de 1 », mais que se passe-t-il si nous augmentons le nombre de qubits ?

- 1 qubit : Superposition de 2 états (0, 1)
- 2 qubits : Superposition de 4 états (00, 01, 10, 11)
- 3 qubits : Superposition de 8 états
- **N qubits : Superposition de $2^N$ motifs** 

Avec seulement 50 qubits, il est possible de conserver simultanément $2^{50}$ (environ 1 100 billions) d'états. Et avec seulement 300 qubits, on peut conserver $2^{300}$ motifs (plus que le nombre de tous les atomes de l'univers !) à la fois. Cette capacité exponentielle de rétention d'informations est le fondement du potentiel des ordinateurs quantiques. Il est physiquement impossible pour un ordinateur classique de stocker dans sa mémoire plus d'états qu'il n'y a d'atomes dans l'univers.

### 2. L'intrication quantique (Entanglement) : L'action fantôme à distance
L'intrication quantique est un phénomène tellement étrange et contraire à l'intuition humaine qu'Einstein l'a appelé « l'action fantôme à distance » (Spooky action at a distance) et a refusé de l'accepter toute sa vie.

Lorsque plusieurs qubits sont dans un état « d'intrication quantique », ils sont fortement liés les uns aux autres, créant une relation semblable à une communauté de destin : **« Lorsque l'état de l'un est déterminé, quelle que soit la distance, l'état de l'autre est instantanément déterminé »**.

Par exemple, supposons qu'il y ait deux qubits A et B dans un état intriqué (ils sont chacun dans une superposition de 0 et de 1). Si A est observé et vaut « 0 », dépassant la vitesse de la lumière qui est la limite de la vitesse de transmission de l'information, l'état de B est instantanément déterminé (par exemple, pour être toujours « 1 »).
Dans un ordinateur quantique, cette intrication quantique est utilisée pour exprimer des corrélations complexes entre plusieurs qubits et effectuer un traitement de l'information massivement parallèle. Sans intrication, la puissance de calcul d'un ordinateur quantique ne serait pas très différente de celle d'un ordinateur classique.

### 3. L'interférence quantique (Quantum Interference) : La magie qui fait ressortir la bonne réponse
Vous pourriez penser : « Si vous pouvez conserver tous les motifs en même temps, pourquoi ne pas les calculer tous en parallèle et obtenir la réponse en un instant ? ». C'est le malentendu le plus courant à propos des ordinateurs quantiques.
Même si vous effectuez des calculs dans un état superposé, vous devez finalement faire une « observation » pour connaître la réponse. Cependant, au moment où vous l'observez, l'état s'effondre de manière aléatoire en un seul des $2^N$ motifs. Avec cela, vous obtiendrez simplement une réponse aléatoire (au hasard).

C'est ici qu'intervient **« l'interférence quantique »** (Interference). Lorsque des ondes entrent en collision, le phénomène où elles se renforcent là où les longueurs d'onde correspondent et s'annulent là où elles sont décalées est utilisé (le principe est fondamentalement le même que celui des écouteurs à réduction de bruit).

Un excellent « algorithme quantique » manipule habilement l'état quantique pendant le processus de calcul afin que **« les amplitudes de probabilité des états (ondes) menant à la bonne réponse se renforcent (amplification) »** et **« les amplitudes de probabilité des états menant à une mauvaise réponse s'annulent (annulation) »**. Puis, lors de l'observation finale, il fait en sorte que la « bonne réponse » apparaisse avec une probabilité de presque 100 %. Concevoir habilement ce processus d'interférence est l'essence même de la programmation quantique.

---

## Chapitre 3 : Comment calcule-t-on ? Les « portes quantiques » et les « circuits quantiques »

Tout comme les ordinateurs classiques utilisent des portes logiques (AND, OR, NOT, etc.) pour effectuer des calculs, les ordinateurs quantiques appliquent des opérations appelées **« portes quantiques »** (Quantum Gates) aux qubits pour effectuer des calculs. Une combinaison de plusieurs portes quantiques est appelée un **circuit quantique** (Quantum Circuit).

L'état d'un qubit est exprimé mathématiquement comme un point sur la surface d'une sphère tridimensionnelle appelée « sphère de Bloch » (Bloch sphere). Le pôle Nord est « 0 », le pôle Sud est « 1 » et l'équateur est un « état où 0 et 1 se superposent à moitié ». Une porte quantique n'est rien d'autre qu'une opération de rotation de l'état (vecteur) à la surface de cette sphère.

Voici quelques-unes des portes quantiques les plus représentatives.

### 1. La porte de Hadamard (Porte H)
Il s'agit de la porte la plus fondamentale spécifique aux ordinateurs quantiques, qui n'existe pas dans les ordinateurs classiques. Faire passer un qubit dans l'état parfait « 0 » à travers une porte H crée un « état de superposition parfaite » (un point sur l'équateur de la sphère de Bloch) où 0 et 1 sont observés avec exactement la moitié de la probabilité chacun. En tant qu'étape d'initialisation du calcul quantique, de nombreux algorithmes commencent par appliquer cette porte H à tous les qubits.

### 2. Les portes de Pauli (Portes X, Y, Z)
Ce sont des portes qui incluent des opérations équivalentes à la porte NOT d'un ordinateur classique (inversant 0 à 1 et 1 à 0). Sur la sphère de Bloch, cela correspond à une rotation de 180 degrés autour des axes X, Y et Z. En particulier, la porte X inverse le pôle Nord (0) vers le pôle Sud (1), elle a donc exactement la même fonction que la porte NOT classique. La porte Z a pour rôle d'inverser la « phase » (comme le timing de l'onde) de la superposition, ce qui est extrêmement important pour provoquer l'interférence quantique.

### 3. La porte CNOT (Porte NOT contrôlée)
C'est une porte super importante pour créer l'intrication quantique. Elle utilise 2 qubits (un bit de contrôle et un bit cible).
Elle fonctionne ainsi : « Si le bit de contrôle est à 1, l'état du bit cible est inversé (porte X). Si le bit de contrôle est à 0, ne rien faire ». À première vue, cela ressemble à un simple branchement conditionnel IF, mais que se passe-t-il si le bit de contrôle est dans un « état de superposition de 0 et de 1 » ? Le bit cible devient un « état où ce qui est inversé et ce qui ne l'est pas se superposent », et les destins des 2 bits sont complètement liés. Les deux qubits sont magnifiquement « intriqués ».

En disposant et en appliquant ces portes dans l'ordre de gauche à droite, comme sur une partition de musique, des algorithmes complexes sont exécutés.

---

## Chapitre 4 : Pour quoi les ordinateurs quantiques sont-ils doués et pour quoi ne le sont-ils pas ?

Je tiens à partager un fait important ici. Un ordinateur quantique n'est pas un dieu omnipotent.
Pour les tâches quotidiennes telles que la navigation sur le Web, le rendu vidéo, le traitement de macros Excel ou l'exécution d'applications pour smartphone générales, il est probable que les ordinateurs quantiques ne surpasseront jamais les ordinateurs classiques. Pour ce traitement séquentiel, les ordinateurs classiques, qui sont déjà hautement optimisés et offrent une vitesse et un faible coût écrasants, sont mieux adaptés.

Les ordinateurs quantiques ne montrent leur véritable valeur que pour **« les problèmes spécifiques où les combinaisons de calculs dans un ordinateur classique explosent de manière exponentielle, prenant un temps comparable à la durée de vie de l'univers »**. C'est ce qu'on appelle la « suprématie quantique » (Quantum Supremacy) ou l'« avantage quantique » (Quantum Advantage).

### Ce pour quoi les ordinateurs quantiques sont doués (Applications tueuses)

#### 1. Factorisation en nombres premiers et cryptanalyse (Algorithme de Shor)
Actuellement, les communications sécurisées sur Internet (telles que les paiements par carte de crédit et la transmission d'informations personnelles) sont protégées par le « cryptage RSA », etc., qui repose sur l'hypothèse que « la factorisation en nombres premiers de très grands nombres est pratiquement impossible (prend énormément de temps) pour un ordinateur classique ».
Cependant, en utilisant l'« algorithme de Shor » découvert par le mathématicien Peter Shor en 1994, les ordinateurs quantiques peuvent exploiter intelligemment les interférences pour le résoudre à une vitesse spectaculaire (temps polynomial). En conséquence, il existe un risque que le système cryptographique actuel s'effondre à l'avenir, et les banques centrales et les agences gouvernementales du monde entier se précipitent pour faire la transition vers la « cryptographie post-quantique » (Post-Quantum Cryptography).

#### 2. Calculs de chimie quantique et développement de nouveaux matériaux et médicaments
Le comportement des molécules et des atomes dans le monde naturel obéit aux lois de la mécanique quantique en premier lieu. Tenter de simuler le comportement de molécules complexes avec un ordinateur classique entraîne une explosion des combinaisons d'interactions électroniques, atteignant la limite des ressources de calcul même pour des molécules relativement petites.
Comme l'a dit le lauréat du prix Nobel de physique Richard Feynman : « Si vous voulez simuler la nature, vous feriez mieux de la rendre quantique », les ordinateurs quantiques démontrent une puissance native écrasante dans la simulation de matériaux. Des avancées permettant de résoudre les défis de l'humanité sont attendues, telles que la conception de nouveaux médicaments révolutionnaires, la découverte de matériaux supraconducteurs à température ambiante, le développement de batteries et de cellules solaires à haut rendement, et la synthèse d'engrais économes en énergie.

#### 3. Problèmes d'optimisation combinatoire et recherche (Algorithme de Grover)
Les algorithmes quantiques sont également efficaces pour trouver la solution optimale parmi un très grand nombre d'options (itinéraires logistiques optimaux, optimisation de portefeuille financier, etc.). En utilisant « l'algorithme de Grover », vous pouvez trouver les données souhaitées en un nombre de fois égal à la racine carrée de l'itinéraire de l'ordinateur classique lors d'une recherche dans une base de données où les données ne sont pas triées. Par exemple, s'il y a 100 millions d'enregistrements de données, une recherche qui prendrait jusqu'à 100 millions de fois avec un ordinateur classique peut être effectuée en seulement 10 000 fois environ.

---

## Chapitre 5 : Le mur matériel qui se dresse sur le chemin : « Décohérence » et « Correction d'erreurs quantiques »

En théorie, un ordinateur quantique est magiquement puissant, mais un mur physique extrêmement haut et escarpé se dresse sur le chemin de sa mise en œuvre pratique. Le plus grand ennemi est le **« bruit »**.

La « superposition » et l'« intrication quantique » des qubits sont des états extrêmement délicats et fragiles. Le simple fait de toucher une légère quantité de chaleur, une fluctuation d'onde électromagnétique ou un rayon cosmique environnant provoque l'effondrement instantané de l'état magique, le transformant en un simple bit classique. Ce phénomène est appelé **« Décohérence »** (effondrement quantique).

### Une concurrence féroce dans les méthodes de réalisation physique
Actuellement, divers instituts à travers le monde mènent des recherches sur la façon de construire physiquement ces qubits délicats, et une lutte pour la suprématie est en cours.

- **Méthode supraconductrice (Superconducting)** : Adoptée par Google, IBM, Amazon, etc. Elle utilise un circuit supraconducteur en forme de boucle et contrôle l'état quantique en le refroidissant avec un énorme réfrigérateur à une température extrêmement basse proche du zéro absolu (environ -273°C). C'est la méthode actuellement la plus avancée et avec laquelle il est le plus facile d'augmenter le nombre de qubits, mais l'équipement de refroidissement est énorme et coûteux.
- **Méthode du piège à ions (Trapped Ion)** : Adoptée par IonQ, Quantinuum, etc. Elle piège les ions (atomes) dans le vide avec des champs électromagnétiques et les contrôle avec des lasers précis. Sa force est que tous les qubits sont uniformes et peuvent maintenir leur état pendant une longue période (long temps de cohérence), mais sa vitesse de fonctionnement est plus lente par rapport à la méthode supraconductrice.
- **Méthode photonique (Photonic)** : PsiQuantum, etc., se concentrent dessus. Elle utilise des particules de lumière (photons). Elle présente l'avantage majeur qu'elle fonctionne en grande partie à température ambiante sans nécessiter un environnement cryogénique, et elle est très compatible avec les technologies de fabrication de puces en silicium et de communication par fibre optique existantes.
- **Méthode topologique (Topological)** : Longtemps étudiée par Microsoft. Il s'agit d'une approche ambitieuse qui utilise les propriétés topologiques (géométrie topologique) de particules spéciales appelées anyons pour créer des qubits fondamentalement résistants au bruit environnemental (moins sujets aux erreurs). On dit qu'elle est la plus forte en théorie, mais qu'elle présente les obstacles à la réalisation physique les plus élevés.

### Le chemin vers le but ultime, l'« ordinateur quantique tolérant aux pannes (FTQC) »
Des erreurs de calcul (telles que le basculement de bits dû aux rayons cosmiques) existent également dans le monde de l'informatique classique d'aujourd'hui, mais comme elles sont parfaitement corrigées par un « code de correction d'erreurs », nous pouvons utiliser nos smartphones sans jamais être conscients d'une erreur. Pour effectuer des calculs à grande échelle pratiques même avec un ordinateur quantique, une **« Correction d'erreurs quantiques »** (Quantum Error Correction: QEC) similaire est indispensable.

Cependant, comme l'état quantique a la propriété de se « briser lorsqu'on l'observe », il y a un dilemme fatal où l'on ne peut pas regarder (observer) directement le contenu pour vérifier les erreurs.
Pour contourner cela, une théorie a été établie pour construire un « qubit logique » stable capable de détecter et de corriger les erreurs en combinant habilement de nombreux « qubits physiques » instables (tels que le code de surface).
Cependant, on dit que 1 000 à 10 000 qubits physiques sont nécessaires pour fabriquer un seul qubit logique. Pour exécuter l'algorithme de Shor et d'autres à l'aide de milliers de qubits logiques, un système massif avec des millions à des dizaines de millions de qubits physiques au total est requis.

Actuellement, nous sommes dans ce qu'on appelle l'ère des appareils **NISQ (Noisy Intermediate-Scale Quantum : Quantique à échelle intermédiaire bruité)**. Ce sont des machines de transition qui fonctionnent avec des dizaines à des centaines de qubits sans correction d'erreurs.
Les experts prédisent qu'il faudra encore des décennies de recherche et de développement à long terme pour atteindre le but ultime d'un **« Ordinateur quantique tolérant aux pannes »** (Fault-Tolerant Quantum Computer: FTQC) entièrement capable de corriger les erreurs.

---

## Chapitre 6 : L'histoire des ordinateurs quantiques et perspectives d'avenir

Enfin, jetons un œil à la façon dont les ordinateurs quantiques sont nés et où ils se dirigent à l'avenir.

### De la naissance de la théorie à la démonstration de la « suprématie quantique »
- **Les années 1980** : Les physiciens Paul Benioff et Richard Feynman ont proposé le concept d'un ordinateur qui utilise les principes de la mécanique quantique. La phrase « Si vous voulez simuler la nature, utilisez la mécanique quantique » en a été le point de départ.
- **1994** : Peter Shor annonce un algorithme quantique de factorisation en nombres premiers (l'algorithme de Shor). Cela a choqué le monde et a déclenché un afflux massif de fonds de recherche.
- **1996** : Lov Grover publie l'algorithme de Grover pour accélérer la recherche de données.
- **2019** : Une étape historique. Google a annoncé qu'il avait utilisé un processeur supraconducteur de 53 qubits appelé « Sycamore » pour effectuer un calcul de vérification de génération de nombres aléatoires, qui prendrait (soi-disant) 10 000 ans sur un superordinateur classique, en environ 200 secondes. Cela a fait grand bruit en tant que première déclaration de démonstration de la **« Suprématie quantique »** (Quantum Supremacy) au monde (plus tard, IBM et d'autres ont amélioré l'algorithme du côté du superordinateur classique et ont rétorqué qu'il pouvait être calculé en quelques jours, conduisant à des débats animés).
- **Après 2023** : IBM annonce le processeur « Condor » avec plus de 1 000 qubits. De plus, l'Université de Harvard et d'autres ont réussi à générer et à manipuler des « qubits logiques », et les premières démonstrations de technologie de correction d'erreurs commencent à être signalées les unes après les autres.

### Vers la technologie de la prochaine génération
Un ordinateur quantique n'est pas simplement un « CPU de nouvelle génération avec une vitesse d'horloge plus rapide ». Il s'agit d'un véritable changement de paradigme en informatique, réécrivant le concept même de calcul à partir de zéro avec les règles de la mécanique quantique qui régissent le monde microscopique.

Il est peu probable que nous ayons un « smartphone quantique personnel » dans nos poches de notre vivant (ce n'est d'ailleurs pas nécessaire). Cependant, l'avenir dans lequel un puissant centre de données quantique de l'autre côté d'un réseau cloud tel qu'AWS ou Azure découvre soudainement un remède miracle contre une maladie incurable, ou produit un matériau d'énergie propre de rêve qui résout le réchauffement climatique (par exemple, un catalyseur qui synthétise l'ammoniac à partir de l'azote de l'air à température ambiante), approche à grands pas.

Actuellement, nous sommes encore aux premiers jours équivalents à l'ENIAC dans les années 1940, qui fonctionnait avec des cartes perforées alors que la pièce entière chauffait à cause de la chaleur d'énormes tubes à vide. Cependant, des chercheurs et ingénieurs de haut niveau du monde entier se creusent les méninges, et des percées technologiques sont signalées chaque jour.
Nous qui pouvons assister en temps réel au processus d'évolution de cette nouvelle « aube du calcul » pouvons être considérés comme vivant dans une période très excitante de l'histoire.

La porte du monde quantique vient de s'ouvrir. Nous devons garder un œil sur les tendances futures.

---
*Cet article vise à expliquer les concepts fondamentaux de l'informatique quantique d'une manière facile à comprendre pour les hommes d'affaires et le grand public intéressé par la technologie. Veuillez noter que des simplifications ont été apportées à partir des définitions mathématiques et physiques strictes (telles que la notation bra-ket et les détails de l'amplitude de probabilité complexe).*
