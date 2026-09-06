---
title: "Comment débuter avec Rust"
slug: "Comment débuter avec Rust"
date: 2022-09-06T00:12:36+09:00
tags: ["Rust"]
draft: false
image: "images/rust_logo.png"
categories: ["Programmation"]
---
# Introduction
Rust est un langage de programmation relativement nouveau qui vous permet d'écrire des modules rapides et économes en mémoire avec une syntaxe moderne.
Il prend en charge le multiplateforme et est également utilisé dans le monde du WebAssembly et des systèmes embarqués.
Il a notamment été adopté par Firefox, DropBox et Cloudflare.

Il attire également l'attention en tant qu'alternative au C++.

# Comment installer

[Installer Rust](https://www.rust-lang.org/ja/tools/install)

Le site ci-dessus fournit des instructions d'installation pour chaque plateforme.

# Premier programme

Enregistrez le programme suivant sous le nom `main.rs`.

```
fn main() {
    println!("Hello, world!");
}
```

En exécutant `rustc main.rs` depuis l'invite de commande ou le terminal, il sera compilé. L'exécution de `./main` (`main.exe` sous Windows) affichera `Hello, world!`.

# Documentation en japonais

[The Rust Programming Language Édition japonaise](https://doc.rust-jp.rs/book-ja/)

Les explications nécessaires pour apprendre Rust sont compilées dans le lien ci-dessus (version traduite en japonais).
Elle est si complète que vous n'avez pas besoin d'acheter un livre sur Rust.

# Si vous voulez l'essayer sur le Web

Si vous voulez l'essayer sur le Web sans installer le compilateur, vous pouvez utiliser [The Rust Playground](https://play.rust-lang.org/).
Après avoir entré le code et cliqué sur le bouton "Run", il sera compilé et exécuté sur le Web.
