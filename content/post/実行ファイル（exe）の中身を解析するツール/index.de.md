---
title: "Tools zur Analyse des Inhalts einer ausführbaren Datei (exe)"
slug: "tools-zur-analyse-des-inhalts-einer-ausfuehrbaren-datei-exe"
date: 2023-04-05T23:31:06+09:00
tags: ["windows", "exe", "ausführbare Datei", "Analyse"]
draft: false
image: "img_1.png"
categories: ["PC & Gadgets"]
---

# Was ist eine ausführbare Datei (exe)?

Eine unter Windows ausführbare Datei. Sie ist grundsätzlich in einem Format geschrieben, das als PE-Format bezeichnet wird.
Sie enthält Maschinencode zur Ausführung sowie Ressourcen wie Symbole und Bilder.

Es gibt mehrere Tools zur Analyse ausführbarer Dateien, und diese stellen wir dieses Mal vor.

## 7-Zip

![img.png](img.png)

EXE-Dateien werden manchmal durch Dateikomprimierung erstellt, da sie im Originalzustand oft sehr groß werden. In diesem Fall können Sie mit der Dateikomprimierungs- und Extraktionssoftware 7-Zip die ausführbare Datei entpacken und ihren Inhalt untersuchen. WinRAR ist ein weiteres Tool, das auf ähnliche Weise entpacken kann.

## Resource Hacker
![img_2.png](img_2.png)

Ermöglicht das Extrahieren von Ressourcen (Symbole, Bitmaps, Dialogfelder, Zeichenfolgen usw.), die sich in EXE-Dateien befinden. Es fungiert auch als Hex-Editor, sodass Sie den Inhalt von EXE-Dateien bearbeiten und umschreiben können.

## PE Explorer
![img_3.png](img_3.png)

Kann PE-Dateien (EXE, DLL, OCX, SYS, Treiber) für Windows analysieren. PE Explorer bietet verschiedene Analysefunktionen, wie z.B. die Anzeige der Dateistruktur, des Datei-Headers, der Verzeichniseinträge sowie exportierter Funktionen und Symbole.

## Dependency Walker
![img_4.png](img_4.png)

Sie können die DLL-Dateien überprüfen, von denen eine EXE-Datei abhängt, und bestätigen, ob sie korrekt geladen wurden. Außerdem können Sie Funktionsaufrufe von DLL-Dateien verfolgen.

Obwohl diese Tools nützlich sind, um den Inhalt von EXE-Dateien zu untersuchen, ist Vorsicht geboten. Das Ändern von Dateien oder deren Nutzung für unbefugte Zwecke kann zu Sicherheitsproblemen oder Urheberrechtsverletzungen führen. Stellen Sie daher sicher, dass Sie dies vor der Verwendung vollständig verstanden haben.
