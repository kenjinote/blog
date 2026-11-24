---
title: "Limpiar publicaciones de Salesforce Chatter: almacenamiento y pasos seguros"

slug: "SalesforceChatter全消しComando"
date: 2022-09-19T21:59:14+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "Las publicaciones de Chatter no consumen el almacenamiento de datos de Salesforce. Comprueba el tipo de almacenamiento, revisa y respalda las publicaciones seleccionadas y elimínalas con Data Loader."
---
**Importante:** Las publicaciones, los comentarios y los cambios registrados de Chatter no cuentan para el almacenamiento de datos de Salesforce. Los archivos adjuntos sí cuentan para el almacenamiento de archivos. Comprueba primero **Storage Usage** en Setup para saber qué categoría está cerca del límite. Borrar todas las publicaciones no libera almacenamiento de datos.

## Revisar de forma segura las publicaciones con archivos adjuntos

El siguiente ejemplo de SOQL es de solo lectura. Muestra publicaciones con archivos adjuntos (`Type = 'ContentPost'`) para revisarlas; no elimina nada.

```sql
SELECT Id, CreatedDate, CreatedById, ParentId, Type
FROM FeedItem
WHERE Type = 'ContentPost'
ORDER BY CreatedDate ASC
```

1. Exporta los ID candidatos con Data Loader o Workbench y reduce el conjunto por fecha, autor, registro principal u otros criterios aprobados.
2. Comprueba el plan de copias de seguridad y recuperación de la organización y prueba el proceso en un Sandbox. Pide al administrador y al propietario de los datos que revisen los ID y el número de eliminaciones.
3. Tras obtener la aprobación, elimina solo los ID seleccionados con Data Loader. El procedimiento masivo documentado por Salesforce también exporta primero los ID de FeedItem con `Type = ContentPost`.

Al borrar un FeedItem, puede eliminarse de forma permanente sin pasar por la papelera y ser irrecuperable. Borrar una publicación quita el archivo del feed; que el archivo siga en su ubicación original o en otros recursos compartidos depende de su estado. No ejecutes un borrado sin filtros de todos los `ContentDocument` ni vacíes toda la papelera. Para liberar almacenamiento de archivos, consulta Storage Usage y revisa el propietario, los accesos compartidos y el impacto de cada archivo antes de actuar.

## Referencias

- [Work with Chatter Posts — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_posts_parent.htm&language=en_US&type=5)
- [Data and Storage Resources — Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.admin_monitorresources.htm&language=en_US&type=5)
- [Mass Delete Chatter Feed Item records that contain an attachment — Salesforce Help](https://help.salesforce.com/s/articleView?id=000198685&language=en_US&type=1)
- [FeedItem — Salesforce Developers](https://developer.salesforce.com/docs/platform/object-reference/references/standard-objects/object-feeditem.html)
- [Delete Files and Links from Chatter Feeds — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_attachments_del.htm&language=en_US&type=5)
