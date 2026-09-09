---
title: 'Salesforce: Befehl zum vollständigen Löschen von Chatter-Beiträgen und Anhängen'
slug: "Salesforceチャッター全消しコマンド"
date: 2022-09-19T21:59:14+09:00
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.webp"
categories: ["IT und Technologie"]
description: 'Stellt einen Befehl vor, der nützlich ist, wenn die Speicherkapazität der Organisation in Salesforce knapp wird, um alle Chatter-Beiträge, Anhänge und Papierkorbdaten stapelweise zu löschen. Dies ist eine Methode zur schnellen Bereinigung unter Verwendung des Fensters für anonyme Ausführung in der Developer Console.'
---
# Salesforce Chatter Alles Löschen Befehl
Dies ist ein Befehl, um alle Beiträge und Anhänge in Salesforce Chatter zu löschen.
Öffnen Sie die Developer Console, wählen Sie im Menü Debug die Option "Open Execute Anonymous Window", fügen Sie den folgenden Code ein und führen Sie ihn aus.
Ich persönlich verwende dies, wenn die Speicherkapazität der Organisation knapp wird.

```
delete [select id from FeedItem];
delete [select id from FeedAttachment];
delete [select id from ContentDocument];

// Papierkorb leeren
database.emptyRecycleBin([select id from ContentDocument where IsDeleted = true ALL ROWS]);
```
