---
title: 'What is the "General Number Field Sieve (GNFS)", Humanity''s Strongest Math that Breaks Internet Cryptography?'
date: 2026-09-05T02:09:08+09:00
tags: ["Math", "Cryptography", "RSA", "GNFS"]
draft: false
image: "gnfs_two_worlds_1788542142485.jpg"
categories: ["Math, Cryptography & Quantum"]
---

# What is the "General Number Field Sieve (GNFS)", Humanity's Strongest Math that Breaks Internet Cryptography?

The internet we use every day. LINE messages, YouTube, Amazon shopping—all communications are protected by "cryptography."
Currently, the most widely used cryptography in the world is "RSA cryptography."

The cornerstone of RSA cryptography's defense is very simple. It utilizes the mathematical property that **"factoring a gigantic number into primes cannot be solved even by computers."**
For example, for "15", we immediately know it's "3 × 5", but the moment this becomes a "270-digit number", even if we bundle all the supercomputers in the world, it would take hundreds of millions of years to solve.

However, mathematicians do not stay silent either. To break this ironclad cryptography, humanity created a magical algorithm (calculation procedure) called the **"General Number Field Sieve (GNFS)"**.

In this article, without using any specialized jargon, and only with knowledge of **junior high school math (prime factorization, algebraic expressions, greatest common divisor)**, we will completely explain the mechanism step-by-step by which this "humanity's strongest algorithm" breaks cryptography!

---

## Chapter 1: The Goal of Decryption is a "Junior High School Formula"

The ultimate special move to confront gigantic prime factorizations. It's this formula learned in junior high school.

> **$X^2 - Y^2 = (X + Y)(X - Y)$**

You might think, "Eh, can such a basic formula break cryptography?" However, this is the master key that unlocks everything.

The ultimate goal for breaking the cryptography is to find, for a gigantic number $N$,
**"Numbers ($X$ and $Y$) where the remainder of $X^2$ and $Y^2$ divided by $N$ are the same."**

### Why does "same remainder" solve the cryptography?
Suppose two numbers, $X^2$ and $Y^2$, have the "same remainder when divided by $N$."
Having the same remainder means there is a rule that **the subtracted "$X^2 - Y^2$" will always be perfectly divisible by $N$ (it becomes a multiple of $N$)**.

Here, let's say the gigantic number $N$ used for cryptography is made of the multiplication of two secret prime numbers ($p$ and $q$) ($N = p \times q$).

Factoring $X^2 - Y^2$ results in **$(X - Y)(X + Y)$**.
The fact that this is a multiple of $N$ means that somewhere in this multiplication, the secret primes $p$ and $q$ are hidden.

Here a miracle occurs.
There is mathematically a **50% (1/2)** probability that the two prime numbers $p$ and $q$ will naturally separate into different rooms, with **"$p$ going to the $(X - Y)$ room"** and **"$q$ going to the $(X + Y)$ room"**.

With only the prime number $p$ in the $(X - Y)$ room, let's calculate the **"Greatest Common Divisor (the largest common part)"** of $(X - Y)$ and $N$.
* Contents of $(X - Y)$ = $p \times$ some number
* Contents of $N$ = $p \times q$
  The only common part is **"$p$"**!

In other words, the moment you calculate the greatest common divisor, the hidden prime number $p$ pops out, and the cryptography is completely decrypted. (*The greatest common divisor can be calculated instantly even on a smartphone using the "Euclidean Algorithm".)

**[A Little Column: Why squared? Why not cubed or doubled?]**
> If it's "$2X - 2Y$", it becomes $2(X - Y)$, and since there's only one room, you can't separate the primes. If it's "$X^3 - Y^3$", the size of the rooms becomes unbalanced, making the calculations unnecessarily heavy. To separate the primes into two, "squaring", which beautifully divides into two rooms, is the most cost-effective.

---

## Chapter 2: How to Find X and Y? The "Prime Card Collection Puzzle"

The goal is clear. However, if you blindly search for "$X^2$ and $Y^2$ that yield the same remainder", you won't find it until the end of the universe.
Therefore, mathematicians came up with a genius method called the **"Prime Card Collection Puzzle"**.

### Step 1: Collect Only Gold Dust (Smooth Numbers) with a Sieve
First, prepare an appropriate number $Z$, square it, and calculate the remainder $W$ when divided by $N$.
(The world of remainders where $Z^2 = W$)

Factorize the resulting remainder $W$. Here, only when a **"$W$ made only of small prime numbers like 2, 3, 5, 7"** appears, you keep that equation as a "winning card", and throw it away if large primes are mixed in.
It's a task like discarding large stones with a sieve in a river and collecting only gold dust.

### Step 2: The Puzzle of Making Everything an "Even Number"
For example, suppose the following three gold dust cards were collected.
* Card A: $Z_1^2 = 2^3 \times 3^1$
* Card B: $Z_2^2 = 2^1 \times 5^1$
* Card C: $Z_3^2 = 3^1 \times 5^1$

Let's multiply all these together.
The right side becomes $(2^3 \times 3^1) \times (2^1 \times 5^1) \times (3^1 \times 5^1)$, and
when summarized and organized, it becomes **"$2^4 \times 3^2 \times 5^2$"**.

Amazingly, the number of prime numbers became "4, 2, 2", which are **all even numbers**!
Having all even numbers means that if you halve the count of everything, it becomes the "square of something."
In other words, $(2^2 \times 3^1 \times 5^1)^2 = (60)^2$.

The left side is $(Z_1 \times Z_2 \times Z_3)^2$, so with this, finally,
**$X = (Z_1 \times Z_2 \times Z_3)$**
**$Y = 60$**
The long-awaited "$X^2 = Y^2$" pair is completed!

For computers, the puzzle of calculating whether the number of primes is "even or odd (0 or 1)" is something they are very good at, so with this method, they can find $X$ and $Y$ at high speed.

---

## Chapter 3: The Wall of Despair That Stands in the Way

Now any cryptography can be broken!... Or so we thought, but a big problem arises.
If the cryptography number $N$ is up to about "100 digits", it can be solved with this method (called the Quadratic Sieve), but when $N$ becomes "200 digits or 300 digits", the $W$ that appears during the calculation becomes too huge.

When the numbers get too huge, "numbers made only of small prime numbers (gold dust)" completely stop appearing. It becomes harder than searching for a contact lens in a desert, and you can't collect the cards to solve the puzzle at all.

Here finally, humanity's ultimate weapon, the **"General Number Field Sieve (GNFS)"**, makes its appearance.

---

## Chapter 4: Humanity's Strongest Idea, Creating "Two Worlds"

The genius idea of GNFS is: **"Calculating only in the real world makes the numbers huge. So, let's create a 'hidden world' using polynomials (algebraic expressions) and split the weight of the calculation into two."**

### The Magic of Algebraic Expressions
GNFS converts the gigantic number $N$ into an algebraic expression using a base number $m$.
For example, if $N=100$, let $m=4$, so $100 = 4^3 + 2(4^2) + 4$.
This is turned into the expression (the hidden world) **$f(x) = x^3 + 2x^2 + x$** using the letter $x$.

The interesting thing about this expression is that it has the property: **"If you substitute $m$ (4 in the example above) for the letter $x$, you can always warp back to the real number $N$."**

### Searching for Gold Dust in Two Worlds Simultaneously
GNFS creates many pairs of random integers $(a, b)$ and performs the following two calculations simultaneously.
1. **Real World**: $a - b \times m$
2. **World of Algebraic Expressions**: The value calculated by the rules of algebraic expressions for $a - b \times x$

By splitting the problem into two worlds, the size of the numbers handled becomes dramatically smaller (lighter). It's the image of splitting a huge rock into two to make them easy-to-handle stones.

Then, you sift and collect only the miracle pairs $(a, b)$ where **"Both in the real world and in the world of algebraic expressions, they are 'made only of small prime numbers (gold dust)'"**. This is the origin of the name "Number Field Sieve."

### The Moment the Cryptography is Finally Broken
Once tens of millions of "gold dust cards" are collected from both worlds, using the giant matrix calculations of supercomputers, you find the "combination where the number of prime numbers all become even", just as we did in Chapter 2.

Once the combination is found,
* Let the squared number made in the real world be **$X^2$**
* Let the squared expression made in the world of algebraic expressions be **$Y(x)^2$**

Finally, substitute $m$ into $x$ of $Y(x)$ in the world of algebraic expressions to warp to the real world and merge them.
Then, just like mathematical magic, a state where **"the remainders of $X^2$ and $Y^2$ are the same"** is strictly completed!

After that, just like in Chapter 1, if you calculate the greatest common divisor of $X - Y$ and $N$, the impregnable RSA cryptography collapses with a crash, and the secret primes reveal themselves.

---

## Conclusion: Mathematics Never Ends

You might have thought, "Alright, with GNFS, any cryptography can be broken!"
However, RSA cryptography is not giving up either. What is currently used on the internet is a monstrously huge number called "RSA-2048 (about 617 digits)".

Even though GNFS is humanity's strongest algorithm, it is said that even to solve 270 digits (RSA-270), it would take thousands or tens of thousands of years even if all the computers in the world were connected. For now, our LINE and bank data are safe.

But what if a **"magic that instantly finds $X$ and $Y$ for any gigantic number"** appears?
Actually, the closest thing to that is the **"Quantum Computer (Shor's Algorithm)"** currently under development. It has been mathematically proven that by using the wave properties of quantum mechanics, one can ignore the tedious card collecting puzzle and draw the answer in one shot.

The endless battle of wits between the people who make cryptography (defense) and the people who make algorithms to break it (attack).
When you learn that the "prime factorization" and "algebraic expressions" learned in junior high school are actually weapons fiercely fighting on the front lines of global security, doesn't math class seem just a little bit more interesting?

The person to discover the strongest algorithm of the future might just be you reading this article!

---
*(Note: This article conceptualizes the mathematical charm of cryptography decryption for junior high school students. Actual GNFS is strictly calculated using advanced university mathematics such as ideal class groups of algebraic number fields and homomorphisms.)*
