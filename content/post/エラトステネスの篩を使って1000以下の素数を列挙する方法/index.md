---
title: 'エラトステネスの篩とは？1000以下の素数を列挙するアルゴリズムと実装'
slug: "エラトステネスの篩を使って1000以下の素数を列挙する方法"
tags: ["エラトステネスの篩", "素数", "数学", "Rust"]
draft: false
math: true
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "エラトステネスの篩で1000以下の素数168個を列挙します。Rustの基本版と奇数候補の版、平方から始める理由、0・1の境界、計算量とメモリの制限を説明します。"
date: 2023-04-09T12:54:24+09:00
lastmod: 2026-10-29
---

エラトステネスの篩は、上限 `n` 以下の素数をまとめて列挙するアルゴリズムです。ここではRustで1000以下の素数168個を出力します。上限も範囲に含み、0と1は素数に含めません。

## 篩の手順と、平方から始める理由

1. 添字0から `n` までを使うため、`n + 1` 要素の真偽値配列を用意します。基本版では真で初期化し、0と1を偽にします。上限が2未満なら、配列の添字1へ触れる前に空の結果を返します。
2. 2から順に候補 `p` を調べます。まだ真なら素数なので、$p^2$ から `p` ずつ増やした倍数を偽にします。`p` 自身は消しません。
3. 倍数を消す処理は $p^2\le n$ の候補までで十分です。合成数には平方根以下の素因数があるからです。
4. 最後に2から `n` までを走査し、真のまま残った数をすべて出力します。出力する範囲を平方根以下に制限するわけではありません。

$p^2$ 未満の倍数 $kp$（$2\le k<p$）は、`k` の素因数が `p` より小さいため、その素因数の段階で消されています。「平方より小さい数の列挙がすべて完了したから」という意味ではありません。

![2から120までの数で篩の手順を示すアニメーション](Animation_Sieb_des_Eratosthenes.gif)

図：SKopp（Suricataによる更新版）、[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Animation_Sieb_des_Eratosthenes.gif)、[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)。ファイルは改変していません。図の範囲は2から120で、以下のコードの上限1000とは異なります。

## Rustの基本実装

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

`sieve.rs` として保存し、`rustc --edition=2021 sieve.rs -o sieve` でコンパイルします。Windowsでは実行ファイル名を `sieve.exe` にします。実行すると168行を出力し、最初の数は2、最後は997です。Rust 1.90.0で実行を確認した例です。

`sieve(0)` と `sieve(1)` は空のベクタ、`sieve(2)` は `[2]` を返します。`p <= n / p` により、平方が上限以下のときだけ `p * p` を計算します。また、残りの距離を確認してから倍数を加算します。浮動小数点の平方根を使う必要はありません。

## 奇数の候補だけを消す実装

2より大きい偶数は合成数なので、2だけを真にし、奇数を候補として初期化できます。奇数の素数 `p` では、平方も奇数です。そこから $2p$ ずつ進めると、奇数の倍数だけを消せます。

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

こちらは別のファイルに保存してコンパイルします。基本版と同じ168個を出力し、0・1では空、2では `[2]` を返します。二つの `main` を同じファイルへまとめないでください。

この版は偶数を処理する一部の作業を省きます。ただし、「偽で初期化すれば常に速い」という保証はありません。初期化・書き込み・メモリアクセスの費用、コンパイラや対象機械によって実行時間は変わります。ここでは速度の比較測定はしていません。また、添字を数値と対応させるため、配列自体は引き続き `n + 1` 要素です。

## 計算量と扱える範囲

通常のRAMモデルで篩の時間計算量は $O(n\log\log n)$、フラグ用の記憶領域は $O(n)$ です。これは漸近的な操作数の評価で、実測時間や任意精度整数のビット計算量ではありません。[Princetonの解析教材](https://introcs.cs.princeton.edu/java/41analysis/)の篩の設問にも、この成長率が示されています。

Rustの [`bool`](https://doc.rust-lang.org/reference/types/boolean.html) は1バイトで、[`Vec<T>`](https://doc.rust-lang.org/std/vec/struct.Vec.html#guarantees) は要素を連続して保持します。この `Vec<bool>` はビット圧縮配列ではありません。フラグの論理的な要素数は `n + 1` で、ベクタの管理情報・確保容量や、返す `Vec<usize>` の領域も別に必要です。

`checked_add` は `n + 1` を表現できない場合に、このコードでは明示的にpanicさせます。それ以外でも十分なメモリを確保できることが必要で、任意に大きい上限まで扱えるわけではありません。大きな区間には分割篩などを検討します。単一の大きな整数の素数判定とは用途が異なります。
