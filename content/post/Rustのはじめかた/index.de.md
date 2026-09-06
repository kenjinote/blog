---
title: "Wie man mit Rust anfängt"
slug: "Wie man mit Rust anfängt"
date: 2022-09-06T00:12:36+09:00
tags: ["Rust"]
draft: false
image: "images/rust_logo.png"
categories: ["Programmierung"]
---
# Einführung
Rust ist eine relativ neue Programmiersprache, mit der Sie schnelle und speichereffiziente Module mit moderner Syntax schreiben können.
Es ist plattformübergreifend und wird auch in der Welt von WebAssembly und eingebetteten Systemen verwendet.
Bekanntermaßen wird es von Firefox, DropBox und Cloudflare eingesetzt.

Es zieht auch als Alternative zu C++ Aufmerksamkeit auf sich.

# Wie man installiert

[Rust installieren](https://www.rust-lang.org/ja/tools/install)

Die obige Website bietet Installationsanweisungen für jede Plattform.

# Erstes Programm

Speichern Sie das folgende Programm als `main.rs`.

```
fn main() {
    println!("Hello, world!");
}
```

Wenn Sie `rustc main.rs` über die Eingabeaufforderung oder das Terminal ausführen, wird es kompiliert. Die Ausführung von `./main` (oder `main.exe` unter Windows) gibt `Hello, world!` aus.

# Japanische Dokumentation

[The Rust Programming Language Japanische Ausgabe](https://doc.rust-jp.rs/book-ja/)

Die Erklärungen, die zum Erlernen von Rust notwendig sind, sind unter dem obigen Link (japanisch übersetzte Version) zusammengestellt.
Sie ist so umfassend, dass Sie kein Buch über Rust kaufen müssen.

# Wenn Sie es im Web ausprobieren möchten

Wenn Sie es im Web ausprobieren möchten, ohne den Compiler zu installieren, können Sie [The Rust Playground](https://play.rust-lang.org/) verwenden.
Nach der Eingabe des Codes und dem Klicken auf die Schaltfläche "Run" wird er im Web kompiliert und ausgeführt.
