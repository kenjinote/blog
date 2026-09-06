---
title: "Como baixar vídeos do YouTube com yt-dlp.exe"
slug: "yt-dlp.exe による YouTube 動画のダウンロード方法"
date: 2024-09-03T14:09:26+09:00
tags: ["YouTube", "Download"]
draft: false
image: "img_1.png"
categories: ["IT/Tecnologia"]
---
# O que é o yt-dlp

O `yt-dlp` é uma ferramenta de linha de comando para baixar vídeos do YouTube.
Além de baixar vídeos, você também pode baixá-los como arquivos de música no formato mp3.

## Download e Instalação

1. Baixe o yt-dlp.exe mais recente da [página de lançamentos do yt-dlp](https://github.com/yt-dlp/yt-dlp/releases).
2. Coloque o yt-dlp.exe em qualquer pasta.
3. Adicione o caminho da pasta do yt-dlp.exe à variável de ambiente Path.

## Como Usar

Execute o yt-dlp.exe no prompt de comando e especifique a URL do vídeo do YouTube.

```
yt-dlp.exe "https://www.youtube.com/watch?v=VIDEO_ID"
```
※ O argumento pode ser apenas a parte do VIDEO_ID.

Para baixar como um arquivo de música mp3, execute o seguinte comando:

```
yt-dlp.exe --extract-audio --audio-format mp3 --embed-thumbnail --add-metadata "https://www.youtube.com/watch?v=VIDEO_ID"
```

Com isso, o vídeo será baixado no diretório atual de onde o comando foi executado.

Isso é tudo.
