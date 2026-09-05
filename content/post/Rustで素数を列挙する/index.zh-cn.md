---
title: '在 Rust 中枚举素数'
date: 2022-09-09T07:08:49+09:00
tags: ["Rust","素数","算法"]
draft: false
image: "images/img.png"
categories: ["编程"]
---
我尝试写了一个在 Rust 中枚举素数的程序。

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
