---
title: "Como fechar e reiniciar o Explorador de Arquivos"
slug: "エクスプローラーの終了・再起動方法"
date: 2024-03-30T15:40:24+09:00
tags: ["Explorador de Arquivos"]
draft: false
image: "img_2.png"
categories: ["TI e Tecnologia"]
---

## Como fechar usando o botão direito na barra de tarefas

Este método funciona no Windows 10. Parece que o menu não aparece no Windows 11.
Se você segurar as teclas `Shift` e `Ctrl` e clicar com o botão direito na barra de tarefas, `Sair do Explorer` aparecerá no menu.

![img.png](img.png)

## Como fechar usando o Gerenciador de Tarefas

1. Pressione as teclas `Ctrl` + `Shift` + `Esc` para abrir o Gerenciador de Tarefas.
2. Selecione `Detalhes`.

![img_3.png](img_3.png)

3. Selecione `explorer.exe`, pressione a tecla `Delete`, e quando perguntado `Deseja finalizar o explorer.exe?`, selecione `Finalizar processo`.

![img_1.png](img_1.png)

## Como fechar usando o Prompt de Comando

1. Pressione as teclas `Win` + `R`, digite `cmd` e pressione `Enter`.
2. Digite `taskkill /f /im explorer.exe` e pressione `Enter`.

## Como iniciar o Explorer a partir do Gerenciador de Tarefas

1. Pressione as teclas `Ctrl` + `Shift` + `Esc` para abrir o Gerenciador de Tarefas.
2. No menu Arquivo, selecione `Executar nova tarefa`.
3. Digite `explorer.exe` e pressione `Enter`.
