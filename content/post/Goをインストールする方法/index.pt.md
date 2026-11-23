---
title: "Instalar Go e executar o primeiro programa"
slug: "GoをInstalaçãoする方法"
date: 2022-09-10T00:48:17+09:00
lastmod: 2026-11-23
lastmod: 2026-11-23
lastmod: 2026-11-23
tags: ["Go", "Instalação"]
draft: false
image: "images/cover.webp"
categories: ["programming"]
description: "Instale Go no Windows, macOS ou Linux, confira com go version, crie um módulo e execute Hello World."
---

# Sobre Go

Go começou como um projeto do Google e hoje é desenvolvido como um projeto de código aberto. É uma linguagem compilada e estaticamente tipada. Go oferece ponteiros, mas não aritmética de ponteiros; seu ambiente de execução inclui um coletor de lixo.

# Instalar Go

Abra o [guia oficial de download e instalação](https://go.dev/doc/install) e escolha as instruções para seu sistema operacional (Windows, macOS ou Linux) e arquitetura de CPU. Siga os passos oficiais, abra um novo terminal e execute:

```sh
go version
```

Se o comando mostrar uma versão, o comando `go` está disponível. Ao atualizar o Go, siga as instruções oficiais para substituir a instalação anterior; não extraia uma versão nova sobre uma instalação existente. Consulte [Gerenciar instalações do Go](https://go.dev/doc/manage-install) para administrar versões.

# Executar Hello, World

Crie uma pasta de trabalho e inicialize um módulo dentro dela:

```sh
mkdir hello
cd hello
go mod init example/hello
```

Crie `hello.go` nessa pasta e salve o código:

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

Execute o programa com:

```sh
go run .
```

Será exibido `Hello, World!`. Para gerar um executável, rode `go build`. O nome e a extensão dependem do sistema operacional; no Windows, normalmente é usado `.exe`.

# Continue aprendendo

- [Tutorial oficial do Go: primeiros passos](https://go.dev/doc/tutorial/getting-started)
- [Perguntas frequentes do Go](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/) (experimente código no navegador)

Os materiais oficiais introdutórios estão disponíveis principalmente em inglês.
