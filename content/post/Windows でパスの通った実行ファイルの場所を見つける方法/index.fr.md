---
title: 'Comment trouver l''emplacement (chemin) d''un fichier exécutable accessible par le PATH sous Windows [Commande where]'
slug: "Windows でパスの通った実行ファイルの場所を見つける方法"
date: 2023-04-03T00:02:55+09:00
tags: ["Windows", "Chemin", "Fichier exécutable", "Invite de commandes"]
draft: false
image: "img.webp"
categories: ["PC・ガジェット"]
description: 'Nous expliquons comment trouver facilement l''emplacement de sauvegarde (chemin complet) d''un fichier exécutable à l''aide de l''invite de commande de Windows ou de PowerShell. Nous présentons une astuce pratique utilisant la commande ''where'' pour localiser rapidement l''emplacement exact d''une application dans le PATH.'
---

# Comment trouver l'emplacement d'un fichier exécutable dans le PATH sous Windows

Lorsque vous exécutez une commande en spécifiant un fichier exécutable, il peut arriver que vous souhaitiez savoir où ce fichier exécutable se trouve. Dans ce cas, vous pouvez trouver l'emplacement du fichier exécutable avec la commande suivante.

```powershell
where <nom_du_fichier_exécutable>
```

Par exemple, si vous souhaitez connaître l'emplacement de Paint (mspaint.exe), procédez comme suit :

```powershell
where mspaint.exe
```

# Références

- [How do I find the location of an executable in Windows?](https://superuser.com/questions/49104/how-do-i-find-the-location-of-an-executable-in-windows)
