---
title: "A Conjectura ABC e a IUT: uma prova reivindicada e um debate em aberto"
date: "2026-09-14T13:00:00+09:00"
lastmod: 2026-11-23
slug: "abc-conjecture"
image: "eyecatch.jpg"
categories: ["mathematics", "science"]
tags: ["ABC Conjecture", "Number Theory", "IUT Theory", "Shinichi Mochizuki"]
draft: false
description: "Uma introdução à conjectura ABC, à prova que Shinichi Mochizuki afirma obter com a IUT, à publicação na PRIMS e ao debate matemático ainda sem resolução."
---

## O que afirma a conjectura ABC

Sejam $a,b,c$ inteiros positivos coprimos dois a dois e tais que $a+b=c$. O **radical** de um inteiro positivo $n$ é o produto de seus divisores primos distintos:

$$\operatorname{rad}(n)=\prod_{p\mid n}p$$

Por exemplo, $\operatorname{rad}(2^3\cdot3^2)=6$. O radical ignora os expoentes dos fatores primos e, por isso, pode ser muito menor do que o próprio inteiro.

A conjectura ABC afirma que, para todo $\varepsilon>0$, existe uma constante $K_\varepsilon$ tal que todo triplo desse tipo satisfaz

$$c\le K_\varepsilon\operatorname{rad}(abc)^{1+\varepsilon}.$$

A constante pode depender de $\varepsilon$. Joseph Oesterlé e David Masser formularam a conjectura em 1985. Ela expressa uma forte restrição entre a adição e a fatoração em primos; não é a regra simples de que fatores primos pequenos de $a$ e $b$ necessariamente forcem um fator primo grande em $c$.

## A prova reivindicada por Mochizuki via IUT

Em 2012, Shinichi Mochizuki, da Universidade de Kyoto, publicou trabalhos que apresentam a teoria de Teichmüller interuniversal (IUT) como um novo arcabouço para problemas de geometria diofantina, incluindo a conjectura ABC. A IUT é uma teoria muito técnica sobre objetos aritméticos, como curvas elípticas sobre corpos de números, e reúne ideias relacionadas à teoria de Teichmüller, à teoria de Hodge–Arakelov e à geometria anabeliana. Conceitos como teatros de Hodge e a rede log-teta são usados para comparar dados aritméticos entre estruturas. Resumi-la como “separar a adição e a multiplicação em universos distintos” seria enganoso.

Mochizuki afirma que a conjectura ABC decorre da IUT. Os quatro artigos passaram por um longo processo de avaliação e foram publicados em uma edição especial de 2021 de *Publications of the Research Institute for Mathematical Sciences* (PRIMS). A publicação é um fato importante, mas não estabelece por si só consenso matemático nem encerra a controvérsia.

## O que continua em disputa

Em um relatório de 2018, Peter Scholze e Jakob Stix argumentaram que existe uma lacuna em uma etapa central — a passagem do Teorema 3.11 ao Corolário 3.12 de IUT III, usada no caminho até a desigualdade ABC. Mochizuki rejeita a crítica por considerá-la baseada em uma interpretação equivocada da teoria e voltou a expor sua posição em um relatório de outubro de 2025. Este trecho resume as posições declaradas pelos autores; não verifica de forma independente a prova da IUT.

Uma explicação cuidadosa distingue, portanto, três pontos: os artigos da IUT foram publicados na PRIMS; Mochizuki afirma que eles provam ABC; e a divergência dos matemáticos sobre o argumento central não foi resolvida. Não é adequado apresentar a conjectura ABC como um teorema amplamente estabelecido.

## Relação com o Último Teorema de Fermat

Se for verdadeira, a conjectura ABC implica o Último Teorema de Fermat: não há soluções inteiras positivas para $x^n+y^n=z^n$ quando $n\ge3$. Trata-se de uma consequência condicional, não de afirmar que o teorema de Fermat continua sem prova; Andrew Wiles e outros já o demonstraram.

Suponha que existisse uma solução $x,y,z$ coprima dois a dois. Para todo inteiro positivo $k$, $(x^{nk},y^{nk},z^{nk})$ também seria um triplo de soma coprimo. Seu radical permaneceria constante, $\operatorname{rad}(x^{nk}y^{nk}z^{nk})=\operatorname{rad}(xyz)$, enquanto $z^{nk}$ cresceria sem limite. Assim, haveria infinitos triplos que violariam a cota ABC para qualquer $\varepsilon>0$ fixo, uma contradição.

## Referências

- [Formulação padrão de ABC (Jordan S. Ellenberg)](https://arxiv.org/abs/math/9909098)
- [Edição especial da PRIMS sobre IUT, 2021](https://ems.press/journals/prims/issues/1507)
- [Relatório de Scholze e Stix (2018)](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf)
- [Relatório de IUT de Mochizuki (outubro de 2025)](https://www.kurims.kyoto-u.ac.jp/~motizuki/IUT-report-2025-10.pdf)
- [Panorama da IUT (Mochizuki, 2012)](https://www.kurims.kyoto-u.ac.jp/~motizuki/Panoramic%20Overview%20of%20Inter-universal%20Teichmuller%20Theory.pdf)

Esta é uma breve introdução à conjectura e à controvérsia pública; não reconstrói nem avalia a prova da IUT.
