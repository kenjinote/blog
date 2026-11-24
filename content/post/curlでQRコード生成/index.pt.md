---
title: 'Como Gerar QR Codes no Prompt de Comando Usando o Comando curl'
slug: "curlでCódigo QR生成"
date: "2024-04-16T00:42:27+09:00"
lastmod: "2026-11-25"
tags: ["Código QR", "curl", "Prompt de Comando"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'Este artigo mostra como usar curl no Prompt de Comando do Windows para gerar QR Codes em texto e imagem e explica os cuidados ao enviar dados a serviços externos.'
---

## Gerar código QR com curl

Aviso: Os métodos apresentados retornam um código QR gerado no lado do servidor, portanto, pode haver registro de logs. Tenha cuidado ao converter informações confidenciais, como informações pessoais, em um código QR.

O texto informado é enviado a um serviço externo; não use informações confidenciais.

### Método 1

Este é um método para gerar um código QR no prompt de comando.
O `qrenco.de` retorna a resposta em formato de texto.

```
curl.exe https://qrenco.de/kenji.blog
```

- Resultado da saída

```
█████████████████████████████
█████████████████████████████
████ ▄▄▄▄▄ █ ▄ ▄ █ ▄▄▄▄▄ ████
████ █   █ █ ▀▀▀██ █   █ ████
████ █▄▄▄█ █▀▀█▀▄█ █▄▄▄█ ████
████▄▄▄▄▄▄▄█▄▀ ▀ █▄▄▄▄▄▄▄████
████▄ █▀▄ ▄▀█▄▀ ▀██▄▀   ▄████
████▀▀▀█  ▄▄ ▄█▄█▀█▀▄██ ▀████
████▄▄▄██▄▄█ █▀█ ▄██▀▀█ █████
████ ▄▄▄▄▄ █▀█ ▀  ▄▀▄▄▄ ▀████
████ █   █ █▄▄ ▄▀▄▀▄ ██ ▀████
████ █▄▄▄█ █▀▀█ ▀▄▄▄ ▄▄██████
████▄▄▄▄▄▄▄█▄▄███▄▄█▄███▄████
█████████████████████████████
█████████████████████████████
```

#### Referência
- [qrenco.de](https://qrenco.de/)

### Método 2

O `api.qrserver.com` retorna uma imagem.

A API GoQR retorna PNG por padrão. Codifique o valor de `data` na URL se ele contiver espaços ou caracteres especiais.

```
curl.exe -o qr.png "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=HelloWorld"
```

- Resultado da saída
![Imagem de exemplo de código QR](qr.webp)

#### Referência
- [QR Code Generator](https://goqr.me/api/doc/create-qr-code/)
- [curl command-line manual](https://curl.se/docs/manpage.html)
