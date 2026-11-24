---
title: "गणित के पाँच सुंदर परिणाम: सटीक कथन और सीमाएँ"
slug: "好きなसूत्र"
date: 2022-10-05T13:24:50+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["गणित"]
draft: false
math: true
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "विल्सन प्रमेय, यूलर सूत्र और सर्वसमिका, फ़र्मा का अंतिम प्रमेय, बेसल समस्या तथा यूलर बहुपद की सीमित अभाज्य-उत्पादक सीमा का सटीक परिचय।"
---
यहाँ पाँच प्रसिद्ध गणितीय परिणाम उनकी स्पष्ट शर्तों के साथ दिए गए हैं। $p,n,k$ पूर्णांक हैं, $i^2=-1$, और $\\pi$ वृत्त की नियतांक है।

## विल्सन का प्रमेय

यदि $p$ अभाज्य है, तो $(p-1)!\equiv -1 \pmod p$। अधिक सटीक रूप में, पूर्णांक $m>1$ अभाज्य है तभी और केवल तभी जब $(m-1)!\equiv -1 \pmod m$। यहाँ $r!$, 1 से $r$ तक के पूर्णांकों का गुणनफल है।

## यूलर का सूत्र और सर्वसमिका

रेडियन में मापे गए वास्तविक $x$ के लिए यूलर का सूत्र $e^{ix}=\cos x+i\sin x$ है। $x=\pi$ रखने पर इसका विशेष रूप, यूलर की सर्वसमिका $e^{i\pi}+1=0$, मिलता है।

## [फ़र्मा का अंतिम प्रमेय](https://kenji.blog/hi/p/fermats-last-theorem/)

हर पूर्णांक $n\ge 3$ के लिए ऐसे धनात्मक पूर्णांक $x,y,z$ नहीं हैं जो $x^n+y^n=z^n$ को संतुष्ट करें। धनात्मक पूर्णांक और घात कम से कम 3 होने की शर्तें आवश्यक हैं।

## बेसल समस्या

सभी धनात्मक पूर्णांकों के वर्गों के व्युत्क्रमों का अनंत योग है: $\displaystyle \sum_{k=1}^{\infty}\frac{1}{k^2}=\frac{\pi^2}{6}$।

## यूलर का अभाज्य-उत्पादक बहुपद

बहुपद $n^2+n+41$, पूर्णांक $n=0,1,\ldots,39$ के लिए अभाज्य संख्या देता है। यह हर पूर्णांक के लिए अभाज्य नहीं देता: $n=40$ पर इसका मान $1681=41^2$ है, जो भाज्य है।

## संदर्भ

- [Wilson’s Theorem — Wolfram MathWorld](https://mathworld.wolfram.com/WilsonsTheorem.html)
- [About Euler’s Identity — Euler-Franeker Memorial University](https://euler.euclid.int/about-eulers-identity/)
- [Fermat’s Last Theorem — University of Cambridge](https://www.maths.cam.ac.uk/features/node/153)
- [The Basel Problem — University of Kentucky](https://clp.math.uky.edu/clp2/chap_seq_ser-5.html)
- [Euler’s prime-producing polynomial revisited — Cambridge University Press](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1F76183BF30CECE688E31E8F10F37AC8/S0025557224000111a.pdf/eulers_primeproducing_polynomial_revisited.pdf)
