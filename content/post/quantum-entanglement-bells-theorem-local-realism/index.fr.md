---
title: "Intrication quantique et inégalités de Bell : L'ultime défaite d'Einstein et l'aube de la révolution de l'information quantique"
description: "« L'action fantôme à distance » et le paradoxe EPR. L'inégalité de Bell prouvant l'effondrement du réalisme local, l'expérience d'Aspect, et la trajectoire vers le prix Nobel."
slug: "quantum-entanglement-bells-theorem-local-realism"
date: "2026-10-03T05:00:00+09:00"
categories: ["physics", "quantum"]
tags: ["quantum-entanglement", "bells-theorem", "quantum-information", "physics-history"]
image: "eyecatch.jpg"
---

# Intrication quantique et inégalités de Bell : L'ultime défaite d'Einstein et l'aube de la révolution de l'information quantique

Le plus grand mystère de la physique moderne et, en même temps, son outil le plus puissant, est l'« intrication quantique (Quantum Entanglement) ». Et l'« inégalité de Bell » a brisé l'intuition humaine du « réalisme local ». Ce ne sont pas de simples jeux théoriques de la physique ; ils nous confrontent à la nature fondamentale de l'univers et servent de base aux technologies de la prochaine génération, telles que les ordinateurs quantiques et la communication cryptographique quantique.

Dans cet article, nous expliquerons en grand détail, du point de vue de la physique, de la science de l'information quantique et de la philosophie des sciences, le drame épique qui commence avec l'article EPR d'Einstein et de ses collègues en 1935, les luttes de la théorie des variables cachées, la dérivation historique de l'inégalité par John Stewart Bell, l'inégalité CHSH et la preuve mathématique de la violation maximale dans la mécanique quantique (la borne de Tsirelson), jusqu'à la vérification expérimentale par Aspect et d'autres, menant au prix Nobel de physique en 2022. De plus, nous approfondirons avec des formules mathématiques des sujets tels que le rejet complet du réalisme local par l'état GHZ d'intrication multipartite, le protocole rigoureux de la téléportation quantique et les méthodes de quantification de l'intrication.

---

## Chapitre 1 : 1935, La contre-attaque d'Einstein

Alors que la mécanique quantique était formalisée dans les années 1920 par l'école de Copenhague (Niels Bohr, Werner Heisenberg, etc.), Albert Einstein nourrissait une profonde insatisfaction à l'égard de son interprétation probabiliste et non déterministe. Sa célèbre phrase « Dieu ne joue pas aux dés » exprime son rejet de la nature probabiliste sous-jacente à la mécanique quantique.

En 1935, avec Boris Podolsky et Nathan Rosen, Einstein a publié un article historique qui restera dans l'histoire de la physique, « La description quantique de la réalité physique peut-elle être considérée comme complète ? » (Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?), connu sous le nom d'« article EPR ». Le but de cet article était de prouver logiquement que la mécanique quantique est « incomplète », c'est-à-dire qu'il doit exister des « variables cachées » que nous ne connaissons pas encore.

### Définitions de la localité et du réalisme

Pour comprendre le développement logique de l'article EPR, il est nécessaire de saisir précisément les deux concepts fondamentaux qu'Einstein et ses collègues ont supposés.

1. **Réalisme (Realism)** :
   L'idée qu'un système physique possède des propriétés (valeurs) physiques déterminées, qu'il soit observé ou non. Dans l'article EPR, il a été défini ainsi : « Si, sans perturber d'aucune façon un système, on peut prédire avec certitude (c'est-à-dire avec une probabilité égale à l'unité) la valeur d'une quantité physique, alors il existe un élément de réalité physique correspondant à cette quantité physique. » En d'autres termes, l'objet possède ses attributs de manière déterministe avant la mesure, ce qui est le bon sens évident de la mécanique classique.
2. **Localité (Locality)** :
   Le principe basé sur la théorie de la relativité stipulant que les opérations ou les mesures effectuées dans l'une des deux régions spatialement séparées ne peuvent pas affecter instantanément la réalité physique de l'autre région à une vitesse supérieure à celle de la lumière. Selon la théorie de la relativité restreinte, la transmission d'informations plus vite que la lumière entraîne une rupture de la causalité, de sorte que toute interaction physique est soumise à la limite de la vitesse de la lumière.

### « L'action fantôme à distance » (Spooky action at a distance) et le paradoxe EPR

Dans l'article EPR, l'expérience de pensée suivante a été présentée.
Considérons deux particules A et B qui se sont fortement éloignées l'une de l'autre après avoir interagi fortement. Dans le cadre de la mécanique quantique, ces deux particules sont dans un état « intriqué (Entangled) » et sont décrites comme une fonction d'onde globale.

Supposons que l'on mesure la position $x_A$ de la particule A. En raison de lois comme la conservation de la quantité de mouvement, lorsque la position de A est déterminée, la position $x_B$ de la particule B l'est instantanément. D'autre part, si on mesure la quantité de mouvement $p_A$ de la particule A, la quantité de mouvement $p_B$ de la particule B est déterminée instantanément.
Selon la mécanique quantique, la position et la quantité de mouvement sont des grandeurs physiques non commutatives ($[x, p] = i\hbar$) et ne peuvent avoir des valeurs déterminées simultanément (principe d'incertitude d'Heisenberg). Cependant, il semble que le choix de la mesure sur A (mesurer la position ou la quantité de mouvement) détermine instantanément, plus vite que la lumière, l'état de B (s'il est dans un état de position déterminée ou de quantité de mouvement déterminée).

Si la « localité » est correcte, il est impossible qu'une mesure sur A affecte instantanément B. Einstein l'a appelée « action fantôme à distance (Spukhafte Fernwirkung / Spooky action at a distance) » et l'a fortement critiquée. Par conséquent, ils ont conclu que B devait posséder à l'avance des valeurs déterminées (variables cachées) pour la position et la quantité de mouvement avant même d'être mesurée, et que la mécanique quantique, incapable de décrire à la fois la position et la quantité de mouvement, est une « théorie incomplète ». Ce paradoxe a été le premier pas vers la compréhension fondamentale de l'intrication dans la théorie de l'information quantique ultérieure.

---

## Chapitre 2 : Le dilemme de la théorie des variables cachées et la mécanique bohmienne

Après la publication de l'article EPR, les physiciens se sont tournés vers l'exploration de l'hypothèse selon laquelle « la mécanique quantique est correcte mais incomplète, et il pourrait exister une théorie déterministe (théorie des variables cachées) à un niveau plus profond ».

### Le faux « théorème d'impossibilité » de von Neumann

C'est le génial mathématicien John von Neumann qui a jeté un froid sur ce débat. Dans son livre de 1932, *Les fondements mathématiques de la mécanique quantique*, il a présenté une preuve (théorème d'impossibilité) selon laquelle il est mathématiquement impossible de construire une « théorie des variables cachées » qui donnerait les mêmes prédictions que la mécanique quantique.
L'autorité de von Neumann était si grande que, pendant les décennies suivantes, la tendance selon laquelle « la recherche de variables cachées est dénuée de sens » a dominé la communauté des physiciens.

Cependant, comme il a été révélé plus tard, la preuve de von Neumann incluait une hypothèse extrêmement restrictive et non physique (l'additivité des valeurs attendues de quantités physiques non commutatives : l'hypothèse que $\langle A+B \rangle = \langle A \rangle + \langle B \rangle$ est valable même au niveau des variables cachées) comme « condition que les variables cachées doivent satisfaire », et n'était donc en réalité pas une preuve complète. Grete Hermann avait remarqué ce défaut très tôt, mais elle n'a pas attiré l'attention à l'époque.

### Mécanique bohmienne : Une théorie des variables cachées non locale

En 1952, David Bohm a brisé le théorème d'impossibilité de von Neumann et a construit une « théorie des variables cachées » déterministe (la mécanique bohmienne, ou théorie de De Broglie-Bohm) qui donne des prédictions parfaitement en accord avec la mécanique quantique.
Dans la théorie de Bohm, les particules ont toujours des positions définies (variables cachées) et sont guidées par un « potentiel quantique » qui s'étend dans tout l'univers. Ce potentiel $Q = -\frac{\hbar^2}{2m}\frac{\nabla^2 R}{R}$, obtenu en transformant l'équation de Schrödinger en coordonnées polaires, a la propriété singulière de ne pas dépendre de la distance et de ne pas s'atténuer.

Cependant, la mécanique bohmienne a eu un prix élevé. Parce que le potentiel quantique affecte instantanément tout l'espace, la théorie était intrinsèquement « non locale ». L'« action fantôme à distance » qu'Einstein détestait le plus était inhérente à la mécanique bohmienne en tant que fondement de la théorie.
Einstein a pris une attitude négative envers la théorie de Bohm, la qualifiant de « solution bon marché », et croyait toujours en l'existence d'une théorie des variables cachées « locale ».

---

## Chapitre 3 : L'état singulet des particules de spin 1/2 et les prédictions rigoureuses de la mécanique quantique

Avant de passer à l'inégalité de Bell, développons complètement le processus de calcul rigoureux bra-ket en utilisant les matrices de Pauli pour les corrélations d'intrication prédites par la mécanique quantique. Ce sera le cœur de la mécanique quantique qui entrera plus tard en conflit avec le réalisme local.

Supposons qu'une paire de particules de spin 1/2 soit générée et se trouve dans un « état singulet » (Singlet State) de spin total zéro. Cet état $|\psi^-\rangle$ est décrit comme suit :

$$ |\psi^-\rangle = \frac{1}{\sqrt{2}} \left( |\uparrow\rangle_A \otimes |\downarrow\rangle_B - |\downarrow\rangle_A \otimes |\uparrow\rangle_B \right) $$

Ici, $|\uparrow\rangle, |\downarrow\rangle$ représentent respectivement les états propres de spin vers le haut ($+1$) et vers le bas ($-1$) (base $z$). Il est parfois écrit de manière simplifiée $|\psi^-\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$.

Alice mesure le spin de chaque particule dans la direction $\vec{a}$, et Bob dans la direction $\vec{b}$. Les vecteurs de direction sont des vecteurs unitaires et peuvent être exprimés en coordonnées sphériques comme $\vec{a} = (\sin\theta_a\cos\phi_a, \sin\theta_a\sin\phi_a, \cos\theta_a)$, etc.
Les opérateurs de mesure de spin dans chaque direction sont $\sigma_a = \vec{a} \cdot \vec{\sigma}$ et $\sigma_b = \vec{b} \cdot \vec{\sigma}$ en utilisant le vecteur des matrices de Pauli $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$.

Ce que nous voulons savoir, c'est la valeur attendue du produit des résultats de mesure d'Alice et de Bob, $\langle \sigma_a \otimes \sigma_b \rangle$. Pour calculer cela, nous le développons selon la définition de la valeur attendue.

$$ \langle \psi^- | (\vec{a} \cdot \vec{\sigma}) \otimes (\vec{b} \cdot \vec{\sigma}) | \psi^- \rangle $$

Tout d'abord, en tant que propriété des matrices de Pauli, considérons $\vec{a} \cdot \vec{\sigma} = a_x \sigma_x + a_y \sigma_y + a_z \sigma_z$. Comme technique astucieuse pour simplifier les calculs, nous utilisons le fait que l'état singulet $|\psi^-\rangle$ est invariant par rotation (il a la même forme dans n'importe quelle base). Cependant, nous effectuerons ici un développement complet par une approche algébrique plus directe.

L'opérateur $(\vec{a} \cdot \vec{\sigma}) \otimes (\vec{b} \cdot \vec{\sigma})$ se développe comme suit :
$$ \sum_{i \in \{x,y,z\}} \sum_{j \in \{x,y,z\}} a_i b_j (\sigma_i \otimes \sigma_j) $$

Par la linéarité, la valeur attendue est :
$$ \sum_{i,j} a_i b_j \langle \psi^- | \sigma_i \otimes \sigma_j | \psi^- \rangle $$
Ici, nous évaluons $\langle \psi^- | \sigma_i \otimes \sigma_j | \psi^- \rangle$ pour chaque composante.

Pour $|\psi^-\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$,
- $\sigma_z \otimes \sigma_z$:
  $\sigma_z \otimes \sigma_z |01\rangle = (+1)(-1)|01\rangle = -|01\rangle$
  $\sigma_z \otimes \sigma_z |10\rangle = (-1)(+1)|10\rangle = -|10\rangle$
  Donc $\sigma_z \otimes \sigma_z |\psi^-\rangle = -|\psi^-\rangle$, et la valeur attendue est $-1$.
- $\sigma_x \otimes \sigma_x$:
  $\sigma_x \otimes \sigma_x |01\rangle = |10\rangle$
  $\sigma_x \otimes \sigma_x |10\rangle = |01\rangle$
  Donc $\sigma_x \otimes \sigma_x \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle) = \frac{1}{\sqrt{2}}(|10\rangle - |01\rangle) = -|\psi^-\rangle$, et la valeur attendue est $-1$.
- $\sigma_y \otimes \sigma_y$:
  De $\sigma_y |0\rangle = i|1\rangle, \sigma_y |1\rangle = -i|0\rangle$,
  $\sigma_y \otimes \sigma_y |01\rangle = (i|1\rangle) \otimes (-i|0\rangle) = |10\rangle$
  $\sigma_y \otimes \sigma_y |10\rangle = (-i|0\rangle) \otimes (i|1\rangle) = |01\rangle$
  Donc $\sigma_y \otimes \sigma_y |\psi^-\rangle = -|\psi^-\rangle$, et la valeur attendue est $-1$.

D'autre part, les valeurs attendues pour les composantes croisées (ex. $\sigma_x \otimes \sigma_y$) sont toutes égales à $0$.
Car, $\sigma_x \otimes \sigma_y |01\rangle = |1\rangle \otimes (-i|0\rangle) = -i|10\rangle$, etc., et en prenant le produit scalaire avec $\langle \psi^-|$, cela s'annule par orthogonalité.

Par conséquent, les termes non nuls sont uniquement ceux où $i=j$, et :
$$ \sum_{i} a_i b_i \langle \psi^- | \sigma_i \otimes \sigma_i | \psi^- \rangle = \sum_{i} a_i b_i (-1) = - (a_x b_x + a_y b_y + a_z b_z) = - \vec{a} \cdot \vec{b} $$
est rigoureusement dérivé.
Si $\theta$ est l'angle entre les vecteurs $\vec{a}$ et $\vec{b}$, par la définition du produit scalaire, $\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta = \cos\theta$ (la longueur est de 1 car les vecteurs de direction sont unitaires).
Par conséquent, la corrélation prédite par la mécanique quantique est l'équation simple et extrêmement belle suivante :

$$ E(\vec{a}, \vec{b}) = \langle \sigma_a \otimes \sigma_b \rangle = - \cos\theta $$

Cette puissante corrélation de $-\cos\theta$ est la source même du « comportement quantique caractéristique » qui ne peut absolument pas être reproduit par une théorie classique des variables cachées.


---

## Chapitre 4 : Le choc de John Stewart Bell et la dérivation rigoureuse de l'inégalité CHSH

En 1964, le physicien irlandais John Stewart Bell, qui menait des recherches en physique des particules au CERN, utilisait son temps libre pour étudier les problèmes fondamentaux de la mécanique quantique. Prenant en compte le fait que la mécanique bohmienne était non locale, il s'est posé la profonde question suivante :

« Serait-il possible de reproduire toutes les prédictions de la mécanique quantique avec une théorie des variables cachées « locale » comme le souhaitait Einstein ? »

Bell a sublimé ce problème, qui n'était qu'un débat philosophique, sous une forme expérimentalement vérifiable grâce à une formalisation mathématique rigoureuse. C'est le « théorème de Bell (Bell's Theorem) » et l'« inégalité de Bell », qui brillent de mille feux dans l'histoire des sciences.
Et en 1969, John Clauser, Michael Horne, Abner Shimony et Richard Holt (CHSH) ont dérivé une inégalité étendue vérifiable dans des expériences réelles, l'« inégalité CHSH ».

### Hypothèses du réalisme local et développement algébrique et intégral de l'inégalité CHSH

Supposons qu'Alice choisisse $a$ ou $a'$ comme paramètre de mesure, et que Bob choisisse $b$ ou $b'$.
Soit $\lambda$ la « variable cachée » basée sur le réalisme local, et $\rho(\lambda)$ sa fonction de densité de probabilité. Les probabilités étant normalisées,
$$ \int \rho(\lambda) d\lambda = 1 $$

Le résultat de mesure $A$ d'Alice est déterminé uniquement par sa direction de mesure $a$ et $\lambda$, et ne dépend pas de la direction de mesure $b$ de Bob (localité).
De même, le résultat de mesure $B$ de Bob n'est déterminé que par $b$ et $\lambda$ (localité). De plus, les résultats sont déterminés avant même d'être mesurés (réalisme). Puisque les résultats sont $+1$ ou $-1$,
$$ A(a, \lambda) = \pm 1, \quad B(b, \lambda) = \pm 1 $$
$$ A(a', \lambda) = \pm 1, \quad B(b', \lambda) = \pm 1 $$

La fonction de corrélation (valeur attendue) des résultats de mesure d'Alice et de Bob est obtenue en intégrant par rapport à la variable cachée $\lambda$.
$$ E(a, b) = \int A(a, \lambda) B(b, \lambda) \rho(\lambda) d\lambda $$

Ici, nous considérons la quantité $S(\lambda)$ suivante, qui est le cœur de l'inégalité CHSH.
$$ S(\lambda) = A(a, \lambda)B(b, \lambda) + A(a, \lambda)B(b', \lambda) + A(a', \lambda)B(b, \lambda) - A(a', \lambda)B(b', \lambda) $$

Nous factorisons cette équation par rapport aux résultats de mesure d'Alice.
$$ S(\lambda) = A(a, \lambda) \left[ B(b, \lambda) + B(b', \lambda) \right] + A(a', \lambda) \left[ B(b, \lambda) - B(b', \lambda) \right] $$

Ici intervient une étape logique extrêmement importante. $B(b, \lambda)$ et $B(b', \lambda)$ prennent tous deux toujours les valeurs $+1$ ou $-1$.
Par conséquent, en considérant leur somme et leur différence, il n'existe que les deux cas suivants.

- Cas 1 : Si $B(b, \lambda) = B(b', \lambda)$
  La somme est $B(b, \lambda) + B(b', \lambda) = \pm 2$, et la différence est $B(b, \lambda) - B(b', \lambda) = 0$.
- Cas 2 : Si $B(b, \lambda) = -B(b', \lambda)$
  La somme est $B(b, \lambda) + B(b', \lambda) = 0$, et la différence est $B(b, \lambda) - B(b', \lambda) = \pm 2$.

Dans les deux cas, l'une des deux crochets $\left[ \dots \right]$ sera toujours $\pm 2$, et l'autre sera toujours $0$.
Et $A(a, \lambda)$ ou $A(a', \lambda)$ multiplié par le $\pm 2$ survivant est également $\pm 1$.
Par conséquent, pour toute valeur de la variable cachée $\lambda$, ce qui suit est toujours algébriquement vrai.
$$ S(\lambda) = \pm 2 $$

C'est-à-dire, en prenant la valeur absolue,
$$ |S(\lambda)| = 2 $$

Pour trouver la valeur attendue $S$ de ce $S(\lambda)$, nous multiplions par la distribution de probabilité $\rho(\lambda)$ et intégrons sur tout l'espace.
$$ |S| = \left| \int S(\lambda) \rho(\lambda) d\lambda \right| \le \int |S(\lambda)| \rho(\lambda) d\lambda $$
En utilisant le fait que $|S(\lambda)| = 2$ et $\int \rho(\lambda) d\lambda = 1$,
$$ |S| \le \int 2 \rho(\lambda) d\lambda = 2 $$

Cette valeur attendue $S$ peut être développée comme la somme et la différence des fonctions de corrélation individuelles.
$$ S = E(a, b) + E(a, b') + E(a', b) - E(a', b') $$

Ainsi, l'« inégalité CHSH » suivante a été dérivée.
$$ |E(a, b) + E(a, b') + E(a', b) - E(a', b')| \le 2 $$

C'est la **limite qui ne peut absolument pas être dépassée** si l'univers obéit au « réalisme local ».

### Violation maximale en mécanique quantique (Borne de Tsirelson)

Rappelez-vous la prédiction de la mécanique quantique dérivée au chapitre 3, $E(\vec{a}, \vec{b}) = -\cos\theta$.
Supposons qu'Alice et Bob règlent leurs instruments de mesure aux angles suivants.
- $a = 0$
- $a' = \pi/2$
- $b = \pi/4$
- $b' = -\pi/4$

(*Notez que si l'on utilise la polarisation des photons, les coefficients sont différents du spin 1/2, et $E = \cos(2\theta)$, mais l'essence reste la même même en calculant avec les paramètres ci-dessus utilisant le spin.)
La différence d'angle entre chaque réglage est,
$|a - b| = \pi/4$
$|a - b'| = \pi/4$
$|a' - b| = \pi/4$
$|a' - b'| = 3\pi/4$

En remplaçant dans les prédictions de la mécanique quantique,
$E(a, b) = -\cos(\pi/4) = -1/\sqrt{2}$
$E(a, b') = -\cos(\pi/4) = -1/\sqrt{2}$
$E(a', b) = -\cos(\pi/4) = -1/\sqrt{2}$
$E(a', b') = -\cos(3\pi/4) = +1/\sqrt{2}$

En remplaçant ceux-ci dans le côté gauche $S$ de l'inégalité CHSH,
$$ S = \left( -\frac{1}{\sqrt{2}} \right) + \left( -\frac{1}{\sqrt{2}} \right) + \left( -\frac{1}{\sqrt{2}} \right) - \left( +\frac{1}{\sqrt{2}} \right) = -\frac{4}{\sqrt{2}} = -2\sqrt{2} $$
En prenant la valeur absolue, on obtient $|S| = 2\sqrt{2} \approx 2.828$.

Cela dépasse clairement la limite de $2$ du réalisme local ($2.828 > 2$). Cette valeur maximale atteignable par la mécanique quantique est appelée la **borne de Tsirelson (Tsirelson Bound)**. Une preuve mathématique rigoureuse a montré que le réalisme local est absolument incompatible avec les prédictions de la mécanique quantique.

---

## Chapitre 5 : L'intrication multipartite et le rejet en « un coup » (All-or-Nothing) du réalisme local

Le théorème de Bell était fondé sur une « inégalité » de corrélation statistique. Cependant, en 1989, Daniel Greenberger, Michael Horne et Anton Zeilinger ont montré qu'en considérant un état intriqué de trois particules (état GHZ), on pouvait complètement réfuter le réalisme local par la contradiction d'un seul résultat de mesure, sans recourir à des inégalités ou à des probabilités statistiques. C'est ce qu'on appelle la « preuve du Tout ou Rien (All-or-Nothing) » ou le « théorème GHZ ».

### Propriétés de l'état GHZ
L'état GHZ de trois particules de spin 1/2 est défini comme suit :
$$ |GHZ\rangle = \frac{1}{\sqrt{2}} \left( |\uparrow\uparrow\uparrow\rangle - |\downarrow\downarrow\downarrow\rangle \right) $$

Appliquons-y les produits d'opérateurs de Pauli suivants.
1. $X_1 Y_2 Y_3 = \sigma_x^{(1)} \otimes \sigma_y^{(2)} \otimes \sigma_y^{(3)}$
2. $Y_1 X_2 Y_3 = \sigma_y^{(1)} \otimes \sigma_x^{(2)} \otimes \sigma_y^{(3)}$
3. $Y_1 Y_2 X_3 = \sigma_y^{(1)} \otimes \sigma_y^{(2)} \otimes \sigma_x^{(3)}$
4. $X_1 X_2 X_3 = \sigma_x^{(1)} \otimes \sigma_x^{(2)} \otimes \sigma_x^{(3)}$

En utilisant $\sigma_x |\uparrow\rangle = |\downarrow\rangle, \sigma_x |\downarrow\rangle = |\uparrow\rangle$
et $\sigma_y |\uparrow\rangle = i|\downarrow\rangle, \sigma_y |\downarrow\rangle = -i|\uparrow\rangle$, si l'on applique $X_1 Y_2 Y_3$ à $|GHZ\rangle$,
$X_1 Y_2 Y_3 |\uparrow\uparrow\uparrow\rangle = |\downarrow\rangle (i|\downarrow\rangle) (i|\downarrow\rangle) = -|\downarrow\downarrow\downarrow\rangle$
$X_1 Y_2 Y_3 |\downarrow\downarrow\downarrow\rangle = |\uparrow\rangle (-i|\uparrow\rangle) (-i|\uparrow\rangle) = -|\uparrow\uparrow\uparrow\rangle$
Par conséquent,
$X_1 Y_2 Y_3 |GHZ\rangle = \frac{1}{\sqrt{2}} (-|\downarrow\downarrow\downarrow\rangle + |\uparrow\uparrow\uparrow\rangle) = |GHZ\rangle$
La valeur propre est $+1$. Par symétrie, les valeurs propres de $Y_1 X_2 Y_3$ et $Y_1 Y_2 X_3$ sont également $+1$.

D'autre part, en appliquant $X_1 X_2 X_3$,
$X_1 X_2 X_3 |\uparrow\uparrow\uparrow\rangle = |\downarrow\downarrow\downarrow\rangle$
$X_1 X_2 X_3 |\downarrow\downarrow\downarrow\rangle = |\uparrow\uparrow\uparrow\rangle$
Par conséquent,
$X_1 X_2 X_3 |GHZ\rangle = \frac{1}{\sqrt{2}} (|\downarrow\downarrow\downarrow\rangle - |\uparrow\uparrow\uparrow\rangle) = -|GHZ\rangle$
La valeur propre est $-1$. La mécanique quantique prédit ces résultats avec certitude (probabilité 1).

### Preuve algébrique de l'effondrement du réalisme local
Dans le réalisme local, on considère que les résultats de mesure sont déterminés par des variables cachées prédéterminées.
Soient $m_x^1, m_y^1 \in \{+1, -1\}$ les résultats de mesure des directions X et Y de la particule 1, respectivement. On définit de même pour les particules 2 et 3.
Le modèle du réalisme local doit satisfaire les 3 équations suivantes afin de s'accorder avec la prédiction $+1$ de la mécanique quantique.
1. $m_x^1 m_y^2 m_y^3 = +1$
2. $m_y^1 m_x^2 m_y^3 = +1$
3. $m_y^1 m_y^2 m_x^3 = +1$

Multiplions ces 3 équations ensemble.
$(m_x^1 m_y^2 m_y^3)(m_y^1 m_x^2 m_y^3)(m_y^1 m_y^2 m_x^3) = +1 \times +1 \times +1 = +1$
En simplifiant le côté gauche, chaque $m_y^i$ est multiplié deux fois, donc $(m_y^i)^2 = 1$.
$m_x^1 m_x^2 m_x^3 (m_y^1)^2 (m_y^2)^2 (m_y^3)^2 = m_x^1 m_x^2 m_x^3 = +1$

En d'autres termes, tant qu'on suit le réalisme local, le résultat de la mesure de $X_1 X_2 X_3$ doit toujours être $+1$.
Cependant, comme nous l'avons vu plus haut, la prédiction rigoureuse de la mécanique quantique (et les résultats expérimentaux réels) est $-1$.
$+1$ et $-1$. Sans même avoir besoin d'une inégalité statistique, le réalisme local et la mécanique quantique sont en contradiction décisive lors d'une seule mesure, ce qui prouve la justesse de la mécanique quantique.

(*À propos, pour l'intrication à trois particules, il existe également l'état W, $|W\rangle = \frac{1}{\sqrt{3}}(|100\rangle + |010\rangle + |001\rangle)$, qui possède des propriétés différentes de l'état GHZ, et qui a la robustesse que l'intrication ne soit pas complètement détruite même si une particule est perdue.)


---

## Chapitre 6 : Applications à la science de l'information quantique et développement rigoureux de la téléportation quantique

L'intrication est passée d'un objet de paradoxe à une « ressource d'information ». Un exemple représentatif est la « téléportation quantique ». Proposée en 1993 par Charles Bennett et al., elle a été démontrée expérimentalement pour la première fois en 1997 par le groupe d'Anton Zeilinger (lauréat du prix Nobel 2022).

### Développement mathématique du protocole de téléportation quantique

Supposons qu'Alice possède un état quantique inconnu $|\phi\rangle = \alpha|0\rangle + \beta|1\rangle$ et veuille le transférer à Bob qui est loin. ($|\alpha|^2 + |\beta|^2 = 1$)
Selon le théorème de non-clonage quantique (No-cloning theorem), cet état ne peut pas être copié et envoyé. De plus, si elle le mesure, l'état s'effondre, et il est impossible de connaître exactement les $\alpha$ et $\beta$ inconnus.

C'est pourquoi Alice et Bob partagent à l'avance une paire de particules intriquées (paire EPR), plus précisément l'état de Bell $|\Phi^+\rangle$ suivant.
$$ |\Phi^+\rangle_{AB} = \frac{1}{\sqrt{2}}(|0\rangle_A |0\rangle_B + |1\rangle_A |1\rangle_B) $$

Alice a la particule qu'elle veut transférer (disons la particule C) et l'une des particules de la paire EPR (particule A). Bob a l'autre particule de la paire EPR (particule B). L'état initial de tout le système est,
$$ |\psi_{total}\rangle = |\phi\rangle_C \otimes |\Phi^+\rangle_{AB} = (\alpha|0\rangle_C + \beta|1\rangle_C) \otimes \frac{1}{\sqrt{2}}(|0\rangle_A |0\rangle_B + |1\rangle_A |1\rangle_B) $$
En développant,
$$ \frac{1}{\sqrt{2}} \left( \alpha|000\rangle + \alpha|011\rangle + \beta|100\rangle + \beta|111\rangle \right) $$
(*Les indices sont dans l'ordre $C, A, B$)

Ici, Alice effectue une « mesure de Bell » sur les particules C et A qu'elle a sous la main. C'est une mesure qui projette les deux particules sur la base des quatre états de Bell suivants.
$|\Phi^\pm\rangle_{CA} = \frac{1}{\sqrt{2}}(|00\rangle \pm |11\rangle)$
$|\Psi^\pm\rangle_{CA} = \frac{1}{\sqrt{2}}(|01\rangle \pm |10\rangle)$

En utilisant ceux-ci pour recalculer $|00\rangle, |01\rangle, |10\rangle, |11\rangle$ et en refactorisant l'état du système global dans la base de Bell $|\cdot\rangle_{CA}$, on peut étonnamment le transformer comme suit.
$$ |\psi_{total}\rangle = \frac{1}{2} \left[ |\Phi^+\rangle_{CA}(\alpha|0\rangle_B + \beta|1\rangle_B) + |\Phi^-\rangle_{CA}(\alpha|0\rangle_B - \beta|1\rangle_B) + |\Psi^+\rangle_{CA}(\alpha|1\rangle_B + \beta|0\rangle_B) + |\Psi^-\rangle_{CA}(\alpha|1\rangle_B - \beta|0\rangle_B) \right] $$

Quand Alice effectue la mesure de Bell, le système s'effondre dans l'un de ces quatre termes avec une probabilité de 1/4.
1. Si Alice obtient $|\Phi^+\rangle$, l'état de Bob devient $\alpha|0\rangle + \beta|1\rangle = |\phi\rangle$, et le transfert est déjà complet (opération unitaire $I$).
2. Si elle obtient $|\Phi^-\rangle$, l'état de Bob est $\alpha|0\rangle - \beta|1\rangle$. Si Bob applique l'opérateur de Pauli $Z$ ($\sigma_z$), l'état redevient $|\phi\rangle$.
3. Si elle obtient $|\Psi^+\rangle$, l'état de Bob est $\alpha|1\rangle + \beta|0\rangle$. Si Bob applique l'opérateur de Pauli $X$ ($\sigma_x$), l'état redevient $|\phi\rangle$.
4. Si elle obtient $|\Psi^-\rangle$, l'état de Bob est $\alpha|1\rangle - \beta|0\rangle$. Bob applique d'abord $Z$ puis $X$ ($XZ$ ou $i\sigma_y$) pour retrouver $|\phi\rangle$.

Alice transmet le résultat de la mesure (2 bits d'information classique : 00, 01, 10, 11) à Bob par le biais de communications ordinaires (téléphone ou Internet). Comme cette communication ne dépasse pas la vitesse de la lumière, elle ne contredit pas la théorie de la relativité. Bob applique l'opérateur de Pauli approprié en fonction des 2 bits reçus, et restaure magnifiquement l'état quantique inconnu $|\phi\rangle$.
C'est le protocole complet de la téléportation quantique.

---

## Chapitre 7 : Quantification de l'intrication (Quantification)

L'intrication ne consiste pas seulement à dire si elle « existe » ou « n'existe pas », mais il est également possible de quantifier « à quel point elle est fortement intriquée ». Dans la théorie de l'information quantique, c'est un sujet de recherche extrêmement important.

### 1. Entropie d'intrication de von Neumann
L'entropie de von Neumann est la mesure standard pour évaluer le degré d'intrication dans un système bipartite $AB$ à l'état pur. Soit $\rho_{AB} = |\psi\rangle\langle\psi|$ la matrice densité du système entier ; on effectue la trace (réduction) sur le système B pour obtenir la matrice densité réduite $\rho_A = \text{Tr}_B(\rho_{AB})$ du système A.
Dans ce cas, l'entropie d'intrication $S$ est définie comme suit :
$$ S(\rho_A) = -\text{Tr}(\rho_A \log_2 \rho_A) $$
Dans un état d'intrication maximale tel qu'un état de Bell, $\rho_A$ est un état complètement mixte (proportionnel à la matrice identité), et prend $S = 1$ (valeur maximale). Intuitivement parlant, cela exprime l'essence de l'intrication : « Alors que l'état global est parfaitement connu, si l'on regarde uniquement la partie (système A), il n'y a aucune information (cela semble aléatoire). »

### 2. Concurrence
Comme mesure de l'intrication d'un système à 2 qubits, y compris les états mixtes, il y a la « concurrence $C(\rho)$ » conçue par William Wootters et al.
Pour la matrice densité $\rho$, on calcule l'état de spin inversé $\tilde{\rho} = (\sigma_y \otimes \sigma_y) \rho^* (\sigma_y \otimes \sigma_y)$ ($\rho^*$ étant le complexe conjugué).
Si les valeurs propres de la matrice $R = \sqrt{\sqrt{\rho} \tilde{\rho} \sqrt{\rho}}$ sont $\lambda_1, \lambda_2, \lambda_3, \lambda_4$ en ordre décroissant, la concurrence est définie comme suit :
$$ C(\rho) = \max(0, \lambda_1 - \lambda_2 - \lambda_3 - \lambda_4) $$
$C(\rho)$ prend une valeur allant de $0$ (pas d'intrication) à $1$ (intrication maximale), et possède la forte propriété mathématique que cette valeur peut être utilisée pour calculer directement une autre mesure appelée « intrication de formation » (Entanglement of Formation).

### 3. Négativité
La mesure basée sur le concept de transposition partielle (Partial Transpose) est la Négativité $\mathcal{N}(\rho)$.
Pour la matrice densité $\rho$ du système $AB$, soit $\rho^{T_B}$ celle transposée uniquement par rapport à la base du système B. Si $\rho$ est un état non intriqué (séparable), toutes les valeurs propres de $\rho^{T_B}$ seront non négatives (critère PPT de Peres-Horodecki).
Inversement, si des valeurs propres négatives existent, cela sert de preuve d'intrication. La Négativité est définie comme suit en utilisant la norme trace $||\cdot||_1$ de $\rho^{T_B}$ :
$$ \mathcal{N}(\rho) = \frac{||\rho^{T_B}||_1 - 1}{2} $$
Ceci est égal à la somme des valeurs absolues des valeurs propres négatives, et sa facilité de calcul en fait un indicateur extrêmement utile pour étudier l'intrication des systèmes de dimension supérieure ou à corps multiples.

---

## Chapitre 8 : Vérification expérimentale et fermeture complète des failles (Loophole)

La théorie est achevée et ses applications sont en vue. Ce qu'il reste à faire est d'interroger la nature en laboratoire pour savoir à laquelle des deux lois elle obéit réellement.

### L'expérience des commutateurs d'Alain Aspect (1982)
Après qu'Alice et Bob ont décidé de l'angle de leurs instruments de mesure, il faut exclure la possibilité que cette information se propage de l'autre côté à une vitesse inférieure ou égale à la vitesse de la lumière pour affecter les « variables cachées ». C'est ce qu'on appelle la « faille de la localité (Locality Loophole) ».
En France, Alain Aspect et al. ont réussi une expérience où le paramètre d'angle de l'instrument de mesure était modifié aléatoirement de manière ultrarapide, à l'aide d'appareils acousto-optiques, pendant que le photon volait de la source de lumière vers l'instrument de mesure. Ce faisant, ils ont créé une situation (séparation spatiale) où l'information ne peut être transmise, même par un signal se déplaçant à la vitesse de la lumière, et ont brillamment observé la violation de l'inégalité. L'« action fantôme à distance » d'Einstein était devenue réalité.

### Le défi ultime : une expérience parfaite sans faille (Loophole-free) (2015)
Même après l'expérience d'Aspect, il restait une très petite marge de contre-argumentation, comme la faible efficacité de détection (la « faille de détection / Fair-sampling Loophole » supposant que les photons qui ne pouvaient pas être mesurés possédaient des variables cachées opportunes).
Cependant, en 2015, de multiples groupes de recherche de l'Université de technologie de Delft aux Pays-Bas, de l'Université de Vienne en Autriche, et du NIST aux États-Unis, ont finalement réussi le test de Bell « Loophole-free » comblant simultanément toutes les failles majeures. Dans l'expérience de Delft, en intriquant des spins d'électrons dans les centres NV de diamants séparés de 1,3 km, la faille de la localité et la faille de détection ont été complètement scellées, enfonçant le dernier clou dans le cercueil du réalisme local.

---

## En guise de conclusion : La lumière apportée par la défaite d'Einstein

En 2022, le prix Nobel de physique a été décerné à Alain Aspect, John Clauser et Anton Zeilinger, les trois hommes qui ont définitivement établi les fondements de la mécanique quantique.

Einstein détestait la nature probabiliste et la non-localité de la mécanique quantique, et a écrit l'article EPR pour la critiquer. Mais ironiquement, ses critiques acerbes ont clairement mis en évidence le concept d'« intrication », et à travers le génie de Bell, ont conduit l'humanité à véritablement comprendre les connexions non locales de l'univers, ouvrant ainsi la voie à leur utilisation en tant que technologie.

La « dernière défaite » d'Einstein n'était en aucun cas une stagnation de la physique, mais plutôt la grande aube où l'humanité a acquis un tout nouveau langage universel appelé l'information quantique.

---
*Auteur : Rédacteur scientifique et technique de l'information quantique*
*Cet article est une explication académique couvrant depuis les fondations de la mécanique quantique jusqu'à la technologie de pointe de l'information quantique.*
