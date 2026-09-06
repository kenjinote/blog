---
title: "Introdução ao vim"
slug: "vim入門"
date: 2024-04-19T22:06:34+09:00
tags: ["vim", "editor de texto"]
draft: false
image: "img.png"
categories: ["Ferramentas e Ambiente de Desenvolvimento"]
---

![img_1.png](img_1.png)

# Introdução ao vim

## Download e Instalação

[https://www.vim.org/download.php](https://www.vim.org/download.php)

No site acima, baixe e instale o módulo apropriado para o seu sistema operacional.

Para Windows, escolher `gvim_X.X.X_x64_signed.exe` é uma boa opção.

## Como Iniciar

No Windows, é necessário registrar a pasta onde `vim.exe` está localizado na variável de ambiente Path.

Como iniciar:

```
vim
```

Para iniciar especificando um nome de arquivo:

```
vim filename.txt
```

## Como Sair

Para sair, digite `:` (dois pontos), depois `q` e pressione Enter.
```
:q
```

Se o arquivo foi modificado, será exibido `Nenhuma gravação desde a última alteração (adicione ! para forçar)`.
Você pode forçar a saída descartando as alterações.
```
:q!
```

Para salvar e sair do arquivo:
```
:wq
```

O seguinte também tem o mesmo significado:
```
:x
```

Você também pode sair pressionando `Shift` e apertando `z` duas vezes. (O mesmo que :wq)

## Modos

O vim possui um `Modo de Comando` e um `Modo de Inserção`. Ao iniciar o vim, ele está no `Modo de Comando`. Pressionar a tecla `i` muda para o `Modo de Inserção`.

No `Modo de Inserção`, como o nome sugere, você pode digitar texto. Para voltar do `Modo de Inserção` para o `Modo de Comando`, pressione a tecla `ESC`.

A alternância entre esses modos é uma característica fundamental do vim.

## Movimentação do Cursor e Rolagem

Resumo da movimentação do cursor e rolagem no `Modo de Comando`.

| Tecla                                | Descrição                      |
|------------------------------------|-------------------------|
| `h` (ou `Ctrl`+`H`, `BackSpace`, `←`) | Mover para a esquerda |
| `j` (ou `Ctrl`+`J` / `N`, `↓`)         | Mover para baixo     |
| `k` (ou `Ctrl`+`P`, `↑`)             | Mover para cima      |
| `l` (ou `Space`, `→`)               | Mover para a direita |
| `+` (ou `Enter`)                   | Mover para o início da próxima linha |
| `-`                                | Mover para o início da linha anterior |
| `Ctrl`+`B` (ou `PageUp`)            | Rolar para cima (página) |
| `Ctrl`+`F` (ou `PageDown`)          | Rolar para baixo (página) |
| `Ctrl`+`U`                         | Rolar para cima (meia página) |
| `Ctrl`+`D`                         | Rolar para baixo (meia página) |
| `Ctrl`+`Y`                         | Rolar para cima (uma linha) |
| `Ctrl`+`E`                         | Rolar para baixo (uma linha) |
| `z` `Enter`                        | Rolar linha do cursor para o topo |
| `z` `.`                            | Rolar linha do cursor para o centro |
| `z` `-`                            | Rolar linha do cursor para a base |
| `0` (ou `\|`)                       | Mover o cursor para o início da linha |
| `$`                                | Mover o cursor para o fim da linha |
| `^` (ou `_`)                        | Mover o cursor para o primeiro caractere não em branco da linha |
| `G` (ou `:$`)                       | Mover o cursor para a última linha |
| `:número_da_linha` `Enter`                     | Mover para a linha especificada |

Ao digitar um `número` antes das teclas de movimento acima, você pode mover várias vezes por essa quantidade.
(Por exemplo, digitar `3j` moverá 3 linhas para baixo a partir da posição atual do cursor.)

## Outros Comandos

| Tecla        | Descrição                   |
|------------|----------------------|
| `Ctrl`+`L` | Redesenhar a tela            |
| `Ctrl`+`G` | Mostrar número de linhas e a posição do cursor |
