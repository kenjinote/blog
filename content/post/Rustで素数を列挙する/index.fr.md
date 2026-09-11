---
title: 'Comment créer un programme pour énumérer les nombres premiers en Rust et des exemples de code'
slug: "Rustで素数を列挙する"
date: 2022-09-09T07:08:49+09:00
tags: ["Rust","Nombres Premiers","Algorithme"]
draft: false
image: "images/img.webp"
categories: ["Programmation"]
description: 'Dans le cadre de l''apprentissage de la programmation en Rust, présente un exemple d''implémentation d''un algorithme simple qui énumère les nombres premiers jusqu''à une limite supérieure spécifiée. Explique clairement comment coder de manière basique en utilisant des boucles et des branchements conditionnels avec des exemples de code spécifiques.'
---
J'ai écrit un programme pour énumérer les nombres premiers en Rust.

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
