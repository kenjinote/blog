---
title: "FizzBuzz"
slug: "FizzBuzz"
date: 2025-04-18T00:58:11+09:00
tags: ["FizzBuzz", "Python", "Algoritmo"]
draft: false
image: "img.png"
categories: ["Programação"]
---

## Afinal, o que é FizzBuzz?

Olá!

Hoje eu gostaria de escrever sobre "FizzBuzz".

Tanto para aqueles que pensam "Ah, eu conheço isso!", quanto para aqueles que dizem "Já ouvi falar, mas não entendo muito bem", por favor, fiquem comigo um pouquinho. Pode ser lido em poucos minutos, e talvez você pense "Faz sentido".

---

### É verdade que "se você não consegue escrever FizzBuzz, você é um fracasso como programador"?

O FizzBuzz, em resumo, é assim.

```python
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

Sim, este é o famoso "Problema FizzBuzz".

Você analisa os números de 1 a 100 em ordem,  
se for um múltiplo de 3, exibe "Fizz", se for um múltiplo de 5, exibe "Buzz",  
se for um múltiplo de ambos, exibe "FizzBuzz" - é algo muito simples.

E, no entanto, por algum motivo, costuma ser tratado como "o teste mínimo para um programador". Aparece em entrevistas, e nas redes sociais você vê comentários do tipo "Alguém que não consegue nem escrever FizzBuzz...".

Mas, espere um minuto.

Podemos realmente dizer que "não conseguir escrever FizzBuzz = não conseguir programar"?

---

### Não é sobre poder ou não, mas se você tem o "estado" para poder

É verdade que o FizzBuzz exige compreensão da sintaxe e pensamento lógico básico. Portanto, faz sentido que seja usado para "verificar os fundamentos".

Mas, veja bem.

Se o ambiente for diferente, os resultados serão diferentes.

Por exemplo,

- Quando você está nervoso na frente de um entrevistador que acabou de conhecer
- Quando você recebe um quadro branco de repente e não tem um editor à mão
- Quando você não consegue se lembrar imediatamente de "Ei, o que é modulo?"

...Isso não acontece? Somos humanos. Eu acho que acontece.

Portanto, em vez de "conseguir escrever FizzBuzz", acho que "conseguir se colocar em um estado em que consiga escrever FizzBuzz" é, na verdade, muito mais importante.

---

### A armadilha do conselho comum de "Basta treinar e ficará tudo bem"

Quando se trata desse assunto, o conselho "Então pratique todos os dias!" tende a surgir.

É verdade que a prática repetida fará com que você o escreva com fluência, e isso em si é bom. Mas se partirmos da premissa de que "se você não conseguir escrever FizzBuzz, você é um fracasso", isso pode se transformar em mero medo.

Em outras palavras, tende a criar uma estrutura onde você sente "Eu cometi um erro = sou inútil".

Por exemplo, quando você acorda tarde, você não tende a pensar "Eu sou preguiçoso..."? Mas pode ser apenas que seu corpo estivesse cansado naquele momento.

O FizzBuzz é a mesma coisa.

---

### Dito isto, o FizzBuzz ainda é uma boa pergunta

Dito isto, o FizzBuzz não é ruim.

Em vez disso, acho que é uma pergunta muito bem elaborada. As regras são simples e é fácil de expandir. Por exemplo, se você mudá-lo assim, seu pensamento se aprofundará.

```python
for i in range(1, 101):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    print(output or i)
```

Este é um exemplo de "Você pode escrever isso mesmo sem usar if-elif-else". É meio inteligente, não é?

Em outras palavras, o FizzBuzz não trata apenas de "se você conseguiu fazer", mas também serve como ponto de partida para ver "como você o escreve" e "o quanto você entende".

---

### Por tanto

Acho que não devemos atribuir muito significado excessivo a se você consegue ou não fazer o FizzBuzz.

Mesmo que você não tenha conseguido escrever, pode ser apenas que "você não estava se sentindo bem agora", e muitas vezes você conseguirá se pensar com cuidado mais tarde.

Não se apresse, vamos avançar devagar.

O código é escrito por humanos. Porque somos humanos, às vezes esquecemos coisas e ficamos nervosos. Aceitando isso, acho que basta se pudermos avançar pouco a pouco.

Então, vamos escrever o código de maneira descontraída hoje.
