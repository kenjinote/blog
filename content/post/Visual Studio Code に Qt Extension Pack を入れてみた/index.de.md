---
title: "Ich habe versucht, das Qt Extension Pack in Visual Studio Code zu installieren"
slug: "Visual Studio Code に Qt Extension Pack を入れてみた"
date: 2024-09-13T00:53:53+09:00
tags: ["Visual Studio Code", "Qt Extension Pack"]
draft: false
image: "img_1.png"
categories: ["ツール・開発環境"]
---

# Starten der Qt-Entwicklung in VSCode: So installieren Sie das Qt Extension Pack

Hallo, hier ist Kenji.
Dieses Mal werde ich vorstellen, „wie man die Qt-Entwicklungsumgebung in Visual Studio Code (im Folgenden VSCode) einrichtet“.

In letzter Zeit möchten neben dem offiziellen Qt Creator immer mehr Menschen Qt-Apps mit VSCode entwickeln, das leichtgewichtig und in hohem Maße erweiterbar ist.
Für diese Personen empfehle ich das **"Qt Extension Pack"** .
Wenn Sie dieses Erweiterungspaket installieren, erhalten Sie auf einen Schlag die wichtigsten Qt-bezogenen Erweiterungen.

---

## Zielpublikum

* Diejenigen, die mit der Entwicklung von GUI-Apps mit Qt beginnen möchten
* Diejenigen, die in VSCode statt im Qt Creator entwickeln möchten
* Diejenigen, die es mühsam finden, Erweiterungen einzeln zu suchen

---

## Voraussetzungen

* VSCode muss installiert sein
  ([Sie können es kostenlos von der offiziellen Website herunterladen](https://code.visualstudio.com/))
* Die Qt-Bibliothek selbst muss installiert sein ([Offizielle Qt-Website](https://www.qt.io/))

---

## Was ist das Qt Extension Pack?

Das Qt Extension Pack ist ein Erweiterungspaket für VSCode.
Durch die Installation werden die folgenden Funktionen automatisch hinzugefügt:

* Unterstützung für `.ui`-Dateien (Qt Designer)
* Syntax-Hervorhebung für `.pro`- und `.qrc`-Dateien
* C++-Code-Vervollständigung, Build- und Debugging-Unterstützung für Qt
* Qt Resource Browser (Ressourcenreferenz)

---

## Installationsanweisungen

### 1. VSCode öffnen

Starten Sie zunächst VSCode.

### 2. Erweiterungsansicht öffnen

Klicken Sie auf die Aktivitätsleiste auf der linken Seite (quadratisches Block-Symbol), um die „Erweiterungen“ anzuzeigen.

Oder Sie können die Tastenkombination
`Ctrl + Shift + X` drücken.

### 3. Nach "Qt Extension Pack" suchen

Geben Sie das folgende Schlüsselwort in die Suchleiste ein:

```
Qt Extension Pack
```

![img.png](img.png)

### 4. Auf die Schaltfläche "Installieren" klicken

Wenn das Zielpaket angezeigt wird, klicken Sie auf die Schaltfläche „Installieren“.
Dadurch werden mehrere Erweiterungen auf einmal installiert, wie zum Beispiel die folgenden:

* Qt Language Support
* QML Support
* Qt Designer Integration
* CMake Tools (unerlässlich für die CMake-kompatible Qt-Entwicklung)

---

## Zusätzliche Projekteinstellungen (Beispiel CMake + Qt)

Wenn Sie das CMake-basierte Qt verwenden, empfehlen wir die Kombination mit den folgenden Erweiterungen:

* [CMake Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)
* [CMake Language Support](https://marketplace.visualstudio.com/items?itemName=twxs.cmake)

Wenn Sie außerdem die folgende Beschreibung in die CMakeLists.txt einfügen, verläuft die Integration mit Qt reibungslos:

```cmake
find_package(Qt6 REQUIRED COMPONENTS Widgets)
target_link_libraries(MyApp PRIVATE Qt6::Widgets)
```

---

## Bonus: Wie öffne ich .ui-Dateien?

`.ui`-Dateien können im Qt Designer bearbeitet werden.
In VSCode können Sie mit der rechten Maustaste auf die `.ui`-Datei klicken → `Open with Qt Designer` auswählen (Qt Designer muss in der Umgebungsvariablen `PATH` enthalten sein).

---

## Zusammenfassung

| Schritt | Inhalt                          |
| -- | --------------------------- |
| 1  | VSCode starten                    |
| 2  | Erweiterungspanel öffnen                  |
| 3  | Nach "Qt Extension Pack" suchen |
| 4  | Auf die Schaltfläche Installieren klicken              |

Der Aufbau einer Qt-Umgebung in VSCode ist viel einfacher geworden als früher.
Es verfügt über genügend Funktionen als Alternative zum Qt Creator und ist für diejenigen zu empfehlen, die leichtgewichtig arbeiten möchten.

---

## Empfohlene Linksammlung

* [Qt Offiziell](https://www.qt.io/)
* [Qt Extension Pack - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=TheQtCompany.qt)
* [VSCode Offiziell](https://code.visualstudio.com/)
* [CMake Tools Erweiterung](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)

---

## Zum Schluss

In Zukunft plane ich, die Entwicklung unter Verwendung der UI-Tools von Qt und QML in dieser Umgebung voranzutreiben.
Beim nächsten Mal werde ich erklären, **wie man eine Qt Hello World-App aus VSCode heraus erstellt und ausführt** .

Bis bald!
