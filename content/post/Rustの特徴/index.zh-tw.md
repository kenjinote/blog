---
title: "Rust 的五項主要特色：安全性、所有權與 Cargo"
slug: "Rustの特徴"
date: 2022-10-03T22:47:20+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "依據官方資料介紹 Rust 的起源、記憶體模型、所有權與借用、平台支援和 Cargo，並說明安全保證範圍及不同目標平台之間的差異。"
---
Rust 是一種著重可靠性與效率的開源程式語言。以下介紹五項主要特色。

1. **起源於 Mozilla、由社群治理**：Rust 最初是 Mozilla Research 專案；自 2015 年起，專案方向與治理便獨立於 Mozilla。
2. **不依賴內建垃圾回收器**：Rust 的設計重視效能與記憶體效率，不需仰賴內建垃圾回收器。
3. **所有權與借用**：所有權、參照與借用機制，讓編譯器能為一般安全 Rust 程式碼提供許多記憶體安全保證。不過，`unsafe` 程式碼及與其他語言的介面仍需仔細檢查。
4. **支援多種平台**：Rust 可編譯至多種作業系統與處理器架構，但不同目標的支援等級與保證並不相同。
5. **Cargo**：Rust 的標準工具 Cargo 除了管理套件，也處理建置與測試等工作。

Rust 專案由社群治理，並獲 Rust Foundation 支援。詳見 [Rust 官方網站](https://www.rust-lang.org/)、[專案沿革](https://blog.rust-lang.org/2020/08/18/laying-the-foundation-for-rusts-future.html)、[所有權指南](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html)、[Cargo 手冊](https://doc.rust-lang.org/cargo/)、[平台支援](https://doc.rust-lang.org/rustc/platform-support.html)與 [Unsafe Rust](https://doc.rust-lang.org/book/ch20-01-unsafe-rust.html)。
