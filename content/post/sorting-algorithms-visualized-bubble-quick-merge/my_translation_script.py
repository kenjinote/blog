import sys, re

def translate_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    translations = {
        'title: "ソートアルゴリズム図解（バブルからクイック、マージソートまで）"': 'title: "Algorithmes de tri expliqués (du tri à bulles au tri rapide et tri fusion)"',
        'description: "プログラミングの基礎であるソートアルゴリズム。バブルソートからクイックソート、マージソートまで、図解とコードで網羅的に解説します。"': 'description: "Les algorithmes de tri sont la base de la programmation. Du tri à bulles au tri rapide et tri fusion, nous les expliquons en détail avec des schémas et du code."',
        '# 1. はじめに：ソートアルゴリズムの深淵なる世界': '# 1. Introduction : Le monde profond des algorithmes de tri',
        'コンピュータサイエンスにおいて、データを特定の順序（昇順または降順）に並べ替える「ソート（整列）」は、最も基本的かつ重要な操作の一つです。検索の高速化、データのグループ化、重複の検出など、あらゆるデータ処理の前段階としてソートアルゴリズムが活躍します。': "En informatique, le « tri », qui consiste à réorganiser des données dans un ordre spécifique (croissant ou décroissant), est l'une des opérations les plus fondamentales et importantes. Les algorithmes de tri sont utilisés comme étape préliminaire dans tout traitement de données, comme l'accélération des recherches, le regroupement de données et la détection de doublons.",
        '本記事では、初心者にもわかりやすいシンプルなアルゴリズムから、実務で活躍する高速なアルゴリズムまで、代表的なソートアルゴリズムを網羅的に解説します。各アルゴリズムの仕組みを **Mermaid** による図解で視覚的に理解し、Pythonコードで実際の実装を確認し、時間計算量などのパフォーマンスを比較していきます。さらに、アルゴリズムの動作を完全に把握するために、要素数50の配列を用いた完全な実行トレースも収録しています。これにより、アルゴリズムの細かな挙動を手にとるように理解できるでしょう。': "Dans cet article, nous expliquons en détail les algorithmes de tri représentatifs, allant des algorithmes simples faciles à comprendre pour les débutants aux algorithmes rapides utilisés dans la pratique. Nous comprendrons visuellement le fonctionnement de chaque algorithme avec des schémas **Mermaid**, vérifierons l'implémentation réelle avec du code Python et comparerons les performances telles que la complexité temporelle. De plus, afin de saisir pleinement le comportement de l'algorithme, nous incluons une trace d'exécution complète utilisant un tableau de 50 éléments. Cela vous permettra de comprendre le comportement détaillé de l'algorithme comme si vous l'aviez entre les mains.",
        '## アルゴリズムの評価指標': '## Critères d\'évaluation des algorithmes',
        '各アルゴリズムを評価する際には、以下の指標が重要になります。': 'Lors de l\'évaluation de chaque algorithme, les critères suivants sont importants.',
        '- **時間計算量 (Time Complexity)** : データの要素数 $n$ に対して、処理時間がどのように増加するかを表します。 $\\text{O}(n^2)$ や $\\text{O}(n \\log n)$ などのオーダー記法（Big-O notation）が使われます。数式内でテキストを扱う場合は $\\text{best}$ のように記述します。': '- **Complexité temporelle (Time Complexity)** : Indique comment le temps de traitement augmente par rapport au nombre d\'éléments $n$ des données. La notation Grand-O (Big-O notation) telle que $\\text{O}(n^2)$ ou $\\text{O}(n \\log n)$ est utilisée. Lors de la manipulation de texte dans des formules mathématiques, nous l\'écrivons comme $\\text{best}$.',
        '- **空間計算量 (Space Complexity)** : 実行時にどれだけの追加メモリを必要とするかを表します。インプレース（In-place）アルゴリズムは追加メモリをほとんど必要としません。': '- **Complexité spatiale (Space Complexity)** : Indique la quantité de mémoire supplémentaire requise lors de l\'exécution. Les algorithmes en place (In-place) nécessitent peu ou pas de mémoire supplémentaire.',
        '- **安定性 (Stability)** : 同じ値を持つ要素の相対的な順序が、ソート前後で保たれるかどうかを示します。安定なソートでは、元の順序が維持されます。': '- **Stabilité (Stability)** : Indique si l\'ordre relatif des éléments ayant la même valeur est conservé avant et après le tri. Dans un tri stable, l\'ordre d\'origine est maintenu.',
        '## 2. バブルソート (Bubble Sort)': '## 2. Tri à bulles (Bubble Sort)',
        '隣り合う要素を比較し、順序が逆であれば交換するという操作を繰り返すアルゴリズムです。泡が水面へ浮かんでいくように、大きな要素が徐々に配列の末尾へと移動していきます。': "Il s'agit d'un algorithme qui répète l'opération consistant à comparer des éléments adjacents et à les échanger si leur ordre est inversé. Tout comme les bulles remontent à la surface de l'eau, les éléments plus grands se déplacent progressivement vers la fin du tableau.",
        '### 計算量と特性': '### Complexité et caractéristiques',
        '- **時間計算量（最良）**: $\\text{O}(n)$': '- **Complexité temporelle (Meilleur cas)** : $\\text{O}(n)$',
        '- **時間計算量（平均）**: $\\text{O}(n^2)$': '- **Complexité temporelle (Cas moyen)** : $\\text{O}(n^2)$',
        '- **時間計算量（最悪）**: $\\text{O}(n^2)$': '- **Complexité temporelle (Pire cas)** : $\\text{O}(n^2)$',
        '- **空間計算量**: $\\text{O}(1)$': '- **Complexité spatiale** : $\\text{O}(1)$',
        '- **安定性**: 安定': '- **Stabilité** : Stable',
        '### 図解 (Mermaid)': '### Schéma (Mermaid)',
        'A["配列の先頭から開始"] --> B{"隣り合う要素を比較"}': 'A["Commencer au début du tableau"] --> B{"Comparer les éléments adjacents"}',
        'B -->|"左 > 右"| C["要素を交換"]': 'B -->|"Gauche > Droite"| C["Échanger les éléments"]',
        'B -->|"左 <= 右"| D["交換しない"]': 'B -->|"Gauche <= Droite"| D["Ne pas échanger"]',
        'C -->|"次へ"| E["次のペアへ"]': 'C -->|"Suivant"| E["Paire suivante"]',
        'D -->|"次へ"| E': 'D -->|"Suivant"| E',
        'E --> F{"末尾に到達したか"}': 'E --> F{"Atteint la fin ?"}',
        'F -->|"No"| B': 'F -->|"Non"| B',
        'F -->|"Yes"| G{"一度も交換しなかったか"}': 'F -->|"Oui"| G{"Aucun échange effectué ?"}',
        'G -->|"Yes"| H["ソート完了"]': 'G -->|"Oui"| H["Tri terminé"]',
        'G -->|"No"| A': 'G -->|"Non"| A',
        '### Python実装': '### Implémentation en Python',
        '### バブルソートの詳細トレース': '### Trace détaillée du tri à bulles',
        '要素数50のランダムな配列に対してバブルソートを実行した際の、各パス完了後の配列の状態を示します。バブルソートがどのように要素を右側に押し出していくかを観察してください。': "Voici l'état du tableau après l'achèvement de chaque passe lors de l'exécution du tri à bulles sur un tableau aléatoire de 50 éléments. Observez comment le tri à bulles pousse les éléments vers la droite.",
        'このパスでは、未ソート部分の中で最大の要素が、まるで泡のように右端へと浮かび上がりました。バブルソートの特性上、1回のパスにつき少なくとも1つの要素が最終的な正しい位置に収まることが保証されます。そのため、パスを重ねるごとに探索範囲を1つずつ狭めていくことができ、無駄な比較操作を減らすことが可能です。しかしながら、データが完全に逆順に並んでいる最悪のケースでは、すべての要素ペアに対して交換操作が発生するため、計算量は $\\text{O}(n^2)$ に達し、パフォーマンスは極めて低くなります。': "Dans cette passe, le plus grand élément de la partie non triée a flotté jusqu'à l'extrémité droite comme une bulle. En raison de la nature du tri à bulles, il est garanti qu'au moins un élément se retrouvera dans sa position correcte finale à chaque passe. Par conséquent, il est possible de réduire la zone de recherche d'une unité à chaque passe, ce qui réduit les opérations de comparaison inutiles. Cependant, dans le pire des cas où les données sont disposées dans un ordre complètement inverse, des opérations d'échange se produisent pour toutes les paires d'éléments, de sorte que la complexité atteint $\\text{O}(n^2)$ et les performances sont extrêmement faibles.",
        'パス 44 で交換が発生しなかったため、ソート完了と判断して終了します。': "Aucun échange ne s'étant produit lors de la passe 44, on considère que le tri est terminé et on s'arrête.",
        '## 3. 挿入ソート (Insertion Sort)': '## 3. Tri par insertion (Insertion Sort)',
        '手元のトランプを並べ替えるときのように、未ソート部分から要素を一つずつ取り出し、ソート済み部分の適切な位置に挿入していくアルゴリズムです。': "Comme on trie des cartes en main, c'est un algorithme qui extrait les éléments un par un de la partie non triée et les insère à la position appropriée dans la partie déjà triée.",
        'A["未ソート部分から1つ要素を取り出す"] --> B{"ソート済み部分の末尾から比較"}': 'A["Extraire 1 élément de la partie non triée"] --> B{"Comparer à partir de la fin de la partie triée"}',
        'B -->|"取り出した要素より大きい"| C["要素を右にずらす"]': 'B -->|"Plus grand que l\'élément extrait"| C["Décaler l\'élément vers la droite"]',
        'B -->|"取り出した要素以下"| D["その位置に挿入"]': 'B -->|"Inférieur ou égal à l\'élément extrait"| D["Insérer à cette position"]',
        'C -->|"前へ"| B': 'C -->|"Précédent"| B',
        'D --> E{"すべての要素を処理したか"}': 'D --> E{"Tous les éléments traités ?"}',
        'E -->|"Yes"| F["ソート完了"]': 'E -->|"Oui"| F["Tri terminé"]',
        'E -->|"No"| A': 'E -->|"Non"| A',
        '### 挿入ソートの詳細トレース': '### Trace détaillée du tri par insertion',
        '要素数50のランダムな配列に対して挿入ソートを実行した際の、各要素挿入後の配列の状態を示します。左側のソート済み部分が徐々に拡大していく様子を確認できます。': "Voici l'état du tableau après l'insertion de chaque élément lors de l'exécution du tri par insertion sur un tableau aléatoire de 50 éléments. Vous pouvez voir comment la partie triée à gauche s'étend progressivement.",
        '挿入ソートは、すでにソートされている配列に対しては $\\text{O}(n)$ の時間で完了するという優れた特性を持っています。データ量が少ない場合や、大部分がソート済みのデータに対しては、定数倍のオーバーヘッドが小さいため、クイックソートやマージソートよりも高速に動作することがよくあります。この特性を活かし、多くの標準ライブラリ（PythonのTimSortなど）では、再帰の末端などのデータサイズが小さい場面で挿入ソートに切り替えるハイブリッドアプローチが採用されています。': "Le tri par insertion a l'excellente propriété de se terminer en un temps de $\\text{O}(n)$ pour les tableaux déjà triés. Pour de petites quantités de données ou pour des données en grande partie triées, il fonctionne souvent plus rapidement que le tri rapide ou le tri fusion car le surcoût (overhead) constant est faible. Tirant parti de cette caractéristique, de nombreuses bibliothèques standard (telles que le TimSort de Python) utilisent une approche hybride qui bascule sur le tri par insertion lorsque la taille des données est petite, par exemple aux extrémités de la récursivité.",
        '## 4. クイックソート (Quick Sort)': '## 4. Tri rapide (Quick Sort)',
        '分割統治法を用いた非常に高速なアルゴリズムです。配列の中から基準値（ピボット）を選び、ピボットより小さい要素と大きい要素に分割します。この操作を再帰的に繰り返すことで全体をソートします。': "Il s'agit d'un algorithme extrêmement rapide utilisant la méthode diviser pour régner (divide and conquer). Il sélectionne une valeur de référence (pivot) dans le tableau et divise le tableau en éléments plus petits et plus grands que le pivot. En répétant cette opération récursivement, l'ensemble est trié.",
        '- **時間計算量（最良）**: $\\text{O}(n \\log n)$': '- **Complexité temporelle (Meilleur cas)** : $\\text{O}(n \\log n)$',
        '- **時間計算量（平均）**: $\\text{O}(n \\log n)$': '- **Complexité temporelle (Cas moyen)** : $\\text{O}(n \\log n)$',
        '- **空間計算量**: $\\text{O}(\\log n)$': '- **Complexité spatiale** : $\\text{O}(\\log n)$',
        '- **安定性**: 不安定': '- **Stabilité** : Instable',
        'A["配列からピボットを選択"] --> B["配列を分割"]': 'A["Sélectionner le pivot dans le tableau"] --> B["Diviser le tableau"]',
        'B -->|"分割1"| C["ピボットより小さいグループ"]': 'B -->|"Division 1"| C["Groupe inférieur au pivot"]',
        'B -->|"分割2"| D["ピボットより大きいグループ"]': 'B -->|"Division 2"| D["Groupe supérieur au pivot"]',
        'C --> E{"要素数が1以下か"}': 'C --> E{"Nombre d\'éléments <= 1 ?"}',
        'D --> F{"要素数が1以下か"}': 'D --> F{"Nombre d\'éléments <= 1 ?"}',
        'E -->|"Yes"| G["ソート完了"]': 'E -->|"Oui"| G["Tri terminé"]',
        'E -->|"No"| A': 'E -->|"Non"| A',
        'F -->|"Yes"| G': 'F -->|"Oui"| G',
        'F -->|"No"| A': 'F -->|"Non"| A',
        'クイックソートは、実務において最も頻繁に利用されるアルゴリズムの一つです。最悪計算量は $\\text{O}(n^2)$ ですが、適切なピボット選択戦略（例えばMedian-of-Three）を用いることで、実質的には常に $\\text{O}(n \\log n)$ で動作します。Pythonの組み込みソート関数 `list.sort()` は、クイックソートではなく、マージソートと挿入ソートを組み合わせた **TimSort (ティムソート)** と呼ばれるアルゴリズムを採用しています。': "Le tri rapide est l'un des algorithmes les plus fréquemment utilisés en pratique. La complexité dans le pire des cas est de $\\text{O}(n^2)$, mais en utilisant une stratégie de sélection de pivot appropriée (par exemple Médiane-de-Trois), il fonctionne pratiquement toujours en $\\text{O}(n \\log n)$. La fonction de tri intégrée de Python, `list.sort()`, n'utilise pas le tri rapide, mais un algorithme appelé **TimSort** qui combine le tri fusion et le tri par insertion.",
        '### ピボット選択の重要性について': '### L\'importance du choix du pivot',
        'クイックソートのパフォーマンスは、ピボットの選び方に大きく依存します。理想的には、常に配列の中央値（メジアン）をピボットとして選択できれば、配列は毎回正確に半分に分割され、再帰の深さは $\\text{O}(\\log n)$ となり、完璧な $\\text{O}(n \\log n)$ の計算量が保証されます。しかし、真の中央値を厳密に見つけ出すには追加の計算コストがかかるため、実用上は定数時間で選択できる近似手法が採用されます。': "Les performances du tri rapide dépendent fortement de la manière dont le pivot est choisi. Idéalement, si la médiane du tableau peut toujours être choisie comme pivot, le tableau sera divisé exactement en deux à chaque fois, la profondeur de récursion sera de $\\text{O}(\\log n)$, et une complexité parfaite de $\\text{O}(n \\log n)$ est garantie. Cependant, trouver la vraie médiane nécessite des coûts de calcul supplémentaires, de sorte qu'en pratique, des méthodes approximatives qui peuvent être sélectionnées en temps constant sont adoptées.",
        'もし配列がすでにソートされている状態で、常に先頭の要素をピボットとして選択した場合、分割された配列の片方は要素数が0、もう片方は $n-1$ となり、再帰の深さが $n$ に達してしまいます。これにより、時間計算量は最悪の $\\text{O}(n^2)$ となり、場合によってはスタックオーバーフローを引き起こす危険性もあります。': "Si le tableau est déjà trié et que le premier élément est toujours sélectionné comme pivot, l'un des tableaux divisés aura 0 élément et l'autre $n-1$ éléments, et la profondeur de récursion atteindra $n$. Par conséquent, la complexité temporelle sera au pire de $\\text{O}(n^2)$ et, dans certains cas, il y a un risque de provoquer un débordement de pile (stack overflow).",
        'このような事態を防ぐため、ランダムにピボットを選択するランダム化クイックソートや、配列の先頭・中央・末尾の3つの要素の中央値をピボットとして採用する手法が一般的に用いられます。これにより、どのような入力データに対しても安定して高速なソート処理を実現できるようになります。': "Afin d'éviter cette situation, le tri rapide randomisé (qui sélectionne le pivot de manière aléatoire) ou la méthode de la médiane de trois (qui adopte la médiane de trois éléments : le premier, le milieu et le dernier du tableau) sont couramment utilisés. Cela permet de réaliser un tri stable et rapide pour n'importe quelle donnée d'entrée.",
        '## 5. マージソート (Merge Sort)': '## 5. Tri fusion (Merge Sort)',
        'ジョン・フォン・ノイマンによって考案された、安定な外部ソートの代表格です。分割統治法に基づき、配列を細かく分割してから、それらをソートされた順序を保ちながら結合（マージ）していきます。': "Inventé par John von Neumann, c'est le représentant typique du tri externe stable. Basé sur la méthode diviser pour régner, il divise finement le tableau, puis les combine (fusionne) tout en maintenant l'ordre trié.",
        '- **時間計算量（最悪）**: $\\text{O}(n \\log n)$': '- **Complexité temporelle (Pire cas)** : $\\text{O}(n \\log n)$',
        '- **空間計算量**: $\\text{O}(n)$': '- **Complexité spatiale** : $\\text{O}(n)$',
        'A["配列を中央で2つに分割"] --> B{"要素数が1以下か"}': 'A["Diviser le tableau en deux au milieu"] --> B{"Nombre d\'éléments <= 1 ?"}',
        'B -->|"Yes"| C["分割完了"]': 'B -->|"Oui"| C["Division terminée"]',
        'B -->|"No"| A': 'B -->|"Non"| A',
        'C --> D["隣り合う部分配列をマージ"]': 'C --> D["Fusionner les sous-tableaux adjacents"]',
        'D --> E{"1つの配列になったか"}': 'D --> E{"Est devenu un seul tableau ?"}',
        'E -->|"No"| D': 'E -->|"Non"| D',
        '### 安定なソートの重要性': '### L\'importance d\'un tri stable',
        'マージソートの最大の特徴は、その **安定性** にあります。安定なソートとは、同じ値を持つ要素の相対的な順序がソート前後で変わらないことを意味します。この性質は、複数の異なる基準でデータを連続してソートする場合に極めて重要になります。': "La principale caractéristique du tri fusion réside dans sa **stabilité**. Un tri stable signifie que l'ordre relatif des éléments ayant la même valeur ne change pas avant et après le tri. Cette propriété est extrêmement importante lorsque l'on trie successivement des données selon plusieurs critères différents.",
        'たとえば、生徒のデータを「テストの点数」でソートした後、「クラス名」でソートし直す場合を考えます。安定なソートアルゴリズムを使用すれば、同じクラスの生徒同士は「テストの点数」の順序が保たれたままになります。マージソートは、結合処理（マージ）において等しい要素の順序を厳密に管理するため、この安定性を完全に保証します。': "Par exemple, considérez le cas où les données des élèves sont triées par « note au test », puis triées à nouveau par « nom de la classe ». Si un algorithme de tri stable est utilisé, l'ordre des « notes au test » est conservé parmi les élèves de la même classe. Le tri fusion gère de manière stricte l'ordre des éléments égaux lors du processus de combinaison (fusion), ce qui garantit totalement cette stabilité.",
        'また、マージソートはデータへのアクセスが逐次的であるため、配列をメモリ上にすべて展開できないような巨大なデータセット（外部メモリ）をソートする際にも極めて有効です。ディスクI/Oの回数を最小限に抑えつつ、効率的にソート処理を進めることができます。これにより、データベースシステムや巨大ファイルの整列処理において、マージソートは今なお最前線で活用され続けています。': "De plus, comme le tri fusion accède aux données de manière séquentielle, il est extrêmement efficace pour trier de très grands ensembles de données (mémoire externe) qui ne peuvent pas être entièrement déployés en mémoire. Il permet de procéder efficacement au traitement du tri tout en minimisant le nombre d'E/S disque. Par conséquent, le tri fusion continue d'être utilisé en première ligne dans les systèmes de bases de données et le traitement du tri de fichiers volumineux.",
        '## 6. まとめ：どのアルゴリズムを選ぶべきか': '## 6. Conclusion : Quel algorithme choisir ?',
        'さまざまなソートアルゴリズムを紹介してきましたが、実務において「唯一の正解」となるアルゴリズムは存在しません。データの性質や制約条件に応じて、適切なアルゴリズムを選択することが求められます。': "Bien que nous ayons présenté divers algorithmes de tri, il n'existe pas d'algorithme qui soit la « seule bonne réponse » en pratique. Il est nécessaire de choisir l'algorithme approprié en fonction de la nature des données et des contraintes.",
        '- データ量が非常に少ない場合や、ほぼソート済みのデータには **挿入ソート** が効果的です。': '- Pour de très petites quantités de données ou des données presque triées, le **tri par insertion** est efficace.',
        '- 一般的な用途で最高速を求める場合は **クイックソート** が最適です。': '- Pour une utilisation générale nécessitant la vitesse maximale, le **tri rapide** est optimal.',
        '- 安定性が必要な場合や、最悪計算量を保証したい場合は **マージソート** が選ばれます。': '- Lorsque la stabilité est requise ou pour garantir la complexité du pire des cas, le **tri fusion** est choisi.',
        '- メモリ制約が厳しく、インプレースで安定した性能を出したい場合は **ヒープソート** が適しています。': '- Lorsque les contraintes de mémoire sont strictes et qu\'une performance stable en place est souhaitée, le **tri par tas (Heap Sort)** est approprié.',
        '近代的なプログラミング言語（Python, Java, Rustなど）の標準ライブラリでは、これらのアルゴリズムの長所を組み合わせたハイブリッド手法（TimSortやIntroSortなど）が採用されており、開発者が自分でソートアルゴリズムをゼロから実装する機会は減っています。しかし、その内部でどのようなトレードオフが考慮されているかを理解することは、よりパフォーマンスの高い堅牢なソフトウェアを設計するための重要な基盤となります。': "Dans les bibliothèques standard des langages de programmation modernes (Python, Java, Rust, etc.), des méthodes hybrides combinant les avantages de ces algorithmes (TimSort, IntroSort, etc.) sont adoptées, et les opportunités pour les développeurs d'implémenter eux-mêmes des algorithmes de tri de zéro ont diminué. Cependant, comprendre quels compromis sont pris en compte en interne est une base importante pour concevoir des logiciels plus performants et plus robustes.",
        'この記事が、あなたのアルゴリズム学習と実務開発の助けになることを願っています。': "Nous espérons que cet article vous aidera dans votre apprentissage des algorithmes et dans votre développement pratique."
    }

    out_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped in translations:
            # maintain leading whitespace
            prefix = line[:len(line) - len(line.lstrip())]
            out_lines.append(prefix + translations[stripped] + "\n")
            continue
        
        # Regex for traces
        if "**初期状態**:" in line:
            line = line.replace("**初期状態**:", "**État initial** :")
        
        line = re.sub(r'\*\*パス (\d+) 完了後\*\*', r"**Après l'étape \1**", line)
        line = re.sub(r'\*\*ステップ (\d+) \(要素 (\d+) を挿入後\)\*\*', r"**Étape \1 (après insertion de l'élément \2)**", line)

        out_lines.append(line)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(out_lines)

if __name__ == "__main__":
    translate_file('index.md', 'index.fr.md')
