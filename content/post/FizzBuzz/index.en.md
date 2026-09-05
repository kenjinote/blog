---
title: 'FizzBuzz'
date: 2025-04-18T00:58:11+09:00
tags: ["FizzBuzz", "Python", "Algorithm"]
draft: false
image: "img.png"
categories: ["Programming"]
---

## What exactly is FizzBuzz, anyway?

Hello!

Today, I'd like to write about "FizzBuzz".

Whether you're thinking, "Ah, I know that one!" or "I've heard of it, but don't really get it," please stick with me for a bit. It takes just a few minutes to read, and you might just have an "aha" moment.

---

### Is it true that "you're disqualified as a programmer if you can't write FizzBuzz"?

Roughly speaking, FizzBuzz looks like this.

```python
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

Yes, this is the famous "FizzBuzz problem."

You go through the numbers from 1 to 100 in order,  
if it's a multiple of 3, print "Fizz", if it's a multiple of 5, print "Buzz",  
and if it's a multiple of both, print "FizzBuzz." It's extremely simple.

And yet, for some reason, it's often treated like a "minimum test for programmers." It comes up in interviews, and on social media you'll occasionally see people flexing with comments like, "If you can't even write FizzBuzz..."

But wait a minute.

Can we really definitively say, "Couldn't write FizzBuzz = can't program"?

---

### It's not about whether you can do it, but whether you're in a "state" to do it

It's true that FizzBuzz requires an understanding of syntax and basic logical thinking. So it makes sense that it's used to "check the basics."

But, hear me out.

If the environment is different, the results will be different.

For example,

- When you're nervous in front of an interviewer you've just met
- When you're suddenly handed a whiteboard and don't have an editor at hand
- When you suddenly draw a blank and think, "Wait, what's modulo again?"

...Doesn't that happen? We're human, after all. I think it does.

Therefore, rather than "whether you can write FizzBuzz," I think what's actually more important is "whether you can get yourself into a state where you can write FizzBuzz."

---

### The pitfall of the common advice to "just train and you'll be fine"

When this topic comes up, the advice "so practice every day!" tends to appear.

It's true that repeated practice will enable you to write it smoothly, and that in itself is a good thing. But if you stand on the premise that "you're disqualified if you can't write FizzBuzz," it can turn into pure fear.

In other words, it tends to create a structure where you feel, "I made a mistake = I'm useless."

For example, on days when you oversleep, don't you tend to think, "I'm lazy..."? But it might just be that your body was accidentally tired.

The same goes for FizzBuzz.

---

### That being said, FizzBuzz is still a good question

That being said, there's nothing wrong with FizzBuzz.

Rather, I think it's a very well-made question. The rules are simple, and it's easy to expand. For example, if you change it like this, it deepens your thinking even more.

```python
for i in range(1, 101):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    print(output or i)
```

This is an example showing that "you don't have to use if-elif-else to write it." It's a bit smart, isn't it?

In other words, FizzBuzz doesn't just show "whether you could do it," but also serves as an entry point to see "how you write it" and "how deeply you understand it."

---

### In conclusion

I don't think you need to attach excessive meaning to whether you can do FizzBuzz or not.

Even if you couldn't write it, it might simply mean "you were just a little off your game," and often you can do it if you think about it carefully later.

Let's not rush and proceed slowly.

Code is written by humans. Because we're human, there are times when we forget things or get nervous. I think it's enough if we can accept that and move forward little by little.

Well then, let's take it easy and write some code today too.
