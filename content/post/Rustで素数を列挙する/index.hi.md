---
title: "Rust में अभाज्य संख्याओं की गणना"
slug: "Rust में अभाज्य संख्याओं की गणना"
date: 2022-09-09T07:08:49+09:00
tags: ["Rust","अभाज्य संख्याएँ","एल्गोरिदम"]
draft: false
image: "images/img.png"
categories: ["प्रोग्रामिंग"]
---
मैंने Rust में अभाज्य संख्याओं की गणना करने के लिए एक प्रोग्राम लिखा है।

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
