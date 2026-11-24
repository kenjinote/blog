---
title: "Cinco características principais do Rust: segurança, ownership e Cargo"
slug: "Rustの特徴"
date: 2022-10-03T22:47:20+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Visão geral da origem do Rust, seu modelo de memória, ownership e borrowing, suporte a plataformas e Cargo, com ressalvas sobre as garantias de segurança."
---
Rust é uma linguagem de programação de código aberto voltada à criação de software confiável e eficiente. Estas são cinco de suas principais características.

1. **Projeto comunitário com origem na Mozilla**: Rust começou como um projeto da Mozilla Research. Desde 2015, a direção e a governança do projeto são independentes da Mozilla.
2. **Sem coletor de lixo integrado**: Rust foi projetado para desempenho e eficiência de memória sem depender de um coletor de lixo integrado.
3. **Ownership e borrowing**: Propriedade, referências e empréstimos permitem que o compilador aplique muitas garantias de segurança de memória no Rust seguro comum. Código `unsafe` e interfaces com outras linguagens ainda exigem revisão cuidadosa.
4. **Suporte amplo a plataformas**: Rust pode ter como alvo muitos sistemas operacionais e arquiteturas de processadores, mas os níveis de suporte e as garantias variam conforme o alvo.
5. **Cargo**: A ferramenta padrão Cargo gerencia pacotes e também executa tarefas como compilação e testes.

O projeto Rust é governado pela comunidade e recebe apoio da Rust Foundation. Consulte o [site oficial do Rust](https://www.rust-lang.org/), a [história do projeto](https://blog.rust-lang.org/2020/08/18/laying-the-foundation-for-rusts-future.html), o [guia de ownership](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html), o [Cargo Book](https://doc.rust-lang.org/cargo/), o [suporte a plataformas](https://doc.rust-lang.org/rustc/platform-support.html) e [Unsafe Rust](https://doc.rust-lang.org/book/ch20-01-unsafe-rust.html).
