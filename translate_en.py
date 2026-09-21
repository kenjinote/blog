import re

with open('c:/work/kenji.blog/content/post/sorting-algorithms-visualized-bubble-quick-merge/index.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Front matter
text = text.replace('title: "ソートアルゴリズム図解（バブルからクイック、マージソートまで）"', 'title: "Sorting Algorithms Visualized (Bubble, Quick, Merge Sort)"')
text = text.replace('description: "プログラミングの基礎であるソートアルゴリズム。バブルソートからクイックソート、マージソートまで、図解とコードで網羅的に解説します。"', 'description: "Sorting algorithms are the foundation of programming. From bubble sort to quick sort and merge sort, we comprehensively explain them with visualizations and code."')

# Headings
text = text.replace('# 1. はじめに：ソートアルゴリズムの深淵なる世界', '# 1. Introduction: The Deep World of Sorting Algorithms')
text = text.replace('## 2. バブルソート (Bubble Sort)', '## 2. Bubble Sort')
text = text.replace('## 3. 挿入ソート (Insertion Sort)', '## 3. Insertion Sort')
text = text.replace('## 4. クイックソート (Quick Sort)', '## 4. Quick Sort')
text = text.replace('## 5. マージソート (Merge Sort)', '## 5. Merge Sort')
text = text.replace('## 6. まとめ：どのアルゴリズムを選ぶべきか', '## 6. Conclusion: Which Algorithm Should You Choose?')
text = text.replace('## アルゴリズムの評価指標', '## Algorithm Evaluation Metrics')
text = text.replace('### Python実装', '### Python Implementation')
text = text.replace('### バブルソートの詳細トレース', '### Detailed Trace of Bubble Sort')
text = text.replace('### ピボット選択の重要性について', '### Importance of Pivot Selection')
text = text.replace('### 図解 (Mermaid)', '### Visualization (Mermaid)')
text = text.replace('### 安定なソートの重要性', '### Importance of Stable Sorting')
text = text.replace('### 挿入ソートの詳細トレース', '### Detailed Trace of Insertion Sort')
text = text.replace('### 計算量と特性', '### Time Complexity and Characteristics')

# Text paragraphs
text = text.replace('コンピュータサイエンスにおいて、データを特定の順序（昇順または降順）に並べ替える「ソート（整列）」は、最も基本的かつ重要な操作の一つです。検索の高速化、データのグループ化、重複の検出など、あらゆるデータ処理の前段階としてソートアルゴリズムが活躍します。', 'In computer science, sorting data into a specific order (ascending or descending) is one of the most fundamental and important operations. Sorting algorithms play a vital role as a preliminary step in all kinds of data processing, such as speeding up searches, grouping data, and detecting duplicates.')

text = text.replace('本記事では、初心者にもわかりやすいシンプルなアルゴリズムから、実務で活躍する高速なアルゴリズムまで、代表的なソートアルゴリズムを網羅的に解説します。各アルゴリズムの仕組みを **Mermaid** による図解で視覚的に理解し、Pythonコードで実際の実装を確認し、時間計算量などのパフォーマンスを比較していきます。さらに、アルゴリズムの動作を完全に把握するために、要素数50の配列を用いた完全な実行トレースも収録しています。これにより、アルゴリズムの細かな挙動を手にとるように理解できるでしょう。', 'In this article, we comprehensively explain representative sorting algorithms, ranging from simple algorithms easy for beginners to understand, to high-speed algorithms active in practical use. You will visually understand how each algorithm works with **Mermaid** diagrams, check actual implementations in Python code, and compare performance such as time complexity. Furthermore, to fully grasp the behavior of the algorithms, a complete execution trace using an array of 50 elements is included. This will allow you to understand the detailed behavior of the algorithms as if holding them in your hands.')

text = text.replace('各アルゴリズムを評価する際には、以下の指標が重要になります。', 'When evaluating each algorithm, the following metrics are important.')

text = text.replace('- **時間計算量 (Time Complexity)** : データの要素数 $n$ に対して、処理時間がどのように増加するかを表します。 $\\text{O}(n^2)$ や $\\text{O}(n \\log n)$ などのオーダー記法（Big-O notation）が使われます。数式内でテキストを扱う場合は $\\text{best}$ のように記述します。', '- **Time Complexity**: Indicates how processing time increases with respect to the number of data elements $n$. Big-O notation, such as $\\text{O}(n^2)$ or $\\text{O}(n \\log n)$, is used. When handling text within formulas, it is written like $\\text{best}$.')

text = text.replace('- **空間計算量 (Space Complexity)** : 実行時にどれだけの追加メモリを必要とするかを表します。インプレース（In-place）アルゴリズムは追加メモリをほとんど必要としません。', '- **Space Complexity**: Indicates how much additional memory is required during execution. In-place algorithms require almost no additional memory.')

text = text.replace('- **安定性 (Stability)** : 同じ値を持つ要素の相対的な順序が、ソート前後で保たれるかどうかを示します。安定なソートでは、元の順序が維持されます。', '- **Stability**: Indicates whether the relative order of elements with the same value is preserved before and after sorting. In stable sorting, the original order is maintained.')

text = text.replace('隣り合う要素を比較し、順序が逆であれば交換するという操作を繰り返すアルゴリズムです。泡が水面へ浮かんでいくように、大きな要素が徐々に配列の末尾へと移動していきます。', 'An algorithm that repeats the operation of comparing adjacent elements and swapping them if they are in the wrong order. Like bubbles rising to the water surface, large elements gradually move to the end of the array.')

text = text.replace('要素数50のランダムな配列に対してバブルソートを実行した際の、各パス完了後の配列の状態を示します。バブルソートがどのように要素を右側に押し出していくかを観察してください。', 'Shows the state of the array after completing each pass when bubble sort is executed on a random array of 50 elements. Observe how bubble sort pushes elements to the right side.')

text = text.replace('このパスでは、未ソート部分の中で最大の要素が、まるで泡のように右端へと浮かび上がりました。バブルソートの特性上、1回のパスにつき少なくとも1つの要素が最終的な正しい位置に収まることが保証されます。そのため、パスを重ねるごとに探索範囲を1つずつ狭めていくことができ、無駄な比較操作を減らすことが可能です。しかしながら、データが完全に逆順に並んでいる最悪のケースでは、すべての要素ペアに対して交換操作が発生するため、計算量は $\\text{O}(n^2)$ に達し、パフォーマンスは極めて低くなります。', 'In this pass, the largest element in the unsorted part floated up to the right end like a bubble. Due to the characteristics of bubble sort, it is guaranteed that at least one element settles into its final correct position per pass. Therefore, as passes accumulate, the search range can be narrowed down one by one, reducing unnecessary comparison operations. However, in the worst-case scenario where the data is in completely reverse order, swap operations occur for all element pairs, so the time complexity reaches $\\text{O}(n^2)$, and performance becomes extremely low.')

text = text.replace('パス 44 で交換が発生しなかったため、ソート完了と判断して終了します。', 'Since no swaps occurred in pass 44, it determines that sorting is complete and terminates.')

text = text.replace('手元のトランプを並べ替えるときのように、未ソート部分から要素を一つずつ取り出し、ソート済み部分の適切な位置に挿入していくアルゴリズムです。', 'Like sorting playing cards in your hand, this algorithm takes elements one by one from the unsorted part and inserts them into the appropriate position in the sorted part.')

text = text.replace('挿入ソートは、すでにソートされている配列に対しては $\\text{O}(n)$ の時間で完了するという優れた特性を持っています。データ量が少ない場合や、大部分がソート済みのデータに対しては、定数倍のオーバーヘッドが小さいため、クイックソートやマージソートよりも高速に動作することがよくあります。この特性を活かし、多くの標準ライブラリ（PythonのTimSortなど）では、再帰の末端などのデータサイズが小さい場面で挿入ソートに切り替えるハイブリッドアプローチが採用されています。', 'Insertion sort has the excellent characteristic of completing in $\\text{O}(n)$ time for arrays that are already sorted. For small amounts of data or mostly sorted data, it often runs faster than quick sort or merge sort due to small constant factor overhead. Leveraging this trait, many standard libraries (like Python\'s TimSort) adopt a hybrid approach that switches to insertion sort when the data size is small, such as at the tail end of recursion.')

text = text.replace('要素数50のランダムな配列に対して挿入ソートを実行した際の、各要素挿入後の配列の状態を示します。左側のソート済み部分が徐々に拡大していく様子を確認できます。', 'Shows the state of the array after inserting each element when insertion sort is executed on a random array of 50 elements. You can confirm how the sorted part on the left gradually expands.')

text = text.replace('分割統治法を用いた非常に高速なアルゴリズムです。配列の中から基準値（ピボット）を選び、ピボットより小さい要素と大きい要素に分割します。この操作を再帰的に繰り返すことで全体をソートします。', 'A very fast algorithm using the divide-and-conquer method. It selects a reference value (pivot) from the array and divides it into elements smaller than the pivot and larger elements. The entire array is sorted by recursively repeating this operation.')

text = text.replace('クイックソートのパフォーマンスは、ピボットの選び方に大きく依存します。理想的には、常に配列の中央値（メジアン）をピボットとして選択できれば、配列は毎回正確に半分に分割され、再帰の深さは $\\text{O}(\\log n)$ となり、完璧な $\\text{O}(n \\log n)$ の計算量が保証されます。しかし、真の中央値を厳密に見つけ出すには追加の計算コストがかかるため、実用上は定数時間で選択できる近似手法が採用されます。', 'The performance of quick sort heavily depends on how the pivot is selected. Ideally, if the median of the array is always selected as the pivot, the array is accurately divided in half every time, the recursion depth becomes $\\text{O}(\\log n)$, and a perfect $\\text{O}(n \\log n)$ time complexity is guaranteed. However, since strictly finding the true median incurs additional computational costs, approximation methods that can be selected in constant time are practically adopted.')

text = text.replace('もし配列がすでにソートされている状態で、常に先頭の要素をピボットとして選択した場合、分割された配列の片方は要素数が0、もう片方は $n-1$ となり、再帰の深さが $n$ に達してしまいます。これにより、時間計算量は最悪の $\\text{O}(n^2)$ となり、場合によってはスタックオーバーフローを引き起こす危険性もあります。', 'If the array is already sorted and the first element is always selected as the pivot, one of the divided arrays will have 0 elements and the other $n-1$, and the recursion depth will reach $n$. As a result, the time complexity becomes the worst-case $\\text{O}(n^2)$, and in some cases, there is a risk of causing a stack overflow.')

text = text.replace('このような事態を防ぐため、ランダムにピボットを選択するランダム化クイックソートや、配列の先頭・中央・末尾の3つの要素の中央値をピボットとして採用する手法が一般的に用いられます。これにより、どのような入力データに対しても安定して高速なソート処理を実現できるようになります。', 'To prevent such situations, randomized quick sort, which randomly selects a pivot, or the method of adopting the median of three elements (first, middle, last) as the pivot is generally used. This makes it possible to achieve stable, high-speed sorting processing for any input data.')

text = text.replace('ジョン・フォン・ノイマンによって考案された、安定な外部ソートの代表格です。分割統治法に基づき、配列を細かく分割してから、それらをソートされた順序を保ちながら結合（マージ）していきます。', 'Invented by John von Neumann, it is a representative stable external sort. Based on the divide-and-conquer method, it finely divides the array and then combines (merges) them while preserving the sorted order.')

text = text.replace('マージソートの最大の特徴は、その **安定性** にあります。安定なソートとは、同じ値を持つ要素の相対的な順序がソート前後で変わらないことを意味します。この性質は、複数の異なる基準でデータを連続してソートする場合に極めて重要になります。', 'The biggest feature of merge sort is its **stability**. A stable sort means that the relative order of elements with the same value does not change before and after sorting. This property becomes extremely important when continuously sorting data based on multiple different criteria.')

text = text.replace('たとえば、生徒のデータを「テストの点数」でソートした後、「クラス名」でソートし直す場合を考えます。安定なソートアルゴリズムを使用すれば、同じクラスの生徒同士は「テストの点数」の順序が保たれたままになります。マージソートは、結合処理（マージ）において等しい要素の順序を厳密に管理するため、この安定性を完全に保証します。', 'For example, consider the case of sorting student data by "test score" and then resorting by "class name". If a stable sorting algorithm is used, students in the same class will maintain the order of their "test scores". Merge sort completely guarantees this stability because it strictly manages the order of equal elements during the merge process.')

text = text.replace('また、マージソートはデータへのアクセスが逐次的であるため、配列をメモリ上にすべて展開できないような巨大なデータセット（外部メモリ）をソートする際にも極めて有効です。ディスクI/Oの回数を最小限に抑えつつ、効率的にソート処理を進めることができます。これにより、データベースシステムや巨大ファイルの整列処理において、マージソートは今なお最前線で活用され続けています。', 'Also, because merge sort accesses data sequentially, it is extremely effective when sorting huge datasets (external memory) where the entire array cannot be expanded in memory. Sorting can proceed efficiently while minimizing the number of disk I/O operations. Because of this, merge sort continues to be used on the front lines in database systems and large file sorting processes.')

text = text.replace('さまざまなソートアルゴリズムを紹介してきましたが、実務において「唯一の正解」となるアルゴリズムは存在しません。データの性質や制約条件に応じて、適切なアルゴリズムを選択することが求められます。', 'We have introduced various sorting algorithms, but there is no "only correct answer" algorithm in practice. It is required to choose the appropriate algorithm according to the characteristics and constraints of the data.')

text = text.replace('- データ量が非常に少ない場合や、ほぼソート済みのデータには **挿入ソート** が効果的です。', '- **Insertion sort** is effective when the data volume is very small or for nearly sorted data.')
text = text.replace('- 一般的な用途で最高速を求める場合は **クイックソート** が最適です。', '- **Quick sort** is optimal when the highest speed is required for general purposes.')
text = text.replace('- 安定性が必要な場合や、最悪計算量を保証したい場合は **マージソート** が選ばれます。', '- **Merge sort** is selected when stability is needed or when the worst-case time complexity needs to be guaranteed.')
text = text.replace('- メモリ制約が厳しく、インプレースで安定した性能を出したい場合は **ヒープソート** が適しています。', '- **Heap sort** is suitable when memory constraints are tight and in-place stable performance is desired.')

text = text.replace('近代的なプログラミング言語（Python, Java, Rustなど）の標準ライブラリでは、これらのアルゴリズムの長所を組み合わせたハイブリッド手法（TimSortやIntroSortなど）が採用されており、開発者が自分でソートアルゴリズムをゼロから実装する機会は減っています。しかし、その内部でどのようなトレードオフが考慮されているかを理解することは、よりパフォーマンスの高い堅牢なソフトウェアを設計するための重要な基盤となります。', 'In standard libraries of modern programming languages (Python, Java, Rust, etc.), hybrid methods (such as TimSort and IntroSort) that combine the strengths of these algorithms are adopted, reducing the opportunities for developers to implement sorting algorithms from scratch themselves. However, understanding what trade-offs are considered internally is an important foundation for designing more performant and robust software.')

text = text.replace('この記事が、あなたのアルゴリズム学習と実務開発の助けになることを願っています。', 'We hope this article helps with your algorithm learning and practical development.')

text = text.replace('クイックソートは、実務において最も頻繁に利用されるアルゴリズムの一つです。最悪計算量は $\\text{O}(n^2)$ ですが、適切なピボット選択戦略（例えばMedian-of-Three）を用いることで、実質的には常に $\\text{O}(n \\log n)$ で動作します。Pythonの組み込みソート関数 `list.sort()` は、クイックソートではなく、マージソートと挿入ソートを組み合わせた **TimSort (ティムソート)** と呼ばれるアルゴリズムを採用しています。', 'Quick sort is one of the most frequently used algorithms in practice. Although its worst-case time complexity is $\\text{O}(n^2)$, by using appropriate pivot selection strategies (such as Median-of-Three), it essentially always operates in $\\text{O}(n \\log n)$. Python\'s built-in sort function `list.sort()` does not use quick sort, but instead adopts an algorithm called **TimSort**, which combines merge sort and insertion sort.')

# List replacements
text = text.replace('- **時間計算量（最良）**: $\\text{O}(n)$', '- **Time Complexity (Best)**: $\\text{O}(n)$')
text = text.replace('- **時間計算量（最良）**: $\\text{O}(n \\log n)$', '- **Time Complexity (Best)**: $\\text{O}(n \\log n)$')
text = text.replace('- **時間計算量（平均）**: $\\text{O}(n^2)$', '- **Time Complexity (Average)**: $\\text{O}(n^2)$')
text = text.replace('- **時間計算量（平均）**: $\\text{O}(n \\log n)$', '- **Time Complexity (Average)**: $\\text{O}(n \\log n)$')
text = text.replace('- **時間計算量（最悪）**: $\\text{O}(n^2)$', '- **Time Complexity (Worst)**: $\\text{O}(n^2)$')
text = text.replace('- **時間計算量（最悪）**: $\\text{O}(n \\log n)$', '- **Time Complexity (Worst)**: $\\text{O}(n \\log n)$')

text = text.replace('- **空間計算量**: $\\text{O}(1)$', '- **Space Complexity**: $\\text{O}(1)$')
text = text.replace('- **空間計算量**: $\\text{O}(\\log n)$', '- **Space Complexity**: $\\text{O}(\\log n)$')
text = text.replace('- **空間計算量**: $\\text{O}(n)$', '- **Space Complexity**: $\\text{O}(n)$')

text = text.replace('- **安定性**: 安定', '- **Stability**: Stable')
text = text.replace('- **安定性**: 不安定', '- **Stability**: Unstable')

text = text.replace('**初期状態**:', '**Initial state**:')
text = re.sub(r'\*\*パス (\d+) 完了後\*\*', r'**After pass \1**', text)
text = re.sub(r'\*\*ステップ (\d+) \(要素 (\d+) を挿入後\)\*\*', r'**Step \1 (After inserting element \2)**', text)

# Mermaid charts translation
mermaid_dict = {
    'A["配列の先頭から開始"]': 'A["Start from beginning of array"]',
    'B{"隣り合う要素を比較"}': 'B{"Compare adjacent elements"}',
    'C["要素を交換"]': 'C["Swap elements"]',
    'D["交換しない"]': 'D["Do not swap"]',
    'E["次のペアへ"]': 'E["Next pair"]',
    'F{"末尾に到達したか"}': 'F{"Reached end?"}',
    'G{"一度も交換しなかったか"}': 'G{"No swaps occurred?"}',
    'H["ソート完了"]': 'H["Sort complete"]',
    '|"左 > 右"|': '|"Left > Right"|',
    '|"左 <= 右"|': '|"Left <= Right"|',
    '|"次へ"|': '|"Next"|',
    '|"No"|': '|"No"|',
    '|"Yes"|': '|"Yes"|',
    
    'A["未ソート部分から1つ要素を取り出す"]': 'A["Take one element from unsorted part"]',
    'B{"ソート済み部分の末尾から比較"}': 'B{"Compare from end of sorted part"}',
    'C["要素を右にずらす"]': 'C["Shift element to right"]',
    'D["その位置に挿入"]': 'D["Insert at that position"]',
    'E{"すべての要素を処理したか"}': 'E{"Processed all elements?"}',
    'F["ソート完了"]': 'F["Sort complete"]',
    '|"取り出した要素より大きい"|': '|"Greater than extracted element"|',
    '|"取り出した要素以下"|': '|"Less than or equal to extracted element"|',
    '|"前へ"|': '|"Previous"|',
    
    'A["配列からピボットを選択"]': 'A["Select pivot from array"]',
    'B["配列を分割"]': 'B["Partition array"]',
    'C["ピボットより小さいグループ"]': 'C["Group smaller than pivot"]',
    'D["ピボットより大きいグループ"]': 'D["Group larger than pivot"]',
    'E{"要素数が1以下か"}': 'E{"1 or fewer elements?"}',
    'G["ソート完了"]': 'G["Sort complete"]',
    '|"分割1"|': '|"Partition 1"|',
    '|"分割2"|': '|"Partition 2"|',

    'A["配列を中央で2つに分割"]': 'A["Divide array in half at center"]',
    'B{"要素数が1以下か"}': 'B{"1 or fewer elements?"}',
    'C["分割完了"]': 'C["Division complete"]',
    'D["隣り合う部分配列をマージ"]': 'D["Merge adjacent subarrays"]',
    'E{"1つの配列になったか"}': 'E{"Became one array?"}'
}

for k, v in mermaid_dict.items():
    text = text.replace(k, v)

with open('c:/work/kenji.blog/content/post/sorting-algorithms-visualized-bubble-quick-merge/index.en.md', 'w', encoding='utf-8') as f:
    f.write(text)
