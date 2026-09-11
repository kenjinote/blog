---
title: '使用Rust枚举素数的程序编写方法及代码示例'
slug: "Rustで素数を列挙する"
date: 2022-09-09T07:08:49+09:00
tags: ["Rust","素数","算法"]
draft: false
image: "images/img.webp"
categories: ["编程"]
description: '作为Rust编程的学习内容，介绍一个枚举指定上限值以内素数的简单算法实现示例。结合具体的示例代码，通俗易懂地讲解使用循环处理及条件分支的基础编码方法。'
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
