---
title: 'Le paradoxe de Saint-Pétersbourg : Combien paieriez-vous pour un jeu dont l''espérance de gain est « infinie » ?'
slug: 'st-petersburg-paradox'
description: 'Un jeu de hasard censé rapporter « à l''infini » mathématiquement. Pourtant, en réalité, personne n''est prêt à payer une somme importante pour y jouer. Cet article explique ce paradoxe historique, qui a mis en lumière l''écart entre la théorie des probabilités et la psychologie humaine (l''utilité) et qui est devenu le fondement de l''économie moderne.'
date: '2026-09-10T05:00:00+09:00'
image: 'img/st_petersburg.jpg'
math: true
mermaid: true
categories:
  - 'Paradoxes mathématiques'
  - 'Théorie des probabilités'
tags:
  - 'Paradoxe'
  - 'Espérance'
  - 'Économie'
  - 'Bernoulli'
---

## 1. Le jeu de rêve à l'espérance « infinie »

Alors que vous vous promenez dans un casino, un croupier vous invite à participer à un nouveau jeu de pile ou face :

**[Règles du jeu]**
1. Vous payez des frais de participation pour commencer le jeu.
2. Vous lancez une pièce. Si elle tombe sur **face**, vos gains sont doublés et vous pouvez lancer la pièce à nouveau.
3. Si elle tombe sur **pile**, le jeu s'arrête. Vous remportez alors les gains accumulés jusqu'à ce moment-là.

La cagnotte de départ est de 2 dollars.
- Si vous obtenez pile au 1er lancer, vous gagnez **2 dollars** et le jeu se termine.
- Si vous obtenez face au 1er lancer, puis pile au 2e, vous gagnez **4 dollars** et le jeu se termine.
- Si vous obtenez face au 1er, face au 2e, puis pile au 3e, vous gagnez **8 dollars** et le jeu se termine.
- ...Et ainsi de suite. Tant que vous obtenez face, les gains doublent indéfiniment : 16 $, 32 $, 64 $...

```mermaid
graph TD
    Start["Début du jeu"] --> Toss1{"1er lancer de pièce"}
    
    Toss1 -->|Pile (1/2)| End1["Fin : Gain de 2 dollars"]
    Toss1 -->|Face (1/2)| Toss2{"2e lancer de pièce"}
    
    Toss2 -->|Pile (1/2)| End2["Fin : Gain de 4 dollars"]
    Toss2 -->|Face (1/2)| Toss3{"3e lancer de pièce"}
    
    Toss3 -->|Pile (1/2)| End3["Fin : Gain de 8 dollars"]
    Toss3 -->|Face (1/2)| Toss4{"..."}
    
    Toss4 -.->|Tant que c'est Face| Infinite["Les gains doublent à l'infini !"]
```

Maintenant, voici une question pour vous.
**Si les frais de participation à ce jeu s'élevaient à "10 000 dollars", y participeriez-vous ?**

La plupart des gens répondraient probablement "non". En effet, il y a une chance sur deux que la pièce tombe sur pile dès le premier lancer, ce qui ne rapporterait que 2 dollars et entraînerait une perte énorme.

Cependant, si l'on s'en tient strictement à la théorie des probabilités (espérance mathématique), un fait étonnant apparaît : **Mathématiquement, que l'entrée coûte 10 000 ou 100 millions de dollars, vous devriez emprunter toute votre fortune pour participer à ce jeu.**

Pourquoi cela ?

---

## 2. Calculons l'espérance mathématique

Il existe un indicateur mathématique appelé **"espérance"** pour déterminer si un jeu de hasard est "rentable ou non".
L'espérance est une valeur qui représente "le gain moyen par partie si l'on répète le jeu de nombreuses fois". La formule consiste à **additionner tous les "(Gains potentiels) × (Probabilité associée)"**.

Calculons l'espérance de notre jeu.

- **Probabilité d'obtenir pile au 1er lancer :** $\frac{1}{2}$
  Le gain est de $2$ dollars.
  Contribution à l'espérance = $2 \times \frac{1}{2} = 1$ dollar

- **Probabilité d'obtenir pile au 2e lancer :** Obtenir face puis pile donne $\frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$
  Le gain est de $4$ dollars.
  Contribution à l'espérance = $4 \times \frac{1}{4} = 1$ dollar

- **Probabilité d'obtenir pile au 3e lancer :** Obtenir face, face, puis pile donne $(\frac{1}{2})^3 = \frac{1}{8}$
  Le gain est de $8$ dollars.
  Contribution à l'espérance = $8 \times \frac{1}{8} = 1$ dollar

- **Probabilité d'obtenir pile au $n$-ième lancer :** $(\frac{1}{2})^n$
  Le gain est de $2^n$ dollars.
  Contribution à l'espérance = $2^n \times (\frac{1}{2})^n = 1$ dollar

En d'autres termes, peu importe au bout de combien de lancers le jeu se termine, l'espérance de ce scénario est **toujours de "1 dollar"**.
Puisque le jeu peut continuer indéfiniment, l'addition de toutes ces espérances donne :

$$ \text{Espérance totale} = 1 + 1 + 1 + 1 + \dots = \infty \text{ (Infini)} $$

La réponse fournie par les mathématiques est que **"l'espérance de ce jeu est infinie"**.
Puisque l'espérance est infinie, quels que soient les frais de participation, il s'agit en théorie absolument d'un "pari gagnant".

C'est ce que l'on appelle le **"Paradoxe de Saint-Pétersbourg"**, formulé en 1713 par Nicolas Bernoulli.
Le résultat mathématique correct (d'une valeur infinie) entre en contradiction flagrante avec le sens commun humain (ne vouloir payer que quelques dollars).

---

## 3. La découverte de l'"utilité" pour réconcilier les mathématiques et la nature humaine

Celui qui a résolu ce paradoxe est le brillant mathématicien Daniel Bernoulli, le cousin de Nicolas. (Le paradoxe porte ce nom car il a présenté son article à l'Académie des sciences de Saint-Pétersbourg).

Daniel s'est intéressé à la psychologie humaine.
Il a estimé que **"les humains ne jugent pas les choses en fonction du 'montant absolu' d'argent, mais selon la 'satisfaction (l'utilité)' que cet argent apporte"**.

C'est ce qu'on appelle la **"loi de l'utilité marginale décroissante"**.

### La valeur de l'argent diminue selon la quantité possédée

Par exemple, si vous avez extrêmement soif dans un désert, le premier verre d'eau a une valeur (satisfaction) telle que vous seriez prêt à payer "10 000 dollars" pour le boire. Cependant, à mesure que vous buvez le 2e puis le 3e verre, la valeur d'un verre d'eau diminue progressivement. Au 10e verre, vous diriez sûrement : "Je n'en veux plus, même gratuit".

Il en va de même pour l'argent.
- Pour quelqu'un qui n'a pas d'économies, recevoir "1 million de dollars" a une valeur immense, capable de sauver une vie.
- En revanche, pour Elon Musk qui possède des milliards d'actifs, recevoir "1 million de dollars" n'a guère plus de valeur (satisfaction) qu'une petite pièce trouvée dans la rue.

En d'autres termes, même si la cagnotte augmente indéfiniment de 2 $ \rightarrow 4 $ \rightarrow 8 $ \rightarrow 16 $..., **la "joie (l'utilité)" ressentie par l'humain n'augmente pas à l'infini proportionnellement au montant**.

---

## 4. Recalcul de l'espérance en utilisant l'"utilité"

Daniel Bernoulli a fait l'hypothèse que "la valeur de l'argent (l'utilité) ressentie par un être humain est proportionnelle au logarithme ($\log$) du montant".

Si le montant est $x$, représentons la valeur (l'utilité) $u(x)$ ressentie par une personne par une fonction logarithmique (considérons ici un modèle simple en base 2).

- Utilité d'un gain de $2$ dollars : $\log_2(2) = 1$
- Utilité d'un gain de $4$ dollars : $\log_2(4) = 2$
- Utilité d'un gain de $8$ dollars : $\log_2(8) = 3$
- Utilité d'un gain de $2^n$ dollars : $\log_2(2^n) = n$

Le montant double à chaque fois, mais la "joie" humaine n'augmente que petit à petit : 1, 2, 3...
Utilisons cette "utilité" pour recalculer l'espérance (**l'utilité espérée**).

$$ \text{Utilité espérée} = \sum_{n=1}^{\infty} \left( n \times \left(\frac{1}{2}\right)^n \right) $$
$$ = 1 \cdot \frac{1}{2} + 2 \cdot \frac{1}{4} + 3 \cdot \frac{1}{8} + 4 \cdot \frac{1}{16} + \dots $$

Si l'on calcule la somme de cette série infinie, le résultat n'est pas "l'infini", mais **converge vers "2"**.
Si l'on calcule à rebours le montant correspondant à une utilité de "2", on obtient $2^2 = 4$ dollars.

En somme, en recalculant avec la psychologie humaine (l'utilité), on parvient à la réponse extrêmement rationnelle et réaliste que **"selon la perception humaine, la valeur de ce jeu est d'environ '4 dollars'"**.
C'est précisément pourquoi nous ne sommes pas disposés à payer 10 000 dollars pour jouer à ce jeu.

---

## 5. Conclusion : Un paradoxe qui a ouvert les portes de l'économie

Le paradoxe de Saint-Pétersbourg est un paradoxe révolutionnaire qui a mathématiquement prouvé l'incohérence entre un chiffre objectif comme le "montant" et une valeur subjective telle que la "satisfaction humaine".

Le concept d'"Utilité" proposé par Daniel Bernoulli est devenu, 200 ans plus tard, l'un des fondements les plus importants de la microéconomie moderne et de l'ingénierie financière (comme la théorie du portefeuille).
Nos comportements, tels que souscrire une assurance ou diversifier nos investissements, peuvent tous être expliqués par ce mécanisme psychologique d'"utilité marginale décroissante" (la souffrance d'une grosse perte est bien plus grande que la joie d'un gros gain).

Un simple problème de calcul sur un jeu de hasard a ainsi permis de déchiffrer l'esprit humain et de donner naissance à cette vaste discipline qu'est l'économie.
