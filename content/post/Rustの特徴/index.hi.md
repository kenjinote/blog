---
title: "Rust की पाँच प्रमुख विशेषताएँ: सुरक्षा, ownership और Cargo"
slug: "Rustの特徴"
date: 2022-10-03T22:47:20+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Rust की उत्पत्ति, मेमोरी मॉडल, ownership और borrowing, प्लेटफ़ॉर्म समर्थन तथा Cargo का परिचय; साथ में सुरक्षा गारंटी की सीमाएँ और टार्गेट के बीच अंतर।"
---
Rust एक ओपन-सोर्स प्रोग्रामिंग भाषा है, जिसका ध्यान भरोसेमंद और कुशल सॉफ़्टवेयर बनाने पर है। इसकी पाँच प्रमुख विशेषताएँ हैं।

1. **Mozilla से शुरू हुआ सामुदायिक प्रोजेक्ट**: Rust की शुरुआत Mozilla Research प्रोजेक्ट के रूप में हुई। 2015 से इसकी दिशा और शासन Mozilla से स्वतंत्र हैं।
2. **अंतर्निहित garbage collector पर निर्भर नहीं**: Rust को अंतर्निहित garbage collector के बिना प्रदर्शन और मेमोरी दक्षता के लिए बनाया गया है।
3. **Ownership और borrowing**: Ownership, references और borrowing सामान्य safe Rust कोड में compiler को मेमोरी सुरक्षा की कई गारंटियाँ लागू करने देते हैं। `unsafe` कोड और दूसरी भाषाओं के साथ इंटरफ़ेस की सावधानी से समीक्षा करनी होती है।
4. **कई प्लेटफ़ॉर्म का समर्थन**: Rust कई ऑपरेटिंग सिस्टम और प्रोसेसर आर्किटेक्चर को target कर सकता है, लेकिन हर target के समर्थन स्तर और गारंटियाँ अलग होती हैं।
5. **Cargo**: Rust का मानक टूल Cargo पैकेज संभालने के साथ build और test जैसे काम भी करता है।

Rust प्रोजेक्ट का शासन समुदाय के पास है और Rust Foundation इसे समर्थन देती है। [Rust की आधिकारिक साइट](https://www.rust-lang.org/), [प्रोजेक्ट का इतिहास](https://blog.rust-lang.org/2020/08/18/laying-the-foundation-for-rusts-future.html), [Ownership मार्गदर्शिका](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html), [Cargo Book](https://doc.rust-lang.org/cargo/), [प्लेटफ़ॉर्म समर्थन](https://doc.rust-lang.org/rustc/platform-support.html) और [Unsafe Rust](https://doc.rust-lang.org/book/ch20-01-unsafe-rust.html) देखें।
