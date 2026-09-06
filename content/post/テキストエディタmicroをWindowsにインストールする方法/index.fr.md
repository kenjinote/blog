---
title: "Comment installer l'éditeur de texte micro sur Windows"
slug: "comment-installer-l-editeur-de-texte-micro-sur-windows"
date: 2024-03-31T21:50:39+09:00
tags: ["micro", "éditeur de texte"]
draft: false
image: "img.png"
categories: ["Outils et environnement de développement"]
---

## Télécharger micro
https://github.com/zyedidia/micro/releases

Ouvrez le lien ci-dessus, cliquez sur `Show all XX assets` (où X est un nombre) et téléchargez `micro-X.X.XX-win64.zip` (où X est un nombre).
Décompressez le fichier zip et placez tous les fichiers dans un dossier de votre choix.

## Configurer les variables d'environnement
Pour utiliser `micro.exe` depuis l'Invite de commandes, vous devez configurer les variables d'environnement.

1. Appuyez sur la `Touche Win` + `Touche R`, tapez `sysdm.cpl` et appuyez sur `Entrée`.
2. Cliquez sur `Paramètres système avancés` dans les `Propriétés système`.
3. Cliquez sur `Variables d'environnement`.
4. Sélectionnez `Path` dans les `Variables système` et cliquez sur `Modifier`.
5. Cliquez sur `Nouveau` et ajoutez le chemin du dossier contenant `micro.exe`.
6. Cliquez sur `OK` pour fermer toutes les boîtes de dialogue.
7. Redémarrez l'Invite de commandes et tapez `nano` pour vérifier si vous pouvez l'exécuter.

## Comment utiliser micro

Lorsque vous tapez `micro` dans l'Invite de commandes et l'exécutez, l'écran suivant s'affiche.
![img_3.png](img_3.png)

Les principales opérations et les raccourcis clavier sont les suivants :

| Raccourci clavier | Opération | 
|--------|-----| 
| Ctrl+Q | Fermer le fichier | 
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
