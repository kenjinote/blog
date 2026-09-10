---
title: 'St. Petersburg Paradox: How Much Would You Pay for a Gamble with "Infinite" Expected Value?'
slug: 'st-petersburg-paradox'
description: 'A gamble that is mathematically supposed to make you "infinite money". Yet, in reality, nobody would pay a large sum for it. We explain the historical paradox that highlighted the gap between probability theory and human psychology (utility), laying the foundation of modern economics.'
date: '2026-09-10T05:00:00+09:00'
image: 'img/st_petersburg.jpg'
math: true
mermaid: true
categories:
  - 'Mathematical Paradox'
  - 'Probability Theory'
tags:
  - 'Paradox'
  - 'Expected Value'
  - 'Economics'
  - 'Bernoulli'
---

## 1. The Dream Gamble with "Infinite" Expected Value

As you walk through a casino, a dealer invites you to play a new coin toss game.

**[Game Rules]**
1. You pay an entry fee to start the game.
2. You toss a coin. If it lands on **Heads**, your prize money doubles, and you get to toss again.
3. The game ends as soon as it lands on **Tails**. You receive the prize money accumulated up to that point.

The initial prize starts at $2.
- If it lands on Tails on the 1st toss, you get **$2** and the game ends.
- If it's Heads on the 1st and Tails on the 2nd, you get **$4** and the game ends.
- If it's Heads on the 1st and 2nd, and Tails on the 3rd, you get **$8** and the game ends.
- ...From then on, as long as Heads keep appearing, the prize doubles to $16, $32, $64... and so on.

```mermaid
graph TD
    Start["Game Start"] --> Toss1{"1st Coin Toss"}
    
    Toss1 -->|Tails (1/2)| End1["End: Win $2"]
    Toss1 -->|Heads (1/2)| Toss2{"2nd Coin Toss"}
    
    Toss2 -->|Tails (1/2)| End2["End: Win $4"]
    Toss2 -->|Heads (1/2)| Toss3{"3rd Coin Toss"}
    
    Toss3 -->|Tails (1/2)| End3["End: Win $8"]
    Toss3 -->|Heads (1/2)| Toss4{"..."}
    
    Toss4 -.->|The longer the streak| Infinite["Prize doubles infinitely!"]
```

Now, here is a question for you.
**If the entry fee for this game were "$10,000 (about 1.5 million yen)", would you participate?**

Most people would probably say "I won't participate". Because there is a 50% chance of getting Tails on the first toss, meaning you would only get $2 and suffer a massive loss.

However, if you calculate this strictly according to mathematical probability theory (expected value), a surprising fact emerges. **Mathematically, whether the entry fee is $10,000 or $100 million, you should participate in this game even if you have to borrow your entire net worth.**

Why on earth is that?

---

## 2. Let's Calculate the Expected Value

To determine whether a gamble is "profitable or not", we use a mathematical metric called **"expected value"**.
The expected value is a number that represents "how much you will make on average per game if you repeat the game many times". The formula is **the sum of all "(prize money) × (probability of getting it)"**.

Let's calculate the expected value for this game.

- **Probability of getting Tails on the 1st toss:** $\frac{1}{2}$
  Prize is $2$.
  Contribution to expected value = $2 \times \frac{1}{2} = 1$ dollar

- **Probability of getting Tails on the 2nd toss:** Getting Heads then Tails, so $\frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$
  Prize is $4$.
  Contribution to expected value = $4 \times \frac{1}{4} = 1$ dollar

- **Probability of getting Tails on the 3rd toss:** Getting Heads, Heads, then Tails, so $(\frac{1}{2})^3 = \frac{1}{8}$
  Prize is $8$.
  Contribution to expected value = $8 \times \frac{1}{8} = 1$ dollar

- **Probability of getting Tails on the $n$-th toss:** $(\frac{1}{2})^n$
  Prize is $2^n$ dollars.
  Contribution to expected value = $2^n \times (\frac{1}{2})^n = 1$ dollar

In other words, no matter what toss the game ends on, the expected value for that pattern is **always "$1"**.
Since the game can potentially continue infinitely, adding all these expected values together results in the following:

$$ \text{Total Expected Value} = 1 + 1 + 1 + 1 + \dots = \infty \text{ (Infinity)} $$

The answer derived by mathematics is **"the expected value of this game is infinite"**.
Since the expected value is infinite, no matter how high the entry fee is, theoretically it is an absolutely "profitable gamble".

This is the **"St. Petersburg Paradox"**, proposed by Nicolaus Bernoulli in 1713.
There is a fierce contradiction between the correct mathematical calculation result (having infinite value) and human realistic sensation (only wanting to pay a few dollars).

---

## 3. The Discovery of "Utility" that Resolves the Gap between Mathematics and Humans

The one who solved this paradox was Daniel Bernoulli, a genius mathematician and cousin of Nicolaus. (It got this name because he presented this paper at the Academy of Sciences in St. Petersburg.)

Daniel delved into human psychology.
He thought, **"Humans do not judge things by the 'absolute monetary amount', but by the 'satisfaction (utility)' that the money brings."**

This is called the **"Law of Diminishing Marginal Utility"**.

### The value of money decreases depending on the amount you hold
For example, when you are extremely thirsty in a desert, the first glass of water has enough value (satisfaction) that you would "want to drink it even if you had to pay 10,000 yen". However, as you drink the second and third glasses, the value of a single glass of water rapidly drops. By the 10th glass, you would likely say "I wouldn't want it even if it were free".

The same goes for money.
- "1 million yen" given to someone with zero savings has immense, life-saving value.
- However, "1 million yen" given to Elon Musk, who has a net worth of tens of billions, only holds about as much value (satisfaction) as a 1-yen coin found on the street.

In other words, even if the prize money doubles infinitely like $2 \rightarrow $4 \rightarrow $8 \rightarrow $16..., **the "happiness (utility)" a human feels does not increase infinitely in proportion to the amount**.

---

## 4. Recalculating the Expected Value using "Utility"

Daniel Bernoulli assumed that "the value (utility) of money felt by humans is proportional to the logarithm ($\log$) of the amount".

Let the amount be $x$, and let's express the value (utility) felt by humans $u(x)$ as a logarithmic function (here we consider a simple model with a base of 2).

- Utility of $2 prize: $\log_2(2) = 1$
- Utility of $4 prize: $\log_2(4) = 2$
- Utility of $8 prize: $\log_2(8) = 3$
- Utility of $2^n$ prize: $\log_2(2^n) = n$

The amount doubles each time, but human "happiness" only increases little by little like 1, 2, 3...
Using this "utility", let's calculate the expected value (**expected utility**) again.

$$ \text{Expected Utility} = \sum_{n=1}^{\infty} \left( n \times \left(\frac{1}{2}\right)^n \right) $$
$$ = 1 \cdot \frac{1}{2} + 2 \cdot \frac{1}{4} + 3 \cdot \frac{1}{8} + 4 \cdot \frac{1}{16} + \dots $$

When you calculate the sum of this infinite series, the result does not become "infinite", but **converges to "2".**
If we reverse calculate the amount for which the utility is "2", it becomes $2^2 = 4$ dollars.

In other words, when recalculated by incorporating human psychology (utility), a very common-sense and realistic answer is derived: **"The value of this game is about '$4' according to human sensation."**
That is precisely why we do not feel like paying $10,000 for this game.

---

## 5. Conclusion: The Paradox that Opened the Door to Economics

The St. Petersburg Paradox was a groundbreaking paradox that mathematically proved that the objective number of "monetary amount" and the subjective value of "human satisfaction" do not match.

The concept of "Utility" proposed by Daniel Bernoulli, 200 years later, became the most important foundation of modern microeconomics and financial engineering (such as portfolio theory).
The behavior of us buying insurance or diversifying investments can all be explained by this human psychological mechanism of "diminishing marginal utility (the pain of a huge loss is far greater than the joy of a huge gain)".

A simple calculation problem of gambling ended up deciphering the human mind and triggering the birth of the massive academic discipline of economics.
