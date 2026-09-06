---
title: "Windows-Tastenkombinationen und kleine Tricks"
slug: "windows-tastenkombinationen-und-kleine-tricks"
date: 2022-09-18T23:49:29+09:00
tags: ["Windows", "Tipps", "Tastenkombinationen"]
draft: false
image: "img.png"
categories: ["PC und Gadgets"]
---
Dies ist eine Sammlung von kleinen Tricks für den alltäglichen Gebrauch unter Windows. Ich würde mich freuen, wenn Windows-Anfänger dies lesen.
Es ist für Windows 11 gedacht, aber ich denke, viele davon können auch unter Windows 10 verwendet werden.

## Fenster schließen
- `Alt + F4` während das Fenster aktiv ist
- `Ctrl + W` während das Fenster aktiv ist. Schließt den Tab oder das Fenster (nur bei unterstützten Anwendungen)
- Doppelklick auf das Symbol links in der Titelleiste des Fensters
- Klick auf das `×` in der Titelleiste des Fensters

## Desktop anzeigen
- `Win + D`. Zweimaliges Drücken kehrt zum ursprünglichen Fensterzustand zurück. Nützlich, wenn Sie den Desktop nur für einen Moment sehen möchten.
- `Win + M`. Alle Anwendungen minimieren. Zweimaliges Drücken macht dies nicht rückgängig.

## Spracheingabe
- `Win + H`. Startet die Spracheingabe. Um die Spracheingabe zu beenden, drücken Sie `Esc` oder erneut `Win + H`.

## Klassisches Rechtsklick-Menü im Explorer anzeigen
- `Shift + F10` oder die Anwendungstaste drücken. Die Anwendungstaste befindet sich unten rechts auf der Tastatur.

## Bereich auswählen und Bildschirm aufnehmen
- Mit `Win + Shift + S` können Sie einen Bereich auswählen und den Bildschirm aufnehmen.
- Mit `Win + Print Screen` oder einfach `Print Screen` können Sie den gesamten Bildschirm aufnehmen.
(Wenn Sie `Win` hinzufügen, wird das aufgenommene Bild in `C:\Users\Benutzername\Pictures\Screenshots` gespeichert.)
- Mit `Alt + Print Screen` können Sie das aktuelle Fenster aufnehmen.

## In der Taskleiste angeheftete Apps starten
- Mit `Win + Zifferntaste` können Sie in der Taskleiste angeheftete Apps starten.  
  Zum Beispiel startet `Win + 1` die erste App von links in der Taskleiste.
- Mit `Win + T` können Sie den Fokus auf die Taskleistensymbole verschieben. Durch mehrmaliges Drücken von `Win + T` oder
  mit `←` oder `→` können Sie die Auswahl verschieben und die ausgewählte App mit der `Enter` -Taste starten.

## Vergrößern/Verkleinern
- `Win + +` startet die Windows-Bildschirmlupe. Weiterhin können Sie mit `Win + + oder -` den Bildschirm vergrößern oder verkleinern.
- Im Editor oder Browser können Sie mit `Ctrl + + oder -` vergrößern oder verkleinern (nur bei unterstützten Apps).

## Windows sperren
- `Win + L`
- `Ctrl + Alt + Del` → `Space` oder `Enter`

## Windows herunterfahren
- Wenn der Desktop mit `Win + M` oder `Win + D` angezeigt wird oder die Taskleiste mit `Win + T` oder `Win + B` aktiv ist, drücken Sie `Alt + F4`, woraufhin der folgende Dialog angezeigt wird. Stellen Sie sicher, dass "Herunterfahren" ausgewählt ist, und drücken Sie `Enter`.
  `Win + R` → `Alt + F4` → `Alt + F4` ist ebenfalls möglich.
  ![img_20.png](img_20.png)
- Mit `Win + X` → `U` → `U` können Sie herunterfahren.
- Sie können herunterfahren, indem Sie `shutdown /s /t 0` in die Eingabeaufforderung oder den "Ausführen"-Dialog (`Win + R`) eingeben. Das Hinzufügen von `/f` erzwingt das Herunterfahren.

## Windows neu starten
- Wenn der Desktop mit `Win + M` oder `Win + D` angezeigt wird oder die Taskleiste mit `Win + T` oder `Win + B` aktiv ist, drücken Sie `Alt + F4`, woraufhin der folgende Dialog angezeigt wird. Drücken Sie einmal `↓`, wählen Sie "Neu starten" und drücken Sie `Enter`.
  `Win + R` → `Alt + F4` → `Alt + F4` ist ebenfalls möglich.
  ![img_21.png](img_21.png)
- Mit `Win + X` → `U` → `R` können Sie neu starten.
- Mit `shutdown /r /t 0` können Sie neu starten. Das Hinzufügen von `/f` erzwingt den Neustart.

## Windows in den Energiesparmodus versetzen (Standby)
- Wenn der Desktop mit `Win + M` oder `Win + D` angezeigt wird oder die Taskleiste mit `Win + T` oder `Win + B` aktiv ist, drücken Sie `Alt + F4`, woraufhin der folgende Dialog angezeigt wird. Drücken Sie einmal `↑`, wählen Sie "Energie sparen" und drücken Sie `Enter`.
  `Win + R` → `Alt + F4` → `Alt + F4` ist ebenfalls möglich.
  ![img_23.png](img_23.png)
- Sie können den Ruhezustand aktivieren, indem Sie `rundll32.exe powrprof.dll,SetSuspendState` in `Win + R` oder in der Eingabeaufforderung eingeben.

## Bei Windows abmelden (Logoff)
- Wenn der Desktop mit `Win + M` oder `Win + D` angezeigt wird oder die Taskleiste mit `Win + T` oder `Win + B` aktiv ist, drücken Sie `Alt + F4`, woraufhin der folgende Dialog angezeigt wird. Drücken Sie zweimal `↑`, wählen Sie "Abmelden" und drücken Sie `Enter`.
  `Win + R` → `Alt + F4` → `Alt + F4` ist ebenfalls möglich.
  ![img_22.png](img_22.png)
- `Win + X` → `U` → `I`
- `Ctrl + Alt + Del` → 2 mal `Tab` oder 2 mal `↓` → `Enter` oder `Space`
- Mit `logoff` können Sie sich abmelden.

## Fenster mit der Tastatur verschieben
- `Win + ←` : Nach links verschieben
- `Win + →` : Nach rechts verschieben
- `Win + ↑` : Nach oben verschieben/maximieren
- `Win + ↓` : Nach unten verschieben/minimieren
- `Win + Shift + ← oder →` : Zwischen mehreren Monitoren verschieben
- `Win + Alt + ← oder → oder ↑ oder ↓` : Fenster ohne Maximieren/Minimieren verschieben
- Im nicht minimierten Zustand `Alt + Space`, dann `M` und anschließend mit den Pfeiltasten verschieben.  
※ Da das Fenster dem Mauszeiger folgt, kann es auch gerettet werden, wenn es außerhalb des Bildschirms angezeigt wird.

## Prozesse im Task-Manager beenden
![img_24.png](img_24.png)
1. Mit `Ctrl + Shift + Esc` können Sie den Task-Manager starten.
2. Mit `Ctrl + Tab` können Sie zwischen den Tabs wechseln.
3. Nachdem Sie im Tab `Details` auf `Tab` gedrückt haben, können Sie durch Eingabe auf der Tastatur nach dem Prozessnamen (Präfix-Suche) suchen.
4. Während der Prozessname ausgewählt ist, drücken Sie die `Delete` -Taste gefolgt von der `Enter` -Taste, um den Prozess zu beenden.

## Prozesse per Befehl anhand des Prozessnamens beenden
- Mit `taskkill /f /im Prozessname` können Sie einen Prozess beenden.
Zum Beispiel können Sie mit `taskkill /f /im explorer.exe` den Explorer beenden.

## Mehrere Instanzen desselben Programms über das Taskleistensymbol starten
- Wenn Sie in der Taskleiste bei gedrückter `Shift` -Taste links klicken, können Sie mehrere Instanzen desselben Programms starten. (Nur für Apps, die dies unterstützen)

## Programme als Administrator starten
- Wenn Sie beim Starten eines Programms `Ctrl + Shift` gedrückt halten, wird das Programm mit Administratorrechten gestartet.

## Explorer starten
- Mit `Win + E` können Sie den Explorer starten.
- Mit `Win + R` rufen Sie "Ausführen" auf, geben Sie `explorer` ein und drücken Sie `Enter`.
- Mit `Ctrl + Shift + N` können Sie einen neuen Ordner erstellen.

## Eingabeaufforderung im aktuell geöffneten Pfad des Explorers öffnen
- Unter Windows 11 können Sie die Eingabeaufforderung über das Rechtsklick-Menü "Terminal" starten.
- Sie können auch `cmd` in die Adressleiste eingeben und die `Enter` -Taste drücken, um die Eingabeaufforderung zu starten.

## Zwischenablage-Verlauf anzeigen
- Mit `Win + V` können Sie den Zwischenablage-Verlauf anzeigen.
Wenn Sie zuvor kopierten Text oder Bilder auswählen, können Sie diese erneut kopieren.

## Ausführen
![img_28.png](img_28.png)
- Mit `Win + R` können Sie den Dialog "Ausführen" starten.

Im Folgenden werden einige Befehle vorgestellt, die Sie im Dialog "Ausführen" oder in der Eingabeaufforderung ausführen können.

## Edge öffnen
![img_18.png](img_18.png)
- Geben Sie `msedge` ein und drücken Sie `Enter`

## Internet Explorer 11 (IE11) öffnen
![img_25.png](img_25.png)
- Geben Sie `powershell.exe -Command "(New-Object -ComObject InternetExplorer.Application).Visible = $true"` ein und drücken Sie `Enter`

## Terminal öffnen
![img_19.png](img_19.png)
- Geben Sie `wt` ein und drücken Sie `Enter`

## Systemsteuerung öffnen
![img_15.png](img_15.png)
- Geben Sie `control` ein und drücken Sie `Enter`
- Kann auch mit `explorer.exe shell:::{26EE0668-A00A-44D7-9371-BEB064C98683}` geöffnet werden.

## Editor (Notepad) starten
![img_4.png](img_4.png)
- Geben Sie `notepad` ein und drücken Sie `Enter`  

## Taschenrechner starten
![img_5.png](img_5.png)
- Geben Sie `calc` ein und drücken Sie `Enter`

## Paint starten
![img_6.png](img_6.png)
- Geben Sie `mspaint` ein und drücken Sie `Enter`  

## PowerShell starten
![img_7.png](img_7.png)
- Geben Sie `powershell` ein und drücken Sie `Enter`  

## Visual Studio Code starten
![img_8.png](img_8.png)
- Geben Sie `code` ein und drücken Sie `Enter`

## Excel starten
![img_9.png](img_9.png)
- Geben Sie `excel` ein und drücken Sie `Enter`  
※ Nur wenn Excel installiert ist.

## Word öffnen
![img_10.png](img_10.png)
- Geben Sie `winword` ein und drücken Sie `Enter`  
※ Nur wenn Word installiert ist.

## PowerPoint öffnen
![img_11.png](img_11.png)
- Geben Sie `powerpnt` ein und drücken Sie `Enter`  
  ※ Nur wenn PowerPoint installiert ist.

## Systemkonfiguration öffnen
![img_1.png](img_1.png)
- Geben Sie `msconfig` ein und drücken Sie `Enter`  

## Systemeigenschaften öffnen
![img_2.png](img_2.png)
- Geben Sie `sysdm.cpl` ein und drücken Sie `Enter`

## Windows-Versionsinformationen öffnen
![img_27.png](img_27.png)
- Geben Sie `winver` ein und drücken Sie `Enter`

## Bildschirmtastatur öffnen
![img_14.png](img_14.png)
- Geben Sie `osk` ein und drücken Sie `Enter`

## WordPad öffnen
![img_12.png](img_12.png)
- Geben Sie `wordpad` oder `write` ein und drücken Sie `Enter`

## Registrierungs-Editor öffnen
![img_13.png](img_13.png)
- Geben Sie `regedit` ein und drücken Sie `Enter`

## Programme und Features öffnen
- Geben Sie `explorer.exe shell:::{7b81be6a-ce2b-4676-a29e-eb907a5126c5}` ein und drücken Sie `Enter`

## Tastatureigenschaften öffnen
- Geben Sie `explorer.exe shell:::{725BE8F7-668E-4C7B-8F90-46BDB0936430}` ein und drücken Sie `Enter`

## Mauseigenschaften öffnen
![img_16.png](img_16.png)
- Geben Sie `explorer.exe shell:::{6C8EEC18-8D75-41B2-A177-8831D59D2D50}` ein und drücken Sie `Enter`

## Sound öffnen
![img_3.png](img_3.png)
- Geben Sie `explorer.exe shell:::{F2DDFC82-8F12-4CDD-B7DC-D4FE1425AA4D}` ein und drücken Sie `Enter`

## Benutzerkonten öffnen
- Geben Sie `explorer.exe shell:::{60632754-c523-4b62-b45c-4172da012619}` ein und drücken Sie `Enter`

## Text der Standard-Meldungsbox kopieren
![img_26.png](img_26.png)
- Mit `Ctrl + C` können Sie den Text einer Standard-Meldungsbox kopieren.
Wenn Sie die obige Meldungsbox kopieren, wird Folgendes in die Zwischenablage kopiert.
```
[Window Title]
WordPad

[Main Instruction]
Möchten Sie die Änderungen an Dokument speichern?

[Speichern (S)] [Nicht speichern (N)] [Abbrechen]
```

## Ausgabe der Eingabeaufforderung in der Zwischenablage speichern
Durch Hinzufügen von ` | clip` (Pipe + clip) hinter einen Befehl, wie z.B. `echo "hello" | clip`, können Sie die Standardausgabe in die Zwischenablage kopieren.

## Ordnerhierarchie als Text ausgeben
In der Eingabeaufforderung können Sie mit dem Befehl `tree` die Ordnerhierarchie als Baumstruktur ausgeben.

Ausgabebeispiel
```
C:.
├─.idea
│  └─libraries
├─binaryeditorbz
├─blog
│  ├─archetypes
│  ├─content
│  ├─data
│  ├─layouts
│  ├─static
│  └─themes
│      └─PaperMod
│          ├─.git
│          │  ├─branches
│          │  ├─hooks
│          │  ├─info
│          │  ├─logs
│          │  │  └─refs
│          │  │      ├─heads
│          │  │      └─remotes
│          │  │          └─origin
│          │  ├─objects
│          │  │  ├─info
│          │  │  └─pack
│          │  └─refs
│          │      ├─heads
│          │      ├─remotes
│          │      │  └─origin
│          │      └─tags
│          ├─.github
│          │  ├─ISSUE_TEMPLATE
│          │  └─workflows
│          ├─assets
│          │  ├─css
│          │  │  ├─common
│          │  │  ├─core
│          │  │  ├─extended
│          │  │  ├─hljs
│          │  │  └─includes
│          │  └─js
│          ├─i18n
│          ├─images
│          └─layouts
│              ├─partials
│              │  └─templates
│              ├─shortcodes
│              └─_default
│                  └─_markup
(und so weiter)
```

## Referenz
- [Windows-Tastenkombinationen](https://support.microsoft.com/de-de/windows/tastenkombinationen-in-windows-dcc61a57-8ff0-cffe-9796-cb9706c75eec)
