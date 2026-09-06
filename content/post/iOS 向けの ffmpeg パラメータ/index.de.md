---
title: "ffmpeg Parameter für iOS"
slug: "iOS 向けの ffmpeg パラメータ"
date: 2025-03-02T04:16:07+09:00
tags: ["iOS", "ffmpeg"]
draft: false
image: "img.png"
categories: ["PC・ガジェット"]
---

# Für iOS optimierte ffmpeg-Konvertierungsparameter

Wir stellen den `ffmpeg`-Befehl vor, um Videos für eine reibungslose Wiedergabe auf iOS-Geräten (iPhone und iPad) zu konvertieren.

```bash
ffmpeg -i input.mp4 \
-c:v libx264 -profile:v high -level 4.1 \
-vf "scale=1920:-2" -r 30 \
-crf 20 -preset slow \
-c:a aac -b:a 128k -ar 48000 \
-movflags +faststart output.mp4
```

### Bedeutung jeder Option (Kurze Erklärung)

| Option                        | Beschreibung                                          |
| ---------------------------- | ------------------------------------------- |
| `-i input.mp4`               | Eingabedatei (zu konvertierendes Video)                              |
| `-c:v libx264`               | Video mit H.264 kodieren (iOS-kompatibel)                       |
| `-profile:v high -level 4.1` | Weitgehend kompatibles Profil und Level für iOS                      |
| `-vf "scale=1920:-2"`        | Größe auf 1920px Breite ändern, Höhe wird automatisch unter Beibehaltung des Seitenverhältnisses angepasst               |
| `-r 30`                      | Bildrate auf 30fps konvertieren                             |
| `-crf 20`                    | Videoqualität (niedrigere Zahlen bedeuten höhere Qualität, empfohlen 18-23)                   |
| `-preset slow`               | Gleichgewicht zwischen Kodierungsgeschwindigkeit und Kompressionsrate (slow bedeutet hohe Kompression und hohe Qualität)              |
| `-c:a aac`                   | Audio wird im AAC-Format kodiert                              |
| `-b:a 128k`                  | Audio-Bitrate auf 128 kbps einstellen                         |
| `-ar 48000`                  | Audio-Abtastrate auf 48 kHz einstellen (empfohlen für iOS)                |
| `-movflags +faststart`       | Setzt einen Index an den Anfang des Videos, um **das Streaming im Web und unter iOS zu beschleunigen** |

---

Mit diesen Einstellungen konvertierte Videos bieten voraussichtlich eine hohe Kompatibilität und reibungslose Wiedergabe auf Apple-Geräten wie iPhone und iPad.

---

Bei Bedarf können Sie die Dateigröße und Bildqualität anpassen, indem Sie Auflösung und Bitrate ändern. Wenn eine hohe Bildqualität erforderlich ist, versuchen Sie, `-crf` auf etwa 18 einzustellen; wenn Sie die Dateigröße reduzieren möchten, stellen Sie ihn auf 22-25 ein.
