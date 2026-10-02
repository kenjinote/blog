---
title: "O Teorema das Quatro Cores e a Revolução na Matemática Computacional: O Enigma de 100 Anos e a Filosofia da Prova por Máquina"
description: "A história da matemática em torno do problema de coloração de mapas planos. Da falsa prova de Kempe à primeira prova por computador da história por Appel & Haken, até a redefinição da 'beleza' matemática."
slug: "four-color-theorem-computer-assisted-proof"
date: "2026-10-03T05:00:00+09:00"
categories: ["mathematics", "computer-science"]
tags: ["graph-theory", "combinatorics", "formal-proof", "mathematics-history"]
image: "eyecatch.jpg"
---

Na história da matemática, um dos teoremas mais famosos e, ao mesmo tempo, mais controversos é o "Teorema das Quatro Cores (Four Color Theorem)". É uma afirmação tão simples que até uma criança no ensino fundamental pode entender: "Para colorir qualquer mapa plano de modo que regiões adjacentes tenham cores diferentes, quatro cores são suficientes". No entanto, a sua prova exigiu mais de um século e uma mudança de paradigma chamada "prova auxiliada por computador", que abalou os fundamentos da matemática como disciplina.

Neste artigo, desvendaremos exaustivamente o Teorema das Quatro Cores a partir de perspectivas matemáticas, históricas e filosóficas, começando com a pergunta ingênua em 1852, passando pelos desafios e fracassos de gênios, até chegar ao ápice da matemática moderna, que aliou-se a uma nova inteligência chamada computador. Em particular, aprofundaremos tópicos matemáticos complexos: a falsa prova de Kempe e a estrutura geométrica do contraexemplo de Heawood, a prova completa do Teorema das Cinco Cores, a matemática do método de descarga, o algoritmo de Appel e Haken, os detalhes da prova formal por Coq e a relação com a completude NP.

## Capítulo 1: 1852, a Pergunta Ingênua de Francis Guthrie e a Elevação à Teoria dos Grafos

### A Proposição do Problema de Coloração de Mapas
A história começa em 1852 com Francis Guthrie, um jovem que havia acabado de se formar na University College London, na Inglaterra. Ao colorir um mapa dos condados ingleses, ele notou um fato curioso: "Por mais complexo que seja um mapa, quatro cores não seriam suficientes para colori-lo de forma que condados adjacentes tenham cores diferentes?"

Francis compartilhou essa dúvida com seu irmão mais novo, Frederick Guthrie, que na época estudava matemática na University College. Frederick apresentou o problema ao seu orientador, Augustus De Morgan, um dos matemáticos mais importantes da época. De Morgan foi imediatamente cativado pelo problema e o compartilhou em uma carta com seu amigo William Rowan Hamilton e outros. Esse foi o momento em que nasceu o brilhante "Problema das Quatro Cores" na história da matemática.

### O Teorema Poliedral de Euler e a Dualidade de Grafos Planos
Para tratar o problema de coloração de mapas com rigor matemático, é essencial formulá-lo na teoria dos grafos. Se tratarmos cada região (país ou estado) no mapa como um "Vértice (Vertex)" e conectarmos regiões adjacentes com uma "Aresta (Edge)", obteremos um "Grafo Plano (Planar Graph)" onde as arestas não se cruzam no plano. Essa conversão é conhecida como a operação de tomar um "Grafo Dual (Dual Graph)". As fronteiras originais do mapa correspondem às arestas do grafo e as faces correspondem aos vértices.

O problema das quatro cores se reduz ao Problema de Coloração de Vértices (Vertex Coloring Problem) em grafos: "É possível colorir os vértices de qualquer grafo plano com 4 cores de modo que vértices adjacentes tenham cores diferentes?"

Aqui, o Teorema Poliedral descoberto por Leonhard Euler desempenha um papel crucial. Em um grafo plano conexo, se o número de vértices for $V$, o número de arestas for $E$ e o número de faces for $F$, a seguinte relação invariante se mantém:

$$V - E + F = 2$$

Ao combinar este teorema com as propriedades fundamentais dos grafos planos, podemos derivar restrições poderosas sobre a estrutura dos grafos planos. Assumiremos que o grafo é um grafo simples sem arestas múltiplas ou auto-loops e, em seguida, consideraremos um "Grafo Plano Maximal (Maximal Planar Graph)" onde todas as faces são triângulos. Qualquer grafo plano pode se tornar um grafo plano maximal pela adição de arestas sem aumentar o número cromático, portanto, é suficiente provar o teorema das quatro cores para grafos planos maximais.

Em um grafo plano maximal, cada face é cercada por exatamente 3 arestas. Como uma aresta limita exatamente 2 faces, a seguinte relação vale estritamente entre o número de faces e o número de arestas:

$$3F = 2E$$

Substituímos isso na fórmula de Euler para eliminar $F$. Substituindo $F = \frac{2}{3}E$ em $V - E + F = 2$, temos:

$$V - E + \frac{2}{3}E = 2 \implies V - \frac{1}{3}E = 2 \implies 3V - E = 6 \implies E = 3V - 6$$

Em um grafo plano simples geral, as faces são cercadas por 3 ou mais arestas, logo $3F \leq 2E$, levando à seguinte desigualdade:

$$E \leq 3V - 6$$

Essa desigualdade mostra que existe um limite superior estrito para a densidade de arestas em um grafo plano. A partir daqui, vamos considerar o grau (Degree, $\deg(v)$) de cada vértice. A soma dos graus de todos os vértices do grafo é exatamente o dobro do número de arestas (Lema do Aperto de Mãos).

$$\sum_{v \in V} \deg(v) = 2E$$

Usando a desigualdade anterior $2E \leq 6V - 12$:

$$\sum_{v \in V} \deg(v) \leq 6V - 12$$

Dividindo ambos os lados pelo número de vértices $V$, obtemos o grau médio dos vértices:

$$\frac{1}{V} \sum_{v \in V} \deg(v) \leq 6 - \frac{12}{V} < 6$$

O fato de que o grau médio é estritamente menor que 6 prova matemática e completamente que "pelo menos um vértice deve ter grau 5 ou menos". Ou seja, em qualquer grafo plano simples, existe pelo menos um vértice que tem grau 1, 2, 3, 4 ou 5. Esse fato é o ponto de partida mais fundamental para o conceito de "configuração inevitável" descrito posteriormente e é a chave absoluta para provar o Teorema das Quatro Cores.

## Capítulo 2: A "Prova" de Alfred Kempe e seu Colapso 11 Anos Depois

### O Conceito das Cadeias de Kempe e a "Prova" Elegante
Em 1879, o advogado e matemático britânico Alfred Bray Kempe finalmente publicou uma "prova" do Problema das Quatro Cores nas revistas *Nature* e *American Journal of Mathematics*. Sua prova era extremamente original e foi aceita como correta pela comunidade matemática mundial por 11 anos.

O núcleo da prova de Kempe era uma ideia revolucionária, agora chamada de "Cadeia de Kempe (Kempe Chain)". Ele usou indução matemática. Assumiu que o teorema das quatro cores era verdadeiro para todos os grafos planos com $k$ vértices e tentou mostrar que também se manteria para um grafo com $k+1$ vértices.

A partir do teorema de Euler mencionado, um grafo plano $G$ com $k+1$ vértices sempre contém um vértice $v$ de grau 5 ou menos. Considere o grafo $G'$ obtido removendo o vértice $v$ e suas arestas conectadas de $G$. Como $G'$ tem $k$ vértices, pela hipótese de indução ele pode ser colorido com 4 cores (vamos chamá-las de vermelho, azul, verde e amarelo). Em seguida, tentamos recolocar $v$ e colori-lo.

1. **Se o grau de $v$ for 3 ou menos:** O número máximo de vértices adjacentes a $v$ é 3. Portanto, das 4 cores, pelo menos uma não é usada pelos vértices adjacentes. Basta pintar $v$ com a cor não usada e a prova está completa.
2. **Se o grau de $v$ for 4:** Suponha que os 4 vértices adjacentes a $v$ (digamos $v_1, v_2, v_3, v_4$ no sentido horário) sejam todos pintados de cores diferentes (vermelho, azul, verde e amarelo). Agora, considere o subgrafo extraído de todo o grafo contendo apenas os vértices "vermelhos" e "verdes" e as arestas que os conectam. Se $v_1$ (vermelho) e $v_3$ (verde) não estiverem conectados dentro deste subgrafo vermelho-verde (ou seja, não houver caminho de $v_1$ a $v_3$ através de vértices vermelhos e verdes), podemos inverter as cores do componente conexo contendo $v_1$ (vermelho para verde e verde para vermelho). Isso é chamado de "inversão da Cadeia de Kempe". Após a inversão, $v_1$ se torna verde, e as cores ao redor de $v$ se reduzem a três: azul, verde, verde e amarelo. Isso torna possível pintar $v$ de vermelho. Se $v_1$ e $v_3$ estiverem conectados, pelas propriedades topológicas dos grafos planos (Teorema da Curva de Jordan), o caminho vermelho-verde conectando $v_1$ e $v_3$ separa $v_2$ (azul) e $v_4$ (amarelo). Portanto, $v_2$ e $v_4$ não podem de forma alguma se conectar através de uma cadeia azul-amarela de Kempe, e o componente azul-amarelo contendo $v_2$ pode ser invertido. Em qualquer caso, podemos reduzir o número de cores ao redor de $v$ para 3, o que nos permite colorir $v$.
3. **Se o grau de $v$ for 5:** Considere o caso em que os 5 vértices adjacentes a $v$, $v_1, v_2, v_3, v_4, v_5$, são pintados respectivamente de vermelho, azul, verde, amarelo e vermelho (como são 5, uma cor se repete). Kempe estendeu o raciocínio para o grau 4 e argumentou que, ao combinar habilmente a inversão de duas cadeias de Kempe diferentes (por exemplo, uma cadeia vermelho-verde e uma cadeia vermelho-amarela), o número de cores ao redor de $v$ pode sempre ser reduzido para 3 ou menos. O seu método aplicava duplamente a lógica de que se uma cadeia está conectada, a outra está separada.

A prova parecia intuitiva, elegante e sem falhas lógicas. Os matemáticos da época acreditaram, sem dúvidas, que o problema das quatro cores havia sido completamente resolvido.

### O Grafo de Contraexemplo de Heawood: A Falha Fatal do "Cruzamento da Dupla Cadeia de Kempe"
No entanto, em 1890, um matemático de 29 anos chamado Percy John Heawood leu minuciosamente o artigo de Kempe e descobriu um salto lógico fatal no argumento envolvendo o vértice de grau 5.

Kempe assumiu implicitamente que, ao realizar as inversões de duas cadeias de Kempe (por exemplo, uma azul-verde e uma azul-amarela) separadamente, elas poderiam ser invertidas de maneira mutuamente independente. No entanto, Heawood provou rigorosamente e geometricamente que, se essas duas cadeias compartilham alguns vértices, a inversão da primeira cadeia altera o estado de coloração do grafo, mudando a conectividade da segunda cadeia.

Heawood construiu um grafo de contraexemplo específico (conhecido hoje como o "Grafo de Heawood" ou seus derivados, um grafo plano maximal composto por 25 vértices). Ele mostrou que neste grafo, ao aplicar o algoritmo de Kempe para reduzir as cores ao redor de um vértice $v$ de grau 5, assim que a cadeia azul-verde é invertida, a cadeia azul-amarela, que originalmente não estava conectada, passa a se conectar; em seguida, ao inverter a cadeia azul-amarela, o vértice verde recém-invertido volta à sua cor original, resultando em um loop em que o número de cores não diminui.

A "troca simultânea de duplas cadeias de Kempe" de Kempe foi uma falácia decorrente de subestimar os complexos entrelaçamentos dos grafos planos, nos quais relações locais de separação topológica não podem ser mantidas globalmente. Com essa descoberta, a prova de Kempe do Teorema das Quatro Cores desmoronou completamente.

### A Prova Matemática Completa do Teorema das Cinco Cores
A prova de Kempe havia desmoronado, mas Heawood não apenas a destruiu. Ele reconheceu que a própria ideia de Kempe (as Cadeias de Kempe) era extremamente útil e usou-a para provar rigorosamente o "Teorema das Cinco Cores (Five Color Theorem)", que afirma que "todo grafo plano pode sempre ser colorido com 5 cores". O processo completo de prova do Teorema das Cinco Cores é o seguinte:

**Teorema:** Qualquer grafo plano $G$ pode ter seus vértices coloridos com 5 cores.
**Prova:** Usamos indução matemática no número de vértices $n$.
Para $n \leq 5$, o caso é trivial. Assuma que todo grafo plano com $n=k$ pode ser colorido com 5 cores, e considere um grafo plano $G$ com $n=k+1$.
Pelos fatos derivados da fórmula de Euler, em $G$ sempre existe um vértice $v$ de grau 5 ou menos.
Como o grafo $G' = G - \{v\}$ obtido pela remoção de $v$ de $G$ tem $k$ vértices, pela hipótese de indução ele pode ser colorido com 5 cores (Cor 1, Cor 2, Cor 3, Cor 4, Cor 5).
Considere devolver o vértice $v$ mantendo a coloração de $G'$.
- **Caso 1: $\deg(v) < 5$.** Como os vértices adjacentes a $v$ são no máximo 4, pelo menos 1 das 5 cores não é usada nos vértices adjacentes. Pinte $v$ com essa cor.
- **Caso 2: $\deg(v) = 5$.** Suponha que os 5 vértices adjacentes a $v$, $v_1, v_2, v_3, v_4, v_5$ (dispostos no sentido horário), sejam todos pintados de cores diferentes (Cor 1, Cor 2, Cor 3, Cor 4, Cor 5, nesta ordem). (Se a mesma cor for usada mais de uma vez, sobrará pelo menos uma cor não usada que pode ser aplicada em $v$).
Agora, no grafo $G'$, considere o subgrafo induzido apenas por vértices pintados com a Cor 1 e a Cor 3, e seja o componente conexo contendo $v_1$ denotado por $C_{13}$ (esta é a cadeia de Kempe).
  - **Subcaso 2a: $v_3 \notin C_{13}$.** Ou seja, não há caminho de $v_1$ para $v_3$ passando apenas por vértices das cores 1 e 3. Neste caso, podemos inverter as cores de todos os vértices em $C_{13}$ (Cor 1 $\leftrightarrow$ Cor 3) e a validade da coloração se mantém. Após a inversão, $v_1$ se torna da Cor 3 e, como $v_3$ também é da Cor 3, a Cor 1 deixa de existir ao redor de $v$. Assim, podemos pintar $v$ com a Cor 1.
  - **Subcaso 2b: $v_3 \in C_{13}$.** Ou seja, há um caminho $P_{13}$ formado por vértices das cores 1 e 3 ligando $v_1$ e $v_3$. Juntando esse caminho $P_{13}$ com o vértice $v$ e as arestas $(v, v_1)$ e $(v, v_3)$, forma-se uma curva fechada (ciclo) no plano. Pelas propriedades dos grafos planos (Teorema da Curva de Jordan), esse ciclo divide o plano em um interior e um exterior.
  Os vértices $v_2$ e $v_4$ estão localizados em lados opostos deste ciclo (um dentro, o outro fora).
  Considere a cadeia de Kempe $C_{24}$ feita de vértices com as cores 2 e 4. Se assumirmos que $v_2$ e $v_4$ estão conectados por essa cadeia, deve existir um caminho $P_{24}$ ligando $v_2$ e $v_4$. No entanto, embora $P_{24}$ deva correr no grafo plano sem se cruzar, ele não pode atravessar o ciclo formado por $P_{13}$ (o que contrariaria a definição de grafo plano).
  Portanto, um caminho de cores 2 e 4 conectando $v_2$ e $v_4$ absolutamente não existe. Ou seja, a cadeia de Kempe $C_{24}$ contendo $v_2$ com cores 2 e 4 não inclui $v_4$.
  Assim, ao inverter as cores dentro de $C_{24}$ (Cor 2 $\leftrightarrow$ Cor 4), $v_2$ passa a ter a Cor 4 e a Cor 2 desaparece do redor de $v$. Finalmente, $v$ pode ser pintado com a Cor 2.

Por meio disso, $v$ pode ser colorido em qualquer situação, e o Teorema das Cinco Cores está completamente provado por indução matemática. $\blacksquare$

Essa prova usa brilhantemente a topologia dos grafos planos (o Teorema da Curva de Jordan), demonstrando o quão robusto o conceito de Kempe da "cadeia de Kempe" é em sua aplicação de cadeias únicas não cruzadas. No entanto, o caminho para as "quatro cores" a partir daqui mergulharia em um oceano absurdo de cálculos através dos novos paradigmas de "redutibilidade" e "conjunto inevitável".

## Capítulo 3: A Matemática do Método de Descarga (Discharging Method) e a Derivação das Configurações Inevitáveis

Após Heawood, os matemáticos assumiram a existência de um "Menor Contraexemplo (Minimum Counterexample)" que não pudesse ser colorido com quatro cores e, por redução ao absurdo, começaram a explorar qual estrutura ele deveria (ou não deveria) ter. Aqui, dois conceitos poderosos se tornam importantes: "Configuração Redutível (Reducible Configuration)" e "Conjunto Inevitável (Unavoidable Set)".

### Redutibilidade (Reducibility)
Uma configuração redutível é um subarranjo local (padrão) de vértices que "absolutamente não poderia existir dentro do grafo se todo o grafo não puder ser colorido com quatro cores (sendo ele o menor contraexemplo)".
Por exemplo, "um vértice de grau 3 ou inferior" e "um vértice de grau 4" são configurações redutíveis. Isso porque, como mencionado antes, ao usar a redução através de cadeias de Kempe, se eles existissem, poderiam ser reduzidos a um problema de um grafo menor, o que contradiz a suposição de ser o "menor contraexemplo".
Em 1913, George David Birkhoff provou que uma configuração específica de 6 vértices chamada "Diamante de Birkhoff" também é redutível. A descoberta das configurações redutíveis avançou, mas a prova não seria alcançada a menos que fosse garantido que elas "devem necessariamente existir" dentro do grafo.

### A Estrutura Matemática do Método de Descarga (Discharging Method)
A estratégia final para provar o Teorema das Quatro Cores resumia-se em: **"Encontrar um conjunto inevitável, onde cada membro dele seja composto por configurações redutíveis"**.
Um conjunto inevitável é uma lista de configurações de tal forma que "todo grafo plano (mais precisamente, grafo plano maximal) tem obrigatoriamente que conter pelo menos uma das configurações daquele conjunto".

Para construir e provar esse conjunto inevitável, a arma extremamente poderosa refinada por Heinrich Heesch é o "Método de Descarga (Discharging Method)". O método de descarga é uma técnica quase mágica para provar teoremas estruturais na teoria dos grafos, utilizando o conceito de carga elétrica do eletromagnetismo como analogia.

O processo matemático do método de descarga é o seguinte:
1. **Atribuição da Carga Inicial:**
   Para cada vértice $v$ do grafo plano maximal, atribuímos uma Carga Inicial (Initial Charge) $ch(v)$ da seguinte forma:
   $$ch(v) = 6 - \deg(v)$$
   Pela equação $\sum_{v} (6 - \deg(v)) = 12$ derivada da fórmula de Euler, a soma das cargas iniciais de todo o grafo é estritamente 12 (um valor positivo).
   Assim, vértices de grau 5 têm carga $+1$, vértices de grau 6 têm $0$, e vértices de grau 7 ou superior têm cargas negativas. (Como podemos assumir que o menor contraexemplo não tem vértices de grau 4 ou menos, o grau mínimo considerado é 5).

2. **Definição das Regras de Transferência de Carga (Discharging Rules):**
   A seguir, são definidas as regras para transferir carga entre vértices adjacentes. A ideia básica é: "fazer fluir (descarregar) carga de um vértice com carga positiva (ou seja, vértices de grau 5) para um vértice com carga negativa (vértices de grau alto, 7 ou superior)".
   Por exemplo, definiam-se dezenas ou centenas de regras detalhadas como "se um vértice $v$ de grau 5 for adjacente a um vértice $u$ de grau 7, transfira $\frac{1}{5}$ de carga de $v$ para $u$".

3. **Derivação de Contradição e Identificação das Configurações Inevitáveis:**
   De acordo com as regras definidas, completa-se toda a transferência de carga (Discharging). Como o movimento de carga é apenas uma transferência interna no grafo, a soma total das cargas permanece 12 (positiva) mesmo após as transferências.
   $$ \sum_{v \in V} ch'(v) = 12 > 0 $$
   (Sendo $ch'(v)$ a carga do vértice $v$ após a transferência).
   O fato de a soma total ser positiva significa que **"mesmo após a transferência de carga, deve existir pelo menos um vértice com carga positiva"**.

   Aqui, a carga final de cada vértice $ch'(v)$ é analisada com base na estrutura local (o padrão de graus desse vértice e de seus vértices adjacentes). Se for provado que "um vértice que não possui determinada configuração específica sob as regras de descarga dadas, acabará sempre com a sua carga final menor ou igual a zero", isso significa que, para a carga final ser positiva, essa "configuração específica" tem que existir obrigatoriamente em alguma parte do grafo.
   Desta forma, uma lista exaustiva de todos os padrões de configurações locais que resultam numa carga final positiva torna-se o "conjunto inevitável".

Heesch estava convencido de que usando este método de descarga, um conjunto inevitável composto por um número finito (provavelmente milhares) de configurações redutíveis poderia ser construído. No entanto, a complexidade computacional para verificar se uma certa configuração é "redutível" explode de forma exponencial com o tamanho de sua borda. Checar a redutibilidade de milhares de configurações por cálculos manuais era humanamente impossível, nem durante toda uma vida.

## Capítulo 4: 1976, O Algoritmo de Verificação Computacional de Appel e Haken

### Definição de D-reduction e C-reduction
Nos anos 70, Kenneth Appel e Wolfgang Haken da Universidade de Illinois embarcaram em um projeto histórico para fundir o método de descarga de Heesch com o poder de cálculo dos computadores.

A tarefa computacional mais pesada em que eles trabalharam foi a "verificação de redutibilidade" das configurações. A redutibilidade é dividida principalmente em dois tipos:
- **D-redutibilidade (D-reducibility / Direct reducibility):** Quando, para todas as possíveis colorações de 4 cores da borda anelar (Ring) que envolve a configuração, a pintura pode ser estendida para o interior da configuração, ou os padrões de cores na borda podem ser transformados, pela inversão das cadeias de Kempe, em padrões que são estensíveis para o interior. Se isso for confirmado, pode-se afirmar imediatamente que a configuração não estará incluída no menor contraexemplo.
- **C-redutibilidade (C-reducibility / Contracting reducibility):** Quando existem padrões que falham no teste de D-redutibilidade, o método de considerar um grafo menor obtido por "contração (fundindo múltiplos vértices num só)" em uma parte da configuração e provar que se esse grafo contraído for 4-colorível, o grafo original também o será.

### O Algoritmo de Verificação de Coloração da Borda Anelar
A tarefa confiada ao computador (IBM 360) foi a execução de um algoritmo de verificação para a D-redutibilidade e a C-redutibilidade em um número massivo de configurações candidatas.

Suponha que uma configuração $C$ possua um anel de borda $R$ (de comprimento $k$). O número de combinações de 4 cores dos vértices no anel é no máximo $4^k$, e mesmo considerando as simetrias, o número é gigantesco. Por exemplo, se o comprimento do anel for $k=14$, é necessário verificar a validade de cerca de 200.000 padrões de colorações de fronteira.
O algoritmo procedia nos seguintes passos:
1. Gerar o conjunto de todos os padrões válidos de coloração com 4 cores da fronteira anelar $R$.
2. Tentar todas as formas de pintar internamente a configuração $C$ com 4 cores e registrar com quais padrões de fronteira elas combinam (ou seja, se são internamente estensíveis).
3. Para os padrões de borda não estensíveis internamente, simular a inversão das cadeias de Kempe. Se a inversão levar a um padrão que já se sabe que é "internamente estensível", esse padrão inicial também será considerado como "resolvido".
4. Repetir esta exploração das transições por inversão, e se todos os padrões de borda puderem ser resolvidos, a configuração $C$ é julgada como "D-redutível".

Como o tempo de computação explode à medida que a extensão do anel cresce, Appel e Haken restringiram o comprimento do anel no máximo a 14, e então fizeram um ajuste minucioso das regras de descarga para construir um conjunto inevitável dentro desses limites. O próprio processo de ajuste foi uma sucessão interminável de tentativas e erros pelo homem e o computador. Esse processo interativo - "os humanos corrigiam as regras de descarga, o computador identificava os candidatos a conjunto inevitável e testava a redutibilidade, e, diante das configurações que falhavam, os humanos alteravam de novo as regras" - continuou por anos.

### 1200 Horas de Computação e o "Q.E.D."
Em 1976, através das regras de descarga primorosamente construídas, eles finalmente descobriram um conjunto inevitável consistindo em **1.936** configurações. Em seguida, após executar o mainframe da Universidade de Illinois por mais de 1200 horas, o computador confirmou que todas as 1.936 configurações eram D-redutíveis ou C-redutíveis.

Eles escreveram de forma sucinta no resumo do seu artigo:
*"Every planar map is four colorable." (Todo mapa plano é quatro-colorível).*

Os selos postais do Departamento de Matemática da Universidade de Illinois apresentavam uma orgulhosa marca: "FOUR COLORS SUFFICE (Quatro cores são suficientes)". Este foi um evento monumental e histórico na matemática em que um computador desempenhou o papel central dos passos dedutivos principais na prova de um teorema.

## Capítulo 5: O Choque no Mundo da Matemática e a Filosofia da "Prova"

O anúncio de Appel e Haken não gerou apenas comemoração no mundo da matemática, mas também profunda confusão e um debate acalorado.

### Uma Prova Ilegível por Seres Humanos É Matemática?
Na tradição matemática, contínua desde a Grécia antiga, a "prova" era o processo no qual matemáticos humanos podiam seguir cada passo lógico, compreendê-los do fundo do coração e se sentirem convencidos. Acreditava-se que o processo de prova continha um profundo insight sobre "por que o teorema se sustenta" e abrigava uma beleza estrutural.

Porém, a prova do Teorema das Quatro Cores era alienígena. O artigo continha apenas a lista de 1.936 configurações e a descrição do algoritmo do computador. O traço (registro de execução) dos testes de redutibilidade era tão grande que seria difícil até mesmo imprimi-lo no papel. Qualquer gênio da matemática acharia impossível refazer esse cálculo manualmente pelo resto da sua vida, certificando-se de que não havia falhas lógicas.

Nasceu uma situação inédita: "Para acreditar que a prova está correta, é preciso acreditar que o hardware do computador não está avariado e que não há bugs no programa de linguagem assembly escrito por Appel e Haken".

O filósofo da ciência Thomas Tymoczko criticou a prova, afirmando que ela havia degenerado da busca pelas verdades a priori da matemática pura, transformando-se em um experimento empírico semelhante à física. A própria definição do ato de "provar" enfrentou uma crise epistemológica.

### Contra-argumentos e Simplificações pela Equipe RSST
Appel e Haken contra-argumentaram contra a crítica, afirmando: "A matemática não são apenas provas belas. Existem problemas intrinsecamente complexos que exigem uma divisão massiva de casos, e se eles superarem o limite dos cérebros humanos, recorrer ao poder da máquina é uma evolução inevitável".

Para dissipar essa frustração, muitos matemáticos tentaram simplificar e reverificar a prova. Em 1997, quatro pesquisadores – Neil Robertson, Daniel P. Sanders, Paul Seymour e Robin Thomas (conhecidos como RSST) – publicaram uma nova prova. Eles tornaram o método de descarga mais sistemático e mais fácil de ser verificado por humanos e diminuíram o tamanho do conjunto inevitável de 1.936 para 633 configurações. Era um algoritmo elegante cujo cálculo terminava em apenas algumas horas.

Ainda assim, não mudou o fato de que a prova continuou dependendo dos "cálculos computacionais de redutibilidade". A "prova bela a papel e caneta", perfeitamente compreensível pela intuição humana, ainda não foi encontrada (e muitos estudiosos da teoria dos grafos pensam que, em princípio, não deverá existir tal prova).

## Capítulo 6: A Prova Formal Completa de Georges Gonthier Utilizando o Coq

Como podemos remover por completo e matematicamente a ansiedade de que "o programa pode ter bugs"? A resposta derradeira para isso é a Formalização Total (Formalization) usando um "Assistente de Prova (Proof Assistant)".

Em 2005, Georges Gonthier do Instituto Nacional de Investigação em Informática e Automática da França (INRIA) e da Microsoft Research, juntamente com Benjamin Werner, conseguiu formalizar a prova do Teorema das Quatro Cores a partir da base, usando o assistente de prova "Coq".

### Formalização do Hipermapa (Hypermap) e da Topologia Combinatória
O Coq é um sistema que, partindo dos axiomas matemáticos, descreve as provas e as verifica de forma automática através de um sistema de regras lógicas extremamente rigoroso (Cálculo de Construções Indutivas).

O maior feito de Gonthier foi o de traduzir o objeto geométrico e intuitivo do grafo plano numa estrutura totalmente algébrica e combinatória capaz de ser compreendida por computadores. Ele definiu uma estrutura de dados chamada "Hypermap (Hipermapa)" para representar as relações entre os vértices, arestas e faces do grafo. Essa é uma forma de representar o grafo através de conjuntos de "dardos (meias arestas)" e grupos de permutações neles operando. Assim, o Teorema de Euler e o Teorema da Curva de Jordan, da topologia, foram formalizados de maneira perfeita na lógica combinatória dos conjuntos finitos e da teoria de grupos.

### Prova da Correção do Próprio Programa de Prova
Além disso, Gonthier descartou "o programa de verificação escrito na linguagem C" usado por Appel-Haken ou pela RSST, implementando ele próprio o algoritmo que avalia a redutibilidade utilizando a linguagem interna do Coq (Gallina). Em seguida, **ele provou matematicamente no próprio Coq a validade intrínseca do algoritmo, demonstrando que "se este algoritmo de avaliação retornar 'True', então a configuração é verdadeiramente redutível"**.

Com isso, a confiabilidade da prova mudou decisivamente. Não havia mais a preocupação com "bugs no algoritmo". Uma vez que o núcleo de verificação lógica do Coq (apenas umas centenas de linhas de código, baseadas no índice de De Bruijn e muito robustas) processe as regras de dedução lógica de forma adequada, é matematicamente garantido que a gigantesca árvore de prova construída por Gonthier está absolutamente certa.

Este foi um novo marco na "prova" matemática. Foi a transição da "prova que um ser humano lê e entende (Informal Proof)" para a "prova formal com a completude lógica atestada pela máquina (Formal Proof)". O Teorema das Quatro Cores tornou-se o primeiro teorema não-trivial na história a alcançar esse nível extremo de rigorosidade.

## Capítulo 7: O Problema das 4 Cores em Grafos Planos e o Paradoxo da Completude NP

Por fim, vejamos o Teorema das Quatro Cores através da ótica da Teoria da Complexidade Computacional (Computational Complexity Theory). Aqui existe um fenômeno muitíssimo interessante, que se assemelha a um paradoxo.

O problema de coloração num grafo geral (determinar se um grafo dado pode ser pintado com $k$ cores) é um dos problemas "NP-Completos (NP-complete)" mais famosos na ciência da computação. O problema particular da "Coloração com 3 cores em Grafos Planos (Planar 3-Colorability)" também é provado ser NP-Completo. Em suma, assume-se que não existe um algoritmo de tempo polinomial que descubra se o grafo plano pode ser colorido com 3 cores, a não ser que $\text{P} = \text{NP}$.

Então, o que dizer sobre a "Coloração com 4 cores em Grafos Planos (Planar 4-Colorability)"? Alguém poderia pensar intuitivamente que, se colorir com 3 cores é NP-Completo, colorir com 4 cores também deve ser igualmente difícil (NP-Completo).

Surpreendentemente, contudo, **a complexidade computacional para o problema de decisão da coloração com 4 cores em um grafo plano é $O(1)$, ou seja, "tempo constante (trivial)".**
Isso acontece porque o Teorema das Quatro Cores assegura que "todos os grafos planos podem ser pintados com 4 cores", portanto o algoritmo nem sequer precisa ver o grafo de entrada; o mero output de "Yes" estará sempre 100% correto. Este é um belo exemplo de como a poderosa garantia de existência pelo Teorema reduziu a complexidade do problema de decisão ao seu limite absoluto.

Entretanto, isso trata apenas do Problema de Decisão (Decision Problem), ou seja, "se é possível colorir ou não". Construir um **algoritmo de coloração (Search Problem) sobre "como realmente colorir o grafo com 4 cores"** é uma história diferente.
Se implementarmos os procedimentos de prova de Appel-Haken ou de RSST como algoritmos, obteremos um algoritmo capaz de encontrar as colorações para as 4 cores, na prática, dado qualquer grafo plano de $N$ vértices. É demonstrado que o algoritmo baseado na prova da RSST produz a 4-coloração em tempo polinomial num pior cenário de $O(N^2)$.

Em outras palavras, se tentarmos colorir um grafo plano com 3 cores, o tempo poderá equivaler a toda a vida útil do universo (por ser NP-Completo); contudo, no instante em que adicionamos uma 4ª cor, a benção oriunda das estruturas matemáticas por trás do Teorema das Quatro Cores nos proverá de algoritmos extremamente rápidos (de $O(N^2)$). É um fato misterioso e extremamente fascinante onde a matemática e a ciência da computação se cruzam.

## Conclusão: O Legado do Teorema das Quatro Cores

O que em 1852 surgiu como a ingênua pergunta de um jovem britânico a respeito da coloração de mapas começou como um mero quebra-cabeça. Contudo, ao longo de mais de um século, ele forjou uma vasta e nova área da matemática — a teoria dos grafos — promoveu a evolução da teoria dos algoritmos e confrontou a humanidade com questões filosóficas profundas: "Poderá uma máquina realizar provas matemáticas?" e "O que é, ao certo, a Verdade Matemática?".

A história do Teorema das Quatro Cores é a história do embate entre os limites da intuição humana e o potencial das máquinas como novos motores lógicos. Atualmente, os sistemas de prova formal baseados no Teorema permitiram a comprovação total de outras questões hercúleas, como a Conjectura de Kepler (em 2014, pelo projeto Flyspeck de Thomas Hales) e o Teorema de Feit-Thompson.

No nosso cotidiano, quando casualmente pintamos um mapa com 4 cores, escondemos por baixo a estética dos poliedros de Euler, o tropeço genial de Kempe, as contraprovas estritas de Heawood, a matemática das descargas de Heesch, os traços de cálculo de supercomputadores que piscaram incansáveis por milhares de horas, e a profunda formalização do hipermapa estrutural no Coq. O Teorema das Quatro Cores permanecerá para sempre como o maior estudo de caso de como a matemática transborda de modo contínuo os confins da percepção humana.
