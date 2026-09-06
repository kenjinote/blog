---
title: "Liste des Commandes Hugo"
slug: "Hugoコマンド一覧"
date: 2024-05-31T01:36:00+09:00
tags: ["hugo", "commandes"]
draft: false
image: "img.png"
categories: ["Opération de Blog"]
---

# Qu'est-ce que Hugo

Hugo est l'un des générateurs de sites statiques. Vous pouvez créer un site Web en convertissant des fichiers Markdown en HTML. Hugo est écrit en langage Go et fonctionne très rapidement.

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
hugo new site <nom-du-site>
```

Commande pour créer un nouveau site. Dans `<nom-du-site>`, spécifiez le nom du site.

## Créer un nouvel article

```bash
hugo new <nom-de-l'article>.md
```

Commande pour créer un nouvel article. Dans `<nom-de-l'article>`, spécifiez le nom de l'article.

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

Commande pour déployer le site. Les paramètres de destination du déploiement sont configurés dans le fichier `config.toml`.

## Afficher la liste des articles

```bash
hugo list all
```

Commande pour afficher la liste des articles.

## Vérifier la configuration

```bash
hugo config
```

Commande pour vérifier la configuration.

## Afficher l'aide

```bash
hugo help
```

Commande pour afficher l'aide.

## Afficher la version

```bash
hugo version
```

Commande pour afficher la version.

Ceci est la liste des commandes Hugo. Comme il existe de nombreuses autres commandes disponibles, veuillez vous référer à la documentation officielle.

# Référence
- [Documentation Officielle Hugo](https://gohugo.io/documentation/)
