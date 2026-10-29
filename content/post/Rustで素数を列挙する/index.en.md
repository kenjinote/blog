---
title: 'How to Create a Program to Enumerate Prime Numbers in Rust and Code Examples'
slug: "RustでPrime Numberを列挙する"
tags: ["Rust", "Prime Numbers", "Algorithm"]
draft: false
image: "images/img.webp"
categories: ["programming"]
description: "List primes with stored-prime trial division in Rust. Handles small bounds and explains the square-root cutoff, vector iteration, bounded increments and practical limits."
date: 2022-09-09T07:08:49+09:00
lastmod: 2026-10-29
---

This Rust example stores the primes it finds and uses them for trial division. `primes_up_to(max)` returns a list of primes up to and including the bound. There are 168 primes at most 1000; 0 and 1 are not primes. This is not a sieve implementation.

## Code

```rust
fn primes_up_to(max: usize) -> Vec<usize> {
    if max < 2 {
        return Vec::new();
    }
    let mut primes = vec![2];
    let mut n = 3;
    while n <= max {
        let mut is_prime = true;
        for &p in &primes {
            if p > n / p {
                break;
            }
            if n % p == 0 {
                is_prime = false;
                break;
            }
        }
        if is_prime {
            primes.push(n);
        }
        if max - n < 2 {
            break;
        }
        n += 2;
    }
    primes
}

fn main() {
    for p in primes_up_to(1000) {
        println!("{}", p);
    }
}
```

## Running and small bounds

Save as `primes.rs` and compile with `rustc --edition=2021 primes.rs -o primes`. On Windows, use `primes.exe` as the executable name. Running it prints 168 lines, starting at 2 and ending at 997. These examples were run with Rust 1.90.0.

`primes_up_to(0)` and `primes_up_to(1)` return an empty vector; `primes_up_to(2)` returns `[2]`, `primes_up_to(3)` returns `[2, 3]`, and `primes_up_to(10)` returns `[2, 3, 5, 7]`. The `usize` parameter type excludes negative bounds. This program does not parse standard input.

## How the test and loop work

1. Return an empty result for a bound below 2. Otherwise, store 2 and test only odd candidates from 3 through the bound. The bound is checked before processing a candidate, so a bound of 2 does not add 3.
2. A composite candidate `n` has a prime factor at most its square root. Such primes are already in the list from earlier candidates. Stop and reject the candidate if a division has no remainder. If no divisor has been found when `p > n / p`, further trial division is unnecessary. Positive integer division expresses the square-root condition without `p * p` or a floating-point square root.
3. `for &p in &primes` borrows the list, receives references in turn, and copies each `usize` value into `p`. A new prime is added only after this loop ends. The final `for p in primes_up_to(1000)` takes values from the returned vector and prints them. [Rust’s Vec documentation](https://doc.rust-lang.org/std/vec/struct.Vec.html) distinguishes borrowed and owned iteration.
4. Inside `n <= max`, `max - n` cannot be negative. If the remaining distance is less than 2, exit before adding; otherwise, perform `n += 2`. This avoids an increment beyond the bound.

## Scope

The original fixed-bound program also correctly prints 168 primes for 1000. However, merely changing its bound to 0, 1 or 2 prints out-of-range values 2 or 3 because the bound is not checked before processing. The reusable function here handles those boundaries.

The list contains one `usize` per discovered prime. Vector metadata and allocated capacity also require memory. A coarse upper bound on trial divisions is `O(max sqrt(max))`, counting a division as one operation; this is not measured runtime or bit complexity. Larger bounds require more time and storage, with no guarantee of quickly listing primes up to arbitrarily large limits. For listing a large range, see the [sieve of Eratosthenes article](https://kenji.blog/en/p/sieve-of-eratosthenes%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A61000%E4%BB%A5%E4%B8%8B%E3%81%AEprime-number%E3%82%92%E5%88%97%E6%8C%99%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/). This is not a cryptographic prime generator.
