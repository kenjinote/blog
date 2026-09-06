---
title: "Como começar com Rust"
slug: "Como começar com Rust"
date: 2022-09-06T00:12:36+09:00
tags: ["Rust"]
draft: false
image: "images/rust_logo.png"
categories: ["Programação"]
---
# Introdução
Rust é uma linguagem de programação relativamente nova que permite escrever módulos rápidos e eficientes em memória com uma sintaxe moderna.
É compatível com várias plataformas e também é usada no mundo do WebAssembly e em sistemas embarcados.
De forma notável, foi adotada pelo Firefox, DropBox e Cloudflare.

Também está atraindo atenção como uma alternativa ao C++.

# Como instalar

[Instalar o Rust](https://www.rust-lang.org/ja/tools/install)

O site acima fornece instruções de instalação para cada plataforma.

# Primeiro programa

Salve o seguinte programa como `main.rs`.

```
fn main() {
    println!("Hello, world!");
}
```

Ao executar `rustc main.rs` no prompt de comando ou terminal, ele será compilado. Executar `./main` (ou `main.exe` no Windows) exibirá `Hello, world!`.

# Documentação em Japonês

[The Rust Programming Language Edição Japonesa](https://doc.rust-jp.rs/book-ja/)

As explicações necessárias para aprender Rust estão compiladas no link acima (versão traduzida para o japonês).
É tão abrangente que você não precisa comprar um livro sobre Rust.

# Se você quiser experimentar na Web

Se você quiser experimentá-lo na Web sem instalar o compilador, pode usar [The Rust Playground](https://play.rust-lang.org/).
Após inserir o código e clicar no botão "Run", ele será compilado e executado na Web.
