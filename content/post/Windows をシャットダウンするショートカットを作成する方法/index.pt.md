---
title: 'Como criar um atalho para desligar o Windows'
slug: "Windows をDesligarするAtalhoを作成する方法"
date: 2023-04-11T17:03:32+09:00
lastmod: "2026-11-25T00:00:00+09:00"
tags: ["Windows", "Desligar", "Atalho"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: 'Crie um atalho na área de trabalho para iniciar o desligamento do Windows 10 ou Windows 11 com dois cliques.'
---
Estas etapas são para Windows 10 e Windows 11. Os nomes dos menus podem variar um pouco conforme a versão e o idioma de exibição.

## Criar o atalho

#### 1. Clique com o botão direito em uma área vazia da área de trabalho e selecione `Novo` > `Atalho`.

#### 2. Digite este comando como local do item e clique em `Avançar`.

```text
shutdown.exe /s /t 0
```

#### 3. Dê um nome ao atalho, como `Desligar`, e clique em `Concluir`.

## Alterar o ícone (opcional)

Clique com o botão direito no atalho e selecione `Propriedades` > `Alterar ícone`. Escolha um ícone em `%SystemRoot%\System32\SHELL32.dll` e clique em `OK`.

Salve seu trabalho antes de usar o atalho. Ele inicia o desligamento do Windows sem uma etapa adicional de confirmação. `/s` solicita o desligamento e `/t 0` define espera zero. O comando não usa `/f`, então os aplicativos podem encerrar normalmente e avisar sobre trabalho não salvo.

[**Microsoft Learn: comando shutdown (em inglês)**](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown/)
