---
title: "Salesforce Chatter Alles Löschen Befehl"
slug: "Salesforceチャッター全消しコマンド"
date: 2022-09-19T21:59:14+09:00
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.png"
categories: ["IT und Technologie"]
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
