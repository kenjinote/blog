---
title: 'Como criar um programa que enumera números primos em Rust e exemplos de código'
slug: "Enumerando Números Primos em Rust"
date: 2022-09-09T07:08:49+09:00
tags: ["Rust","Números Primos","Algoritmo"]
draft: false
image: "images/img.webp"
categories: ["Programação"]
description: 'Como parte do aprendizado da programação em Rust, apresentamos um exemplo de implementação de um algoritmo simples para listar os números primos até um limite especificado. Explicamos métodos básicos de codificação que usam processamento de loop e desvio condicional de maneira fácil de entender através de código de amostra concreto.'
---
Escrevi um programa para enumerar números primos em Rust.

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
