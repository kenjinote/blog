---
title: 'O que é o "General Number Field Sieve (GNFS)", a matemática mais poderosa da humanidade que quebra a criptografia da internet?'
slug: "インターネットの暗号を破る人類最強の数学「一般数体篩法（GNFS）」とは？"
date: 2026-09-05T02:09:08+09:00
tags: ["Matemática", "Criptografia", "RSA", "GNFS"]
draft: false
image: "gnfs_two_worlds_1788542142485.jpg"
categories: ["Matemática・Criptografia・Quântica"]
---

# O que é o "General Number Field Sieve (GNFS)", a matemática mais poderosa da humanidade que quebra a criptografia da internet?

A internet que usamos todos os dias. Mensagens no LINE, YouTube, compras na Amazon etc., todas as comunicações são protegidas por "criptografia".
Atualmente, a criptografia mais utilizada em todo o mundo é a "Criptografia RSA".

O núcleo da defesa da Criptografia RSA é muito simples. Ele utiliza a propriedade matemática de que ** "a fatoração em números primos de números gigantescos não pode ser resolvida nem mesmo por computadores" ** .
Por exemplo, para "15", sabemos imediatamente que é "3 × 5", mas no instante em que isso se torna um "número de 270 dígitos", levaria centenas de milhões de anos para ser resolvido, mesmo se conectássemos todos os supercomputadores do mundo.

No entanto, os matemáticos não ficaram em silêncio. Para quebrar essa criptografia impenetrável, a humanidade criou um algoritmo (procedimento de cálculo) quase mágico chamado ** "General Number Field Sieve (GNFS)" ** .

Neste artigo, sem usar nenhum jargão técnico e apenas com o conhecimento da ** matemática do ensino fundamental (fatoração em primos, expressões algébricas, máximo divisor comum) ** , explicaremos passo a passo como esse "algoritmo mais forte da humanidade" quebra a criptografia!

---

## Capítulo 1: O objetivo da decodificação é uma "fórmula da 8ª série"

O maior golpe especial para enfrentar a gigantesca fatoração em números primos. É essa fórmula aprendida na 8ª série:

> ** $X^2 - Y^2 = (X + Y)(X - Y)$ **

Você pode pensar: "Sério que uma fórmula tão básica pode quebrar a criptografia?". No entanto, esta é a chave mestra que revela tudo.

O maior objetivo para quebrar a criptografia é, para um número gigante $N$, encontrar ** "números ($X$ e $Y$) onde o resto da divisão de $X^2$ e $Y^2$ por $N$ seja o mesmo" ** .

### Por que "ter o mesmo resto" quebra a criptografia?
Suponha que dois números, $X^2$ e $Y^2$, tenham "o mesmo resto quando divididos por $N$".
Ter o mesmo resto significa que existe uma regra onde ** a subtração "$X^2 - Y^2$" será sempre perfeitamente divisível por $N$ (será um múltiplo de $N$) ** .

Aqui, vamos supor que o número gigante $N$ usado na criptografia seja composto pela multiplicação de dois números primos secretos ($p$ e $q$) ($N = p \times q$).

Fatorando $X^2 - Y^2$, obtemos ** $(X - Y)(X + Y)$ ** .
O fato de isso ser um múltiplo de $N$ significa que, em algum lugar dessa multiplicação, os primos secretos $p$ e $q$ estão escondidos.

Aqui, um milagre acontece.
Há uma probabilidade matemática de ** 50% (metade) ** de que os dois primos $p$ e $q$ se separem em salas diferentes: ** "$p$ vai para a sala de $(X - Y)$" e "$q$ vai para a sala de $(X + Y)$" ** .

Com apenas o primo $p$ tendo entrado na sala de $(X - Y)$, vamos calcular o ** "máximo divisor comum (a maior peça em comum)" ** de $(X - Y)$ e $N$.
* Conteúdo de $(X - Y)$ = $p \times$ algum número
* Conteúdo de $N$ = $p \times q$
  A única peça comum é ** "$p$" ** !

Ou seja, no instante em que o máximo divisor comum é calculado, o número primo oculto $p$ é revelado e a criptografia é completamente decodificada. (*O máximo divisor comum pode ser calculado instantaneamente em um smartphone usando o "Algoritmo de Euclides").

** 【Pequena Coluna: Por que o quadrado? Cubo ou o dobro não servem?】 **
> Com "$2X - 2Y$", torna-se $2(X - Y)$ e há apenas uma sala, então você não pode separar os primos. Com "$X^3 - Y^3$", os tamanhos das salas ficam desequilibrados e o cálculo torna-se desnecessariamente pesado. Para separar os primos em dois, o "quadrado" que se divide perfeitamente em duas salas tem o melhor custo-benefício.

---

## Capítulo 2: Como encontrar X e Y? "Quebra-cabeça de coleta de cartas de números primos"

O objetivo é claro. No entanto, mesmo se procurarmos cegamente por "$X^2$ e $Y^2$ que têm o mesmo resto", o fim do universo chegaria antes de encontrá-los.
Então, os matemáticos criaram um método genial chamado ** "quebra-cabeça de coleta de cartas de números primos" ** .

### Step 1: Coletar apenas ouro em pó (números suaves) com uma peneira
Primeiro, prepare um número apropriado $Z$, eleve-o ao quadrado e calcule o resto $W$ ao dividi-lo por $N$.
(O mundo dos restos de $Z^2 = W$)

Fatore o resto obtido $W$ em números primos. Aqui, apenas quando aparecer ** "um $W$ composto apenas de pequenos primos como 2, 3, 5, 7, etc." ** , guarde essa equação como um "cartão premiado" e jogue-a fora se houver primos grandes misturados.
É como jogar fora as pedras grandes com uma peneira num rio para coletar apenas o pó de ouro.

### Step 2: O quebra-cabeça para tornar tudo "par"
Por exemplo, suponha que as 3 seguintes cartas de pó de ouro foram coletadas.
* Carta A: $Z_1^2 = 2^3 \times 3^1$
* Carta B: $Z_2^2 = 2^1 \times 5^1$
* Carta C: $Z_3^2 = 3^1 \times 5^1$

Vamos multiplicar todos eles.
O lado direito se torna $(2^3 \times 3^1) \times (2^1 \times 5^1) \times (3^1 \times 5^1)$,
E ao organizá-los juntos, obtemos ** "$2^4 \times 3^2 \times 5^2$" ** .

Surpreendentemente, a quantidade de números primos tornou-se "4, 2, 2", ** todos sendo um número par ** !
O fato de todos serem pares significa que se você reduzir a quantidade total pela metade, será "o quadrado de algo".
Ou seja, $(2^2 \times 3^1 \times 5^1)^2 = (60)^2$.

O lado esquerdo é $(Z_1 \times Z_2 \times Z_3)^2$, então finalmente chegamos a:
** $X = (Z_1 \times Z_2 \times Z_3)$ **
** $Y = 60$ **
O tão esperado par "$X^2 = Y^2$" está completo!

Para computadores, o quebra-cabeça de calcular se a quantidade de números primos é "par ou ímpar (0 ou 1)" é algo em que eles são muito bons, então, com este método, é possível encontrar $X$ e $Y$ em alta velocidade.

---

## Capítulo 3: A Parede do Desespero se ergue

Agora qualquer criptografia pode ser quebrada! ...ou assim pensávamos, mas um grande problema ocorreu.
Se o número da criptografia $N$ tiver até cerca de "100 dígitos", este método (chamado Sieve Quadrático) pode resolvê-lo, mas quando $N$ se torna "200 ou 300 dígitos", o $W$ que surge no meio do cálculo torna-se demasiado grande.

Quando os números ficam demasiado grandes, "números compostos apenas por pequenos números primos (pó de ouro)" deixam de aparecer. Torna-se mais difícil do que procurar lentes de contacto no deserto, e as cartas necessárias para resolver o quebra-cabeça não se acumulam de forma alguma.

Aqui, a arma final da humanidade, o ** "General Number Field Sieve (GNFS)" ** , finalmente entra em cena.

---

## Capítulo 4: A ideia mais forte da humanidade de criar "Dois Mundos"

A ideia genial do GNFS é: ** "Os números tornam-se gigantescos porque calculamos apenas no mundo real. Então, vamos criar um 'mundo dos bastidores' usando polinómios (fórmulas com letras) para dividir o peso do cálculo em dois." ** 

### A magia das fórmulas com letras
O GNFS converte o número gigante $N$ em uma fórmula com letras, utilizando um número base $m$.
Por exemplo, se $N=100$, com $m=4$, então $100 = 4^3 + 2(4^2) + 4$.
Transformamos isso numa fórmula (o mundo dos bastidores) usando a letra $x$: ** $f(x) = x^3 + 2x^2 + x$ ** .

O mais interessante dessa fórmula é que ela possui a propriedade de que ** "se substituirmos $x$ por $m$ (4 no exemplo acima), sempre podemos voltar ao número real $N$" ** .

### Procurando pó de ouro em 2 mundos simultaneamente
O GNFS cria muitos pares de números inteiros aleatórios $(a, b)$ e realiza os seguintes dois cálculos em simultâneo:
1. ** Mundo Real ** : $a - b \times m$
2. ** Mundo das Letras ** : O valor de $a - b \times x$ calculado pelas regras dos polinómios

Ao dividir o problema em dois mundos, o tamanho dos números tratados diminui (fica mais leve) drasticamente. É como dividir uma pedra gigante em dois para transformá-la em pedras mais fáceis de manusear.

Então, utilizamos uma peneira para separar e recolher apenas os pares milagrosos $(a, b)$ onde ** "tanto no mundo real quanto no mundo das letras, ambos são 'compostos apenas de pequenos primos (pó de ouro)'" ** . Esta é a origem do nome "Crivo do Corpo de Números".

### O momento em que a criptografia é finalmente quebrada
Quando dezenas de milhões de "cartões de pó de ouro" são recolhidos de ambos os mundos, o supercomputador utiliza cálculos gigantescos de matrizes para encontrar "uma combinação em que o número de primos seja todo par", tal como fizemos no Capítulo 2.

Assim que a combinação for encontrada:
* Deixe o número ao quadrado no mundo real ser ** $X^2$ **
* Deixe a fórmula quadrada criada no mundo das letras ser ** $Y(x)^2$ ** 

Por fim, substitua $x$ na fórmula de letras $Y(x)$ por $m$, saltando de volta para o mundo real e unindo-os.
Então, como que por magia matemática, a condição onde ** "os restos de $X^2$ e $Y^2$ são iguais" ** é estritamente alcançada!

O resto, como no Capítulo 1, é apenas calcular o máximo divisor comum entre $X - Y$ e $N$, e a impenetrável criptografia RSA desmoronará, revelando os primos secretos.

---

## Conclusão: A matemática não acaba

Você pode estar a pensar: "Fantástico, com o GNFS qualquer criptografia pode ser quebrada!".
No entanto, a criptografia RSA também não se deu por vencida. O que é utilizado na internet atual é um número gigantesco e monstruoso chamado "RSA-2048 (cerca de 617 dígitos)".

Por mais que o GNFS seja o algoritmo mais poderoso da humanidade, diz-se que para resolver até mesmo 270 dígitos (RSA-270), levaria milhares ou dezenas de milhares de anos, mesmo conectando computadores do mundo inteiro. Por agora, os nossos dados bancários e do LINE estão seguros.

Mas e se aparecesse uma ** "magia capaz de encontrar instantaneamente $X$ e $Y$ para qualquer número gigante" ** ?
Na verdade, a coisa mais próxima disso é o ** "Computador Quântico (Algoritmo de Shor)" ** , que está atualmente em desenvolvimento. Utilizando a natureza ondulatória da mecânica quântica, foi provado matematicamente que é possível ignorar o aborrecido quebra-cabeças da recolha de cartas e chegar à resposta de uma só vez.

A interminável batalha de inteligência entre os que criam a criptografia (defesa) e os que criam algoritmos para a quebrar (ataque).
Saber que a "fatoração em números primos" e as "fórmulas com letras" ensinadas na escola secundária são, na verdade, as armas na linha da frente da segurança global não faz com que as aulas de matemática pareçam um pouco mais interessantes?

Quem descobrirá o algoritmo mais forte do futuro poderá ser você, que está a ler este artigo!

--- 
*(※Este artigo é uma adaptação conceptual do encanto matemático da quebra de códigos para estudantes. O GNFS real é rigorosamente calculado utilizando matemática universitária avançada, tal como os grupos da classe de ideais dos corpos numéricos algébricos e homomorfismos)*
