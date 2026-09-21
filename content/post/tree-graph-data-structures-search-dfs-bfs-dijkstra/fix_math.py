import re

with open("index.en.md", "r", encoding="utf-8") as f:
    content = f.read()

target = r'優先度付きキュー（Priority Queue）を用いることで、効率的に探索を行うことができます。数式表現としては、 $ d(v) $ を始点から頂点 $ v $ までの最短距離とすると、エッジ $ (u, v) $ の重み $ w(u, v) $ に対して、 $ d(v) = \min(d(v), d(u) + w(u, v)) $ と更新します。数式としては $$ d(v) \le d(u) + w(u, v) $$ という性質を満たします。ここで、 $ \text{cost} $ が最小となる経路を選びます。'

# The file might have actual tab characters instead of \t
target_with_tab = target.replace(r'\text', '\text')

replacement = r'By using a Priority Queue, searches can be performed efficiently. As a mathematical expression, letting $ d(v) $ be the shortest distance from the starting point to vertex $ v $, for an edge $ (u, v) $ with weight $ w(u, v) $, we update it as $ d(v) = \min(d(v), d(u) + w(u, v)) $. Mathematically, it satisfies the property $$ d(v) \le d(u) + w(u, v) $$. Here, we choose the path where $ \text{cost} $ is minimized.'

content = content.replace(target, replacement)
content = content.replace(target_with_tab, replacement)

# Let's also do a partial match just in case
part1 = r'優先度付きキュー（Priority Queue）を用いることで'
part2 = r'が最小となる経路を選びます。'

lines = content.split('\n')
for i, line in enumerate(lines):
    if part1 in line and part2 in line:
        lines[i] = replacement

with open("index.en.md", "w", encoding="utf-8") as f:
    f.write('\n'.join(lines))
