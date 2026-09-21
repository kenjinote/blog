---
title: "Introduction to Dynamic Programming (DP) and Famous Problems (Knapsack, Fibonacci)"
description: "Overcome the algorithm hurdle 'Dynamic Programming (DP)'. We explain the difference between memoized recursion and the bottom-up approach in an easy-to-understand way, using the Fibonacci sequence and the Knapsack problem as examples."
slug: "dynamic-programming-dp-introduction-knapsack-fibonacci"
date: 2026-09-22T04:00:00+09:00
image: "eyecatch.jpg"
categories: ["computer-science"]
tags: ["algorithms", "dynamic-programming", "dp", "knapsack", "optimization"]
---

# 1. Introduction

As you progress in learning programming and algorithms, there is a major wall that many learners face. That is **Dynamic Programming** (abbreviated as **DP**). Just hearing the name might make you brace yourself, thinking, "It sounds difficult" or "Does it require specialized mathematical knowledge?" However, once you understand the essence, you will find that DP is a very powerful and intuitive problem-solving technique.

In this article, we will start from the basic concepts of DP and thoroughly explain the way of thinking and implementation methods using the "Fibonacci sequence" and the "Knapsack problem," which are representative problems. Let's deepen our understanding step by step with Python code.


# 2. What is Dynamic Programming (DP)?

Dynamic Programming is a technique that divides a complex problem into multiple smaller subproblems and proceeds to solve them while recording (memoizing) the solution of each subproblem. This eliminates the waste of repeating the same calculations and can dramatically reduce computation time.

The core of DP lies in the following two characteristics:

1. **Optimal Substructure**: The property that the optimal solution of a large problem can be constructed from the optimal solutions of its smaller subproblems.
2. **Overlapping Subproblems**: The property that the same small problems appear repeatedly.

For problems with these characteristics, DP is extremely powerful.

## Two Approaches to DP

There are broadly two implementation approaches to DP.

### 1. Memoized Recursion (Top-Down Approach)
Start from a large problem and recursively call smaller problems. At that time, save (memoize) the calculated result in an array or hash map, and when the same problem appears again, return the memoized value without recalculating.

### 2. Bottom-Up Approach (Divide and Conquer and Table Filling)
Calculate the solutions starting from the smallest problem and record them in an array (DP table). Gradually solve larger problems using the solutions of smaller problems, and finally obtain the solution to the problem you want to solve.


# 3. Basics: Learning DP with the Fibonacci Sequence

As a first step to understand the concept of DP, we will take up the Fibonacci sequence.

The Fibonacci sequence is a sequence defined as follows:
$ F(0) = 0 $
$ F(1) = 1 $
$ F(n) = F(n-1) + F(n-2) \quad \text{for } n \ge 2 $

## 3.1 The Trap of Simple Recursive Calls

Let's write a function in Python exactly as defined.

```python
def fib_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)
```

This implementation is intuitive, but there is a major problem. That is, **the computational complexity increases exponentially**. Let's look at the function call tree when calculating $F(5)$.

```mermaid
graph TD
    A["F("5")"] --> B["F("4")"]
    A --> C["F("3")"]
    B --> D["F("3")"]
    B --> E["F("2")"]
    C --> F["F("2")"]
    C --> G["F("1")"]
    D --> H["F("2")"]
    D --> I["F("1")"]
    E --> J["F("1")"]
    E --> K["F("0")"]
    F --> L["F("1")"]
    F --> M["F("0")"]
    H --> N["F("1")"]
    H --> O["F("0")"]
```

As you can see, $F(3)$ and $F(2)$ are calculated over and over again. The computational complexity is $O(2^n)$, and as $n$ becomes large, the computation will not finish in a practical amount of time.

## 3.2 Memoized Recursion (Top-Down Approach)

What eliminates this waste is **memoization**. Let's save the calculated results.

```python
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
```

With this, each $F(i)$ is calculated only once, and the computational complexity drops drastically to $O(n)$.

## 3.3 Bottom-Up Approach (DP Table)

To avoid the overhead of recursive calls, the bottom-up approach calculates from the bottom up.

```python
def fib_dp(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
        
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n]
```

Prepare an array `dp` and fill it in order starting from the smallest index. This is a typical use of a DP table.


# 4. Applications: Knapsack Problem

The true worth of DP is demonstrated when solving optimization problems. Here, let's consider the famous "0-1 Knapsack problem."

## 4.1 Problem Setting

You are a thief (that is the setting). You have a knapsack with capacity $W$. In front of you, there are $N$ items, and each item $i$ has a weight $w_i$ and a value $v_i$.

Select items within a range that does not exceed the knapsack's capacity, and **maximize the total value** of the items you take home. However, there is only one of each item, and you either "choose (1)" or "don't choose (0)" it.

## 4.2 State Definition and Recurrence Relation

When solving a problem with DP, the most important things are the **state definition** and the derivation of the **recurrence relation (state transition equation)**.

Define the state as follows:
$dp[i][w]$: The maximum value when choosing from the first $i$ items such that the total weight is $w$ or less.

Here, when considering the $i$-th item (weight $w_i$, value $v_i$), you have the following two choices:

1. **When not choosing**:
    The maximum value is the same as the previous state $dp[i-1][w]$.
2. **When choosing** (only possible if $w \ge w_i$):
    Add the value $v_i$ of item $i$ to the state where $w_i$ is subtracted from the capacity. That is, $dp[i-1][w - w_i] + v_i$.

Therefore, the recurrence relation is as follows:

$$
dp[i][w] = 
egin{cases}
\max(dp[i-1][w], dp[i-1][w - w_i] + v_i) & 	ext{if } w \ge w_i \
dp[i-1][w] & 	ext{otherwise}
\end{cases}
$$

## 4.3 Python Implementation

Drop this recurrence relation exactly into a program.

```python
def knapsack(weights, values, W):
    N = len(weights)
    # Initialize DP table: (N+1) x (W+1) 2D array
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    
    # Fill the DP table
    for i in range(1, N + 1):
        for w in range(W + 1):
            if w >= weights[i-1]:
                # Take the maximum of choosing and not choosing
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            else:
                # When it cannot be chosen due to exceeding capacity
                dp[i][w] = dp[i-1][w]
                
    return dp[N][W]
```

### Transition of the DP Table

Let's trace the transition of the `dp` table in an example.

| $i$ \ $w$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 3 | 3 | 3 | 3 |
| 2 | 0 | 2 | 3 | 5 | 5 | 5 |
| 3 | 0 | 2 | 3 | 5 | 6 | 7 |
| 4 | 0 | 2 | 3 | 5 | 6 | 7 |

In this way, by finding the optimal solutions starting from subproblems with small capacity and a small number of items, the answer is finally obtained.


# 5. Detailed Explanation and Algorithmic Exploration for a Deeper Understanding of DP

To solidify your understanding of DP, it is essential to be exposed to more examples and learn state transitions of various patterns.

## 5.1 Edit Distance (Levenshtein Distance)

Given two strings $S$ and $T$, this is the problem of finding the minimum number of "insert," "delete," and "replace" operations on $S$ to convert it to $T$.

### Recurrence Relation

$$
dp[i][j] = 
egin{cases}
dp[i-1][j-1] & 	ext{if } S[i-1] == T[j-1] \
\min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1 & 	ext{otherwise}
\end{cases}
$$

## 5.2 Space Complexity Optimization Technique (In-place Updating)

In previous implementations, $O(NW)$ or $O(MN)$ memory was used to calculate state transitions. However, if you observe the recurrence relation closely, you will often find that only the "previous row" is needed to update a state.

For example, using the recurrence relation of the Knapsack problem, a 2D array can be reduced to a 1D array. When updating, by updating from right to left, you can prevent the bug of overwriting the value of $i-1$ during the calculation of the current $i$.

```python
def knapsack_optimized(weights, values, W):
    N = len(weights)
    dp = [0] * (W + 1)
    
    for i in range(N):
        # By updating in reverse order, a 1D array is sufficient
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
            
    return dp[W]
```


### Advanced Explanation Part 1: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 2: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 3: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 4: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 5: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 6: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 7: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 8: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 9: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 10: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 11: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 12: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 13: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 14: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 15: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 16: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 17: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 18: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 19: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 20: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 21: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 22: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 23: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 24: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 25: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 26: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 27: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 28: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 29: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 30: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 31: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 32: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 33: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 34: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 35: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 36: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 37: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 38: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 39: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

### Advanced Explanation Part 40: Limitations of DP and Algorithm Selection

The strength of dynamic programming is that it avoids overlapping subproblems, but that still doesn't mean all problems can be solved quickly. For example, the computational complexity of the Knapsack problem is $O(NW)$, which at first glance looks like polynomial time. However, $W$ is the "value" of the input, and it can be exponentially large relative to the input size (number of bits). Such computational complexity is called **pseudo-polynomial time**.

If $W$ is extremely large, this DP technique cannot be applied because simply allocating the array will exhaust memory and the number of loop iterations will be enormous. In that case, you need to switch to DP with respect to the upper limit $V$ of the sum of values, or use another approach such as half enumeration (Meet in the Middle).

Also, when debugging DP, it is most effective to **compare the table calculated by hand with small-scale inputs and the table output by the program**. By preparing paper and a pen and actually drawing a 2D table, you can easily understand "why this recurrence relation is formed" and "where the transition is wrong."

# 6. Conclusion

Dynamic programming (DP) might feel unapproachable at first. However, by starting with the intuitive understanding of "eliminating wasteful calculations" in the Fibonacci sequence and taking steps toward "defining states and transitions" like in the Knapsack problem, you can definitely master it.

**"How to define the state"**
**"From what smaller states can that state be calculated (recurrence relation)"**

The shortest way to cultivate the ability to see through these two points is to be exposed to many problems and try writing DP tables with your own hands. By all means, please try taking on challenges using the knowledge learned in this article as a weapon.
