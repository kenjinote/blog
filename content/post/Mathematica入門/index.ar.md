---le: 'مقدمة في Mathematica: كيفية استخدام الأوامر الأساسية مثل المعادلات والتفاضل والتكامل'
slug: "Mathematica入門"
date: 2024-07-25T01:36:19+09:00
tags: ["Mathematica", "رياضيات", "خوارزميات"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: 'نشرح للمبتدئين كيفية الاستخدام الأساسي وأوامر الحساب في Mathematica. قمنا بتجميع أمثلة محددة للدوال المستخدمة بشكل متكرر مثل حل المعادلات وأنظمة المعادلات (Solve)، والمتباينات (Reduce)، والتفاضل (D)، والتكامل (Integrate)، وحساب المصفوفات.'
lastmod: "2026-11-24T00:00:00+09:00"

---
# مقدمة في Mathematica

## حل المعادلات

```
Solve[x^2 - 3 x + 2 == 0, x]
```

الخرج
```
{{x -> 1}, {x -> 2}}
```

## إيجاد حلول المعادلات في نطاق الأعداد الصحيحة
```
Solve[x^2 - 3 x + 2 == 0 && 0 <= x <= 2, x, Integers]
```
الخرج
```
{{x -> 1}, {x -> 2}}
```

## حل نظام من المعادلات
```
Solve[{x + y == 3, x - y == 1}, {x, y}]
```
الخرج
```
{{x -> 2, y -> 1}}
```

## حل المتباينات
```
Reduce[x^2 - 3 x + 2 > 0, x]
```
الخرج
```
x < 1 || x > 2
```

## التفاضل
```
D[x^2, x]
```
الخرج
```
2 x
```

## التكامل
```
Integrate[x^2, x]
```
الخرج
```
x^3/3
```

## إيجاد النهاية
```
Limit[1/x, x -> 0, Direction -> "FromAbove"]
```
الخرج
```
Infinity
```

النهاية عندما يقترب x من الصفر من اليمين هي Infinity. النهاية الحقيقية من الجهتين غير موجودة. يحدد Direction جهة الاقتراب الأحادية.

## إيجاد المتسلسلة
```
Sum[1/n^2, {n, 1, Infinity}]
```
الخرج
```
π^2/6
```

## إنشاء مصفوفة
```
m = {{1, 2}, {3, 4}}
```

## إيجاد ضرب المصفوفات
```
m . m
```
الخرج
```
{{7, 10}, {15, 22}}
```

## إيجاد المصفوفة المعكوسة
```
Inverse[m]
```
الخرج
```
{{-2, 1}, {3/2, -1/2}}
```

## إيجاد [القيم الذاتية والمتجهات الذاتية](https://kenji.blog/ar/p/eigenvalues-and-eigenvectors/)
```
Eigensystem[m]
```
الخرج
```
{{(5 + Sqrt[33])/2, (5 - Sqrt[33])/2}, {{2, (3 + Sqrt[33])/2}, {2, (3 - Sqrt[33])/2}}}
```

القيم الذاتية لهذه المصفوفة هي (5 ± √33)/2. قد يختلف ترتيب المتجهات الذاتية أو قياسها؛ وتحقق كل قيمة ومتجه العلاقة m.v = λv.

## إيجاد الضرب النقطي للمتجهات
```
{1, 2} . {3, 4}
```
الخرج
```
11
```

## إيجاد الضرب التقاطعي للمتجهات
```
Cross[{1, 2, 3}, {4, 5, 6}]
```
الخرج
```
{-3, 6, -3}
```

## إيجاد مقدار المتجه
```
Norm[{1, 2, 3}]
```
الخرج
```
√14
```

## إيجاد زاوية المتجه
```
ArcCos[{1, 2} . {3, 4}/(Norm[{1, 2}] Norm[{3, 4}])]
```

الخرج
```
ArcCos[11/(√5 √25)]
```

## إيجاد الإسقاط المتجهي
```
Projection[{1, 2}, {3, 4}]
```
الخرج
```
{33/25, 44/25}
```

إسقاط {1,2} على {3,4} يستخدم نسبة الضرب الداخلي 11/25، فتكون النتيجة {33/25,44/25}.







## إيجاد دوران المتجه
```
RotationMatrix[π/2].{1, 0}
```

الخرج
```
{0, 1}
```

## إيجاد انتقال المتجه
```
TranslationTransform[{1, 2}][{3, 4}]
```
الخرج
```
{4, 6}
```

## إيجاد تحجيم المتجه
```
ScalingTransform[{2, 3}][{1, 1}]
```
الخرج
```
{2, 3}
```

## إيجاد انعكاس المتجه
```
ReflectionTransform[{0, 1}][{1, 1}]
```
الخرج
```
{1, -1}
```

الوسيطة الأولى لـ ReflectionTransform هي العمودي على المرآة. العمودي {0,1} يحدد محور x ويحوّل {1,1} إلى {1,-1}.

القيم العشوائية التالية توضيحية وتتغير في كل تقييم. تعيد RandomInteger[] القيمة 0 أو 1. ويساعد SeedRandom على إعادة السلسلة بالمولد والإصدار نفسيهما.









## توليد أرقام عشوائية
```
RandomReal[]
```


الخرج
```
0.123456
```

## توليد أرقام عشوائية (أعداد صحيحة)
```
RandomInteger[]
```
الخرج
```
0
```

## توليد أرقام عشوائية (ضمن نطاق)
```
RandomReal[{1, 10}]
```
الخرج
```
5.6789
```

## توليد أرقام عشوائية (أعداد صحيحة ضمن نطاق)
```
RandomInteger[{1, 10}]
```
الخرج
```
5
```

## توليد أرقام عشوائية (توزيع محدد)
```
RandomVariate[NormalDistribution[0, 1]]
```
الخرج
```
0.123456
```

## توليد أرقام عشوائية (توزيع محدد، عدد محدد)
```
RandomVariate[NormalDistribution[0, 1], 10]
```
الخرج
```
{0.123456, 0.234567, 0.345678, 0.456789, 0.567890, 0.678901, 0.789012, 0.890123, 0.901234, 0.012345}
```

## توليد أرقام عشوائية (توزيع، عدد، وبذرة محددة)
```
SeedRandom[12345]
RandomVariate[NormalDistribution[0, 1], 10]
```
الخرج
```
(* Output intentionally omitted: exact sequence depends on the Wolfram Language version. *)
```

## تطبيق دالة على عناصر المصفوفة
```
Map[Sqrt, {1, 4, 9}]
Sqrt /@ {1, 4, 9}
Map[#^(1/2)&, {1, 4, 9}]
```
الخرج
```
{1, 2, 3}
```

## تعريف دالة باستخدام تعبير لامبدا
```
f = Function[x, x^2]
f[3]
```
الخرج
```
9
```

## تركيب الدوال
```
f = Function[x, x^2]
g = Function[x, x + 1]
h = Function[x, f[g[x]]]
h[3]
```
الخرج
```
16
```

## الإشارة إلى نتيجة الحساب السابق
```
% + 1
```
الخرج
```
17
```

## دوال نقية
```
(#+3)&[5]
```
الخرج
```
8
```

## استخراج من المصفوفة
```
Select[{1, 2, 3, 4, 5}, EvenQ]
Select[{1, 2, 3, 4, 5}, Mod[#,2]==0&]
```
الخرج
```
{2, 4}
```


## الوثائق الرسمية للدوال

[Solve](https://reference.wolfram.com/language/ref/Solve.html) · [Reduce](https://reference.wolfram.com/language/ref/Reduce.html) · [D](https://reference.wolfram.com/language/ref/D.html) · [Integrate](https://reference.wolfram.com/language/ref/Integrate.html) · [Limit](https://reference.wolfram.com/language/ref/Limit.html) · [Sum](https://reference.wolfram.com/language/ref/Sum.html) · [Inverse](https://reference.wolfram.com/language/ref/Inverse.html) · [Eigensystem](https://reference.wolfram.com/language/ref/Eigensystem.html) · [Projection](https://reference.wolfram.com/language/ref/Projection.html) · [RotationMatrix](https://reference.wolfram.com/language/ref/RotationMatrix.html) · [ReflectionTransform](https://reference.wolfram.com/language/ref/ReflectionTransform.html) · [RandomReal](https://reference.wolfram.com/language/ref/RandomReal.html) · [RandomInteger](https://reference.wolfram.com/language/ref/RandomInteger.html) · [RandomVariate](https://reference.wolfram.com/language/ref/RandomVariate.html)
