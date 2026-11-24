---le: 'Mathematica परिचय: समीकरण, डिफरेंशियल और इंटीग्रल कैलकुलस जैसी बुनियादी कमांड का उपयोग कैसे करें'
slug: "Mathematica入門"
date: 2024-07-25T01:36:19+09:00
tags: ["Mathematica", "गणित", "एल्गोरिथ्म"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: 'शुरुआती लोगों के लिए Mathematica का उपयोग करने के बुनियादी तरीके और गणना कमांड समझाए गए हैं। समीकरणों और युगपत समीकरणों (Solve), असमानताओं (Reduce), डिफरेंशियल (D), इंटीग्रल (Integrate), और मैट्रिक्स गणना जैसे अक्सर उपयोग किए जाने वाले कार्यों के विशिष्ट उदाहरण संक्षेप में दिए गए हैं।'
lastmod: "2026-11-24T00:00:00+09:00"

---
# Mathematica का परिचय

## समीकरण हल करना

```
Solve[x^2 - 3 x + 2 == 0, x]
```

आउटपुट
```
{{x -> 1}, {x -> 2}}
```

## पूर्णांक सीमा में समीकरण का हल ढूँढना
```
Solve[x^2 - 3 x + 2 == 0 && 0 <= x <= 2, x, Integers]
```
आउटपुट
```
{{x -> 1}, {x -> 2}}
```

## युगपत समीकरण हल करना
```
Solve[{x + y == 3, x - y == 1}, {x, y}]
```
आउटपुट
```
{{x -> 2, y -> 1}}
```

## असमानताएं हल करना
```
Reduce[x^2 - 3 x + 2 > 0, x]
```
आउटपुट
```
x < 1 || x > 2
```

## अवकलन करना
```
D[x^2, x]
```
आउटपुट
```
2 x
```

## समाकलन करना
```
Integrate[x^2, x]
```
आउटपुट
```
x^3/3
```

## सीमा ज्ञात करना
```
Limit[1/x, x -> 0, Direction -> "FromAbove"]
```
आउटपुट
```
Infinity
```

x के 0 के दाईं ओर से पास आने पर सीमा Infinity है। दोनों ओर से वास्तविक सीमा मौजूद नहीं है। Direction से एकतरफा दिशा चुनी जा सकती है।

## श्रृंखला ज्ञात करना
```
Sum[1/n^2, {n, 1, Infinity}]
```
आउटपुट
```
π^2/6
```

## मैट्रिक्स बनाना
```
m = {{1, 2}, {3, 4}}
```

## मैट्रिक्स का गुणनफल ज्ञात करना
```
m . m
```
आउटपुट
```
{{7, 10}, {15, 22}}
```

## व्युत्क्रम मैट्रिक्स ज्ञात करना
```
Inverse[m]
```
आउटपुट
```
{{-2, 1}, {3/2, -1/2}}
```

## [आइगेनवैल्यू और आइगेनवेक्टर](https://kenji.blog/hi/p/eigenvalues-and-eigenvectors/) ज्ञात करना
```
Eigensystem[m]
```
आउटपुट
```
{{(5 + Sqrt[33])/2, (5 - Sqrt[33])/2}, {{2, (3 + Sqrt[33])/2}, {2, (3 - Sqrt[33])/2}}}
```

इस मैट्रिक्स के eigenvalues (5 ± √33)/2 हैं। eigenvectors का क्रम या गुणक अलग हो सकता है; प्रत्येक युग्म m.v = λv को संतुष्ट करता है।

## सदिशों का बिंदु गुणनफल ज्ञात करना
```
{1, 2} . {3, 4}
```
आउटपुट
```
11
```

## सदिशों का क्रॉस गुणनफल ज्ञात करना
```
Cross[{1, 2, 3}, {4, 5, 6}]
```
आउटपुट
```
{-3, 6, -3}
```

## सदिश का परिमाण ज्ञात करना
```
Norm[{1, 2, 3}]
```
आउटपुट
```
√14
```

## सदिशों का कोण ज्ञात करना
```
ArcCos[{1, 2} . {3, 4}/(Norm[{1, 2}] Norm[{3, 4}])]
```

आउटपुट
```
ArcCos[11/(√5 √25)]
```

## सदिश का प्रक्षेपण ज्ञात करना
```
Projection[{1, 2}, {3, 4}]
```
आउटपुट
```
{33/25, 44/25}
```

{1,2} को {3,4} पर प्रक्षेपित करने में डॉट-प्रोडक्ट अनुपात 11/25 होता है और परिणाम {33/25,44/25} है।







## सदिश का घूर्णन ज्ञात करना
```
RotationMatrix[π/2].{1, 0}
```

आउटपुट
```
{0, 1}
```

## सदिश का स्थानांतरण ज्ञात करना
```
TranslationTransform[{1, 2}][{3, 4}]
```
आउटपुट
```
{4, 6}
```

## सदिश की स्केलिंग ज्ञात करना
```
ScalingTransform[{2, 3}][{1, 1}]
```
आउटपुट
```
{2, 3}
```

## सदिश का परावर्तन ज्ञात करना
```
ReflectionTransform[{0, 1}][{1, 1}]
```
आउटपुट
```
{1, -1}
```

ReflectionTransform का पहला तर्क दर्पण का normal है। {0,1} normal x-अक्ष को दर्शाता है और {1,1} को {1,-1} में बदलता है।

नीचे दिए गए यादृच्छिक परिणाम केवल उदाहरण हैं और हर मूल्यांकन पर बदलते हैं। RandomInteger[] 0 या 1 देता है। SeedRandom उसी जनरेटर और संस्करण में क्रम दोहराने में मदद करता है।









## यादृच्छिक संख्याएँ उत्पन्न करना
```
RandomReal[]
```


आउटपुट
```
0.123456
```

## यादृच्छिक संख्याएँ उत्पन्न करना (पूर्णांक)
```
RandomInteger[]
```
आउटपुट
```
0
```

## यादृच्छिक संख्याएँ उत्पन्न करना (सीमा निर्दिष्ट)
```
RandomReal[{1, 10}]
```
आउटपुट
```
5.6789
```

## यादृच्छिक संख्याएँ उत्पन्न करना (पूर्णांक, सीमा निर्दिष्ट)
```
RandomInteger[{1, 10}]
```
आउटपुट
```
5
```

## यादृच्छिक संख्याएँ उत्पन्न करना (वितरण निर्दिष्ट)
```
RandomVariate[NormalDistribution[0, 1]]
```
आउटपुट
```
0.123456
```

## यादृच्छिक संख्याएँ उत्पन्न करना (वितरण, मात्रा निर्दिष्ट)
```
RandomVariate[NormalDistribution[0, 1], 10]
```
आउटपुट
```
{0.123456, 0.234567, 0.345678, 0.456789, 0.567890, 0.678901, 0.789012, 0.890123, 0.901234, 0.012345}
```

## यादृच्छिक संख्याएँ उत्पन्न करना (वितरण, मात्रा, बीज निर्दिष्ट)
```
SeedRandom[12345]
RandomVariate[NormalDistribution[0, 1], 10]
```
आउटपुट
```
(* Output intentionally omitted: exact sequence depends on the Wolfram Language version. *)
```

## सरणी के तत्वों पर फ़ंक्शन लागू करना
```
Map[Sqrt, {1, 4, 9}]
Sqrt /@ {1, 4, 9}
Map[#^(1/2)&, {1, 4, 9}]
```
आउटपुट
```
{1, 2, 3}
```

## लैम्ब्डा एक्सप्रेशन का उपयोग करके फ़ंक्शन परिभाषित करना
```
f = Function[x, x^2]
f[3]
```
आउटपुट
```
9
```

## फ़ंक्शन रचना
```
f = Function[x, x^2]
g = Function[x, x + 1]
h = Function[x, f[g[x]]]
h[3]
```
आउटपुट
```
16
```

## पिछली गणना के परिणाम का संदर्भ देना
```
% + 1
```
आउटपुट
```
17
```

## शुद्ध फ़ंक्शन
```
(#+3)&[5]
```
आउटपुट
```
8
```

## सरणी निष्कर्षण
```
Select[{1, 2, 3, 4, 5}, EvenQ]
Select[{1, 2, 3, 4, 5}, Mod[#,2]==0&]
```
आउटपुट
```
{2, 4}
```


## फ़ंक्शन के आधिकारिक दस्तावेज़

[Solve](https://reference.wolfram.com/language/ref/Solve.html) · [Reduce](https://reference.wolfram.com/language/ref/Reduce.html) · [D](https://reference.wolfram.com/language/ref/D.html) · [Integrate](https://reference.wolfram.com/language/ref/Integrate.html) · [Limit](https://reference.wolfram.com/language/ref/Limit.html) · [Sum](https://reference.wolfram.com/language/ref/Sum.html) · [Inverse](https://reference.wolfram.com/language/ref/Inverse.html) · [Eigensystem](https://reference.wolfram.com/language/ref/Eigensystem.html) · [Projection](https://reference.wolfram.com/language/ref/Projection.html) · [RotationMatrix](https://reference.wolfram.com/language/ref/RotationMatrix.html) · [ReflectionTransform](https://reference.wolfram.com/language/ref/ReflectionTransform.html) · [RandomReal](https://reference.wolfram.com/language/ref/RandomReal.html) · [RandomInteger](https://reference.wolfram.com/language/ref/RandomInteger.html) · [RandomVariate](https://reference.wolfram.com/language/ref/RandomVariate.html)
