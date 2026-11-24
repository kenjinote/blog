---le: 'Mathematica入門：方程式・微分積分など基本コマンドの使い方'
slug: "Mathematica入門"
date: 2024-07-25T01:36:19+09:00
tags: ["Mathematica", "数学", "アルゴリズム"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: '初心者向けにMathematicaの基本的な使い方と計算コマンドを解説します。方程式や連立方程式の解法（Solve）、不等式（Reduce）、微分（D）、積分（Integrate）、行列計算など、よく使う関数の具体例をまとめました。'
lastmod: "2026-11-24T00:00:00+09:00"

---
# Mathematica入門

## 方程式を解く

```
Solve[x^2 - 3 x + 2 == 0, x]
```

出力
```
{{x -> 1}, {x -> 2}}
```

## 整数の範囲で方程式の解を求める
```
Solve[x^2 - 3 x + 2 == 0 && 0 <= x <= 2, x, Integers]
```
出力
```
{{x -> 1}, {x -> 2}}
```

## 連立方程式を解く
```
Solve[{x + y == 3, x - y == 1}, {x, y}]
```
出力
```
{{x -> 2, y -> 1}}
```

## 不等式を解く
```
Reduce[x^2 - 3 x + 2 > 0, x]
```
出力
```
x < 1 || x > 2
```

## 微分する
```
D[x^2, x]
```
出力
```
2 x
```

## 積分する
```
Integrate[x^2, x]
```
出力
```
x^3/3
```

## 極限を求める
```
Limit[1/x, x -> 0, Direction -> "FromAbove"]
```
出力
```
Infinity
```

xを0の右側から近づけた極限はInfinityです。実数の両側極限は存在しません。Directionで近づく向きを指定できます。

## 級数を求める
```
Sum[1/n^2, {n, 1, Infinity}]
```
出力
```
π^2/6
```

## 行列を作成する
```
m = {{1, 2}, {3, 4}}
```

## 行列の積を求める
```
m . m
```
出力
```
{{7, 10}, {15, 22}}
```

## 逆行列を求める
```
Inverse[m]
```
出力
```
{{-2, 1}, {3/2, -1/2}}
```

## [固有値と固有ベクトル](https://kenji.blog/p/eigenvalues-and-eigenvectors/)を求める
```
Eigensystem[m]
```
出力
```
{{(5 + Sqrt[33])/2, (5 - Sqrt[33])/2}, {{2, (3 + Sqrt[33])/2}, {2, (3 - Sqrt[33])/2}}}
```

この行列の固有値は(5±√33)/2です。固有ベクトルの順序や倍率は出力で異なる場合がありますが、各組はm.v=λvを満たします。

## ベクトルの内積を求める
```
{1, 2} . {3, 4}
```
出力
```
11
```

## ベクトルの外積を求める
```
Cross[{1, 2, 3}, {4, 5, 6}]
```
出力
```
{-3, 6, -3}
```

## ベクトルの大きさを求める
```
Norm[{1, 2, 3}]
```
出力
```
√14
```

## ベクトルの角度を求める
```
ArcCos[{1, 2} . {3, 4}/(Norm[{1, 2}] Norm[{3, 4}])]
```

出力
```
ArcCos[11/(√5 √25)]
```

## ベクトルの射影を求める
```
Projection[{1, 2}, {3, 4}]
```
出力
```
{33/25, 44/25}
```

{1,2}を{3,4}へ正射影すると、係数は内積比11/25となり、結果は{33/25,44/25}です。







## ベクトルの回転を求める
```
RotationMatrix[π/2].{1, 0}
```

出力
```
{0, 1}
```

## ベクトルの平行移動を求める
```
TranslationTransform[{1, 2}][{3, 4}]
```
出力
```
{4, 6}
```

## ベクトルの拡大縮小を求める
```
ScalingTransform[{2, 3}][{1, 1}]
```
出力
```
{2, 3}
```

## ベクトルの反転を求める
```
ReflectionTransform[{0, 1}][{1, 1}]
```
出力
```
{1, -1}
```

ReflectionTransformの第1引数は鏡面の法線です。法線{0,1}はx軸を表し、{1,1}を{1,-1}へ写します。

乱数の出力例は説明用で、評価のたびに変わります。RandomInteger[]は0または1を返します。SeedRandomは同じ乱数生成器・バージョンで系列を再現するために使います。









## 乱数を生成する
```
RandomReal[]
```


出力
```
0.123456
```

## 乱数を生成する（整数）
```
RandomInteger[]
```
出力
```
0
```

## 乱数を生成する（範囲指定）
```
RandomReal[{1, 10}]
```
出力
```
5.6789
```

## 乱数を生成する（整数、範囲指定）
```
RandomInteger[{1, 10}]
```
出力
```
5
```

## 乱数を生成する（分布指定）
```
RandomVariate[NormalDistribution[0, 1]]
```
出力
```
0.123456
```

## 乱数を生成する（分布指定、個数指定）
```
RandomVariate[NormalDistribution[0, 1], 10]
```
出力
```
{0.123456, 0.234567, 0.345678, 0.456789, 0.567890, 0.678901, 0.789012, 0.890123, 0.901234, 0.012345}
```

## 乱数を生成する（分布指定、個数指定、シード指定）
```
SeedRandom[12345]
RandomVariate[NormalDistribution[0, 1], 10]
```
出力
```
(* Output intentionally omitted: exact sequence depends on the Wolfram Language version. *)
```

## 配列の要素に関数を適用する
```
Map[Sqrt, {1, 4, 9}]
Sqrt /@ {1, 4, 9}
Map[#^(1/2)&, {1, 4, 9}]
```
出力
```
{1, 2, 3}
```

## ラムダ式を使って関数を定義する
```
f = Function[x, x^2]
f[3]
```
出力
```
9
```

## 関数を合成する
```
f = Function[x, x^2]
g = Function[x, x + 1]
h = Function[x, f[g[x]]]
h[3]
```
出力
```
16
```

## 直前の計算結果を参照する
```
% + 1
```
出力
```
17
```

## 純関数
```
(#+3)&[5]
```
出力
```
8
```

## 配列の抽出
```
Select[{1, 2, 3, 4, 5}, EvenQ]
Select[{1, 2, 3, 4, 5}, Mod[#,2]==0&]
```
出力
```
{2, 4}
```



## 関数の公式資料

[Solve](https://reference.wolfram.com/language/ref/Solve.html) · [Reduce](https://reference.wolfram.com/language/ref/Reduce.html) · [D](https://reference.wolfram.com/language/ref/D.html) · [Integrate](https://reference.wolfram.com/language/ref/Integrate.html) · [Limit](https://reference.wolfram.com/language/ref/Limit.html) · [Sum](https://reference.wolfram.com/language/ref/Sum.html) · [Inverse](https://reference.wolfram.com/language/ref/Inverse.html) · [Eigensystem](https://reference.wolfram.com/language/ref/Eigensystem.html) · [Projection](https://reference.wolfram.com/language/ref/Projection.html) · [RotationMatrix](https://reference.wolfram.com/language/ref/RotationMatrix.html) · [ReflectionTransform](https://reference.wolfram.com/language/ref/ReflectionTransform.html) · [RandomReal](https://reference.wolfram.com/language/ref/RandomReal.html) · [RandomInteger](https://reference.wolfram.com/language/ref/RandomInteger.html) · [RandomVariate](https://reference.wolfram.com/language/ref/RandomVariate.html)
