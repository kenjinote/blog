from pathlib import Path
import re,json,hashlib
root=Path.cwd(); bundle=root/'content/post/Qiskit入門'; today='2026-11-24'; source_rel=f'post/{bundle.name}/index.md'
refs=[
('Qiskit installation','https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit'),
('Local simulators','https://quantum.cloud.ibm.com/docs/en/guides/local-simulators'),
('Qiskit 1.0 migration notes','https://quantum.cloud.ibm.com/docs/en/guides/qiskit-1.0-features'),
('QuantumCircuit API','https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.QuantumCircuit'),
('AerSimulator API','https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html')]
code="""```bash
python -m pip install qiskit qiskit-aer
```

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure_all()

simulator = AerSimulator()
result = simulator.run(circuit, shots=1000).result()
print(result.get_counts(circuit))
```"""
R={
'ja':("Qiskitで学ぶ量子プログラミング入門","量子ビット、測定、もつれの基本を説明し、現在のQiskitとAerSimulatorでベル状態をシミュレーションします。",r"""# 量子プログラミングの基本

量子コンピュータは量子力学に従う状態を操作して計算します。量子計算があらゆる問題を速く解くわけではなく、特定の問題や条件で古典計算に対する高速化が知られています。実用上の性能は、アルゴリズム、ハードウェア、ノイズ、誤り訂正などに左右されます。

## 量子ビットと測定

1量子ビットの純粋状態は $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$ と表せ、$|\alpha|^2+|\beta|^2=1$ です。計算基底で測定すると、0と1がそれぞれ $|\alpha|^2$、$|\beta|^2$ の確率で得られます。n量子ビットの状態ベクトルには $2^n$ 個の振幅がありますが、これは2^n個の答えを一度に読み出せることや、一般の計算が指数的に速くなることを意味しません。

## ゲートともつれ

量子ゲートは量子状態に作用するユニタリ変換です。Xゲートは0と1を交換し、Hゲートは基底状態を重ね合わせへ移し、CNOTは制御ビットが1のとき標的ビットを反転します。Hを第1量子ビットに適用し、続けてCNOTを適用すると、$(|00\rangle+|11\rangle)/\sqrt{2}$ というベル状態が得られます。測定結果には相関がありますが、もつれを使って光速より速く情報を送ることはできません。

## Qiskitのインストールとベル状態

Qiskit SDKは量子回路の作成・変換に使います。Qiskit 1.0以降、Aerシミュレータは別パッケージの `qiskit-aer` です。以下はローカルの理想シミュレーションで、実機のノイズや性能を再現するものではありません。

"""+code+r"""

理想シミュレータでは、測定結果は `00` と `11` だけになり、その回数はショット数を増やすとおおむね半分ずつに近づきます。有限回の測定では偏りが生じます。実機ではノイズにより `01` や `10` も出ることがあります。ビット列の表示順序は古典レジスタの規約を確認してください。

## アルゴリズムの速度について

Deutsch–Jozsaの1回のオラクル呼出しという結果は、関数が定数か均衡かという約束と理想的なオラクルを仮定したクエリ計算量の話です。Grover探索は、N個から印の付いた項目を探す非構造化探索で、理想的なオラクル呼出しを $O(\sqrt{N})$ 回にできます。これは一般のデータベース処理全体が同じ倍率で速くなるという意味ではありません。

## 参考資料

"""+"\n".join(f'- [{n}]({u})' for n,u in refs)),
'en':("An Introduction to Quantum Programming with Qiskit","Learn the basics of qubits, measurement, and entanglement, then simulate a Bell state with current Qiskit and AerSimulator.",r"""# Quantum-programming basics

Quantum computers process states governed by quantum mechanics. They do not solve every problem faster: speedups are known for particular problems under particular assumptions. Practical performance depends on the algorithm, hardware, noise, and error correction.

## Qubits and measurement

A pure state of one qubit is $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$, with $|\alpha|^2+|\beta|^2=1$. Measurement in the computational basis returns 0 or 1 with probabilities $|\alpha|^2$ and $|\beta|^2$. An n-qubit state vector has $2^n$ amplitudes, but that does not let us read out $2^n$ answers at once or make arbitrary computations exponentially faster.

## Gates and entanglement

Quantum gates are unitary transformations on quantum states. X swaps 0 and 1; H creates a superposition from a basis state; CNOT flips its target when its control is 1. Applying H to the first qubit and then CNOT produces the Bell state $(|00\rangle+|11\rangle)/\sqrt{2}$. Its measurement outcomes are correlated, but entanglement cannot transmit information faster than light.

## Install Qiskit and build a Bell circuit

The Qiskit SDK creates and transforms circuits. Since Qiskit 1.0, Aer is a separate package, `qiskit-aer`. This example uses an ideal local simulator; it does not model hardware noise or hardware performance.

"""+code+r"""

In an ideal simulation, only `00` and `11` occur, with counts approaching an even split as the number of shots increases. Finite sampling can be uneven. Hardware noise can also produce `01` or `10`. Check the classical-register convention when interpreting bit-string order.

## About algorithmic speedups

The one-query Deutsch–Jozsa result is a query-complexity statement under the promise that the function is constant or balanced and assuming an ideal oracle. Grover search can find a marked item among N unstructured candidates with $O(\sqrt{N})$ ideal oracle calls. This does not mean every database task becomes faster by that factor.

## References

"""+"\n".join(f'- [{n}]({u})' for n,u in refs)),
'zh-cn':("Qiskit量子编程入门","了解量子比特、测量和纠缠的基础，并使用当前版本的Qiskit与AerSimulator模拟贝尔态。",r"""# 量子编程基础

量子计算机通过操控遵循量子力学的状态来计算。它并不能让所有问题都更快；已知的加速只适用于特定问题和前提。实际性能取决于算法、硬件、噪声和纠错。

## 量子比特与测量

单个量子比特的纯态可写为 $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$，且 $|\alpha|^2+|\beta|^2=1$。在计算基下测量，得到0或1的概率分别为 $|\alpha|^2$ 和 $|\beta|^2$。n个量子比特的状态向量有 $2^n$ 个振幅，但这不代表能一次读出 $2^n$ 个答案，也不代表任意计算都会获得指数级加速。

## 量子门与纠缠

量子门是作用于量子态的酉变换。X门交换0和1；H门将基态变为叠加态；当控制位为1时，CNOT门翻转目标位。先对第一个量子比特施加H门，再施加CNOT，可得到贝尔态 $(|00\rangle+|11\rangle)/\sqrt{2}$。其测量结果具有相关性，但纠缠不能用于超光速传递信息。

## 安装Qiskit并构造贝尔态电路

Qiskit SDK用于创建和转换量子电路。自Qiskit 1.0起，Aer模拟器由单独的 `qiskit-aer` 软件包提供。以下示例使用本机理想模拟器，不模拟真实硬件的噪声或性能。

"""+code+r"""

理想模拟只会得到 `00` 和 `11`，随着测量次数增加，计数大致趋于各占一半。有限次采样会有偏差。真实硬件的噪声也可能产生 `01` 或 `10`。解释比特串顺序时，请核对经典寄存器的约定。

## 关于算法加速

Deutsch–Jozsa算法的一次预言机调用结论，是在函数满足“常数或均衡”的承诺并假设预言机理想时，对查询复杂度的描述。Grover搜索在N个无结构候选项中寻找标记项，需要 $O(\sqrt{N})$ 次理想预言机调用。这不表示所有数据库任务都会按该比例加速。

## 参考资料

"""+"\n".join(f'- [{n}]({u})' for n,u in refs)),
'zh-tw':("Qiskit 量子程式設計入門","認識量子位元、測量與糾纏，並使用目前版本的 Qiskit 和 AerSimulator 模擬貝爾態。",r"""# 量子程式設計基礎

量子電腦透過操控遵循量子力學的狀態來計算。它不會讓所有問題都變快；已知的加速只適用於特定問題與前提。實際效能取決於演算法、硬體、雜訊與錯誤更正。

## 量子位元與測量

單一量子位元的純態可寫成 $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$，且 $|\alpha|^2+|\beta|^2=1$。在計算基底測量時，得到0或1的機率分別為 $|\alpha|^2$ 和 $|\beta|^2$。n個量子位元的狀態向量有 $2^n$ 個振幅，但這不代表能一次讀出 $2^n$ 個答案，也不代表任意計算都會獲得指數級加速。

## 量子閘與糾纏

量子閘是作用於量子狀態的么正變換。X閘交換0與1；H閘將基底狀態轉成疊加態；控制位為1時，CNOT閘會翻轉目標位。先對第一個量子位元施加H閘，再施加CNOT，可得到貝爾態 $(|00\rangle+|11\rangle)/\sqrt{2}$。其測量結果彼此相關，但糾纏不能用來超光速傳遞資訊。

## 安裝 Qiskit 並建立貝爾態電路

Qiskit SDK 用來建立與轉換量子電路。自 Qiskit 1.0 起，Aer 模擬器由獨立套件 `qiskit-aer` 提供。以下範例使用本機理想模擬器，不模擬真實硬體的雜訊或效能。

"""+code+r"""

理想模擬只會得到 `00` 和 `11`；測量次數增加時，計數大致趨近各半。有限次取樣仍可能不均。真實硬體雜訊也可能產生 `01` 或 `10`。解讀位元字串順序時，請確認古典暫存器的慣例。

## 關於演算法加速

Deutsch–Jozsa 演算法的一次預言機呼叫，是在函數符合「常數或平衡」承諾並假設預言機理想時的查詢複雜度結果。Grover 搜尋在 N 個無結構候選項中尋找標記項，需要 $O(\sqrt{N})$ 次理想預言機呼叫。這不表示所有資料庫工作都會按此比例加速。

## 參考資料

"""+"\n".join(f'- [{n}]({u})' for n,u in refs)),
'es':("Introducción a la programación cuántica con Qiskit","Aprende los conceptos de qubits, medición y entrelazamiento, y simula un estado de Bell con Qiskit y AerSimulator actuales.",r"""# Fundamentos de la programación cuántica

Las computadoras cuánticas calculan manipulando estados que obedecen la mecánica cuántica. No aceleran todos los problemas: las ventajas conocidas se aplican a problemas y supuestos específicos. El rendimiento práctico depende del algoritmo, el hardware, el ruido y la corrección de errores.

## Qubits y medición

El estado puro de un qubit se expresa como $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$, con $|\alpha|^2+|\beta|^2=1$. Al medir en la base computacional, se obtiene 0 o 1 con probabilidades $|\alpha|^2$ y $|\beta|^2$. El vector de estado de n qubits tiene $2^n$ amplitudes, pero eso no permite leer $2^n$ respuestas de una vez ni hace exponencialmente más rápido cualquier cálculo.

## Puertas y entrelazamiento

Las puertas cuánticas son transformaciones unitarias de los estados. X intercambia 0 y 1; H lleva un estado base a una superposición; CNOT invierte el objetivo cuando el control es 1. Aplicar H al primer qubit y después CNOT produce el estado de Bell $(|00\rangle+|11\rangle)/\sqrt{2}$. Sus mediciones están correlacionadas, pero el entrelazamiento no permite transmitir información más rápido que la luz.

## Instalar Qiskit y crear un circuito de Bell

El SDK de Qiskit sirve para crear y transformar circuitos. Desde Qiskit 1.0, Aer se distribuye por separado como `qiskit-aer`. El ejemplo usa un simulador local ideal; no reproduce el ruido ni el rendimiento del hardware real.

"""+code+r"""

En una simulación ideal solo aparecen `00` y `11`, con recuentos que se aproximan a la mitad al aumentar los tiros. El muestreo finito puede variar. El ruido del hardware también puede producir `01` o `10`. Comprueba la convención del registro clásico al interpretar el orden de los bits.

## Sobre la velocidad de los algoritmos

El resultado de una consulta de Deutsch–Jozsa es de complejidad de consultas y presupone que la función promete ser constante o equilibrada, además de un oráculo ideal. Grover puede encontrar un elemento marcado entre N candidatos sin estructura en $O(\sqrt{N})$ consultas ideales al oráculo. Esto no significa que toda tarea con bases de datos se acelere en esa proporción.

## Referencias

"""+"\n".join(f'- [{n}]({u})' for n,u in refs)),
'fr':("Introduction à la programmation quantique avec Qiskit","Découvrez les qubits, la mesure et l’intrication, puis simulez un état de Bell avec les versions actuelles de Qiskit et AerSimulator.",r"""# Bases de la programmation quantique

Les ordinateurs quantiques calculent en manipulant des états régis par la mécanique quantique. Ils n’accélèrent pas tous les problèmes : les accélérations connues concernent des problèmes et des hypothèses spécifiques. Les performances pratiques dépendent de l’algorithme, du matériel, du bruit et de la correction d’erreurs.

## Qubits et mesure

L’état pur d’un qubit s’écrit $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$, avec $|\alpha|^2+|\beta|^2=1$. Une mesure dans la base computationnelle renvoie 0 ou 1 avec les probabilités $|\alpha|^2$ et $|\beta|^2$. Le vecteur d’état de n qubits comporte $2^n$ amplitudes, mais cela ne permet pas de lire $2^n$ réponses à la fois et ne rend pas tout calcul exponentiellement plus rapide.

## Portes et intrication

Les portes quantiques sont des transformations unitaires des états. X échange 0 et 1 ; H transforme un état de base en superposition ; CNOT inverse la cible lorsque le contrôle vaut 1. Appliquer H au premier qubit puis CNOT produit l’état de Bell $(|00\rangle+|11\rangle)/\sqrt{2}$. Les mesures sont corrélées, mais l’intrication ne permet pas de transmettre de l’information plus vite que la lumière.

## Installer Qiskit et créer un circuit de Bell

Le SDK Qiskit sert à créer et transformer des circuits. Depuis Qiskit 1.0, Aer est distribué séparément dans `qiskit-aer`. L’exemple utilise un simulateur local idéal ; il ne reproduit ni le bruit ni les performances d’un matériel réel.

"""+code+r"""

Une simulation idéale ne produit que `00` et `11`, avec des comptes qui tendent vers la moitié chacun lorsque le nombre de tirs augmente. Un échantillon fini peut être déséquilibré. Le bruit matériel peut aussi produire `01` ou `10`. Vérifiez la convention du registre classique pour interpréter l’ordre des bits.

## À propos de l’accélération des algorithmes

Le résultat d’une requête de Deutsch–Jozsa relève de la complexité des requêtes et suppose que la fonction promise est constante ou équilibrée, ainsi qu’un oracle idéal. Grover trouve un élément marqué parmi N candidats non structurés en $O(\sqrt{N})$ appels idéaux à l’oracle. Cela ne signifie pas que toute tâche sur une base de données s’accélère dans cette proportion.

## Références

"""+"\n".join(f'- [{n}]({u})' for n,u in refs)),
'de':("Einführung in Quantenprogrammierung mit Qiskit","Lernen Sie Qubits, Messung und Verschränkung kennen und simulieren Sie einen Bell-Zustand mit aktuellem Qiskit und AerSimulator.",r"""# Grundlagen der Quantenprogrammierung

Quantencomputer berechnen durch Manipulation von Zuständen, die der Quantenmechanik folgen. Sie beschleunigen nicht jedes Problem; bekannte Vorteile gelten für bestimmte Probleme und Voraussetzungen. Die praktische Leistung hängt von Algorithmus, Hardware, Rauschen und Fehlerkorrektur ab.

## Qubits und Messung

Ein reiner Qubit-Zustand lautet $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$, wobei $|\alpha|^2+|\beta|^2=1$ gilt. Eine Messung in der Rechenbasis liefert 0 oder 1 mit den Wahrscheinlichkeiten $|\alpha|^2$ und $|\beta|^2$. Der Zustandsvektor von n Qubits hat $2^n$ Amplituden. Das bedeutet jedoch weder, dass sich $2^n$ Antworten auf einmal auslesen lassen, noch dass jede Berechnung exponentiell schneller wird.

## Gatter und Verschränkung

Quantengatter sind unitäre Transformationen von Quantenzuständen. X vertauscht 0 und 1; H überführt einen Basiszustand in eine Superposition; CNOT invertiert das Ziel, wenn das Steuerbit 1 ist. H auf dem ersten Qubit und danach CNOT erzeugen den Bell-Zustand $(|00\rangle+|11\rangle)/\sqrt{2}$. Die Messergebnisse sind korreliert, doch Verschränkung kann keine Information schneller als Licht übertragen.

## Qiskit installieren und einen Bell-Schaltkreis erstellen

Das Qiskit-SDK erstellt und transformiert Schaltkreise. Seit Qiskit 1.0 wird Aer separat als `qiskit-aer` bereitgestellt. Das Beispiel nutzt einen idealen lokalen Simulator und bildet weder Hardware-Rauschen noch reale Hardware-Leistung ab.

"""+code+r"""

In der idealen Simulation treten nur `00` und `11` auf; mit mehr Messungen nähern sich die Häufigkeiten jeweils der Hälfte. Bei endlicher Stichprobe kann es Abweichungen geben. Hardware-Rauschen kann auch `01` oder `10` erzeugen. Beachten Sie beim Lesen der Bitreihenfolge die Konvention des klassischen Registers.

## Zur Beschleunigung von Algorithmen

Das Ergebnis einer Abfrage beim Deutsch-Jozsa-Algorithmus gilt im Abfragekomplexitätsmodell: Die Funktion muss als konstant oder ausgeglichen versprochen sein, und das Orakel gilt als ideal. Grover findet ein markiertes Element unter N unstrukturierten Kandidaten mit $O(\sqrt{N})$ idealen Orakelaufrufen. Das bedeutet nicht, dass jede Datenbankaufgabe proportional schneller wird.

## Quellen

"""+"\n".join(f'- [{n}]({u})' for n,u in refs)),
'pt':("Introdução à programação quântica com Qiskit","Conheça qubits, medição e emaranhamento e simule um estado de Bell com as versões atuais do Qiskit e AerSimulator.",r"""# Fundamentos da programação quântica

Computadores quânticos calculam manipulando estados regidos pela mecânica quântica. Eles não aceleram todos os problemas: as vantagens conhecidas valem para problemas e hipóteses específicos. O desempenho prático depende do algoritmo, do hardware, do ruído e da correção de erros.

## Qubits e medição

O estado puro de um qubit é $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$, com $|\alpha|^2+|\beta|^2=1$. Uma medição na base computacional retorna 0 ou 1 com probabilidades $|\alpha|^2$ e $|\beta|^2$. O vetor de estado de n qubits tem $2^n$ amplitudes, mas isso não permite ler $2^n$ respostas de uma só vez nem torna qualquer cálculo exponencialmente mais rápido.

## Portas e emaranhamento

Portas quânticas são transformações unitárias dos estados. X troca 0 e 1; H transforma um estado da base em superposição; CNOT inverte o alvo quando o controle é 1. Aplicar H ao primeiro qubit e depois CNOT produz o estado de Bell $(|00\rangle+|11\rangle)/\sqrt{2}$. As medições são correlacionadas, mas o emaranhamento não transmite informação mais rápido que a luz.

## Instalar Qiskit e criar um circuito de Bell

O SDK Qiskit cria e transforma circuitos. Desde o Qiskit 1.0, Aer é distribuído separadamente pelo pacote `qiskit-aer`. O exemplo usa um simulador local ideal e não reproduz o ruído nem o desempenho de hardware real.

"""+code+r"""

Na simulação ideal, só aparecem `00` e `11`; com mais medições, as contagens tendem a ficar próximas da metade para cada resultado. Uma amostra finita pode variar. O ruído do hardware também pode produzir `01` ou `10`. Confira a convenção do registrador clássico para interpretar a ordem dos bits.

## Sobre aceleração de algoritmos

O resultado de uma consulta do algoritmo Deutsch–Jozsa é uma afirmação de complexidade de consultas e pressupõe a promessa de que a função é constante ou balanceada e um oráculo ideal. Grover encontra um item marcado entre N candidatos não estruturados com $O(\sqrt{N})$ consultas ideais ao oráculo. Isso não significa que toda tarefa de banco de dados terá aceleração nessa proporção.

## Referências

"""+"\n".join(f'- [{n}]({u})' for n,u in refs)),
'ko':("Qiskit 양자 프로그래밍 입문","큐비트, 측정, 얽힘의 기초를 살펴보고 현재 Qiskit과 AerSimulator로 벨 상태를 시뮬레이션합니다.",r"""# 양자 프로그래밍 기초

양자 컴퓨터는 양자역학을 따르는 상태를 조작해 계산합니다. 모든 문제를 더 빠르게 푸는 것은 아니며, 알려진 속도 향상은 특정 문제와 가정에 한정됩니다. 실제 성능은 알고리즘, 하드웨어, 잡음, 오류 정정에 좌우됩니다.

## 큐비트와 측정

한 큐비트의 순수 상태는 $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$로 쓰며 $|\alpha|^2+|\beta|^2=1$입니다. 계산 기저에서 측정하면 0과 1이 각각 $|\alpha|^2$, $|\beta|^2$의 확률로 나옵니다. n큐비트 상태 벡터에는 $2^n$개의 진폭이 있지만, 그렇다고 $2^n$개의 답을 한 번에 읽거나 임의의 계산을 지수적으로 빠르게 할 수 있는 것은 아닙니다.

## 게이트와 얽힘

양자 게이트는 양자 상태에 작용하는 유니터리 변환입니다. X는 0과 1을 바꾸고, H는 기저 상태를 중첩으로 바꾸며, CNOT은 제어 비트가 1일 때 표적 비트를 뒤집습니다. 첫 번째 큐비트에 H를 적용한 다음 CNOT을 적용하면 벨 상태 $(|00\rangle+|11\rangle)/\sqrt{2}$가 됩니다. 측정 결과는 상관관계를 보이지만 얽힘으로 빛보다 빠르게 정보를 보낼 수는 없습니다.

## Qiskit 설치 및 벨 회로 작성

Qiskit SDK로 회로를 만들고 변환합니다. Qiskit 1.0부터 Aer 시뮬레이터는 별도 패키지인 `qiskit-aer`로 배포됩니다. 아래 예제는 로컬 이상 시뮬레이션이며 실제 하드웨어의 잡음이나 성능을 재현하지 않습니다.

"""+code+r"""

이상적인 시뮬레이션에서는 `00`과 `11`만 나오며, 측정 횟수가 늘수록 각 결과의 횟수는 대략 절반에 가까워집니다. 유한한 표본에서는 차이가 생길 수 있습니다. 실제 하드웨어 잡음은 `01`이나 `10`도 만들 수 있습니다. 비트 문자열 순서는 고전 레지스터 규약을 확인하세요.

## 알고리즘 속도 향상에 관해

Deutsch–Jozsa 알고리즘의 한 번 오라클 호출 결과는 함수가 상수 또는 균형 함수라는 약속과 이상적인 오라클을 가정한 쿼리 복잡도 결과입니다. Grover 검색은 구조 없는 N개 후보에서 표시된 항목을 이상적인 오라클 $O(\sqrt{N})$회 호출로 찾습니다. 모든 데이터베이스 작업이 그 비율만큼 빨라진다는 뜻은 아닙니다.

## 참고 자료

"""+"\n".join(f'- [{n}]({u})' for n,u in refs)),
'hi':("Qiskit के साथ क्वांटम प्रोग्रामिंग का परिचय","क्यूबिट, मापन और एंटैंगलमेंट की मूल बातें जानें और वर्तमान Qiskit तथा AerSimulator से Bell अवस्था का अनुकरण करें।",r"""# क्वांटम प्रोग्रामिंग की मूल बातें

क्वांटम कंप्यूटर क्वांटम यांत्रिकी के नियमों वाले अवस्थाओं को बदलकर गणना करते हैं। वे हर समस्या को तेज़ नहीं करते; ज्ञात लाभ खास समस्याओं और मान्यताओं पर निर्भर हैं। व्यावहारिक प्रदर्शन एल्गोरिदम, हार्डवेयर, शोर और त्रुटि-सुधार पर निर्भर करता है।

## क्यूबिट और मापन

एक क्यूबिट की शुद्ध अवस्था $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$ होती है, जहाँ $|\alpha|^2+|\beta|^2=1$। कम्प्यूटेशनल आधार में मापन से 0 या 1 मिलने की संभावनाएँ क्रमशः $|\alpha|^2$ और $|\beta|^2$ हैं। n क्यूबिट के अवस्था-वेक्टर में $2^n$ आयाम होते हैं, पर इससे $2^n$ उत्तर एक साथ पढ़े नहीं जा सकते और न ही हर गणना घातांकीय रूप से तेज़ होती है।

## गेट और एंटैंगलमेंट

क्वांटम गेट अवस्थाओं पर एकात्मक रूपांतरण हैं। X, 0 और 1 को बदलता है; H आधार-अवस्था को सुपरपोज़िशन में बदलता है; नियंत्रण बिट 1 होने पर CNOT लक्ष्य को पलटता है। पहले क्यूबिट पर H और फिर CNOT लगाने से Bell अवस्था $(|00\rangle+|11\rangle)/\sqrt{2}$ मिलती है। मापन परिणाम सहसंबद्ध होते हैं, लेकिन एंटैंगलमेंट से प्रकाश से तेज़ सूचना नहीं भेजी जा सकती।

## Qiskit स्थापित करें और Bell सर्किट बनाएँ

Qiskit SDK से सर्किट बनाए और रूपांतरित किए जाते हैं। Qiskit 1.0 से Aer अलग `qiskit-aer` पैकेज है। यह उदाहरण स्थानीय आदर्श सिम्युलेटर चलाता है; यह वास्तविक हार्डवेयर के शोर या प्रदर्शन को नहीं दर्शाता।

"""+code+r"""

आदर्श सिमुलेशन में केवल `00` और `11` आते हैं और शॉट बढ़ाने पर उनकी संख्या लगभग आधी-आधी होती है। सीमित नमूने में अंतर हो सकता है। हार्डवेयर शोर से `01` या `10` भी आ सकते हैं। बिट स्ट्रिंग का क्रम समझते समय क्लासिकल रजिस्टर के नियम देखें।

## एल्गोरिदम की गति के बारे में

Deutsch–Jozsa का एक ओरेकल-कॉल परिणाम क्वेरी जटिलता के संदर्भ में है: फ़ंक्शन के स्थिर या संतुलित होने की शर्त और आदर्श ओरेकल माना जाता है। Grover खोज बिना संरचना वाले N उम्मीदवारों में चिह्नित वस्तु को $O(\sqrt{N})$ आदर्श ओरेकल कॉल में ढूँढती है। इसका अर्थ यह नहीं कि हर डेटाबेस कार्य उसी अनुपात में तेज़ होगा।

## संदर्भ

"""+"\n".join(f'- [{n}]({u})' for n,u in refs)),
'id':("Pengantar Pemrograman Kuantum dengan Qiskit","Pelajari qubit, pengukuran, dan keterikatan, lalu simulasikan keadaan Bell dengan Qiskit dan AerSimulator versi terkini.",r"""# Dasar pemrograman kuantum

Komputer kuantum menghitung dengan memanipulasi keadaan yang mengikuti mekanika kuantum. Komputer ini tidak mempercepat semua masalah; percepatan yang diketahui berlaku pada masalah dan asumsi tertentu. Kinerja praktis bergantung pada algoritma, perangkat keras, derau, dan koreksi kesalahan.

## Qubit dan pengukuran

Keadaan murni satu qubit ditulis $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$, dengan $|\alpha|^2+|\beta|^2=1$. Pengukuran dalam basis komputasi menghasilkan 0 atau 1 dengan probabilitas $|\alpha|^2$ dan $|\beta|^2$. Vektor keadaan n qubit memiliki $2^n$ amplitudo, tetapi itu tidak berarti kita dapat membaca $2^n$ jawaban sekaligus atau membuat semua perhitungan jauh lebih cepat.

## Gerbang dan keterikatan

Gerbang kuantum adalah transformasi uniter pada keadaan kuantum. X menukar 0 dan 1; H mengubah keadaan basis menjadi superposisi; CNOT membalik target saat kontrol bernilai 1. Menerapkan H pada qubit pertama lalu CNOT menghasilkan keadaan Bell $(|00\rangle+|11\rangle)/\sqrt{2}$. Hasil pengukurannya berkorelasi, tetapi keterikatan tidak dapat mengirim informasi lebih cepat daripada cahaya.

## Memasang Qiskit dan membuat sirkuit Bell

SDK Qiskit digunakan untuk membuat dan mengubah sirkuit. Sejak Qiskit 1.0, Aer tersedia sebagai paket terpisah `qiskit-aer`. Contoh ini memakai simulator lokal ideal; ini tidak meniru derau atau kinerja perangkat keras nyata.

"""+code+r"""

Dalam simulasi ideal, hanya `00` dan `11` yang muncul; jumlahnya mendekati separuh masing-masing jika jumlah pengukuran ditambah. Sampel terbatas dapat berbeda. Derau perangkat keras juga dapat menghasilkan `01` atau `10`. Periksa konvensi register klasik saat membaca urutan bit.

## Tentang percepatan algoritma

Hasil satu pemanggilan oracle Deutsch–Jozsa adalah pernyataan kompleksitas kueri dengan janji bahwa fungsi bersifat konstan atau seimbang dan oracle dianggap ideal. Grover mencari item bertanda di antara N kandidat tak terstruktur dengan $O(\sqrt{N})$ pemanggilan oracle ideal. Ini tidak berarti semua tugas basis data menjadi lebih cepat dengan rasio tersebut.

## Referensi

"""+"\n".join(f'- [{n}]({u})' for n,u in refs)),
'ar':("مقدمة في البرمجة الكمومية باستخدام Qiskit","تعرّف إلى الكيوبتات والقياس والتشابك، ثم حاك حالة بيل باستخدام Qiskit وAerSimulator بالإصدارات الحالية.",r"""# أساسيات البرمجة الكمومية

تحسب الحواسيب الكمومية عبر معالجة حالات تخضع لميكانيكا الكم. وهي لا تسرّع كل المسائل؛ فالتسريعات المعروفة تخص مسائل وافتراضات محددة. ويتوقف الأداء العملي على الخوارزمية والعتاد والضوضاء وتصحيح الأخطاء.

## الكيوبتات والقياس

تكتب الحالة النقية لكيوبت واحد على الصورة $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$، حيث $|\alpha|^2+|\beta|^2=1$. يعطي القياس في الأساس الحاسوبي 0 أو 1 باحتمالين $|\alpha|^2$ و$|\beta|^2$. يحتوي متجه الحالة لـn كيوبتات على $2^n$ سعة، لكن هذا لا يعني إمكانية قراءة $2^n$ جواب دفعة واحدة أو تسريع أي حساب أُسّيًا.

## البوابات والتشابك

البوابات الكمومية تحويلات وحدوية للحالات. تبدّل X بين 0 و1؛ وتحول H حالة أساس إلى تراكب؛ وتقلب CNOT الهدف عندما تكون قيمة التحكم 1. يؤدي تطبيق H على الكيوبت الأول ثم CNOT إلى حالة بيل $(|00\rangle+|11\rangle)/\sqrt{2}$. تتسم نتائج القياس بالترابط، لكن التشابك لا يتيح إرسال معلومات أسرع من الضوء.

## تثبيت Qiskit وبناء دائرة بيل

تُستخدم حزمة Qiskit SDK لإنشاء الدوائر وتحويلها. ومنذ Qiskit 1.0، تتوفر Aer في حزمة منفصلة اسمها `qiskit-aer`. يستخدم المثال محاكيًا محليًا مثاليًا؛ ولا يحاكي ضوضاء العتاد الحقيقي أو أداءه.

"""+code+r"""

في المحاكاة المثالية لا تظهر إلا `00` و`11`، ويقترب عدد كل منهما من النصف عند زيادة عدد القياسات. وقد تختلف عينة محدودة. يمكن لضوضاء العتاد أن تنتج أيضًا `01` أو `10`. راجع اصطلاح السجل الكلاسيكي عند تفسير ترتيب البتات.

## حول تسريع الخوارزميات

نتيجة استدعاء واحد لخوارزمية Deutsch–Jozsa هي نتيجة في تعقيد الاستعلامات، وتفترض أن الدالة ثابتة أو متوازنة وأن الصندوق الأسود مثالي. تبحث خوارزمية Grover عن عنصر معلّم بين N مرشحًا غير منظّم باستخدام $O(\sqrt{N})$ استدعاءات مثالية للصندوق الأسود. ولا يعني ذلك تسريع كل مهام قواعد البيانات بهذه النسبة.

## مراجع

"""+"\n".join(f'- [{n}]({u})' for n,u in refs)),
'ru':("Введение в квантовое программирование с Qiskit","Изучите кубиты, измерение и запутанность, затем смоделируйте состояние Белла в актуальных Qiskit и AerSimulator.",r"""# Основы квантового программирования

Квантовые компьютеры выполняют вычисления, управляя состояниями, подчиняющимися квантовой механике. Они не ускоряют все задачи: известные преимущества относятся к определённым задачам и предположениям. Практическая производительность зависит от алгоритма, оборудования, шума и коррекции ошибок.

## Кубиты и измерение

Чистое состояние одного кубита записывается как $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$, где $|\alpha|^2+|\beta|^2=1$. Измерение в вычислительном базисе даёт 0 или 1 с вероятностями $|\alpha|^2$ и $|\beta|^2$. Вектор состояния n кубитов содержит $2^n$ амплитуд, но это не позволяет сразу прочитать $2^n$ ответов и не ускоряет произвольные вычисления экспоненциально.

## Гейты и запутанность

Квантовые гейты — унитарные преобразования состояний. X меняет 0 и 1 местами; H переводит базисное состояние в суперпозицию; CNOT меняет целевой кубит, если управляющий равен 1. Применение H к первому кубиту, а затем CNOT создаёт состояние Белла $(|00\rangle+|11\rangle)/\sqrt{2}$. Результаты измерений коррелированы, но запутанность не позволяет передавать информацию быстрее света.

## Установка Qiskit и создание схемы Белла

SDK Qiskit используют для создания и преобразования схем. Начиная с Qiskit 1.0, Aer распространяется отдельно в пакете `qiskit-aer`. Пример использует идеальный локальный симулятор и не воспроизводит шум или производительность реального оборудования.

"""+code+r"""

В идеальной симуляции появляются только `00` и `11`, а при увеличении числа измерений их частоты приближаются к половине. Конечная выборка может быть неравномерной. Шум оборудования может также приводить к `01` или `10`. При чтении порядка битов учитывайте соглашение классического регистра.

## Об ускорении алгоритмов

Результат одного вызова оракула в алгоритме Deutsch–Jozsa относится к сложности запросов и предполагает обещание, что функция постоянна или сбалансирована, а оракул идеален. Поиск Гровера находит помеченный элемент среди N неструктурированных вариантов за $O(\sqrt{N})$ идеальных вызовов оракула. Это не означает, что любая задача с базой данных ускоряется в такой пропорции.

## Источники

"""+"\n".join(f'- [{n}]({u})' for n,u in refs))}
langs=('ja','en','zh-cn','es','ko','pt','zh-tw','hi','fr','de','ar','ru','id')
for lang in langs:
 p=bundle/('index.md' if lang=='ja' else f'index.{lang}.md'); old=p.read_text(encoding='utf-8-sig')
 fm=re.match(r'(?s)^---\s*\n(.*?)\n---\s*\n',old)
 if not fm: raise ValueError(p)
 title,description,body=R[lang]
 front=fm.group(1)
 front=re.sub(r'(?m)^title:.*$', 'title: '+json.dumps(title,ensure_ascii=False),front)
 front=re.sub(r'(?m)^description:.*$', 'description: '+json.dumps(description,ensure_ascii=False),front)
 front=re.sub(r'(?m)^lastmod:.*\n?', '',front)
 front=front.rstrip()+f'\nlastmod: {today}\n'
 p.write_text('---\n'+front+'---\n'+body.strip()+'\n',encoding='utf-8')
source=bundle/'index.md'; norm=lambda p:hashlib.sha256(p.read_text(encoding='utf-8-sig').replace('\r\n','\n').encode()).hexdigest(); sh=norm(source)
checks={'meaning':('checked','Aligned the explanation of state amplitudes, measurement, gates, Bell-state correlations, and algorithm assumptions with the reviewed source and IBM references.'),'terminology':('checked','Checked qubit, computational basis, unitary gate, entanglement, Aer simulator, oracle, and query-complexity terms.'),'mathematics':('checked','Verified amplitude normalization and outcome probabilities; the Bell-state circuit and ideal counts; and the conditional query-complexity statements for Deutsch–Jozsa and Grover.'),'code':('checked','Updated to the Qiskit 1.x separate qiskit-aer package and AerSimulator API. Code was statically reviewed; Qiskit and qiskit-aer are not installed in this workspace, so it was not executed here.'),'links':('checked','Replaced archived qiskit.org links with current official IBM Quantum installation, local-simulator, migration, QuantumCircuit, and AerSimulator documentation.')}
reviews={}; source_rel=f'post/{bundle.name}/index.md'
for lang in langs[1:]:
 rel=f'post/{bundle.name}/index.{lang}.md'; p=root/'content'/rel
 reviews[rel]={'reviewKind':'ai','reviewedAt':today,'reviewer':'Codex (AI)','source':source_rel,'sourceHash':sh,'translationHash':norm(p),'summary':'Rewrote and aligned this translation with the corrected Qiskit and quantum-computing explanations.','checks':{k:{'status':v[0],'note':v[1]} for k,v in checks.items()},'limitations':['AI-assisted review; no human or native-speaker certification.','The sample targets current Qiskit 1.x APIs but was not executed because Qiskit packages are absent in this workspace.','Quantum algorithm speedups are stated only in the specified query/oracle model; no claim of general practical speedup is made.']}
evidence={'version':1,'batch':117,'article':'Qiskitを使った量子プログラミング超入門','reviewedAt':today,'sourceHash':sh,'sources':[u for n,u in refs],'scope':'Rewrote the Japanese article and twelve translations. Checked quantum-state mathematics, measurement, superposition versus readout, no-signalling in entanglement, current Qiskit packaging and AerSimulator code, ideal-simulation interpretation, query-complexity conditions, and official links.','findings':['Removed claims that n-qubit superposition itself gives general exponential parallel speedup; clarified that measurement does not expose all amplitudes.','Corrected entanglement explanation: Bell-state outcomes are correlated but cannot transmit information faster than light.','Qualified quantum-computing applications and Deutsch–Jozsa/Grover speedups by their problem and oracle assumptions.','Replaced outdated Qiskit/Aer references and code with Qiskit 1.x plus separately installed qiskit-aer and AerSimulator.','Distinguished ideal local simulation from noisy hardware results and documented sampling variation and bit-order caveat.'],'publicationPending':True,'reviews':reviews}
doc=root/'docs/translation-review';(doc/'batch-117.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
ledger_path=root/'data/translation_reviews.json';ledger=json.loads(ledger_path.read_text(encoding='utf-8'))
for rel,review in reviews.items():
 rec={k:review[k] for k in ('source','reviewedAt','reviewer','sourceHash','translationHash','reviewKind')};rec['evidence']='docs/translation-review/batch-117.json';rec['evidenceHash']=hashlib.sha256(json.dumps(review,ensure_ascii=False,sort_keys=True).encode()).hexdigest();ledger['reviews'][rel]=rec
ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# live verifier entry
v=doc/'verify_batches_087_092_live.py';s=v.read_text(encoding='utf-8');mark='    116: {\n';block='''    117: {
        "bundle": ROOT / "content/post/Qiskit入門",
        "slug": "qiskit-quantum-programming-intro",
        "links": [
            "https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit",
            "https://quantum.cloud.ibm.com/docs/en/guides/local-simulators",
            "https://quantum.cloud.ibm.com/docs/en/guides/qiskit-1.0-features",
            "https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.QuantumCircuit",
            "https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html",
        ],
        "markers": ["2^n", "|alpha|^2", "AerSimulator", "measure_all()", "O(\\\\sqrt{N})", "Deutsch"],
        "date": "2026-09-11",
    },
'''
if '    117: {' not in s:
 if mark not in s: raise ValueError('verifier insertion point not found')
 s=s.replace(mark,block+mark,1)
s=s.replace('114, 115, 116), default=116','114, 115, 116, 117), default=117')
v.write_text(s,encoding='utf-8')
print(json.dumps({'batch':117,'translations':len(reviews),'sourceHash':sh},ensure_ascii=False))
