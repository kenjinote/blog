---
title: 'Introduction à l''écriture et l''exécution de tests en Rust (cargo test)'
slug: "Rustでテストを書く"
date: 2022-10-01T02:00:59+09:00
tags: ["Rust","Tests"]
draft: false
image: "images/rust_logo.webp"
categories: ["Programmation"]
description: 'Explique pour les débutants comment écrire du code de test en Rust et la procédure d''exécution des tests à l''aide de la commande cargo test. Présente en détail l''utilisation de l''attribut #[test] et les résultats de sortie lors du succès ou de l''échec avec des exemples de code concrets.'
---

Pour écrire des tests en Rust, créez la fonction en ajoutant l'attribut `#[test]` une ligne au-dessus de la définition de la fonction de test.

```rust
fn plus(a:i32,b:i32)->i32 {
  a+b
}

#[test]
fn plus_test() {
  assert_eq!(plus(1, 1), 2);
}
```

Le code de test peut être exécuté avec `cargo test`. Si le test réussit, il affichera `ok`.
S'il échoue, il affichera `FAILED`.

En cas de succès
```bash
C:\Users\admin\Desktop\test1>cargo test
   Compiling test1 v0.1.0 (C:\Users\admin\Desktop\test1)
    Finished test [unoptimized + debuginfo] target(s) in 0.35s
     Running unittests src\main.rs (target\debug\deps\test1-be5d3118bc52cb3a.exe)

running 1 test
test plus_test ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s
```

En cas d'échec
```bash
C:\Users\admin\Desktop\test1>cargo test
   Compiling test1 v0.1.0 (C:\Users\admin\Desktop\test1)
    Finished test [unoptimized + debuginfo] target(s) in 0.33s
     Running unittests src\main.rs (target\debug\deps\test1-be5d3118bc52cb3a.exe)

running 1 test
test plus_test ... FAILED

failures:

---- plus_test stdout ----
thread 'plus_test' panicked at 'assertion failed: `(left == right)`
  left: `2`,
 right: `3`', src\main.rs:7:5
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace


failures:
    plus_test

test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

error: test failed, to rerun pass '--bin test1'
```
