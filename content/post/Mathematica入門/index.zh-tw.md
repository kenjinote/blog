---
title: 'Mathematica 入門：方程式、微積分等基本指令的使用方法'
slug: "Mathematica入門"
date: 2024-07-25T01:36:19+09:00
tags: ["Mathematica", "數學", "演算法"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: '為初學者說明 Mathematica 的基本使用方法與計算指令。整理了方程式與聯立方程式的解法 (Solve)、不等式 (Reduce)、微分 (D)、積分 (Integrate) 及矩陣計算等常用函數的具體範例。'
lastmod: "2026-11-24T00:00:00+09:00"
mermaid: true
---
# Mathematica 入門

## 解方程式

```
Solve[x^2 - 3 x + 2 == 0, x]
```

輸出
```
{{x -> 1}, {x -> 2}}
```

## 在整數範圍內求方程式的解
```
Solve[x^2 - 3 x + 2 == 0 && 0 <= x <= 2, x, Integers]
```
輸出
```
{{x -> 1}, {x -> 2}}
```

## 解聯立方程式
```
Solve[{x + y == 3, x - y == 1}, {x, y}]
```
輸出
```
{{x -> 2, y -> 1}}
```

## 解不等式
```
Reduce[x^2 - 3 x + 2 > 0, x]
```
輸出
```
x < 1 || x > 2
```

## 微分
```
D[x^2, x]
```
輸出
```
2 x
```

## 積分
```
Integrate[x^2, x]
```
輸出
```
x^3/3
```

## 求極限
```
Limit[1/x, x -> 0, Direction -> "FromAbove"]
```
輸出
```
Infinity
```

x 從右側趨近 0 時，極限為 Infinity。雙側實數極限不存在。可用 Direction 指定單側趨近方向。

## 求級數
```
Sum[1/n^2, {n, 1, Infinity}]
```
輸出
```
π^2/6
```

## 建立矩陣
```
m = {{1, 2}, {3, 4}}
```

## 求矩陣乘積
```
m . m
```
輸出
```
{{7, 10}, {15, 22}}
```

## 求反矩陣
```
Inverse[m]
```
輸出
```
{{-2, 1}, {3/2, -1/2}}
```

## 求[特徵值與特徵向量](https://kenji.blog/zh-tw/p/eigenvalues-and-eigenvectors/)
```
Eigensystem[m]
```
輸出
```
{{(5 + Sqrt[33])/2, (5 - Sqrt[33])/2}, {{2, (3 + Sqrt[33])/2}, {2, (3 - Sqrt[33])/2}}}
```

此矩陣的特徵值為 (5±√33)/2。特徵向量的順序或倍數可能不同，但每組值與向量都滿足 m.v=λv。

## 求向量內積
```
{1, 2} . {3, 4}
```
輸出
```
11
```

## 求向量外積
```
Cross[{1, 2, 3}, {4, 5, 6}]
```
輸出
```
{-3, 6, -3}
```

## 求向量的大小
```
Norm[{1, 2, 3}]
```
輸出
```
√14
```

## 求向量的角度
```
ArcCos[{1, 2} . {3, 4}/(Norm[{1, 2}] Norm[{3, 4}])]
```

輸出
```
ArcCos[11/(√5 √25)]
```

## 求向量的投影
```
Projection[{1, 2}, {3, 4}]
```
輸出
```
{33/25, 44/25}
```

將 {1,2} 正交投影到 {3,4} 時，係數為內積比 11/25，結果是 {33/25,44/25}。







## 求向量的旋轉
```
RotationMatrix[π/2].{1, 0}
```

輸出
```
{0, 1}
```

## 求向量的平移
```
TranslationTransform[{1, 2}][{3, 4}]
```
輸出
```
{4, 6}
```

## 求向量的縮放
```
ScalingTransform[{2, 3}][{1, 1}]
```
輸出
```
{2, 3}
```

## 求向量的反射
```
ReflectionTransform[{0, 1}][{1, 1}]
```
輸出
```
{1, -1}
```

ReflectionTransform 的第一個引數是鏡面的法向量。法向量 {0,1} 代表 x 軸，因此 {1,1} 會映射為 {1,-1}。

下方亂數輸出僅供示例，每次計算都會改變。RandomInteger[] 會回傳 0 或 1。SeedRandom 可在相同產生器與版本下重現亂數序列。









## 產生亂數
```
RandomReal[]
```


輸出
```
0.123456
```

## 產生亂數（整數）
```
RandomInteger[]
```
輸出
```
0
```

## 產生亂數（指定範圍）
```
RandomReal[{1, 10}]
```
輸出
```
5.6789
```

## 產生亂數（整數、指定範圍）
```
RandomInteger[{1, 10}]
```
輸出
```
5
```

## 產生亂數（指定分佈）
```
RandomVariate[NormalDistribution[0, 1]]
```
輸出
```
0.123456
```

## 產生亂數（指定分佈、指定數量）
```
RandomVariate[NormalDistribution[0, 1], 10]
```
輸出
```
{0.123456, 0.234567, 0.345678, 0.456789, 0.567890, 0.678901, 0.789012, 0.890123, 0.901234, 0.012345}
```

## 產生亂數（指定分佈、指定數量、指定種子）
```
SeedRandom[12345]
RandomVariate[NormalDistribution[0, 1], 10]
```
輸出
```
(* Output intentionally omitted: exact sequence depends on the Wolfram Language version. *)
```

## 將函數套用至陣列元素
```
Map[Sqrt, {1, 4, 9}]
Sqrt /@ {1, 4, 9}
Map[#^(1/2)&, {1, 4, 9}]
```
輸出
```
{1, 2, 3}
```

## 使用 [Lambda](https://kenji.blog/zh-tw/p/serverless-architecture-aws-lambda-cold-start/) 運算式定義函數
```
f = Function[x, x^2]
f[3]
```
輸出
```
9
```

## 合成函數
```
f = Function[x, x^2]
g = Function[x, x + 1]
h = Function[x, f[g[x]]]
h[3]
```
輸出
```
16
```

## 參考前一次的計算結果
```
% + 1
```
輸出
```
17
```

## 純函數
```
(#+3)&[5]
```
輸出
```
8
```

## 擷取陣列
```
Select[{1, 2, 3, 4, 5}, EvenQ]
Select[{1, 2, 3, 4, 5}, Mod[#,2]==0&]
```
輸出
```
{2, 4}
```


## 函數官方文件

[Solve](https://reference.wolfram.com/language/ref/Solve.html) · [Reduce](https://reference.wolfram.com/language/ref/Reduce.html) · [D](https://reference.wolfram.com/language/ref/D.html) · [Integrate](https://reference.wolfram.com/language/ref/Integrate.html) · [Limit](https://reference.wolfram.com/language/ref/Limit.html) · [Sum](https://reference.wolfram.com/language/ref/Sum.html) · [Inverse](https://reference.wolfram.com/language/ref/Inverse.html) · [Eigensystem](https://reference.wolfram.com/language/ref/Eigensystem.html) · [Projection](https://reference.wolfram.com/language/ref/Projection.html) · [RotationMatrix](https://reference.wolfram.com/language/ref/RotationMatrix.html) · [ReflectionTransform](https://reference.wolfram.com/language/ref/ReflectionTransform.html) · [RandomReal](https://reference.wolfram.com/language/ref/RandomReal.html) · [RandomInteger](https://reference.wolfram.com/language/ref/RandomInteger.html) · [RandomVariate](https://reference.wolfram.com/language/ref/RandomVariate.html)
