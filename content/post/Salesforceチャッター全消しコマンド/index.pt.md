---
title: "Como organizar publicações do Salesforce Chatter: armazenamento e cuidados"

slug: "SalesforceChatter全消しComando"
date: 2022-09-19T21:59:14+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "Publicações do Chatter não consomem o armazenamento de dados do Salesforce. Veja como identificar o tipo de armazenamento, revisar e fazer backup dos posts selecionados e excluí-los com segurança pelo Data Loader."
---
**Importante:** Publicações, comentários e alterações rastreadas do Chatter não contam para o armazenamento de dados do Salesforce. Os arquivos anexados contam para o armazenamento de arquivos. Primeiro, confira **Storage Usage** em Setup para identificar qual categoria está próxima do limite. Excluir todas as publicações não libera armazenamento de dados.

## Revisar com segurança publicações com anexos

O exemplo SOQL abaixo é somente de leitura. Ele lista publicações com arquivos anexados (`Type = 'ContentPost'`) para revisão; não exclui dados.

```sql
SELECT Id, CreatedDate, CreatedById, ParentId, Type
FROM FeedItem
WHERE Type = 'ContentPost'
ORDER BY CreatedDate ASC
```

1. Exporte os IDs candidatos pelo Data Loader ou Workbench e restrinja o conjunto por data, autor, registro pai ou outros critérios aprovados.
2. Confira o plano de backup e recuperação da organização e teste o processo em um Sandbox. Peça ao administrador e ao proprietário dos dados para revisar os IDs e a quantidade de exclusões.
3. Após a aprovação, exclua somente os IDs selecionados com o Data Loader. O procedimento em massa documentado pela Salesforce também exporta os IDs de FeedItem com `Type = ContentPost` antes da exclusão.

A exclusão de FeedItem pode ser definitiva e não passar pela lixeira, portanto talvez não seja possível recuperá-la. Excluir uma publicação remove o anexo do feed; a permanência do arquivo no local original ou em outros compartilhamentos depende do estado dele. Não execute exclusão sem filtros em todos os `ContentDocument` nem esvazie toda a lixeira. Para reduzir o armazenamento de arquivos, consulte Storage Usage e verifique o proprietário, os compartilhamentos e o impacto de cada arquivo antes de agir.

## Referências

- [Work with Chatter Posts — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_posts_parent.htm&language=en_US&type=5)
- [Data and Storage Resources — Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.admin_monitorresources.htm&language=en_US&type=5)
- [Mass Delete Chatter Feed Item records that contain an attachment — Salesforce Help](https://help.salesforce.com/s/articleView?id=000198685&language=en_US&type=1)
- [FeedItem — Salesforce Developers](https://developer.salesforce.com/docs/platform/object-reference/references/standard-objects/object-feeditem.html)
- [Delete Files and Links from Chatter Feeds — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_attachments_del.htm&language=en_US&type=5)
