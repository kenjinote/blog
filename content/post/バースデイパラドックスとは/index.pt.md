---
title: "O que é o Paradoxo do Aniversário?"
slug: "バースデイパラドックスとは"
date: 2024-04-02T01:20:50+09:00
tags: ["Matemática", "Paradoxo"]
draft: false
math: true
image: "img.png"
categories: ["Matemática, Criptografia, Quântica"]
---

## Você conhece o Paradoxo do Aniversário?

Vou contar uma história um pouco intrigante.
Para a "probabilidade de haver pessoas com o mesmo aniversário" ser alta, quantas pessoas você acha que precisam se reunir?

Por exemplo, um ano tem 365 dias, então quando dizem que "se 23 pessoas se reunirem, a probabilidade de alguém compartilhar o aniversário é superior a 50%"... de alguma forma, parece ir contra a intuição.

Mas isso **realmente é mais de 50%.** 

---

## Por que isso acontece?

Esse fenômeno é chamado de "Paradoxo do Aniversário".
O nome diz "paradoxo" (contra-senso), mas há uma razão matemática sólida.

Quando o número de pessoas é "n", **a probabilidade de ninguém compartilhar o aniversário** é calculada pela seguinte fórmula:

```
P(ninguém compartilha) = 365/365 × 364/365 × 363/365 × ... × (365 - n + 1)/365
```

Subtraindo isso de 1, obtemos a "probabilidade de compartilhar com alguém".

---

## Observando os resultados...

| Número de Pessoas | Probabilidade de haver pessoas com o mesmo aniversário |
| ----------------- | ------------------------------------------------------ |
| 10 pessoas        | Cerca de 11.7%                                         |
| 20 pessoas        | Cerca de 41.1%                                         |
| 23 pessoas        | **Cerca de 50.7% (Preste atenção aqui!)** |
| 30 pessoas        | Cerca de 70.6%                                         |
| 70 pessoas        | **Incríveis 99.9%!** |

Em outras palavras, com apenas **23 pessoas** , há mais de 50% de chance de alguém compartilhar o aniversário.
Isso se aplica facilmente a uma sala de aula ou a uma reunião de trabalho.

---

## Resumo: A diferença entre a intuição e a matemática é fascinante

O "Paradoxo do Aniversário" é um exemplo interessante de como nossa intuição e a probabilidade matemática real divergem.
Saber sobre coisas assim pode animar pequenas conversas e quizzes!

---

## Links de Referência

* [Paradoxo do Aniversário (Wikipedia)](https://ja.wikipedia.org/wiki/%E8%AA%95%E7%94%9F%E6%97%A5%E3%81%AE%E3%83%91%E3%83%A9%E3%83%89%E3%83%83%E3%82%AF%E3%82%B9)
