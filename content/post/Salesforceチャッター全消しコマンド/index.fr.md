---
title: "Nettoyer les publications Salesforce Chatter : stockage et étapes sûres"

slug: "SalesforceChatter全消しCommande"
date: 2022-09-19T21:59:14+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "Les publications Chatter ne consomment pas le stockage de données Salesforce. Vérifiez le type de stockage, sauvegardez et examinez les publications ciblées, puis supprimez-les avec Data Loader."
---
**Important :** les publications, commentaires et modifications suivies de Chatter ne comptent pas dans le stockage de données Salesforce. Les fichiers joints comptent dans le stockage de fichiers. Consultez d’abord **Storage Usage** dans Setup pour savoir quelle catégorie approche sa limite. Supprimer toutes les publications ne libérera pas de stockage de données.

## Examiner en toute sécurité les publications avec pièces jointes

L’exemple SOQL ci-dessous est en lecture seule. Il répertorie les publications avec pièces jointes (`Type = 'ContentPost'`) pour examen ; il ne supprime rien.

```sql
SELECT Id, CreatedDate, CreatedById, ParentId, Type
FROM FeedItem
WHERE Type = 'ContentPost'
ORDER BY CreatedDate ASC
```

1. Exportez les ID candidats avec Data Loader ou Workbench, puis réduisez la sélection par date, auteur, enregistrement parent ou autres critères approuvés.
2. Vérifiez le plan de sauvegarde et de restauration de l’organisation et testez la procédure dans un Sandbox. Faites vérifier les ID et le nombre de suppressions par l’administrateur et le propriétaire des données.
3. Après approbation, supprimez uniquement les ID sélectionnés avec Data Loader. La procédure de suppression en masse documentée par Salesforce exporte également les ID FeedItem de type `ContentPost` avant leur suppression.

La suppression d’un FeedItem peut être définitive, sans passage par la corbeille, et donc irrécupérable. Supprimer une publication retire sa pièce jointe du fil ; le maintien du fichier à son emplacement d’origine ou dans d’autres partages dépend de son état. N’effectuez pas de suppression sans filtre sur tous les `ContentDocument` et ne videz pas toute la corbeille. Pour réduire le stockage des fichiers, consultez Storage Usage et vérifiez le propriétaire, les partages et l’impact de chaque fichier avant d’agir.

## Références

- [Work with Chatter Posts — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_posts_parent.htm&language=en_US&type=5)
- [Data and Storage Resources — Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.admin_monitorresources.htm&language=en_US&type=5)
- [Mass Delete Chatter Feed Item records that contain an attachment — Salesforce Help](https://help.salesforce.com/s/articleView?id=000198685&language=en_US&type=1)
- [FeedItem — Salesforce Developers](https://developer.salesforce.com/docs/platform/object-reference/references/standard-objects/object-feeditem.html)
- [Delete Files and Links from Chatter Feeds — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_attachments_del.htm&language=en_US&type=5)
