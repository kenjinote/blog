---
title: "Does seeing a blue apple prove 'ravens are black'? : Hempel's Ravens"
description: "Can we prove the hypothesis that 'all ravens are black' without ever seeing a single raven? The paradox of induction created by logical equivalence."
date: 2026-09-10T21:00:00+09:00
draft: false
slug: "hempels-ravens"
image: "img/hempels_ravens.jpg"
math: true
mermaid: true
categories: ["Mathematical Paradoxes", "Logic"]
tags: ["Paradox", "Induction", "Logical Equivalence", "Contrapositive"]
---

How do scientists prove theories? Usually, they use "induction," gathering data by observing the world.
For example, if you wanted to prove the hypothesis that "all ravens are black," you would observe ravens around the world and confirm one by one that they are black.

However, in the 1940s, logician Carl Hempel pointed out a strange logical loophole hidden in this commonplace scientific method.
This is the paradox of **Hempel's Ravens**, which states that **"simply seeing a blue apple or a red shoe serves as evidence that 'ravens are black'."**

## Logical Substitution: The Magic of the Contrapositive

To understand Hempel's argument, we must recall the concept of the **"contrapositive"** learned in high school mathematics.

In logic, if a proposition "If A, then B" is true, its contrapositive "If not B, then not A" must also be true (this is called logical equivalence).

Hypothesis $H_1$: **"All ravens are black (If it is a raven, then it is black)"**

Let's take the contrapositive of this hypothesis $H_1$.
It becomes "If it is not black, then it is not a raven."

Hypothesis $H_2$: **"Everything that is not black is not a raven"**

According to the rules of logic, $H_1$ and $H_2$ have **exactly the same meaning (equivalence)**. If one is proven, the other is automatically proven as well.

## Proving Ravens Without Seeing Ravens

Now, to confirm hypothesis $H_1$ (ravens are black), every time you find a black raven, the certainty (evidence) of the hypothesis gets a little stronger.
This is something everyone can agree on.

However, since $H_1$ and $H_2$ mean the same thing, finding evidence for hypothesis $H_2$ (things that are not black are not ravens) should directly serve as evidence for hypothesis $H_1$.

So, what constitutes evidence for $H_2$?
You just need to find something that is "not black and not a raven."

- Suppose there is a **"blue apple"** on the table. It is not black, and it is not a raven. Therefore, it is evidence supporting $H_2$.
- There are **"red shoes"** in the closet. These are also not black and not ravens. They are evidence for $H_2$.
- A **"white cloud"** is floating in the sky. This is also evidence for $H_2$.

Since evidence for $H_2$ holds the same value as evidence for $H_1$, the following bizarre conclusion is logically derived:

**"The more you observe blue apples and red shoes in a room, the more the hypothesis 'all ravens are black' is proven to be true."**

```mermaid
graph TD
    A["Proposition H1: All ravens are black"] <-->|Logical equivalence (Contrapositive)| B["Proposition H2: What is not black is not a raven"]
    
    C["Observation: Black raven"] -->|Serves as evidence for| A
    D["Observation: Blue apple"] -->|Serves as evidence for| B
    
    D -.->|Therefore, this should also be evidence for?| A
    
    style A fill:#4CAF50,stroke:#333,stroke-width:2px,color:#fff
    style B fill:#4CAF50,stroke:#333,stroke-width:2px,color:#fff
    style C fill:#2196F3,stroke:#333,color:#fff
    style D fill:#FF9800,stroke:#333,color:#fff
```

## Why Is It Counterintuitive?

No ornithologist anywhere in the world grows more convinced that "ravens are black" by looking at a blue apple. Although it should be perfectly correct logically, why does our common sense reject this?

Several approaches have been proposed in the fields of philosophy and statistics to address this paradox.

### 1. The Bayesian Solution (Difference in Information Content)

The most compelling counterargument from the perspective of modern statistics (Bayesian probability) focuses on the difference in the "strength of evidence (information content)."

In the world, there are overwhelmingly more "things that are not black" than "black things," and astronomically more "things that are not ravens" than "ravens."

When you see a blue apple, it certainly serves as evidence that "all ravens are black," but **its value as evidence (the increase in probability) is infinitely close to zero**.
Confirming just one of the countless "non-black things" in the vast universe raises the probability that "ravens are black" by an amount comparable to the effect of removing a single grain of sand from a desert. On the other hand, directly finding one black raven carries an overwhelmingly greater evidentiary value.

In other words, the Bayesian solution is that logically "a blue apple is evidence," but practically "its evidentiary value is equal to zero and can be ignored."

### 2. The Limits of "Indoor Ornithology"

This paradox highlights how the foundation of science known as "induction (deriving general laws from observation)" rests on a fragile premise. Relying solely on logical equivalence would enable "indoor ornithology," where one could verify any universal law ("all swans are white," "no aliens are green," etc.) simply by observing the junk in a room without ever going outside.

Hempel's Ravens is a fascinating paradox that shows that the words "evidence" and "proof" we unconsciously use cannot be fully captured by the rules of pure symbolic logic alone.
