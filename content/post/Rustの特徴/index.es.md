---
title: "Cinco características clave de Rust: seguridad, ownership y Cargo"
slug: "Rustの特徴"
date: 2022-10-03T22:47:20+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Resumen del origen de Rust, su modelo de memoria, ownership y borrowing, compatibilidad de plataformas y Cargo, con aclaraciones sobre el alcance de las garantías de seguridad."
---
Rust es un lenguaje de programación de código abierto centrado en crear software fiable y eficiente. Estas son cinco de sus características principales.

1. **Un proyecto comunitario con raíces en Mozilla**: Rust nació como un proyecto de Mozilla Research. Desde 2015, la dirección y la gobernanza del proyecto son independientes de Mozilla.
2. **Sin recolector de basura integrado**: Rust está diseñado para ofrecer rendimiento y eficiencia de memoria sin depender de un recolector de basura integrado.
3. **Ownership y borrowing**: La propiedad, las referencias y los préstamos permiten al compilador aplicar muchas garantías de seguridad de memoria en Rust seguro. El código `unsafe` y las interfaces con otros lenguajes requieren una revisión cuidadosa.
4. **Compatibilidad amplia con plataformas**: Rust puede compilarse para muchos sistemas operativos y arquitecturas, aunque el nivel de soporte y las garantías varían según el destino.
5. **Cargo**: La herramienta estándar Cargo gestiona paquetes y también tareas como compilar y probar.

El proyecto Rust está gobernado por la comunidad y recibe apoyo de la Rust Foundation. Consulta el [sitio oficial de Rust](https://www.rust-lang.org/), la [historia del proyecto](https://blog.rust-lang.org/2020/08/18/laying-the-foundation-for-rusts-future.html), la [guía de ownership](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html), el [manual de Cargo](https://doc.rust-lang.org/cargo/), la [compatibilidad de plataformas](https://doc.rust-lang.org/rustc/platform-support.html) y [Rust inseguro](https://doc.rust-lang.org/book/ch20-01-unsafe-rust.html).
