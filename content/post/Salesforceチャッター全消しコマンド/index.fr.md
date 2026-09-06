---
title: "Commande pour Tout Supprimer dans Salesforce Chatter"
slug: "Salesforceチャッター全消しコマンド"
date: 2022-09-19T21:59:14+09:00
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.png"
categories: ["Informatique et Technologie"]
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
