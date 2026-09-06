---
title: "Einführung in vim"
slug: "vim入門"
date: 2024-04-19T22:06:34+09:00
tags: ["vim", "Texteditor"]
draft: false
image: "img.png"
categories: ["Tools und Entwicklungsumgebung"]
---

![img_1.png](img_1.png)

# Einführung in vim

## Download und Installation

[https://www.vim.org/download.php](https://www.vim.org/download.php)

Laden Sie von der obigen Website das entsprechende Modul für Ihr Betriebssystem herunter und installieren Sie es.

Für Windows ist die Wahl von `gvim_X.X.X_x64_signed.exe` eine gute Option.

## Starten

Unter Windows müssen Sie den Ordner, der `vim.exe` enthält, in der Umgebungsvariable Path registrieren.

Wie man startet:

```
vim
```

Um mit Angabe eines Dateinamens zu starten:

```
vim filename.txt
```

## Beenden

Um zu beenden, geben Sie `:` (Doppelpunkt) ein, gefolgt von `q`, und drücken Sie die Eingabetaste.
```
:q
```

Wenn die Datei geändert wurde, wird `Kein Schreibvorgang seit der letzten Änderung (fügen Sie ! hinzu, um das Verwerfen zu erzwingen)` angezeigt.
Sie können das Beenden erzwingen, indem Sie die Änderungen verwerfen.
```
:q!
```

Um die Datei zu speichern und zu beenden:
```
:wq
```

Das Folgende hat ebenfalls die gleiche Bedeutung:
```
:x
```

Sie können auch beenden, indem Sie `Shift` gedrückt halten und zweimal `z` drücken. (Gleichwertig zu :wq)

## Modi

Der vim verfügt über einen `Kommandomodus` und einen `Einfügemodus`. Beim Start von vim befindet er sich im `Kommandomodus`, und das Drücken der `i`-Taste wechselt in den `Einfügemodus`.

Im `Einfügemodus` können Sie, wie der Name schon sagt, Text eingeben. Um vom `Einfügemodus` zurück in den `Kommandomodus` zu wechseln, drücken Sie die `ESC`-Taste.

Dieser Wechsel der Eingabemodi ist ein Hauptmerkmal von vim.

## Cursorbewegung und Scrollen

Zusammenfassung der Cursorbewegung und des Scrollens im `Kommandomodus`.

| Taste                                | Beschreibung                    |
|------------------------------------|-------------------------|
| `h` (oder `Ctrl`+`H`, `BackSpace`, `←`) | Nach links bewegen      |
| `j` (oder `Ctrl`+`J` / `N`, `↓`)         | Nach unten bewegen      |
| `k` (oder `Ctrl`+`P`, `↑`)             | Nach oben bewegen       |
| `l` (oder `Space`, `→`)               | Nach rechts bewegen     |
| `+` (oder `Enter`)                   | Zum Anfang der nächsten Zeile bewegen |
| `-`                                | Zum Anfang der vorherigen Zeile bewegen |
| `Ctrl`+`B` (oder `PageUp`)            | Nach oben scrollen (Seite) |
| `Ctrl`+`F` (oder `PageDown`)          | Nach unten scrollen (Seite) |
| `Ctrl`+`U`                         | Eine halbe Seite nach oben scrollen |
| `Ctrl`+`D`                         | Eine halbe Seite nach unten scrollen |
| `Ctrl`+`Y`                         | Eine Zeile nach oben scrollen |
| `Ctrl`+`E`                         | Eine Zeile nach unten scrollen |
| `z` `Enter`                        | Zeile mit dem Cursor an den oberen Bildschirmrand scrollen |
| `z` `.`                            | Zeile mit dem Cursor in die Bildschirmmitte scrollen |
| `z` `-`                            | Zeile mit dem Cursor an den unteren Bildschirmrand scrollen |
| `0` (oder `\|`)                       | Cursor an den Zeilenanfang bewegen |
| `$`                                | Cursor an das Zeilenende bewegen |
| `^` (oder `_`)                        | Cursor an den Zeilenanfang bewegen (ohne Leerzeichen und Tab) |
| `G` (oder `:$`)                       | Cursor zur letzten Zeile bewegen |
| `:zeilennummer` `Enter`                     | Zur angegebenen Zeile bewegen |

Indem Sie eine `Zahl` vor den obigen Bewegungstasten eingeben, können Sie sich um diese Anzahl mehrfach bewegen.
(Zum Beispiel bewegt die Eingabe von `3j` Sie um 3 Zeilen von der aktuellen Cursorposition nach unten.)

## Andere Befehle

| Taste        | Beschreibung                 |
|------------|----------------------|
| `Ctrl`+`L` | Bildschirm neu zeichnen      |
| `Ctrl`+`G` | Gesamtzeilenzahl der Datei, Cursorposition usw. anzeigen |
