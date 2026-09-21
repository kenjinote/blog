import re

file_path = r'c:\work\kenji.blog\content\post\tree-graph-data-structures-search-dfs-bfs-dijkstra\index.md'
out_path = r'c:\work\kenji.blog\content\post\tree-graph-data-structures-search-dfs-bfs-dijkstra\index.fr.md'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('	ext{cost}', '\\text{cost}')

replacements = {
    'title: "木構造とグラフ構造の探索（DFS, BFS, ダイクストラ法）"': 'title: "Exploration des structures de données en arbre et en graphe (DFS, BFS, Algorithme de Dijkstra)"',
    'description: "複雑なデータ関係を表現する木構造とグラフ構造。深さ優先探索(DFS)、幅優先探索(BFS)から最短経路問題(ダイクストラ法)まで徹底解説します。"': 'description: "Structures de données en arbre et en graphe pour représenter des relations complexes. Explication détaillée de la recherche en profondeur (DFS), de la recherche en largeur (BFS) et du problème du plus court chemin (algorithme de Dijkstra)."',
    '# 木構造とグラフ構造の探索について': '# À propos de l\'exploration des structures en arbre et en graphe',
    '## はじめに': '## Introduction',
    '本記事では、コンピュータサイエンスにおいて非常に重要な役割を果たすデータ構造である **木構造** （Tree）および **グラフ構造** （Graph）について、その基本概念から探索アルゴリズムまでを詳細に解説します。': 'Dans cet article, nous expliquerons en détail les concepts de base et les algorithmes d\'exploration pour les **structures en arbre** (Tree) et les **structures en graphe** (Graph), qui sont des structures de données jouant un rôle très important en informatique.',
    'データ構造とアルゴリズムの分野において、これらは避けて通れないテーマです。特に **深さ優先探索** （DFS）、 **幅優先探索** （BFS）、そして最短経路問題を解くための **ダイクストラ法** （Dijkstra\'s Algorithm）は、プログラミングコンテストや実務においても頻繁に登場します。': 'Dans le domaine des structures de données et des algorithmes, ce sont des thèmes incontournables. En particulier, la **recherche en profondeur** (DFS), la **recherche en largeur** (BFS) et l\' **algorithme de Dijkstra** (Dijkstra\'s Algorithm) pour résoudre le problème du plus court chemin apparaissent fréquemment dans les concours de programmation et dans la pratique.',
    '## 1. 木構造（Tree）の基本': '## 1. Bases de la structure en arbre (Tree)',
    '木構造は、階層的な関係を持つデータを表現するのに適したデータ構造です。ファイルシステムや組織図、HTMLのDOMツリーなど、様々な場面で利用されています。': 'La structure en arbre est une structure de données adaptée pour représenter des données ayant une relation hiérarchique. Elle est utilisée dans diverses situations telles que les systèmes de fichiers, les organigrammes et les arbres DOM HTML.',
    '木構造は、以下の要素から構成されます。': 'Une structure en arbre se compose des éléments suivants :',
    '- **ノード** （Node）: データを保持する要素': '- **Nœud** (Node) : Élément qui contient les données',
    '- **エッジ** （Edge）: ノード同士を結ぶ線': '- **Arête** (Edge) : Ligne reliant les nœuds',
    '- **根ノード** （Root Node）: 木の一番上にあるノード。親を持たないノードです。': '- **Nœud racine** (Root Node) : Le nœud tout en haut de l\'arbre. C\'est un nœud qui n\'a pas de parent.',
    '- **葉ノード** （Leaf Node）: 子を持たないノードです。': '- **Nœud feuille** (Leaf Node) : C\'est un nœud qui n\'a pas d\'enfant.',
    '木構造における探索の基本として、深さ優先探索（DFS）と幅優先探索（BFS）があります。': 'Comme base de l\'exploration dans une structure en arbre, il y a la recherche en profondeur (DFS) et la recherche en largeur (BFS).',
    '## 2. 深さ優先探索（DFS: Depth-First Search）': '## 2. Recherche en profondeur (DFS: Depth-First Search)',
    '深さ優先探索は、あるノードから出発し、可能な限り深く進み、行き止まりに達したら一つ前のノードに戻って探索を続けるアルゴリズムです。再帰関数を用いることで、非常にシンプルに実装することができます。スタック（Stack）と呼ばれるデータ構造を利用することもあります。': 'La recherche en profondeur est un algorithme qui part d\'un certain nœud, va aussi loin que possible et, lorsqu\'il atteint une impasse, retourne au nœud précédent pour continuer la recherche. En utilisant une fonction récursive, il peut être implémenté très simplement. Il utilise parfois aussi une structure de données appelée pile (Stack).',
    '### 木構造におけるDFSのPython実装例': '### Exemple d\'implémentation Python de DFS pour une structure en arbre',
    '## 3. 幅優先探索（BFS: Breadth-First Search）': '## 3. Recherche en largeur (BFS: Breadth-First Search)',
    '幅優先探索は、根ノードから出発し、同じ深さのノードをすべて探索してから、次の深さのノードへ進むアルゴリズムです。キュー（Queue）と呼ばれるデータ構造を利用します。最短経路を求める際などによく用いられます。': 'La recherche en largeur est un algorithme qui part du nœud racine, explore tous les nœuds de la même profondeur, puis passe aux nœuds de la profondeur suivante. Il utilise une structure de données appelée file d\'attente (Queue). Il est souvent utilisé pour trouver le plus court chemin.',
    '### 木構造におけるBFSのPython実装例': '### Exemple d\'implémentation Python de BFS pour une structure en arbre',
    '## 4. グラフ構造（Graph）の基本': '## 4. Bases de la structure de graphe (Graph)',
    'グラフ構造は、ノード（頂点: Vertex）とエッジ（辺: Edge）の集合で構成されます。木構造もグラフの一種（閉路を持たない無向グラフ、または有向グラフ）ですが、一般的なグラフは閉路（Cycle）を持つことがあり、複数の親を持つことも可能です。': 'La structure de graphe est composée d\'un ensemble de nœuds (Sommet : Vertex) et d\'arêtes (Bord : Edge). Une structure en arbre est également un type de graphe (un graphe non orienté sans cycles ou un graphe orienté), mais un graphe général peut avoir des cycles (Cycle) et peut également avoir plusieurs parents.',
    'グラフには以下の種類があります。': 'Il existe les types de graphes suivants :',
    '- **無向グラフ** （Undirected Graph）: エッジに方向がないグラフ': '- **Graphe non orienté** (Undirected Graph) : Graphe où les arêtes n\'ont pas de direction',
    '- **有向グラフ** （Directed Graph）: エッジに方向があるグラフ': '- **Graphe orienté** (Directed Graph) : Graphe où les arêtes ont une direction',
    '- **重み付きグラフ** （Weighted Graph）: エッジに重み（コスト）が設定されているグラフ': '- **Graphe pondéré** (Weighted Graph) : Graphe où les arêtes ont un poids (coût)',
    '## 5. ダイクストラ法（Dijkstra\'s Algorithm）': '## 5. Algorithme de Dijkstra (Dijkstra\'s Algorithm)',
    'ダイクストラ法は、重み付きグラフにおいて、ある始点から他のすべての頂点への最短経路を求めるアルゴリズムです。ただし、エッジの重みが非負（0以上）である必要があります。': 'L\'algorithme de Dijkstra est un algorithme permettant de trouver le plus court chemin d\'un point de départ à tous les autres sommets dans un graphe pondéré. Cependant, les poids des arêtes doivent être non négatifs (0 ou plus).',
    '優先度付きキュー（Priority Queue）を用いることで、効率的に探索を行うことができます。数式表現としては、 $ d(v) $ を始点から頂点 $ v $ までの最短距離とすると、エッジ $ (u, v) $ の重み $ w(u, v) $ に対して、 $ d(v) = \min(d(v), d(u) + w(u, v)) $ と更新します。数式としては $$ d(v) \le d(u) + w(u, v) $$ という性質を満たします。ここで、 $ \\text{cost} $ が最小となる経路を選びます。': 'En utilisant une file de priorité (Priority Queue), la recherche peut être effectuée efficacement. En termes de formule, si $ d(v) $ est la distance la plus courte du point de départ au sommet $ v $, alors pour le poids $ w(u, v) $ de l\'arête $ (u, v) $, nous mettons à jour $ d(v) = \min(d(v), d(u) + w(u, v)) $. Il satisfait la propriété $$ d(v) \le d(u) + w(u, v) $$ comme formule. Ici, nous choisissons le chemin pour lequel $ \\text{coût} $ est minimisé.',
    '### ダイクストラ法のPython実装例': '### Exemple d\'implémentation Python de l\'algorithme de Dijkstra',
    '# ツリーの構築': '# Construction de l\'arbre',
    '# 最短距離を無限大で初期化': '# Initialiser la distance la plus courte à l\'infini',
    '# グラフの定義（隣接リスト形式）': '# Définition du graphe (format de liste d\'adjacence)',
    '詳細なアルゴリズムの解説と補足事項について、以下にさらに記述を追加します。これらは非常に重要です。': 'Pour une explication détaillée de l\'algorithme et des remarques supplémentaires, des descriptions additionnelles seront ajoutées ci-dessous. Elles sont très importantes.',
    '\\text{cost}': '\\text{coût}'
}

for jp, fr in replacements.items():
    text = text.replace(jp, fr)

mermaid_replacements = {
    '"Root"': '"Racine"',
    '"NodeA"': '"NoeudA"',
    '"NodeB"': '"NoeudB"',
    '"Leaf1"': '"Feuille1"',
    '"Leaf2"': '"Feuille2"',
    '"Leaf3"': '"Feuille3"',
}
for jp, fr in mermaid_replacements.items():
    text = text.replace(jp, fr)

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Done')
