---
title: 'Como encontrar a localização (caminho) do arquivo executável no PATH do Windows [comando where]'
slug: "Windows でパスの通った実行ファイルの場所を見つける方法"
date: 2023-04-03T00:02:55+09:00
tags: ["Windows", "Caminho", "Arquivo executável", "Prompt de Comando"]
draft: false
image: "img.webp"
categories: ["PC・ガジェット"]
description: 'Explicamos como verificar facilmente o local de salvamento (caminho completo) do arquivo executável no Prompt de Comando do Windows ou no PowerShell. Apresentamos um truque útil para localizar rapidamente o local exato do aplicativo no caminho usando o comando ''where''.'
---

# Como encontrar a localização de um arquivo executável no PATH do Windows

Quando você executa um comando especificando um arquivo executável, há momentos em que deseja saber onde esse arquivo executável está localizado. Nesses casos, você pode descobrir a localização do arquivo executável com o seguinte comando.

```powershell
where <nome_do_arquivo_executável>
```

Por exemplo, se você quiser saber a localização do Paint (mspaint.exe), faça o seguinte:

```powershell
where mspaint.exe
```

# Referências

- [How do I find the location of an executable in Windows?](https://superuser.com/questions/49104/how-do-i-find-the-location-of-an-executable-in-windows)
