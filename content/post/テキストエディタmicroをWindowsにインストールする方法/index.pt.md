---
title: 'Pode ser usado no Windows! Como instalar o leve editor de texto ''micro'''
slug: "Editor de TextomicroをWindowsにInstalaçãoする方法"
date: "2024-03-31T21:50:39+09:00"
lastmod: "2026-11-25"
tags: ["micro", "editor de texto"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Explicaremos os procedimentos para instalar o ''micro'', um editor de texto para terminais que funciona confortavelmente no prompt de comando no Windows, até definir as variáveis de ambiente e torná-lo pronto para uso.'
---

## Baixar o micro
https://github.com/micro-editor/micro/releases/latest
Em Assets da versão mais recente, baixe o arquivo para Windows x64 (por exemplo, `micro-<version>-win64.zip`) e extraia-o em uma pasta de sua escolha.

No Windows em ARM, escolha o arquivo ARM64 correspondente.

## Configurar as variáveis de ambiente
Para usar o `micro.exe` pelo Prompt de Comando, você precisa configurar as variáveis de ambiente.

1. Pressione `Win` + `R`, digite `sysdm.cpl` e pressione `Enter`.
2. Abra a guia Avançado e clique em Variáveis de Ambiente.
3. Em Variáveis de usuário da sua conta, selecione `Path` e clique em Editar. Se não estiver listado, crie `Path`.
4. Clique em Novo e adicione o caminho da pasta que contém `micro.exe`.
5. Clique em OK para fechar as caixas de diálogo.
6. Abra novamente o Prompt de Comando e execute `micro` para confirmar que ele inicia.

## Como usar o micro

Ao digitar `micro` no Prompt de Comando e executá-lo, a seguinte tela será exibida.
![img_3.png](img_3.webp)

As principais operações e teclas de atalho são as seguintes:

| Tecla de atalho | Operação | 
|--------|-----| 
| Ctrl+Q | Fechar o arquivo atual (o micro sai se for o último arquivo) |
| Ctrl+S | Salvar arquivo | 
| Ctrl+O | Abrir arquivo | 
| Ctrl+A | Selecionar tudo | 
| Ctrl+X | Cortar seleção | 
| Ctrl+C | Copiar seleção | 
| Ctrl+V | Colar | 
| Ctrl+Z | Desfazer | 
| Ctrl+Y | Refazer | 
| Ctrl+E | Executar comando do editor | 

## Referência
- [micro](https://micro-editor.github.io/)
- [Default key bindings](https://github.com/micro-editor/micro/blob/master/runtime/help/defaultkeys.md)
