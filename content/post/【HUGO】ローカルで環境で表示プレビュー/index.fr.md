---
title: "Installer Hugo sous Windows et prévisualiser le site en local"
slug: "【HUGO】ローカルで環境で表示プレビュー"
tags: ["HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Installez Hugo sous Windows, configurez PATH si nécessaire et prévisualisez un site local avec ses brouillons à l'aide des commandes actuelles."
date: "2022-09-05T12:28:01+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Installer Hugo sous Windows et prévisualiser un site en local

> **Mis à jour le 24 novembre 2026.** L'article précédent dépendait de la sortie de Hugo 0.102.3 et de procédures Windows datant de 2022. Cette version suit la documentation officielle actuelle pour Windows et la CLI. Hugo, les fenêtres Windows et les paquets peuvent évoluer ; référez-vous aux guides officiels liés si l'écran diffère.

## Installer Hugo

Sous Windows 10 ou version ultérieure, WinGet est une option simple. Ouvrez un nouveau terminal après l'installation, puis exécutez la commande ci-dessous. Sinon, téléchargez dans les versions officielles l'archive correspondant à votre version de Windows et à l'architecture du processeur, extrayez-la et placez `hugo.exe` dans un dossier. Ajoutez à PATH le dossier contenant l'exécutable, pas le fichier lui-même.

Pour modifier PATH manuellement, recherchez dans le menu Démarrer « Modifier les variables d'environnement de votre compte », puis ajoutez par exemple `C:/Hugo/bin` à la variable utilisateur `Path`. Ouvrez ensuite un nouveau terminal.

## Installer Hugo

```powershell
winget install -e --id Hugo.Hugo
hugo version
```

```powershell
hugo server --buildDrafts
```

## Prévisualiser en local

Lancez le serveur depuis la racine du projet Hugo, où se trouve le fichier ou dossier de configuration. `--buildDrafts` inclut les brouillons dans l'aperçu. N'utilisez pas une sortie contenant des brouillons pour une publication en production. Ouvrez dans le navigateur l'URL affichée par Hugo. Par défaut, il s'agit de `http://localhost:1313/` ; vérifiez la sortie si le port est déjà utilisé. Appuyez sur Ctrl+C dans le terminal pour arrêter le serveur.

## Références officielles

- [Installation sous Windows](https://gohugo.io/installation/windows/)
- [Utilisation de base et brouillons](https://gohugo.io/getting-started/usage/)
- [Commande hugo server](https://gohugo.io/commands/hugo_server/)
