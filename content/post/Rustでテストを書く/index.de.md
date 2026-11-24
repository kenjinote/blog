---
title: 'Einführung in das Schreiben und Ausführen von Tests in Rust (cargo test)'
slug: "RustでTestを書く"
date: "2022-10-01T02:00:59+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust","Tests"]
draft: false
image: "images/rust_logo.webp"
categories: ["programming"]
description: 'Erklärt für Anfänger, wie man Testcode in Rust schreibt und Tests mit dem Befehl cargo test ausführt. Stellt die Verwendung des #[test]-Attributs und die Ausgabeergebnisse bei Erfolg oder Fehlschlag mit konkreten Codebeispielen ausführlich vor.'
---

[Rust](https://kenji.blog/de/p/webassembly-wasm-current-future/) führt Funktionen mit `#[test]` als Tests aus. Dieses Beispiel definiert einen Einheitstest für eine Additionsfunktion in einem `#[cfg(test)]`-Modul.

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

`cargo test` erstellt und startet die Tests des Pakets. Erfolgreiche Tests zeigen `ok`; die Zusammenfassung enthält `test result: ok`.

```bash
cargo test
```

Schlägt eine Assertion fehl, wird der betreffende Test als `FAILED` markiert und Cargo endet mit einem Fehler. Pfade, Zeilennummern und Laufzeiten hängen von Umgebung und Rust-Version ab.

## Quellen

- [The Rust Programming Language: How to Write Tests](https://doc.rust-lang.org/book/ch11-01-writing-tests.html)
- [The Cargo Book: cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html)
- [The Rust Reference: test attributes](https://doc.rust-lang.org/reference/attributes/testing.html)
