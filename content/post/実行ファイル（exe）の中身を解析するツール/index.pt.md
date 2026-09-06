---
title: "Ferramentas para Analisar o Conteúdo de Arquivos Executáveis (exe)"
slug: "ferramentas-para-analisar-arquivos-executaveis-exe"
date: 2023-04-05T23:31:06+09:00
tags: ["windows", "exe", "executável", "análise"]
draft: false
image: "img_1.png"
categories: ["PC e Gadgets"]
---

# O que é um arquivo executável (exe)?

Um arquivo executável no Windows. Ele é escrito basicamente no que é chamado de formato PE.
Contém código de linguagem de máquina para execução, bem como recursos como ícones e imagens.

Existem várias ferramentas disponíveis para analisar arquivos executáveis, e nós as apresentaremos desta vez.

## 7-Zip

![img.png](img.png)

Arquivos EXE às vezes são criados pela compactação de arquivos porque tendem a se tornar grandes em seu estado original. Neste caso, usando o software de compactação/descompactação de arquivos 7-Zip, você pode descompactar o arquivo executável e examinar seu conteúdo. O WinRAR é outra ferramenta que pode descompactar arquivos de forma semelhante.

## Resource Hacker
![img_2.png](img_2.png)

Permite extrair recursos (ícones, bitmaps, caixas de diálogo, strings, etc.) localizados dentro de arquivos EXE. Também funciona como um editor hexadecimal, permitindo que você edite e reescreva o conteúdo dos arquivos EXE.

## PE Explorer
![img_3.png](img_3.png)

Pode analisar arquivos PE (EXE, DLL, OCX, SYS, drivers) para Windows. O PE Explorer fornece vários recursos analíticos, incluindo exibição da estrutura do arquivo, cabeçalho do arquivo, entradas de diretório, além de funções e símbolos exportados.

## Dependency Walker
![img_4.png](img_4.png)

Você pode verificar os arquivos DLL dos quais um arquivo EXE depende e confirmar se estão carregados corretamente. Também permite rastrear chamadas de função para arquivos DLL.

Embora essas ferramentas sejam úteis para examinar o conteúdo de arquivos EXE, é necessário cautela. Modificar arquivos ou usá-los para fins não autorizados pode causar problemas de segurança ou violações de leis de direitos autorais, portanto, certifique-se de entender isso completamente antes de usá-las.
