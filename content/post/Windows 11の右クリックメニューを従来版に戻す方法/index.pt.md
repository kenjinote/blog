---
title: "Abrir o menu de contexto clássico no Windows 11"
slug: "Windows 11のMenu de Contextoを従来版に戻す方法"
tags: ["Windows11", "Explorador de Arquivos"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: "Como abrir o menu de contexto clássico com Mostrar mais opções no Windows 11 e conhecer uma alternativa pelo Registro que pode não funcionar em todas as versões."
date: "2024-03-30T13:13:36+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Abrir o menu de contexto clássico no Windows 11

No Windows 11, clique com o botão direito em um item e selecione Mostrar mais opções para abrir o menu de contexto clássico. Também é possível selecionar um item e pressionar `Shift`+`F10`, ou manter `Shift` pressionado enquanto clica com o botão direito para abrir Mostrar mais opções. Experimente primeiro esses recursos integrados.

> A alteração do Registro abaixo é uma solução alternativa não oficial para deixar o menu clássico como padrão. Ela não é um procedimento oficialmente suportado pela Microsoft e pode não funcionar em algumas versões do Windows. Faça uma cópia de segurança do Registro antes de editá-lo.

## Etapas da alternativa pelo Registro

1. Abra o Editor do Registro.

Pressione `Tecla Win` + `R`, digite `regedit` e pressione `Enter`.
![img_1.png](img_1.webp)　

2. Navegue até `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`. Se esta chave não existir, crie-a.


3. Navegue até `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`. Se esta chave não existir, crie-a.
4. Verifique se `(Padrão)` em `InprocServer32` não possui valor.

![img_2.png](img_2.webp)

5. Reinicie o computador.
6. Confirme se o menu de contexto retornou à versão clássica.

Para desfazer a alteração, exclua a chave `{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}` que você criou e reinicie o Explorador de Arquivos. Faça uma cópia de segurança das configurações existentes antes de alterá-las.

## Referências

- [Suporte da Microsoft: Explorador de Arquivos no Windows](https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows)
- [Suporte da Microsoft: Atalhos de teclado do Windows](https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows)
