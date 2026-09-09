---
title: 'Conjectura de Collatz'
slug: "conjectura-de-collatz"
date: 2025-07-15T18:03:03+09:00
tags: ["Conjectura de Collatz", "Matemática", "Programação", "Algoritmos"]
draft: false
image: "img.webp"
categories: ["Matemática, Criptografia e Quântica"]
---

# É verdade que "qualquer número sempre termina em 1"? ── Brincando com a Conjectura de Collatz

Olá! Aqui é o kenji.

De repente, se você ouvisse falar de uma "regra onde qualquer número acaba virando 1 no final", não acharia um pouco estranho?

> Por exemplo, o 19, o 87 ou até 1000000.
> Se você for modificando os números de acordo com uma regra simples, por algum motivo o resultado sempre converge para "1".

Essa história que parece um sonho é a **Conjectura de Collatz (Collatz Conjecture)**.

---

## Afinal, o que é a Conjectura de Collatz?

Primeiro, vou apresentar a regra.

* Início: Escolha qualquer **número inteiro positivo**
* Operação:

    * Se for par → Divida pela metade (n → n / 2)
    * Se for ímpar → Multiplique por 3 e adicione 1 (n → 3n + 1)

Repetindo isso continuamente, a conjectura diz que **qualquer número acabará chegando a 1**.

Por exemplo, começando com `6`:

```
6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
```

E veja, virou "1". Bem-vindo de volta!

---

## Vamos tentar no código: Collatz com Python

Pois bem, nessas horas a maneira mais rápida é testar com código!
Vamos imprimir uma "sequência de Collatz" em Python.

```python
def collatz(n):
    steps = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps.append(n)
    return steps

# Exemplo: Começando com 19
print(collatz(19))
```

Quando você executa:

```
[19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
```

Ele chega perfeitamente ao 1.
Dá bastante volta, mas no fim sempre cruza a linha de chegada!


A propósito, se começarmos do **27**, ele também chegará a 1.

```
print(collatz(27))
```

Quando você executa:

```
[27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242,
121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350,
175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167,
502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479,
1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911,
2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732,
866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35,
106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
```

Inacreditável, leva 111 passos!

E mais, em alguns momentos chega a inflar para mais de 9000.
É o padrão de dar uma volta gigantesca antes de alcançar a linha de chegada.

---

## Mas afinal, o que isso tem de tão incrível?

O que torna essa conjectura incrível é o seguinte:

> **Embora não tenha sido provada, parece que com qualquer número sempre termina em 1**

É essa a parte surpreendente.

O quê? E se for 1 trilhão, ou 10 quatrilhões...?

Para quem pensou isso, ótima observação.
Na verdade, usando computadores, já foi verificado até cerca de "2 elevado a 68",
e **todos chegaram a 1**. Inacreditável...

Porém, **ainda não foi teoricamente provado que "todos serão assim"**.
Isso é o que chamamos de "problema em aberto" no mundo da matemática.

---

## Por que chega a "1"? Uma abordagem pela teoria das probabilidades (Contexto Matemático)

Parece mágica que qualquer número acabe virando 1, mas de um **ponto de vista probabilístico**, existe uma razão lógica para dizer "é, faz sentido que seja assim".

Se fizermos `3n + 1` para um número ímpar $n$, a resposta sempre será **par**.
Portanto, no próximo passo o número com certeza será dividido por 2, resultando em praticamente $\frac{3n + 1}{2} \approx 1.5n$.

E a probabilidade de esse número ser par novamente é $\frac{1}{2}$.
Se for par, será dividido por 2 de novo e ficará $0.75n$, tornando-se menor do que o número original.

Embora não seja matematicamente rigoroso, sabe-se que ao pegar a média geométrica da "taxa de multiplicação" ao pular de um ímpar para o próximo ímpar, ela será **aproximadamente $\frac{3}{4}$ vezes** (um modelo probabilístico heurístico).
Ou seja, **em média os valores tendem a encolher**, por isso eles acabam caindo e sendo sugados para o 1 no final.

## E se mudarmos um pouco a regra? (Comparação com outras conjecturas)

Dá vontade de pensar: "E se em vez de multiplicar por 3, fosse por 5?".
Na verdade, isso é conhecido como o **problema $5n + 1$**, e neste caso, nem todos os números convergem para 1.

No caso do $5n + 1$, foi confirmado que existem vários loops (ciclos) diferentes, e também foi apontada a possibilidade de existirem números que continuam crescendo infinitamente (divergência).
Além disso, no caso do **problema $3n - 1$**, além do loop "$1 \to 2 \to 1$", também existe outro loop como "$5 \to 14 \to 7 \to 20 \to 10 \to 5$".

Isso mostra como a propriedade da Conjectura de Collatz de "tudo convergir para 1 (loop $4 \to 2 \to 1$)" se sustenta em um equilíbrio perfeito e extremamente delicado.

---

## O limite alcançado pela humanidade ①: Os limites da força bruta por computadores

Atualmente, matemáticos e entusiastas da ciência da computação ao redor do mundo continuam calculando exaustivamente a Conjectura de Collatz usando computação distribuída (projetos que reúnem o poder de processamento de PCs no mundo todo) e GPUs.

Até 2020, foi confirmado por computador que a Conjectura de Collatz é verdadeira (finalmente chega a 1) para todos os valores iniciais abaixo de impressionantes **$2^{68}$ (cerca de 295 quintilhões)**.

No entanto, no mundo da matemática, não se pode dizer "como verificamos até 295 quintilhões, então deve estar tudo certo". Em um oceano infinito de números, até $2^{68}$ é apenas "a primeira gota d'água".

---

## O limite alcançado pela humanidade ②: Indecidibilidade e o avanço de Terence Tao

Para a pergunta "Por que ninguém consegue provar isso?", o genial matemático britânico John Conway provou em 1972 que um problema que expande um pouco a Conjectura de Collatz é **"indecidível (Turing-completo)"**.
Este é um fato assustador que afeta as raízes da ciência da computação: dependendo da regra, "um algoritmo para determinar se chegará a 1 não existe em princípio". Existe até a possibilidade de a própria Conjectura de Collatz ser uma proposição improvável dentro da estrutura da matemática moderna.

Mas, em 2019, finalmente ocorreu um grande avanço (breakthrough).
Um dos maiores matemáticos geniais da era moderna, **Terence Tao**, usando equações diferenciais parciais e métodos da teoria das probabilidades, provou que "(embora não se possa dizer estritamente todos) **para quase todos os valores iniciais, a sequência de Collatz acaba atingindo um valor muito menor do que o número original**".

Esta não é uma prova completa de que "tudo vira 1", mas surpreendeu o mundo matemático como **o marco histórico mais próximo da verdade sobre a Conjectura de Collatz alcançado pela humanidade**.

---

## Quem foi o Sr. Collatz?

E, lendo até aqui, você deve estar pensando: "Afinal, quem é Collatz?".
Vou apresentá-lo adequadamente!

* Nome: **Lothar Collatz**
* Nacionalidade: Alemanha
* Anos de vida: 1910 a 1990
* Profissão: Matemático (atuou nas áreas de análise funcional e teoria dos números)

Ele propôs essa conjectura em 1937, e
depois disso, por mais de 80 anos, **ninguém conseguiu provar nem refutar**.

Aliás, esse problema é tão simples, mas tão profundo, que
até mesmo o grande Paul Erdős (matemático superfamoso) disse o seguinte:

> "A matemática ainda não está madura o suficiente para lidar com problemas como o de Collatz."

Ou seja, há a teoria de que a matemática da humanidade ainda não alcançou esse mistério...

---

## Não precisa de "fórmulas complicadas"

O lado bom da Conjectura de Collatz é que **qualquer um pode brincar** com ela.

Você pode fazer com papel e caneta.
Se escrever um código em Python, pode testar automaticamente.
E, ainda assim, **os matemáticos de ponta estão levando isso muito a sério**.

Isso não é emocionante?

---

## Bônus: Código para testar tudo de uma vez

Aqui está também um código para você testar vários números de uma só vez.

```python
for n in range(1, 21):
    steps = collatz(n)
    print(f"{n}: {steps} (Passos: {len(steps)-1})")
```

Isso gerará as sequências de Collatz de "1 a 20" de uma vez.

---

## Conclusão: Este mundo é mesmo misterioso

E assim é a Conjectura de Collatz.

* Apesar de ser superfácil
* Ninguém consegue provar
* É um grande problema no mundo da matemática

É basicamente um grande aglomerado de mistérios.

Até mesmo iniciantes em programação podem tentar, então não deixe de brincar com isso!

---

## Links recomendados (para os interessados)

* [Wikipedia: Conjectura de Collatz](https://pt.wikipedia.org/wiki/Conjectura_de_Collatz)
* [Artigo de Terence Tao (em inglês)](https://arxiv.org/abs/1909.03562)
* Também seria divertido criar uma versão visualizada em Python! (Farei isso se houver demanda)

---

Para aqueles que querem saber mais sobre esse tipo de tema "Matemática misteriosa × Programação",
fiquem à vontade para pedir "Conte-me mais!".
Qualquer hora dessas vou apresentar a Hipótese de Riemann, histórias sobre números primos e muito mais!

---

📮 Fim!

---
