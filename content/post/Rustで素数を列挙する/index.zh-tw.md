---
title: '在 Rust 中列舉質數的程式建立方法與程式碼範例'
slug: "Rustで質數を列挙する"
tags: ["Rust","質數","演算法"]
draft: false
image: "images/img.webp"
categories: ["programming"]
description: "用已知質數試除，在Rust中列舉上限以下的質數。說明0、1、2的邊界、平方根截止條件、向量迭代、遞增範圍及適用情境。"
date: 2022-09-09T07:08:49+09:00
lastmod: 2026-10-29
---

這個Rust範例儲存已經找到的質數，並用它們進行試除。`primes_up_to(max)` 傳回不大於上限的質數列表，包含上限本身。1000以下有168個質數；0與1不是質數。這並不是篩法的實作。

## 程式碼

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

## 執行與較小的上限

儲存為 `primes.rs`，使用 `rustc --edition=2021 primes.rs -o primes` 編譯。在Windows上，將執行檔名稱指定為 `primes.exe`。執行後輸出168行，第一個數為2，最後一個為997。這些範例已在Rust 1.90.0上執行。

`primes_up_to(0)` 與 `primes_up_to(1)` 傳回空的向量；`primes_up_to(2)` 傳回 `[2]`，`primes_up_to(3)` 傳回 `[2, 3]`，`primes_up_to(10)` 傳回 `[2, 3, 5, 7]`。參數型別 `usize` 不包含負數上限。這個程式不解析標準輸入。

## 判斷與迴圈的原理

1. 上限小於2時傳回空的結果。否則儲存2，並從3開始只檢查不大於上限的奇數候選。處理候選之前就檢查上限，因此上限為2時不會加入3。
2. 若候選 `n` 是合數，它有一個不大於其平方根的質因數。這些質數在處理較小候選時就已經進入列表。若能整除，就將候選判為合數並停止；若尚未找到因數且已滿足 `p > n / p`，則不必繼續試除。這裡用正整數除法表示平方根條件，不計算 `p * p`，也不使用浮點數平方根。
3. `for &p in &primes` 借用列表，依序取得參考，並將每個 `usize` 值複製到 `p`。只有這個迴圈結束後才加入新質數。最後的 `for p in primes_up_to(1000)` 則從傳回的向量取出值並輸出。[Rust的Vec文件](https://doc.rust-lang.org/std/vec/struct.Vec.html)說明了借用迭代與擁有所有權時的迭代之間的差異。
4. 在 `n <= max` 的迴圈本體內，`max - n` 不會為負。剩餘距離小於2時，在加法之前結束；否則才執行 `n += 2`，避免增加後的值超過上限。

## 適用範圍

原來固定上限1000的程式也能正確輸出168個質數。不過若只將上限改成0、1或2，因為沒有在處理前檢查上限，就會輸出範圍外的2或3。這裡將程式碼整理成可重複使用的函式，並處理這些邊界。

列表為每個已找到的質數儲存一個 `usize`，向量的管理資訊與配置容量也需要記憶體。將一次除法視為一個操作時，試除次數的粗略上界可寫為 `O(max sqrt(max))`；這不是實測時間或位元複雜度。上限越大，所需時間與儲存空間越多，不能保證快速列舉任意大上限以下的質數。列舉較大範圍時，也可參閱[埃拉托斯特尼篩法文章](https://kenji.blog/zh-tw/p/%E5%9F%83%E6%8B%89%E6%89%98%E6%96%AF%E7%89%B9%E5%B0%BC%E7%AF%A9%E6%B3%95%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A61000%E4%BB%A5%E4%B8%8B%E3%81%AE%E8%B3%AA%E6%95%B8%E3%82%92%E5%88%97%E6%8C%99%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/)。這不是密碼學質數產生器。
