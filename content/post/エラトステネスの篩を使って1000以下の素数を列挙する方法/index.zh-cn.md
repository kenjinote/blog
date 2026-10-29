---
title: '什么是埃拉托斯特尼筛法？列举1000以内素数的算法与实现'
slug: "埃拉托斯特尼筛法を使って1000以下の素数を列挙する方法"
tags: ["埃拉托斯特尼筛法", "素数", "数学", "Rust"]
draft: false
math: true
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "用Rust筛法列举不大于1000的168个素数，解释从平方开始筛除、奇数候选、0和1的边界、复杂度与内存限制。"
date: 2023-04-09T12:54:24+09:00
lastmod: 2026-10-29
---

埃拉托斯特尼筛法用于一次列举上限 `n` 以下的所有素数，包含上限本身。这里用Rust输出不大于1000的168个素数。0和1不是素数。

## 筛法步骤与从平方开始的原因

1. 要使用0到 `n` 的下标，需要分配 `n + 1` 个布尔元素。基本版先初始化为真，再将0和1设为假。上限小于2时，在访问下标1之前返回空结果。
2. 从2开始按递增顺序检查候选 `p`。若标记仍为真，`p` 就是素数：从 $p^2$ 开始，以 `p` 为步长将倍数设为假。不要将 `p` 本身设为假。
3. 只需对满足 $p^2\le n$ 的候选执行筛除，因为每个合数都有一个不大于其平方根的素因子。
4. 最后扫描2到 `n`，输出仍标记为真的所有数。输出范围并不局限于平方根以内。

小于 $p^2$ 的倍数 $kp$（$2\le k<p$）已经被 `k` 的某个小于 `p` 的素因子筛除。这并不意味着所有较小的数都已经完成了列举。

![以2到120的数演示筛法步骤的动画](Animation_Sieb_des_Eratosthenes.gif)

图片：SKopp，Suricata更新版本，[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Animation_Sieb_des_Eratosthenes.gif)，[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)。文件未经修改。图片的范围是2到120，而下方代码使用的上限是1000。

## Rust基本实现

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

保存为 `sieve.rs`，使用 `rustc --edition=2021 sieve.rs -o sieve` 编译。在Windows上，将可执行文件名指定为 `sieve.exe`。运行后输出168行，首个数为2，最后一个为997。这些示例已在Rust 1.90.0上运行。

`sieve(0)` 和 `sieve(1)` 返回空向量，`sieve(2)` 返回 `[2]`。条件 `p <= n / p` 确保只在平方不超过上限时计算 `p * p`。每次增加倍数之前还会检查剩余距离，不需要使用浮点平方根。

## 只筛除奇数候选的实现

大于2的偶数都是合数。因此可以只将2标记为真，并将奇数初始化为候选。对于奇素数 `p`，其平方也是奇数；从平方开始以 $2p$ 为步长，就只会访问奇数倍数。

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

将这一版保存到另一个文件并编译。它输出相同的168个素数，对0和1返回空结果，对2返回 `[2]`。不要把两个 `main` 函数放在同一个文件中。

这一版省略了部分偶数处理，但“初始化为假就一定更快”并无保证。初始化、写入、内存访问的开销，以及编译器和目标机器都会影响运行时间。这里没有进行计时比较。为使下标直接对应数值，数组仍有 `n + 1` 个元素。

## 复杂度与上限的适用范围

在通常的RAM模型下，筛法的时间复杂度为 $O(n\log\log n)$，标记所需的存储空间为 $O(n)$。这是渐近的操作数和存储量估计，并非实测时间或任意精度整数的位复杂度。[Princeton的算法分析教材](https://introcs.cs.princeton.edu/java/41analysis/)中的筛法习题也给出了这一增长率。

Rust的 [`bool`](https://doc.rust-lang.org/reference/types/boolean.html) 占一个字节，[`Vec<T>`](https://doc.rust-lang.org/std/vec/struct.Vec.html#guarantees) 连续存储元素。这里的 `Vec<bool>` 不是位压缩数组。标记的逻辑元素个数为 `n + 1`，还需要向量的管理信息、分配容量以及返回的 `Vec<usize>` 所占的空间。

若无法表示 `n + 1`，`checked_add` 会返回 `None`，随后的 `expect` 会触发panic。其他情况下也必须有足够的可用内存，并不能处理任意大的上限。对于较大的区间，可以考虑分段筛。列举一个范围内的素数，与判断单个大整数是否为素数，适用场景不同。
