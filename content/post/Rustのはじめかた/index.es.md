---



title: "Cómo empezar con Rust"
slug: "Rustのはじめかた"
date: 2022-09-06T00:12:36+09:00
tags: ["Rust"]
draft: false
image: "images/rust_logo.png"
categories: ["Programación"]
---



# Introducción
Rust es un lenguaje de programación relativamente nuevo que permite escribir módulos rápidos y eficientes en el uso de la memoria con una sintaxis moderna.
Es compatible con múltiples plataformas y se utiliza en mundos como WebAssembly y sistemas embebidos.
Como ejemplos famosos, es utilizado por Firefox, DropBox y Cloudflare.

También está llamando la atención como una alternativa a C++.

# Método de instalación

[Instalar Rust](https://www.rust-lang.org/ja/tools/install)

En el sitio mencionado anteriormente se publican los métodos de instalación para cada plataforma.

# Primer programa

Guarde el siguiente programa como `main.rs`.

```
fn main() {
    println!("Hello, world!");
}
```

Al ejecutar `rustc main.rs` desde el símbolo del sistema o la terminal,
se compilará, y al ejecutar `./main` (`main.exe` en el caso de Windows), se imprimirá `Hello, world!`.

# Documentación en japonés

[The Rust Programming Language Versión Japonesa](https://doc.rust-jp.rs/book-ja/)

Las explicaciones necesarias para aprender Rust están recopiladas en el enlace anterior (versión traducida al japonés).
Es tan completo que no hay necesidad de comprar un libro de texto de Rust.

# Si desea probarlo en la Web

Si desea probarlo en la Web sin instalar un compilador, puede utilizar [The Rust Playground](https://play.rust-lang.org/).
Al ingresar el código y presionar el "botón de ejecución", se compilará y ejecutará en la Web.
