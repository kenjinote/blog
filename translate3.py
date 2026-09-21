import re

content = open('c:/work/kenji.blog/content/post/sorting-algorithms-visualized-bubble-quick-merge/index.zh-tw.md', 'r', encoding='utf-8').read()

content = re.sub(r'パス \d+ で交換が発生しなかったため、ソート完了と判断して終了します。', '因為在此次循環中沒有發生交換，所以判斷排序完成並結束。', content)
content = content.replace('手元のトランプを並べ替えるときのように、未ソート部分から要素を一つずつ取り出し、ソート済み部分の適切な位置に挿入していくアルゴリズムです。', '這是一種如同整理手中撲克牌般，從未排序部分逐一取出元素，並插入到已排序部分適當位置的演算法。')
content = content.replace('A["未ソート部分から1つ要素を取り出す"]', 'A["從未排序部分取出1個元素"]')
content = content.replace('B{"ソート済み部分の末尾から比較"}', 'B{"從已排序部分的末端開始比較"}')
content = content.replace('|"取り出した要素より大きい"|', '|"大於取出的元素"|')
content = content.replace('C["要素を右にずらす"]', 'C["將元素向右移動"]')
content = content.replace('|"取り出した要素以下"|', '|"小於等於取出的元素"|')
content = content.replace('D["その位置に挿入"]', 'D["插入到該位置"]')
content = content.replace('|"前へ"|', '|"往前"|')
content = content.replace('E{"すべての要素を処理したか"}', 'E{"是否已處理所有元素"}')
content = content.replace('|"Yes"|', '|"Yes"|')
content = content.replace('F["ソート完了"]', 'F["排序完成"]')

content = content.replace('### 挿入ソートの詳細トレース', '### 插入排序的詳細追蹤')
content = content.replace('要素数50のランダムな配列に対して挿入ソートを実行した際の、各要素挿入後の配列の状態を示します。左側のソート済み部分が徐々に拡大していく様子を確認できます。', '顯示針對具有 50 個元素的隨機陣列執行插入排序時，各個元素插入後的陣列狀態。可以確認到左側已排序部分逐漸擴大的情況。')
content = re.sub(r'\*\*ステップ (\d+) \(要素 (\d+) を挿入後\)\*\*', r'**步驟 \1 (插入元素 \2 後)**', content)

content = content.replace('挿入ソートは、すでにソートされている配列に対しては $\\text{O}(n)$ の時間で完了するという優れた特性を持っています。データ量が少ない場合や、大部分がソート済みのデータに対しては、定数倍のオーバーヘッドが小さいため、クイックソートやマージソートよりも高速に動作することがよくあります。この特性を活かし、多くの標準ライブラリ（PythonのTimSortなど）では、再帰の末端などのデータサイズが小さい場面で挿入ソートに切り替えるハイブリッドアプローチが採用されています。', '插入排序具有對已排序的陣列能以 $\\text{O}(n)$ 的時間完成的優秀特性。在資料量少的情況，或是大部分已排序的資料中，因為常數倍的負擔較小，所以通常會比快速排序或合併排序運作得更快。活用這項特性，在許多標準函式庫（如 Python 的 TimSort 等）中，會在遞迴末端等資料量較小的場景採用切換為插入排序的混合方法。')

with open('c:/work/kenji.blog/content/post/sorting-algorithms-visualized-bubble-quick-merge/index.zh-tw.md', 'w', encoding='utf-8') as f:
    f.write(content)
