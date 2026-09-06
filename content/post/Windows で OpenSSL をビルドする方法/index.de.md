---
title: "Wie man OpenSSL unter Windows kompiliert"
slug: "Windows で OpenSSL をビルドする方法"
date: 2023-04-07T21:06:32+09:00
tags: ["Windows", "OpenSSL", "Kompilierung", "C++"]
draft: false
image: "img.png"
categories: ["Programmierung"]
---

# Was ist OpenSSL?

Es ist eine Open-Source-Bibliothek, die die notwendige Verarbeitung für verschlüsselte Kommunikation bereitstellt.

Um es in einem Programm verwenden zu können, müssen Sie es kompilieren, um eine Bibliothek zu erstellen, da der C-Quellcode veröffentlicht wird.

Nachfolgend stellen wir den Kompilierungsvorgang vor.

# Vorbereitung der Build-Umgebung

- **Perl**

  Laden Sie `strawberry-perl-5.32.1.1-64bit.msi` von [https://strawberryperl.com/](https://strawberryperl.com/) herunter. Die neueste Version sollte in Ordnung sein.

- **NASM**

  Laden Sie `2.16.01/nasm-2.16.01-win64.zip` unter `Download` von [https://www.nasm.us/](https://www.nasm.us/) herunter. Die neueste Non-RC-Version sollte in Ordnung sein.
  Nach der Installation müssen Sie den Ordner, in dem NASM installiert ist, in der Umgebungsvariablen PATH registrieren.

- **Visual Studio 2022** oder **Build Tools for Visual Studio 2022**

  Installieren Sie `Visual Studio 2022 Community` oder `Build Tools for Visual Studio 2022` von [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/).
  
# OpenSSL-Build-Prozedur unter Windows

1. Laden Sie `openssl-3.1.0.tar.gz` von [https://www.openssl.org/source/](https://www.openssl.org/source/) herunter und entpacken Sie es. Wenn Sie es nicht entpacken können, führen Sie `tar -xzf openssl-3.1.0.tar.gz` in der Eingabeaufforderung aus.
2. Starten Sie die Eingabeaufforderung **mit Administratorrechten**.
3. Öffnen Sie den entpackten Ordner.
4. Führen Sie den folgenden Befehl aus. *Ändern Sie den Teil `Community`, damit er Ihrer installierten Version von Visual Studio entspricht.
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
```
5. Führen Sie den folgenden Befehl aus:
```
perl Configure VC-WIN64A
```
6. Führen Sie den folgenden Befehl aus (dauert ziemlich lange):
```
nmake
```
7. Führen Sie den folgenden Befehl aus (dauert ziemlich lange):
```
nmake test
```
8. Führen Sie den folgenden Befehl aus:
```
nmake install
```

Wenn es erfolgreich war, wird OpenSSL in `C:\Program Files\OpenSSL` installiert.

Das ist alles.

# Referenzen
[https://ja.wikipedia.org/wiki/OpenSSL](https://ja.wikipedia.org/wiki/OpenSSL)
