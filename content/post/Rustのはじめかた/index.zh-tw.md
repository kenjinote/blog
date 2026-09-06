---
title: "如何開始使用 Rust"
slug: "如何開始使用 Rust"
date: 2022-09-06T00:12:36+09:00
tags: ["Rust"]
draft: false
image: "images/rust_logo.png"
categories: ["程式設計"]
---
# 簡介
Rust 是一種相對較新的程式語言，它允許您使用現代語法編寫快速且記憶體效率高的模組。
它支援多平台，也被用於 WebAssembly 和嵌入式系統領域。
著名的是，它被 Firefox、DropBox 和 Cloudflare 採用。

它也作為 C++ 的替代品而受到關注。

# 安裝方法

[安裝 Rust](https://www.rust-lang.org/ja/tools/install)

上述網站提供了各個平台的安裝說明。

# 第一個程式

將以下程式儲存為 `main.rs`。

```
fn main() {
    println!("Hello, world!");
}
```

從命令提示字元或終端機執行 `rustc main.rs` 時，它將被編譯。執行 `./main`（在 Windows 上為 `main.exe`）將輸出 `Hello, world!`。

# 日語文件

[The Rust Programming Language 日語版](https://doc.rust-jp.rs/book-ja/)

學習 Rust 所需的說明都集中在上面的連結（日語翻譯版）中。
它非常全面，以至於您不需要購買 Rust 的書籍。

# 如果您想在 Web 上嘗試

如果您想在不安裝編譯器的情況下在 Web 上嘗試，可以使用 [The Rust Playground](https://play.rust-lang.org/)。
輸入程式碼並按下「執行」按鈕後，它將在 Web 上編譯並執行。
