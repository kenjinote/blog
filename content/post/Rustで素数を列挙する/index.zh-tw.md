---
title: '在 Rust 中列舉質數的程式建立方法與程式碼範例'
slug: "Rustで素数を列挙する"
date: 2022-09-09T07:08:49+09:00
tags: ["Rust","質數","演算法"]
draft: false
image: "images/img.webp"
categories: ["程式設計"]
description: '作為 Rust 程式設計的學習，介紹列舉至指定上限值為止所有質數的簡易演算法實作範例。搭配具體的範例程式碼，淺顯易懂地解說使用迴圈處理與條件判斷的基本編寫方法。'
---
我寫了一個在 Rust 中列舉質數的程式。

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
