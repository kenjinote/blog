---
title: "Comment fermer et redémarrer l'Explorateur"
slug: "エクスプローラーの終了・再起動方法"
date: 2024-03-30T15:40:24+09:00
tags: ["Explorateur"]
draft: false
image: "img_2.png"
categories: ["IT et Technologie"]
---

## Comment fermer depuis le menu du clic droit de la barre des tâches

Cette méthode fonctionne sous Windows 10. Il semble que le menu ne s'affiche pas sous Windows 11.
Si vous maintenez les touches `Shift` et `Ctrl` enfoncées et faites un clic droit sur la barre des tâches, `Quitter l'Explorateur` apparaîtra dans le menu.

![img.png](img.png)

## Comment fermer depuis le Gestionnaire des tâches

1. Appuyez sur les touches `Ctrl` + `Shift` + `Esc` pour ouvrir le Gestionnaire des tâches.
2. Sélectionnez `Détails`.

![img_3.png](img_3.png)

3. Sélectionnez `explorer.exe`, appuyez sur la touche `Suppr`, et lorsqu'on vous demande `Voulez-vous mettre fin à explorer.exe ?`, sélectionnez `Fin de tâche`.

![img_1.png](img_1.png)

## Comment fermer depuis l'Invite de commandes

1. Appuyez sur les touches `Win` + `R`, tapez `cmd`, et appuyez sur `Entrée`.
2. Tapez `taskkill /f /im explorer.exe`, et appuyez sur `Entrée`.

## Comment démarrer l'Explorateur depuis le Gestionnaire des tâches

1. Appuyez sur les touches `Ctrl` + `Shift` + `Esc` pour ouvrir le Gestionnaire des tâches.
2. Dans le menu Fichier, sélectionnez `Exécuter une nouvelle tâche`.
3. Tapez `explorer.exe`, et appuyez sur `Entrée`.
