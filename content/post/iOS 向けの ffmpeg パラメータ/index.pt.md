---
title: "Parâmetros do ffmpeg para iOS"
slug: "iOS 向けの ffmpeg パラメータ"
date: 2025-03-02T04:16:07+09:00
tags: ["iOS", "ffmpeg"]
draft: false
image: "img.png"
categories: ["PC・ガジェット"]
---

# Parâmetros de conversão do ffmpeg otimizados para iOS

Apresentamos o comando `ffmpeg` para converter vídeos para que possam ser reproduzidos sem problemas em dispositivos iOS (iPhone e iPad).

```bash
ffmpeg -i input.mp4 \
-c:v libx264 -profile:v high -level 4.1 \
-vf "scale=1920:-2" -r 30 \
-crf 20 -preset slow \
-c:a aac -b:a 128k -ar 48000 \
-movflags +faststart output.mp4
```

### Significado de cada opção (breve explicação)

| Opção                        | Descrição                                          |
| ---------------------------- | ------------------------------------------- |
| `-i input.mp4`               | Arquivo de entrada (vídeo a ser convertido)                              |
| `-c:v libx264`               | Codificar vídeo com H.264 (compatível com iOS)                       |
| `-profile:v high -level 4.1` | Perfil e nível amplamente compatíveis com iOS                      |
| `-vf "scale=1920:-2"`        | Redimensionar para 1920px de largura, a altura é ajustada automaticamente mantendo a proporção               |
| `-r 30`                      | Converter a taxa de quadros para 30fps                             |
| `-crf 20`                    | Qualidade de vídeo (números menores significam maior qualidade, recomendado 18–23)                   |
| `-preset slow`               | Equilíbrio entre velocidade de codificação e taxa de compressão (slow significa alta compressão e alta qualidade)              |
| `-c:a aac`                   | O áudio é codificado no formato AAC                              |
| `-b:a 128k`                  | Definir taxa de bits de áudio para 128kbps                         |
| `-ar 48000`                  | Definir taxa de amostragem de áudio para 48kHz (recomendado para iOS)                |
| `-movflags +faststart`       | Coloca um índice no início do vídeo para **acelerar a reprodução por streaming na Web e no iOS** |

---

Espera-se que os vídeos convertidos com essas configurações tenham alta compatibilidade e reprodução suave em dispositivos da Apple, como iPhone e iPad.

---

Se necessário, você pode ajustar o tamanho do arquivo e a qualidade da imagem alterando a resolução e a taxa de bits. Se precisar de alta qualidade de imagem, tente definir o `-crf` para cerca de 18; se quiser reduzir o tamanho do arquivo, defina-o para 22–25.
