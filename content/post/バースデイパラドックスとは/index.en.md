---
title: 'What is the Birthday Paradox?'
slug: "バースデイパラドックスとは"
date: 2024-04-02T01:20:50+09:00
tags: ["Mathematics", "Paradox"]
draft: false
math: true
image: "img.png"
categories: ["Math, Cryptography, Quantum"]
---

## Do you know the Birthday Paradox?

Let me tell you a slightly mysterious story.
How many people do you think need to gather for the "probability of people having the same birthday" to become high?

For example, a year has 365 days, so when you're told "if 23 people gather, the probability of someone sharing a birthday is over 50%"... it feels somewhat counterintuitive, right?

But this is **actually over 50%.**

---

## Why does this happen?

This phenomenon is called the "Birthday Paradox".
Its name contains "paradox", but there is a proper mathematical reason for it.

When the number of people is "n", the **probability that no one shares a birthday** can be calculated with the following formula:

```
P(No one shares) = 365/365 × 364/365 × 363/365 × ... × (365 - n + 1)/365
```

By subtracting that from 1, you get the "probability of sharing a birthday with someone".

---

## Looking at the results...

| Number of People | Probability of people having the same birthday |
| --- | ------------------ |
| 10 people | Approx. 11.7% |
| 20 people | Approx. 41.1% |
| 23 people | **Approx. 50.7% (Focus here!)** |
| 30 people | Approx. 70.6% |
| 70 people | **A whopping approx. 99.9%!** |

In other words, with just **23 people**, there is a more than half chance that someone will share a birthday.
It seems like this could apply quite often in a school class or a workplace meeting, right?

---

## Conclusion: The gap between intuition and mathematics is interesting

The "Birthday Paradox" is an interesting example where our intuition and actual mathematical probabilities diverge.
Knowing this kind of story might make for lively small talk or a fun quiz!

---

## Reference Links

* [Birthday problem (Wikipedia)](https://en.wikipedia.org/wiki/Birthday_problem)
