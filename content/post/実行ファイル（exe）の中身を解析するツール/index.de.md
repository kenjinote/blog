---
title: "Tools zur Analyse des Inhalts einer ausführbaren Datei (exe)"
slug: "tools-zur-analyse-des-inhalts-einer-ausfuehrbaren-datei-exe"
date: 2023-04-05T23:31:06+09:00
tags: ["windows", "exe", "ausführbare datei", "analyse"]
draft: false
image: "img_1.png"
categories: ["PC und Gadgets"]
---

# Was ist eine ausführbare Datei (exe)?

Eine ausführbare Datei unter Windows. Sie ist im Allgemeinen in einem Format geschrieben, das als PE-Format bekannt ist.
Sie enthält Maschinencode zur Ausführung sowie Ressourcen wie Symbole und Bilder.

Da es mehrere Tools zur Analyse von ausführbaren Dateien gibt, werde ich diese hier vorstellen.

## 7-Zip

![img.png](img.png)

EXE-Dateien werden manchmal komprimiert erstellt, da ihre Größe ansonsten sehr groß werden könnte. In diesem Fall können Sie durch die Verwendung der Dateikomprimierungs- und Dekomprimierungssoftware 7-Zip die ausführbare Datei entpacken und ihren Inhalt untersuchen. Ein weiteres Tool, das auf ähnliche Weise entpacken kann, ist WinRAR.

## Resource Hacker
![img_2.png](img_2.png)

Sie können Ressourcen (Symbole, Bitmaps, Dialogfelder, Zeichenfolgen usw.) extrahieren, die sich in der EXE-Datei befinden. Da es auch als Hex-Editor fungiert, können Sie den Inhalt der EXE-Datei bearbeiten und umschreiben.

## PE Explorer
![img_3.png](img_3.png)

Sie können PE-Dateien (EXE, DLL, OCX, SYS, Treiber) für Windows analysieren. PE Explorer bietet verschiedene Analysefunktionen, wie die Anzeige der Dateistruktur, des Dateiheaders, der Verzeichniseinträge und der exportierten Funktionen und Symbole.

## Dependency Walker
![img_4.png](img_4.png)

Sie können die DLL-Dateien untersuchen, von denen eine EXE-Datei abhängt, und überprüfen, ob sie korrekt geladen werden. Sie können auch Funktionsaufrufe von DLL-Dateien verfolgen.

## Ghidra

![img_5.png](img_5.png)

Ein leistungsstarkes Reverse-Engineering-Tool, das von der NSA (National Security Agency der USA) entwickelt und als Open Source kostenlos veröffentlicht wurde. Es ist sehr beliebt, da es nicht nur EXE-Dateien disassemblieren (in Assemblersprache umwandeln) kann, sondern auch eine Dekompilierungsfunktion in eine Form bietet, die der C-Sprache nahekommt.

## IDA Free / IDA Pro

![img_6.png](img_6.png)

Ein hochfunktionaler Disassembler und Dekompiler, der zum weltweiten Industriestandard für die Malware-Analyse und das Reverse Engineering geworden ist. Die Pro-Version ist sehr teuer, aber Sie können die funktionseingeschränkte "IDA Free"-Version für den persönlichen oder nicht-kommerziellen Gebrauch kostenlos nutzen.

## x64dbg (x32dbg)

![img_7.png](img_7.png)

Ein Open-Source-Debugger für Windows. Er ist auf die "dynamische Analyse" spezialisiert, bei der der Inhalt und der Speicherstatus durch schrittweise Ausführung analysiert werden, während die ausführbare Datei ausgeführt wird. Er wird häufig zum Entschlüsseln von Crackmes (Aufgabenprogramme zur Analyse) und zur Untersuchung des Verhaltens von Malware verwendet.

## ILSpy / dotPeek

![img_8.png](img_8.png)

Wenn die Ziel-EXE-Datei in einer .NET-Sprache wie C# geschrieben ist, können Sie diese Tools verwenden, um sie fast auf den Zustand des ursprünglichen Quellcodes zu dekompilieren (Rückübersetzung) und ihren Inhalt vollständig offenzulegen.

Diese Tools sind nützlich, um den Inhalt von EXE-Dateien zu untersuchen, aber Vorsicht ist geboten. Das Bearbeiten von Dateien oder deren Nutzung für illegale Zwecke kann urheberrechtliche oder sicherheitsrelevante Probleme verursachen. Verwenden Sie sie daher nur mit ausreichendem Verständnis.
