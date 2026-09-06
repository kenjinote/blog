---




title: "Rust에서 소수 나열하기"
slug: "Rustで素数を列挙する"
date: 2022-09-09T07:08:49+09:00
tags: ["Rust","소수","알고리즘"]
draft: false
image: "images/img.png"
categories: ["프로그래밍"]
---




Rust로 소수를 나열하는 프로그램을 작성해 보았습니다.

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
