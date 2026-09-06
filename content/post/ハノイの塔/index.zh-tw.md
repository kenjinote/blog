---
title: "漢諾塔"
slug: "hanoi-tower"
date: 2025-04-17T22:23:14+09:00
tags: ["漢諾塔", "演算法", "Python"]
draft: false
image: "img.png"
categories: ["程式設計"]
---

# 漢諾塔

你好！

今天，我想透過一個 Python 範例程式來解釋「漢諾塔」。

---

## 什麼是漢諾塔？

漢諾塔是一個使用 3 根柱子和多個圓盤的謎題。圓盤的大小各不相同，最初它們按從大到小的順序堆疊在一根柱子上。規則如下：

1. 每次只能移動一個圓盤。
2. 較大的圓盤不能放在較小的圓盤上。

這個謎題被認為是學習遞迴思考的最佳教材。遞迴是一種透過將問題分解成相同類型的更小問題來解決問題的方法。在漢諾塔中，為了移動 n 個圓盤，我們重複移動 n-1 個圓盤的操作。

---

## 用 Python 解決漢諾塔

以下是用 Python 解決漢諾塔的範例程式碼。

```python
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)

# 範例：將 3 個圓盤從 A 移動到 C
hanoi(3, 'A', 'C', 'B')
```

在這個程式碼中，`hanoi` 函數被遞迴呼叫，並顯示移動圓盤的步驟。例如，在 3 個圓盤的情況下，可以獲得以下輸出：

```
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
```

透過這種方式，使用遞迴方法，可以簡單地解決複雜的問題。

---

## 移動 64 個圓盤需要多長時間？

漢諾塔的移動次數最少需要 2^n - 1 次。也就是說，要移動 64 個圓盤，需要 2^64 - 1 次，約 1.84×10^19 次移動。即使 1 秒移動 1 次，也需要大約 5849 億年。這大約是宇宙年齡（約 137 億年）的 42 倍。

因此，隨著圓盤數量的增加，所需的移動次數呈指數級增長。所以，在現實中移動 64 個圓盤是不切實際的。

---

## 總結

漢諾塔是學習遞迴思考的最佳謎題。使用 Python，您可以輕鬆實現其解決方案。然而，請注意，隨著圓盤數量的增加，所需的移動次數會急劇增加。

了解遞迴方法並嘗試實際編寫程式碼，可以幫助您提高程式設計技能。請務必挑戰一下漢諾塔。

--- 
