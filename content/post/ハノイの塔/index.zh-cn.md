---
title: '汉诺塔'
slug: "ハノイの塔"
date: 2025-04-17T22:23:14+09:00
tags: ["汉诺塔", "算法", "Python"]
draft: false
image: "img.png"
categories: ["编程"]
---

# 汉诺塔

你好！

今天，我想一边展示Python的示例程序，一边为大家讲解“汉诺塔”。

---

## 什么是汉诺塔？

汉诺塔是一个使用3根柱子和多个圆盘的益智游戏。圆盘大小不一，最初按照从大到小的顺序堆叠在一根柱子上。规则如下：

1. 每次只能移动1个圆盘。
2. 较小的圆盘上不能放置较大的圆盘。

这个益智游戏被认为是学习递归思维的最佳教材。递归是一种将某个问题分解为同类型的较小问题来解决的方法。在汉诺塔中，为了移动n个圆盘，我们会重复执行移动n-1个圆盘的操作。

---

## 让我们用Python来解汉诺塔

以下是用Python解汉诺塔的示例代码。


```python
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)

# 示例：将3个圆盘从A移动到C
hanoi(3, 'A', 'C', 'B')
```


在这段代码中，`hanoi` 函数被递归调用，并输出移动圆盘的步骤。例如，在有3个圆盘的情况下，会得到以下输出：


```
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
```

像这样，通过使用递归方法，复杂的问题也能简单地解决。

---

## 移动64个圆盘需要多长时间？

汉诺塔的移动次数至少需要 2^n - 1 次。也就是说，要移动64个圆盘，需要 2^64 - 1 次，大约 1.84×10^19 次移动。即使每秒移动一次，大约也需要5849亿年。这大约是宇宙年龄（约137亿年）的42倍。

像这样，随着圆盘数量的增加，所需的移动次数呈指数级增长。因此，在现实中移动64个圆盘是不切实际的。

---

## 总结

汉诺塔是学习递归思维的最佳益智游戏。使用Python，可以轻松实现其解法。然而，随着圆盘数量的增加，所需的移动次数会急剧增加，因此需要注意。

通过理解递归方法并实际编写代码，可以提高编程技能。请务必挑战一下汉诺塔。

--- 
