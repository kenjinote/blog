---
title: 'كيفية إنشاء برنامج لسرد الأعداد الأولية في Rust وأمثلة على الكود'
slug: "Rustで素数を列挙する"
date: 2022-09-09T07:08:49+09:00
tags: ["Rust","أعداد أولية","خوارزمية"]
draft: false
image: "images/img.webp"
categories: ["برمجة"]
description: 'كجزء من تعلم برمجة Rust، نعرض مثالاً لتنفيذ خوارزمية بسيطة تسرد الأعداد الأولية حتى قيمة حد أقصى محددة. نشرح بوضوح طرق البرمجة الأساسية باستخدام عمليات التكرار والجمل الشرطية مع أمثلة كود محددة.'
---
لقد كتبت برنامجًا لسرد الأعداد الأولية في Rust.

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
