---
title: 'O que é o Crivo de Eratóstenes? Algoritmo e implementação para enumerar números primos até 1000'
slug: "Crivo de Eratóstenesを使って1000以下のNúmero Primoを列挙する方法"
tags: ["Crivo de Eratóstenes", "Números primos", "Matemática", "Rust"]
draft: false
math: true
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "Liste os 168 primos até 1000 em Rust. Entenda o início no quadrado, candidatos ímpares, limites 0 e 1, complexidade e restrições de memória."
date: 2023-04-09T12:54:24+09:00
lastmod: 2026-10-29
---

O crivo de Eratóstenes lista todos os primos até um limite superior `n`, inclusive. Aqui, programas em Rust imprimem os 168 primos menores ou iguais a 1000. O limite está incluído; 0 e 1 não são primos.

## Etapas do crivo e por que começar no quadrado

1. Aloque `n + 1` elementos booleanos para usar os índices de 0 a `n`. A versão básica inicializa todos como verdadeiros e marca 0 e 1 como falsos. Para um limite menor que 2, retorna um resultado vazio antes de acessar o índice 1.
2. Examine os candidatos `p` em ordem crescente, começando por 2. Se a marca ainda for verdadeira, `p` é primo: marque como falsos os múltiplos a partir de $p^2$, avançando de `p` em `p`. Não marque o próprio `p`.
3. Basta eliminar múltiplos para candidatos que satisfaçam $p^2\le n$, pois todo composto tem um fator primo menor ou igual à sua raiz quadrada.
4. Ao final, percorra de 2 a `n` e imprima todos os números cuja marca continua verdadeira. A faixa de saída não se limita à raiz quadrada.

Um múltiplo $kp$ menor que $p^2$, com $2\le k<p$, já foi eliminado por um fator primo de `k` menor que `p`. Isso não significa que todos os números menores já tenham sido listados.

![Animação do crivo com os números de 2 a 120](Animation_Sieb_des_Eratosthenes.gif)

Imagem: SKopp, versão atualizada por Suricata, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Animation_Sieb_des_Eratosthenes.gif), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). O arquivo não foi modificado. A ilustração vai de 2 a 120; os programas abaixo usam o limite 1000.

## Implementação básica em Rust

```rust
fn sieve(n: usize) -> Vec<usize> {
    if n < 2 {
        return Vec::new();
    }
    let len = n.checked_add(1).expect("n + 1 is too large");
    let mut is_prime = vec![true; len];
    is_prime[0] = false;
    is_prime[1] = false;

    let mut p = 2;
    while p <= n / p {
        if is_prime[p] {
            let mut multiple = p * p;
            loop {
                is_prime[multiple] = false;
                if n - multiple < p {
                    break;
                }
                multiple += p;
            }
        }
        p += 1;
    }

    (2..=n).filter(|&i| is_prime[i]).collect()
}

fn main() {
    for prime in sieve(1000) {
        println!("{}", prime);
    }
}
```

Salve como `sieve.rs` e compile com `rustc --edition=2021 sieve.rs -o sieve`. No Windows, use `sieve.exe` como nome do executável. A execução imprime 168 linhas, começando por 2 e terminando em 997. Estes exemplos foram executados com Rust 1.90.0.

`sieve(0)` e `sieve(1)` retornam um vetor vazio; `sieve(2)` retorna `[2]`. A condição `p <= n / p` garante que `p * p` só seja calculado quando o quadrado está dentro do limite. Antes de somar o próximo múltiplo, verifica-se a distância restante. Não é necessário calcular uma raiz quadrada em ponto flutuante.

## Versão que elimina apenas candidatos ímpares

Os pares maiores que 2 são compostos. Portanto, podemos marcar 2 como verdadeiro e inicializar apenas os ímpares como candidatos. Para um primo ímpar `p`, o quadrado também é ímpar; avançar a partir dele em passos de $2p$ visita somente múltiplos ímpares.

```rust
fn sieve_odd(n: usize) -> Vec<usize> {
    if n < 2 {
        return Vec::new();
    }
    let len = n.checked_add(1).expect("n + 1 is too large");
    let mut is_prime = vec![false; len];
    is_prime[2] = true;
    for i in (3..=n).step_by(2) {
        is_prime[i] = true;
    }

    let mut p = 3;
    while p <= n / p {
        if is_prime[p] {
            let step = 2 * p;
            let mut multiple = p * p;
            loop {
                is_prime[multiple] = false;
                if n - multiple < step {
                    break;
                }
                multiple += step;
            }
        }
        p += 2;
    }

    (2..=n).filter(|&i| is_prime[i]).collect()
}

fn main() {
    for prime in sieve_odd(1000) {
        println!("{}", prime);
    }
}
```

Salve esta versão em outro arquivo e compile. Ela imprime os mesmos 168 primos, retorna um resultado vazio para 0 e 1, e `[2]` para 2. Não junte as duas funções `main` no mesmo arquivo.

Esta versão pula parte do trabalho com números pares. Entretanto, inicializar como falso não garante maior velocidade. O tempo depende da inicialização, das escritas, do acesso à memória, do compilador e da máquina. Não há comparação de tempos medidos aqui. O array ainda contém `n + 1` elementos para que os índices correspondam diretamente aos números.

## Complexidade e limites de uso

No modelo RAM usual, o crivo usa tempo $O(n\log\log n)$ e espaço $O(n)$ para as marcas. São estimativas assintóticas de operações e armazenamento, não tempos medidos nem complexidade em bits para inteiros de precisão arbitrária. O exercício do crivo no [material de análise de Princeton](https://introcs.cs.princeton.edu/java/41analysis/) também apresenta esse crescimento.

Em Rust, [`bool`](https://doc.rust-lang.org/reference/types/boolean.html) ocupa um byte, e [`Vec<T>`](https://doc.rust-lang.org/std/vec/struct.Vec.html#guarantees) armazena elementos contíguos. Este `Vec<bool>` não é um array de bits compactados. A quantidade lógica de marcas é `n + 1`; os metadados do vetor, a capacidade alocada e o `Vec<usize>` retornado também exigem memória.

Se `n + 1` não puder ser representado, `checked_add` retorna `None`, e o `expect` seguinte provoca um panic. Nos demais casos, ainda é preciso dispor de memória suficiente; limites arbitrariamente grandes não são suportados. Para intervalos grandes, considere um crivo segmentado. Listar primos de um intervalo tem uma finalidade diferente de testar um único inteiro grande.
