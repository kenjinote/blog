---
title: "Salesforce-Chatter-Beiträge bereinigen: Speicher und sichere Schritte"

slug: "SalesforceChatter全消しBefehl"
date: 2022-09-19T21:59:14+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "Chatter-Beiträge zählen nicht zum Salesforce-Datenspeicher. Prüfen Sie den Speichertyp, sichern und kontrollieren Sie ausgewählte Beiträge und löschen Sie sie anschließend sicher mit Data Loader."
---
**Wichtig:** Chatter-Beiträge, Kommentare und nachverfolgte Änderungen werden nicht auf den Salesforce-Datenspeicher angerechnet. Anhänge zählen zum Dateispeicher. Prüfen Sie zuerst **Storage Usage** in Setup, welche Speicherart nahezu ausgeschöpft ist. Das Löschen aller Beiträge gibt keinen Datenspeicher frei.

## Beiträge mit Anhängen sicher prüfen

Das folgende SOQL-Beispiel ist schreibgeschützt. Es listet Beiträge mit Dateianhängen (`Type = 'ContentPost'`) zur Prüfung auf und löscht nichts.

```sql
SELECT Id, CreatedDate, CreatedById, ParentId, Type
FROM FeedItem
WHERE Type = 'ContentPost'
ORDER BY CreatedDate ASC
```

1. Exportieren Sie mögliche IDs mit Data Loader oder Workbench und grenzen Sie sie nach Datum, Autor, übergeordnetem Datensatz oder anderen genehmigten Kriterien ein.
2. Prüfen Sie den Sicherungs- und Wiederherstellungsplan der Organisation und testen Sie den Ablauf in einer Sandbox. Lassen Sie IDs und Löschanzahl von Administrator und Dateneigentümer prüfen.
3. Löschen Sie nach Freigabe ausschließlich die ausgewählten IDs mit Data Loader. Auch das von Salesforce dokumentierte Massenverfahren exportiert zuerst FeedItem-IDs mit `Type = ContentPost`.

Das Löschen eines FeedItem kann endgültig sein und den Papierkorb umgehen, sodass eine Wiederherstellung möglicherweise unmöglich ist. Beim Löschen eines Beitrags wird der Anhang aus dem Feed entfernt; ob die Datei am ursprünglichen Ort oder in anderen Freigaben verbleibt, hängt von ihrem Status ab. Löschen Sie nicht ungefiltert alle `ContentDocument` und leeren Sie nicht den gesamten Papierkorb. Prüfen Sie für die Bereinigung des Dateispeichers Storage Usage sowie Eigentümer, Freigaben und Auswirkungen jeder Datei.

## Quellen

- [Work with Chatter Posts — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_posts_parent.htm&language=en_US&type=5)
- [Data and Storage Resources — Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.admin_monitorresources.htm&language=en_US&type=5)
- [Mass Delete Chatter Feed Item records that contain an attachment — Salesforce Help](https://help.salesforce.com/s/articleView?id=000198685&language=en_US&type=1)
- [FeedItem — Salesforce Developers](https://developer.salesforce.com/docs/platform/object-reference/references/standard-objects/object-feeditem.html)
- [Delete Files and Links from Chatter Feeds — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_attachments_del.htm&language=en_US&type=5)
