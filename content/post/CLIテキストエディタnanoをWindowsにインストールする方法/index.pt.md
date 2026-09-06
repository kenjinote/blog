---
title: "Como instalar o editor de texto CLI nano no Windows"
slug: "CLIテキストエディタnanoをWindowsにインストールする方法"
date: 2024-03-31T18:09:32+09:00
tags: ["nano", "editor de texto"]
draft: false
image: "img_1.png"
categories: ["Ferramentas e Ambiente de Desenvolvimento"]
---

## Baixar o nano.exe
https://sourceforge.net/projects/nano-for-windows/

Abra o link acima, clique em `Download` e baixe o `GNU-Nano_Win32(static).zip`.
Extraia o arquivo zip e coloque o `nano.exe` em qualquer pasta.
* A entrada de texto em japonês não é suportada (em 31/03/2024).

## Configurar variáveis de ambiente
Para usar o `nano.exe` no Prompt de Comando, você precisa configurar as variáveis de ambiente.

1. Pressione a `tecla Win` + `tecla R`, digite `sysdm.cpl` e pressione `Enter`.
2. Clique em `Propriedades do Sistema` na janela de Propriedades do Sistema.
3. Clique em `Variáveis de Ambiente`.
4. Selecione `Path` em `Variáveis de sistema` e clique em `Editar`.
5. Clique em `Novo` e adicione o caminho do `nano.exe`.
6. Clique em `OK` para fechar todas as caixas de diálogo.
7. Reinicie o Prompt de Comando, digite `nano` e verifique se ele é executado.

## Como usar o nano

Ao digitar `nano` e executar, a seguinte tela será exibida:

![img_2.png](img_2.png)

As descrições dos atalhos são exibidas na parte inferior da tela.

O significado dos símbolos é o seguinte:

- `^` representa a tecla `Ctrl`.
- `M-` representa a tecla `Alt`.

Para salvar e fechar, pressione `Ctrl` + `S` e depois `Ctrl` + `X`.

## Referência
- [GNU nano](https://www.nano-editor.org/)
