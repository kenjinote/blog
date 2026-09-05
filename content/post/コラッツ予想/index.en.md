---
title: 'Collatz Conjecture'
date: 2025-07-15T18:03:03+09:00
tags: ["Collatz Conjecture", "Math", "Programming", "Algorithm"]
draft: false
image: "img.png"
categories: ["Math, Cryptography, Quantum"]
---

# Is it true that "any number eventually becomes 1"? ── Playing with the Collatz Conjecture

Hello! I'm kenji.

Suddenly, but if you hear "a rule where any number eventually becomes 1",
isn't it a bit mysterious?

> For example, 19, or 87, or even 1000000.
> If you tweak the numbers according to appropriate rules, for some reason it converges to "1" at the end.

Such a dream-like story is the **Collatz Conjecture**.

---

## What is the Collatz Conjecture anyway?

First, let me introduce the rules.

* Start: Choose any **positive integer**
* Operation:

    * If it is even → Halve it (n → n / 2)
    * If it is odd → Triple it and add 1 (n → 3n + 1)

If you repeat this forever, the conjecture says that **any number will eventually reach 1**.

For example, starting from `6`:

```
6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
```

It properly became "1". Welcome back!

---

## Let's do it in code: Collatz in Python

Now, in times like this, it's faster to try it in code!
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

# Example: Starting from 19
print(collatz(19))
```

When you execute it:

```
[19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
```

It splendidly reaches 1.
Even though it takes quite a detour, it firmly reaches the goal at the end!


By the way, even if you start from 29, it reaches 1 in the same way.

```python
print(collatz(29))
```

When you execute it:

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

Moreover, there are scenes where it balloons to over 9000 along the way.
It's a pattern that takes a huge detour before reaching the goal.

---

## So, what's amazing about it in the end?

What's amazing about this conjecture is,

> **Even though it hasn't been proven, it seems to become 1 no matter what number you use**

That's the point.

Eh? Then, what about 1 trillion, or 10 quadrillion...?

If you thought that, you are sharp.
Actually, it has been verified up to about "2 to the 68th power" using computers,
and **all have reached 1**. Unbelievable...

But, **it hasn't been theoretically proven that "it always happens"**.
This is what they call an "unsolved problem" in the world of mathematics.

---

## Who is Mr. Collatz?

So, reading this far, you might wonder "who is Collatz anyway?".
Let me introduce him properly!

* Name: **Lothar Collatz**
* Nationality: Germany
* Year of birth: 1910 - 1990
* Title: Mathematician (Active in the fields of functional analysis and number theory)

He proposed this conjecture in 1937,
and since then, for over 80 years, **no one has been able to prove or disprove it**.

By the way, this problem is so simple yet so deep that
even Paul Erdős (a super famous mathematician) is said to have said this:

> "Mathematics may not be ready for such problems."

In other words, the theory that human mathematics hasn't caught up with this mystery yet...

---

## No "complex math formulas" are necessary

The good thing about the Collatz Conjecture is that **anyone can play with it**.

You can do it if you have paper and pen.
If you write code in Python, you can test it automatically.
And yet, **cutting-edge mathematicians are seriously challenging it**.

Doesn't it make you excited?

---

## Bonus: Code to test it all at once

I'll also include code to test various numbers all at once.

```python
for n in range(1, 21):
    steps = collatz(n)
    print(f"{n}: {steps} (Steps: {len(steps)-1})")
```

This outputs the Collatz sequences from "1 to 20" all at once.

---

## Conclusion: This world is indeed mysterious

So, that's the Collatz Conjecture.

* Even though it's super simple
* No one can prove it
* It's a huge problem in the math community

It's an existence like a cluster of mysteries.

Even programming beginners can try it, so please definitely play with it~!

---

## Recommended Links (For interested people)

* [Wikipedia: Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture)
* [Terence Tao Paper (English)](https://arxiv.org/abs/1909.03562)
* It's also fun to try making a visualizer in Python! (I'll make one if there's a request)

---

If you want to know more about this kind of "mysterious math x programming" topics,
please feel free to request "tell me more".
Eventually, I'll introduce various things like the Riemann hypothesis and prime numbers!

---

📮 The End!

---
