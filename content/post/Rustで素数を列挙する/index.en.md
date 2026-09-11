---
title: 'How to Create a Program to Enumerate Prime Numbers in Rust and Code Examples'
slug: "Rustで素数を列挙する"
date: 2022-09-09T07:08:49+09:00
tags: ["Rust", "Prime Numbers", "Algorithm"]
draft: false
image: "images/img.webp"
categories: ["Programming"]
description: 'Introduces an implementation example of a simple algorithm to enumerate prime numbers up to a specified upper limit as a learning exercise for Rust programming. Explains the basic coding method using loops and conditional branching clearly with specific sample code.'
---
I wrote a program to enumerate prime numbers in Rust.

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
