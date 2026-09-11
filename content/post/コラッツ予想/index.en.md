---
title: 'What is the Collatz Conjecture? Verifying a Mathematical Unsolved Problem Where Any Number Eventually Reaches 1 in Python'
slug: "コラッツ予想"
date: 2025-07-15T18:03:03+09:00
tags: ["Collatz Conjecture", "Math", "Programming", "Algorithm"]
draft: false
image: "img.webp"
categories: ["Math/Cryptography/Quantum"]
description: 'Will repeating ''halve if even, multiply by 3 and add 1 if odd'' always result in 1? An easy-to-understand explanation of the mysterious rules behind the famous unsolved mathematical problem, the ''Collatz Conjecture''. Furthermore, we''ll write a Python program to simulate and see if sequences actually converge to 1.'
---

# "Any number will eventually become 1"? ── Playing with the Collatz Conjecture

Hello! It's kenji.

All of a sudden, doesn't it sound a bit mysterious when you hear about "a rule where any number eventually becomes 1"?

> For example, 19, or 87, or even 1000000.
> If you manipulate the number according to a certain rule, it somehow converges to "1" in the end.

Such a dream-like story is the **Collatz Conjecture**.

---

## What exactly is the Collatz Conjecture?

First, let's introduce the rules.

* Start: Pick any **positive integer**
* Operation:

    * If it's even → Halve it (n → n / 2)
    * If it's odd → Multiply by 3 and add 1 (n → 3n + 1)

The conjecture is that if you keep repeating this, **any number will eventually reach 1**.

For example, starting with `6`:

```
6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
```

It properly became "1". Welcome back!

---

## Let's try it with code: Collatz in Python

Now, in times like this, it's faster to test it with code!
Let's output the "Collatz sequence" in Python.

```python
def collatz(n):
    steps = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps.append(n)
    return steps

# Example: Let's start with 19
print(collatz(19))
```

When you run it:

```
[19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
```

It beautifully reaches 1.
It takes quite a detour, but reaches the goal securely at the end!


By the way, even if you start with **27**, it reaches 1 in the same way.

```
print(collatz(27))
```

When you run it:

```
[27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242,
121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350,
175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167,
502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479,
1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911,
2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732,
866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35,
106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
```

Surprisingly, it takes 111 steps!

Moreover, there are moments where it swells up to over 9000 along the way.
It's a pattern that takes a massive detour before hitting the goal.

---

## So, what's so amazing about it?

What's amazing about this conjecture is,

> **Even though it hasn't been proven, it seems to become 1 no matter what number you try**

That's the point.

Eh? What about 1 trillion, or 10 quadrillion...?

For those who thought that, you're sharp.
Actually, it has been verified using computers up to about "2 to the power of 68",
and **all of them have reached 1**. Unbelievable...

However, **it hasn't been theoretically proven that "it works for all of them"**.
This is what's called an "unsolved problem" in the world of mathematics.

---

## Why does it become "1"? An approach from probability theory (Mathematical background)

It seems like magic that any number eventually becomes 1, but from a **probabilistic perspective**, there is a reasonable logic of "well, that seems likely to happen."

If you apply `3n + 1` to an odd number $n$, the answer is always an **even number**.
Therefore, in the next step, it will definitely be divided by 2, practically becoming $\frac{3n + 1}{2} \approx 1.5n$.

Then, the probability that the resulting number is even again is $\frac{1}{2}$.
If it's even, it's further divided by 2 to become $0.75n$, which is smaller than the original number.

Although not mathematically rigorous, it is known that taking the geometric mean of the "multiplier" when jumping from one odd number to the next odd number gives **approximately $\frac{3}{4}$ times** (a heuristic probability model).
In other words, **since the value tends to shrink on average**, it eventually falls as if being sucked into 1.

## What if we slightly change the rules? (Comparison with other conjectures)

"Well then, what if we multiply by 5 instead of 3?" you might want to consider.
Actually, this is known as the **$5n + 1$ problem**, and in this case, not all numbers converge to 1.

In the case of $5n + 1$, it has been confirmed that multiple different loops (cycles) exist, and it's also been pointed out that there might be numbers that continue to grow infinitely (divergence).
Also, in the case of the **$3n - 1$ problem**, aside from the "$1 \to 2 \to 1$" loop, there is another loop like "$5 \to 14 \to 7 \to 20 \to 10 \to 5$".

You can see how the property of the Collatz Conjecture, "everything converges to 1 (the $4 \to 2 \to 1$ loop)", rests upon an incredibly exquisite balance.

---

## Humanity's milestone ①: The limits of brute force by computers

Currently, mathematicians and computer science enthusiasts around the world are continuously calculating the Collatz Conjecture, making full use of distributed computing (projects that combine the computational power of PCs worldwide) and GPUs.

As of 2020, computers have confirmed that the Collatz Conjecture holds true (eventually becomes 1) for all initial values up to a staggering **$2^{68}$ (about 295,000 trillion)**.

However, in the world of mathematics, you can't say, "Since we've checked up to 295 quadrillion, it must be true for everything." From the perspective of the infinite sea of numbers, even $2^{68}$ is nothing more than "the first drop."

---

## Humanity's milestone ②: Undecidability and Terence Tao's breakthrough

In response to the question "Why can't anyone prove it?", brilliant British mathematician John Conway proved in 1972 that a slightly extended problem of the Collatz Conjecture is **"Turing complete" (undecidable)**.
This is a terrifying fact deeply related to the foundations of computer science, meaning that depending on the rules, "an algorithm to determine whether it reaches 1 does not exist in principle." The Collatz Conjecture itself might even be an unprovable proposition within the framework of modern mathematics.

However, in 2019, a major breakthrough finally occurred.
**Terence Tao**, one of the greatest genius mathematicians of our modern era, proved that "(while we can't strictly say for all) **for almost all initial values, the Collatz sequence eventually reaches a value much smaller than the original number**" by utilizing partial differential equations and probability theory.

Although this is not a complete proof that "everything becomes 1," it caused a stir in the global mathematical community as **the historical milestone where humanity came closest to the truth of the Collatz Conjecture**.

---

## Who is Mr. Collatz?

Now, reading up to this point, you might think, "Who is Collatz anyway?"
Let me properly introduce him!

* Name: **Lothar Collatz**
* Nationality: Germany
* Lifespan: 1910 - 1990
* Title: Mathematician (Active in the fields of functional analysis and number theory)

He proposed this conjecture in 1937,
and for over 80 years since then, **no one has been able to prove or disprove it**.

By the way, this problem is so simple yet so profoundly deep,
that even Paul Erdős (a super famous mathematician) allegedly said this:

> "Mathematics may not be ready for such problems."

In other words, the theory is that humanity's mathematics hasn't caught up to this mystery yet...

---

## No "difficult formulas" are necessary

The great thing about the Collatz Conjecture is that **anyone can play with it**.

You can do it if you have pen and paper.
If you write code in Python, you can test it automatically.
And yet, **cutting-edge mathematicians are seriously challenging it**.

Doesn't that somehow make you excited?

---

## Bonus: Code to test it all at once

I'll also leave a piece of code here to try out various numbers all together.

```python
for n in range(1, 21):
    steps = collatz(n)
    print(f"{n}: {steps} (Number of steps: {len(steps)-1})")
```

This will spit out the Collatz sequences for "1 to 20" all at once.

---

## Conclusion: This world is mysterious after all

So, there you have it, the Collatz Conjecture.

* Even though it's incredibly simple
* No one can prove it
* It's a huge problem in the mathematical world

It's a phenomenon that's essentially a block of mystery.

Even beginners in programming can try it, so please do play around with it!

---

## Recommended Links (For those interested)

* [Wikipedia: Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture)
* [Terence Tao's paper (English)](https://arxiv.org/abs/1909.03562)
* Building a visualized version in Python is also fun! (I'll make one if there are requests)

---

If you'd like to know more topics like this "mysterious mathematics × programming,"
please feel free to request with a "tell me more."
Eventually, I'll introduce various things like the Riemann hypothesis and stories about prime numbers!

---

📮 The End!

---
