---
title: "La conjecture P ≠ NP : un problème ouvert en complexité"
slug: "Problème P=NP"
tags: ["Conjecture P≠NP", "Mathématiques", "Problèmes non résolus"]
draft: false
categories: ["math-cryptography-quantum"]
description: "Présentation de P, NP, des certificats de longueur polynomiale, de SAT et de la question ouverte P = NP ?"
image: eyecatch.jpg
date: 2024-09-11T02:22:39+09:00
lastmod: 2026-11-24
---
# Que sont P et NP ?

**P** est la classe des problèmes de décision résolubles en temps polynomial par rapport à la taille de l’entrée. **NP** est la classe des problèmes de décision pour lesquels chaque instance de réponse oui possède un certificat (une solution proposée) dont la longueur est bornée par un polynôme de la taille de l’entrée et dont la validité peut être vérifiée en temps polynomial. Toute solution trouvée pour un problème de P peut aussi être vérifiée en temps polynomial ; ainsi **P ⊆ NP**.

## SAT comme exemple

SAT demande s’il existe une affectation rendant vraie une formule booléenne donnée. Pour une instance positive, cette affectation sert de certificat : vérifier qu’elle satisfait chaque clause prend un temps polynomial en la taille de la formule. SAT, y compris 3-SAT, est NP-complet. Un algorithme polynomial pour SAT impliquerait donc **P = NP**. NP-complet signifie que tout problème de NP se réduit à ce problème en temps polynomial.

## La question ouverte

On ne sait toujours pas si **P = NP** ou **P ≠ NP**. Le Clay Mathematics Institute classe P vs. NP parmi les problèmes non résolus. P≠NP est une conjecture largement étudiée, et non un théorème démontré. En termes simples, la question est de savoir si tout problème dont une solution proposée se vérifie efficacement peut aussi être résolu efficacement.

## Références

- [Clay Mathematics Institute: P vs NP](https://www.claymath.org/millennium/p-vs-np/)
- [Stephen Cook, official problem description (PDF)](https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf)
- [MIT OpenCourseWare: NP-Completeness, Lecture 16 (PDF)](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/f2829e57caade7e7f21d765b8e7b9058_MIT6_046JS15_lec16.pdf)
