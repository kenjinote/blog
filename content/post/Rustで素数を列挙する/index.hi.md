---
title: 'Rust में अभाज्य संख्याओं की सूची बनाने के लिए प्रोग्राम कैसे बनाएं और कोड उदाहरण'
slug: "Rust में अभाज्य संख्याओं की गणना"
date: 2022-09-09T07:08:49+09:00
tags: ["Rust","अभाज्य संख्याएँ","एल्गोरिदम"]
draft: false
image: "images/img.webp"
categories: ["प्रोग्रामिंग"]
description: 'Rust प्रोग्रामिंग सीखने के लिए, हम निर्दिष्ट ऊपरी सीमा तक अभाज्य संख्याओं को सूचीबद्ध करने वाले एक सरल एल्गोरिदम का कार्यान्वयन उदाहरण प्रस्तुत करते हैं। लूप और सशर्त शाखाओं का उपयोग करके बुनियादी कोडिंग विधि को विशिष्ट नमूना कोड के साथ स्पष्ट रूप से समझाया गया है।'
---
मैंने Rust में अभाज्य संख्याओं की गणना करने के लिए एक प्रोग्राम लिखा है।

```rust
fn main() {
	let max = 1000;
    let mut primes = vec![2];
    let mut n = 3;
    loop {
        let mut is_prime = true;
        for p in &primes {
            if n % p == 0 {
                is_prime = false;
                break;
            }
        }
        if is_prime {
            primes.push(n);
        }
        n += 2;
		if n > max {
			break;
		}
    }
    for p in &primes {
		println!("{}", p);
    }
}
```
