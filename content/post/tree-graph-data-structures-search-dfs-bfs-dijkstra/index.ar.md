---
title: "استكشاف هياكل الشجرة والرسوم البيانية (DFS, BFS, خوارزمية ديكسترا)"
date: "2026-09-24T19:44:38+09:00"
description: "هياكل الشجرة والرسوم البيانية لتمثيل علاقات البيانات المعقدة. شرح شامل من بحث العمق أولاً (DFS)، بحث العرض أولاً (BFS) إلى مشكلة المسار الأقصر (خوارزمية ديكسترا)."
slug: "tree-graph-data-structures-search-dfs-bfs-dijkstra"
date: 2026-09-22T03:00:00+09:00
image: "eyecatch.jpg"
categories: ["computer-science"]
tags: ["algorithms", "graph", "tree", "dfs", "bfs", "dijkstra"]
---

# حول استكشاف هياكل الشجرة والرسوم البيانية

## مقدمة
في هذه المقالة، سنشرح بالتفصيل **هيكل الشجرة** (Tree) و **هيكل الرسم البياني** (Graph)، وهما هياكل بيانات تلعب دورًا مهمًا للغاية في علوم الكمبيوتر، بدءًا من المفاهيم الأساسية إلى خوارزميات الاستكشاف.

في مجال هياكل البيانات والخوارزميات، هذه موضوعات لا يمكن تجنبها. بشكل خاص، **بحث العمق أولاً** (DFS) و **بحث العرض أولاً** (BFS) و **خوارزمية ديكسترا** (Dijkstra's Algorithm) لحل مشكلة المسار الأقصر، تظهر بشكل متكرر في مسابقات البرمجة والممارسة العملية.


## 1. أساسيات هيكل الشجرة (Tree)
هيكل الشجرة هو هيكل بيانات مناسب لتمثيل البيانات ذات العلاقات الهرمية. يتم استخدامه في مواقف مختلفة، مثل أنظمة الملفات، المخططات التنظيمية، وشجرة DOM في HTML.

يتكون هيكل الشجرة من العناصر التالية:
- **العقدة** (Node): العنصر الذي يحمل البيانات.
- **الحافة** (Edge): الخط الذي يربط بين العقد.
- **العقدة الجذرية** (Root Node): العقدة الموجودة في أعلى الشجرة. إنها عقدة ليس لها أب.
- **العقدة الورقية** (Leaf Node): العقدة التي ليس لها أبناء.

```mermaid
graph TD
  "Root" --> "NodeA"
  "Root" --> "NodeB"
  "NodeA" --> "Leaf1"
  "NodeA" --> "Leaf2"
  "NodeB" --> "Leaf3"
```

كأساس للاستكشاف في هيكل الشجرة، يوجد بحث العمق أولاً (DFS) وبحث العرض أولاً (BFS).

## 2. بحث العمق أولاً (DFS: Depth-First Search)
بحث العمق أولاً هو خوارزمية تبدأ من عقدة معينة، وتتقدم بعمق قدر الإمكان، وعندما تصل إلى طريق مسدود، تعود إلى العقدة السابقة وتستمر في الاستكشاف. باستخدام الدوال العودية (Recursive functions)، يمكن تنفيذه ببساطة شديدة. يمكن استخدام هيكل بيانات يسمى المكدس ([Stack](https://kenji.blog/ar/p/c-language-pointers-memory-management-stack-heap/)) أحيانًا.

### مثال على تنفيذ DFS في هيكل الشجرة باستخدام Python

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

# بناء الشجرة
root = TreeNode("Root")
node_a = TreeNode("A")
node_b = TreeNode("B")
root.children.extend([node_a, node_b])
node_a.children.extend([TreeNode("C"), TreeNode("D")])

print("DFS Traversal:")
dfs_tree(root)
```

## 3. بحث العرض أولاً (BFS: Breadth-First Search)
بحث العرض أولاً هو خوارزمية تبدأ من العقدة الجذرية، وتستكشف جميع العقد التي في نفس العمق أولاً، ثم تنتقل إلى العقد في العمق التالي. يستخدم هيكل بيانات يسمى الطابور (Queue). غالبًا ما يتم استخدامه عند العثور على المسار الأقصر وغيرها.

### مثال على تنفيذ BFS في هيكل الشجرة باستخدام Python

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

## 4. أساسيات هيكل الرسم البياني (Graph)
يتكون هيكل الرسم البياني من مجموعة من العقد (Vertex) والحواف (Edge). هيكل الشجرة هو أيضًا نوع من الرسم البياني (رسم بياني غير موجه لا يحتوي على دورات، أو رسم بياني موجه)، ولكن الرسم البياني العام قد يحتوي على دورة (Cycle)، ويمكن أن يكون له آباء متعددون.

هناك الأنواع التالية من الرسوم البيانية:
- **رسم بياني غير موجه** (Undirected Graph): رسم بياني ليس لحوافه اتجاه.
- **رسم بياني موجه** (Directed Graph): رسم بياني لحوافه اتجاه.
- **رسم بياني مرجح** (Weighted Graph): رسم بياني تم تعيين وزن (تكلفة) لحوافه.

```mermaid
graph LR
  "A" -- "5" --> "B"
  "A" -- "2" --> "C"
  "B" -- "1" --> "D"
  "C" -- "8" --> "D"
  "C" -- "4" --> "E"
  "D" -- "3" --> "E"
```

## 5. خوارزمية ديكسترا (Dijkstra's Algorithm)
خوارزمية ديكسترا هي خوارزمية لإيجاد أقصر مسار من نقطة بداية إلى جميع القمم الأخرى في رسم بياني مرجح. ومع ذلك، يجب أن تكون أوزان الحواف غير سالبة (0 أو أكثر).

باستخدام طابور الأولوية (Priority Queue)، يمكنك إجراء البحث بكفاءة. كتعبير رياضي، إذا كان $ d(v) $ هو المسار الأقصر من نقطة البداية إلى القمة $ v $، فبالنسبة للوزن $ w(u, v) $ للحافة $ (u, v) $، نقوم بالتحديث كـ $ d(v) = \min(d(v), d(u) + w(u, v)) $. كصيغة، فإنه يلبي الخاصية $ d(v) \le d(u) + w(u, v) $. هنا، نختار المسار حيث تكون $ \text{التكلفة} $ في الحد الأدنى.

### مثال على تنفيذ خوارزمية ديكسترا باستخدام Python

```python
import heapq

def dijkstra(graph, start):
    # تهيئة المسافة الأقصر إلى ما لا نهاية
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

# تعريف الرسم البياني (تنسيق قائمة المجاورة)
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

لمزيد من الشرح التفصيلي للخوارزميات والملاحظات الإضافية، نضيف المزيد من الوصف أدناه. هذه في غاية الأهمية.
