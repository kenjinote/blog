---
title: "Rustの主な特徴5つ：メモリ安全性・所有権・Cargo"
slug: "Rustの特徴"
date: 2022-10-03T22:47:20+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Rustの成り立ち、ガベージコレクションに頼らない設計、所有権と借用、プラットフォーム対応、Cargoの役割を公式資料に沿って紹介します。安全性の保証範囲やターゲットごとの対応差も補足します。"
---
Rustは、信頼性と効率性を重視するオープンソースのプログラミング言語です。主な特徴を5つ紹介します。

1. **Mozilla Researchから始まったコミュニティプロジェクト**：RustはMozilla Researchのプロジェクトとして始まりました。2015年以降、プロジェクトの方針と運営はMozillaから独立しています。
2. **ガベージコレクターに頼らない設計**：Rustは組み込みのガベージコレクターなしで、性能とメモリ効率を重視したソフトウェアを作れます。
3. **所有権と借用**：所有権、参照、借用の仕組みは、通常の安全なRustコードにおける多くのメモリ安全性をコンパイル時に保証します。ただし、`unsafe`コードや他言語との連携では、開発者が安全性を慎重に確認する必要があります。
4. **幅広いプラットフォーム対応**：多くのOSやプロセッサ向けにコンパイルできますが、各ターゲットのサポート水準や保証は同じではありません。
5. **Cargo**：Rustの標準ツールCargoは、パッケージ管理に加えてビルドやテストなども扱います。

Rustプロジェクトは現在、コミュニティによって運営され、Rust Foundationが支援しています。詳しくは [Rust公式サイト](https://www.rust-lang.org/)、[プロジェクトの沿革](https://blog.rust-lang.org/2020/08/18/laying-the-foundation-for-rusts-future.html)、[所有権](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html)、[Cargo](https://doc.rust-lang.org/cargo/)、[プラットフォーム対応](https://doc.rust-lang.org/rustc/platform-support.html)、[Unsafe Rust](https://doc.rust-lang.org/book/ch20-01-unsafe-rust.html)を参照してください。
