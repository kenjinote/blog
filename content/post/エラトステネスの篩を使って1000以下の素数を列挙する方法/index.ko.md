---
title: '에라토스테네스의 체란? 1000 이하의 소수를 나열하는 알고리즘과 구현'
slug: "에라토스테네스의 체を使って1000以下の소수を列挙する方法"
tags: ["에라토스테네스의 체", "소수", "수학", "Rust"]
draft: false
math: true
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "Rust의 체로 1000 이하 소수 168개를 나열합니다. 제곱부터 지우는 이유, 홀수 후보, 0과 1의 경계, 복잡도와 메모리 한계를 설명합니다."
date: 2023-04-09T12:54:24+09:00
lastmod: 2026-10-29
---

에라토스테네스의 체는 상한 `n` 이하의 모든 소수를 나열합니다. 여기서는 Rust로 1000 이하의 소수 168개를 출력합니다. 상한도 포함하며 0과 1은 소수가 아닙니다.

## 체의 절차와 제곱부터 시작하는 이유

1. 인덱스 0부터 `n`까지 쓰려면 불리언 원소 `n + 1`개를 할당해야 합니다. 기본 버전은 참으로 초기화한 뒤 0과 1을 거짓으로 표시합니다. 상한이 2보다 작으면 인덱스 1에 접근하기 전에 빈 결과를 반환합니다.
2. 2부터 후보 `p`를 오름차순으로 확인합니다. 표시가 아직 참이면 `p`는 소수입니다. $p^2$부터 `p`씩 증가시키며 배수를 거짓으로 표시합니다. `p` 자체는 지우지 않습니다.
3. 배수를 지우는 처리는 $p^2\le n$인 후보까지만 하면 됩니다. 모든 합성수에는 그 제곱근 이하의 소인수가 있기 때문입니다.
4. 마지막으로 2부터 `n`까지 검사해 참으로 남은 모든 수를 출력합니다. 출력 범위가 제곱근 이하로 제한되는 것은 아닙니다.

$p^2$보다 작은 배수 $kp$에서 $2\le k<p$이면, `k`의 소인수 중 `p`보다 작은 수를 처리할 때 이미 지워집니다. 더 작은 모든 수의 나열이 끝났다는 뜻이 아닙니다.

![2부터 120까지의 수로 체의 절차를 보여 주는 애니메이션](Animation_Sieb_des_Eratosthenes.gif)

그림: SKopp, Suricata가 갱신한 버전, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Animation_Sieb_des_Eratosthenes.gif), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). 파일은 수정하지 않았습니다. 그림의 범위는 2부터 120까지이며, 아래 코드의 상한 1000과는 다릅니다.

## Rust 기본 구현

```rust
fn sieve(n: usize) -> Vec<usize> {
    if n < 2 {
        return Vec::new();
    }
    let len = n.checked_add(1).expect("n + 1 is too large");
    let mut is_prime = vec![true; len];
    is_prime[0] = false;
    is_prime[1] = false;

    let mut p = 2;
    while p <= n / p {
        if is_prime[p] {
            let mut multiple = p * p;
            loop {
                is_prime[multiple] = false;
                if n - multiple < p {
                    break;
                }
                multiple += p;
            }
        }
        p += 1;
    }

    (2..=n).filter(|&i| is_prime[i]).collect()
}

fn main() {
    for prime in sieve(1000) {
        println!("{}", prime);
    }
}
```

`sieve.rs`로 저장하고 `rustc --edition=2021 sieve.rs -o sieve`로 컴파일합니다. Windows에서는 실행 파일 이름을 `sieve.exe`로 지정합니다. 실행하면 168줄을 출력하며 첫 수는 2, 마지막 수는 997입니다. 이 예제는 Rust 1.90.0에서 실행했습니다.

`sieve(0)`과 `sieve(1)`은 빈 벡터를, `sieve(2)`는 `[2]`를 반환합니다. `p <= n / p`는 제곱이 상한 이내일 때만 `p * p`를 계산하게 합니다. 다음 배수를 더하기 전에는 남은 거리를 확인합니다. 부동소수점 제곱근이 필요하지 않습니다.

## 홀수 후보만 지우는 구현

2보다 큰 짝수는 합성수입니다. 따라서 2를 참으로 표시하고 홀수만 후보로 초기화할 수 있습니다. 홀수 소수 `p`의 제곱도 홀수이며, 여기서 $2p$씩 증가시키면 홀수 배수만 방문합니다.

```rust
fn sieve_odd(n: usize) -> Vec<usize> {
    if n < 2 {
        return Vec::new();
    }
    let len = n.checked_add(1).expect("n + 1 is too large");
    let mut is_prime = vec![false; len];
    is_prime[2] = true;
    for i in (3..=n).step_by(2) {
        is_prime[i] = true;
    }

    let mut p = 3;
    while p <= n / p {
        if is_prime[p] {
            let step = 2 * p;
            let mut multiple = p * p;
            loop {
                is_prime[multiple] = false;
                if n - multiple < step {
                    break;
                }
                multiple += step;
            }
        }
        p += 2;
    }

    (2..=n).filter(|&i| is_prime[i]).collect()
}

fn main() {
    for prime in sieve_odd(1000) {
        println!("{}", prime);
    }
}
```

이 버전은 별도 파일에 저장해 컴파일합니다. 같은 소수 168개를 출력하며, 0과 1에는 빈 결과를, 2에는 `[2]`를 반환합니다. 두 `main` 함수를 한 파일에 합치지 마세요.

이 버전은 짝수를 처리하는 일부 작업을 생략합니다. 다만 거짓으로 초기화하면 언제나 더 빠르다는 보장은 없습니다. 실행 시간은 초기화, 쓰기, 메모리 접근, 컴파일러와 대상 기계에 따라 달라집니다. 여기서는 실행 시간을 측정해 비교하지 않았습니다. 인덱스와 수를 직접 대응시키므로 배열 자체는 여전히 원소 `n + 1`개를 가집니다.

## 복잡도와 적용 가능한 상한

일반적인 RAM 모델에서 체의 시간 복잡도는 $O(n\log\log n)$이고 표시용 저장 공간은 $O(n)$입니다. 이는 점근적인 연산 횟수와 저장량 평가이며, 실측 시간이나 임의 정밀도 정수의 비트 복잡도가 아닙니다. [Princeton의 알고리즘 분석 자료](https://introcs.cs.princeton.edu/java/41analysis/)에 있는 체 연습문제도 이 증가율을 제시합니다.

Rust의 [`bool`](https://doc.rust-lang.org/reference/types/boolean.html)은 1바이트이며 [`Vec<T>`](https://doc.rust-lang.org/std/vec/struct.Vec.html#guarantees)는 원소를 연속해서 저장합니다. 이 `Vec<bool>`은 비트를 압축한 배열이 아닙니다. 논리적인 표시 원소 수는 `n + 1`개이며, 벡터의 관리 정보, 할당 용량과 반환하는 `Vec<usize>`에도 공간이 필요합니다.

`n + 1`을 표현할 수 없으면 `checked_add`는 `None`을 반환하고, 뒤따르는 `expect`가 panic을 일으킵니다. 다른 경우에도 충분한 메모리가 필요하므로 상한을 임의로 크게 할 수는 없습니다. 큰 구간에는 분할 체 등을 고려합니다. 범위의 소수를 나열하는 일은 하나의 큰 정수에 대한 소수 판별과 용도가 다릅니다.
