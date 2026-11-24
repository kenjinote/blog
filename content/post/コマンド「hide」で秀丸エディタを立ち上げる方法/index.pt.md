---
date: 2024-03-29T23:45:37+09:00
lastmod: 2026-11-25
title: 'Inicie o Editor Hidemaru com um único comando ''hide''! Métodos de configuração convenientes no Windows'
slug: "Comando「hide」でHidemaru Editorを立ち上げる方法"
tags: ["comando", "Hidemaru Editor", "registro"]
draft: false
image: "img_2.webp"
categories: ["tools-development-environment"]
description: "Registre um nome em App Paths e inicie o Hidemaru Editor pela caixa Executar ou com start hide no Windows 10/11."
---

## Aqui está como iniciar o Hidemaru Editor com o comando 'hide'.

Nota: Este método foi testado no `Windows 10/11`.

1. Abra o Editor do Registro.
2. Navegue até `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths`.
3. Crie uma chave chamada `hide.exe` em `App Paths`. **A parte antes de `.exe` no nome desta chave se torna o nome do comando.**
4. Defina o valor `(Padrão)` da chave `hide.exe` para o caminho do arquivo executável do Hidemaru Editor. No meu ambiente, era `"C:\Program Files (x86)\Hidemaru\Hidemaru.exe"`.
5. O valor Path é opcional. Omita-o, a menos que o app precise de diretórios DLL extras; ShellExecuteEx os acrescenta ao PATH do processo.
6. Digite hide em Executar (Win + R). No Prompt de Comando use start hide; digitar apenas hide não é o método descrito.

```reg
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\hide.exe]
@="C:\\Program Files (x86)\\Hidemaru\\Hidemaru.exe"
```
Se você salvar o conteúdo acima em um arquivo `.reg` e executá-lo, as configurações serão adicionadas ao registro.

Este .reg registra o app para o usuário atual. Substitua o caminho pelo executável real. Para todos os usuários, troque HKEY_CURRENT_USER por HKEY_LOCAL_MACHINE e importe como administrador.


## Referências

- [Microsoft: Application Registration and App Paths](https://learn.microsoft.com/en-us/windows/win32/shell/app-registration)
- [Microsoft: start command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/start)

![img_1.png](img_1.webp)
