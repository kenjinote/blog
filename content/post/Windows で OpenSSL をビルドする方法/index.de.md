---
date: 2023-04-07T21:06:32+09:00
lastmod: 2026-11-25
title: 'Schritte und Umgebungseinrichtung zum Kompilieren und Installieren von OpenSSL unter Windows'
slug: "Windows で OpenSSL をBuildする方法"
tags: ["Windows", "OpenSSL", "Kompilierung", "C++"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Anleitung zum Build von OpenSSL aus dem Quellcode unter Windows mit OpenSSL 3.5.9 als Beispiel und den Werkzeugen und Schritten für x64."
---

# Was ist OpenSSL?

Für die Verwendung von OpenSSL in einer Anwendung benötigen Sie Entwicklungsheader und Bibliotheken. Sie können eine Binärdistribution beziehen oder den Quellcode je nach Bedarf selbst bauen; diese Seite beschreibt den Build aus dem Quellcode.

Below, we will introduce the build procedure.
# Vorbereitung der Build-Umgebung

- **Perl**

  Laden Sie `strawberry-perl-5.42.3.1-64bit.msi` von [https://strawberryperl.com/](https://strawberryperl.com/) herunter. Die neueste Version sollte in Ordnung sein.

- **NASM**

  Laden Sie `3.02/nasm-3.02-win64.zip` unter `Download` von [https://www.nasm.us/](https://www.nasm.us/) herunter. Die neueste Non-RC-Version sollte in Ordnung sein.
  Nach der Installation müssen Sie den Ordner, in dem NASM installiert ist, in der Umgebungsvariablen PATH registrieren.

- **Visual Studio 2022** oder **Build Tools for Visual Studio 2022**

  Installieren Sie `Visual Studio 2022 Community` oder `Build Tools for Visual Studio 2022` von [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/).
  
# OpenSSL-Build-Prozedur unter Windows

1. Laden Sie `openssl-3.5.9.tar.gz` von [https://openssl-library.org/source/](https://openssl-library.org/source/) herunter und entpacken Sie es. Wenn Sie es nicht entpacken können, führen Sie `tar -xzf openssl-3.5.9.tar.gz` in der Eingabeaufforderung aus.

Am 25.11.2026 gehört OpenSSL 3.5.9 zur unterstützten LTS-Reihe 3.5, die bis zum 08.04.2030 unterstützt wird. Prüfen Sie beim Build auf der offiziellen Downloadseite den neuesten unterstützten Patchstand.

2. Verwenden Sie die x64-Entwicklereingabeaufforderung von Visual Studio. Starten Sie sie nur dann als Administrator, wenn Sie unter Program Files installieren.
3. Öffnen Sie den entpackten Ordner.
4. Führen Sie den folgenden Befehl aus. *Ändern Sie den Teil `Community`, damit er Ihrer installierten Version von Visual Studio entspricht.
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
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
Die Installation an diesem Standardziel benötigt Administratorrechte. Geben Sie bei der Konfiguration ein beschreibbares prefix an, wenn Sie keine erhöhten Rechte nutzen möchten.

Das ist alles.

# Referenzen

- [OpenSSL supported releases and lifecycle](https://openssl-library.org/source/)
- [OpenSSL Windows build notes](https://github.com/openssl/openssl/blob/master/NOTES-WINDOWS.md)
- [OpenSSL build and install guide](https://github.com/openssl/openssl/blob/master/INSTALL.md)
- [Microsoft: x64 MSVC command prompt](https://learn.microsoft.com/en-us/cpp/build/how-to-enable-a-64-bit-visual-cpp-toolset-on-the-command-line?view=msvc-170)
- [NASM stable releases](https://www.nasm.us/)
- [Strawberry Perl for Windows](https://strawberryperl.com/)