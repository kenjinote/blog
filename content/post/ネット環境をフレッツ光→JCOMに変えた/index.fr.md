---
title: "J'ai changé mon environnement internet de Flet's Hikari vers J:COM"
slug: "ネット環境をフレッツ光→JCOMに変えた"
date: 2022-09-05T22:48:51+09:00
tags: ["J:COM","Flet's Hikari","Ligne internet"]
draft: false
image: "jcom.png"
categories: ["IT・Technologie"]
---

# Changement de l'environnement internet de la maison de Flet's Hikari vers J:COM

![](flets_hikari.png)

![](jcom.png)

Sur la recommandation d'une connaissance, j'ai changé la ligne internet de ma maison de Flet's Hikari vers J:COM. Les raisons sont,

1. Les frais mensuels sont moins chers. 3 619 yens → 2 180 yens
2. La vitesse d'internet passe de 100MBps à 320MBps

Ce sont ces points.

# Impressions après utilisation
Cela fait environ une semaine depuis le changement, et pour le moment il n'y a presque aucun problème. Je note ci-dessous quelques points qui m'ont interpellé.

En changeant réellement, j'ai remarqué que la vitesse de téléchargement est effectivement devenue plus rapide, passant de 60MBps à un peu moins de 320MBps. Cependant,
en ce qui concerne la vitesse d'envoi, elle est tombée à environ 10MBps, alors qu'elle était de 40MBps à l'époque de Flet's Hikari. Il semble que ce soit une spécification du côté de J:COM.
Pour le moment, comme je ne fais pas de streaming ou de téléchargement de grandes quantités de données, je vais voir comment cela évolue.

De plus, ces derniers temps, ma famille et moi faisons principalement du télétravail, et aujourd'hui, pour la première fois, internet a été coupé pendant quelques dizaines de minutes. Il s'est rétabli automatiquement, mais
ce n'est peut-être pas bon signe. Cela ne fait même pas une semaine depuis le changement...

Pour information, comme J:COM restreint les communications P2P, il semble que la vitesse des applications P2P soit faible. Ceux qui utilisent le P2P devraient être prudents.

# À propos du service
Lors de la signature du contrat, si l'on s'abonne à Netflix ou Disney+, on reçoit une carte QUO de 40 000 yens, ce qui compense les frais d'abonnement à chaque service et rend les frais mensuels
légèrement moins chers en moyenne, j'ai donc souscrit au service en même temps que le contrat. Netflix a un contrat d'un an, Disney+ un contrat de six mois, et il semble qu'il faille procéder soi-même aux démarches de résiliation.

Comme le changement est encore récent, si de nouvelles impressions ou ressentis sur l'utilisation apparaissent, je mettrai à nouveau l'article à jour. À bientôt,

# 09/06 Difficultés de connexion à internet
- 06/09/2022 vers 13:13 environ 3 à 5 minutes
- 06/09/2022 vers 13:30 environ 3 à 5 minutes
- Plusieurs fois par la suite...

![Diagnostic réseau](trouble_shooting.png)

Comme il semble que le problème vienne du DNS, j'ai configuré le serveur DNS en me référant à [ici](https://internet.watch.impress.co.jp/docs/column/shimizu/1367271.html).
On verra ce que cela donne... Même avec la configuration DNS, je n'arrivais pas à me connecter, alors j'ai contacté le support qui m'a dit qu'une maintenance d'urgence était en cours... L'état de la connexion s'est amélioré juste après ma demande, je pense donc qu'ils ont pris des mesures.
