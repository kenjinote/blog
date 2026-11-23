---
title: 'Installation de la CLI Hugo et liste des commandes de base fréquemment utilisées'
slug: "HugoCommande一覧"
date: 2024-05-31T01:36:00+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["hugo", "commandes"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Nous présentons comment installer la CLI du générateur de site statique rapide Hugo et une liste des commandes de base fréquemment utilisées pour la gestion de blog. Nous expliquons les opérations que les débutants sur Hugo doivent retenir, telles que le lancement d''un nouveau site, la création d''articles, le démarrage d''un serveur local et la compilation.'
---

# Qu'est-ce que Hugo

Hugo est l'un des générateurs de sites statiques. Vous pouvez créer un site Web en convertissant des fichiers Markdown en HTML. Hugo est écrit en langage [Go](https://kenji.blog/fr/p/programming-languages-history-paradigm-evolution/) et fonctionne très rapidement.

Ce blog est également créé avec Hugo.

# Installation de la CLI Hugo

Pour installer la CLI Hugo, exécutez la commande ci-dessous.

※ Ceci est un exemple pour macOS. Pour les autres systèmes d'exploitation, veuillez vous référer à la documentation officielle.

```bash
brew install hugo
```

Vous pouvez l'installer en utilisant Homebrew.

# Liste des Commandes Hugo

Hugo propose diverses commandes. Les commandes fréquemment utilisées sont résumées ci-dessous.

## Créer un nouveau site

```bash
hugo new project <site-name>
```

Crée un nouveau site avec le nom indiqué.

## Créer un nouvel article

```bash
hugo new content posts/<post-name>.md
```

Crée un nouveau fichier de contenu au chemin indiqué.

## Démarrer le serveur

```bash
hugo server
```

Commande pour démarrer le serveur local. Il est accessible à l'adresse `http://localhost:1313`.

## Construire (Build)

```bash
hugo
```

Commande pour construire le site. Les fichiers HTML seront générés dans le répertoire `public`.

## Déployer

```bash
hugo deploy
```

Cette commande déploie le site vers les fournisseurs de stockage cloud pris en charge. Configurez une cible dans la section `deployment` et authentifiez-vous avec l’interface en ligne de commande du fournisseur. Ce n’est pas une commande générique pour tout hébergement web, comme GitHub Pages. Hugo v0.159.2 et les versions ultérieures nécessitent l’édition Deploy.

## Afficher la liste des articles

```bash
hugo list all
```

Affiche tout le contenu, y compris les brouillons, les contenus à date future et les contenus expirés.

## Vérifier la configuration

```bash
hugo config
```

Affiche les paramètres par défaut et ceux définis pour le site.

## Afficher l'aide

```bash
hugo help
```

Commande pour afficher l'aide.

## Afficher la version

```bash
hugo version
```

Affiche la version de Hugo et les informations sur l’environnement.


Ceci est la liste des commandes Hugo. Comme il existe de nombreuses autres commandes disponibles, veuillez vous référer à la documentation officielle.

# Référence
- [Créer un projet](https://gohugo.io/commands/hugo_new_project/)
- [Créer du contenu](https://gohugo.io/commands/hugo_new_content/)
- [Déployer](https://gohugo.io/commands/hugo_deploy/)
- [Lister tout le contenu](https://gohugo.io/commands/hugo_list_all/)
- [Installer sur macOS](https://gohugo.io/installation/macos/)
