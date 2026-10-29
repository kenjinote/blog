---
title: '使用Rust枚举素数的程序编写方法及代码示例'
slug: "Rustで素数を列挙する"
tags: ["Rust","素数","算法"]
draft: false
image: "images/img.webp"
categories: ["programming"]
description: "用已知素数试除，在Rust中列举上限以内的素数。说明0、1、2的边界、平方根截断、向量迭代、安全的递增条件与适用范围。"
date: 2022-09-09T07:08:49+09:00
lastmod: 2026-10-29
---

这个Rust示例保存已经找到的素数，并用它们进行试除。`primes_up_to(max)` 返回不大于上限的素数列表，包含上限本身。1000以内有168个素数；0和1不是素数。这并不是筛法的实现。

## 代码

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

## 运行与较小的上限

保存为 `primes.rs`，使用 `rustc --edition=2021 primes.rs -o primes` 编译。在Windows上，将可执行文件名指定为 `primes.exe`。运行后输出168行，首个数为2，最后一个为997。这些示例已在Rust 1.90.0上运行。

`primes_up_to(0)` 和 `primes_up_to(1)` 返回空向量；`primes_up_to(2)` 返回 `[2]`，`primes_up_to(3)` 返回 `[2, 3]`，`primes_up_to(10)` 返回 `[2, 3, 5, 7]`。参数类型 `usize` 不包含负数上限。这个程序不解析标准输入。

## 判断与循环的原理

1. 上限小于2时返回空结果。否则保存2，并从3开始只检查不大于上限的奇数候选。处理候选之前就检查上限，因此上限为2时不会添加3。
2. 若候选 `n` 是合数，它有一个不大于其平方根的素因子。这些素数在处理较小候选时就已进入列表。若能整除，就将候选判为合数并停止；若尚未找到因子且已满足 `p > n / p`，则无须继续试除。这里用正整数除法表示平方根条件，不计算 `p * p`，也不使用浮点平方根。
3. `for &p in &primes` 借用列表，依次取得引用，并将每个 `usize` 值复制到 `p`。只在这个循环结束之后才添加新素数。最后的 `for p in primes_up_to(1000)` 则从返回的向量中取出值并输出。[Rust的Vec文档](https://doc.rust-lang.org/std/vec/struct.Vec.html)说明了借用迭代与拥有所有权时的迭代之间的区别。
4. 在 `n <= max` 的循环体内，`max - n` 不会为负。剩余距离小于2时，在加法之前退出；否则才执行 `n += 2`，从而避免增加后的值超过上限。

## 适用范围

原来的固定上限1000程序也能正确输出168个素数。但若只将上限改成0、1或2，因为没有在处理前检查上限，就会输出范围外的2或3。这里将代码整理为可复用函数，并处理这些边界。

列表为每个已找到的素数保存一个 `usize`，向量的管理信息和分配容量也需要内存。将一次除法计为一个操作时，试除次数的粗略上界可写为 `O(max sqrt(max))`；这不是实测时间或位复杂度。上限越大，所需时间和存储越多，不能保证快速列举任意大上限以内的素数。列举较大范围时，也可参阅[埃拉托斯特尼筛法文章](https://kenji.blog/zh-cn/p/%E5%9F%83%E6%8B%89%E6%89%98%E6%96%AF%E7%89%B9%E5%B0%BC%E7%AD%9B%E6%B3%95%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A61000%E4%BB%A5%E4%B8%8B%E3%81%AE%E7%B4%A0%E6%95%B0%E3%82%92%E5%88%97%E6%8C%99%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/)。这不是密码学素数生成器。
