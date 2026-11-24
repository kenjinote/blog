---
title: 'Comment créer un raccourci pour insérer la date actuelle dans IntelliJ IDEA'
slug: "IntelliJ IDEAでDateを貼り付けるCommandeを追加する"
date: 2022-09-04T05:59:04+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.webp"
categories: ["it-technology"]
description: 'Créez un modèle dynamique IntelliJ IDEA qui insère une date et une heure au format ISO 8601 avec le décalage du fuseau horaire local. Ce guide suit la documentation JetBrains actuelle pour l’expression et la touche d’expansion.'
---

# Introduction

Si vous saisissez souvent des horodatages, un modèle dynamique IntelliJ IDEA peut les insérer à partir d’une abréviation. Cet exemple crée un horodatage ISO 8601 avec l’heure locale et le décalage horaire de l’ordinateur.

## Créer le modèle dynamique

1. Ouvrez **Settings > Editor > Live Templates**. Sous Windows ou Linux, passez par **File > Settings** ; sous macOS, par **IntelliJ IDEA > Settings**.
2. Choisissez un groupe de modèles (par exemple **other**), puis cliquez sur **+ > Live Template**.
3. Saisissez `date` dans **Abbreviation** et ajoutez une courte **Description**.
4. Dans **Template text**, saisissez `$date$`.
5. Cliquez sur **Edit Variables**. Pour la variable `date`, saisissez `date("yyyy-MM-dd'T'HH:mm:ssXXX")` dans **Expression**. Activez **Skip if defined** pour calculer automatiquement la valeur à l’expansion.
6. Cliquez sur **Define** et sélectionnez les contextes où le modèle doit être disponible (choisissez **Everywhere** si nécessaire). Enregistrez les paramètres.

## Utiliser le modèle

Dans l’éditeur, saisissez `date` et appuyez sur la touche d’expansion par défaut, **Tab**. IntelliJ IDEA insère la date et l’heure système actuelles, par exemple `2026-11-24T09:30:00+09:00`. L’heure et le décalage dépendent du fuseau horaire actuel de l’ordinateur. Si vous avez modifié la touche d’expansion, vérifiez-la dans Live Templates.

Le motif `XXX` produit un décalage horaire ISO 8601. L’expression ne fixe pas `+09:00` : elle utilise le fuseau horaire local de chaque lecteur. Vérifiez que l’horodatage correspond bien à l’heure de publication souhaitée.

## Références

- [Créer et modifier des modèles dynamiques](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Variables de modèles dynamiques et fonction date](https://www.jetbrains.com/help/idea/template-variables.html)
- [Configurer la touche d’expansion](https://www.jetbrains.com/help/idea/settings-live-templates.html)
