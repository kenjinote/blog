---
title: 'Введение в Mathematica: Как использовать базовые команды для уравнений, дифференцирования и интегрирования'
slug: "Mathematica入門"
date: 2024-07-25T01:36:19+09:00
tags: ["Mathematica", "Математика", "Алгоритмы"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: 'Руководство для начинающих по основам использования Mathematica и командам вычислений. Собраны конкретные примеры часто используемых функций, таких как решение уравнений и систем уравнений (Solve), неравенств (Reduce), дифференцирование (D), интегрирование (Integrate) и матричные вычисления.'
lastmod: "2026-11-24T00:00:00+09:00"
mermaid: true
---
# Введение в Mathematica

## Решение уравнений

```
Solve[x^2 - 3 x + 2 == 0, x]
```

Вывод
```
{{x -> 1}, {x -> 2}}
```

## Поиск решений уравнений в целых числах
```
Solve[x^2 - 3 x + 2 == 0 && 0 <= x <= 2, x, Integers]
```
Вывод
```
{{x -> 1}, {x -> 2}}
```

## Решение систем уравнений
```
Solve[{x + y == 3, x - y == 1}, {x, y}]
```
Вывод
```
{{x -> 2, y -> 1}}
```

## Решение неравенств
```
Reduce[x^2 - 3 x + 2 > 0, x]
```
Вывод
```
x < 1 || x > 2
```

## Дифференцирование
```
D[x^2, x]
```
Вывод
```
2 x
```

## Интегрирование
```
Integrate[x^2, x]
```
Вывод
```
x^3/3
```

## Вычисление пределов
```
Limit[1/x, x -> 0, Direction -> "FromAbove"]
```
Вывод
```
Infinity
```

Предел при стремлении x к 0 справа равен Infinity. Двусторонний предел по вещественным числам не существует. Направление одностороннего предела задаёт Direction.

## Вычисление рядов
```
Sum[1/n^2, {n, 1, Infinity}]
```
Вывод
```
π^2/6
```

## Создание матриц
```
m = {{1, 2}, {3, 4}}
```

## Умножение матриц
```
m . m
```
Вывод
```
{{7, 10}, {15, 22}}
```

## Вычисление обратной матрицы
```
Inverse[m]
```
Вывод
```
{{-2, 1}, {3/2, -1/2}}
```

## Поиск собственных значений и векторов
```
Eigensystem[m]
```
Вывод
```
{{(5 + Sqrt[33])/2, (5 - Sqrt[33])/2}, {{2, (3 + Sqrt[33])/2}, {2, (3 - Sqrt[33])/2}}}
```

Собственные значения этой матрицы равны (5 ± √33)/2. Порядок и масштаб собственных векторов могут различаться; каждая пара удовлетворяет m.v = λv.

## Скалярное произведение векторов
```
{1, 2} . {3, 4}
```
Вывод
```
11
```

## Векторное произведение векторов
```
Cross[{1, 2, 3}, {4, 5, 6}]
```
Вывод
```
{-3, 6, -3}
```

## Вычисление длины вектора
```
Norm[{1, 2, 3}]
```
Вывод
```
√14
```

## Вычисление угла между векторами
```
ArcCos[{1, 2} . {3, 4}/(Norm[{1, 2}] Norm[{3, 4}])]
```

Вывод
```
ArcCos[11/(√5 √25)]
```

## Проекция вектора
```
Projection[{1, 2}, {3, 4}]
```
Вывод
```
{33/25, 44/25}
```

При ортогональной проекции {1,2} на {3,4} отношение скалярных произведений равно 11/25, результат — {33/25,44/25}.







## Вращение вектора
```
RotationMatrix[π/2].{1, 0}
```

Вывод
```
{0, 1}
```

## Параллельный перенос вектора
```
TranslationTransform[{1, 2}][{3, 4}]
```
Вывод
```
{4, 6}
```

## Масштабирование вектора
```
ScalingTransform[{2, 3}][{1, 1}]
```
Вывод
```
{2, 3}
```

## Отражение вектора
```
ReflectionTransform[{0, 1}][{1, 1}]
```
Вывод
```
{1, -1}
```

Первый аргумент ReflectionTransform задаёт нормаль зеркала. Нормаль {0,1} соответствует оси x и переводит {1,1} в {1,-1}.

Приведённые ниже случайные результаты иллюстративны и меняются при каждом вычислении. RandomInteger[] возвращает 0 или 1. SeedRandom воспроизводит последовательность с тем же генератором и версией.









## Генерация случайных чисел
```
RandomReal[]
```


Вывод
```
0.123456
```

## Генерация случайных чисел (целые числа)
```
RandomInteger[]
```
Вывод
```
0
```

## Генерация случайных чисел (с указанием диапазона)
```
RandomReal[{1, 10}]
```
Вывод
```
5.6789
```

## Генерация случайных чисел (целые числа, с указанием диапазона)
```
RandomInteger[{1, 10}]
```
Вывод
```
5
```

## Генерация случайных чисел (с указанием распределения)
```
RandomVariate[NormalDistribution[0, 1]]
```
Вывод
```
0.123456
```

## Генерация случайных чисел (с распределением и количеством)
```
RandomVariate[NormalDistribution[0, 1], 10]
```
Вывод
```
{0.123456, 0.234567, 0.345678, 0.456789, 0.567890, 0.678901, 0.789012, 0.890123, 0.901234, 0.012345}
```

## Генерация случайных чисел (распределение, количество, seed)
```
SeedRandom[12345]
RandomVariate[NormalDistribution[0, 1], 10]
```
Вывод
```
(* Output intentionally omitted: exact sequence depends on the Wolfram Language version. *)
```

## Применение функции к элементам массива
```
Map[Sqrt, {1, 4, 9}]
Sqrt /@ {1, 4, 9}
Map[#^(1/2)&, {1, 4, 9}]
```
Вывод
```
{1, 2, 3}
```

## Определение функции с помощью лямбда-выражения
```
f = Function[x, x^2]
f[3]
```
Вывод
```
9
```

## Композиция функций
```
f = Function[x, x^2]
g = Function[x, x + 1]
h = Function[x, f[g[x]]]
h[3]
```
Вывод
```
16
```

## Ссылка на результат предыдущего вычисления
```
% + 1
```
Вывод
```
17
```

## Чистые функции
```
(#+3)&[5]
```
Вывод
```
8
```

## Извлечение из массива
```
Select[{1, 2, 3, 4, 5}, EvenQ]
Select[{1, 2, 3, 4, 5}, Mod[#,2]==0&]
```
Вывод
```
{2, 4}
```


## Официальная документация функций

[Solve](https://reference.wolfram.com/language/ref/Solve.html) · [Reduce](https://reference.wolfram.com/language/ref/Reduce.html) · [D](https://reference.wolfram.com/language/ref/D.html) · [Integrate](https://reference.wolfram.com/language/ref/Integrate.html) · [Limit](https://reference.wolfram.com/language/ref/Limit.html) · [Sum](https://reference.wolfram.com/language/ref/Sum.html) · [Inverse](https://reference.wolfram.com/language/ref/Inverse.html) · [Eigensystem](https://reference.wolfram.com/language/ref/Eigensystem.html) · [Projection](https://reference.wolfram.com/language/ref/Projection.html) · [RotationMatrix](https://reference.wolfram.com/language/ref/RotationMatrix.html) · [ReflectionTransform](https://reference.wolfram.com/language/ref/ReflectionTransform.html) · [RandomReal](https://reference.wolfram.com/language/ref/RandomReal.html) · [RandomInteger](https://reference.wolfram.com/language/ref/RandomInteger.html) · [RandomVariate](https://reference.wolfram.com/language/ref/RandomVariate.html)
