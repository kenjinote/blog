---
title: 'Utilisable sur Windows ! Comment installer l''éditeur de texte léger ''micro'''
slug: "Éditeur de textemicroをWindowsにInstallationする方法"
date: "2024-03-31T21:50:39+09:00"
lastmod: "2026-11-25"
tags: ["micro", "éditeur de texte"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Nous expliquons de manière simple la procédure pour installer l''éditeur de texte pour terminal ''micro'', qui fonctionne confortablement dans l''invite de commande, sur Windows, et comment configurer les variables d''environnement pour pouvoir l''utiliser.'
---

## Télécharger micro
https://github.com/micro-editor/micro/releases/latest
Dans Assets de la dernière version, téléchargez l’archive Windows x64 (par exemple, `micro-<version>-win64.zip`) et extrayez-la dans le dossier de votre choix.

Pour Windows sur ARM, choisissez plutôt l’archive ARM64 correspondante.

## Configurer les variables d'environnement
Pour utiliser `micro.exe` depuis l'Invite de commandes, vous devez configurer les variables d'environnement.

1. Appuyez sur `Win` + `R`, saisissez `sysdm.cpl`, puis appuyez sur `Entrée`.
2. Ouvrez l’onglet Paramètres système avancés et cliquez sur Variables d’environnement.
3. Dans Variables utilisateur pour votre compte, sélectionnez `Path` et cliquez sur Modifier. Créez `Path` s’il n’existe pas.
4. Cliquez sur Nouveau et ajoutez le chemin du dossier contenant `micro.exe`.
5. Cliquez sur OK pour fermer les boîtes de dialogue.
6. Rouvrez l’Invite de commandes et exécutez `micro` pour vérifier qu’il démarre.

## Comment utiliser micro

Lorsque vous tapez `micro` dans l'Invite de commandes et l'exécutez, l'écran suivant s'affiche.
![img_3.png](img_3.webp)

Les principales opérations et les raccourcis clavier sont les suivants :

| Raccourci clavier | Opération | 
|--------|-----| 
| Ctrl+Q | Fermer le fichier actuel (micro se ferme s’il s’agit du dernier fichier) |
| Ctrl+S | Enregistrer le fichier | 
| Ctrl+O | Ouvrir un fichier | 
| Ctrl+A | Tout sélectionner | 
| Ctrl+X | Couper la sélection | 
| Ctrl+C | Copier la sélection | 
| Ctrl+V | Coller | 
| Ctrl+Z | Annuler | 
| Ctrl+Y | Rétablir | 
| Ctrl+E | Exécuter la commande de l'éditeur | 

## Référence
- [micro](https://micro-editor.github.io/)
- [Default key bindings](https://github.com/micro-editor/micro/blob/master/runtime/help/defaultkeys.md)
