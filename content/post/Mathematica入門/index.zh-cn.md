---le: 'Mathematica入门：方程、微积分等基本命令的使用方法'
slug: "Mathematica入門"
date: 2024-07-25T01:36:19+09:00
tags: ["Mathematica", "数学", "算法"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: '面向初学者讲解Mathematica的基本使用方法和计算命令。总结了常用的函数及具体示例，包括方程式及联立方程式的求解（Solve）、不等式（Reduce）、微分（D）、积分（Integrate）和矩阵计算等。'
lastmod: "2026-11-24T00:00:00+09:00"

---
# Mathematica入门

## 解方程

```
Solve[x^2 - 3 x + 2 == 0, x]
```

输出
```
{{x -> 1}, {x -> 2}}
```

## 在整数范围内求方程的解
```
Solve[x^2 - 3 x + 2 == 0 && 0 <= x <= 2, x, Integers]
```
输出
```
{{x -> 1}, {x -> 2}}
```

## 解方程组
```
Solve[{x + y == 3, x - y == 1}, {x, y}]
```
输出
```
{{x -> 2, y -> 1}}
```

## 解不等式
```
Reduce[x^2 - 3 x + 2 > 0, x]
```
输出
```
x < 1 || x > 2
```

## 微分
```
D[x^2, x]
```
输出
```
2 x
```

## 积分
```
Integrate[x^2, x]
```
输出
```
x^3/3
```

## 求极限
```
Limit[1/x, x -> 0, Direction -> "FromAbove"]
```
输出
```
Infinity
```

x 从右侧趋近 0 时，极限为 Infinity。双侧实数极限不存在。可以用 Direction 指定单侧趋近方向。

## 求级数
```
Sum[1/n^2, {n, 1, Infinity}]
```
输出
```
π^2/6
```

## 创建矩阵
```
m = {{1, 2}, {3, 4}}
```

## 求矩阵乘积
```
m . m
```
输出
```
{{7, 10}, {15, 22}}
```

## 求逆矩阵
```
Inverse[m]
```
输出
```
{{-2, 1}, {3/2, -1/2}}
```

## 求[特征值与特征向量](https://kenji.blog/zh-cn/p/eigenvalues-and-eigenvectors/)
```
Eigensystem[m]
```
输出
```
{{(5 + Sqrt[33])/2, (5 - Sqrt[33])/2}, {{2, (3 + Sqrt[33])/2}, {2, (3 - Sqrt[33])/2}}}
```

此矩阵的特征值为 (5±√33)/2。特征向量的顺序或倍数可能不同，但每组值与向量都满足 m.v=λv。

## 求向量的点积
```
{1, 2} . {3, 4}
```
输出
```
11
```

## 求向量的叉积
```
Cross[{1, 2, 3}, {4, 5, 6}]
```
输出
```
{-3, 6, -3}
```

## 求向量的模（大小）
```
Norm[{1, 2, 3}]
```
输出
```
√14
```

## 求向量的夹角
```
ArcCos[{1, 2} . {3, 4}/(Norm[{1, 2}] Norm[{3, 4}])]
```

输出
```
ArcCos[11/(√5 √25)]
```

## 求向量的投影
```
Projection[{1, 2}, {3, 4}]
```
输出
```
{33/25, 44/25}
```

将 {1,2} 正交投影到 {3,4} 时，系数为内积之比 11/25，结果是 {33/25,44/25}。







## 求向量的旋转
```
RotationMatrix[π/2].{1, 0}
```

输出
```
{0, 1}
```

## 求向量的平移
```
TranslationTransform[{1, 2}][{3, 4}]
```
输出
```
{4, 6}
```

## 求向量的缩放
```
ScalingTransform[{2, 3}][{1, 1}]
```
输出
```
{2, 3}
```

## 求向量的反转（反射）
```
ReflectionTransform[{0, 1}][{1, 1}]
```
输出
```
{1, -1}
```

ReflectionTransform 的第一个参数是镜面的法向量。法向量 {0,1} 表示 x 轴，因此 {1,1} 映射为 {1,-1}。

下方随机数输出仅作示例，每次计算都会变化。RandomInteger[] 返回 0 或 1。SeedRandom 可在相同生成器和版本下重现随机序列。









## 生成随机数
```
RandomReal[]
```


输出
```
0.123456
```

## 生成随机数（整数）
```
RandomInteger[]
```
输出
```
0
```

## 生成随机数（指定范围）
```
RandomReal[{1, 10}]
```
输出
```
5.6789
```

## 生成随机数（整数、指定范围）
```
RandomInteger[{1, 10}]
```
输出
```
5
```

## 生成随机数（指定分布）
```
RandomVariate[NormalDistribution[0, 1]]
```
输出
```
0.123456
```

## 生成随机数（指定分布、指定数量）
```
RandomVariate[NormalDistribution[0, 1], 10]
```
输出
```
{0.123456, 0.234567, 0.345678, 0.456789, 0.567890, 0.678901, 0.789012, 0.890123, 0.901234, 0.012345}
```

## 生成随机数（指定分布、指定数量、指定种子）
```
SeedRandom[12345]
RandomVariate[NormalDistribution[0, 1], 10]
```
输出
```
(* Output intentionally omitted: exact sequence depends on the Wolfram Language version. *)
```

## 对数组元素应用函数
```
Map[Sqrt, {1, 4, 9}]
Sqrt /@ {1, 4, 9}
Map[#^(1/2)&, {1, 4, 9}]
```
输出
```
{1, 2, 3}
```

## 使用[Lambda](https://kenji.blog/zh-cn/p/serverless-architecture-aws-lambda-cold-start/)表达式定义函数
```
f = Function[x, x^2]
f[3]
```
输出
```
9
```

## 复合函数
```
f = Function[x, x^2]
g = Function[x, x + 1]
h = Function[x, f[g[x]]]
h[3]
```
输出
```
16
```

## 引用上一次的计算结果
```
% + 1
```
输出
```
17
```

## 纯函数
```
(#+3)&[5]
```
输出
```
8
```

## 数组提取
```
Select[{1, 2, 3, 4, 5}, EvenQ]
Select[{1, 2, 3, 4, 5}, Mod[#,2]==0&]
```
输出
```
{2, 4}
```


## 函数官方文档

[Solve](https://reference.wolfram.com/language/ref/Solve.html) · [Reduce](https://reference.wolfram.com/language/ref/Reduce.html) · [D](https://reference.wolfram.com/language/ref/D.html) · [Integrate](https://reference.wolfram.com/language/ref/Integrate.html) · [Limit](https://reference.wolfram.com/language/ref/Limit.html) · [Sum](https://reference.wolfram.com/language/ref/Sum.html) · [Inverse](https://reference.wolfram.com/language/ref/Inverse.html) · [Eigensystem](https://reference.wolfram.com/language/ref/Eigensystem.html) · [Projection](https://reference.wolfram.com/language/ref/Projection.html) · [RotationMatrix](https://reference.wolfram.com/language/ref/RotationMatrix.html) · [ReflectionTransform](https://reference.wolfram.com/language/ref/ReflectionTransform.html) · [RandomReal](https://reference.wolfram.com/language/ref/RandomReal.html) · [RandomInteger](https://reference.wolfram.com/language/ref/RandomInteger.html) · [RandomVariate](https://reference.wolfram.com/language/ref/RandomVariate.html)
