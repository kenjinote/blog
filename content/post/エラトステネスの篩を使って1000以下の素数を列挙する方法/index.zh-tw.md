---
title: "如何使用埃拉托斯特尼篩法列出1000以下的質數"
slug: "如何使用埃拉托斯特尼篩法列出1000以下的質數"
date: 2023-04-09T12:54:24+09:00
tags: ["埃拉托斯特尼篩法", "質數", "數學", "Rust"]
draft: false
math: true
image: "img.png"
categories: ["數學・密碼學・量子"]
---

## 什麼是埃拉托斯特尼篩法

埃拉托斯特尼篩法是一種用來找出一定範圍內所有質數的演算法。
演算法很簡單，可以透過以下步驟實現：

1. 建立一個包含 N 個元素的布林值陣列，並將所有元素初始化為 true。
2. 將陣列的第 0 個和第 1 個元素設為 false（因為 0 和 1 不是質數）。
3. 如果陣列的第 2 個元素為 true，則輸出 2 為質數。
4. 將陣列中 $2^2$ 以上的 2 的倍數對應的元素全部設為 false ※
5. 如果陣列的第 3 個元素為 true，則輸出 3 為質數。
6. 將陣列中 $3^2$ 以上的 3 的倍數對應的元素全部設為 false。
7. 對於第 4 個、第 5 個，……直到第 N 個元素，重複相同的處理。

※ 將平方以上的元素設為 false 的原因在於，小於平方的數字已經被處理過（列舉已完成）。

![](Animation_Sieb_des_Eratosthenes.gif)


## Rust 實作

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

## 稍微最佳化版本

考慮到以下幾點，我們進行稍微最佳化的實作：

- 將陣列初始化為 false 而不是 true（這樣速度更快）。
- 因為 2 的倍數不是質數，所以省略將 2 的倍數設為 false 的處理。
- 不需要迴圈到 n，只需列舉到 n 的平方根為止的質數，就能找出所有小於等於 n 的質數。

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

## 參考資料
- [埃拉托斯特尼篩法](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE%E7%AF%A9)
