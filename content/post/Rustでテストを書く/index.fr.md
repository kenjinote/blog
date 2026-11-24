---
title: 'Introduction à l''écriture et l''exécution de tests en Rust (cargo test)'
slug: "RustでTestを書く"
date: "2022-10-01T02:00:59+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust","Tests"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Explique pour les débutants comment écrire du code de test en Rust et la procédure d''exécution des tests à l''aide de la commande cargo test. Présente en détail l''utilisation de l''attribut #[test] et les résultats de sortie lors du succès ou de l''échec avec des exemples de code concrets.'
---

[Rust](https://kenji.blog/fr/p/webassembly-wasm-current-future/) exécute comme tests les fonctions marquées avec `#[test]`. Cet exemple définit un test unitaire d’addition dans un module `#[cfg(test)]`.

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

`cargo test` compile et exécute les tests du paquet. Les tests réussis affichent `ok` et le résumé contient `test result: ok`.

```bash
cargo test
```

Si une assertion échoue, le test concerné est marqué `FAILED` et Cargo se termine avec une erreur. Les chemins, numéros de ligne et durées dépendent de l’environnement et de la version de Rust.

## Références

- [The Rust Programming Language: How to Write Tests](https://doc.rust-lang.org/book/ch11-01-writing-tests.html)
- [The Cargo Book: cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html)
- [The Rust Reference: test attributes](https://doc.rust-lang.org/reference/attributes/testing.html)
