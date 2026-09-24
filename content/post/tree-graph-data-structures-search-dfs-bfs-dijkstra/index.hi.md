---
title: "ट्री और ग्राफ डेटा संरचनाओं की खोज (DFS, BFS, डिजक्स्ट्रा एल्गोरिदम)"
date: "2026-09-24T19:44:38+09:00"
description: "ट्री और ग्राफ संरचनाएं जो जटिल डेटा संबंधों का प्रतिनिधित्व करती हैं। गहराई-प्रथम खोज (DFS), चौड़ाई-प्रथम खोज (BFS) से लेकर सबसे छोटे पथ की समस्या (डिजक्स्ट्रा एल्गोरिदम) तक विस्तृत विवरण।"
slug: "tree-graph-data-structures-search-dfs-bfs-dijkstra"
date: 2026-09-22T03:00:00+09:00
image: "eyecatch.jpg"
categories: ["computer-science"]
tags: ["algorithms", "graph", "tree", "dfs", "bfs", "dijkstra"]
---

# ट्री और ग्राफ डेटा संरचनाओं की खोज के बारे में

## परिचय
इस लेख में, हम **ट्री संरचना** (Tree) और **ग्राफ संरचना** (Graph) के बारे में विस्तार से चर्चा करेंगे, जो कंप्यूटर विज्ञान में एक अत्यंत महत्वपूर्ण भूमिका निभाने वाली डेटा संरचनाएं हैं, इनकी मूल अवधारणाओं से लेकर खोज एल्गोरिदम तक।

डेटा संरचनाओं और एल्गोरिदम के क्षेत्र में, ये ऐसे विषय हैं जिन्हें नजरअंदाज नहीं किया जा सकता है। विशेष रूप से **गहराई-प्रथम खोज** (DFS), **चौड़ाई-प्रथम खोज** (BFS), और सबसे छोटे पथ की समस्या को हल करने के लिए **डिजक्स्ट्रा एल्गोरिदम** (Dijkstra's Algorithm) अक्सर प्रोग्रामिंग प्रतियोगिताओं और व्यावहारिक कार्यों में दिखाई देते हैं।

## 1. ट्री संरचना (Tree) की मूल बातें
ट्री संरचना एक डेटा संरचना है जो पदानुक्रमित संबंधों वाले डेटा का प्रतिनिधित्व करने के लिए उपयुक्त है। इसका उपयोग विभिन्न स्थितियों में किया जाता है, जैसे कि फ़ाइल सिस्टम, संगठन चार्ट और HTML के DOM ट्री में।

ट्री संरचना निम्नलिखित तत्वों से बनी होती है:
- **नोड** (Node): वह तत्व जो डेटा रखता है
- **एज** (Edge): नोड्स को जोड़ने वाली रेखा
- **रूट नोड** (Root Node): ट्री के शीर्ष पर स्थित नोड। यह ऐसा नोड है जिसका कोई पैरेंट नहीं होता है।
- **लीफ नोड** (Leaf Node): वह नोड जिसका कोई चाइल्ड नहीं होता है।

```mermaid
graph TD
  "Root" --> "NodeA"
  "Root" --> "NodeB"
  "NodeA" --> "Leaf1"
  "NodeA" --> "Leaf2"
  "NodeB" --> "Leaf3"
```

ट्री संरचना में खोज के मूल आधार के रूप में, गहराई-प्रथम खोज (DFS) और चौड़ाई-प्रथम खोज (BFS) हैं।

## 2. गहराई-प्रथम खोज (DFS: Depth-First Search)
गहराई-प्रथम खोज एक एल्गोरिदम है जो किसी नोड से शुरू होता है, जहाँ तक संभव हो गहराई तक जाता है, और जब यह एक डेड-एंड पर पहुँच जाता है, तो यह पिछले नोड पर वापस आ जाता है और खोजना जारी रखता है। रिकर्सिव फ़ंक्शन का उपयोग करके, इसे बहुत ही सरलता से लागू किया जा सकता है। यह स्टैक ([Stack](https://kenji.blog/hi/p/c-language-pointers-memory-management-stack-heap/)) नामक डेटा संरचना का भी उपयोग कर सकता है।

### ट्री संरचना में DFS का Python कार्यान्वयन उदाहरण

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def dfs_tree(node):
    if node is None:
        return
    print(f"Visiting {node.value}")
    for child in node.children:
        dfs_tree(child)

# ट्री का निर्माण
root = TreeNode("Root")
node_a = TreeNode("A")
node_b = TreeNode("B")
root.children.extend([node_a, node_b])
node_a.children.extend([TreeNode("C"), TreeNode("D")])

print("DFS Traversal:")
dfs_tree(root)
```

## 3. चौड़ाई-प्रथम खोज (BFS: Breadth-First Search)
चौड़ाई-प्रथम खोज एक एल्गोरिदम है जो रूट नोड से शुरू होता है, समान गहराई वाले सभी नोड्स की खोज करता है, और फिर अगली गहराई केেম गहराई के नोड्स पर आगे बढ़ता है। यह क्यू (Queue) नामक डेटा संरचना का उपयोग करता है। इसका उपयोग अक्सर सबसे छोटे पथ को खोजने के लिए किया जाता है।

### ट्री संरचना में BFS का Python कार्यान्वयन उदाहरण

```python
from collections import deque

def bfs_tree(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        current = queue.popleft()
        print(f"Visiting {current.value}")
        for child in current.children:
            queue.append(child)

print("BFS Traversal:")
bfs_tree(root)
```

## 4. ग्राफ संरचना (Graph) की मूल बातें
ग्राफ संरचना नोड्स (शीर्ष: Vertex) और एजेज (किनारे: Edge) के एक सेट से बनी होती है। ट्री संरचना भी एक प्रकार का ग्राफ है (बिना चक्र वाला एक अप्रत्यक्ष ग्राफ, या एक निर्देशित ग्राफ), लेकिन एक सामान्य ग्राफ में चक्र (Cycle) हो सकते हैं और कई पैरेंट्स का होना भी संभव है।

ग्राफ के निम्नलिखित प्रकार होते हैं:
- **अप्रत्यक्ष ग्राफ** (Undirected Graph): ऐसा ग्राफ जिसमें एजेज की कोई दिशा नहीं होती है
- **निर्देशित ग्राफ** (Directed Graph): ऐसा ग्राफ जिसमें एजेज की दिशा होती है
- **वेटेड ग्राफ** (Weighted Graph): ऐसा ग्राफ जिसमें एजेज का वजन (लागत) निर्धारित होता है

```mermaid
graph LR
  "A" -- "5" --> "B"
  "A" -- "2" --> "C"
  "B" -- "1" --> "D"
  "C" -- "8" --> "D"
  "C" -- "4" --> "E"
  "D" -- "3" --> "E"
```

## 5. डिजक्स्ट्रा एल्गोरिदम (Dijkstra's Algorithm)
डिजक्स्ट्रा एल्गोरिदम एक वेटेड ग्राफ में, किसी दिए गए प्रारंभिक बिंदु से अन्य सभी शीर्षों तक के सबसे छोटे पथ को खोजने के लिए एक एल्गोरिदम है। हालाँकि, एजेज का वजन गैर-नकारात्मक (0 या अधिक) होना चाहिए।

प्राथमिकता कतार (Priority Queue) का उपयोग करके, आप कुशलता से खोज कर सकते हैं। गणितीय अभिव्यक्ति के रूप में, यदि $ d(v) $ प्रारंभिक बिंदु से शीर्ष $ v $ तक की सबसे छोटी दूरी है, तो एज $ (u, v) $ के वजन $ w(u, v) $ के लिए, हम इसे $ d(v) = \min(d(v), d(u) + w(u, v)) $ के रूप में अपडेट करते हैं। गणितीय सूत्र के रूप में, यह गुण $ d(v) \le d(u) + w(u, v) $ को संतुष्ट करता है। यहाँ, वह पथ चुना जाता है जहाँ $ \text{लागत} $ न्यूनतम हो।

### डिजक्स्ट्रा एल्गोरिदम का Python कार्यान्वयन उदाहरण

```python
import heapq

def dijkstra(graph, start):
    # सबसे छोटी दूरी को अनंत पर इनिशियलाइज़ करें
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# ग्राफ की परिभाषा (एडजेसेंसी सूची प्रारूप)
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'D': 1},
    'C': {'D': 8, 'E': 4},
    'D': {'E': 3},
    'E': {}
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(f"Shortest paths from {start_node}: {shortest_paths}")
```
