---
title: "Autômatos e Teoria das Linguagens Formais: Os Bastidores das Expressões Regulares e a Hierarquia de Chomsky"
description: "Exploraremos profundamente os 'autômatos' e a 'teoria das linguagens formais' por trás das expressões regulares e dos compiladores de linguagens de programação, incluindo a hierarquia de Chomsky."
slug: automata-formal-language-theory
date: "2026-09-24T16:08:36+09:00"
image: eyecatch.jpg
categories:
  - computer-science
tags:
  - automata
  - formal-language
  - regex
  - algorithms
  - mathematics
---

Uma teoria grandiosa que sustenta a base da ciência da computação: os **Autômatos** (Automata) e a **Teoria das Linguagens Formais** (Formal Language Theory).

Desde as expressões regulares (Regular Expressions) que escrevemos no dia a dia, passando pelos compiladores que decifram o código-fonte das linguagens de programação, até o processamento de linguagem natural, essa teoria é a base de tudo. Neste artigo, tendo como eixo a classificação chamada Hierarquia de Chomsky (Chomsky Hierarchy), guiaremos você por esse mundo profundo onde o próprio conceito de computação é definido de forma matemática e abstrata.

---

## 1. O que é uma Linguagem Formal?

Em contraste com as "linguagens naturais" como o português ou o japonês que usamos normalmente, uma linguagem estritamente definida por regras matemáticas é chamada de **Linguagem Formal** (Formal Language). Uma linguagem formal é composta pelos seguintes elementos básicos.

### Alfabeto e Cadeia de Caracteres

Na teoria das linguagens formais, um **alfabeto** (Alphabet) é um conjunto finito e não vazio de símbolos. Geralmente, é representado pelo símbolo $ \Sigma $ (sigma).

$$
\Sigma = \{ 0, 1 \}
$$

O exemplo acima é o alfabeto do sistema binário. Uma sequência de comprimento finito de símbolos gerados a partir desse alfabeto é chamada de **Cadeia de Caracteres** (String) ou **Palavra** (Word).

O conjunto de todas as cadeias de caracteres formadas a partir do alfabeto $ \Sigma $ (incluindo a cadeia vazia $ \epsilon $) é denotado como $ \Sigma^* $ usando o Fecho de Kleene (Kleene Star).

### Definição de Linguagem

Uma linguagem formal $ L $ é definida como um subconjunto de $ \Sigma^* $. Ou seja, $ L \subseteq \Sigma^* $.

Por exemplo, "o conjunto de cadeias formadas por 0 e 1, que sempre terminam em 1" é uma linguagem. Esta linguagem $ L $ pode ser descrita da seguinte forma.

$$
L = \{ w1 \mid w \in \{ 0, 1 \}^* \}
$$

O objetivo principal da teoria das linguagens formais é esclarecer como esses conjuntos de cadeias de caracteres que podem existir infinitamente (linguagens) podem ser representados e reconhecidos por regras finitas (gramáticas) ou por máquinas com um número finito de estados (autômatos).

---

## 2. Hierarquia de Chomsky (Chomsky Hierarchy)

Em 1956, o linguista Noam Chomsky classificou as linguagens formais em 4 níveis, de acordo com a força das restrições de suas regras de produção. Esta é a **Hierarquia de Chomsky**.

A hierarquia é classificada da seguinte forma (do Tipo-0 ao Tipo-3). Quanto maior o número, mais restrita é a classe de linguagens que pode ser expressa, mas, em contrapartida, torna-se mais fácil para um computador analisá-la.

```mermaid
flowchart TD
    "Type0"["Type-0: Linguagens Recursivamente Enumeráveis\n(Máquina de Turing)"]
    "Type1"["Type-1: Linguagens Sensíveis ao Contexto\n(Autômato Linearmente Limitado)"]
    "Type2"["Type-2: Linguagens Livres de Contexto\n(Autômato com Pilha)"]
    "Type3"["Type-3: Linguagens Regulares\n(Autômato Finito)"]

    "Type0" --- "Type1"
    "Type1" --- "Type2"
    "Type2" --- "Type3"

    style "Type0" fill:#f9f9f9,stroke:#333,stroke-width:2px
    style "Type1" fill:#e9e9e9,stroke:#333,stroke-width:2px
    style "Type2" fill:#d9d9d9,stroke:#333,stroke-width:2px
    style "Type3" fill:#c9c9c9,stroke:#333,stroke-width:2px
```

1.  **Tipo-3 (Linguagens Regulares)**: Expressas por expressões regulares e reconhecíveis por autômatos finitos.
2.  **Tipo-2 (Linguagens Livres de Contexto)**: Usadas na sintaxe de linguagens de programação e reconhecíveis por autômatos com pilha.
3.  **Tipo-1 (Linguagens Sensíveis ao Contexto)**: Reconhecíveis por autômatos linearmente limitados.
4.  **Tipo-0 (Linguagens Recursivamente Enumeráveis)**: Reconhecíveis por máquinas de Turing. Todas as linguagens computáveis.

A partir do próximo capítulo, examinaremos mais a fundo essa hierarquia, de baixo para cima (a partir do Tipo-3, que possui restrições mais fortes).

---

## 3. Linguagens Regulares e Autômatos Finitos (Tipo-3)

### Autômatos Finitos (DFA / NFA)

No nível mais interno da hierarquia de Chomsky encontram-se as **Linguagens Regulares** (Regular Languages). O modelo computacional que reconhece essas linguagens é o **Autômato Finito** (Finite Automata, FA).

Entre os autômatos finitos, existem o **DFA** (Deterministic Finite Automaton), onde as transições de estado são determinísticas, e o **NFA** (Nondeterministic Finite Automaton), onde são não-determinísticas. Surpreendentemente, está provado que a classe de linguagens que ambos conseguem reconhecer é exatamente a mesma (DFA e NFA são equivalentes).

Matematicamente, um DFA é definido pela seguinte 5-tupla $ M = (Q, \Sigma, \delta, q_0, F) $.

*   $ Q $: Conjunto finito de estados
*   $ \Sigma $: Alfabeto
*   $ \delta $: Função de transição de estado ( $ \delta: Q \times \Sigma \rightarrow Q $ )
*   $ q_0 $: Estado inicial ( $ q_0 \in Q $ )
*   $ F $: Conjunto de estados de aceitação (estados finais) ( $ F \subseteq Q $ )

#### Exemplo prático: DFA que aceita cadeias contendo "101"

Considere um DFA que reconhece cadeias que contêm "101" como substring, dentro do alfabeto $ \Sigma = \{ 0, 1 \} $.

```mermaid
stateDiagram-v2
    [*] --> "q0"
    "q0" --> "q1" : "1"
    "q0" --> "q0" : "0"
    "q1" --> "q2" : "0"
    "q1" --> "q1" : "1"
    "q2" --> "q3" : "1"
    "q2" --> "q0" : "0"
    "q3" --> "q3" : "0, 1"
    "q3" --> [*]
```

Este diagrama de transição de estados pode ser implementado como um programa Python.

```python
class DFA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.alphabet = {'0', '1'}
        self.start_state = 'q0'
        self.accept_states = {'q3'}
        
        # Função de transição de estado
        self.transitions = {
            'q0': {'0': 'q0', '1': 'q1'},
            'q1': {'0': 'q2', '1': 'q1'},
            'q2': {'0': 'q0', '1': 'q3'},
            'q3': {'0': 'q3', '1': 'q3'}
        }
        
    def accepts(self, string: str) -> bool:
        current_state = self.start_state
        for char in string:
            if char not in self.alphabet:
                return False
            current_state = self.transitions[current_state][char]
        return current_state in self.accept_states

# Testes
dfa = DFA()
test_strings = ["001010", "11101", "1001", "010", "101"]

for s in test_strings:
    result = dfa.accepts(s)
    print(f"String '{s}': {'Accepted' if result else 'Rejected'}")
```

### Relação com Expressões Regulares (Teorema de Kleene)

As **Expressões Regulares** (Regular Expressions) usadas na programação são uma notação para descrever essas linguagens regulares. Stephen Kleene provou o teorema de que "uma linguagem poder ser expressa por uma expressão regular é equivalente a poder ser aceita por um autômato finito".

Os motores de expressões regulares das linguagens de programação reais (por exemplo, o módulo `re` no Python) constroem internamente um NFA a partir de um padrão de expressão regular fornecido e avaliam a cadeia de caracteres.

### Limitações do Lema do Bombeamento (Pumping Lemma)

Embora as linguagens regulares sejam muito úteis, elas têm limitações. Por exemplo, "o conjunto de cadeias de caracteres onde $ n $ letras $ a $ são seguidas por $ n $ letras $ b $" ( $ L = \{ a^n b^n \mid n \ge 0 \} $ ) não é uma linguagem regular. Os autômatos finitos não possuem memória (como pilhas) para "contar", portanto, não conseguem lembrar infinitamente quantas letras $ a $ ocorreram. O método matemático para provar isso é o **Lema do Bombeamento para Linguagens Regulares**.

---

## 4. Linguagens Livres de Contexto e Autômatos com Pilha (Tipo-2)

Para representar o balanceamento de parênteses, que não pode ser expresso por linguagens regulares, ou a sintaxe de linguagens de programação (como aninhamento de `if-else`), são necessárias as **Linguagens Livres de Contexto** (Context-Free Languages, CFL).

### Autômatos com Pilha (PDA)

O modelo computacional que reconhece as linguagens livres de contexto é o **Autômato com Pilha** (Pushdown Automaton, PDA). Um PDA é um autômato finito ao qual se adiciona uma **Pilha** ([Stack](https://kenji.blog/pt/p/c-language-pointers-memory-management-stack-heap/), uma memória do tipo último a entrar, primeiro a sair). O uso de uma pilha permite fazer coisas como "lembrar o número de parênteses abertos e consumi-los cada vez que um parêntese de fechamento aparece".

#### Exemplo prático: PDA que aceita $ a^n b^n $

Vamos implementar um PDA que aceita cadeias de caracteres contendo o mesmo número de $ a $ e $ b $ contínuos no alfabeto $ \Sigma = \{ a, b \} $.

```python
class PDA:
    def __init__(self):
        self.stack = []
        self.state = 'q0'
        
    def accepts(self, string: str) -> bool:
        self.stack = []
        self.state = 'q_a' # Estado para ler 'a'
        
        for char in string:
            if self.state == 'q_a':
                if char == 'a':
                    self.stack.append('A') # Empilha
                elif char == 'b':
                    self.state = 'q_b'
                    if not self.stack:
                        return False
                    self.stack.pop() # Desempilha
                else:
                    return False
            elif self.state == 'q_b':
                if char == 'b':
                    if not self.stack:
                        return False
                    self.stack.pop()
                else:
                    return False
                    
        # Ao terminar de ler a string, se a pilha estiver vazia, aceita
        return len(self.stack) == 0

# Testes
pda = PDA()
print("aaabbb:", pda.accepts("aaabbb")) # True
print("aabbb:", pda.accepts("aabbb"))   # False
print("ab:", pda.accepts("ab"))         # True
print("a:", pda.accepts("a"))           # False
```

### Gramática Livre de Contexto (CFG) e BNF

As regras que geram as linguagens livres de contexto são chamadas de **Gramática Livre de Contexto** (Context-Free Grammar, CFG). Uma CFG é definida por $ (V, \Sigma, R, S) $.
Aqui, $ R $ é um conjunto de regras de produção na forma de $ A \rightarrow \gamma $. ( $ A $ é um símbolo não-terminal e $ \gamma $ é uma sequência de símbolos terminais e não-terminais ).

O **BNF** (Backus-Naur Form), frequentemente visto nas especificações de linguagens de programação, é uma metalinguagem para descrever essa gramática livre de contexto. Abaixo está um exemplo de BNF que define expressões matemáticas.

```bnf
<expr>   ::= <expr> "+" <term> | <term>
<term>   ::= <term> "*" <factor> | <factor>
<factor> ::= "(" <expr> ")" | <number>
<number> ::= "0" | "1" | "2" | ... | "9"
```

Na fase de **Análise Sintática** (Parsing) de um compilador, um algoritmo (como analisadores LL ou analisadores LR) que aplica o princípio do PDA verifica se a sequência de tokens gerada pelo analisador léxico segue essa gramática livre de contexto, e constrói uma Árvore de Sintaxe Abstrata (AST).

---

## 5. Linguagens Sensíveis ao Contexto e Autômatos Linearmente Limitados (Tipo-1)

Embora as linguagens livres de contexto possam representar a maior parte da sintaxe de uma linguagem de programação, elas não conseguem representar restrições dependentes do contexto ao redor (restrições semânticas), como "apenas variáveis declaradas podem ser usadas". Quem lida com isso são as **Linguagens Sensíveis ao Contexto** (Context-Sensitive Languages, CSL).

### Autômato Linearmente Limitado (LBA)

Quem reconhece as linguagens sensíveis ao contexto é o **Autômato Linearmente Limitado** (Linear Bounded Automaton, LBA). O LBA é um tipo de máquina de Turing, mas possui a característica de que o comprimento da sua fita é limitado a um tamanho proporcional (linear) ao comprimento da cadeia de caracteres de entrada.

Um exemplo típico de uma linguagem sensível ao contexto é $ L = \{ a^n b^n c^n \mid n \ge 1 \} $. Como um PDA tem apenas uma pilha, ele consegue igualar a quantidade de $ a $ e $ b $, mas não a quantidade de $ c $ que os segue (porque ele consome os elementos da pilha ao contar os $ a $). Como o LBA pode se mover para frente e para trás na fita, ele consegue reconhecer essa linguagem.

Acredita-se que as linguagens naturais (linguagens humanas) geralmente são mais complexas que as linguagens livres de contexto e possuem propriedades mais próximas das linguagens sensíveis ao contexto.

---

## 6. Linguagens Recursivamente Enumeráveis e Máquinas de Turing (Tipo-0)

O último nível a se chegar são as **Linguagens Recursivamente Enumeráveis** (Recursively Enumerable Languages) e a **Máquina de Turing** ([Turing Machine](https://kenji.blog/pt/p/turing-machine-computability/)).

### Máquina de Turing: O Modelo Definitivo de Computação

A Máquina de Turing, proposta por Alan Turing em 1936, possui uma capacidade computacional teoricamente equivalente aos limites de qualquer computador moderno (computadores com arquitetura de von Neumann).

A máquina de Turing é composta por uma "fita" infinita, um "cabeçote" que se move para a esquerda e para a direita enquanto lê e escreve na fita, e um número finito de "estados".

```mermaid
flowchart LR
    subgraph "Tape"
        direction LR
        "T1"["..."] --- "T2"["0"] --- "T3"["1"] --- "T4"["1"] --- "T5"["0"] --- "T6"["..."]
    end
    "Head"(("Head")) --> "T3"
    "State"["State: q_read\n(Finite Control)"] --- "Head"
```

### O Problema da Parada ([Halting Problem](https://kenji.blog/pt/p/turing-machine-computability/))

Uma das descobertas mais importantes no contexto das máquinas de Turing é a existência da **Incomputabilidade** (Undecidability).
O famoso **Problema da Parada** diz que "não existe nenhum programa (algoritmo) que, dado um programa qualquer e sua entrada, possa determinar se esse programa irá parar em algum momento ou cairá num loop infinito".

Isso indica um limite matemático de que, independentemente de quão poderosa seja a IA ou o computador que criarmos, "nunca será possível criar uma ferramenta de análise estática perfeita que detecte automaticamente e com antecedência todos os bugs e loops infinitos".

---

## 7. A Intersecção entre o Desenvolvimento de Software Moderno e a Teoria das Linguagens Formais

As teorias que vimos até agora não estão, de forma alguma, restritas a uma torre de marfim acadêmica. Elas estão ativas em todas as partes da engenharia de software moderna.

1.  **Geração Automática de Analisadores Léxicos (Lexer)**: Ferramentas como `Lex` e `Flex` convertem expressões regulares escritas por desenvolvedores em um DFA e geram automaticamente um código C de alta velocidade.
2.  **Geração Automática de Analisadores Sintáticos (Parser)**: Ferramentas como `Yacc` e `Bison` geram automaticamente um analisador LR (uma aplicação do PDA) a partir do BNF (gramática livre de contexto) escrito pelos desenvolvedores.
3.  **Parsing de JSON e XML**: A validação e o parsing desses formatos de dados também são baseados nos algoritmos da teoria das linguagens formais.
4.  **Destaque de Sintaxe (Syntax Highlighting) de Editores**: Os IDEs conseguem colorir o código de forma rápida porque, nos bastidores, um autômato finito está em operação.

### A Armadilha dos Motores Regex (Catastrophic Backtracking)

Os motores de expressões regulares embutidos em muitas linguagens de programação ([Java](https://kenji.blog/pt/p/programming-languages-history-paradigm-evolution/), Python, Ruby, JavaScript, etc.) não são DFAs puros e teóricos, mas sim implementados com base em um NFA com retrocesso (backtracking engine).

Por causa disso, se você fornecer uma cadeia de caracteres astuta a um padrão específico de expressão regular (ex.: `(a+)+$`), a complexidade de tempo explode exponencialmente, o que pode causar uma vulnerabilidade chamada **ReDoS** (Regular Expression Denial of [Service](https://kenji.blog/pt/p/kubernetes-k8s-architecture-pod-service-ingress/)), onde o sistema congela. Se você conhecer a teoria, poderá pensar logicamente por que o retrocesso (backtracking) ocorre e como reescrever o padrão para reduzi-lo a um processamento seguro equivalente a um DFA.

---

## Resumo: A Estética da Abstração

Os **Autômatos e a Teoria das Linguagens Formais** são o ápice da abstração para um modelo matemático puro, que elimina completamente a estrutura física do computador (CPU e memória) e questiona "o que é computação" e "o que é linguagem".

*   **Tipo-3 (DFA)**: Máquina sem memória (Expressões regulares)
*   **Tipo-2 (PDA)**: Máquina com memória de pilha (Análise sintática)
*   **Tipo-1 (LBA)**: Máquina com fita finita
*   **Tipo-0 (TM)**: Máquina com fita infinita (Computador universal)

O código-fonte que escrevemos todos os dias é decomposto do Tipo-2 (sintaxe) para o Tipo-3 (léxico) por uma multidão de autômatos gigantescos chamados compiladores, para finalmente ser traduzido em linguagem de máquina.

Mesmo que os frameworks superficiais e as tendências de linguagens mudem, essa sólida base matemática que persiste desde a década de 1950 nunca mudará. De vez em quando, quando você se deparar com um quebra-cabeça complexo de expressões regulares ou tiver a oportunidade de escrever um novo parser, que tal refletir sobre as grandes teorias de Turing e Chomsky que estão por trás de tudo isso?
