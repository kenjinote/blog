---
title: "Como instalar o editor de texto micro no Windows"
slug: "como-instalar-o-editor-de-texto-micro-no-windows"
date: 2024-03-31T21:50:39+09:00
tags: ["micro", "editor de texto"]
draft: false
image: "img.png"
categories: ["Ferramentas e Ambiente de Desenvolvimento"]
---

## Baixar o micro
https://github.com/zyedidia/micro/releases

Abra o link acima, clique em `Show all XX assets` (onde X é um número) e baixe o `micro-X.X.XX-win64.zip` (onde X é um número).
Extraia o arquivo zip e coloque todos os arquivos em uma pasta de sua escolha.

## Configurar as variáveis de ambiente
Para usar o `micro.exe` pelo Prompt de Comando, você precisa configurar as variáveis de ambiente.

1. Pressione a `tecla Win` + `tecla R`, digite `sysdm.cpl` e pressione `Enter`.
2. Clique em `Configurações avançadas do sistema` nas `Propriedades do Sistema`.
3. Clique em `Variáveis de Ambiente`.
4. Selecione `Path` em `Variáveis do sistema` e clique em `Editar`.
5. Clique em `Novo` e adicione o caminho para a pasta que contém o `micro.exe`.
6. Clique em `OK` para fechar todas as caixas de diálogo.
7. Reinicie o Prompt de Comando e digite `nano` para verificar se ele pode ser executado.

## Como usar o micro

Ao digitar `micro` no Prompt de Comando e executá-lo, a seguinte tela será exibida.
![img_3.png](img_3.png)

As principais operações e teclas de atalho são as seguintes:

| Tecla de atalho | Operação | 
|--------|-----| 
| Ctrl+Q | Fechar arquivo | 
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
