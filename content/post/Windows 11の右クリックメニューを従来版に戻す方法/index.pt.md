---
title: 'Como restaurar o menu de contexto do Windows 11 para a versão clássica (especificação antiga) [Configurações do Registro]'
slug: "como-restaurar-o-menu-de-contexto-classico-no-windows-11"
date: 2024-03-30T13:13:36+09:00
tags: ["Windows11", "Explorador de Arquivos"]
draft: false
image: "img.webp"
categories: ["PC e Gadgets"]
description: 'Explicamos como restaurar o novo menu de contexto do Windows 11 para a versão clássica do Windows 10. Apresentamos um procedimento simples para sempre mostrar o menu da especificação antiga alterando as configurações usando o Editor do Registro.'
---

# Como restaurar o menu de contexto clássico no Windows 11

Aqui está como restaurar o menu de contexto clássico (menu do botão direito) no Windows 11.

1. Abra o Editor do Registro.

Pressione `Tecla Win` + `R`, digite `regedit` e pressione `Enter`.
![img_1.png](img_1.webp)　

2. Navegue até `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`. Se esta chave não existir, crie-a.


4. Navegue até `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`. Se esta chave não existir, crie-a.
5. Verifique se `(Padrão)` em `InprocServer32` não possui valor.

![img_2.png](img_2.webp)

6. Reinicie o computador.
7. Confirme se o menu de contexto retornou à versão clássica.
