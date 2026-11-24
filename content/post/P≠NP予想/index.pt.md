---
title: "A conjectura P ≠ NP: um problema em aberto na complexidade"
slug: "Conjectura P≠NP"
tags: ["Conjectura P≠NP", "Matemática", "Problemas Não Resolvidos"]
draft: false
categories: ["math-cryptography-quantum"]
description: "Introdução a P, NP, certificados de tamanho polinomial, SAT e à questão ainda aberta de P ser ou não igual a NP."
image: eyecatch.jpg
date: 2024-09-11T02:22:39+09:00
lastmod: 2026-11-24
---
# O que são P e NP?

**P** é a classe de problemas de decisão resolvíveis em tempo polinomial em relação ao tamanho da entrada. **NP** é a classe de problemas de decisão em que cada instância cuja resposta é sim possui um certificado (uma solução proposta) de comprimento limitado por um polinômio do tamanho da entrada e verificável em tempo polinomial. Uma solução de um problema em P também pode ser verificada em tempo polinomial; portanto, **P ⊆ NP**.

## SAT como exemplo

SAT pergunta se uma fórmula booleana dada tem uma atribuição que a torna verdadeira. Para uma instância positiva, essa atribuição é o certificado: verificar se satisfaz cada cláusula leva tempo polinomial no tamanho da fórmula. SAT, inclusive 3-SAT, é NP-completo. Assim, um algoritmo polinomial para SAT implicaria **P = NP**. NP-completo significa que todo problema de NP pode ser reduzido a esse problema em tempo polinomial.

## A questão em aberto

Ainda não se sabe se **P = NP** ou **P ≠ NP**. O Clay Mathematics Institute classifica P vs. NP como não resolvido. P≠NP é uma conjectura amplamente estudada, não um teorema provado. Em termos simples, pergunta-se se todo problema cuja solução proposta pode ser verificada eficientemente também pode ser resolvido eficientemente.

## Referências

- [Clay Mathematics Institute: P vs NP](https://www.claymath.org/millennium/p-vs-np/)
- [Stephen Cook, official problem description (PDF)](https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf)
- [MIT OpenCourseWare: NP-Completeness, Lecture 16 (PDF)](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/f2829e57caade7e7f21d765b8e7b9058_MIT6_046JS15_lec16.pdf)
