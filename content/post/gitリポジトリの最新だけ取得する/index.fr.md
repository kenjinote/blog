---
title: 'Comment récupérer uniquement le dernier commit d''un dépôt avec Git clone'
slug: "obtenir-uniquement-la-derniere-version-du-depot-git"
date: 2024-04-27T02:54:12+09:00
tags: ["git", "dépôt", "commande"]
draft: false
image: "img.webp"
categories: ["Outils et environnement de développement"]
description: 'Nous expliquons comment récupérer uniquement le dernier commit (clone superficiel) sans télécharger tout l''historique d''un dépôt Git. Il s''agit d''une technique pratique pour économiser de l''espace disque et cloner rapidement un dépôt à l''aide de l''option « --depth 1 ».'
---

# Obtenir uniquement la dernière version du dépôt git

Vous pouvez obtenir uniquement la dernière version du dépôt avec la commande suivante.
C'est utile lorsque vous souhaitez obtenir le dépôt rapidement pour économiser de l'espace disque.

```
git clone --depth 1 <URL du dépôt>
```
