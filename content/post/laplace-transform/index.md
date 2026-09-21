---
title: "ラプラス変換：難しい微分方程式を「代数方程式」に変換して解く技術"
description: "ラプラス変換の基礎から微分方程式への応用までを徹底解説。時間領域と複素周波数領域を行き来する強力な数学的ツールの本質に迫ります。"
slug: "laplace-transform"
date: "2026-09-20T14:40:00+09:00"
image: "eyecatch.jpg"
categories:
  - "mathematics"
tags:
  - "ラプラス変換"
  - "微分方程式"
  - "応用数学"
---

## はじめに：[ラプラス変換](https://kenji.blog/p/laplace-transform/)とは何か？

物理学や工学、あるいは経済学など、時間とともに変化する現象を記述する際に **微分方程式** は欠かせないツールです。しかし、複雑な微分方程式をそのまま解くことは非常に困難な場合があります。そこで登場するのが **[ラプラス変換](https://kenji.blog/p/laplace-transform/)** ([Laplace Transform](https://kenji.blog/p/laplace-transform/)) です。

[ラプラス変換](https://kenji.blog/p/laplace-transform/)は、簡単に言えば「難しい微分方程式を、簡単な代数方程式（四則演算だけで解ける方程式）に変換する魔法のツール」です。時間領域（$t$）で表現された複雑な問題を、複素周波数領域（$s$）へと写像し、そこで簡単に解を求めた後、再び時間領域に戻すという手順を踏みます。

この記事では、[ラプラス変換](https://kenji.blog/p/laplace-transform/)の基礎から、その強力な性質、そして実際に微分方程式を解く具体的な手順までを詳細に解説します。

## [ラプラス変換](https://kenji.blog/p/laplace-transform/)の定義

時間 $t \ge 0$ で定義された実数値関数 $f(t)$ に対する[ラプラス変換](https://kenji.blog/p/laplace-transform/) $\mathcal{L}\{f(t)\}$ は、次のような広義積分で定義されます。

$$
F(s) = \mathcal{L}\{f(t)\} = \int_{0}^{\infty} f(t) e^{-st} dt
$$

ここで、$s$ は複素数の変数（複素周波数）であり、$s = \sigma + j\omega$ （$j$ は虚数単位）と表されます。変換後の関数 $F(s)$ は $s$ の関数となります。

この積分が無限大に発散せず、有限な値として存在する（収束する）ためには、$s$ の実部 $\sigma$ がある値より大きくなければなりません。この条件を満たす領域を **収束領域** と呼びます。

## なぜ[ラプラス変換](https://kenji.blog/p/laplace-transform/)が便利なのか？

[ラプラス変換](https://kenji.blog/p/laplace-transform/)が微分方程式の解法において極めて強力な理由は、主に以下の2点にあります。

1. **微分が「掛け算」に変わる**：時間領域での微分操作 $d/dt$ が、$s$ 領域では「$s$ を掛ける」という単純な代数操作に変換されます。
2. **初期条件が自然に組み込まれる**：変換の公式の中に $f(0)$ などの初期値が含まれるため、初期条件を後から代入する手間が省け、計算ミスを減らすことができます。

## 重要な[ラプラス変換](https://kenji.blog/p/laplace-transform/)の性質

[ラプラス変換](https://kenji.blog/p/laplace-transform/)には、計算を劇的に簡単にするいくつかの重要な性質があります。

### 1. 線形性 (Linearity)

定数 $a, b$ と関数 $f(t), g(t)$ に対して、以下の関係が成り立ちます。

$$
\mathcal{L}\{a f(t) + b g(t)\} = a \mathcal{L}\{f(t)\} + b \mathcal{L}\{g(t)\}
$$

### 2. 第一移動定理 (First Shifting Theorem)

関数 $f(t)$ に指数関数 $e^{at}$ が掛けられている場合、$s$ 領域では平行移動として現れます。

$$
\mathcal{L}\{e^{at} f(t)\} = F(s - a)
$$

### 3. 微分の[ラプラス変換](https://kenji.blog/p/laplace-transform/)

これが微分方程式を解くための最重要公式です。

- **一階微分**: $\mathcal{L}\{f'(t)\} = s F(s) - f(0)$
- **二階微分**: $\mathcal{L}\{f''(t)\} = s^2 F(s) - s f(0) - f'(0)$

このように、微分の階数が上がるごとに $s$ の次数が上がり、初期値が引き算されていく形になります。

## 基本的な関数の変換表

よく使われる基本的な関数の[ラプラス変換](https://kenji.blog/p/laplace-transform/)をいくつか紹介します。これらは公式として覚えておくと便利です。

| 時間領域 $f(t)$ | $s$ 領域 $F(s)$ |
| :--- | :--- |
| $1$ (単位ステップ関数) | $\frac{1}{s}$ |
| $t$ | $\frac{1}{s^2}$ |
| $e^{at}$ | $\frac{1}{s - a}$ |
| $\sin(\omega t)$ | $\frac{\omega}{s^2 + \omega^2}$ |
| $\cos(\omega t)$ | $\frac{s}{s^2 + \omega^2}$ |

## 微分方程式の解法ステップ

[ラプラス変換](https://kenji.blog/p/laplace-transform/)を用いて微分方程式を解く手順は、非常にシステマティックです。以下のフローチャートにその全体像を示します。

```mermaid
flowchart TD
  A["時間領域の微分方程式"] -->|"ラプラス変換を実行"| B["s領域の代数方程式"]
  B -->|"代数的計算（整理）"| C["s領域の解 F("s")"]
  C -->|"逆ラプラス変換を実行"| D["時間領域の解 f("t")"]
```

1. **[ラプラス変換](https://kenji.blog/p/laplace-transform/)を実行**：与えられた微分方程式の両辺を[ラプラス変換](https://kenji.blog/p/laplace-transform/)します。ここで初期条件を代入します。
2. **$s$ 領域の代数方程式を解く**：未知の関数 $F(s)$ について、単なる代数方程式として解きます（移項や割り算など）。
3. **逆[ラプラス変換](https://kenji.blog/p/laplace-transform/)を実行**：得られた $F(s)$ を部分分数分解などを用いて基本的な関数の形に変形し、逆[ラプラス変換](https://kenji.blog/p/laplace-transform/) $\mathcal{L}^{-1}$ を行って時間領域の関数 $f(t)$ に戻します。

## 具体例：RC回路の過渡応答

簡単な例として、抵抗 $R$ とコンデンサ $C$ を直列に接続したRC回路に、直流電圧 $E$ をかけた場合の電荷 $q(t)$ の変化を求めてみましょう。

回路方程式は以下のようになります。

$$
R \frac{dq(t)}{dt} + \frac{1}{C} q(t) = E
$$

初期条件を $q(0) = 0$ とします。

**ステップ1：[ラプラス変換](https://kenji.blog/p/laplace-transform/)**
両辺を[ラプラス変換](https://kenji.blog/p/laplace-transform/)します。$q(t)$ の[ラプラス変換](https://kenji.blog/p/laplace-transform/)を $Q(s)$ とします。

$$
R (s Q(s) - q(0)) + \frac{1}{C} Q(s) = \frac{E}{s}
$$

$q(0) = 0$ なので、方程式は次のように簡略化されます。

$$
\left(R s + \frac{1}{C}\right) Q(s) = \frac{E}{s}
$$

**ステップ2：代数的計算**
これを $Q(s)$ について解きます。

$$
Q(s) = \frac{E / s}{R s + \frac{1}{C}} = \frac{E}{R s \left(s + \frac{1}{RC}\right)}
$$

逆[ラプラス変換](https://kenji.blog/p/laplace-transform/)しやすいように、部分分数分解を行います。

$$
Q(s) = C E \left( \frac{1}{s} - \frac{1}{s + \frac{1}{RC}} \right)
$$

**ステップ3：逆[ラプラス変換](https://kenji.blog/p/laplace-transform/)**
変換表を用いて、時間領域に戻します。$\frac{1}{s}$ は $1$ に、$\frac{1}{s + a}$ は $e^{-at}$ に戻ることを利用します。

$$
q(t) = C E \left( 1 - e^{-\frac{t}{RC}} \right)
$$

これが求める解です。最初は電荷が $0$ で、時間が経つにつれて徐々に $CE$ に漸近していく様子が、複雑な微積分を直接解くことなく導き出せました。

## まとめ

[ラプラス変換](https://kenji.blog/p/laplace-transform/)は、一見すると抽象的で難解な概念に思えるかもしれません。しかし、「微分を掛け算に変換する」という強力な性質により、工学や物理学における複雑なシステム解析を劇的に単純化する不可欠なツールです。

まずは基本的な変換表を理解し、簡単な微分方程式から手を動かして解いてみることで、この「魔法の手法」の真の価値を実感できるはずです。
