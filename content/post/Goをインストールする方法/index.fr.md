---
title: "Comment installer Go"
slug: "comment-installer-go"
date: 2022-09-10T00:48:17+09:00
tags: ["Go", "Installation"]
draft: false
image: "images/cover.png"
categories: ["Programmation"]
---
# Introduction
Go est un langage de programmation relativement nouveau publié par Google en 2009.
Le compilateur, les outils et les bibliothèques de Go sont open source.
De plus, Go est un langage à typage statique comme C ou Java, mais il n'utilise pas de pointeurs comme le langage C.

# Méthode d'installation

[Installer Go](https://go.dev/dl/)

Les programmes d'installation pour chaque plateforme sont publiés sur le site ci-dessus.

Suivez les instructions à l'écran pour procéder à l'installation.
![img.png](images/img.png)

![img_1.png](images/img_1.png)

![img_2.png](images/img_2.png)

![img_3.png](images/img_3.png)

![img_5.png](images/img_5.png)

![img_6.png](images/img_6.png)

Installation terminée. Facile, n'est-ce pas ?

# Premier programme

Enregistrez le programme suivant sous le nom `hello.go`.

```go
package main

import "fmt"

func main() {
  fmt.Printf("Hello World\n")
}
```

En exécutant `go run hello.go` depuis l'invite de commande ou le terminal, `Hello, world!` s'affichera.

Pour compiler, l'exécution de `go build hello.go` générera `hello.exe`.
En exécutant `hello.exe`, `Hello, world!` s'affichera.

# Vous pouvez également exécuter du code sur une page web

[https://go.dev/play/](https://go.dev/play/)

![img_7.png](images/img_7.png)

# Documentation japonaise

[http://go.shibu.jp/](http://go.shibu.jp/)

Les explications nécessaires pour apprendre Go sont regroupées dans le lien ci-dessus (version traduite en japonais).
La technologie liée à Go est tellement ouverte et riche qu'il n'est presque pas nécessaire d'acheter des textes papier.

Alors, profitez bien de Go !
