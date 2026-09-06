---
title: '使用埃拉托斯特尼筛法列举1000以下的素数'
slug: "エラトステネスの篩を使って1000以下の素数を列挙する方法"
date: 2023-04-09T12:54:24+09:00
tags: ["埃拉托斯特尼筛法", "素数", "数学", "Rust"]
draft: false
math: true
image: "img.png"
categories: ["数学・密码・量子"]
---

## 什么是埃拉托斯特尼筛法

埃拉托斯特尼筛法是一种用于列举小于等于某个数值的所有素数的算法。
算法非常简单，可以通过以下步骤实现：

1. 创建一个包含 N 个元素的 bool 值数组，并将所有元素初始化为 true
2. 将数组的第 0 个和第 1 个元素设为 false（因为 0 和 1 不是素数）
3. 如果数组的第 2 个元素为 true，则将 2 作为素数输出
4. 将数组中 $2^2$ 及以上的所有 2 的倍数位置的元素设为 false※
5. 如果数组的第 3 个元素为 true，则将 3 作为素数输出
6. 将数组中 $3^2$ 及以上的所有 3 的倍数位置的元素设为 false
7. 对于第 4 个、第 5 个、……、第 N 个元素，重复相同的处理

※ 之所以将平方以上的元素作为 false 的目标，是因为小于平方的数已经被处理过（列举已完成）。

![](Animation_Sieb_des_Eratosthenes.gif)


## Rust 中的实现

```
fn main() {
    let n = 1000;
    let mut is_prime = vec![true; n+1];
    is_prime[0] = false;
    is_prime[1] = false;
    for i in 2..=n {
        if is_prime[i] {
            println!("{}", i);
            let mut j = i * i;
            while j <= n {
                is_prime[j] = false;
                j += i;
            }
        }
    }
}
```

## 稍微优化的版本

考虑到以下几点，我们进行稍微优化后的实现：

- 数组不使用 true 而是使用 false 进行初始化（这样更快）
- 2 的倍数不是素数，所以省略将 2 的倍数元素设为 false 的处理
- 不需要循环到 n，只需列举到 n 的平方根即可找出 n 以下的素数

```
fn main() {
    let n = 1000;
    let mut is_prime = vec![false; n+1];
    is_prime[2] = true;
    for i in (3..=n).step_by(2) {
        is_prime[i] = true;
    }
    for i in 3..=((n as f64).sqrt() as usize) {
        if is_prime[i] {
            let mut j = i * i;
            while j <= n {
                is_prime[j] = false;
                j += i * 2;
            }
        }
    }
    for i in (2..=n).filter(|&x| is_prime[x]) {
        println!("{}", i);
    }
}
```

## 参考
- [埃拉托斯特尼筛法](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE%E7%AF%A9)
