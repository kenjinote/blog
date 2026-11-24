---
title: "Fünf zentrale Merkmale von Rust: Sicherheit, Ownership und Cargo"
slug: "Rustの特徴"
date: 2022-10-03T22:47:20+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Überblick über Rusts Ursprung, Speichermodell, Ownership und Borrowing, Plattformunterstützung und Cargo sowie über Grenzen der Sicherheitsgarantien."
---
Rust ist eine Open-Source-Programmiersprache für zuverlässige und effiziente Software. Hier sind fünf wichtige Merkmale.

1. **Community-Projekt mit Ursprung bei Mozilla**: Rust begann als Mozilla-Research-Projekt. Seit 2015 sind Ausrichtung und Governance des Projekts unabhängig von Mozilla.
2. **Kein integrierter Garbage Collector**: Rust ist auf Leistung und Speichereffizienz ausgelegt, ohne auf einen integrierten Garbage Collector angewiesen zu sein.
3. **Ownership und Borrowing**: Ownership, Referenzen und Borrowing ermöglichen dem Compiler, viele Speicher-Sicherheitsgarantien für gewöhnlichen sicheren Rust-Code durchzusetzen. `unsafe`-Code und Schnittstellen zu anderen Sprachen müssen weiterhin sorgfältig geprüft werden.
4. **Unterstützung vieler Plattformen**: Rust kann auf zahlreiche Betriebssysteme und Prozessorarchitekturen ausgerichtet werden; Umfang und Garantien der Unterstützung unterscheiden sich jedoch je nach Target.
5. **Cargo**: Das Standardwerkzeug Cargo verwaltet Pakete und übernimmt außerdem Aufgaben wie Build und Tests.

Das Rust-Projekt wird von der Community gesteuert und von der Rust Foundation unterstützt. Siehe die [offizielle Rust-Website](https://www.rust-lang.org/), die [Projektgeschichte](https://blog.rust-lang.org/2020/08/18/laying-the-foundation-for-rusts-future.html), den [Ownership-Leitfaden](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html), das [Cargo Book](https://doc.rust-lang.org/cargo/), die [Plattformunterstützung](https://doc.rust-lang.org/rustc/platform-support.html) und [Unsafe Rust](https://doc.rust-lang.org/book/ch20-01-unsafe-rust.html).
