---
title: 'Sleeping Beauty Paradox: Is the coin probability 1/2 or 1/3? A difficult problem dividing probability theory'
slug: 'sleeping-beauty-paradox'
description: '"Now that you are awake, what is the probability that the coin toss resulted in heads?" We explain the latest paradox that continues to divide mathematicians and philosophers worldwide into the "1/2 camp" and the "1/3 camp" despite its very simple setup.'
date: '2026-09-10T09:00:00+09:00'
image: 'img/sleeping_beauty.jpg'
math: true
mermaid: true
categories:
  - 'Mathematical Paradoxes'
  - 'Probability Theory'
tags:
  - 'Paradox'
  - 'Conditional Probability'
  - 'Bayes Theorem'
  - 'Philosophy'
---

## 1. The Rules of a Strange Experiment

You (Sleeping Beauty) have been selected as a subject for a certain scientific experiment.
The experiment runs from Sunday to Wednesday. On Sunday night, you are given a sleeping pill and fall asleep.

After you fall asleep, the experimenter tosses a **single fair coin** (a coin with an exactly 1/2 probability of landing heads or tails). And depending on the result, you will be awakened according to the following schedule.

**[If the coin toss result is "Heads"]**
- You will be awakened once on Monday and asked a question. After that, you will be put back to sleep and will not awaken again until the experiment ends (Wednesday).

**[If the coin toss result is "Tails"]**
- You will be awakened on Monday and asked a question. After that, you will be given a special drug (an amnesia drug) and put back to sleep.
- You will be awakened once more on Tuesday and asked the same question. After that, you will be put back to sleep again, and the experiment will end (Wednesday).

* Due to the effects of the amnesia drug, when you awaken, you will not be able to remember "what day of the week it is today" or "whether you have been awakened in the past" at all.

```mermaid
graph TD
    Sunday["Sunday: Beauty goes to sleep"] --> Toss{"Coin Toss"}
    
    Toss -->|Heads (1/2)| Mon_Heads["Monday: Awaken + Question<br>(Then experiment ends)"]
    Toss -->|Tails (1/2)| Mon_Tails["Monday: Awaken + Question<br>(Then amnesia)"]
    
    Mon_Tails --> Tue_Tails["Tuesday: Awaken + Question<br>(Then experiment ends)"]
    
    style Toss fill:#ff9999,stroke:#333
    style Mon_Heads fill:#aaffaa,stroke:#333
    style Mon_Tails fill:#aaffaa,stroke:#333
    style Tue_Tails fill:#aaffaa,stroke:#333
```

Now, it is Monday (or Tuesday), and you have awakened.
There are no clocks or calendars in the room, so you do not know what day it is today.

There, the experimenter comes in and asks you this question.
**"Given that you are currently awake, what do you think is the probability that the tossed coin was 'Heads'?"**

You are a beauty well-versed in mathematics. Now, how do you answer?

---

## 2. Two Clashing Factions: 1/2 or 1/3?

This problem was devised in the 1990s and published in an academic journal by philosopher Adam Elga in 2000.
The probability of the coin seems obvious, but actually, over this problem, mathematicians, statisticians, and philosophers around the world have split cleanly into two camps: the **"1/2 Faction (Halfers)"** and the **"1/3 Faction (Thirders)"**, engaging in fierce debate to this day.

Let's hear the "perfect logic" of each camp.

### The Claim of the "1/2 Faction (Halfers)"
> "Since the coin is a fair coin with no cheating, the probability of heads coming up is naturally 1/2.
> No matter how many times the experimenter wakes me up or erases my memory after I fall asleep, it **does not affect the physical outcome of the coin at all**.
> The probability at the time the coin was tossed was 1/2, and my waking up gives me no new information (clues to guess whether it is heads or tails). Therefore, the probability remains 1/2."

This is a very sound opinion that emphasizes objective physical phenomena and the non-update of information.

### The Claim of the "1/3 Faction (Thirders)"
> "The very fact that you are 'awake' is information that changes the probability.
> Suppose we repeated this experiment 100 times (100 weeks).
> The coin should be 'Heads' 50 times and 'Tails' 50 times.
> 
> - For the 50 weeks where Heads comes up, you awaken only once on Monday $\rightarrow$ **Number of awakenings for 'Heads' is 50 times**
> - For the 50 weeks where Tails comes up, you awaken twice, on Monday and Tuesday $\rightarrow$ **Number of awakenings for 'Tails' is 100 times**
> 
> In other words, the situation of the moment you wake up has 150 times in total, out of which the 'pattern of awakening on Heads' is 50 times, and the 'pattern of awakening on Tails' is 100 times.
> Therefore, the probability that the awakening you are currently experiencing is 'Heads' is 50 / 150 = **1/3**!"

This is a powerful opinion based on "frequentism" or the "anthropic principle," which incorporates the very situation that "you currently exist (are observing)" into the calculation as an element of the probability space.

---

## 3. Calculating with Bayes' Theorem

There is also an attempt to unravel this problem using "Bayes' Theorem," a tool for mathematically updating probabilities.
Let's organize the logic of the "1/3 faction" from the perspective of conditional probability.

Your state when you awaken is one of the following three:
1. $E_1$: The coin is "Heads", and it is now "Monday"
2. $E_2$: The coin is "Tails", and it is now "Monday"
3. $E_3$: The coin is "Tails", and it is now "Tuesday"

The probability of "Heads" is $1/2$, and the probability of "Tails" is $1/2$.
However, in the case of Tails, "Monday" and "Tuesday" are perfectly symmetrical (you cannot distinguish them since you have no memory), so it is thought that $E_2$ and $E_3$ are equally likely to occur.

Since the sum of the overall probabilities must be $1$, if we assign equal probability to each awakening as an independent "event (observation point)":
$P(E_1) = 1/3$
$P(E_2) = 1/3$
$P(E_3) = 1/3$
Thus, the conclusion is that the "probability it was Heads ($P(E_1)$)" is $1/3$.

On the other hand, the "1/2 faction" argues against this, stating, "Monday and Tuesday when the coin is Tails ($E_2$ and $E_3$) are merely dependent events derived from the single result of one coin toss, and it is wrong to count them as independent probabilities in the first place."

---

## 4. Why Does This Problem Not Get Resolved?

The reason why the "Sleeping Beauty problem" plagues scholars so much is not due to a mere calculation error or illusion.
It is because this problem touches upon the deepest and most fundamental question of probability theory: **"What exactly is probability?"**

- For the **1/2 faction**, probability is a "physical property of the coin" or an "objective fact".
- For the **1/3 faction**, probability is the "degree of belief of the observer (Beauty)" or the "frequency of observation".

Profound themes that connect to the "measurement problem" in quantum mechanics and the "anthropic principle" in cosmology (the idea of calculating the probability of the universe backward from the fact that we exist) are condensed into this simple coin toss experiment.

## 5. Summary

If you were a subject in this experiment, would you answer "1/2" or "1/3" when you wake up?

Whichever you answer, world-class mathematicians will stand behind you to defend you.
How a seemingly simple mathematical definition collapses the moment it is tied to troublesome concepts like human "subjectivity" and "existence." The paradox continues to shake our common sense today.
