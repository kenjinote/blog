---
title: "Teoria de Ramsey: A ordem surge inevitavelmente na desordem — Provando as relações entre 6 pessoas por coloração"
date: "2026-09-24T19:44:38+09:00"
description: "Em qualquer grupo de 6 pessoas, sempre existem 3 pessoas que se conhecem mutuamente ou 3 que não se conhecem mutuamente. Provamos o número de Ramsey R(3,3)=6 com diagramas coloridos, exploramos o contraexemplo de 5 pessoas, verificamos todas as 32.768 possibilidades e abordamos aplicações em sequências numéricas e redes."
date: 2026-09-16T20:05:00+09:00
image: "eyecatch.jpg"
categories: ["mathematics"]
tags: ["Teoria de Ramsey", "Teoria dos Grafos", "Combinatória", "Princípio da Casa dos Pombos", "Python"]
slug: "ramsey-theory"
math: true
---

## 1. Ao reunir 6 pessoas, um trio específico é inevitável

Imagine que 6 pessoas se reúnem em uma festa. Alguns podem ser velhos conhecidos, enquanto outros estão se encontrando pela primeira vez. Não importa quão intricadas sejam as relações de quem conhece quem, uma das duas seguintes situações sempre acontecerá:

- **Quaisquer duas pessoas escolhidas entre essas três se conhecem mutuamente.**
- **Quaisquer duas pessoas escolhidas entre essas três não se conhecem mutuamente.**

Não estamos dizendo que isso acontece "na maioria das vezes". Independentemente de como os relacionamentos estejam configurados, o trio será encontrado sem exceção. Além disso, o número 6 é o mínimo. Com 5 pessoas, é perfeitamente possível construir uma configuração na qual nenhum dos dois tipos de trio se forme.

Essa pequena surpresa é a porta de entrada para a **[Teoria de Ramsey](https://kenji.blog/pt/p/ramsey-theory/)**. Por mais que você particione ou subdivida uma grande estrutura de maneira complexa, se ela for grande o suficiente, será impossível evitar completamente o surgimento de uma subestrutura menor com propriedades homogêneas. Essa área da matemática estuda justamente essa "regularidade inevitável".

No entanto, isso não significa que qualquer regra arbitrária surja do caos. Só se torna uma proposição matemática quando definimos com precisão qual é o objeto de estudo, em quantas classes ele é classificado e qual formato estamos procurando. Comecemos por um exemplo simples e intuitivo que pode ser desenhado com 6 pontos em uma folha de papel.

## 2. Representando as relações humanas com linhas vermelhas e azuis

### Premissas do modelo

Neste artigo, consideramos que "conhecer alguém" é uma relação simétrica: se A conhece B, então B também conhece A. Além disso, cada par é categorizado de forma binária e precisa como "se conhecem" ou "não se conhecem".

Relações unilaterais (como apenas saber o nome de alguém à distância) ou situações ambíguas não fazem parte deste modelo. Vale destacar também que "não se conhecerem" não significa que sejam "inimigos" ou que "não se gostem".

Representamos as pessoas como pontos (vértices) e as relações entre cada par de pessoas como linhas (arestas).

| Elemento do diagrama | Significado |
|---|---|
| Ponto (vértice) | 1 participante |
| Linha contínua vermelha | As duas pessoas se conhecem mutuamente |
| Linha tracejada azul | As duas pessoas não se conhecem mutuamente |
| [Tri](https://kenji.blog/pt/p/sorting-algorithms/)ângulo formado por 3 lados da mesma cor | O trio que estamos procurando |

Como conectamos todos os pares possíveis entre todos os participantes, temos um **grafo completo**. Um grafo completo com $n$ vértices é denotado por $K_n$, e o número de arestas é dado por:

$$
\binom{n}{2}=\frac{n(n-1)}{2}
$$

Para 6 pessoas, existem 15 arestas. O fato de "A conhecer B e C" não garante que os três se conheçam mutuamente; a aresta entre B e C também precisa ser vermelha. Lembre-se de que a condição fundamental é que **todos os 3 lados** do triângulo tenham a mesma cor.

A partir daqui, chamamos um triângulo totalmente vermelho ou totalmente azul de **triângulo monocromático**. Para garantir a acessibilidade visual mesmo para quem tem dificuldade em distinguir cores, os diagramas mostram as arestas vermelhas como linhas contínuas e as azuis como linhas tracejadas.

## 3. Demonstração: por que o trio é garantido com 6 pessoas

A única ferramenta necessária para esta demonstração é o [Princípio da Casa dos Pombos](../pigeonhole-principle-hash-collision/). Usamos o fato simples e intuitivo de que: "ao distribuir 5 objetos em 2 categorias, pelo menos uma das categorias conterá 3 ou mais objetos".

### Passo 1: Focar em uma única pessoa

Escolha qualquer uma das 6 pessoas e chame-a de A. Do vértice A, partem 5 arestas em direção às outras 5 pessoas. Como cada aresta é vermelha ou azul, pelo menos 3 delas terão a mesma cor:

$$
\left\lceil\frac{5}{2}\right\rceil=3
$$

Aqui, $\lceil x\rceil$ denota a função teto, ou seja, o menor número inteiro maior ou igual a $x$. Da mesma forma, se houvesse no máximo 2 arestas vermelhas e no máximo 2 azuis, o total seria de no máximo 4 arestas, o que não cobre as 5 existentes.

Suponha, sem perda de generalidade, que haja 3 ou mais arestas vermelhas, e chamemos as três pessoas conectadas a elas de B, C e D. Assim, as arestas A–B, A–C e A–D são todas vermelhas. (Se houvesse 3 ou mais arestas azuis, bastaria inverter os papéis de vermelho e azul no argumento a seguir).

### Passo 2: Analisar as conexões entre B, C e D

Ao observar as 3 arestas entre B, C e D (B–C, B–D e C–D), existem apenas dois casos possíveis:

**Caso 1: Existe pelo menos uma aresta vermelha.** Por exemplo, se a aresta B–C for vermelha, como A–B e A–C já são vermelhas, o trio A, B e C forma um triângulo vermelho. As cores das outras duas arestas não importam.

**Caso 2: Não há nenhuma aresta vermelha.** Nesse caso, B–C, B–D e C–D devem ser todas azuis. Dessa vez, os vértices B, C e D formam um triângulo azul.

![Diagrama de prova mostrando que, ao escolher 3 arestas da mesma cor a partir de A, forma-se um triângulo vermelho se houver uma aresta vermelha entre os outros 3 vértices, ou um triângulo azul se não houver](six-person-proof.svg)

As arestas cinzas e as arestas omitidas no diagrama representam partes cujas cores são irrelevantes para a prova. No grafo completo real, cada uma delas também seria colorida de vermelho ou azul.

Com isso, demonstramos que qualquer coloração possível contém um triângulo monocromático. Não foi preciso analisar exaustivamente todas as 15 arestas: **as 5 arestas incidentes em uma única pessoa e as relações entre as 3 pessoas adjacentes foram suficientes para cobrir todas as possibilidades.** [Explicação em material didático universitário](https://ximera.osu.edu/math/combinatorics/combinatoricsBook/combinatoricsBook/combinatorics/ramseyTheory/ramseyTheory)

## 4. Por que 5 pessoas não são suficientes?

Dizer que "6 pessoas são suficientes" e que "6 é o número mínimo" são duas afirmações distintas. Para demonstrar a minimalidade, precisamos exibir pelo menos um exemplo com 5 pessoas que não satisfaça a condição.

Posicionemos 5 pessoas nos vértices de um pentágono regular. Colorimos de vermelho as 5 arestas do perímetro que conectam vértices adjacentes. As 5 arestas diagonais restantes são coloridas de azul.

![Contraexemplo de 5 pessoas com o perímetro do pentágono em vermelho e as diagonais em azul. Não há triângulos em nenhuma das duas cores](five-person-counterexample.svg)

Observando apenas as arestas vermelhas, temos um ciclo de comprimento 5 ao redor do pentágono. Não importa quais 3 vértices sejam escolhidos, é impossível fechar um triângulo apenas com arestas vermelhas. Observando apenas as arestas azuis, temos uma estrela de cinco pontas; no entanto, reordenando os vértices, ela também forma um ciclo simples de 5 vértices. Portanto, também não existem triângulos azuis.

Note que os pontos de interseção das linhas da estrela não são vértices: apenas os 5 pontos de A a E representam pessoas. As pequenas regiões triangulares formadas pelo cruzamento visual das linhas não contam como triângulos neste problema.

Como conseguimos evitar tanto o trio vermelho quanto o trio azul, 5 pessoas não garantem a propriedade. Juntando isso à garantia de que "com 6 pessoas é sempre verdadeiro", estabelecemos que o número mínimo é exatamente 6.

## 5. Esse "tamanho mínimo" é chamado de Número de Ramsey

Quando as arestas de um grafo completo são coloridas de vermelho e azul, o número mínimo de vértices necessário para garantir a existência de um subgrafo completo vermelho $K_s$ ou um subgrafo completo azul $K_t$ é denominado **número de Ramsey**, denotado por $R(s,t)$.

Um subgrafo $K_s$ vermelho significa que todas as arestas entre os $s$ vértices escolhidos são vermelhas; não basta que estejam simplesmente conectados por um caminho vermelho. Como $K_3$ representa um triângulo, a conclusão a que chegamos até aqui se resume a:

$$
R(3,3)=6
$$

O Teorema de Ramsey afirma que, para quaisquer inteiros finitos fixados $s$ e $t$, esse número finito sempre existe. Porém, "existir" é bem diferente de "ser fácil de calcular". Embora a prova para triângulos seja curta e direta, encontrar o número exato para grupos monocromáticos maiores torna-se exponencialmente difícil.

Um limite superior clássico é dado pela seguinte relação recursiva:

$$
R(s,t)\leq R(s-1,t)+R(s,t-1)
\qquad(s,t\geq3)
$$

Definindo o lado direito como $N$, escolhemos 1 vértice arbitrário entre os $N$ vértices. Se houver $R(s-1,t)$ ou mais vértices conectados a ele por arestas vermelhas, esse subgrupo conterá um $K_{s-1}$ vermelho ou um $K_t$ azul. Se for o primeiro caso, adicionando o vértice inicial obtemos um $K_s$ vermelho; se for o segundo, o objetivo já está cumprido.

Se não houver tantas arestas vermelhas assim, haverá pelo menos $R(s,t-1)$ vértices conectados por arestas azuis. O mesmo raciocínio se aplica simetricamente à outra cor. Esta é uma extensão natural da prova anterior: "focar em um vértice e agrupar seus vizinhos da mesma cor".

Partindo dos valores de fronteira $R(2,t)=t$ e $R(s,2)=s$, podemos construir sucessivos limites superiores finitos usando essa relação. Contudo, como se trata de uma desigualdade, o valor obtido nem sempre é o mínimo exato. É fundamental distinguir entre "um tamanho que oferece garantia teórica" e o "valor mínimo estritamente necessário".

## 6. A diferença entre "quase certamente" e "sempre, sem exceção"

Como experimento mental, imagine que cada aresta seja colorida de vermelho ou azul de forma independente com probabilidade $1/2$. Esse modelo probabilístico não é necessário para a demonstração teórica, mas ajuda a ilustrar as diferenças de comportamento de maneira intuitiva.

Mantendo os vértices rotulados como A, B, C, ..., o número total de colorações possíveis é dado por:

$$
2^{\binom{n}{2}}
$$

Para 6 pessoas, temos $2^{15}=32.768$ colorações possíveis. Examinando exaustivamente todos os casos de 3 a 6 pessoas, obtemos os seguintes resultados:

| Número de pessoas | Total de colorações | Colorações sem triângulos monocromáticos | Proporção com triângulos monocromáticos |
|---|---:|---:|---:|
| 3 pessoas | 8 | 6 | 25,00% |
| 4 pessoas | 64 | 18 | 71,88% |
| 5 pessoas | 1.024 | 12 | 98,83% |
| 6 pessoas | 32.768 | 0 | 100,00% |

![Comparação da proporção de existência de triângulos monocromáticos para 3 a 6 pessoas. Para 5 pessoas é de 98,83%, restando 12 contraexemplos, enquanto para 6 pessoas atinge 100%](coloring-probability.svg)

Mesmo para 5 pessoas, se colorirmos as arestas aleatoriamente, em cerca de 98,83% das vezes haverá um triângulo monocromático. Quem testar apenas algumas vezes pode facilmente ter a ilusão de que "5 pessoas já bastam". No entanto, das 1.024 possibilidades, restam 12 contraexemplos. Há uma diferença conceitual profunda entre "ter alta probabilidade" e "não existir nenhum contraexemplo".

Esta tabela reflete a distribuição quando as arestas são coloridas de forma equiprovável e independente. Ela não afirma que os relacionamentos humanos reais ocorram com 50% de chance de forma isolada. Por outro lado, o teorema para 6 pessoas independe de probabilidades: ele se sustenta com certeza matemática absoluta, por mais desbalanceadas ou enviesadas que sejam as relações.

### Em média, quantos triângulos aparecem?

Para quaisquer 3 vértices fixos, existem 3 arestas e $2^3 = 8$ colorações possíveis. Dessas, apenas 2 (todas vermelhas ou todas azuis) são monocromáticas, de modo que a probabilidade é de $2/8 = 1/4$. Sendo $T$ o número total de triângulos monocromáticos, pela linearidade da esperança matemática, temos:

$$
E[T]=\binom{n}{3}\frac14
$$

Para 6 pessoas, a média é de exatamente 5 triângulos. Embora diferentes triângulos compartilhem arestas e não sejam independentes entre si, a linearidade da esperança não requer independência.

Contudo, o fato de o valor esperado ser estritamente positivo não implica que triângulos existam em todas as colorações possíveis. Para 5 pessoas, a média é de 2,5 triângulos, mas ainda assim existem contraexemplos com exatamente 0 triângulos. Não confundir o "caso médio" com o "pior caso" é uma lição fundamental proporcionada pela [Teoria de Ramsey](https://kenji.blog/pt/p/ramsey-theory/).

## 7. Verificando todas as 32.768 possibilidades em Python

O código a seguir utiliza apenas a biblioteca padrão do Python. Representamos o vermelho por 0 e o azul por 1, mapeando a cor de cada aresta a um bit de um número inteiro. Para cada conjunto de 3 vértices, verificamos se as 3 arestas correspondentes possuem a mesma cor.

```python
from itertools import combinations

def check_all(n):
    edges = list(combinations(range(n), 2))
    edge_index = {edge: i for i, edge in enumerate(edges)}
    triples = [
        [edge_index[e] for e in combinations(vertices, 2)]
        for vertices in combinations(range(n), 3)
    ]
    total = 1 << len(edges)
    without_triangle = 0
    minimum = len(triples)

    for coloring in range(total):
        count = 0
        for i, j, k in triples:
            if ((coloring >> i) & 1) == ((coloring >> j) & 1) == ((coloring >> k) & 1):
                count += 1
        without_triangle += (count == 0)
        minimum = min(minimum, count)

    return total, without_triangle, minimum

for n in range(3, 7):
    total, missing, minimum = check_all(n)
    print(f"{n} pessoas: total de {total} colorações, sem triângulos {missing}, mínimo {minimum}")
```

```text
3 pessoas: total de 8 colorações, sem triângulos 6, mínimo 0
4 pessoas: total de 64 colorações, sem triângulos 18, mínimo 0
5 pessoas: total de 1024 colorações, sem triângulos 12, mínimo 0
6 pessoas: total de 32768 colorações, sem triângulos 0, mínimo 2
```

O resultado de que há "no mínimo 2" triângulos para 6 pessoas é um fato ainda mais forte do que a nossa demonstração inicial sugeria. De fato, se denotarmos o número de arestas vermelhas incidentes no vértice $v$ por $r_v$ e de arestas azuis por $b_v$, temos $r_v+b_v=5$, o que implica $r_vb_v\leq6$.

Em qualquer triângulo não monocromático, há exatamente dois vértices onde se encontram uma aresta vermelha e uma azul. Contando o número de pares "uma aresta vermelha e uma aresta azul" incidentes em cada vértice, cada triângulo não monocromático é contado exatamente duas vezes. Como o número total de triângulos em $K_6$ é $\binom{6}{3} = 20$, temos:

$$
T=\binom63-\frac12\sum_{v=1}^{6}r_vb_v
\geq20-\frac12\cdot6\cdot6=2
$$

o que prova matematicamente o mínimo de 2. Além disso, dividindo os 6 vértices em dois grupos de 3, colorindo as arestas internas de cada grupo de vermelho e todas as arestas entre os grupos de azul, obtemos exatamente dois triângulos vermelhos e nenhum triângulo azul. Logo, o valor mínimo de 2 é exato e inatingível para baixo.

Embora essa enumeração exaustiva seja eficaz para números pequenos, o total de colorações cresce a uma taxa de $2^{n(n-1)/2}$. Executar esse código para valores maiores de $n$ torna-se proibitivamente pesado; por isso, limitamos a demonstração computacional a grupos de 3 a 6 pessoas. Os gráficos e a distribuição detalhada podem ser consultados no [script de reprodução](generate_graphs.py) e no [JSON com os resultados dos cálculos](calculation-results.json).

## 8. Aplicação 1: Redes com "conexão total" ou "desconexão total"

Substituamos o termo "conhecidos" pela existência de uma conexão direta entre dispositivos. Suponha que tenhamos 6 dispositivos de rede e que cada par apresente ou "uma conexão direta" ou "nenhuma conexão direta". Se os enlaces não forem direcionados, o mesmo teorema se aplica de forma direta.

Assim, garante-se a existência de um grupo de 3 dispositivos no qual todos os pares possuem conexões diretas mútuas, ou de um grupo de 3 dispositivos no qual nenhum par possui conexão direta. Na [teoria dos grafos](/pt/p/graph-theory-dijkstra-a-star/), o primeiro caso corresponde a um **clique** de 3 vértices, e o segundo, a um **conjunto independente** de 3 vértices. Vale notar que "sem conexão direta" não significa que a comunicação seja impossível através de dispositivos intermediários.

Essa perspectiva é útil para analisar compatibilidade entre pares de tarefas ou validar o design de pequenas redes. Por exemplo, se você exigir que "não haja nenhum trio onde todos os pares sejam mutualmente compatíveis, nem nenhum trio onde todos sejam mutualmente incompatíveis", saberá, antes mesmo de iniciar qualquer busca exaustiva, que tal exigência é impossível de satisfazer caso haja 6 elementos no sistema.

No entanto, o teorema não permite escolher qual dos dois cenários ocorrerá: pode ser que você precise de um trio compatível, mas o sistema apresente apenas um trio mutuamente incompatível. Além disso, a compatibilidade entre pares não garante automaticamente que haja recursos para executar os 3 elementos simultaneamente. O escopo da garantia matemática restringe-se estritamente às relações binárias definidas.

## 9. Aplicação 2: Extraindo sequências crescentes ou decrescentes de dados desordenados

Considere 6 números distintos dispostos em uma determinada ordem. Para quaisquer duas posições $i$ e $j$ com $i < j$, conectamos essas posições por uma aresta vermelha se $a_i < a_j$, ou por uma aresta azul se $a_i > a_j$.

Isso constitui uma 2-coloração de arestas de um grafo completo com 6 vértices. Pelo que já provamos, um triângulo monocromático é garantido. Se denotarmos os três índices em ordem crescente por $i < j < k$, então, se o triângulo for vermelho, temos:

$$
a_i\lt a_j\lt a_k
$$

e se o triângulo for azul, temos:

$$
a_i\gt a_j\gt a_k
$$

Em outras palavras, **é sempre possível extrair 3 termos que sejam estritamente crescentes ou 3 termos que sejam estritamente decrescentes, preservando a ordem original dos elementos.** Esses termos não precisam ser adjacentes. Uma sequência formada pela extração de elementos que preserva a ordem relativa original é chamada de subsequência.

![Diagrama mostrando a extração da subsequência crescente 1, 2, 3 a partir da sequência 4, 1, 5, 2, 6, 3 selecionando as posições originais 2, 4 e 6](monotone-subsequence.svg)

Na sequência $4, 1, 5, 2, 6, 3$ ilustrada na figura, ao selecionar o 2º, o 4º e o 6º elementos, obtemos a subsequência crescente $1, 2, 3$. Os números não foram reordenados artificialmente; foram selecionados respeitando rigorosamente a ordem em que apareciam.

Esse conceito fundamenta a busca por subestruturas regulares em sequências de dados. No entanto, o fato de existirem 3 pontos crescentes não serve como evidência de uma tendência global de alta na série temporal: se qualquer sequência aleatória de 6 elementos forçada a conter tal padrão pela matemática pura, sua mera presença não representa um fenômeno estatisticamente especial.

Vale notar que, no caso específico de sequências numéricas, 6 termos não são o mínimo absoluto: na verdade, qualquer sequência de 5 termos distintos já garante uma subsequência monotônica (crescente ou decrescente) de comprimento 3. Este é um caso particular do Teorema de Erdős–Szekeres sobre subsequências monótonas. Como as relações de ordem transitivas em sequências impõem restrições adicionais às cores das arestas, obtém-se um resultado ainda mais forte do que em 2-colorações arbitrárias. [Notas de aula sobre subsequências monótonas](https://ywigderson.math.ethz.ch/math/static/pcmi2025/Notes10.pdf)

## 10. Conclusão: mesmo na desordem, existem formas inevitáveis

Ao modelar os relacionamentos de 6 pessoas com arestas vermelhas e azuis e focar nas 5 arestas que partem de uma única pessoa, provamos com elegância que um triângulo monocromático é inevitável. O pentágono com 5 pessoas fornece um contraexemplo concreto, estabelecendo que o número de Ramsey é $R(3,3)=6$.

Os três pontos essenciais a reter são:

- **"Sempre" não significa "com alta probabilidade em testes aleatórios".** Para 5 pessoas, a probabilidade é de cerca de 98,83%, mas ainda existem contraexemplos; para 6 pessoas, não resta nenhum.
- **A existência de um padrão difere do seu significado prático.** Encontrar um triângulo monocromático ou uma subsequência crescente não dita as propriedades globais nem relações de causa e efeito no conjunto de dados.
- **Toda garantia matemática depende de premissas e condições bem definidas.** É necessário especificar se a relação é simétrica, se todos os pares podem ser bipartidos e qual subestrutura exata está sendo buscada.

O fascínio da [Teoria de Ramsey](https://kenji.blog/pt/p/ramsey-theory/) não reside em tornar um sistema complexo simples, mas sim em demonstrar que, mesmo que o todo permaneça caótico e desordenado, é absolutamente impossível eliminar pequenas regularidades locais dentro dele. Com apenas alguns pontos e linhas traçados no papel, podemos comprovar a força desse pensamento matemático.

### Referências

- Ohio [State](https://kenji.blog/pt/p/iac-infrastructure-as-code-terraform/) University, [Ramsey Theory](https://ximera.osu.edu/math/combinatorics/combinatoricsBook/combinatoricsBook/combinatorics/ramseyTheory/ramseyTheory): Explicação sobre 2-coloração de arestas e pequenos números de Ramsey.
- Yuval Wigderson, PCMI 2025, [Extremal graph theory and Ramsey theory: Lecture 10](https://ywigderson.math.ethz.ch/math/static/pcmi2025/Notes10.pdf): Notas de aula sobre conceitos do tipo Ramsey, incluindo subsequências monótonas.

Os diagramas deste artigo, a tabela de enumeração exaustiva e as distribuições de probabilidade e contagem foram gerados com o script Python incluído no repositório.

