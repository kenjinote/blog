---
title: 'What is the Sieve of Eratosthenes? Algorithm and Implementation for Enumerating Primes Up to and Including 1000'
slug: "Sieve of Eratosthenesを使って1000以下のPrime Numberを列挙する方法"
tags: ["Sieve of Eratosthenes", "Prime Numbers", "Math", "Rust"]
draft: false
math: true
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "List the 168 primes up to and including 1000 with Rust sieve implementations. Explains square-start marking, odd candidates, small bounds, complexity and memory limits."
date: 2023-04-09T12:54:24+09:00
lastmod: 2026-10-29
---

The sieve of Eratosthenes lists all primes up to an inclusive upper bound `n`. Here, Rust programs print the 168 primes at most 1000. The bound is included; 0 and 1 are not primes.

## Sieve steps and why marking starts at the square

1. Allocate `n + 1` boolean elements to use indices from 0 through `n`. The basic version initializes them to true and marks 0 and 1 false. For a bound below 2, return an empty result before accessing index 1.
2. Examine candidates `p` in increasing order, starting at 2. If the flag is still true, `p` is prime: mark multiples starting at $p^2$, advancing by `p`, as false. Do not mark `p` itself.
3. Marking multiples only requires candidates satisfying $p^2\le n$, because every composite has a prime factor at most its square root.
4. Finally, scan from 2 through `n` and output every number whose flag remains true. The output range is not restricted to the square root.

A multiple $kp$ below $p^2$, where $2\le k<p$, has already been marked by a prime factor of `k` smaller than `p`. This does not mean that all smaller numbers have already been enumerated.

![Animation illustrating the sieve on numbers from 2 through 120](Animation_Sieb_des_Eratosthenes.gif)

Image: SKopp, version updated by Suricata, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Animation_Sieb_des_Eratosthenes.gif), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). The file is unmodified. The illustration covers 2 through 120, while the programs below use a bound of 1000.

## Basic Rust implementation

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

Save as `sieve.rs` and compile with `rustc --edition=2021 sieve.rs -o sieve`. On Windows, use `sieve.exe` as the executable name. Running it prints 168 lines, starting with 2 and ending with 997. These examples were run with Rust 1.90.0.

`sieve(0)` and `sieve(1)` return an empty vector; `sieve(2)` returns `[2]`. The condition `p <= n / p` ensures that `p * p` is evaluated only when the square is within the bound. The remaining distance is checked before adding the next multiple. No floating-point square root is needed.

## A version that marks only odd candidates

Even numbers greater than 2 are composite. We can therefore mark 2 as true and initialize only odd numbers as candidates. For an odd prime `p`, its square is odd; advancing from it by $2p$ visits only odd multiples.

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

Save this version in a separate file and compile it. It outputs the same 168 primes, returns an empty result for 0 or 1, and returns `[2]` for 2. Do not combine the two `main` functions in one file.

This version skips some work on even numbers. However, initializing to false is not a guarantee of better speed. Runtime depends on initialization, writes, memory access, the compiler and the target machine. No timing comparison is presented here. The array still contains `n + 1` elements so that indices correspond directly to numbers.

## Complexity and supported bounds

In the usual RAM model, the sieve takes $O(n\log\log n)$ time and $O(n)$ flag storage. These are asymptotic operation and storage estimates, not measured runtimes or bit complexity for arbitrary-precision integers. The sieve exercise in [Princeton’s analysis material](https://introcs.cs.princeton.edu/java/41analysis/) also gives this growth rate.

Rust’s [`bool`](https://doc.rust-lang.org/reference/types/boolean.html) occupies one byte, and [`Vec<T>`](https://doc.rust-lang.org/std/vec/struct.Vec.html#guarantees) stores elements contiguously. This `Vec<bool>` is not a bit-packed array. The logical flag count is `n + 1`; vector metadata, allocated capacity and the returned `Vec<usize>` also require storage.

If `n + 1` cannot be represented, `checked_add` returns `None`, and the following `expect` triggers a panic. Otherwise, sufficient memory must still be available; the implementation does not support arbitrarily large bounds. Consider a segmented sieve for large intervals. Listing a range of primes serves a different purpose from testing one large integer.
