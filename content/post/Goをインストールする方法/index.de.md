---
title: "Go installieren und das erste Programm ausführen"
slug: "GoをInstallationする方法"
date: 2022-09-10T00:48:17+09:00
lastmod: 2026-11-23
lastmod: 2026-11-23
lastmod: 2026-11-23
tags: ["Go", "Installation"]
draft: false
image: "images/cover.webp"
categories: ["programming"]
description: "Installieren Sie Go unter Windows, macOS oder Linux, prüfen Sie die Installation mit go version, erstellen Sie ein Modul und führen Sie Hello World aus."
---

# Über Go

Go wurde bei Google begonnen und wird heute als Open-Source-Projekt weiterentwickelt. Es ist eine statisch typisierte, kompilierte Sprache. Go unterstützt Zeiger, aber keine Zeigerarithmetik; die Laufzeit enthält eine Garbage Collection.

# Go installieren

Öffnen Sie die [offizielle Anleitung zum Herunterladen und Installieren](https://go.dev/doc/install) und wählen Sie die Schritte für Ihr Betriebssystem (Windows, macOS oder Linux) und Ihre CPU-Architektur. Folgen Sie der offiziellen Anleitung, öffnen Sie anschließend ein neues Terminal und führen Sie Folgendes aus:

```sh
go version
```

Wenn der Befehl eine Versionsnummer ausgibt, ist `go` verfügbar. Folgen Sie beim Aktualisieren den offiziellen Anweisungen zum Ersetzen der vorhandenen Installation; entpacken Sie eine neue Version nicht über eine vorhandene Installation. Hinweise zur Versionsverwaltung finden Sie unter [Go-Installationen verwalten](https://go.dev/doc/manage-install).

# Hello, World ausführen

Erstellen Sie einen Arbeitsordner und initialisieren Sie darin ein Modul:

```sh
mkdir hello
cd hello
go mod init example/hello
```

Erstellen Sie darin die Datei `hello.go` und speichern Sie diesen Code:

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

Führen Sie das Programm so aus:

```sh
go run .
```

Die Ausgabe lautet `Hello, World!`. Mit `go build` erstellen Sie eine ausführbare Datei. Name und Erweiterung hängen vom Betriebssystem ab; unter Windows wird normalerweise `.exe` verwendet.

# Weiterlernen

- [Offizielles Go-Tutorial: Erste Schritte](https://go.dev/doc/tutorial/getting-started)
- [Go-FAQ](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/) (Code im Browser ausprobieren)

Offizielle Einführungsmaterialien sind überwiegend auf Englisch verfügbar.
