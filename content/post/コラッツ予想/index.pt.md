---
title: "コラッツ予想"
slug: "コラッツ予想"
date: 2025-07-15T18:03:03+09:00
tags: ["コラッツ予想", "数学", "プログラミング", "アルゴリズム"]
draft: false
image: "img.png"
categories: ["数学・暗号・量子"]
---

# "É verdade que qualquer número termina em 1?" ── Brincando com a Conjectura de Collatz

Olá! Aqui é o kenji.

De repente, se você ouvir "uma regra em que qualquer número finalmente se torna 1",
não parece um pouco estranho?

> Por exemplo, 19, 87 ou até 1000000.
> Se você manipular os números de acordo com uma regra simples, por algum motivo, no final converge para "1".

Essa história de sonho é a ** Conjectura de Collatz (Collatz Conjecture) **.

---

## Afinal, o que é a Conjectura de Collatz?

Primeiro, vou apresentar as regras.

* Início: Escolha qualquer ** número inteiro positivo **.
* Operação:

    * Se for par → reduza pela metade (n → n / 2)
    * Se for ímpar → multiplique por 3 e adicione 1 (n → 3n + 1)

Repetindo isso várias vezes, é uma conjectura de que ** qualquer número finalmente chegará a 1 **.

Por exemplo, começando com `6`:

```
6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
```

Tornou-se "1" direitinho. Bem-vindo de volta!

---

## Vamos fazer isso com código: Collatz em Python

Bem, nessas horas, é mais rápido testar com código!
Vamos imprimir a "Sequência de Collatz" em Python.

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

# Exemplo: começar com 19
print(collatz(19))
```

Ao executar:

```
[19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
```

Chega a 1 brilhantemente.
Embora faça muitos desvios, no final chega ao objetivo!


A propósito, se você começar com 29, também chegará a 1 da mesma forma.

```python
print(collatz(29))
```

Ao executar:

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

Uau, leva 111 passos!

E também, há cenas em que infla para mais de 9000 no caminho.
É um padrão em que você faz um desvio insano antes de chegar ao fim.

---

## E então, o que é tão incrível sobre isso?

O que é incrível sobre essa conjectura é,

> ** Embora não tenha sido provado, parece que qualquer número que você tentar se tornará 1 **

É isso.

Eh? Então, e 1 trilhão, ou 10 quatrilhões...?

Para quem pensou assim, muito perspicaz.
Na verdade, usando computadores, foi confirmado até cerca de "2 elevado a 68",
e ** todos chegaram a 1 **. Inacreditável...

Mas, ** não foi provado teoricamente que "todos serão assim" **.
Este é o chamado "problema não resolvido" no mundo da matemática.

---

## Quem é o Sr. Collatz?

Então, lendo até aqui, você provavelmente está pensando "Afinal, quem é Collatz?".
Vou apresentá-lo adequadamente!

* Nome: ** Lothar Collatz (Lothar Collatz) **
* Nacionalidade: Alemanha
* Ano de nascimento: 1910 a 1990
* Título: Matemático (ativo nos campos da análise funcional e teoria dos números)

Ele propôs essa conjectura em 1937,
e desde então, por mais de 80 anos, ** ninguém foi capaz de prová-la ou refutá-la **.

A propósito, este problema é tão simples, mas tão profundo que
até o Paul Erdős (matemático super famoso) disse algo assim.

> "A matemática ainda é imatura para lidar com Collatz"

Em outras palavras, a teoria de que a matemática da humanidade ainda não alcançou este mistério...

---

## "Fórmulas matemáticas difíceis" não são necessárias

A coisa boa sobre a Conjectura de Collatz é que ** qualquer um pode jogar **.

Você pode fazer isso com papel e caneta.
Se você escrever o código em Python, pode testá-lo automaticamente.
E mesmo assim, ** os matemáticos de ponta estão levando isso a sério **.

De alguma forma, não é emocionante?

---

## Bônus: Código para testar tudo de uma vez

Também postarei um código para testar vários números ao mesmo tempo.

```python
for n in range(1, 21):
    steps = collatz(n)
    print(f"{n}: {steps} (Passos: {len(steps)-1})")
```

Isso nos dará as Sequências de Collatz de "1 a 20" de uma só vez.

---

## Conclusão: Este mundo é, afinal, misterioso

Então, essa é a Conjectura de Collatz.

* Embora seja super simples
* Ninguém pode provar
* Um grande problema no mundo da matemática

Era uma existência como uma massa de mistérios.

Até mesmo iniciantes em programação podem tentar, então por favor, brinque com isso!

---

## Links recomendados (para os interessados)

* [Wikipedia: Conjectura de Collatz](https://ja.wikipedia.org/wiki/コラッツ予想)
* [Artigo de Terence Tao (Inglês)](https://arxiv.org/abs/1909.03562)
* Também é divertido criar uma versão visualizada em Python! (Farei uma se houver demanda)

---

Se você quiser saber mais sobre esse tipo de material de "Matemática misteriosa x Programação",
fique à vontade para solicitar e dizer "Me ensine mais".
Eventualmente, apresentarei várias coisas, como a Hipótese de Riemann e números primos!

---

📮Fim!

---
