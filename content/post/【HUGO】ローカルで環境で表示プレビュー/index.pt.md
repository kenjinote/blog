---
title: "【HUGO】Visualização no ambiente local"
slug: "【HUGO】Visualização no ambiente local"
date: 2022-09-05T12:28:01+09:00
tags: ["HUGO"]
draft: false
image: "img.png"
categories: ["Operação do Blog"]
---
# Instalação do HUGO

## Download
[Download do HUGO](https://github.com/gohugoio/hugo/releases)

A partir do site acima, baixe e extraia o módulo do Windows que corresponde ao seu ambiente.
No meu caso, baixei "hugo_0.102.3_Windows-64bit.zip".

## Extração
Extraia o arquivo zip baixado e copie o hugo.exe dentro dele para uma pasta que você criar, por exemplo, C:\bin.

## Registrar nas Variáveis de Ambiente
Registre nas variáveis de ambiente para poder executar o hugo.exe de qualquer lugar.
As operações abaixo são para o Windows 11, mas você deve conseguir registrar com um procedimento semelhante:

1. Pressione Win+Pause para abrir as informações da versão
2. Clique em Configurações avançadas do sistema
3. Clique em Variáveis de Ambiente
4. Selecione Path e clique em Editar
5. Clique em Novo, digite "C:\bin" em uma nova linha e clique em OK para fechar a caixa de diálogo
 
# Visualizar o blog
No prompt de comando, navegue até a pasta do blog HUGO e execute o comando abaixo.

`hugo server -D`

O resultado da execução está abaixo. (-D é uma opção para exibir artigos em rascunho.)

```
C:\Users\win11\IdeaProjects\kenji.blog>hugo server -D
Start building sites …
hugo v0.102.3-b76146b129d7caa52417f8e914fc5b9271bf56fc windows/amd64 BuildDate=2022-09-01T10:16:19Z VendorInfo=gohugoio

                   | JA
-------------------+-----
  Pages            | 39
  Paginator pages  |  0
  Non-page files   |  7
  Static files     |  0
  Processed images |  0
  Aliases          | 13
  Sitemaps         |  1
  Cleaned          |  0

Built in 161 ms
Watching for changes in C:\Users\win11\IdeaProjects\kenji.blog\{archetypes,content,themes}
Watching for config changes in C:\Users\win11\IdeaProjects\kenji.blog\config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

Como o endereço é exibido durante a execução (no exemplo acima, `http://localhost:1313/`), copie o endereço no seu navegador.
A visualização é atualizada automaticamente toda vez que o arquivo é salvo.
Para terminar a visualização, digite Ctrl+C no prompt de comando.
