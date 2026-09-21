import re

def translate():
    with open(r'c:\work\kenji.blog\content\post\dynamic-programming-dp-introduction-knapsack-fibonacci\index.md', 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Front matter
    text = re.sub(r'title: .*', 'title: "Introducción a la Programación Dinámica (DP) y problemas famosos (Mochila, Fibonacci)"', text)
    text = re.sub(r'description: .*', 'description: "El gran obstáculo de los algoritmos, la «Programación Dinámica (DP)». Explicamos la diferencia entre la recursión con memorización y el enfoque de abajo hacia arriba de forma sencilla, usando la secuencia de Fibonacci y el problema de la mochila como ejemplos."', text)
    text = re.sub(r'categories: .*', 'categories: ["ciencia-de-la-computacion"]', text)
    text = re.sub(r'tags: .*', 'tags: ["algoritmos", "programacion-dinamica", "dp", "mochila", "optimizacion"]', text)

    # Math
    text = text.replace(r'\text{for }', r'\text{para }')
    text = text.replace(r'\text{if }', r'\text{si }')
    text = text.replace(r'\text{otherwise}', r'\text{en otro caso}')

    # Code comments
    text = text.replace('# DPテーブルの初期化: (N+1) x (W+1) の2次元配列', '# Inicialización de la tabla DP: array 2D de (N+1) x (W+1)')
    text = text.replace('# DPテーブルを埋める', '# Llenar la tabla DP')
    text = text.replace('# 選ぶ場合と選ばない場合の最大値を取る', '# Tomar el valor máximo entre elegir y no elegir')
    text = text.replace('# 容量オーバーで選べない場合', '# Caso en que no se puede elegir por exceso de capacidad')
    text = text.replace('# 逆順に更新することで、1次元配列で済む', '# Al actualizar en orden inverso, basta con un array 1D')

    # Text replacements
    text = text.replace('# 1. はじめに', '# 1. Introducción')
    text = text.replace('プログラミングやアルゴリズムの学習を進めていくと、多くの学習者が直面する大きな壁があります。それが **動的計画法** （Dynamic Programming、略して **DP** ）です。名前だけを聞くと、「何だか難しそう」「数学の専門知識が必要なのでは？」と身構えてしまうかもしれません。しかし、本質を理解すれば、DPは非常に強力で、かつ直感的な問題解決手法であることがわかります。', 'Al avanzar en el aprendizaje de programación y algoritmos, hay un gran obstáculo al que se enfrentan muchos estudiantes. Ese es la **Programación Dinámica** (Dynamic Programming, abreviado como **DP** ). Solo al escuchar el nombre, podrías ponerte a la defensiva pensando: «Parece difícil» o «¿No se necesitan conocimientos matemáticos especializados?». Sin embargo, si entiendes su esencia, te darás cuenta de que la DP es un método de resolución de problemas muy poderoso y, a la vez, intuitivo.')
    text = text.replace('本記事では、DPの基本概念から出発し、代表的な問題である「フィボナッチ数列」と「ナップサック問題」を例に、その考え方と実装方法を徹底的に解説します。Pythonのコードを交えながら、段階的に理解を深めていきましょう。', 'En este artículo, partiendo de los conceptos básicos de la DP y usando como ejemplos problemas representativos como la «secuencia de Fibonacci» y el «problema de la mochila», explicaremos exhaustivamente su forma de pensar y métodos de implementación. Profundicemos en su comprensión paso a paso, intercalando código en Python.')

    text = text.replace('# 2. 動的計画法（DP）とは何か？', '# 2. ¿Qué es la Programación Dinámica (DP)?')
    text = text.replace('動的計画法（Dynamic Programming）は、複雑な問題を複数の小さな部分問題に分割し、それぞれの部分問題の解を記録（メモ）しながら解き進める手法です。これにより、同じ計算を繰り返す無駄を省き、計算時間を劇的に短縮することができます。', 'La Programación Dinámica (Dynamic Programming) es un método que divide un problema complejo en varios subproblemas más pequeños y avanza resolviéndolos mientras registra (memoriza) las soluciones de cada subproblema. Con esto, se elimina el desperdicio de repetir los mismos cálculos y se puede reducir drásticamente el tiempo de computación.')
    text = text.replace('DPの核心は以下の2つの特徴にあります。', 'El núcleo de la DP reside en las siguientes 2 características.')
    text = text.replace('1.  **部分構造最適性** （Optimal Substructure）：大きな問題の最適解が、その小さな部分問題の最適解から構成できるという性質。', '1.  **Subestructura Óptima** (Optimal Substructure): La propiedad de que la solución óptima de un problema grande se puede componer a partir de las soluciones óptimas de sus subproblemas pequeños.')
    text = text.replace('2.  **部分問題の重複** （Overlapping Subproblems）：同じ小さな問題が何度も繰り返し現れるという性質。', '2.  **Superposición de Subproblemas** (Overlapping Subproblems): La propiedad de que el mismo subproblema pequeño aparece repetidamente varias veces.')
    text = text.replace('これらの特徴を持つ問題に対して、DPは絶大な威力を発揮します。', 'Para problemas que tienen estas características, la DP demuestra un poder inmenso.')

    text = text.replace('## DPの2つのアプローチ', '## 2 enfoques de la DP')
    text = text.replace('DPには、大きく分けて2つの実装アプローチがあります。', 'La DP se divide a grandes rasgos en 2 enfoques de implementación.')
    text = text.replace('### 1. メモ化再帰（トップダウン方式）', '### 1. Recursión con memorización (Enfoque Top-down)')
    text = text.replace('大きな問題から出発し、再帰的に小さな問題を呼び出します。その際、一度計算した結果を配列やハッシュマップに保存（メモ）しておき、同じ問題が再度現れたときは、再計算せずにメモした値を返します。', 'Se parte de un problema grande y se llaman recursivamente a problemas más pequeños. En ese momento, los resultados calculados una vez se guardan (memorizan) en un array o hash map, y cuando el mismo problema vuelve a aparecer, se devuelve el valor memorizado sin recalcularlo.')
    text = text.replace('### 2. ボトムアップ方式（分割統治とテーブル埋め）', '### 2. Enfoque Bottom-up (Divide y vencerás y llenado de tablas)')
    text = text.replace('最も小さな問題から順に解を計算し、配列（DPテーブル）に記録していきます。小さな問題の解を使って徐々に大きな問題を解き、最終的に求めたい問題の解を得ます。', 'Se calculan las soluciones en orden desde el problema más pequeño y se registran en un array (tabla DP). Usando las soluciones de los problemas pequeños se resuelven gradualmente los problemas más grandes y, finalmente, se obtiene la solución del problema que se desea encontrar.')

    text = text.replace('# 3. 基礎編：フィボナッチ数列で学ぶDP', '# 3. Nivel Básico: Aprender DP con la secuencia de Fibonacci')
    text = text.replace('DPの概念を理解するための最初の一歩として、フィボナッチ数列を取り上げます。', 'Como primer paso para entender el concepto de la DP, tomaremos la secuencia de Fibonacci.')
    text = text.replace('フィボナッチ数列は、次のように定義される数列です。', 'La secuencia de Fibonacci es una secuencia definida de la siguiente manera.')

    text = text.replace('## 3.1 単純な再帰呼び出しの罠', '## 3.1 La trampa de la llamada recursiva simple')
    text = text.replace('定義通りにPythonで関数を書いてみましょう。', 'Vamos a escribir la función en Python tal como se define.')
    text = text.replace('この実装は直感的ですが、大きな問題があります。それは **計算量が指数関数的に増大する** ということです。$F(5)$ を計算する際の関数の呼び出しツリーを見てみましょう。', 'Esta implementación es intuitiva, pero tiene un gran problema. Eso es que **la complejidad computacional aumenta exponencialmente** . Veamos el árbol de llamadas de la función al calcular $F(5)$.')
    text = text.replace('ご覧の通り、$F(3)$ や $F(2)$ が何度も重複して計算されています。計算量は $O(2^n)$ となり、$n$ が大きくなると実用的な時間で計算が終わらなくなります。', 'Como pueden ver, $F(3)$ y $F(2)$ se calculan repetidamente muchas veces. La complejidad computacional es de $O(2^n)$, y a medida que $n$ se hace grande, el cálculo no terminará en un tiempo práctico.')

    text = text.replace('## 3.2 メモ化再帰（トップダウン方式）', '## 3.2 Recursión con memorización (Enfoque Top-down)')
    text = text.replace('この無駄を省くのが **メモ化** です。一度計算した結果を保存しておきましょう。', 'Lo que elimina este desperdicio es la **memorización** . Guardemos los resultados calculados una vez.')
    text = text.replace('これにより、各 $F(i)$ は一度しか計算されなくなり、計算量は $O(n)$ に激減します。', 'Con esto, cada $F(i)$ solo se calculará una vez y la complejidad computacional se reducirá drásticamente a $O(n)$.')

    text = text.replace('## 3.3 ボトムアップ方式（DPテーブル）', '## 3.3 Enfoque Bottom-up (Tabla DP)')
    text = text.replace('再帰呼び出しのオーバーヘッドを避けるため、下から順に計算していくのがボトムアップ方式です。', 'Para evitar la sobrecarga de las llamadas recursivas, el enfoque bottom-up calcula en orden desde abajo.')
    text = text.replace('配列 `dp` を用意し、インデックスが小さい方から順番に埋めていきます。これが典型的なDPテーブルの使い方です。', 'Preparamos un array `dp` y lo llenamos en orden desde los índices más pequeños. Este es el uso típico de una tabla DP.')

    text = text.replace('# 4. 応用編：ナップサック問題', '# 4. Nivel Aplicado: Problema de la mochila')
    text = text.replace('DPの真骨頂は、最適化問題を解くときに発揮されます。ここでは有名な「0-1ナップサック問題」を考えましょう。', 'El verdadero valor de la DP se muestra al resolver problemas de optimización. Aquí consideraremos el famoso «problema de la mochila 0-1».')

    text = text.replace('## 4.1 問題設定', '## 4.1 Configuración del problema')
    text = text.replace('あなたは泥棒です（という設定です）。容量が $W$ のナップサックを持っています。目の前には $N$ 個の品物があり、それぞれの品物 $i$ には重さ $w_i$ と価値 $v_i$ が設定されています。', 'Eres un ladrón (esa es la premisa). Tienes una mochila con capacidad $W$. Delante de ti hay $N$ artículos, y cada artículo $i$ tiene asignado un peso $w_i$ y un valor $v_i$.')
    text = text.replace('ナップサックの容量を超えない範囲で品物を選び、持ち帰る品物の **価値の合計を最大化** してください。ただし、各品物は1つしかなく、「選ぶ（1）」か「選ばない（0）」かのどちらかです。', 'Selecciona los artículos sin exceder la capacidad de la mochila y **maximiza la suma de valores** de los artículos que te llevas. Sin embargo, solo hay un artículo de cada tipo, por lo que debes elegir «llevar (1)» o «no llevar (0)».')

    text = text.replace('## 4.2 状態の定義と漸化式', '## 4.2 Definición del estado y relación de recurrencia')
    text = text.replace('DPで問題を解く際、最も重要なのが **状態の定義** と **漸化式（状態遷移方程式）** の導出です。', 'Al resolver problemas con DP, lo más importante es la **definición del estado** y la derivación de la **relación de recurrencia (ecuación de transición de estado)** .')
    text = text.replace('状態を次のように定義します。', 'Definimos el estado de la siguiente manera.')
    text = text.replace('$dp[i][w]$ ：最初の $i$ 個の品物の中から、重さの合計が $w$ 以下になるように選んだときの価値の最大値。', '$dp[i][w]$ : El valor máximo cuando se eligen entre los primeros $i$ artículos de modo que la suma de los pesos sea menor o igual a $w$.')
    text = text.replace('ここで、$i$ 番目の品物（重さ $w_i$、価値 $v_i$）を考えるとき、次の2つの選択肢があります。', 'Aquí, al considerar el artículo número $i$ (peso $w_i$, valor $v_i$), hay 2 opciones.')
    text = text.replace('1.  **選ばない場合**：', '1.  **Caso de no elegir** :')
    text = text.replace('    価値の最大値は、前の状態 $dp[i-1][w]$ と同じです。', '    El valor máximo es el mismo que el del estado anterior $dp[i-1][w]$.')
    text = text.replace('2.  **選ぶ場合**（ただし $w \ge w_i$ の場合のみ可能）：', '2.  **Caso de elegir** (solo posible si $w \ge w_i$):')
    text = text.replace('    容量から $w_i$ を引いた状態に、品物 $i$ の価値 $v_i$ を足します。すなわち、$dp[i-1][w - w_i] + v_i$ となります。', '    Al estado en el que se ha restado $w_i$ a la capacidad, le sumamos el valor $v_i$ del artículo $i$. Es decir, se convierte en $dp[i-1][w - w_i] + v_i$.')
    text = text.replace('したがって、漸化式は次のようになります。', 'Por lo tanto, la relación de recurrencia es la siguiente.')

    text = text.replace('## 4.3 Python実装', '## 4.3 Implementación en Python')
    text = text.replace('この漸化式をそのままプログラムに落とし込みます。', 'Llevaremos esta relación de recurrencia directamente a un programa.')

    text = text.replace('### DPテーブルの推移', '### Transición de la tabla DP')
    text = text.replace('ある例での `dp` テーブルの推移を追ってみましょう。', 'Vamos a seguir la transición de la tabla `dp` en un ejemplo.')
    text = text.replace('このように、小さな容量・少ない品数の部分問題から順に最適解を求めていくことで、最終的に答えが求まります。', 'De esta manera, al encontrar la solución óptima en orden desde los subproblemas con poca capacidad y pocos artículos, finalmente se encuentra la respuesta.')

    text = text.replace('# 5. より深くDPを理解するための詳細解説とアルゴリズムの探求', '# 5. Explicación detallada y exploración de algoritmos para entender la DP más profundamente')
    text = text.replace('DPへの理解を確固たるものにするためには、より多くの例題に触れ、様々なパターンの状態遷移を学ぶことが不可欠です。', 'Para consolidar la comprensión de la DP, es esencial exponerse a más ejemplos y aprender los diversos patrones de transición de estados.')

    text = text.replace('## 5.1 編集距離（レーベンシュタイン距離）', '## 5.1 Distancia de edición (Distancia de Levenshtein)')
    text = text.replace('二つの文字列 $S$ と $T$ が与えられたとき、$S$ に「挿入」「削除」「置換」の操作を最小何回行えば $T$ に変換できるかを求める問題です。', 'Dadas dos cadenas $S$ y $T$, es un problema para encontrar el número mínimo de operaciones de «inserción», «eliminación» y «sustitución» necesarias en $S$ para convertirla en $T$.')
    text = text.replace('### 漸化式', '### Relación de recurrencia')

    text = text.replace('## 5.2 空間計算量の最適化技術（インプレース更新）', '## 5.2 Técnica de optimización de la complejidad espacial (Actualización in-place)')
    text = text.replace('これまでの実装では、状態遷移の計算に $O(NW)$ や $O(MN)$ のメモリを使用してきました。しかし、漸化式をよく観察すると、ある状態の更新には「一つ前の行」しか必要ないことが多いです。', 'En las implementaciones hasta ahora, hemos estado usando una memoria de $O(NW)$ u $O(MN)$ para calcular las transiciones de estados. Sin embargo, observando de cerca la relación de recurrencia, para actualizar un cierto estado, a menudo solo se necesita la «fila anterior».')
    text = text.replace('例えば、ナップサック問題の漸化式を利用して、2次元配列を1次元配列に削減することができます。更新の際、右から左に向かって更新することで、現在の $i$ の計算中に $i-1$ の値を上書きしてしまうバグを防ぐことができます。', 'Por ejemplo, utilizando la relación de recurrencia del problema de la mochila, un array 2D se puede reducir a un array 1D. Al momento de actualizar, al hacerlo de derecha a izquierda, se puede evitar el error de sobrescribir el valor de $i-1$ durante el cálculo actual de $i$.')

    text = text.replace('動的計画法の強みは部分構造の重複を避けることですが、それでもすべての問題が高速に解けるわけではありません。例えば、ナップサック問題の計算量は $O(NW)$ であり、これは一見多項式時間に見えます。しかし、$W$ は入力の「値」であり、入力サイズ（ビット数）に対しては指数的な大きさになり得ます。このような計算量を **擬似多項式時間** と呼びます。', 'La fuerza de la programación dinámica radica en evitar la superposición de subestructuras, pero aun así, no todos los problemas se pueden resolver a alta velocidad. Por ejemplo, la complejidad computacional del problema de la mochila es de $O(NW)$, lo que a primera vista parece tiempo polinomial. Sin embargo, $W$ es el «valor» de entrada, que puede ser exponencialmente grande en relación con el tamaño de la entrada (número de bits). A esta complejidad computacional se le llama **tiempo pseudopolinomial** .')
    text = text.replace('もし $W$ が非常に大きい場合、配列の確保だけでメモリが枯渇し、ループ回数も膨大になるため、このDP手法は適用できなくなります。その場合は、価値の総和の上限 $V$ に対するDPに切り替えるか、半分全列挙（Meet in the Middle）などの別のアプローチが必要になります。', 'Si $W$ es muy grande, simplemente con reservar el array se agotará la memoria, y el número de bucles será enorme, por lo que este método de DP no se podrá aplicar. En ese caso, se debe cambiar a una DP respecto al límite superior de la suma de los valores $V$, o se requerirá un enfoque diferente como la enumeración de la mitad completa (Meet in the Middle).')
    text = text.replace('また、DPのデバッグにおいては、 **小規模な入力で手計算したテーブルと、プログラムが出力するテーブルを比較する** ことが最も効果的です。紙とペンを用意し、2次元の表を実際に書いてみることで、「なぜこの漸化式になるのか」「どこで遷移を間違えているのか」が手に取るようにわかります。', 'Además, en la depuración de DP, **comparar una tabla calculada a mano con una entrada pequeña con la tabla que genera el programa** es lo más efectivo. Al preparar papel y lápiz e intentar escribir la tabla 2D, podrás entender a la perfección «por qué se convierte en esta relación de recurrencia» o «dónde te equivocaste en la transición».')

    text = text.replace('# 6. おわりに', '# 6. Conclusión')
    text = text.replace('動的計画法（DP）は、初めはとっつきにくく感じるかもしれません。しかし、フィボナッチ数列での「無駄な計算の排除」という直感的な理解から出発し、ナップサック問題のような「状態と遷移の定義」へと段階を踏むことで、必ずマスターすることができます。', 'Al principio, podrías sentir que es difícil acercarse a la Programación Dinámica (DP). Sin embargo, partiendo de una comprensión intuitiva como la «eliminación de cálculos inútiles» en la secuencia de Fibonacci, y avanzando hacia la «definición de estados y transiciones» como en el problema de la mochila, definitivamente podrás dominarla.')
    text = text.replace('**「状態をどう定義するか」**', '**«Cómo definir el estado»**')
    text = text.replace('**「その状態はどういう小さな状態から計算できるか（漸化式）」**', '**«A partir de qué pequeños estados se puede calcular ese estado (relación de recurrencia)»**')
    text = text.replace('この2点を見抜く力を養うには、多くの問題に触れ、自分の手でDPテーブルを書いてみることが一番の近道です。ぜひ、本記事で学んだ知識を武器に、挑戦してみてください。', 'Para cultivar la capacidad de ver a través de estos 2 puntos, la forma más rápida es interactuar con muchos problemas e intentar escribir tablas DP con tus propias manos. Por favor, asume el desafío armado con los conocimientos aprendidos en este artículo.')

    # Using regex to replace all sections from 1 to 40
    text = re.sub(r'### 発展解説パート \d+：DPの限界とアルゴリズム選択', lambda m: m.group(0).replace('### 発展解説パート', '### Parte de Explicación Avanzada').replace('：DPの限界とアルゴリズム選択', ': Límites de la DP y selección de algoritmos'), text)

    with open(r'c:\work\kenji.blog\content\post\dynamic-programming-dp-introduction-knapsack-fibonacci\index.es.md', 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == "__main__":
    translate()
