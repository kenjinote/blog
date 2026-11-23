---


title: "Instalar Go y ejecutar tu primer programa"
slug: "GoをInstalaciónする方法"
date: 2022-09-10T00:48:17+09:00
lastmod: 2026-11-23
lastmod: 2026-11-23
lastmod: 2026-11-23
tags: ["Go","Instalación"]
draft: false
image: "images/cover.webp"
categories: ["programming"]
description: "Instala Go en Windows, macOS o Linux, comprueba la instalación con go version, crea un módulo y ejecuta Hello World."
---

# Acerca de Go

Go nació como un proyecto de Google y hoy se desarrolla como proyecto de código abierto. Es un lenguaje compilado y de tipado estático. Go admite punteros, pero no aritmética de punteros; su entorno de ejecución incluye un recolector de basura.

# Instalar Go

Abre la [guía oficial de descarga e instalación](https://go.dev/doc/install) y elige las instrucciones para tu sistema operativo (Windows, macOS o Linux) y arquitectura de CPU. Sigue los pasos oficiales y abre una terminal nueva para ejecutar:

```sh
go version
```

Si el comando muestra una versión, `go` está disponible. Al actualizar Go, sigue las instrucciones oficiales para sustituir la instalación anterior; no descomprimas una versión nueva encima de una instalación existente. Consulta [Administrar instalaciones de Go](https://go.dev/doc/manage-install) para gestionar versiones.

# Ejecutar Hello, World

Crea una carpeta de trabajo e inicializa un módulo dentro de ella:

```sh
mkdir hello
cd hello
go mod init example/hello
```

Crea `hello.go` en esa carpeta y guarda este código:

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

Ejecuta el programa así:

```sh
go run .
```

Se mostrará `Hello, World!`. Para generar un ejecutable, ejecuta `go build`. El nombre y la extensión dependen del sistema operativo; en Windows normalmente se usa `.exe`.

# Sigue aprendiendo

- [Tutorial oficial de Go: primeros pasos](https://go.dev/doc/tutorial/getting-started)
- [Preguntas frecuentes de Go](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/) (prueba código en el navegador)

Los materiales oficiales de introducción están disponibles principalmente en inglés.
