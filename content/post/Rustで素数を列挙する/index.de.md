---
title: 'Wie man ein Programm zur Aufzählung von Primzahlen in Rust erstellt und Codebeispiele'
slug: "Aufzählung von Primzahlen in Rust"
date: 2022-09-09T07:08:49+09:00
tags: ["Rust","Primzahlen","Algorithmus"]
draft: false
image: "images/img.webp"
categories: ["Programmierung"]
description: 'Stellt als Lernmaterial für die Rust-Programmierung ein Implementierungsbeispiel eines einfachen Algorithmus vor, der Primzahlen bis zu einer angegebenen Obergrenze aufzählt. Erklärt leicht verständlich grundlegende Codierungsmethoden mit Schleifen und bedingten Verzweigungen zusammen mit konkretem Beispielcode.'
---
Ich habe ein Programm geschrieben, um Primzahlen in Rust aufzuzählen.

```rust
fn main() {
	let max = 1000;
    let mut primes = vec![2];
    let mut n = 3;
    loop {
        let mut is_prime = true;
        for p in &primes {
            if n % p == 0 {
                is_prime = false;
                break;
            }
        }
        if is_prime {
            primes.push(n);
        }
        n += 2;
		if n > max {
			break;
		}
    }
    for p in &primes {
		println!("{}", p);
    }
}
```
