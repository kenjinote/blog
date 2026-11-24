---
title: "Como usar yt-dlp.exe: baixar conteúdo autorizado e converter para MP3"
slug: "yt-dlp.exe による YouTube VídeoのDownload方法"
tags: ["yt-dlp", "YouTube", "media tools"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "Como obter e atualizar yt-dlp.exe, salvar um vídeo e converter áudio para MP3. Use a ferramenta de acordo com os direitos do conteúdo e os termos do YouTube."
date: "2024-09-03T14:09:26+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Como usar yt-dlp.exe: baixar conteúdo autorizado e converter para MP3

yt-dlp é uma ferramenta de linha de comando de código aberto para baixar vídeos e áudio. Estes exemplos mostram o uso básico no Windows.

## Use somente quando permitido

Use yt-dlp apenas com conteúdo de sua propriedade ou com autorização do titular, e somente quando permitido pelos termos do YouTube e pela legislação aplicável. Você pode baixar seus próprios vídeos enviados pelo YouTube Studio.

## Instalação e atualização

Baixe o `yt-dlp.exe` para Windows na página oficial de versões e coloque-o em uma pasta. Adicione essa pasta ao `PATH` para executá-lo de qualquer diretório. Obtenha o executável somente nas versões oficiais.

```powershell
yt-dlp.exe --version
yt-dlp.exe -U
```

## Uso básico

No Prompt de Comando ou no PowerShell, informe o URL do vídeo. O arquivo será salvo no diretório atual.

```powershell
yt-dlp.exe "https://www.youtube.com/watch?v=VIDEO_ID"
```

Para converter o áudio em MP3, use `-x` e `--audio-format mp3`.

```powershell
yt-dlp.exe -x --audio-format mp3 "https://www.youtube.com/watch?v=VIDEO_ID"
```

Confira a versão com `yt-dlp.exe --version`. Atualize um binário de versão com `yt-dlp.exe -U`. A conversão para MP3 requer `ffmpeg` e `ffprobe`. Se a extração parar de funcionar após mudanças no YouTube, atualize o yt-dlp e consulte as dependências atuais no README oficial.

Para incorporar miniaturas ou metadados, adicione `--embed-thumbnail` ou `--embed-metadata`; dependendo do formato, outras ferramentas podem ser necessárias.

## Se não funcionar

Atualize para a versão mais recente e consulte a documentação oficial sobre dependências e suporte atuais. Não contorne restrições nem baixe conteúdo sem autorização.

## Referências

- [yt-dlp official releases](https://github.com/yt-dlp/yt-dlp/releases/latest)
- [yt-dlp README and documentation](https://github.com/yt-dlp/yt-dlp#readme)
- [YouTube Terms of Service](https://www.youtube.com/t/terms)
- [YouTube Help: download your own videos](https://support.google.com/youtube/answer/56100)
