---




title: 'Rust에서 소수를 열거하는 프로그램의 작성 방법과 코드 예제'
slug: "Rustで素数を列挙する"
date: 2022-09-09T07:08:49+09:00
tags: ["Rust","소수","알고리즘"]
draft: false
image: "images/img.webp"
categories: ["프로그래밍"]
description: 'Rust 프로그래밍 학습의 일환으로 지정된 상한값까지의 소수를 열거하는 간단한 알고리즘의 구현 예를 소개합니다. 루프 처리 및 조건 분기를 이용한 기본적인 코딩 방법을 구체적인 샘플 코드와 함께 알기 쉽게 설명합니다.'
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
