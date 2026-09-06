---
title: "Énumération des nombres premiers en Rust"
slug: "Énumération des nombres premiers en Rust"
date: 2022-09-09T07:08:49+09:00
tags: ["Rust","Nombres Premiers","Algorithme"]
draft: false
image: "images/img.png"
categories: ["Programmation"]
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
