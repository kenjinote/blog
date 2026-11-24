---




title: 'Mathematica 입문: 방정식·미분적분 등 기본 명령어 사용법'
slug: "Mathematica入門"
date: 2024-07-25T01:36:19+09:00
tags: ["Mathematica", "수학", "알고리즘"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: '초보자를 위해 Mathematica의 기본적인 사용법과 계산 명령어를 설명합니다. 방정식과 연립방정식 풀이(Solve), 부등식(Reduce), 미분(D), 적분(Integrate), 행렬 계산 등 자주 사용하는 함수의 구체적인 예를 정리했습니다.'
lastmod: "2026-11-24T00:00:00+09:00"

---








# Mathematica 입문

## 방정식 풀기

```
Solve[x^2 - 3 x + 2 == 0, x]
```

출력
```
{{x -> 1}, {x -> 2}}
```

## 정수 범위에서 방정식의 해 구하기
```
Solve[x^2 - 3 x + 2 == 0 && 0 <= x <= 2, x, Integers]
```
출력
```
{{x -> 1}, {x -> 2}}
```

## 연립방정식 풀기
```
Solve[{x + y == 3, x - y == 1}, {x, y}]
```
출력
```
{{x -> 2, y -> 1}}
```

## 부등식 풀기
```
Reduce[x^2 - 3 x + 2 > 0, x]
```
출력
```
x < 1 || x > 2
```

## 미분하기
```
D[x^2, x]
```
출력
```
2 x
```

## 적분하기
```
Integrate[x^2, x]
```
출력
```
x^3/3
```

## 극한 구하기
```
Limit[1/x, x -> 0, Direction -> "FromAbove"]
```
출력
```
Infinity
```

x가 오른쪽에서 0으로 다가갈 때 극한은 Infinity입니다. 양쪽 실수 극한은 존재하지 않습니다. Direction으로 한쪽 극한 방향을 지정할 수 있습니다.

## 급수 구하기
```
Sum[1/n^2, {n, 1, Infinity}]
```
출력
```
π^2/6
```

## 행렬 만들기
```
m = {{1, 2}, {3, 4}}
```

## 행렬의 곱 구하기
```
m . m
```
출력
```
{{7, 10}, {15, 22}}
```

## 역행렬 구하기
```
Inverse[m]
```
출력
```
{{-2, 1}, {3/2, -1/2}}
```

## 고유값과 고유벡터 구하기
```
Eigensystem[m]
```
출력
```
{{(5 + Sqrt[33])/2, (5 - Sqrt[33])/2}, {{2, (3 + Sqrt[33])/2}, {2, (3 - Sqrt[33])/2}}}
```

이 행렬의 고윳값은 (5±√33)/2입니다. 고유벡터의 순서나 배율은 다를 수 있지만 각 값과 벡터의 쌍은 m.v=λv를 만족합니다.

## 벡터의 내적 구하기
```
{1, 2} . {3, 4}
```
출력
```
11
```

## 벡터의 외적 구하기
```
Cross[{1, 2, 3}, {4, 5, 6}]
```
출력
```
{-3, 6, -3}
```

## 벡터의 크기 구하기
```
Norm[{1, 2, 3}]
```
출력
```
√14
```

## 벡터의 각도 구하기
```
ArcCos[{1, 2} . {3, 4}/(Norm[{1, 2}] Norm[{3, 4}])]
```

출력
```
ArcCos[11/(√5 √25)]
```

## 벡터의 사영 구하기
```
Projection[{1, 2}, {3, 4}]
```
출력
```
{33/25, 44/25}
```

{1,2}를 {3,4}에 정사영하면 내적 비율은 11/25이고 결과는 {33/25,44/25}입니다.







## 벡터의 회전 구하기
```
RotationMatrix[π/2].{1, 0}
```

출력
```
{0, 1}
```

## 벡터의 평행이동 구하기
```
TranslationTransform[{1, 2}][{3, 4}]
```
출력
```
{4, 6}
```

## 벡터의 확대 축소 구하기
```
ScalingTransform[{2, 3}][{1, 1}]
```
출력
```
{2, 3}
```

## 벡터의 반전 구하기
```
ReflectionTransform[{0, 1}][{1, 1}]
```
출력
```
{1, -1}
```

ReflectionTransform의 첫 번째 인수는 거울면의 법선입니다. 법선 {0,1}은 x축을 나타내며 {1,1}을 {1,-1}로 변환합니다.

아래 난수 출력은 예시이며 평가할 때마다 달라집니다. RandomInteger[]는 0 또는 1을 반환합니다. SeedRandom은 같은 생성기와 버전에서 난수열을 재현하는 데 사용합니다.









## 난수 생성하기
```
RandomReal[]
```


출력
```
0.123456
```

## 난수 생성하기 (정수)
```
RandomInteger[]
```
출력
```
0
```

## 난수 생성하기 (범위 지정)
```
RandomReal[{1, 10}]
```
출력
```
5.6789
```

## 난수 생성하기 (정수, 범위 지정)
```
RandomInteger[{1, 10}]
```
출력
```
5
```

## 난수 생성하기 (분포 지정)
```
RandomVariate[NormalDistribution[0, 1]]
```
출력
```
0.123456
```

## 난수 생성하기 (분포 지정, 개수 지정)
```
RandomVariate[NormalDistribution[0, 1], 10]
```
출력
```
{0.123456, 0.234567, 0.345678, 0.456789, 0.567890, 0.678901, 0.789012, 0.890123, 0.901234, 0.012345}
```

## 난수 생성하기 (분포 지정, 개수 지정, 시드 지정)
```
SeedRandom[12345]
RandomVariate[NormalDistribution[0, 1], 10]
```
출력
```
(* Output intentionally omitted: exact sequence depends on the Wolfram Language version. *)
```

## 배열의 요소에 함수 적용하기
```
Map[Sqrt, {1, 4, 9}]
Sqrt /@ {1, 4, 9}
Map[#^(1/2)&, {1, 4, 9}]
```
출력
```
{1, 2, 3}
```

## 람다식을 사용하여 함수 정의하기
```
f = Function[x, x^2]
f[3]
```
출력
```
9
```

## 함수 합성하기
```
f = Function[x, x^2]
g = Function[x, x + 1]
h = Function[x, f[g[x]]]
h[3]
```
출력
```
16
```

## 직전 계산 결과 참조하기
```
% + 1
```
출력
```
17
```

## 순수 함수
```
(#+3)&[5]
```
출력
```
8
```

## 배열 추출하기
```
Select[{1, 2, 3, 4, 5}, EvenQ]
Select[{1, 2, 3, 4, 5}, Mod[#,2]==0&]
```
출력
```
{2, 4}
```


## 함수 공식 문서

[Solve](https://reference.wolfram.com/language/ref/Solve.html) · [Reduce](https://reference.wolfram.com/language/ref/Reduce.html) · [D](https://reference.wolfram.com/language/ref/D.html) · [Integrate](https://reference.wolfram.com/language/ref/Integrate.html) · [Limit](https://reference.wolfram.com/language/ref/Limit.html) · [Sum](https://reference.wolfram.com/language/ref/Sum.html) · [Inverse](https://reference.wolfram.com/language/ref/Inverse.html) · [Eigensystem](https://reference.wolfram.com/language/ref/Eigensystem.html) · [Projection](https://reference.wolfram.com/language/ref/Projection.html) · [RotationMatrix](https://reference.wolfram.com/language/ref/RotationMatrix.html) · [ReflectionTransform](https://reference.wolfram.com/language/ref/ReflectionTransform.html) · [RandomReal](https://reference.wolfram.com/language/ref/RandomReal.html) · [RandomInteger](https://reference.wolfram.com/language/ref/RandomInteger.html) · [RandomVariate](https://reference.wolfram.com/language/ref/RandomVariate.html)
