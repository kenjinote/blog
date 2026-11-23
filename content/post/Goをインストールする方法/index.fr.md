---
title: "Installer Go et exécuter votre premier programme"
slug: "GoをInstallationする方法"
date: 2022-09-10T00:48:17+09:00
lastmod: 2026-11-23
lastmod: 2026-11-23
lastmod: 2026-11-23
tags: ["Go", "Installation"]
draft: false
image: "images/cover.webp"
categories: ["programming"]
description: "Installez Go sous Windows, macOS ou Linux, vérifiez-le avec go version, créez un module et exécutez Hello World."
---

# À propos de Go

Go a été lancé chez Google et est désormais développé comme projet open source. C’est un langage compilé à typage statique. Go prend en charge les pointeurs, mais pas l’arithmétique des pointeurs ; son environnement d’exécution inclut un ramasse-miettes.

# Installer Go

Ouvrez le [guide officiel de téléchargement et d’installation](https://go.dev/doc/install), puis choisissez les instructions correspondant à votre système (Windows, macOS ou Linux) et à l’architecture du processeur. Suivez les étapes officielles, ouvrez un nouveau terminal et exécutez :

```sh
go version
```

Si la commande affiche une version, la commande `go` est disponible. Pour mettre Go à jour, suivez la procédure officielle de remplacement ; ne décompressez pas une nouvelle version par-dessus une installation existante. Consultez [Gérer les installations de Go](https://go.dev/doc/manage-install) pour gérer plusieurs versions.

# Exécuter Hello, World

Créez un dossier de travail et initialisez-y un module :

```sh
mkdir hello
cd hello
go mod init example/hello
```

Créez `hello.go` dans ce dossier et enregistrez le code suivant :

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

Exécutez le programme avec :

```sh
go run .
```

Le message `Hello, World!` s’affiche. Pour générer un exécutable, lancez `go build`. Son nom et son extension dépendent du système ; sous Windows, l’extension `.exe` est normalement utilisée.

# Pour aller plus loin

- [Tutoriel officiel Go : démarrer](https://go.dev/doc/tutorial/getting-started)
- [FAQ Go](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/) (pour essayer du code dans un navigateur)

Les ressources officielles d’initiation sont principalement disponibles en anglais.
