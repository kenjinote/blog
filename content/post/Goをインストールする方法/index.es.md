---


title: "Cómo instalar Go"
date: 2022-09-10T00:48:17+09:00
tags: ["Go","Instalación"]
draft: false
image: "images/cover.png"
categories: ["Programación"]
---


# Introducción
Go es un lenguaje de programación relativamente nuevo publicado por Google en 2009.
El compilador, las herramientas y las bibliotecas de Go se publican como código abierto.
Además, Go es un lenguaje de tipado estático como C y Java, pero es un lenguaje que no utiliza punteros como el lenguaje C.

# Método de instalación

[Instalar Go](https://go.dev/dl/)

Desde el sitio anterior, se publican instaladores para cada plataforma.

Siga la pantalla para proceder con la instalación.
![img.png](images/img.png)

![img_1.png](images/img_1.png)

![img_2.png](images/img_2.png)

![img_3.png](images/img_3.png)

![img_5.png](images/img_5.png)

![img_6.png](images/img_6.png)

La instalación se ha completado. Es fácil, ¿verdad?

# Primer programa

Guarde el siguiente programa como `hello.go`.

```go
package main

import "fmt"

func main() {
  fmt.Printf("Hello World\n")
}
```

Al ejecutar `go run hello.go` desde el símbolo del sistema o la terminal, se mostrará `Hello, world!`.

Si desea compilarlo, al ejecutar `go build hello.go`, se generará `hello.exe`.
Al ejecutar `hello.exe`, se mostrará `Hello, world!`.

# También puede ejecutar código en la página web

[https://go.dev/play/](https://go.dev/play/)

![img_7.png](images/img_7.png)

# Documentación en japonés

[http://go.shibu.jp/](http://go.shibu.jp/)

Las explicaciones necesarias para aprender Go están concentradas en el enlace anterior (versión traducida al japonés).
Dado que la tecnología relacionada con Go es abierta, es tan completa que no es necesario comprar textos en papel.

¡Entonces, que disfrutes de tu vida con Go!
