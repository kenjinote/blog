---
slug: compressed-sensing-overview
title: "Sensing Comprimido: Como Recuperar Sinais Originais com Poucas Observações"
description: "Um tema moderno conectado a imagens médicas, astronomia e compressão de imagens."
categories: ["mathematics", "computer-science"]
tags: ["math", "signal-processing", "algorithm", "science"]
date: "2026-09-25T11:25:00+09:00"
image: eyecatch.jpg
---

# O que é Sensing Comprimido (Compressed Sensing)?

Na ciência de dados moderna e no processamento de sinais, uma das mudanças de paradigma mais revolucionárias é o "Sensing Comprimido" (Compressed Sensing / Compressive Sensing). Tradicionalmente, ao converter sinais analógicos como áudio, imagens ou ondas eletromagnéticas em dados digitais para um computador, seguíamos a lei absoluta do "Teorema de Amostragem de Nyquist-Shannon". No entanto, o sensing comprimido desafia esse senso comum e fornece uma garantia matemática surpreendente: "se o sinal atender a uma determinada condição (esparsidade), é possível recuperar o sinal original perfeitamente a partir de dados de observação muito menores do que o exigido pelo teorema de amostragem".

Neste artigo, começaremos pelos fundamentos do teorema de amostragem, abordaremos profundamente a definição matemática de esparsidade, o relaxamento para o problema de otimização $L_1$ e o núcleo do avanço teórico feito por Emmanuel Candès, Terence Tao e outros, usando fórmulas matemáticas. Além disso, cobriremos casos de aplicação, como a aceleração de ressonância magnética (MRI) e a construção de imagens de buracos negros, até o código de implementação específico usando Python, para revelar a imagem completa do sensing comprimido.

## 1. O Teorema de Amostragem de Nyquist-Shannon e suas Limitações

### Fundamentos do Teorema de Amostragem
Em meados do século 20, a base da teoria da informação foi estabelecida por Claude Shannon e Harry Nyquist através do "Teorema de Amostragem". Este teorema define as condições para converter um sinal analógico contínuo num sinal digital discreto da seguinte forma:

> **Teorema de Amostragem de Nyquist-Shannon**
> Para reconstruir perfeitamente um sinal limitado em banda por $f_{\max}$, o sinal deve ser amostrado com uma frequência de amostragem de pelo menos $2f_{\max}$ (a taxa de Nyquist).

Por exemplo, o limite superior de audição para o ouvido humano é cerca de 20 kHz. Portanto, num CD de música, a amostragem é feita a mais do que o dobro disso, a 44.1 kHz. Expressado matematicamente, se um sinal contínuo $x(t)$ tiver uma transformada de Fourier $X(f)$ e $X(f) = 0$ para $|f| > f_{\max}$, $x(t)$ pode ser perfeitamente recuperado pela seguinte fórmula de interpolação usando a função sinc:

$$ x(t) = \sum_{n=-\infty}^{\infty} x\left(\frac{n}{2f_{\max}}\right) \operatorname{sinc}\left(2f_{\max}t - n\right) $$

### Explosão de Dados e Limitações do Teorema
O teorema de amostragem é muito poderoso e é a pedra angular das comunicações digitais modernas. No entanto, com os avanços tecnológicos, a quantidade de informações capturadas por sensores aumentou explosivamente. Em imagens médicas de alta resolução (MRI ou TC), matrizes de radiotelescópios astronómicos ou sistemas de radar de banda ultra-larga, a amostragem segundo a taxa de Nyquist resulta numa quantidade enorme de dados a observar.

Como resultado, surgem os seguintes problemas:
1. **Aumento do tempo de varredura**: Na MRI, por exemplo, recolher dados leva muito tempo, impondo um fardo físico aos pacientes.
2. **Limites do hardware**: A fabricação de conversores A/D para amostrar sinais de frequência ultra-alta torna-se tecnicamente difícil ou extremamente dispendiosa.
3. **Pressão no armazenamento e comunicação de dados**: Os custos associados a guardar e transmitir enormes quantidades de dados amostrados aumentam dramaticamente.

O paradigma convencional era "amostrar massivamente e, depois, comprimir por software (como JPEG ou MP3) para descartar dados desnecessários". No entanto, levanta-se a questão: "Se, afinal, os dados vão ser descartados, será possível amostrar (sentir) diretamente apenas as informações necessárias desde o início?". O sensing comprimido tornou isso possível.

## 2. Definição Matemática de Esparsidade (Sparsity)

A condição absoluta para que o sensing comprimido funcione é a **esparsidade (sparsity)**. A esparsidade refere-se à propriedade em que "quando um sinal é transformado sob uma base apropriada (método de representação), a maior parte dos seus componentes se torna zero (ou valores muito próximos de zero)".

### Formulação de Vetores Esparsos
Considere um sinal discreto (vetor) de comprimento $N$, $\mathbf{x} \in \mathbb{R}^N$. Suponha que este sinal pode ser expresso usando uma certa matriz de base ortogonal $\mathbf{\Psi} \in \mathbb{R}^{N \times N}$ (por exemplo, a matriz da transformada de Fourier ou matriz da transformada wavelet) da seguinte forma:

$$ \mathbf{x} = \mathbf{\Psi} \mathbf{s} $$

Onde, $\mathbf{s} \in \mathbb{R}^N$ é o vetor de coeficientes na base $\mathbf{\Psi}$.
Deste vetor $\mathbf{s}$, se o número de elementos não-zero for $K$ ($K \ll N$), diz-se que $\mathbf{x}$ é **$K$-esparso ($K$-sparse)**. Matematicamente, isso é definido usando a norma $L_0$ (uma função que conta o número de elementos não-zero):

$$ \|\mathbf{s}\|_0 = K $$

### Esparsidade no Mundo Real
Surpreendentemente, muitos sinais na natureza tornam-se esparsos se escolhermos a base apropriada.
- **Imagens**: Imagens naturais não são esparsas no espaço dos pixels, mas ao aplicar uma transformada wavelet ou uma transformada discreta de cosseno (DCT), a maioria dos componentes de alta frequência aproxima-se de zero, tornando-as esparsas (este é o princípio da compressão JPEG).
- **Áudio**: Os sinais de áudio são contínuos no domínio do tempo, mas no domínio da frequência (após a transformada de Fourier), apenas alguns componentes principais de frequência (frequência fundamental e harmónicas) têm valores altos.

O sensing comprimido é uma tecnologia que utiliza esta "redundância inerente ao sinal" para efetuar a compressão de dados diretamente na fase de amostragem.

## 3. Formulação do Sensing Comprimido e a Matriz de Observação

Assumindo que o sinal é esparso, como recuperamos o sinal com poucos dados?
Considere fazer $M$ observações lineares de um sinal desconhecido $\mathbf{x} \in \mathbb{R}^N$ (com $M < N$). O processo de observação é expresso pela matriz de observação $\mathbf{\Phi} \in \mathbb{R}^{M \times N}$ da seguinte maneira:

$$ \mathbf{y} = \mathbf{\Phi} \mathbf{x} = \mathbf{\Phi} \mathbf{\Psi} \mathbf{s} = \mathbf{A} \mathbf{s} $$

Onde,
- $\mathbf{y} \in \mathbb{R}^M$: vetor de dados de observação
- $\mathbf{A} = \mathbf{\Phi} \mathbf{\Psi} \in \mathbb{R}^{M \times N}$: matriz de sensing

O nosso objetivo é recuperar o vetor de coeficientes desconhecido $\mathbf{s}$ (e, por fim, $\mathbf{x}$) a partir dos dados de observação $\mathbf{y}$ e da matriz $\mathbf{A}$.

### O Problema do Sistema Subdeterminado
No entanto, enfrentamos uma barreira matemática aqui. Visto que $M < N$ (há mais incógnitas do que equações), o sistema de equações simultâneas $\mathbf{y} = \mathbf{A} \mathbf{s}$ é um **sistema subdeterminado (underdetermined system)**, o que significa que tem um número infinito de soluções. Na álgebra linear convencional, é impossível encontrar uma solução única.

Aqui é onde utilizamos o conhecimento prévio de que "$\mathbf{s}$ é esparso (os componentes não-zero são extremamente raros)". De entre os infinitos candidatos a solução, a que for mais esparsa (tiver o menor número de componentes não-zero) tem uma elevada probabilidade de ser o sinal verdadeiro. Formulado como um problema de otimização, fica:

$$ (P_0) \quad \min_{\mathbf{s} \in \mathbb{R}^N} \|\mathbf{s}\|_0 \quad \text{subject to} \quad \mathbf{y} = \mathbf{A} \mathbf{s} $$

### Dificuldade da Otimização $L_0$
Idealmente, resolveríamos o problema $(P_0)$ acima. Contudo, sabe-se que o problema de minimização de $\|\mathbf{s}\|_0$ é matematicamente **NP-difícil (NP-hard)**. Como exige testar todas as combinações de componentes não-zero, se a dimensão $N$ for grande, nem mesmo supercomputadores modernos conseguem resolvê-lo num tempo inferior à idade do universo.

## 4. Relaxamento para o Problema de Otimização $L_1$: O Avanço de Candès e Tao

O motivo pelo qual o sensing comprimido explodiu como tecnologia prática foi o facto de ter sido dada uma prova matemática incrível de que este insolúvel problema de otimização $L_0$ podia ser substituído por um **problema de otimização $L_1$** computável, chegando **exatamente à mesma resposta** sob determinadas condições.

Entre 2004 e 2006, Emmanuel Candès, Terence Tao e David Donoho estabeleceram os fortes fundamentos teóricos para isto.

### Minimização da Norma $L_1$
Em vez da norma $L_0$, usamos a norma $L_1$, que é a soma dos valores absolutos de cada elemento do vetor.

$$ \|\mathbf{s}\|_1 = \sum_{i=1}^N |s_i| $$

Com isso, o problema sofre um "relaxamento" (relaxation) para a seguinte forma:

$$ (P_1) \quad \min_{\mathbf{s} \in \mathbb{R}^N} \|\mathbf{s}\|_1 \quad \text{subject to} \quad \mathbf{y} = \mathbf{A} \mathbf{s} $$

O problema de minimização $L_1$ é um tipo de problema de otimização convexa, pelo que algoritmos existentes altamente eficientes, como a Programação Linear (Linear Programming), podem ser usados para calcular a solução exata em tempo polinomial.

### Porquê $L_1$? (Intuição Geométrica)
Porquê a norma $L_1$ e não a norma $L_2$ (método dos mínimos quadrados)? Isto pode ser entendido de forma geométrica.
A restrição $\mathbf{y} = \mathbf{A}\mathbf{s}$ forma um hiperplano no espaço de alta dimensão. A minimização da norma equivale a expandir uma curva de nível (bola) centrada na origem e encontrar o ponto onde esta toca pela primeira vez o hiperplano.

- **Bola $L_2$ ($\|\mathbf{s}\|_2 \le R$)**: A sua forma é uma esfera suave. O ponto onde toca no hiperplano ficará, na maioria das vezes, longe de todos os eixos coordenados. Consequentemente, a solução obtida é um vetor "denso" com todos os elementos diferentes de zero.
- **Bola $L_1$ ($\|\mathbf{s}\|_1 \le R$)**: A sua forma é um poliedro (como um losango ou octaedro) e possui muitos "cantos (vértices)". Esses cantos estão localizados nos eixos das coordenadas. Ao pressionar o hiperplano, a probabilidade de ele tocar na "esquina" é alta. Tocar num canto significa que os valores noutros eixos coordenados serão zero, o que resulta numa solução esparsa.

### RIP (Restricted Isometry Property: Propriedade da Isometria Restrita)
Candès e Tao introduziram o conceito de **RIP (Propriedade da Isometria Restrita)** como condição suficiente para a minimização $L_1$ coincidir com a minimização $L_0$.
Uma matriz de sensing $\mathbf{A}$ satisfaz a RIP de ordem $K$ se, para qualquer vetor $K$-esparso $\mathbf{s}$, existir uma constante pequena $\delta_K \in (0,1)$ que cumpra a seguinte desigualdade:

$$ (1 - \delta_K) \|\mathbf{s}\|_2^2 \le \|\mathbf{A}\mathbf{s}\|_2^2 \le (1 + \delta_K) \|\mathbf{s}\|_2^2 $$

Intuitivamente, esta é a propriedade pela qual "a matriz $\mathbf{A}$ preserva o comprimento de qualquer vetor esparso (quase) inalterado". Candès e Tao provaram brilhantemente que se $\mathbf{A}$ satisfizer certas condições RIP, a solução de $(P_1)$ numa situação sem ruído coincide perfeitamente com a solução de $(P_0)$.

Ainda de forma mais prática, foi demonstrado que ao utilizar **matrizes aleatórias (matrizes de números aleatórios de distribuições gaussianas ou de Bernoulli)** como matriz de observação $\mathbf{\Phi}$, estas satisfazem as condições RIP com alta probabilidade. Por outras palavras, "amostrar aleatoriamente" é a estratégia de amostragem mais eficiente e universal no sensing comprimido.

Ficou provado que o número de observações necessárias $M$ em relação ao comprimento do sinal $N$ e a esparsidade $K$ exige uma ordem de grandeza de apenas:

$$ M \ge C \cdot K \log\left(\frac{N}{K}\right) $$
($C$ é uma constante)

Isto significa que, em comparação com as $N$ observações necessárias pelo teorema da amostragem, são necessárias muito menos observações (dependendo de $K$).

## 5. Casos de Aplicação de Sensing Comprimido

A teoria do sensing comprimido revolucionou vários campos da engenharia de informação e da física.

### 1. Aceleração de MRI (Imagem por Ressonância Magnética)
Um dos casos mais bem-sucedidos de aplicação comercial é a MRI. A MRI utiliza um forte campo magnético para obter imagens de cortes transversais do corpo humano, mas existem limitações físicas na recolha de dados (dados no domínio da frequência chamados de espaço-k), o que exige tempo.
Permanecer imóvel durante longos períodos é difícil, seja para pacientes pediátricos ou quando se tiram imagens de órgãos que se movem, como o coração. Ao aplicar sensing comprimido à MRI, os dados recolhidos no espaço-k são aleatoriamente rarefeitos (subamostrados), permitindo com êxito reduzir o tempo de varrimento para uma fração do método tradicional. Atualmente, os principais fabricantes de equipamentos médicos, como Siemens e GE, vendem aparelhos de MRI que vêm equipados de fábrica com a tecnologia de sensing comprimido.

### 2. Imagens de Buracos Negros (Telescópio do Horizonte de Eventos)
Em 2019, a equipa de investigação internacional "Telescópio do Horizonte de Eventos (EHT)" obteve a primeira imagem de uma sombra de um buraco negro na história. Para criar um telescópio virtual gigante do tamanho da Terra, integraram-se dados de radiotelescópios dispersos por todo o mundo (Very Long Baseline Interferometry: VLBI). Contudo, há limites na distribuição de telescópios na Terra e os dados observacionais continham enormes "lacunas (dados em falta)".
Para reconstruir a imagem do buraco negro a partir de dados tão esparsos, foi desenvolvido um algoritmo chamado CHIRP (Continuous High-resolution Image Reconstruction using Patch priors). Isto também pode ser visto como uma aplicação de sensing comprimido, explorando a esparsidade e os conhecimentos prévios estruturais inerentes às imagens do universo.

### 3. Câmara de um Só Pixel (Single-Pixel Camera)
Uma equipa de pesquisa na Rice University desenvolveu uma câmara que possui apenas um elemento recetor de luz (pixel).
Usando um DMD (Dispositivo de Micro-espelhos Digitais), a luz de um objeto é refletida em padrões aleatórios e a soma é medida por esse único sensor. Repetindo esse processo milhares de vezes, consegue-se reconstruir imagens com milhões de pixéis. Esta tecnologia é extremamente útil para imagens em faixas de comprimento de onda (como infravermelhos e ondas terahertz) nas quais produzir sensores com múltiplos pixéis é muito dispendioso.

## 6. Exemplo de Implementação de Sensing Comprimido em Python

Visto que apenas a teoria pode não parecer concreta, vamos simular o sensing comprimido utilizando Python.
Aqui, vamos gerar um sinal esparso unidimensional e recuperar o sinal original usando otimização $L_1$ a partir de um pequeno número de observações aleatórias. A otimização usa a biblioteca `cvxpy`.

### Instalação de Bibliotecas Necessárias
```bash
pip install numpy matplotlib cvxpy
```

### Código de Implementação

```python
import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cp

# Fixar a semente aleatória
np.random.seed(42)

# --- 1. Configuração do Problema ---
N = 1000  # Dimensão do sinal (quantidade que devia ser amostrada originalmente)
K = 50    # Esparsidade (número de elementos não zero)
M = 250   # Número de observações (apenas 25% de N)

# --- 2. Geração do Sinal Verdadeiro Esparso ---
# Criação do sinal verdadeiro x_true (valores iniciais todos zero)
x_true = np.zeros(N)
# Escolhe K índices aleatoriamente e define valores não-zero (distribuição gaussiana)
nonzero_indices = np.random.choice(N, K, replace=False)
x_true[nonzero_indices] = np.random.randn(K)

# --- 3. Simulação do Processo de Observação ---
# Geração de matriz de observação gaussiana aleatória A (M x N)
A = np.random.randn(M, N)
# Normalização por coluna (norma torna-se 1)
A = A / np.linalg.norm(A, axis=0)

# Dados observados y = A * x_true
y = A @ x_true

# --- 4. Recuperação do Sinal por Sensing Comprimido (Otimização L1) ---
# Definir problema de otimização usando cvxpy
x_reconstruct = cp.Variable(N)
# Função objetivo: Minimização da Norma L1
objective = cp.Minimize(cp.norm(x_reconstruct, 1))
# Restrições: y = A * x (corresponder aos dados observados)
constraints = [A @ x_reconstruct == y]

# Definir e resolver o problema
prob = cp.Problem(objective, constraints)
print("Executando o cálculo de otimização...")
prob.solve(solver=cp.ECOS)

# Sinal recuperado
x_rec = x_reconstruct.value

# --- 5. Visualização dos Resultados ---
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(x_true, label='Sinal Verdadeiro', alpha=0.7)
plt.title(f'Sinal Esparso Original (N={N}, K={K})')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(x_rec, color='red', label='Sinal Recuperado', alpha=0.7)
plt.title(f'Recuperado via Minimização L1 (M={M} observações)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Verificação da Precisão da Recuperação
error = np.linalg.norm(x_true - x_rec)
print(f"Erro de recuperação (norma L2): {error:.6e}")
```

### Explicação do Código
1. **Geração do Sinal**: De $N=1000$ dimensões, criamos um vetor esparso `x_true` onde apenas $K=50$ posições têm um valor (sendo o resto zero).
2. **Observação**: Pelo teorema de amostragem, precisaríamos de 1000 medições. Aqui, obtemos os dados `y` usando apenas $M=250$ (25%) com uma matriz de observação aleatória `A`.
3. **Recuperação**: Dando como entrada os dados observados `y` e a matriz `A`, usamos `cvxpy` para encontrar $\mathbf{x}$ "que tenha a menor norma $L_1$ entre as soluções de $\mathbf{y} = \mathbf{A}\mathbf{x}$".
4. **Resultado**: Quando o cálculo termina, o erro de recuperação será um valor muito pequeno, como inferior a `1e-9`, confirmando que o sinal verdadeiro foi **perfeitamente (exatamente) recuperado** usando apenas 25% dos dados observacionais.

```mermaid
flowchart LR
    X["Sinal esparso desconhecido\nx (N dim)"] -->|Matriz de observação\naleatória A| Y["Dados de observação\ny (M dim, M < N)"]
    Y -->|Otimização L1\n(Algoritmo de otimização convexa)| X_hat["Sinal recuperado\nx^"]
    X -. "Garantia de exatidão perfeita" .-> X_hat
```

## 7. Resumo e Perspetivas Futuras

O sensing comprimido mudou fundamentalmente o paradigma da história do processamento de sinais. A abordagem de "medir inteligentemente apenas a quantidade necessária desde o início" em oposição a "medir muito para depois deitar fora" é suportada por profundas teorias da matemática (otimização convexa, [teoria das matrizes aleatórias](/pt/p/random-matrix-theory/), geometria de alta dimensão).

Atualmente, pesquisas que combinam o sensing comprimido e a aprendizagem profunda (Deep Learning) estão bastante ativas. Em vez dos algoritmos de otimização $L_1$ convencionais, utilizar as redes neuronais para resolver problemas inversos com mais velocidade e precisão (Deep Unfolding / Algorithm Unrolling) está a tornar-se uma abordagem predominante. Desta forma, é possível aprender a desenhar a própria matriz de observação baseado nos dados (data-driven), acelerando mais ainda a MRI ou promovendo a aplicação em reconstrução de imagem robusta contra ruídos.

A magia matemática do sensing comprimido de prever com precisão todo o cenário através de escassas informações continuará a providenciar uns "novos olhos" no futuro, em campos onde a explosão de dados é um desafio, como na condução autónoma, redes de sensores IoT e explorações espaciais.
