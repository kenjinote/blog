---
title: "【Für Anfänger】Schritte zur Installation von libcurl (mit OpenSSL-Unterstützung) in Visual Studio mit vcpkg"
slug: "vcpkg を使って Visual Studio に curl をインストール"
date: 2025-07-07T21:46:08+09:00
tags: ["vcpkg", "curl", "Visual Studio", "C++"]
draft: false
image: "img.png"
categories: ["Werkzeuge und Entwicklungsumgebung"]
---

## Wenn Sie libcurl (mit OpenSSL-Unterstützung) in Visual Studio verwenden möchten, ist die Installation von vcpkg einfach und empfehlenswert

Wenn es darum geht, HTTP-Kommunikation in C++ zu behandeln, wird oft libcurl verwendet. Aber das Kompilieren und Anpassen von Abhängigkeiten ist überraschend mühsam, nicht wahr?

In solchen Fällen ist das C++-Bibliotheksverwaltungstool von Microsoft, ** "vcpkg" ** , sehr nützlich.
Dieses Mal stellen wir die Schritte von der Einführung von libcurl (OpenSSL-kompatibel) mit cpkg bis hin zur reibungslosen Nutzung in Visual Studio vor.

---

### Installation von vcpkg (nur für diejenigen, die es noch nicht installiert haben)

Lassen Sie uns zuerst cpkg installieren. Bitte führen Sie die folgenden Schritte in PowerShell aus.

`powershell
git clone https://github.com/microsoft/vcpkg
cd vcpkg
.ootstrap-vcpkg.bat
`

※Wenn Git noch nicht installiert ist, installieren Sie es bitte von der [Offiziellen Git-Website](https://git-scm.com/).

---

### Installation von libcurl (OpenSSL-kompatibel)

Als Nächstes verwenden wir vcpkg, um libcurl zu installieren. Um die 64-Bit-Version mit OpenSSL-Unterstützung anzugeben, führen Sie den folgenden Befehl aus.

`powershell
vcpkg install curl[ssl] --triplet x64-windows
`

Wenn Sie diesen Befehl ausführen, werden notwendige Abhängigkeiten (wie OpenSSL) automatisch mit eingerichtet.

---

### Integrationseinstellungen für Visual Studio

Um die mit vcpkg eingeführten Bibliotheken einfach in Ihrem Visual Studio-Projekt verwenden zu können, konfigurieren Sie die Integrationseinstellungen mit dem folgenden Befehl.

`powershell
vcpkg integrate install
`

Sobald dies eingerichtet ist, steht #include <curl/curl.h> in Visual Studio-Projekten automatisch zur Verfügung, und Sie müssen Bibliothekspfade oder Linker-Einstellungen nicht mehr manuell vornehmen.

---

## Fazit

Damit ist die Vorbereitung zur Einführung von libcurl (OpenSSL-kompatibel) in Visual Studio abgeschlossen.

* Mit vcpkg können Sie mühsame Abhängigkeiten auf einmal verwalten
* Installieren Sie libcurl ganz einfach mit cpkg install curl[ssl] --triplet x64-windows
* Eine automatische Integration mit Visual Studio ist mit cpkg integrate install möglich

Jetzt müssen Sie nur noch den Header in Ihr Projekt einbinden und die libcurl-API verwenden, um mit der Entwicklung zu beginnen.
Nutzen Sie das praktische vcpkg, um Ihre Entwicklungseffizienz auf einen Schlag zu steigern.
