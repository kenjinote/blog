---
title: 'Tower of Hanoi'
slug: "ハノイの塔"
date: 2025-04-17T22:23:14+09:00
tags: ["Tower of Hanoi", "Algorithm", "Python"]
draft: false
image: "img.png"
categories: ["Programming"]
---

# Tower of Hanoi

Hello!

Today, I would like to explain the "Tower of Hanoi" along with a Python sample program.

---

## What is the Tower of Hanoi?

The Tower of Hanoi is a puzzle using three rods and multiple disks. The disks vary in size and are initially stacked on one rod in decreasing order of size. The rules are as follows:

1. Only one disk can be moved at a time.
2. A larger disk cannot be placed on top of a smaller disk.

This puzzle is considered an excellent teaching material for learning recursive thinking. Recursion is a method of solving a problem by breaking it down into smaller problems of the same type. In the Tower of Hanoi, to move n disks, the operation of moving n-1 disks is repeated.

---

## Let's Solve the Tower of Hanoi in Python

Below is a sample code to solve the Tower of Hanoi in Python.


```python
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)

# Example: Move 3 disks from A to C
hanoi(3, 'A', 'C', 'B')
```


In this code, the `hanoi` function is called recursively, and the steps to move the disks are printed. For example, in the case of 3 disks, you will get the following output:


```
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
```

In this way, by using a recursive approach, even complex problems can be solved simply.

---

## How Long Does It Take to Move 64 Disks?

The minimum number of moves for the Tower of Hanoi is 2^n - 1. This means that to move 64 disks, it requires 2^64 - 1 moves, or approximately 1.84 × 10^19 moves. Even if you could make one move per second, it would take about 584.9 billion years. This is roughly 42 times the age of the universe (about 13.7 billion years).

Thus, as the number of disks increases, the required number of moves increases exponentially. Therefore, it is not realistic to actually move 64 disks.

---

## Conclusion

The Tower of Hanoi is a perfect puzzle for learning recursive thinking. Using Python, you can easily implement its solution. However, care must be taken as the required number of moves increases sharply as the number of disks increases.

By understanding the recursive approach and actually writing the code, you can improve your programming skills. By all means, give the Tower of Hanoi a try.

---
