---
title: "Connexion à Distance Facile avec TeamViewer"
slug: "Connexion à Distance Facile avec TeamViewer"
date: 2023-01-13T01:45:00+09:00
tags: ["TeamViewer", "Commande", "Connexion à Distance"]
draft: false
image: "img.png"
categories: ["Informatique・Technologie"]
---

# Connexion à Distance Facile avec TeamViewer

L'utilisation de TeamViewer permet d'établir facilement une connexion de bureau à distance.

Démarrez TeamViewer sur la destination et la source distantes,
entrez l'ID et le mot de passe de la destination sur la source pour vous connecter à distance.

Pour vous connecter à distance via la ligne de commande, procédez comme suit:

```
%ProgramFiles%\TeamViewer\TeamViewer.exe -i <ID> -P <Password>
```
Entrez l'ID de la destination dans `<ID>` et le mot de passe de la destination dans `<Password>`.

Il est pratique de créer un fichier de raccourci avec la commande ci-dessus, car cela permet d'omettre la saisie de l'ID/PW.

Site de référence : [Command line parameters](https://community.teamviewer.com/English/kb/articles/34447-command-line-parameters)
