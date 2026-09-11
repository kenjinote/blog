---
title: 'Como Gerar QR Codes no Prompt de Comando Usando o Comando curl'
slug: "curlでQRコード生成"
date: 2024-04-16T00:42:27+09:00
tags: ["Código QR", "curl", "Prompt de Comando"]
draft: false
image: "img.webp"
categories: ["TI e Tecnologia"]
description: 'Aprenda a gerar e exibir códigos QR em modo texto no Prompt de Comando do Windows usando o comando curl. Também explicamos as precauções sobre o manuseio de informações pessoais ao usar a API externa (qrenco.de).'
---

## Gerar código QR com curl

Aviso: Os métodos apresentados retornam um código QR gerado no lado do servidor, portanto, pode haver registro de logs. Tenha cuidado ao converter informações confidenciais, como informações pessoais, em um código QR.

### Método 1

Este é um método para gerar um código QR no prompt de comando.
O `qrenco.de` retorna a resposta em formato de texto.

```
curl qrenco.de/kenji.blog
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

```
curl -o qr.webp "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=HelloWorld"
```

- Resultado da saída
![](qr.webp)

#### Referência
- [QR Code Generator](https://goqr.me/api/doc/create-qr-code/)
