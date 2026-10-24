---
title: "Séries de Taylor et de Maclaurin : La magie de l'approximation de fonctions complexes avec des polynômes"
description: "Une explication détaillée des séries de Taylor et de Maclaurin, les secrets du calcul infinitésimal, des significations intuitives aux dérivations mathématiques et applications en programmation et physique."
slug: "taylor-and-maclaurin-series"
date: "2026-09-20T14:30:00+09:00"
lastmod: 2026-10-24
image: "eyecatch.jpg"
categories: ["mathematics"]
tags:
  - "Calcul infinitésimal"
  - "Série de Taylor"
  - "Série de Maclaurin"
  - "Approximation de fonctions"
---

## Introduction

Un **polynôme de Taylor** approche une fonction au voisinage d'un point en y faisant coïncider sa valeur et un nombre fini de dérivées. La somme infinie construite à partir de ces coefficients est la **série de Taylor** ; lorsque le centre est zéro, on parle de **série de Maclaurin**. La convergence de la série et l'égalité de sa somme avec la fonction initiale doivent être vérifiées séparément.

À partir des fonctions exponentielle et trigonométriques, nous expliquerons comment déterminer les coefficients, sous quelles conditions les égalités sont valables et comment majorer l'erreur de troncature. Un exemple pédagogique en Python illustre ensuite l'approximation de $\sin x$ près de zéro.

## Pourquoi approximer des fonctions avec des polynômes ?

Pour commencer, pourquoi est-il nécessaire de représenter une fonction par un polynôme ( $a + bx + cx^2 + \dots$ ) ?

```mermaid
flowchart LR
    A["Fonction analytique près du centre"] -->|"Développement de Taylor dans son intervalle de convergence"| B["Série entière"]
    B -->|"Troncature à des termes finis"| C["Approximation polynomiale"]
    C -->|"Arithmétique de base uniquement"| D["Calcul informatique à grande vitesse"]
```

Approcher une fonction non linéaire par un polynôme peut simplifier son évaluation, sa dérivation et son intégration. Une fois ses coefficients fixés, un polynôme s'évalue par additions et multiplications. Le reste et les erreurs numériques permettent de déterminer le domaine d'utilisation et la précision de l'approximation.

## Compréhension intuitive de la série de Maclaurin

Considérons d'abord le **développement de Maclaurin**, qui approche une fonction près de $x=0$.
Supposons que $f$ possède les dérivées nécessaires au voisinage de zéro. Choisissons un degré fini $n$ et déterminons les coefficients du polynôme $P_n$ suivant :

$$ P_n(x) = c_0 + c_1 x + c_2 x^2 + \dots + c_n x^n $$

Les coefficients sont déterminés en égalant les valeurs et les dérivées en zéro. La condition sur la dérivée seconde ci-dessous s'applique pour $n\ge2$.

1. **Condition sur la valeur** : $P_n(0)=f(0)$ donne $c_0=f(0)$. Le terme constant assure l'égalité des valeurs en zéro.
2. **Condition sur la dérivée première** : $P_n'(0)=f'(0)$ donne $c_1=f'(0)$. Le polynôme $P_1(x)=f(0)+f'(0)x$ est l'approximation par la tangente en zéro.
3. **Condition sur la dérivée seconde** : On impose $P_n''(0)=f''(0)$. Comme $P_n''(0)=2c_2$, on obtient $c_2=f''(0)/2!$. En présence de termes de degré supérieur, la dérivée complète $P_n''(x)$ n'est généralement pas la constante $2c_2$.
4. **Condition générale** : Pour $k\le n$, imposer $P_n^{(k)}(0)=f^{(k)}(0)$ détermine $c_k=f^{(k)}(0)/k!$. Le reste présenté plus loin majore l'erreur au voisinage du centre.

## Formule et dérivation de la série de Maclaurin

Si $f$ est indéfiniment dérivable, ces coefficients définissent sa série de Maclaurin. Pour écrire une égalité avec $f(x)$ comme ci-dessous, la série doit cependant converger vers $f(x)$ au point considéré. C'est le cas dans un voisinage approprié de zéro lorsque $f$ y est analytique. Être indéfiniment dérivable ne suffit pas.

$$ f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f^{(3)}(0)}{3!}x^3 + \dots $$

Écrit en utilisant la notation sigma, cela ressemble à ceci :

$$ f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!} x^n $$

Ici, $f^{(n)}(0)$ est la valeur obtenue en dérivant la fonction $f(x)$ $n$ fois puis en évaluant la dérivée en zéro, et $n!$ représente la factorielle de $n$ ( $n \times (n-1) \times \dots \times 1$ ).

## Séries de Maclaurin des fonctions typiques

Les séries suivantes de l'exponentielle, du sinus et du cosinus convergent vers les fonctions correspondantes pour tout réel $x$. Les arguments trigonométriques sont exprimés en radians.

### 1. Fonction exponentielle $e^x$

La fonction exponentielle $f(x)=e^x$ reste $e^x$ après un nombre quelconque de dérivations. Toutes ses dérivées en zéro valent donc $1$ ($f^{(n)}(0)=1$).

$$ e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots = \sum_{n=0}^{\infty} \frac{x^n}{n!} $$

### 2. Fonctions trigonométriques $\sin x$ et $\cos x$

Les dérivées successives de $\sin x$ suivent le cycle $\cos x, -\sin x, -\cos x, \sin x, \dots$. En $x=0$, seules les dérivées d'ordre impair sont non nulles ; celles d'ordre pair valent $0$.

$$ \sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} x^{2n+1} $$

De même, pour $\cos x$, seuls les termes d'ordres pairs subsistent.

$$ \cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \dots = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n)!} x^{2n} $$

## Extension à la série de Taylor

Déplacer le centre de zéro vers $a$ donne la série de Taylor. Si $f$ est analytique près de $a$, l'égalité suivante est valable là où la série représente la fonction initiale. Les approximations ne supposant qu'un nombre fini de dérivées relèvent du polynôme de Taylor fini et de son reste, présentés plus loin.

$$ f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \dots = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x-a)^n $$

Cette formule démontre sa puissance lorsque vous souhaitez prédire la valeur d'une fonction à un endroit légèrement éloigné de $x=a$ ( $x = a + \Delta x$ ).

## Applications des séries de Taylor

### Approximation linéaire en physique

En physique, les approximations linéaires par des polynômes de Taylor sont fréquentes. Pour un pendule, exprimons l'angle $\theta$ en radians et supposons $|\theta|\ll1$. On utilise alors l'approximation du premier degré du sinus :

$$ \sin \theta \approx \theta \quad (\text{lorsque } \theta \text{ est suffisamment petit}) $$

Cette approximation linéarise l'équation du pendule et donne une période indépendante de l'amplitude dans le cadre de l'approximation des petites oscillations. La période réelle d'un pendule simple dépend de l'amplitude ; cette même approximation ne s'applique pas aux grandes oscillations.

### Programmation et calcul numérique

L'évaluation numérique des fonctions emploie diverses méthodes, dont les approximations polynomiales. Le module `math` de CPython fait principalement appel à la bibliothèque mathématique C de la plateforme ; les algorithmes dépendent de cette implémentation. L'exemple pédagogique suivant additionne quelques termes près de zéro, par exemple pour $|x|\le1$, et ne reproduit pas l'implémentation interne de la bibliothèque standard.

```python
import math

def approx_sin(x, terms=10):
    """
    Exemple pédagogique de somme finie de Maclaurin pour sin(x) près de zéro
    x : Angle en radians
    terms : Nombre de termes additionnés (entier positif ; 10 dans cet exemple)
    """
    result = 0.0
    for n in range(terms):
        # Calculer chaque terme : (-1)^n * x^(2n+1) / (2n+1)!
        sign = (-1) ** n
        numerator = x ** (2 * n + 1)
        denominator = math.factorial(2 * n + 1)
        result += sign * (numerator / denominator)
    return result

# Test : x = 1.0 radian (environ 57.3 degrés)
x_val = 1.0
print(f"Valeur approximative : {approx_sin(x_val)}")
print(f"Valeur de math.sin (pour comparaison) : {math.sin(x_val)}")
```

## Rayon de convergence et Théorème de Taylor

Le **rayon de convergence** $R$ est un nombre indiquant la distance au centre $a$ à l'intérieur de laquelle une série entière converge, $|x-a|<R$ ; ce n'est pas le nom de l'intervalle. Les cas $R=0$ et $R=\infty$ sont possibles. Les points frontières $|x-a|=R$ doivent être étudiés séparément. Par exemple, la série de Maclaurin de $\ln(1+x)$ a pour rayon 1 et vaut la fonction pour les réels $-1<x\le1$. Elle converge conditionnellement en $x=1$ et diverge en $x=-1$.

Pour une approximation finie, supposons que $f$ soit de classe $C^{n+1}$ sur l'intervalle reliant $a$ à $x$. Le théorème de Taylor donne :

$$
f(x)=P_{n,a}(x)+R_n(x),\qquad P_{n,a}(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k
$$

$$
R_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}
$$

Ici, $\xi$ se situe entre $a$ et $x$. Si $|f^{(n+1)}|\le M$ sur l'intervalle, alors $|R_n(x)|\le M|x-a|^{n+1}/(n+1)!$. Pour établir l'égalité entre une fonction et sa série de Taylor infinie, on peut vérifier que ce reste tend vers zéro lorsque $n\to\infty$.

Le code précédent additionne 10 termes, jusqu'à $x^{19}$. Le coefficient de degré 20 du sinus étant nul, le théorème de Taylor majore l'erreur de troncature en $x=1$ par $1/21!$, soit environ $1.96\times10^{-20}$. Cette borne concerne la somme finie calculée exactement dans les nombres réels ; les erreurs d'arrondi des calculs en virgule flottante de Python sont distinctes. La sortie de `math.sin` est elle aussi une valeur en virgule flottante servant de comparaison, et non la valeur mathématique exacte.

### Une fonction lisse qui n'est pas représentée par sa série de Taylor

$$
g(x)=\begin{cases}e^{-1/x},&x>0,\\0,&x\le0.\end{cases}
$$

Cette fonction est indéfiniment dérivable et toutes ses dérivées en zéro sont nulles. Sa série de Taylor en zéro est donc identiquement nulle et converge pour tout $x$. Mais pour $x>0$, on a $g(x)>0$ : la somme de la série ne coïncide pas avec la fonction initiale. Cet exemple distingue la convergence de la série de l'égalité de sa somme avec la fonction.

## Conclusion

Les polynômes de Taylor fournissent des approximations locales et les restes majorent leurs erreurs. Pour utiliser une série de Taylor comme une égalité, il faut vérifier son intervalle de convergence et l'égalité de sa somme avec la fonction initiale. Ces distinctions aident à déterminer la précision et le domaine d'application des approximations en physique et en calcul numérique.

## Références

- [NIST DLMF §1.4(vi) : Théorème de Taylor et restes pour une variable réelle](https://dlmf.nist.gov/1.4#vi)
- [MIT 18.100A : Basic Analysis §§4.3 et 5.4 (analyticité, régularité, série logarithmique et exemple non analytique)](https://ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/mit18_100af20_basic_analysis.pdf)
- [MIT 16.07 Lecture 24 : Approximation du pendule pour de petites amplitudes et dépendance en amplitude](https://ocw.mit.edu/courses/16-07-dynamics-fall-2009/c0c881f96f4ff4e21f082c88e8b015d6_MIT16_07F09_Lec24.pdf)
- [Python 3.12 math : Fonctions mathématiques et détails d'implémentation de CPython](https://docs.python.org/3.12/library/math.html)
