with open(r'c:\work\kenji.blog\content\post\tree-graph-data-structures-search-dfs-bfs-dijkstra\index.md', 'r', encoding='utf-8') as f:
    text = f.read()

src1 = '''# 木構造とグラフ構造の探索について

## はじめに
本記事では、コンピュータサイエンスにおいて非常に重要な役割を果たすデータ構造である **木構造** （Tree）および **グラフ構造** （Graph）について、その基本概念から探索アルゴリズムまでを詳細に解説します。

データ構造とアルゴリズムの分野において、これらは避けて通れないテーマです。特に **深さ優先探索** （DFS）、 **幅優先探索** （BFS）、そして最短経路問題を解くための **ダイクストラ法** （Dijkstra's Algorithm）は、プログラミングコンテストや実務においても頻繁に登場します。'''

src4 = '''## 4. グラフ構造（Graph）の基本
グラフ構造は、ノード（頂点: Vertex）とエッジ（辺: Edge）の集合で構成されます。木構造もグラフの一種（閉路を持たない無向グラフ、または有向グラフ）ですが、一般的なグラフは閉路（Cycle）を持つことがあり、複数の親を持つことも可能です。

グラフには以下の種類があります。
- **無向グラフ** （Undirected Graph）: エッジに方向がないグラフ
- **有向グラフ** （Directed Graph）: エッジに方向があるグラフ
- **重み付きグラフ** （Weighted Graph）: エッジに重み（コスト）が設定されているグラフ

```mermaid
graph LR
  "A" -- "5" --> "B"
  "A" -- "2" --> "C"
  "B" -- "1" --> "D"
  "C" -- "8" --> "D"
  "C" -- "4" --> "E"
  "D" -- "3" --> "E"
```'''

src5 = r'''## 5. ダイクストラ法（Dijkstra's Algorithm）
ダイクストラ法は、重み付きグラフにおいて、ある始点から他のすべての頂点への最短経路を求めるアルゴリズムです。ただし、エッジの重みが非負（0以上）である必要があります。

優先度付きキュー（Priority Queue）を用いることで、効率的に探索を行うことができます。数式表現としては、 $ d(v) $ を始点から頂点 $ v $ までの最短距離とすると、エッジ $ (u, v) $ の重み $ w(u, v) $ に対して、 $ d(v) = \min(d(v), d(u) + w(u, v)) $ と更新します。数式としては $$ d(v) \le d(u) + w(u, v) $$ という性質を満たします。ここで、 $ \text{cost} $ が最小となる経路を選びます。

### ダイクストラ法のPython実装例

```python
import heapq

def dijkstra(graph, start):
    # 最短距離を無限大で初期化
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

# グラフの定義（隣接リスト形式）
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
```'''

print("Block 1 count:", text.count(src1))
print("Block 4 count:", text.count(src4))
print("Block 5 count:", text.count(src5))
print("Cost string count:", text.count(r'$ \text{cost} $'))
