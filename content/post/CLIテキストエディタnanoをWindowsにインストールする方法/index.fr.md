---
title: "Comment installer l'éditeur de texte CLI nano sur Windows"
slug: "CLIテキストエディタnanoをWindowsにインストールする方法"
date: 2024-03-31T18:09:32+09:00
tags: ["nano", "éditeur de texte"]
draft: false
image: "img_1.png"
categories: ["Outils et environnement de développement"]
---

## Télécharger nano.exe
https://sourceforge.net/projects/nano-for-windows/

Ouvrez le lien ci-dessus, cliquez sur `Download` et téléchargez `GNU-Nano_Win32(static).zip`.
Extrayez le fichier zip et placez `nano.exe` dans n'importe quel dossier.
* La saisie en japonais n'est pas prise en charge (au 31/03/2024).

## Configurer les variables d'environnement
Pour utiliser `nano.exe` à partir de l'invite de commande, vous devez configurer les variables d'environnement.

1. Appuyez sur la `Touche Win` + `Touche R`, tapez `sysdm.cpl` et appuyez sur `Entrée`.
2. Cliquez sur `Paramètres système avancés` dans la fenêtre Propriétés système.
3. Cliquez sur `Variables d'environnement`.
4. Sélectionnez `Path` sous `Variables système` et cliquez sur `Modifier`.
5. Cliquez sur `Nouveau` et ajoutez le chemin vers `nano.exe`.
6. Cliquez sur `OK` pour fermer toutes les boîtes de dialogue.
7. Redémarrez l'invite de commande, tapez `nano` et vérifiez s'il s'exécute.

## Comment utiliser nano

Lorsque vous tapez `nano` et l'exécutez, l'écran suivant s'affiche.

![img_2.png](img_2.png)

Les descriptions des raccourcis sont affichées au bas de l'écran.

La signification des symboles est la suivante :

- `^` représente la touche `Ctrl`.
- `M-` représente la touche `Alt`.

Pour enregistrer et fermer, appuyez sur `Ctrl` + `S`, puis sur `Ctrl` + `X`.

## Référence
- [GNU nano](https://www.nano-editor.org/)
