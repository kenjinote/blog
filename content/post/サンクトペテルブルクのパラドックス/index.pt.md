---
title: 'Paradoxo de São Petersburgo: Quanto você pagaria por uma aposta com valor esperado "infinito"?'
slug: 'st-petersburg-paradox'
description: 'Uma aposta que matematicamente deveria lhe render "lucro infinito". No entanto, ninguém pagaria uma grande quantia por ela na realidade. Explicamos esse paradoxo histórico que destacou a divergência entre a teoria das probabilidades e a psicologia humana (utilidade), tornando-se a base da economia moderna.'
date: '2026-09-10T05:00:00+09:00'
image: 'img/st_petersburg.jpg'
math: true
mermaid: true
categories:
  - 'Paradoxos Matemáticos'
  - 'Teoria das Probabilidades'
tags:
  - 'Paradoxo'
  - 'Valor Esperado'
  - 'Economia'
  - 'Bernoulli'
---

## 1. A aposta dos sonhos com valor esperado "infinito"

Enquanto você caminha por um cassino, um crupiê o convida para um novo jogo de cara ou coroa:

**【Regras do Jogo】**
1. Você paga uma taxa de inscrição para começar o jogo.
2. Uma moeda é lançada. Se der **Cara**, o prêmio dobra e a moeda é lançada novamente.
3. Se der **Coroa**, o jogo termina. Você recebe o prêmio acumulado até aquele momento.

O prêmio inicial começa em 2 dólares.
- Se der Coroa no 1º lançamento, você ganha **2 dólares** e o jogo termina.
- Se der Cara no 1º e Coroa no 2º, você ganha **4 dólares** e termina.
- Se der Cara no 1º e 2º, e Coroa no 3º, você ganha **8 dólares** e termina.
- ...A partir daí, enquanto der Cara, o prêmio dobra infinitamente: 16 dólares, 32 dólares, 64 dólares...

```mermaid
graph TD
    Start["Início do Jogo"] --> Toss1{"1º Lançamento"}
    
    Toss1 -->|Coroa (1/2)| End1["Fim: Ganha 2 dólares"]
    Toss1 -->|Cara (1/2)| Toss2{"2º Lançamento"}
    
    Toss2 -->|Coroa (1/2)| End2["Fim: Ganha 4 dólares"]
    Toss2 -->|Cara (1/2)| Toss3{"3º Lançamento"}
    
    Toss3 -->|Coroa (1/2)| End3["Fim: Ganha 8 dólares"]
    Toss3 -->|Cara (1/2)| Toss4{"..."}
    
    Toss4 -.->|Quanto mais consecutivas| Infinite["O prêmio dobra infinitamente!"]
```

Agora, uma pergunta para você:
**Se a taxa de inscrição deste jogo fosse de "10.000 dólares", você participaria?**

Provavelmente, a maioria das pessoas responderia "não participo". Isso porque, em metade das vezes, o primeiro lançamento será coroa e você receberá apenas 2 dólares, sofrendo um grande prejuízo.

No entanto, se calcularmos fielmente usando a teoria das probabilidades da matemática (valor esperado), um fato surpreendente é revelado. **Matematicamente, seja a taxa de inscrição de 10.000 ou 1 milhão de dólares, você deveria fazer um empréstimo com todo o seu patrimônio para participar deste jogo.**

Mas por que será?

---

## 2. Vamos calcular o valor esperado

Um indicador matemático para julgar se uma aposta é "vantajosa ou desvantajosa" é o **"valor esperado"**.
O valor esperado é um número que representa "quanto você ganharia em média por rodada se repetisse o jogo muitas vezes". A fórmula é **a soma de todos os "(prêmio ganho) × (sua probabilidade)"**.

Vamos calcular o valor esperado do nosso jogo.

- **Probabilidade de dar Coroa na 1ª vez:** $\frac{1}{2}$
  O prêmio é $2$ dólares.
  Contribuição para o valor esperado = $2 \times \frac{1}{2} = 1$ dólar

- **Probabilidade de dar Coroa na 2ª vez:** A sequência é Cara, Coroa, então $\frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$
  O prêmio é $4$ dólares.
  Contribuição para o valor esperado = $4 \times \frac{1}{4} = 1$ dólar

- **Probabilidade de dar Coroa na 3ª vez:** A sequência é Cara, Cara, Coroa, então $(\frac{1}{2})^3 = \frac{1}{8}$
  O prêmio é $8$ dólares.
  Contribuição para o valor esperado = $8 \times \frac{1}{8} = 1$ dólar

- **Probabilidade de dar Coroa na $n$-ésima vez:** $(\frac{1}{2})^n$
  O prêmio é $2^n$ dólares.
  Contribuição para o valor esperado = $2^n \times (\frac{1}{2})^n = 1$ dólar

Ou seja, não importa em que rodada termine, o valor esperado de cada padrão é **sempre "1 dólar"**.
Como o jogo pode continuar infinitamente, a soma de todos esses valores esperados fica assim:

$$ \text{Valor Esperado Total} = 1 + 1 + 1 + 1 + \dots = \infty \text{ (infinito)} $$

A resposta calculada pela matemática foi que **"o valor esperado deste jogo é infinito"**.
Como o valor esperado é infinito, independentemente de quão alta seja a taxa de inscrição, logicamente essa é uma "aposta lucrativa".

Este é o **"Paradoxo de São Petersburgo"**, proposto por Nicolaus Bernoulli em 1713.
Há uma forte contradição entre o resultado matemático correto (o jogo tem valor infinito) e a intuição humana realista (não queremos pagar mais do que alguns dólares).

---

## 3. A descoberta da "Utilidade" que resolve a divergência entre matemática e humanos

Quem resolveu este paradoxo foi o primo de Nicolaus, o genial matemático Daniel Bernoulli. (Recebeu este nome porque ele apresentou o artigo na Academia de Ciências de São Petersburgo.)

Daniel se aprofundou na psicologia humana.
Ele pensou: **"As pessoas não julgam as coisas pelo 'valor absoluto' do dinheiro, mas pela 'satisfação (utilidade)' que o dinheiro proporciona"**.

A isso chamamos de **"Lei da Utilidade Marginal Decrescente"**.

### O valor do dinheiro diminui de acordo com a quantidade que você possui
Por exemplo, quando você está com muita sede no deserto, o 1º copo de água tem um valor (satisfação) pelo qual você pagaria até "10.000 dólares". No entanto, ao beber o 2º, o 3º, o valor de cada copo de água cai vertiginosamente. No 10º copo, você diria "não quero nem de graça".

Com o dinheiro é a mesma coisa.
- Para uma pessoa com zero economias, ganhar "10.000 dólares" tem um valor imenso que pode salvar sua vida.
- No entanto, para Elon Musk, com um patrimônio de bilhões, ganhar "10.000 dólares" tem apenas o valor (satisfação) equivalente a encontrar uma moeda no chão.

Ou seja, mesmo que o prêmio aumente infinitamente de 2 dólares $\rightarrow$ 4 dólares $\rightarrow$ 8 dólares $\rightarrow$ 16 dólares..., **a "alegria (utilidade)" sentida pelas pessoas não aumenta infinitamente de forma proporcional ao valor**.

---

## 4. Recalculando o valor esperado usando "Utilidade"

Daniel Bernoulli presumiu que "o valor (utilidade) do dinheiro sentido pelas pessoas é proporcional ao logaritmo ($\log$) do montante".

Seja o valor $x$, representamos o valor percebido (utilidade) humano $u(x)$ através de uma função logarítmica (vamos usar um modelo simples com base 2).

- Utilidade do prêmio de $2$ dólares: $\log_2(2) = 1$
- Utilidade do prêmio de $4$ dólares: $\log_2(4) = 2$
- Utilidade do prêmio de $8$ dólares: $\log_2(8) = 3$
- Utilidade do prêmio de $2^n$ dólares: $\log_2(2^n) = n$

Enquanto o montante dobra, a "alegria" humana aumenta apenas um pouco: 1, 2, 3...
Usando esta "utilidade", vamos calcular o valor esperado novamente (**utilidade esperada**).

$$ \text{Utilidade Esperada} = \sum_{n=1}^{\infty} \left( n \times \left(\frac{1}{2}\right)^n \right) $$
$$ = 1 \cdot \frac{1}{2} + 2 \cdot \frac{1}{4} + 3 \cdot \frac{1}{8} + 4 \cdot \frac{1}{16} + \dots $$

Ao calcular a soma desta série infinita, o resultado não é "infinito", mas **converge para "2".**
Se calcularmos de volta o valor em dinheiro para a utilidade "2", teremos $2^2 = 4$ dólares.

Em outras palavras, ao recalcular incorporando a psicologia humana (utilidade), chegamos a uma resposta extremamente sensata e realista: **"O valor deste jogo, na percepção humana, é de aproximadamente '4 dólares'."**
É por isso que não nos sentimos inclinados a pagar 10.000 dólares por este jogo.

---

## 5. Resumo: O paradoxo que abriu as portas da Economia

O Paradoxo de São Petersburgo foi um paradoxo inovador que provou matematicamente a divergência entre os números objetivos, chamados de "valor", e o valor subjetivo humano, chamado de "satisfação".

O conceito de "Utilidade (Utility)" proposto por Daniel Bernoulli, após 200 anos, tornou-se a base mais importante da microeconomia moderna e da engenharia financeira (como a Teoria do Portfólio).
Comportamentos como o de adquirir seguros ou diversificar investimentos podem ser todos explicados por este mecanismo psicológico humano da "utilidade marginal decrescente" (a dor de uma grande perda é muito maior do que a alegria de um grande ganho).

Um simples problema de cálculo de apostas acabou se tornando o gatilho para decifrar a mente humana e dar origem à vasta disciplina da economia.
