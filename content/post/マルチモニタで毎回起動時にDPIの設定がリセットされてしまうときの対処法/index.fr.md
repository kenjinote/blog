---
title: "Windows 11 : vérifier le démarrage rapide si la mise à l’échelle change"

slug: "Multi-écransで毎回起動時にDPIの設定がリセットされてしまうときの対処法"
date: 2024-04-29T19:42:20+09:00
lastmod: "2026-11-24T00:00:00+09:00"

tags: ["Plusieurs moniteurs", "DPI", "Panneau de configuration"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Piste de dépannage prudente sous Windows 11 : désactiver temporairement le démarrage rapide, tester un arrêt puis un démarrage, et rétablir le réglage si cela ne change rien."
---
Le démarrage rapide enregistre la session du noyau et l’état des pilotes dans un fichier d’hibernation lors de l’arrêt afin d’accélérer le démarrage suivant. Le désactiver peut ralentir le démarrage. La documentation Microsoft ne l’identifie pas comme cause de réinitialisation de la mise à l’échelle multi-écrans ; utilisez ces étapes comme test temporaire, pas comme correctif confirmé.

## Modifier temporairement le réglage

1. Ouvrez le Panneau de configuration et choisissez **Options d’alimentation**.
2. Ouvrez **Choisir l’action des boutons d’alimentation**.
3. Cliquez sur **Modifier des paramètres actuellement non disponibles** (des droits d’administrateur peuvent être nécessaires).
4. Décochez **Activer le démarrage rapide (recommandé)**, puis cliquez sur **Enregistrer les modifications**.
5. Choisissez **Arrêter**, rallumez le PC et vérifiez si la mise à l’échelle est conservée. Le test doit suivre un arrêt puis une mise sous tension ; **Redémarrer** n’utilise pas le démarrage rapide.

Si cela ne change rien, réactivez l’option sur la même page. Les libellés peuvent varier selon la langue de Windows et ses mises à jour.

## Références Microsoft

- [Shut down, sleep, or hibernate your PC — Microsoft Support](https://support.microsoft.com/en-us/windows/experience/power-battery/shut-down-sleep-or-hibernate-your-pc)
- [System power states — Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/power/system-power-states)
- [Distinguishing Fast Startup from Wake-from-Hibernation — Microsoft Learn](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/distinguishing-fast-startup-from-wake-from-hibernation)
