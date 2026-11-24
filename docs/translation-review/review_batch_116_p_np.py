from pathlib import Path
import re, json, hashlib
root=Path.cwd(); bundle=root/'content/post/P≠NP予想'; today='2026-11-24'
refs={
'cmi':'[Clay Mathematics Institute: P vs NP](https://www.claymath.org/millennium/p-vs-np/)',
'pdf':'[Stephen Cook, official problem description (PDF)](https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf)',
'mit':'[MIT OpenCourseWare: NP-Completeness, Lecture 16 (PDF)](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/f2829e57caade7e7f21d765b8e7b9058_MIT6_046JS15_lec16.pdf)'}
texts={
'ja':("P≠NP予想：計算量理論の未解決問題", "クラスPとNP、証明書の長さ、SATの例を通して、PとNPが等しいかという未解決問題を説明します。", """# PとNPとは

**P**は、入力サイズの多項式時間で解ける決定問題のクラスです。**NP**は、Yesである入力について、入力サイズの多項式で抑えられる長さの証明書（解の候補）があれば、それを多項式時間で検証できる決定問題のクラスです。ここで「多項式」は入力サイズに対するものです。解ける問題は解を求めてから検証できるため、**P ⊆ NP**です。

## SATを例にする

SATは、与えられた論理式を真にする変数への割当てが存在するかを問う問題です。Yesの例では、その割当てを証明書として渡し、各節が満たされるかを式のサイズに対して多項式時間で確認できます。SAT（3-SATを含む）はNP完全です。したがってSATに多項式時間アルゴリズムが見つかれば **P = NP** が導かれます。NP完全とは、NPのどの問題も多項式時間でその問題へ帰着できることを指します。

## 未解決の問い

**P = NPか、それともP ≠ NPか**は未解決です。クレイ数学研究所はP対NP問題を未解決問題として掲載しています。P≠NPは広く研究される予想ですが、証明済みの定理として述べることはできません。この問題は、解を効率よく検証できるなら効率よく見つけられるのか、という問いです。

## 参考資料

- """+refs['cmi']+"\n- "+refs['pdf']+"\n- "+refs['mit']),
'en':("The P vs. NP Conjecture: An Open Problem in Complexity Theory", "An introduction to P, NP, polynomial-length certificates, SAT, and the open question of whether P equals NP.", """# What are P and NP?

**P** is the class of decision problems solvable in polynomial time in the input size. **NP** is the class of decision problems for which every yes-instance has a certificate (a proposed solution) whose length is bounded by a polynomial in the input size and whose validity can be checked in polynomial time. Because a solution to a problem in P can also be checked in polynomial time, **P ⊆ NP**.

## SAT as an example

SAT asks whether a given Boolean formula has an assignment that makes it true. For a yes-instance, the assignment is a certificate: checking that it satisfies every clause takes polynomial time in the formula size. SAT, including 3-SAT, is NP-complete. Therefore, a polynomial-time algorithm for SAT would imply **P = NP**. NP-completeness means that every problem in NP can be reduced to the problem in polynomial time.

## The open question

Whether **P = NP** or **P ≠ NP** remains open. The Clay Mathematics Institute lists P vs. NP as unsolved. P≠NP is a widely studied conjecture, not a proved theorem. Informally, the question asks whether every problem whose proposed solution can be checked efficiently can also be solved efficiently.

## References

- """+refs['cmi']+"\n- "+refs['pdf']+"\n- "+refs['mit']),
'zh-cn':("P与NP问题：计算复杂性理论中的未解问题", "通过多项式长度证书和SAT示例，介绍P、NP以及P是否等于NP这一未解问题。", """# 什么是P和NP？

**P**是指能在关于输入规模的多项式时间内求解的判定问题类。**NP**是指对于每个答案为“是”的实例，都存在一个长度受输入规模多项式界定的证书（候选解），并且可以在多项式时间内验证其正确性的判定问题类。P中的问题也能在多项式时间内验证，因此 **P ⊆ NP**。

## 以SAT为例

SAT询问给定布尔公式是否存在使公式为真的变量赋值。对于答案为“是”的实例，该赋值就是证书；检查它是否满足每个子句，只需关于公式长度的多项式时间。SAT（包括3-SAT）是NP完全问题。因此，如果SAT存在多项式时间算法，就能推出 **P = NP**。NP完全表示NP中的每个问题都能在多项式时间内归约到该问题。

## 尚未解决的问题

**P = NP还是P ≠ NP**仍未解决。克雷数学研究所将P与NP问题列为未解决问题。P≠NP是受到广泛研究的猜想，并非已经证明的定理。通俗地说，这个问题是在问：凡是能高效验证候选解的问题，是否也都能高效求解？

## 参考资料

- """+refs['cmi']+"\n- "+refs['pdf']+"\n- "+refs['mit']),
'zh-tw':("P 與 NP 問題：計算複雜度理論中的未解問題", "透過多項式長度證明憑證與 SAT 範例，介紹 P、NP，以及 P 是否等於 NP 這個未解問題。", """# 什麼是 P 與 NP？

**P** 是指可在相對於輸入大小的多項式時間內解決的判定問題類別。**NP** 是指對每個答案為「是」的輸入，都有一份長度受輸入大小多項式界定的證明憑證（候選解），且可在多項式時間內驗證其正確性的判定問題類別。P 中的問題也能在多項式時間內驗證，因此 **P ⊆ NP**。

## 以 SAT 為例

SAT 詢問給定布林公式是否存在能使公式為真的變數指派。對答案為「是」的輸入，該指派就是證明憑證；檢查它是否滿足每個子句，只需相對於公式大小的多項式時間。SAT（包括 3-SAT）是 NP 完全問題。因此，若 SAT 有多項式時間演算法，就能推出 **P = NP**。NP 完全表示 NP 中的每個問題都能在多項式時間內歸約至該問題。

## 尚未解決的問題

**P = NP 還是 P ≠ NP** 仍未解決。克雷數學研究所將 P 與 NP 問題列為未解問題。P≠NP 是廣受研究的猜想，並非已證明的定理。簡單來說，這是在問：凡是能有效率地驗證候選解的問題，是否也都能有效率地求解？

## 參考資料

- """+refs['cmi']+"\n- "+refs['pdf']+"\n- "+refs['mit']),
'es':("La conjetura P ≠ NP: un problema abierto de complejidad", "Introducción a P, NP, los certificados de longitud polinómica, SAT y la pregunta abierta de si P es igual a NP.", """# ¿Qué son P y NP?

**P** es la clase de problemas de decisión que pueden resolverse en tiempo polinómico respecto del tamaño de la entrada. **NP** es la clase de problemas de decisión para los que cada instancia con respuesta sí tiene un certificado (una solución propuesta) de longitud acotada por un polinomio del tamaño de la entrada, cuya validez puede comprobarse en tiempo polinómico. Todo problema de P también se puede verificar en tiempo polinómico, por lo que **P ⊆ NP**.

## SAT como ejemplo

SAT pregunta si una fórmula booleana dada tiene una asignación que la hace verdadera. Para una instancia afirmativa, la asignación es el certificado: comprobar que satisface cada cláusula requiere tiempo polinómico en el tamaño de la fórmula. SAT, incluido 3-SAT, es NP-completo. Por tanto, un algoritmo de tiempo polinómico para SAT implicaría **P = NP**. NP-completo significa que todo problema de NP se puede reducir a ese problema en tiempo polinómico.

## La pregunta abierta

Aún no se sabe si **P = NP** o **P ≠ NP**. El Clay Mathematics Institute clasifica P vs. NP como no resuelto. P≠NP es una conjetura ampliamente estudiada, no un teorema demostrado. En términos sencillos, se pregunta si todo problema cuya solución propuesta puede verificarse eficientemente también puede resolverse eficientemente.

## Referencias

- """+refs['cmi']+"\n- "+refs['pdf']+"\n- "+refs['mit']),
'fr':("La conjecture P ≠ NP : un problème ouvert en complexité", "Présentation de P, NP, des certificats de longueur polynomiale, de SAT et de la question ouverte P = NP ?", """# Que sont P et NP ?

**P** est la classe des problèmes de décision résolubles en temps polynomial par rapport à la taille de l’entrée. **NP** est la classe des problèmes de décision pour lesquels chaque instance de réponse oui possède un certificat (une solution proposée) dont la longueur est bornée par un polynôme de la taille de l’entrée et dont la validité peut être vérifiée en temps polynomial. Toute solution trouvée pour un problème de P peut aussi être vérifiée en temps polynomial ; ainsi **P ⊆ NP**.

## SAT comme exemple

SAT demande s’il existe une affectation rendant vraie une formule booléenne donnée. Pour une instance positive, cette affectation sert de certificat : vérifier qu’elle satisfait chaque clause prend un temps polynomial en la taille de la formule. SAT, y compris 3-SAT, est NP-complet. Un algorithme polynomial pour SAT impliquerait donc **P = NP**. NP-complet signifie que tout problème de NP se réduit à ce problème en temps polynomial.

## La question ouverte

On ne sait toujours pas si **P = NP** ou **P ≠ NP**. Le Clay Mathematics Institute classe P vs. NP parmi les problèmes non résolus. P≠NP est une conjecture largement étudiée, et non un théorème démontré. En termes simples, la question est de savoir si tout problème dont une solution proposée se vérifie efficacement peut aussi être résolu efficacement.

## Références

- """+refs['cmi']+"\n- "+refs['pdf']+"\n- "+refs['mit']),
'de':("Die P-NP-Frage: ein offenes Problem der Komplexitätstheorie", "Einführung in P, NP, polynomial lange Zertifikate, SAT und die offene Frage, ob P gleich NP ist.", """# Was sind P und NP?

**P** ist die Klasse der Entscheidungsprobleme, die in Polynomialzeit bezüglich der Eingabelänge lösbar sind. **NP** ist die Klasse der Entscheidungsprobleme, bei denen jede Ja-Instanz ein Zertifikat (einen Lösungsvorschlag) besitzt, dessen Länge durch ein Polynom der Eingabelänge beschränkt ist und das in Polynomialzeit überprüft werden kann. Eine Lösung für ein Problem in P lässt sich ebenfalls in Polynomialzeit prüfen; daher gilt **P ⊆ NP**.

## SAT als Beispiel

SAT fragt, ob es eine Variablenbelegung gibt, die eine gegebene boolesche Formel erfüllt. Bei einer Ja-Instanz ist diese Belegung das Zertifikat; die Prüfung aller Klauseln benötigt polynomielle Zeit in der Formellänge. SAT, einschließlich 3-SAT, ist NP-vollständig. Ein Polynomialzeitalgorithmus für SAT würde daher **P = NP** implizieren. NP-vollständig bedeutet, dass sich jedes Problem aus NP in Polynomialzeit auf dieses Problem reduzieren lässt.

## Die offene Frage

Ob **P = NP** oder **P ≠ NP** gilt, ist weiterhin offen. Das Clay Mathematics Institute führt P vs. NP als ungelöst. P≠NP ist eine viel untersuchte Vermutung, kein bewiesener Satz. Vereinfacht lautet die Frage: Kann jedes Problem, dessen Lösungsvorschlag effizient überprüfbar ist, auch effizient gelöst werden?

## Quellen

- """+refs['cmi']+"\n- "+refs['pdf']+"\n- "+refs['mit']),
'pt':("A conjectura P ≠ NP: um problema em aberto na complexidade", "Introdução a P, NP, certificados de tamanho polinomial, SAT e à questão ainda aberta de P ser ou não igual a NP.", """# O que são P e NP?

**P** é a classe de problemas de decisão resolvíveis em tempo polinomial em relação ao tamanho da entrada. **NP** é a classe de problemas de decisão em que cada instância cuja resposta é sim possui um certificado (uma solução proposta) de comprimento limitado por um polinômio do tamanho da entrada e verificável em tempo polinomial. Uma solução de um problema em P também pode ser verificada em tempo polinomial; portanto, **P ⊆ NP**.

## SAT como exemplo

SAT pergunta se uma fórmula booleana dada tem uma atribuição que a torna verdadeira. Para uma instância positiva, essa atribuição é o certificado: verificar se satisfaz cada cláusula leva tempo polinomial no tamanho da fórmula. SAT, inclusive 3-SAT, é NP-completo. Assim, um algoritmo polinomial para SAT implicaria **P = NP**. NP-completo significa que todo problema de NP pode ser reduzido a esse problema em tempo polinomial.

## A questão em aberto

Ainda não se sabe se **P = NP** ou **P ≠ NP**. O Clay Mathematics Institute classifica P vs. NP como não resolvido. P≠NP é uma conjectura amplamente estudada, não um teorema provado. Em termos simples, pergunta-se se todo problema cuja solução proposta pode ser verificada eficientemente também pode ser resolvido eficientemente.

## Referências

- """+refs['cmi']+"\n- "+refs['pdf']+"\n- "+refs['mit']),
'ko':("P 대 NP 추측: 계산 복잡도 이론의 미해결 문제", "다항식 길이 증명서와 SAT 예시를 통해 P, NP와 P=NP 여부라는 미해결 문제를 설명합니다.", """# P와 NP란?

**P**는 입력 크기에 대한 다항 시간 안에 풀 수 있는 결정 문제의 집합입니다. **NP**는 답이 ‘예’인 각 입력에 대해 입력 크기의 다항식으로 길이가 제한되는 증명서(제안된 해)가 있고, 이를 다항 시간 안에 검증할 수 있는 결정 문제의 집합입니다. P의 해도 다항 시간에 검증할 수 있으므로 **P ⊆ NP**입니다.

## SAT 예시

SAT는 주어진 불리언 식을 참으로 만드는 변수 할당이 존재하는지 묻습니다. ‘예’인 입력에서는 그 할당이 증명서이며, 모든 절을 만족하는지 식의 크기에 대한 다항 시간에 확인할 수 있습니다. 3-SAT를 포함한 SAT는 NP-완전입니다. 따라서 SAT를 다항 시간에 푸는 알고리즘이 있다면 **P = NP**가 됩니다. NP-완전이란 NP의 모든 문제가 다항 시간 환원을 통해 해당 문제로 변환될 수 있다는 뜻입니다.

## 미해결 질문

**P = NP인지 P ≠ NP인지**는 아직 밝혀지지 않았습니다. 클레이 수학연구소는 P 대 NP를 미해결 문제로 분류합니다. P≠NP는 널리 연구되는 추측이지 증명된 정리는 아닙니다. 쉽게 말해, 제안된 해를 효율적으로 검증할 수 있는 모든 문제를 효율적으로 풀 수도 있는지를 묻는 문제입니다.

## 참고 자료

- """+refs['cmi']+"\n- "+refs['pdf']+"\n- "+refs['mit']),
'hi':("P बनाम NP अनुमान: संगणना जटिलता का एक अनसुलझा प्रश्न", "बहुपद लंबाई वाले प्रमाणपत्र और SAT उदाहरण के माध्यम से P, NP और P=NP के खुले प्रश्न का परिचय।", """# P और NP क्या हैं?

**P** उन निर्णय समस्याओं का वर्ग है जिन्हें इनपुट के आकार के बहुपद समय में हल किया जा सकता है। **NP** उन निर्णय समस्याओं का वर्ग है जिनके प्रत्येक ‘हाँ’ उदाहरण के लिए एक प्रमाणपत्र (प्रस्तावित हल) होता है, जिसकी लंबाई इनपुट आकार के बहुपद से सीमित होती है और जिसकी वैधता बहुपद समय में जाँची जा सकती है। P की समस्या का हल भी बहुपद समय में जाँचा जा सकता है, इसलिए **P ⊆ NP**।

## SAT का उदाहरण

SAT पूछता है कि क्या दिए गए बूलियन सूत्र को सत्य करने वाला चर-आवंटन मौजूद है। ‘हाँ’ उदाहरण में वह आवंटन प्रमाणपत्र है; प्रत्येक क्लॉज संतुष्ट है या नहीं, यह सूत्र के आकार के बहुपद समय में जाँचा जा सकता है। 3-SAT सहित SAT, NP-पूर्ण है। इसलिए SAT के लिए बहुपद-समय एल्गोरिदम से **P = NP** निष्कर्ष निकलेगा। NP-पूर्ण का अर्थ है कि NP की हर समस्या को बहुपद समय में इस समस्या में घटाया जा सकता है।

## खुला प्रश्न

**P = NP है या P ≠ NP**, यह अब भी अनसुलझा है। क्ले मैथमेटिक्स इंस्टीट्यूट P बनाम NP को अनसुलझी समस्या मानता है। P≠NP व्यापक रूप से अध्ययन किया गया अनुमान है, सिद्ध प्रमेय नहीं। सरल शब्दों में प्रश्न यह है कि क्या जिस समस्या के प्रस्तावित हल को कुशलता से जाँचा जा सकता है, उसे कुशलता से हल भी किया जा सकता है।

## संदर्भ

- """+refs['cmi']+"\n- "+refs['pdf']+"\n- "+refs['mit']),
'id':("Konjektur P ≠ NP: masalah terbuka dalam teori kompleksitas", "Pengantar P, NP, sertifikat berpanjang polinomial, SAT, dan pertanyaan terbuka apakah P sama dengan NP.", """# Apa itu P dan NP?

**P** adalah kelas masalah keputusan yang dapat diselesaikan dalam waktu polinomial terhadap ukuran masukan. **NP** adalah kelas masalah keputusan yang setiap instans berjawaban ya memiliki sertifikat (calon solusi) dengan panjang yang dibatasi polinomial terhadap ukuran masukan dan dapat diverifikasi dalam waktu polinomial. Solusi masalah di P juga dapat diverifikasi dalam waktu polinomial, sehingga **P ⊆ NP**.

## SAT sebagai contoh

SAT menanyakan apakah rumus Boolean yang diberikan memiliki penetapan variabel yang membuatnya benar. Untuk instans berjawaban ya, penetapan tersebut menjadi sertifikat; memeriksa semua klausa membutuhkan waktu polinomial terhadap ukuran rumus. SAT, termasuk 3-SAT, adalah NP-lengkap. Karena itu, algoritma waktu polinomial untuk SAT akan menyiratkan **P = NP**. NP-lengkap berarti setiap masalah di NP dapat direduksi ke masalah tersebut dalam waktu polinomial.

## Pertanyaan terbuka

Belum diketahui apakah **P = NP** atau **P ≠ NP**. Clay Mathematics Institute mencantumkan P vs. NP sebagai masalah yang belum terselesaikan. P≠NP adalah dugaan yang banyak diteliti, bukan teorema yang telah dibuktikan. Secara sederhana, pertanyaannya adalah apakah setiap masalah yang calon solusinya dapat diperiksa secara efisien juga dapat diselesaikan secara efisien.

## Referensi

- """+refs['cmi']+"\n- "+refs['pdf']+"\n- "+refs['mit']),
'ar':("حدسية P ≠ NP: مسألة مفتوحة في نظرية التعقيد", "مقدمة إلى الفئتين P وNP، والشهادات ذات الطول متعدد الحدود، ومثال SAT، والسؤال المفتوح حول تساوي P وNP.", """# ما الفئتان P وNP؟

**P** هي فئة مسائل القرار التي يمكن حلها بزمن متعدد الحدود بالنسبة إلى حجم الإدخال. أما **NP** فهي فئة مسائل القرار التي يكون لكل حالة جوابها «نعم» شهادةٌ (حل مقترح) طولها محدود بمتعدد حدود في حجم الإدخال، ويمكن التحقق من صحتها بزمن متعدد الحدود. ويمكن أيضًا التحقق من حل أي مسألة في P بهذا الزمن، لذلك **P ⊆ NP**.

## مثال SAT

يسأل SAT عما إذا كان هناك إسناد للمتغيرات يجعل صيغة منطقية معطاة صحيحة. في حالة جوابها «نعم»، يكون ذلك الإسناد شهادة؛ ويمكن التحقق من استيفائه لكل بند بزمن متعدد الحدود في حجم الصيغة. ومسألة SAT، بما فيها 3-SAT، كاملة بالنسبة إلى NP. لذلك فإن وجود خوارزمية متعددة الحدود لـSAT يستلزم **P = NP**. وتعني NP-الكاملة أن كل مسألة في NP يمكن اختزالها إلى هذه المسألة بزمن متعدد الحدود.

## السؤال المفتوح

لا يزال غير معروف هل **P = NP** أم **P ≠ NP**. ويصنف معهد كلاي للرياضيات مسألة P مقابل NP على أنها غير محلولة. وP≠NP حدسية تُدرس على نطاق واسع، وليست مبرهنة مثبتة. وببساطة، تسأل المسألة عما إذا كان كل ما يمكن التحقق بكفاءة من حل مقترح له يمكن أيضًا حله بكفاءة.

## مراجع

- """+refs['cmi']+"\n- "+refs['pdf']+"\n- "+refs['mit']),
'ru':("Гипотеза P ≠ NP: открытая задача теории сложности", "Введение в классы P и NP, сертификаты полиномиальной длины, пример SAT и открытый вопрос о равенстве P и NP.", """# Что такое P и NP?

**P** — класс задач принятия решений, решаемых за полиномиальное время относительно размера входа. **NP** — класс задач принятия решений, для каждого экземпляра со ответом «да» которого существует сертификат (предлагаемое решение) длины, ограниченной полиномом от размера входа, и его можно проверить за полиномиальное время. Решение задачи из P также можно проверить за полиномиальное время, поэтому **P ⊆ NP**.

## Пример SAT

SAT спрашивает, существует ли присваивание переменных, делающее заданную булеву формулу истинной. Для экземпляра с ответом «да» такое присваивание служит сертификатом: проверка всех клауз занимает полиномиальное время от размера формулы. SAT, включая 3-SAT, является NP-полной задачей. Следовательно, полиномиальный алгоритм для SAT означал бы **P = NP**. NP-полнота означает, что любую задачу из NP можно свести к этой задаче за полиномиальное время.

## Открытый вопрос

Пока неизвестно, верно ли **P = NP** или **P ≠ NP**. Математический институт Клэя относит проблему P против NP к нерешённым. P≠NP — широко изучаемая гипотеза, а не доказанная теорема. Проще говоря, вопрос в том, можно ли эффективно решить любую задачу, для которой предложенное решение можно эффективно проверить.

## Источники

- """+refs['cmi']+"\n- "+refs['pdf']+"\n- "+refs['mit'])}
texts['id']=("Konjektur P ≠ NP: masalah terbuka dalam teori kompleksitas", "Pengantar kelas P dan NP, sertifikat berpanjang polinomial, contoh SAT, dan pertanyaan terbuka apakah P sama dengan NP.", "\n".join([
"# Apa itu P dan NP?",
"",
"**P** adalah kelas masalah keputusan yang dapat diselesaikan dalam waktu polinomial terhadap ukuran masukan. **NP** adalah kelas masalah keputusan yang setiap instans dengan jawaban ya memiliki sertifikat (calon solusi) dengan panjang yang dibatasi polinomial terhadap ukuran masukan dan dapat diverifikasi dalam waktu polinomial. Solusi masalah di P juga dapat diverifikasi dalam waktu polinomial, sehingga **P ⊆ NP**.",
"",
"## SAT sebagai contoh",
"",
"SAT menanyakan apakah rumus Boolean yang diberikan memiliki penetapan variabel yang membuatnya benar. Untuk instans dengan jawaban ya, penetapan tersebut menjadi sertifikat; memeriksa semua klausa membutuhkan waktu polinomial terhadap ukuran rumus. SAT, termasuk 3-SAT, adalah NP-lengkap. Karena itu, algoritma waktu polinomial untuk SAT akan menyiratkan **P = NP**. NP-lengkap berarti setiap masalah di NP dapat direduksi ke masalah tersebut dalam waktu polinomial.",
"",
"## Pertanyaan terbuka",
"",
"Belum diketahui apakah **P = NP** atau **P ≠ NP**. Clay Mathematics Institute mencantumkan P vs. NP sebagai masalah yang belum terselesaikan. P≠NP adalah dugaan yang banyak diteliti, bukan teorema yang telah dibuktikan. Secara sederhana, pertanyaannya adalah apakah setiap masalah yang calon solusinya dapat diperiksa secara efisien juga dapat diselesaikan secara efisien.",
"",
"## Referensi",
"",
"- "+refs['cmi'],"- "+refs['pdf'],"- "+refs['mit']]))
langs=('en','zh-cn','es','ko','pt','zh-tw','hi','fr','de','ar','ru','id')
source_rel='post/P≠NP予想/index.md'; source_path=root/'content'/source_rel
# date corrected; retain original publication date, add an explicit review/update date
for lang,(title,desc,body) in texts.items():
 p=bundle/('index.md' if lang=='ja' else f'index.{lang}.md')
 original=p.read_text(encoding='utf-8-sig')
 fm=re.match(r'(?s)^---\s*\n(.*?)\n---\s*\n',original)
 if not fm: raise ValueError(f'front matter missing: {p}')
 front=fm.group(1)
 front=re.sub(r'(?m)^title:.*$', 'title: '+json.dumps(title,ensure_ascii=False),front)
 front=re.sub(r'(?m)^description:.*$', 'description: '+json.dumps(desc,ensure_ascii=False),front)
 front=re.sub(r'(?m)^date:.*\n?', '', front)
 front=re.sub(r'(?m)^lastmod:.*\n?', '', front)
 front=front.rstrip()+f'\ndate: 2024-09-11T02:22:39+09:00\nlastmod: {today}\n'
 p.write_text('---\n'+front+'---\n'+body.strip()+'\n',encoding='utf-8')
source_hash=hashlib.sha256(source_path.read_text(encoding='utf-8-sig').replace('\r\n','\n').encode('utf-8')).hexdigest()
records={}; allchecks={
'meaning':('checked','Compared the definitions, implication P subset NP, SAT certificate example, NP-completeness consequence, and unresolved status against the Japanese source and primary references.'),
'terminology':('checked','Checked consistent use of decision problem, polynomial time, certificate/witness, SAT, reduction, and NP-complete.'),
'mathematics':('checked','Confirmed certificate length is polynomial in input size, P subset NP, polynomial-time SAT implies P=NP, and no separation is claimed as proved.'),
'code':('not_applicable','The article contains no program code or executable algorithm.'),
'links':('checked','Added and checked the Clay Mathematics Institute problem page and official problem description plus MIT OpenCourseWare lecture notes.')}
for lang in langs:
 rel=f'post/{bundle.name}/index'+('' if lang=='ja' else f'.{lang}')+'.md'; p=root/'content'/rel
 records[rel]={'reviewKind':'ai','reviewedAt':today,'reviewer':'Codex (AI)','source':source_rel,'sourceHash':source_hash,'translationHash':hashlib.sha256(p.read_text(encoding='utf-8-sig').replace('\r\n','\n').encode('utf-8')).hexdigest(),'summary':'Revised and aligned the article/translation using CMI and MIT primary educational references; corrected the missing polynomial certificate-length bound.','checks':{k:{'status':v[0],'note':v[1]} for k,v in allchecks.items()},'limitations':['AI-assisted review; no human or native-speaker language certification.','This is an introductory overview, not a proof of P≠NP or a formal complexity-theory textbook.']}
entry={'version':1,'batch':116,'article':'P≠NP予想','reviewedAt':today,'sourceHash':source_hash,'sources':list(refs.values()),'scope':'Reviewed the Japanese article and all twelve translations for meaning, terminology, mathematical definitions and implications, code applicability, and links. Added an input-size polynomial bound on certificate length, a SAT/NP-completeness example, and the current unresolved status; removed an unsourced claim about what many researchers believe.','findings':['Removed the duplicate future date and restored the original publication date, with lastmod set to the review date.','Defined NP with a certificate whose length is polynomially bounded by input size; explained why P is a subset of NP.','Added SAT as an NP-complete example and the conditional implication that polynomial-time SAT yields P=NP.','Stated that P vs. NP remains unsolved and did not present P≠NP as a proven result.','Added primary Clay Institute sources and MIT OpenCourseWare notes in all locales.'],'publicationPending':True,'reviews':records}
doc=root/'docs/translation-review'; doc.mkdir(exist_ok=True)
(doc/'batch-116.json').write_text(json.dumps(entry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
ledger_path=root/'data/translation_reviews.json'; ledger=json.loads(ledger_path.read_text(encoding='utf-8'))
for rel,review in records.items():
 rec={k:review[k] for k in ('source','reviewedAt','reviewer','sourceHash','translationHash','reviewKind')}; rec['evidence']='docs/translation-review/batch-116.json'; rec['evidenceHash']=hashlib.sha256(json.dumps(review,ensure_ascii=False,sort_keys=True).encode()).hexdigest(); ledger['reviews'][rel]=rec
ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
verifier=doc/'verify_batches_087_092_live.py'; s=verifier.read_text(encoding='utf-8')
marker='    115: {\n'
block='''    116: {\n        "bundle": ROOT / "content/post/P≠NP予想",\n        "slug": "P≠NP予想",\n        "links": [\n            "https://www.claymath.org/millennium/p-vs-np/",\n            "https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf",\n            "https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/f2829e57caade7e7f21d765b8e7b9058_MIT6_046JS15_lec16.pdf",\n        ],\n        "markers": ["NP-complete", "P = NP", "P ⊆ NP", "certificate", "2024-09-11"],\n        "date": "2024-09-11",\n    },\n'''
if '    116: {' not in s:
 if marker not in s: raise ValueError('verifier insertion point missing')
 s=s.replace(marker,block+marker,1)
s=s.replace('106, 107, 108, 109, 110, 111, 112, 113, 114, 115), default=115','106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116), default=116')
verifier.write_text(s,encoding='utf-8')
print(json.dumps({'batch':116,'locales':len(records),'sourceHash':source_hash},ensure_ascii=False))
