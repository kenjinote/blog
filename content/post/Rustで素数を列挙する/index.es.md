---



title: 'Ejemplo de código y creación de un programa en Rust para enumerar números primos'
slug: "Rustで素数を列挙する"
date: 2022-09-09T07:08:49+09:00
tags: ["Rust","números primos","algoritmos"]
draft: false
image: "images/img.webp"
categories: ["programación"]
description: 'Como aprendizaje de programación en Rust, presentamos un ejemplo de implementación de un algoritmo simple para enumerar números primos hasta un valor límite especificado. Explicamos de forma sencilla métodos de codificación básicos usando bucles y condiciones con código de muestra concreto.'
---



He escrito un programa para enumerar números primos en Rust.

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
