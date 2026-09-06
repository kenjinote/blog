---
title: "L'histoire secrète du développement de LogicPad"
slug: "LogicPad 開発秘話"
date: 2025-07-30T23:51:35+09:00
tags: ["LogicPad", "Développement", "Histoire secrète"]
draft: false
image: "img.png"
categories: ["Informatique et technologie"]
---

# Un outil pour "ceux qui ne peuvent pas coder, mais qui ont de la logique". La raison pour laquelle j'ai créé LogicPad

Bonjour, je suis kenji. Je suis le créateur de l'outil low-code " [LogicPad](https://logicpad.org) ".
Cette fois, il ne s'agit pas d'une présentation du produit, mais je voudrais écrire sur les coulisses du développement, "Pourquoi ai-je décidé de créer cela ?", et sur mes propres pensées d'un point de vue un peu personnel.

Honnêtement, ce n'était pas seulement le développement d'un outil.
Mon passé, les frustrations au travail, mes compétences et le désir ardent de "créer un jour mon propre produit" —
LogicPad est né du résultat de la convergence de toutes ces choses.

En d'autres termes, **c'est aussi le "projet d'une vie"** pour moi.
Je vais écrire ce contexte aussi honnêtement et passionnément que possible.

---

## Je voulais un produit pour lequel je pourrais dire fièrement "C'est moi qui l'ai fait"

Pour être honnête, c'était ma première motivation.

Depuis toujours, j'ai aimé écrire du code, que ce soit pour le travail ou comme passe-temps. J'ai également été impliqué dans divers développements.
Mais, un jour, j'ai soudainement réalisé.
**"Je n'ai aucun produit que j'ai lancé dans le monde sous mon nom, sous ma responsabilité."** 

Bien sûr, il y a de la valeur dans ce que nous créons en équipe, et il y a eu beaucoup de travaux dont je suis fier.
Mais quelque part, il y avait aussi un sentiment de vide, "Vais-je terminer ma carrière sous le nom de quelqu'un d'autre comme ça ?".

Juste une fois suffirait.
**Je veux laisser quelque chose dont je puisse dire fièrement, "C'est moi qui l'ai fait".** 
C'est dans cet esprit que j'ai commencé à concevoir LogicPad. C'était il y a environ 6 ans (vers 2019).
(L'idée originale elle-même remonte à 2015 environ, lorsque j'ai découvert Blueprint, le langage de programmation visuelle d'Unreal Engine.)

![Blueprint](img_1.png)
---

## Je ne peux pas m'y mettre car je ne sais pas coder. N'est-ce pas dommage ?

Il y avait beaucoup de personnes excellentes sur mon lieu de travail.

Elles peuvent construire de la logique. Elles maîtrisent les fonctions Excel et peuvent voir l'essence du problème.
Mais — à l'étape "écrire du code", leurs mains s'arrêtent.

"Je fais cette tâche à chaque fois en regardant le manuel de procédure, mais n'y a-t-il pas moyen de l'automatiser ?"
"Oui, c'est possible. Mais... pour cela, il faut écrire du code..."

Nous avons eu de telles conversations à maintes reprises.

À chaque fois, je pensais :
**"C'est un tel gâchis de s'arrêter au mur du code alors qu'on comprend la logique."** 

---

## L'option d'un éditeur low-code

En fait, dans mon emploi précédent, je développais un logiciel de CAO 2D fonctionnant via une interface graphique (GUI).
Avec la CAO, vous utilisez la souris pour assembler des formes, n'est-ce pas ?
En d'autres termes, c'est un monde où **"la logique est construite par l'opération"** .

J'ai pensé : "C'est très compatible avec le low-code".

En remontant encore plus loin, depuis mon époque étudiante, j'ai toujours écrit du code et produit en masse de petits programmes dès qu'une idée me venait, comme le traitement d'images, le traitement numérique, des outils Windows et des outils de publication automatique sur les réseaux sociaux.
Je pense qu'il y en a plus de 600. Ils sont toujours sur mon GitHub aujourd'hui.

À l'époque, je ne pensais pas à la signification.
C'était juste "Je le fais parce que j'ai envie de le faire". C'était tout.

Mais maintenant, en créant LogicPad...

**J'ai eu l'impression que les points s'étaient enfin rejoints.** 

---

## Facile à utiliser, mais puissant. La difficulté de l'équilibre

Ce à quoi je pensais constamment en faisant avancer le développement, c'était
**"En faire un outil intuitif à utiliser, mais en même temps robuste."** 

Si vous ajoutez des fonctions, vous pouvez faire plus de choses. Mais cela devient plus difficile à utiliser.
Si vous simplifiez, n'importe qui peut l'utiliser. Mais il y aura alors des personnes qui ne seront pas satisfaites.

Pour qu'on ne dise pas : "Les outils low-code ne sont que des jouets, n'est-ce pas ?".
Mais je ne veux pas non plus qu'on dise : "En fin de compte, ça ne sert à rien si on ne code pas."

**Je me battais constamment sur la ligne de démarcation entre l'intuition et l'expressivité.** 

J'ai reconstruit l'interface utilisateur à maintes reprises, je l'ai jetée à maintes reprises,
Et quand je me suis enfin approché d'une forme où je me suis dit "Ça va le faire", j'étais vraiment heureux.

---

## J'ai été sauvé par les mots de ma première "utilisatrice"

La première fois que j'ai donné LogicPad, c'était à une ancienne collègue.
Elle n'est pas douée en informatique, et elle a peur du code. Mais elle est douée pour la logique.

Après lui avoir expliqué un peu et l'avoir laissée manipuler... Je ne peux pas oublier la phrase qu'elle a dite quelques minutes plus tard.

> **"Avec ça, je pense que même moi, je pourrais le faire !"** 

À ce moment-là, j'ai failli pleurer.
C'est ce que je voulais lui offrir.

Non pas un outil qui fonctionne, mais **le sentiment de "Je l'ai créé moi-même !"** .
J'étais convaincu que c'était là la véritable valeur de LogicPad.

---

## Quand le nombre de créateurs augmente, la société devient bien plus intéressante

Je pense que la "démocratisation de la technologie" est vraiment importante.

La technologie a le pouvoir de changer le monde.
Mais le nombre de personnes qui peuvent la manipuler est limité.

Et si on pouvait créer une application simplement "en comprenant la logique" ?

**Davantage de personnes pourraient passer du "côté de la création".** 
Et je pense que ce qui naîtra de là dépassera notre imagination actuelle.

Si LogicPad pouvait devenir cette porte d'entrée.
Je veux que ce soit un outil qui transforme le "je veux créer" en "je peux créer".

C'est mon souhait.

---

## En conclusion

LogicPad est encore en version bêta et n'est pas terminé.
Il y a encore des tonnes d'améliorations à apporter et de choses que je veux faire.

Mais, je mets **tous les "points" de ma vie dans cet outil.** 
Maintenant, je peux dire avec fierté :

**"C'est le produit que j'ai créé."** 

---

### 👇 Bonus : Ce que vous pouvez faire avec LogicPad

* Construir des processus par glisser-déposer
* Les branchements conditionnels et les variables peuvent également être gérés dans l'interface graphique
* Divers nœuds de collaboration IA sont disponibles
* L'extension pour les utilisateurs avancés est également possible grâce à l'insertion de scripts
* Fonctions mathématiques et traitement de données de haute précision (calculs numériques avec une précision infinie, etc.)
* Une multitude de raccourcis clavier pour les utilisateurs avancés
* Prend en charge les langues de plus de 90 pays

---

### Ce que je veux faire à l'avenir

* Générer de la logique à partir du langage naturel en collaboration avec l'IA
* Un système qui permet aux utilisateurs de créer des nœuds personnalisés
* Construire une plateforme où les nœuds et la logique créés peuvent être partagés

---

## ✍️ Postface

Merci beaucoup d'avoir lu jusqu'ici.
Ce n'était pas seulement le développement d'un outil, mais un défi dans lequel j'ai mis ma propre expérience, ma passion et des fragments de ma vie.

"Je ne sais pas coder, mais j'ai de la logique."
Un avenir où ces personnes pourront **"créer"** par elles-mêmes.
C'est ce que je veux continuer à viser à travers LogicPad.

Je serais très heureux si vous pensiez, ne serait-ce qu'un peu, "J'ai envie de l'utiliser".
Si vous êtes intéressé, n'hésitez pas à essayer [LogicPad](https://logicpad.org).

Et si vous avez des impressions ou des remarques après l'avoir utilisé, même les plus petites, n'hésitez pas.
Votre voix sera une force majeure pour façonner la prochaine étape de ce produit.

Merci pour votre soutien continu.
