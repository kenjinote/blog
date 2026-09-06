---
title: "Obtenir uniquement la dernière version du dépôt git"
slug: "obtenir-uniquement-la-derniere-version-du-depot-git"
date: 2024-04-27T02:54:12+09:00
tags: ["git", "dépôt", "commande"]
draft: false
image: "img.png"
categories: ["Outils et environnement de développement"]
---

# Obtenir uniquement la dernière version du dépôt git

Vous pouvez obtenir uniquement la dernière version du dépôt avec la commande suivante.
C'est utile lorsque vous souhaitez obtenir le dépôt rapidement pour économiser de l'espace disque.

```
git clone --depth 1 <URL du dépôt>
```
