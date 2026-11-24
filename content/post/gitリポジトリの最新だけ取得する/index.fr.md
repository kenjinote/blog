---
title: 'Cloner un dépôt Git avec un historique superficiel'
slug: "gitDépôtの最新だけ取得する"
date: 2024-04-27T02:54:12+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "dépôt", "commande"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Découvrez ce que transfère git clone --depth 1, comment choisir une branche et récupérer davantage d’historique.'
---

# Cloner un dépôt avec un historique superficiel

`git clone --depth 1` crée un clone superficiel dont la profondeur d’historique est de un à partir de la tête de la branche sélectionnée. Par défaut, il s’agit de la branche par défaut du dépôt distant. Cela réduit l’historique des commits transféré, mais Git télécharge toujours les fichiers actuels et les objets nécessaires : un dépôt contenant de gros fichiers peut donc rester volumineux.

```sh
git clone --depth 1 <repository-url>
```

Pour choisir une branche, indiquez son nom :

```sh
git clone --depth 1 --single-branch --branch <branch> <repository-url>
```

Vous pouvez récupérer davantage d’historique ensuite, par exemple :

```sh
git -C <directory> fetch --deepen=50 origin <branch>
```

Remplacez `<directory>` et `<branch>` par les noms utilisés. Avec `--depth`, Git implique aussi `--single-branch`, sauf indication contraire. Consultez les manuels officiels de [`git clone`](https://git-scm.com/docs/git-clone) et [`git fetch`](https://git-scm.com/docs/git-fetch), notamment pour `--unshallow`.
