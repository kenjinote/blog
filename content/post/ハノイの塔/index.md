---
title: 'ハノイの塔'
date: 2025-04-17T22:23:14+09:00
tags: ["ハノイの塔", "アルゴリズム", "Python"]
draft: false
image: "img.png"
---

# ハノイの塔

こんにちは！

今日は「ハノイの塔」について、Pythonのサンプルプログラムを交えながら解説していきたいと思います。

---

## ハノイの塔って何？

ハノイの塔は、3本の棒と複数の円盤を使ったパズルです。円盤は大きさが異なり、最初は一つの棒に大きい順に積み重ねられています。ルールは以下の通りです：

1. 一度に動かせる円盤は1枚だけ。
2. 小さい円盤の上に大きい円盤を置くことはできません。

このパズルは、再帰的な思考を学ぶのに最適な教材とされています。再帰とは、ある問題を同じ種類のより小さな問題に分解して解決する方法です。ハノイの塔では、n枚の円盤を移動するために、n-1枚の円盤を移動するという操作を繰り返します。

---

## Pythonでハノイの塔を解いてみよう

以下は、Pythonでハノイの塔を解くためのサンプルコードです。


```python
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)

# 例: 3枚の円盤をAからCへ移動
hanoi(3, 'A', 'C', 'B')
```


このコードでは、`hanoi`関数が再帰的に呼び出され、円盤を移動する手順が表示されます。例えば、3枚の円盤の場合、以下のような出力が得られます：


```
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
```

このように、再帰的なアプローチを使うことで、複雑な問題もシンプルに解決できます。

---

## 64枚の円盤を移動するのにどれくらい時間がかかるの？

ハノイの塔の移動回数は、最小でも2^n - 1回必要です。つまり、64枚の円盤を移動するには、2^64 - 1回、約1.84×10^19回の移動が必要です。もし1秒に1回移動できたとしても、約5849億年かかります。これは、宇宙の年齢（約137億年）の約42倍です。

このように、円盤の数が増えると、必要な移動回数が指数関数的に増加します。そのため、実際に64枚の円盤を移動するのは現実的ではありません。

---

## まとめ

ハノイの塔は、再帰的な思考を学ぶのに最適なパズルです。Pythonを使えば、簡単にその解法を実装できます。しかし、円盤の数が増えると、必要な移動回数が急激に増加するため、注意が必要です。

再帰的なアプローチを理解し、実際にコードを書いてみることで、プログラミングのスキルを向上させることができます。ぜひ、ハノイの塔に挑戦してみてください。

--- 