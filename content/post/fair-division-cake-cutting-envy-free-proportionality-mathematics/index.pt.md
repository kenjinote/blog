---
title: "Como dividir um bolo de forma 'justa'? A matemática da partilha livre de inveja e design de mecanismos"
date: 2026-10-14T01:00:00+09:00
draft: false
slug: "fair-division-cake-cutting-envy-free-proportionality-mathematics"
tags:
  - Matemática
  - Teoria dos Jogos
  - Teoria da Decisão
  - Algoritmos
  - Economia
categories:
  - Matemática
image: "eyecatch.jpg"
math: true
---

Seja ao repartir uma herança familiar complexa, dividir bens acumulados num divórcio litigioso ou fixar quartos e aluguel entre colegas de apartamento, a humanidade depara-se inevitavelmente com o dilema da <strong>justiça (equidade)</strong>.

A regra secular mais conhecida para duas pessoas é a clássica: *«Um corta, o outro escolhe (Cut and Choose)»*. Quem corta empenha-se em criar duas partes rigorosamente iguais para se proteger, e quem escolhe fica livre para selecionar o pedaço que mais lhe agrada.

Mas como proceder quando há <strong>três ou mais pessoas</strong> envolvidas?
E se o bolo não for homogêneo — tendo cobertura de chocolate de um lado, morangos no centro e creme de baunilha do outro — e os participantes tiverem preferências altamente assimétricas? Dividir em três volumes geometricamente idênticos provocará a revolta daquele que detesta morangos.

Existe algum algoritmo matemático rigoroso que garanta que todos fiquem plenamente satisfeitos e <strong>ninguém sinta inveja da fatia alheia</strong>?

Esse é o cerne da <strong>teoria da partilha justa (Fair Division)</strong>, amplamente conhecida como o <strong>problema da divisão do bolo (Cake-Cutting Problem)</strong>. Formulado na década de 1940 pelo matemático polonês Hugo Steinhaus, este campo transcendeu a curiosidade recreativa para se tornar uma sofisticada disciplina científica que articula teoria da medida, topologia algébrica (lema de Sperner e teoremas de ponto fixo), teoria dos jogos e ciência da computação. Em 2016, Haris Aziz e Simon Mackenzie alcançaram um marco histórico mundial ao provar o primeiro algoritmo finito e limitado sem inveja para qualquer número arbitrário $n$ de pessoas.

---

## 1. Fundamentos em teoria da medida

O bolo é formalmente modelado como um intervalo real contínuo $X = [0, 1]$ ou um subconjunto compacto mensurável de $\mathbb{R}^d$. Qualquer fatia corresponde a um elemento da $\sigma$-álgebra de Borel $\mathcal{B}(X)$.

Cada participante $i \in \{1, \dots, n\}$ possui uma medida de valor subjetiva $V_i: \mathcal{B}(X) \to [0, 1]$ não atômica, aditiva e não negativa:
1. <strong>Normalização</strong>: $V_i(X) = 1, V_i(\emptyset) = 0$.
2. <strong>Aditividade</strong>: $A \cap B = \emptyset \implies V_i(A \cup B) = V_i(A) + V_i(B)$.
3. <strong>Divisibilidade (Não-atomicidade)</strong>: A lâmina da faca pode cortar em qualquer ponto com precisão infinitesimal contínua.

Sob a hipótese de continuidade absoluta em relação à medida de Lebesgue, existe uma função de densidade de valor $v_i(x)$ tal que $V_i(A) = \int_A v_i(x) \, dx$. O ponto fulcral deste modelo é o respeito total à individualidade: cada pessoa julga o bolo unicamente através da sua própria escala de valores interna, sem interferência alheia.

---

## 2. Quatro critérios fundamentais de equidade

Para uma partição $(X_1, \dots, X_n)$ do bolo:

| Critério | Definição formal | Significado |
| :---: | :---: | :---: |
| <strong>Proporcionalidade (PROP)</strong> | $\forall i, \quad V_i(X_i) \ge \frac{1}{n}$ | Cada um recebe pelo menos $1/n$ do valor total sob a sua ótica |
| <strong>Ausência de Inveja (EF)</strong> | $\forall i, j, \quad V_i(X_i) \ge V_i(X_j)$ | Ninguém prefere a fatia de outrem à sua própria |
| <strong>Equitabilidade (EQ)</strong> | $\forall i, j, \quad V_i(X_i) = V_j(X_j)$ | Utilidades subjetivas numericamente idênticas |
| <strong>Eficiência de Pareto (PE)</strong> | Impossível melhorar alguém sem prejudicar outro | Eficiência máxima e ausência total de desperdício |

### Por que a ausência de inveja é muito superior
Para dois jogadores ($n=2$), proporcionalidade e ausência de inveja são equivalentes. No entanto, para três ou mais pessoas, a proporcionalidade não elimina conflitos!
Se Alice recebe uma fatia de valor $0,35$ ($> 0,333$), ela obteve uma parcela proporcional. Mas se Bob recebe uma fatia que Alice avalia em $0,50$, ela sentirá uma profunda e corrosiva <strong>inveja</strong>. A <strong>ausência de inveja (Envy-Freeness)</strong> é o padrão de ouro indiscutível para a pacificação social duradoura.

---

## 3. O protocolo Selfridge-Conway para 3 pessoas

Desenvolvido por volta de 1960 por John Selfridge e John Horton Conway, este brilhante algoritmo resolve a partilha para três jogadores em no máximo cinco cortes:

1. <strong>Etapa 1 (Divisão do bolo principal e apara)</strong>:
   - $P_1$ divide o bolo em três fatias iguais perante $V_1$ ($A, B, C$).
   - $P_2$ apara a fatia maior para igualá-la à segunda maior, gerando sobras $T$.
   - Escolha das fatias principais: $P_3$ escolhe primeiro, depois $P_2$ (que tem o dever de escolher a fatia aparada se $P_3$ não a escolher), e finalmente $P_1$.
   - $P_1$ recebe uma fatia intacta de valor $1/3$, ficando imune a qualquer sentimento de inveja!
2. <strong>Etapa 2 (Distribuição das sobras $T$)</strong>:
   - O jogador que ficou com a fatia aparada é denominado $T_{\text{in}}$, e o outro entre $\{P_2, P_3\}$ é denominado $T_{\text{out}}$.
   - $T_{\text{out}}$ divide as sobras $T$ em três partes iguais.
   - Ordem de escolha: $T_{\text{in}} \to P_1 \to T_{\text{out}}$.
   - <strong>O golpe de mestre do protocolo</strong>: mesmo que $T_{\text{in}}$ recebesse a totalidade das sobras $T$, o conjunto valeria no máximo $1/3$ aos olhos de $P_1$. Logo, $P_1$ jamais invejará $T_{\text{in}}$!

---

## 4. Topologia e harmonia de aluguéis: Lema de Sperner

Francis Su aplicou o <strong>lema de Sperner</strong> em 1999 para provar que quartos e aluguel compartilhado podem sempre ser precificados de forma a eliminar qualquer inveja entre colegas de casa (*Rental Harmony*). Ao triangular o simplex dos preços e rotular os vértices com as escolhas ótimas dos moradores, garante-se matematicamente a existência de um ponto de equilíbrio no qual todos escolhem quartos distintos em perfeita harmonia.

---

## 5. Bens indivisíveis e o bem-estar de Nash

Quando os bens a serem repartidos não podem ser cortados fisicamente sem destruição de valor (veículos, casas, joias), a ausência estrita de inveja é muitas vezes impossível. A ciência da computação contemporânea introduziu os conceitos de <strong>EF1 (Livre de inveja exceto por um item)</strong> e <strong>EFX</strong>.

O resultado culminante de Caragiannis et al. (2016) demonstrou que a maximização do <strong>Bem-Estar Social de Nash</strong> (o produto das utilidades individuais) satisfaz automaticamente tanto o critério EF1 quanto a Eficiência de Pareto, harmonizando eficiência econômica com justiça social.

---

## 6. Conclusão

A matemática da divisão justa nos ensina que a verdadeira equidade não consiste em uma padronização geométrica artificial, mas no respeito profundo às preferências subjetivas individuais. Mediante o desenho de regras e incentivos adequados, as diferenças de gosto tornam-se pontes para a cooperação e o benefício mútuo.
