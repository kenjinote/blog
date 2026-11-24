---
title: 'Warum für Icons, die mit der Funktion LoadIcon abgerufen wurden, kein DestroyIcon erforderlich ist'
slug: "LoadIconはDestroyIconを呼び出す必要はない"
date: 2024-04-19T01:55:17+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["Symbol", "LoadIcon", "DestroyIcon", "Windows-Programmierung"]
draft: false
categories: ["programming"]
description: 'Ob DestroyIcon erforderlich ist, hängt davon ab, ob das Handle auf eine gemeinsam genutzte oder vom Aufrufer verwaltete Ressource verweist. Diese Anleitung erläutert LoadIcon, LoadImage und CopyIcon sowie widersprüchliche Microsoft-Dokumentation zu einigen Erstellungs-APIs.'
image: eyecatch.jpg
---

# Besitz von Icon-Handles

Ob `DestroyIcon` aufgerufen werden muss, hängt davon ab, ob das Icon gemeinsam genutzt wird oder dem Aufrufer gehört und von ihm freigegeben werden muss. Das Zerstören eines gemeinsam genutzten Icons kann andere Codeabschnitte beeinträchtigen, die dieselbe Ressource verwenden.

## Wann DestroyIcon nicht aufgerufen wird

- Ein von `LoadIcon` zurückgegebenes Icon wird gemeinsam genutzt. Rufen Sie dafür nicht `DestroyIcon` auf. `LoadIcon` lädt ein Icon in der Standardgröße der Systemmetriken; für eine bestimmte Größe verwenden Sie `LoadImage`.
- Wird `LR_SHARED` an `LoadImage` übergeben, ist das Handle gemeinsam genutzt. Rufen Sie `DestroyIcon` nicht auf. Verwenden Sie `LR_SHARED` nicht für Bilder aus Dateien oder für nicht standardmäßige Größen.
- `CopyImage` kann das ursprüngliche Handle zurückgeben, wenn `LR_COPYRETURNORG` gesetzt und das Eingabe-`hImage` ein gemeinsam genutztes Icon ist. Zerstören Sie dieses Handle nicht.

## Wann DestroyIcon aufgerufen wird

Geben Sie Icons, die dem Aufrufer gehören, nach der Verwendung mit `DestroyIcon` frei. Microsoft nennt folgende Beispiele:

- `CreateIconFromResourceEx` ohne `LR_SHARED`
- `CreateIconIndirect`
- `CopyIcon`, das ein dupliziertes Icon-Handle zurückgibt
- Ein mit `LoadImage` ohne `LR_SHARED` geladenes Icon

## Hinweis zu CreateIconFromResource

Die allgemeine Microsoft-Dokumentation zu `DestroyIcon` führt `CreateIconFromResource` als Quelle gemeinsam genutzter Icons auf; die einzelnen Funktionsseiten sagen dagegen, dass `DestroyIcon` aufgerufen werden soll. Auch die Seiten zu `CreateIconFromResource` und `CreateIconFromResourceEx` widersprechen sich intern bezüglich `LR_SHARED` und der Freigabe des zurückgegebenen Handles. Leiten Sie die Besitzverhältnisse bei diesen APIs nicht allein aus der allgemeinen Regel ab, sondern prüfen Sie die aktuelle Dokumentation der jeweiligen Funktion. Dieser Widerspruch ist unabhängig vom Verhalten gemeinsam genutzter `LoadIcon`-Handles.

Ein an `DestroyIcon` übergebenes Icon darf nicht verwendet werden. Prüfen Sie, ob das Handle gemeinsam genutzt wird und ob sein Quellmodul noch geladen ist.

## Quellen

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
