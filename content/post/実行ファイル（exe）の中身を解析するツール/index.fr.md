---
title: "Outils pour analyser le contenu d'un fichier exécutable (exe)"
slug: "outils-pour-analyser-le-contenu-dun-fichier-executable-exe"
date: 2023-04-05T23:31:06+09:00
tags: ["windows", "exe", "fichier exécutable", "analyse"]
draft: false
image: "img_1.png"
categories: ["PC et Gadgets"]
---

# Qu'est-ce qu'un fichier exécutable (exe) ?

Un fichier exécutable sous Windows. Il est fondamentalement écrit dans un format appelé format PE.
Il contient le code machine pour l'exécution, ainsi que des ressources telles que des icônes et des images.

Il existe plusieurs outils pour analyser les fichiers exécutables, nous allons donc les présenter cette fois-ci.

## 7-Zip

![img.png](img.png)

Les fichiers EXE peuvent être volumineux, ils sont donc parfois compressés lors de leur création. Dans ce cas, en utilisant le logiciel de compression et d'extraction de fichiers 7-Zip, vous pouvez extraire le fichier exécutable et examiner son contenu. Un outil similaire permettant l'extraction est WinRAR.

## Resource Hacker
![img_2.png](img_2.png)

Vous pouvez extraire les ressources (icônes, bitmaps, boîtes de dialogue, chaînes de caractères, etc.) à l'intérieur d'un fichier EXE. Il fonctionne également comme un éditeur hexadécimal, ce qui vous permet de modifier et de réécrire le contenu du fichier EXE.

## PE Explorer
![img_3.png](img_3.png)

Vous pouvez analyser les fichiers PE pour Windows (EXE, DLL, OCX, SYS, pilotes). PE Explorer offre diverses fonctionnalités d'analyse, telles que l'affichage de la structure du fichier, de l'en-tête du fichier, des entrées de répertoire et des fonctions et symboles exportés.

## Dependency Walker
![img_4.png](img_4.png)

Vous pouvez vérifier les fichiers DLL dont dépend un fichier EXE et vous assurer qu'ils sont correctement chargés. Vous pouvez également suivre les appels de fonction des fichiers DLL.

## Ghidra

![img_5.png](img_5.png)

Il s'agit d'un puissant outil de rétro-ingénierie développé par la NSA (National Security Agency) et publié gratuitement en open source. Il est très populaire car il dispose non seulement d'une fonction de désassemblage des fichiers EXE (conversion en langage assembleur) mais aussi d'une fonction de décompilation vers un format proche du langage C.

## IDA Free / IDA Pro

![img_6.png](img_6.png)

Il s'agit d'un désassembleur et décompilateur très avancé qui est devenu une norme mondiale de l'industrie pour l'analyse de logiciels malveillants et la rétro-ingénierie. La version Pro est très chère, mais pour un usage personnel ou non commercial, vous pouvez utiliser gratuitement la version aux fonctionnalités limitées "IDA Free".

## x64dbg (x32dbg)

![img_7.png](img_7.png)

Il s'agit d'un débogueur open source pour Windows. Il est spécialisé dans "l'analyse dynamique", qui permet d'analyser le contenu et l'état de la mémoire étape par étape lors de l'exécution du fichier exécutable, et est souvent utilisé pour décoder des crackmes (programmes de défi pour l'analyse) ou enquêter sur le comportement de logiciels malveillants.

## ILSpy / dotPeek

![img_8.png](img_8.png)

Si le fichier EXE cible est créé avec un langage de la famille .NET tel que C#, l'utilisation de ces outils vous permet de le décompiler (rétro-compiler) à un état presque identique au code source d'origine pour en révéler tout le contenu.

Ces outils sont utiles pour examiner le contenu des fichiers EXE, mais la prudence est de mise. La modification de fichiers ou leur utilisation à des fins non autorisées peut entraîner des problèmes de droits d'auteur ou de sécurité, veillez donc à les utiliser avec une pleine compréhension.
