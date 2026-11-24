---
title: 'Introducción a cómo escribir y ejecutar pruebas en Rust (cargo test)'
slug: "RustでPruebaを書く"
date: "2022-10-01T02:00:59+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust","Pruebas"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Explicamos para principiantes cómo escribir código de prueba en Rust y los pasos para ejecutar las pruebas usando el comando cargo test. Mostramos en detalle el uso del atributo #[test] y los resultados mostrados en caso de éxito o fracaso, junto con ejemplos de código específicos.'
---

[Rust](https://kenji.blog/es/p/webassembly-wasm-current-future/) ejecuta como pruebas las funciones marcadas con `#[test]`. Este ejemplo define una prueba unitaria para una función de suma dentro de un módulo `#[cfg(test)]`.

```rust
fn add(left: i32, right: i32) -> i32 {
    left + right
}

#[cfg(test)]
mod tests {
    use super::add;

    #[test]
    fn adds_two_numbers() {
        assert_eq!(add(2, 2), 4);
    }
}
```

`cargo test` compila y ejecuta las pruebas del paquete. Las pruebas aprobadas muestran `ok` y el resumen incluye `test result: ok`.

```bash
cargo test
```

Si falla una aserción, la prueba correspondiente aparece como `FAILED` y Cargo termina con error. Las rutas, líneas y tiempos varían según el entorno y la versión de Rust.

## Referencias

- [The Rust Programming Language: How to Write Tests](https://doc.rust-lang.org/book/ch11-01-writing-tests.html)
- [The Cargo Book: cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html)
- [The Rust Reference: test attributes](https://doc.rust-lang.org/reference/attributes/testing.html)
