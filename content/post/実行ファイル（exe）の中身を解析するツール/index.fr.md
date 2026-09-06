---
title: "Outils pour analyser le contenu d'un fichier exécutable (exe)"
slug: "outils-pour-analyser-le-contenu-dun-fichier-executable-exe"
date: 2023-04-05T23:31:06+09:00
tags: ["windows", "exe", "fichier exécutable", "analyse"]
draft: false
image: "img_1.png"
categories: ["PC & Gadgets"]
---

# Qu'est-ce qu'un fichier exécutable (exe) ?

Un fichier exécutable sous Windows. Il est écrit essentiellement dans ce qu'on appelle le format PE.
Il contient du code en langage machine pour l'exécution, ainsi que des ressources telles que des icônes et des images.

Il existe plusieurs outils pour analyser les fichiers exécutables, et nous vous les présentons cette fois-ci.

## 7-Zip

![img.png](img.png)

Les fichiers EXE sont parfois créés en compressant des fichiers car ils ont tendance à devenir volumineux à l'état brut. Dans ce cas, en utilisant le logiciel de compression et d'extraction de fichiers 7-Zip, vous pouvez extraire le fichier exécutable et examiner son contenu. WinRAR est un autre outil capable d'extraire de la même manière.

## Resource Hacker
![img_2.png](img_2.png)

Vous permet d'extraire des ressources (icônes, bitmaps, boîtes de dialogue, chaînes de caractères, etc.) situées dans les fichiers EXE. Il fonctionne également comme un éditeur hexadécimal, ce qui vous permet de modifier et de réécrire le contenu des fichiers EXE.

## PE Explorer
![img_3.png](img_3.png)

Peut analyser les fichiers PE pour Windows (EXE, DLL, OCX, SYS, pilotes). PE Explorer offre diverses fonctions d'analyse, telles que l'affichage de la structure du fichier, de l'en-tête du fichier, des entrées de répertoire, ainsi que des fonctions et symboles exportés.

## Dependency Walker
![img_4.png](img_4.png)

Vous pouvez vérifier les fichiers DLL dont dépend un fichier EXE et confirmer s'ils sont chargés correctement. Il vous permet également de suivre les appels de fonctions des fichiers DLL.

Bien que ces outils soient utiles pour examiner le contenu des fichiers EXE, la prudence est de mise. La modification de fichiers ou leur utilisation à des fins non autorisées peut entraîner des problèmes de sécurité ou de violation du droit d'auteur, alors assurez-vous de bien comprendre cela avant de les utiliser.
