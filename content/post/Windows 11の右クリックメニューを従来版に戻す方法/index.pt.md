---
title: "Como restaurar o menu de contexto clássico no Windows 11"
slug: "como-restaurar-o-menu-de-contexto-classico-no-windows-11"
date: 2024-03-30T13:13:36+09:00
tags: ["Windows11", "Explorador de Arquivos"]
draft: false
image: "img.png"
categories: ["PC e Gadgets"]
---

# Como restaurar o menu de contexto clássico no Windows 11

Aqui está como restaurar o menu de contexto clássico (menu do botão direito) no Windows 11.

1. Abra o Editor do Registro.

Pressione `Tecla Win` + `R`, digite `regedit` e pressione `Enter`.
![img_1.png](img_1.png)　

2. Navegue até `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`. Se esta chave não existir, crie-a.


4. Navegue até `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`. Se esta chave não existir, crie-a.
5. Verifique se `(Padrão)` em `InprocServer32` não possui valor.

![img_2.png](img_2.png)

6. Reinicie o computador.
7. Confirme se o menu de contexto retornou à versão clássica.
