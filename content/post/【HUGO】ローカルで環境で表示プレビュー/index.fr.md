---
title: "【HUGO】Aperçu de l'affichage dans l'environnement local"
slug: "【HUGO】Aperçu de l'affichage dans l'environnement local"
date: 2022-09-05T12:28:01+09:00
tags: ["HUGO"]
draft: false
image: "img.png"
categories: ["Opération de blog"]
---
# Installation de HUGO

## Téléchargement
[Téléchargement de HUGO](https://github.com/gohugoio/hugo/releases)

À partir du site ci-dessus, téléchargez et extrayez le module Windows adapté à votre environnement.
Dans mon cas, j'ai téléchargé "hugo_0.102.3_Windows-64bit.zip".

## Extraction
Extrayez le fichier zip téléchargé, et copiez le fichier hugo.exe qui s'y trouve dans un dossier que vous avez créé, par exemple C:\bin.

## Enregistrer dans les variables d'environnement
Enregistrez-le dans les variables d'environnement pour pouvoir exécuter hugo.exe de n'importe où.
Les opérations ci-dessous concernent Windows 11, mais vous devriez pouvoir l'enregistrer avec une procédure similaire :

1. Appuyez sur Win+Pause pour ouvrir les informations de version
2. Cliquez sur Paramètres système avancés
3. Cliquez sur Variables d'environnement
4. Sélectionnez Path et cliquez sur Modifier
5. Cliquez sur Nouveau, entrez "C:\bin" sur une nouvelle ligne, puis cliquez sur OK pour fermer la boîte de dialogue
 
# Prévisualiser le blog
Dans l'invite de commandes, accédez au dossier du blog HUGO et exécutez la commande ci-dessous.

`hugo server -D`

Le résultat de l'exécution est ci-dessous. (-D est une option pour afficher les articles en brouillon.)

```
C:\Users\win11\IdeaProjects\kenji.blog>hugo server -D
Start building sites …
hugo v0.102.3-b76146b129d7caa52417f8e914fc5b9271bf56fc windows/amd64 BuildDate=2022-09-01T10:16:19Z VendorInfo=gohugoio

                   | JA
-------------------+-----
  Pages            | 39
  Paginator pages  |  0
  Non-page files   |  7
  Static files     |  0
  Processed images |  0
  Aliases          | 13
  Sitemaps         |  1
  Cleaned          |  0

Built in 161 ms
Watching for changes in C:\Users\win11\IdeaProjects\kenji.blog\{archetypes,content,themes}
Watching for config changes in C:\Users\win11\IdeaProjects\kenji.blog\config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

Puisque l'adresse est affichée lors de l'exécution (dans l'exemple ci-dessus, `http://localhost:1313/`), copiez cette adresse dans votre navigateur.
L'aperçu est mis à jour automatiquement à chaque fois que le fichier est enregistré.
Pour terminer l'aperçu, tapez Ctrl+C dans l'invite de commandes.
