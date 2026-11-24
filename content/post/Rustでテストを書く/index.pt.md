---
title: 'Introdução sobre como escrever e executar testes em Rust (cargo test)'
slug: "RustでTesteを書く"
date: "2022-10-01T02:00:59+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust","Testes"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Explicamos aos iniciantes como escrever códigos de teste em Rust e os passos para executá-los usando o comando cargo test. Apresentamos em detalhes, com exemplos práticos de código, como usar o atributo #[test] e os resultados de saída em caso de sucesso ou falha.'
---

[Rust](https://kenji.blog/pt/p/webassembly-wasm-current-future/) executa como testes as funções marcadas com `#[test]`. Este exemplo define um teste unitário para uma função de soma dentro de um módulo `#[cfg(test)]`.

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

`cargo test` compila e executa os testes do pacote. Os testes aprovados mostram `ok`, e o resumo inclui `test result: ok`.

```bash
cargo test
```

Se uma asserção falhar, o teste correspondente será marcado como `FAILED` e o Cargo terminará com erro. Caminhos, linhas e tempos variam conforme o ambiente e a versão do Rust.

## Referências

- [The Rust Programming Language: How to Write Tests](https://doc.rust-lang.org/book/ch11-01-writing-tests.html)
- [The Cargo Book: cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html)
- [The Rust Reference: test attributes](https://doc.rust-lang.org/reference/attributes/testing.html)
