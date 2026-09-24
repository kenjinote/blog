---
title: "Théorème Fondamental de l'Algèbre : Preuve qu'une Équation de Degré n a Toujours n Racines Complexes"
description: "Une explication détaillée de l'histoire, de la signification intuitive et de la belle preuve du théorème fondamental de l'algèbre à l'aide de l'analyse complexe (théorème de Liouville)."
slug: "fundamental-theorem-of-algebra"
date: "2026-09-24T16:08:36+09:00"
image: "eyecatch.jpg"
categories:
  - "Mathématiques"
tags:
  - "Algèbre"
  - "Analyse complexe"
  - "Preuve"
  - "Théorème"
---

## Introduction : La Quête d'Équations et de Racines

L'histoire des mathématiques est aussi l'histoire de la quête des nombres inconnus. Lorsque nous étudions les équations du second degré au collège, nous apprenons la formule quadratique. Cependant, si nous nous limitons au domaine des nombres réels, nous remarquons rapidement qu'il existe des équations "sans solution réelle". Par exemple, l'équation $x^2 + 1 = 0$ n'a pas de solution dans l'ensemble des nombres réels. En effet, le carré de n'importe quel nombre réel $x$ est toujours supérieur ou égal à $0$, et l'ajout de $1$ ne peut jamais donner $0$.

Pour résoudre ce problème, un nombre hypothétique dont le carré est $-1$ a été introduit, à savoir l'unité imaginaire $i$. Le système de nombres qui inclut cette unité s'appelle les nombres complexes. En introduisant les nombres complexes, les solutions de $x^2 + 1 = 0$ peuvent être trouvées sous la forme $x = \pm i$.

Ici, une grande question se pose : "Si nous étendons le système de nombres aux nombres complexes, pouvons-nous dire que toute équation aura toujours une solution ?" Ou bien, "Aurons-nous jamais besoin d'introduire encore un nouveau type de nombre ?"

Les mathématiques apportent une réponse très claire et magnifique à cette question. C'est le sujet de cet article : le **Théorème fondamental de l'algèbre**. Ce théorème affirme que "tout polynôme de degré $n$ à coefficients complexes a toujours une racine (solution) dans les nombres complexes". En d'autres termes, dans le vaste océan des nombres complexes, la solution de toute équation existe toujours, garantissant qu'il n'est plus nécessaire d'inventer de nouveaux nombres.

Dans cet article, nous expliquerons en détail ce **Théorème fondamental de l'algèbre**, en partant de son contexte historique, en passant par une approche intuitive basée sur la topologie, pour finalement présenter une preuve rigoureuse et magnifique utilisant l'analyse complexe.

## Contexte Historique du [Théorème Fondamental de l'Algèbre](https://kenji.blog/fr/p/fundamental-theorem-of-algebra/)

Le **Théorème fondamental de l'algèbre** n'a pas été prouvé du jour au lendemain. De nombreux grands mathématiciens ont lutté pour obtenir une preuve complète, sans jamais douter de la vérité du théorème.

Au 17ème siècle, des mathématiciens comme [René Descartes](https://kenji.blog/fr/p/descartes/) et Albert Girard savaient déjà empiriquement qu'une "équation de degré $n$ devrait avoir $n$ racines". Cependant, dans le cadre mathématique de l'époque, il n'y avait aucun moyen rigoureux de le prouver.

Au début du 18ème siècle, des géants des mathématiques comme Jean le Rond d'Alembert et [Leonhard Euler](https://kenji.blog/fr/p/euler/) ont tenté la preuve. D'Alembert a publié une preuve en 1746, et le théorème est parfois appelé "théorème de d'Alembert" en France ; cependant, selon les normes modernes, sa preuve manquait de rigueur topologique dans certains domaines. Euler a également essayé de montrer que tout polynôme à coefficients réels pouvait être factorisé en produit de polynômes linéaires et quadratiques, mais a laissé une lacune logique.

La première preuve essentiellement complète de ce théorème imprenable a été donnée par nul autre que [Carl Friedrich Gauss](https://kenji.blog/fr/p/gauss/). Dans sa thèse de doctorat de 1799, il a souligné les défauts des preuves des mathématiciens précédents et a présenté une preuve basée sur l'intuition géométrique. Gauss a fourni quatre preuves différentes pour ce théorème au cours de sa vie, indiquant l'importance qu'il y attachait.

La preuve la plus standard et la plus élégante aujourd'hui est considérée comme celle basée sur la théorie de l'analyse complexe, construite par le mathématicien français Joseph [Liouville](https://kenji.blog/fr/p/liouville/) et d'autres. Dans la seconde moitié de cet article, nous présenterons la preuve utilisant le théorème de [Liouville](https://kenji.blog/fr/p/liouville/).

## Énoncé Précis du Théorème

Tout d'abord, décrivons l'affirmation du théorème en termes mathématiquement précis.

**Théorème (Théorème fondamental de l'algèbre)**
Pour tout nombre entier naturel $n \ge 1$ et des coefficients complexes $a_0, a_1, \dots, a_n$ (où $a_n \neq 0$), un polynôme $P(z)$ est défini comme suit :

$$
P(z) = a_n z^n + a_{n-1} z^{n-1} + \dots + a_1 z + a_0
$$

Alors, l'équation $P(z) = 0$ a au moins une solution dans le plan complexe. C'est-à-dire qu'il existe un nombre complexe $\alpha$ tel que $P(\alpha) = 0$.

À première vue, il dit seulement "au moins une", mais en le combinant avec le théorème du reste des polynômes, nous pouvons facilement déduire l'affirmation plus forte selon laquelle "une équation de degré $n$ a exactement $n$ solutions complexes, en comptant les multiplicités". (Ce point sera expliqué en détail dans la section "Corollaire du théorème" ci-dessous.)

## Compréhension Intuitive : Approche Topologique

Avant de plonger dans la preuve rigoureuse, saisissons une image intuitive des raisons pour lesquelles ce théorème est vrai. Ici, nous introduisons une approche utilisant le concept d'"indice de lacet" (Winding number) issu de la topologie.

Représentons un point sur le plan complexe sous forme polaire par $z = R e^{i\theta}$. Ici, $R$ est la distance (rayon) par rapport à l'origine, et $\theta$ est l'angle.

Considérons le polynôme $P(z) = a_n z^n + a_{n-1} z^{n-1} + \dots + a_0$. Si $R$ est très grand, la valeur absolue de $z$ devient massive, et la valeur du polynôme est presque entièrement dominée par le terme de plus haut degré $a_n z^n$. C'est-à-dire que, lorsque $R$ est suffisamment grand, nous pouvons approcher $P(z) \approx a_n z^n$.

Maintenant, supposons que nous fassions parcourir à $z$ un cercle complet le long d'un cercle géant de rayon $R$. Au fur et à mesure que $\theta$ passe de $0$ à $2\pi$, l'angle de $z^n$ devient $n\theta$, passant de $0$ à $2n\pi$. Cela signifie que la trajectoire tracée par $P(z)$ devient une courbe fermée qui s'enroule autour de l'origine du plan complexe exactement $n$ fois.

Ensuite, imaginez le processus de réduction continue de ce rayon $R$. Au fur et à mesure que $R$ diminue progressivement, la courbe fermée tracée par $P(z)$ se déforme aussi de manière continue. Finalement, lorsque $R = 0$, la courbe se réduit à un seul point, $P(0) = a_0$.

La continuité est la clé ici. Une grande boucle qui s'enroulait initialement autour de l'origine $n$ fois se réduit finalement à un seul point qui ne contient pas l'origine. Topologiquement, il est impossible pour la boucle de se réduire de manière continue à un point éloigné de l'origine sans croiser l'origine. En d'autres termes, quelque part dans le processus de rétrécissement, cette courbe doit passer par l'origine ($0$).

Le moment où la courbe passe par l'origine, cela signifie exactement qu'il existe un $z$ tel que $P(z) = 0$. C'est la raison intuitive pour laquelle une solution doit toujours exister.

```mermaid
flowchart TD
    %% Aperçu de la cartographie des courbes
    A["Grand cercle de rayon R centré à l'origine"] -->|"Cartographie par le polynôme P("z")"| B["Courbe fermée sur le plan complexe"]
    B -->|"Lorsque R est suffisamment grand"| C["Courbe s'enroulant autour de l'origine n fois"]
    C -->|"Réduction continue de R à 0"| D["La courbe se réduit aussi continuellement vers l'origine"]
    D -->|"Continuité topologique"| E["Doit passer par l'origine en cours de route"]
    E -->|"P("z") = 0"| F["L'existence d'une racine est prouvée"]
```

## Préparation de l'Analyse Complexe : Théorème de [Liouville](https://kenji.blog/fr/p/liouville/)

Ayant acquis une compréhension intuitive, nous allons maintenant introduire la preuve la plus belle et la plus rigoureuse des mathématiques modernes. Cette preuve utilise une arme puissante de l'analyse complexe : le **Théorème de [Liouville](https://kenji.blog/fr/p/liouville/)**.

L'analyse complexe est le domaine qui traite du calcul infinitésimal des fonctions de variables complexes. Contrairement aux fonctions de nombres réels, la dérivabilité (holomorphie) des fonctions complexes est une condition extrêmement forte ; une fonction complexe qui est dérivable même une seule fois a la propriété étonnante d'être indéfiniment dérivable et capable d'être développée en une série de Taylor.

Une fonction qui est dérivable (holomorphe) sur tout le plan complexe s'appelle une **fonction entière**. Les polynômes $P(z)$ et la fonction exponentielle $e^z$ sont des exemples typiques de fonctions entières.

Le théorème de [Liouville](https://kenji.blog/fr/p/liouville/) est un théorème profondément puissant concernant ces fonctions entières.

**Théorème (Théorème de [Liouville](https://kenji.blog/fr/p/liouville/))**
Toute fonction entière bornée doit être une fonction constante.

Ici, "bornée" signifie que pour tous les nombres complexes $z$, la valeur absolue de la fonction $|f(z)|$ ne dépasse pas un certain nombre réel $M$ ; c'est-à-dire qu'il existe un $M$ tel que $|f(z)| \le M$.

Dans le monde des nombres réels, une fonction comme $f(x) = \sin(x)$ est dérivable sur toute la droite des nombres et est bornée par $-1 \le \sin(x) \le 1$. Ce n'est pas une fonction constante. Cependant, le théorème de [Liouville](https://kenji.blog/fr/p/liouville/) affirme que cela ne peut jamais se produire dans le monde complexe. Si une fonction est holomorphe sur tout le plan complexe et que sa valeur ne diverge pas vers l'infini, c'est simplement une constante plate.

## Preuve Rigoureuse du [Théorème Fondamental de l'Algèbre](https://kenji.blog/fr/p/fundamental-theorem-of-algebra/)

Prouvons maintenant le théorème fondamental de l'algèbre en utilisant le théorème de [Liouville](https://kenji.blog/fr/p/liouville/). Vous serez étonné par l'éclat de cette preuve. Ici, nous utilisons un raisonnement par l'absurde (preuve par contradiction).

**Preuve**

Supposons que pour tout polynôme $P(z) = a_n z^n + \dots + a_1 z + a_0$ de degré $n$ ($n \ge 1$) à coefficients complexes (où $a_n \neq 0$), l'équation $P(z) = 0$ n'a aucune solution sur le plan complexe.

C'est-à-dire, supposons que $P(z) \neq 0$ pour tous les nombres complexes $z$.

Ensuite, définissez une nouvelle fonction $f(z)$ comme suit :

$$
f(z) = \frac{1}{P(z)}
$$

Par notre hypothèse, le dénominateur $P(z)$ ne devient jamais $0$, donc cette fonction $f(z)$ n'a aucune singularité (points où le dénominateur est $0$) nulle part sur le plan complexe. Puisque le polynôme $P(z)$ est partout holomorphe (dérivable), son inverse est également holomorphe tant qu'il n'est pas égal à $0$. Par conséquent, $f(z)$ est une fonction holomorphe sur tout le plan complexe, c'est-à-dire une **fonction entière**.

Ensuite, nous examinons le comportement de $f(z)$ lorsque $|z|$ tend vers l'infini. En utilisant l'inégalité triangulaire, lorsque $|z|$ est suffisamment grand, l'ampleur de la valeur absolue du polynôme $P(z)$ est dominée par le terme de plus haut degré, divergeant ainsi vers l'infini.

Strictement parlant, lorsque $|z| \to \infty$,

$$
|P(z)| = |z|^n \left| a_n + \frac{a_{n-1}}{z} + \dots + \frac{a_0}{z^n} \right| \to \infty
$$

Le fait que la valeur absolue de $P(z)$ diverge vers l'infini signifie que la valeur absolue de son inverse $f(z) = 1/P(z)$ converge vers $0$.

C'est-à-dire,

$$
\lim_{|z| \to \infty} |f(z)| = 0
$$

Une limite de $0$ signifie qu'à l'extérieur d'un cercle d'un rayon $R$ suffisamment grand, la valeur peut être bornée, par exemple, $|f(z)| \le 1$.
D'autre part, à l'intérieur de la région du disque fermé (une région fermée bornée) incluant l'intérieur du cercle de rayon $R$, une fonction continue doit avoir une valeur maximale.
Par conséquent, à la fois à l'extérieur et à l'intérieur du cercle, la valeur absolue de $f(z)$ ne dépasse jamais une certaine limite supérieure finie. C'est-à-dire que $f(z)$ est une fonction **bornée**.

Jusqu'à ce stade, nous avons montré que $f(z)$ est à la fois une "fonction entière" et "bornée".
Ici, nous appliquons le **théorème de [Liouville](https://kenji.blog/fr/p/liouville/)**. Une fonction entière bornée doit être une constante. Par conséquent, il existe un nombre complexe $c$ tel que pour tout $z$,

$$
f(z) = c
$$

Cependant, puisque $\lim_{|z| \to \infty} f(z) = 0$, cette constante $c$ doit être $0$.
C'est-à-dire que $f(z) = 0$ pour tous les $z$.

Mais puisque $f(z) = \frac{1}{P(z)}$, il est impossible que la fonction fractionnaire soit égale à $0$ (car le numérateur est $1$). C'est une contradiction évidente.

Cette contradiction découle de notre hypothèse selon laquelle "$P(z) = 0$ n'a aucune solution sur le plan complexe".
Ainsi, par l'absurde, il est prouvé que $P(z) = 0$ a au moins une solution sur le plan complexe.

(Fin de la preuve)

## Corollaire du Théorème : Factorisation en Facteurs Linéaires

Le théorème fondamental de l'algèbre garantit l'existence d'"au moins une solution". En combinant ce fait avec le **Théorème de factorisation** pour la division polynomiale, nous pouvons prouver qu'un polynôme peut être complètement factorisé en un produit de termes linéaires.

Étant donné un polynôme de degré $n$ $P_n(z)$, le théorème fondamental de l'algèbre stipule qu'il existe une solution $\alpha_1$ telle que $P_n(\alpha_1) = 0$. Selon le théorème de factorisation, $P_n(z)$ a $(z - \alpha_1)$ comme facteur. C'est-à-dire qu'il peut être factorisé comme suit :

$$
P_n(z) = (z - \alpha_1) P_{n-1}(z)
$$

Ici, $P_{n-1}(z)$ est un polynôme de degré $n-1$. Si $n-1 \ge 1$, nous pouvons appliquer à nouveau le théorème fondamental de l'algèbre pour trouver une solution $\alpha_2$ pour $P_{n-1}(z)$. En répétant cela $n$ fois, nous pouvons le factoriser complètement comme suit :

$$
P_n(z) = a_n (z - \alpha_1)(z - \alpha_2) \dots (z - \alpha_n)
$$

De ce résultat, nous pouvons tirer la conclusion profondément belle et complète qu' **"une équation de degré $n$ à coefficients complexes a exactement $n$ solutions, en comptant les multiplicités"**. C'est pourquoi on l'appelle le "Théorème fondamental".

De plus, pour les polynômes dont tous les coefficients sont des nombres réels, si $\alpha$ est une solution, son conjugué complexe $\overline{\alpha}$ doit également être une solution. En utilisant cette propriété, nous pouvons également déduire le fait que "tout polynôme à coefficients réels peut être complètement factorisé en un produit de polynômes linéaires et quadratiques dans l'ensemble des nombres réels".

## Conclusion

Dans cet article, nous avons examiné en détail le théorème fondamental de l'algèbre, couvrant son contexte historique, son intuition topologique et sa preuve analytique complexe utilisant le théorème de [Liouville](https://kenji.blog/fr/p/liouville/).

À première vue, c'est un théorème sur les équations algébriques, mais le fait que sa preuve la plus élégante emprunte le pouvoir de l'analyse (calcul infinitésimal) et de la topologie démontre la profondeur des mathématiques et la beauté de la façon dont les différents domaines sont étroitement imbriqués.

La longue quête de l'humanité pour trouver les racines des équations a gagné la vaste scène du plan complexe grâce à l'introduction des nouveaux nombres imaginaires, et la complétude de cette scène a été prouvée par le théorème fondamental de l'algèbre. Ce théorème est devenu la clé qui a ouvert les portes brillantes menant à la théorie de [Galois](https://kenji.blog/fr/p/galois/) et à la géométrie algébrique, qui forment le socle des mathématiques modernes.
