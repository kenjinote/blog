---



title: 'Salesforce: Comando para borrar todas las publicaciones y archivos adjuntos de Chatter'
slug: "Salesforceチャッター全消しコマンド"
date: 2022-09-19T21:59:14+09:00
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.webp"
categories: ["IT y Tecnología"]
description: 'Presentamos comandos para eliminar masivamente todas las publicaciones, archivos adjuntos de Chatter y datos de la papelera, muy útiles cuando la capacidad de almacenamiento de la organización en Salesforce está llena. Se trata de un método rápido de limpieza utilizando la Ventana de Ejecución Anónima desde la Consola del Desarrollador.'
---



# Comando para eliminar todo en Salesforce Chatter
Este es un comando para eliminar todas las publicaciones y archivos adjuntos en Salesforce Chatter.
Abra la Consola del desarrollador, seleccione "Open Execute anonymous Window" en el menú Debug, pegue el siguiente código y ejecútelo.
Personalmente, lo utilizo cuando la capacidad de almacenamiento de la organización está al límite.

```
delete [select id from FeedItem];
delete [select id from FeedAttachment];
delete [select id from ContentDocument];

// Vaciar papelera de reciclaje
database.emptyRecycleBin([select id from ContentDocument where IsDeleted = true ALL ROWS]);
```
