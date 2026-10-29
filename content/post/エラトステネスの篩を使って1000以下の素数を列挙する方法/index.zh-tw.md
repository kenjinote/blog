---
title: '什麼是埃拉托斯特尼篩法？列舉 1000 以下質數的演算法與實作'
slug: "埃拉托斯特尼篩法を使って1000以下の質數を列挙する方法"
tags: ["埃拉托斯特尼篩法", "質數", "數學", "Rust"]
draft: false
math: true
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "以Rust篩法列舉不大於1000的168個質數，說明從平方開始篩除、奇數候選、0與1的邊界、複雜度及記憶體限制。"
date: 2023-04-09T12:54:24+09:00
lastmod: 2026-10-29
---

埃拉托斯特尼篩法用來一次列舉上限 `n` 以下的所有質數，包含上限本身。這裡以Rust輸出不大於1000的168個質數。0與1不是質數。

## 篩法步驟與從平方開始的原因

1. 要使用0到 `n` 的索引，需要配置 `n + 1` 個布林元素。基本版先初始化為真，再將0與1設為假。上限小於2時，在存取索引1之前傳回空的結果。
2. 從2開始依遞增順序檢查候選 `p`。若旗標仍為真，`p` 就是質數：從 $p^2$ 開始，以 `p` 為步長將倍數設為假。不要將 `p` 本身設為假。
3. 只需對滿足 $p^2\le n$ 的候選執行篩除，因為每個合數都有一個不大於其平方根的質因數。
4. 最後掃描2到 `n`，輸出旗標仍為真的所有數。輸出範圍並不限於平方根以下。

小於 $p^2$ 的倍數 $kp$（$2\le k<p$）已經由 `k` 的某個小於 `p` 的質因數篩除。這並不代表所有較小的數都已經完成列舉。

![以2到120的數示範篩法步驟的動畫](Animation_Sieb_des_Eratosthenes.gif)

圖片：SKopp，Suricata更新版本，[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Animation_Sieb_des_Eratosthenes.gif)，[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)。檔案未經修改。圖片範圍為2到120，下方程式碼使用的上限則是1000。

## Rust基本實作

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

儲存為 `sieve.rs`，使用 `rustc --edition=2021 sieve.rs -o sieve` 編譯。在Windows上，將執行檔名稱指定為 `sieve.exe`。執行後輸出168行，第一個數為2，最後一個為997。這些範例已在Rust 1.90.0上執行。

`sieve(0)` 與 `sieve(1)` 傳回空的向量，`sieve(2)` 傳回 `[2]`。條件 `p <= n / p` 確保只在平方不超過上限時才計算 `p * p`。每次增加倍數前，也會檢查剩餘距離，因此不需要使用浮點數平方根。

## 只篩除奇數候選的實作

大於2的偶數都是合數。因此可以只將2標記為真，並將奇數初始化為候選。對於奇質數 `p`，其平方也是奇數；從平方開始以 $2p$ 為步長，就只會存取奇數倍數。

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

將這一版儲存到另一個檔案並編譯。它會輸出相同的168個質數，對0與1傳回空的結果，對2傳回 `[2]`。不要把兩個 `main` 函式放在同一個檔案中。

這一版省略了部分偶數處理，但「初始化為假就一定比較快」並無保證。初始化、寫入與記憶體存取的成本，以及編譯器和目標機器都會影響執行時間。這裡沒有進行計時比較。為了讓索引直接對應數值，陣列仍有 `n + 1` 個元素。

## 複雜度與上限的適用範圍

在一般的RAM模型下，篩法的時間複雜度為 $O(n\log\log n)$，旗標所需的儲存空間為 $O(n)$。這是漸近的操作次數與儲存量估計，並非實測時間或任意精度整數的位元複雜度。[Princeton的演算法分析教材](https://introcs.cs.princeton.edu/java/41analysis/)中的篩法習題也給出了這個成長率。

Rust的 [`bool`](https://doc.rust-lang.org/reference/types/boolean.html) 占一個位元組，[`Vec<T>`](https://doc.rust-lang.org/std/vec/struct.Vec.html#guarantees) 連續儲存元素。這裡的 `Vec<bool>` 不是位元壓縮陣列。旗標的邏輯元素個數為 `n + 1`，向量的管理資訊、配置容量與傳回的 `Vec<usize>` 也需要額外空間。

若無法表示 `n + 1`，`checked_add` 會傳回 `None`，接著由 `expect` 引發panic。其他情況也必須有足夠的可用記憶體，並不能處理任意大的上限。較大的區間可以考慮分段篩。列舉範圍內的質數，與判斷單一大整數是否為質數，適用情境不同。
