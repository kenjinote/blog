---
title: 'Salesforce : Commande pour supprimer toutes les publications et pièces jointes Chatter'
slug: "Salesforceチャッター全消しコマンド"
date: 2022-09-19T21:59:14+09:00
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.webp"
categories: ["Informatique et Technologie"]
description: 'Présente une commande pour supprimer en lot tous les messages Chatter, les pièces jointes et les données de la corbeille, utile lorsque la capacité de stockage de l''organisation est serrée dans Salesforce. Il s''agit d''une méthode pour nettoyer rapidement en utilisant la fenêtre d''exécution anonyme de la console du développeur.'
---
# Commande pour Tout Supprimer dans Salesforce Chatter
Ceci est une commande pour supprimer toutes les publications et pièces jointes dans Salesforce Chatter.
Ouvrez la Developer Console, sélectionnez "Open Execute Anonymous Window" dans le menu Debug, collez le code suivant et exécutez-le.
J'utilise personnellement cela lorsque la capacité de stockage de l'organisation s'épuise.

```
delete [select id from FeedItem];
delete [select id from FeedAttachment];
delete [select id from ContentDocument];

// Vider la corbeille
database.emptyRecycleBin([select id from ContentDocument where IsDeleted = true ALL ROWS]);
```
