---
title: 'Monty Hall problem'
date: 2024-03-31T23:41:51+09:00
tags: ["Math", "Probability", "Monty Hall problem"]
draft: false
image: "img_1.png"
categories: ["Math・Cryptography・Quantum"]
---

## What is the Monty Hall problem?
The Monty Hall problem is a brain teaser, in the form of a probability puzzle, loosely based on the American television game show "Let's Make a Deal" and named after its original host, Monty Hall. The problem is as follows:

Premise: One of the three doors has a prize behind it, and the other two have a dud (goat).

1. The participant chooses one of the three doors.
2. The host opens one of the other two doors that the participant did not choose, revealing a dud.
3. The participant is asked whether they want to change their chosen door.

The problem is to consider whether the participant should change the door or not.

## Solution
The solution to the Monty Hall problem is as follows:

1. If the participant does not change the initially chosen door
   - Probability of winning: 1/3
   - Probability of losing: 2/3

2. After the host opens the dud door
    - If not changed, probability of winning: 1/3 (Does not change from the winning probability in step 1.)
    - If changed, probability of winning: 2/3 (The probability of the remaining options.)

Therefore, the participant has a higher probability of winning by changing the door.

## Reference
- Wikipedia [Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem)
