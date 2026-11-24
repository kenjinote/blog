---
title: 'Comment ajouter la fonction grep de Hidemaru Editor au menu du clic droit dans Windows'
date: 2024-04-03T00:00:46+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Explorateur de fichiersのMenu du clic droitにÉditeur Hidemarugrepを追加する"
tags: ["Hidemaru Editor", "Explorateur", "Menu contextuel", "grep", "Registre"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Nous présentons une procédure de configuration pratique pour ajouter la fonction grep de Hidemaru Editor au menu du clic droit de l''Explorateur de fichiers sous Windows 10/11. Nous expliquons clairement une méthode simple utilisant un fichier d''enregistrement de registre.'
---
Voici comment ajouter le grep de Hidemaru Editor au menu contextuel (clic droit) de l'Explorateur sous Windows 10/11.

 **Avertissement : La procédure suivante modifie le registre. Veuillez le faire à vos propres risques.**

Ce fichier ajoute des commandes de dossier pour l’utilisateur actuel uniquement ; il n’ajoute pas « Ouvrir avec Hidemaru » à tous les fichiers et ne modifie pas toute la machine. Avant l’importation, ouvrez-le dans le Bloc-notes et vérifiez ou corrigez le chemin de l’exécutable. Si les clés existent déjà, exportez-les dans l’Éditeur du Registre (Fichier > Exporter). Sous Windows 11, les commandes héritées peuvent se trouver sous « Afficher plus d’options ». La prise en charge de Windows 10 a pris fin le 14 octobre 2025. Le fichier de suppression fourni ne retire que ces entrées de l’utilisateur actuel ; il n’annule pas une ancienne inscription système. Si vous avez importé l’ancien fichier, vérifiez et supprimez ses clés séparément dans l’Éditeur du Registre.
## Procédure

1. Ouvrez le lien ci-dessous et enregistrez-le dans n'importe quel dossier.

[秀丸レジストリ登録.reg](秀丸レジストリ登録.reg)

[Supprimer les entrées Hidemaru du registre](秀丸レジストリ解除.reg)

2. Double-cliquez sur le fichier `秀丸レジストリ登録.reg` pour l'ajouter au registre.

## Référence

- [秀丸grepをフォルダの右クリックメニューから行う](https://aimek-developer.blogspot.com/2019/02/grep.html)

## Références officielles

- [Hidemaru startup options](https://help.maruo.co.jp/hidemaru/html/230_Option.html)
- [Microsoft: Back up and restore the registry](https://support.microsoft.com/en-us/windows/experience/backup-recovery/how-to-back-up-and-restore-the-registry-in-windows)
- [Microsoft: File Explorer context menu](https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows)
- [Microsoft: Windows 10 end of support](https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025)
- [Microsoft: reg import](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-import)
