---
title: "Очистка публикаций Salesforce Chatter: хранилище и безопасный порядок"

slug: "SalesforceДребезг контактов全消しКоманда"
date: 2022-09-19T21:59:14+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "Публикации Chatter не занимают хранилище данных Salesforce. Узнайте, как проверить тип хранилища, сохранить и проверить выбранные публикации, а затем безопасно удалить их через Data Loader."
---
**Важно:** публикации, комментарии и отслеживаемые изменения Chatter не учитываются в хранилище данных Salesforce. Вложения учитываются в файловом хранилище. Сначала проверьте **Storage Usage** в Setup, чтобы узнать, какой тип хранилища близок к лимиту. Удаление всех публикаций не освободит хранилище данных.

## Безопасная проверка публикаций с вложениями

Следующий пример SOQL доступен только для чтения. Он выводит публикации с файловыми вложениями (`Type = 'ContentPost'`) для проверки и ничего не удаляет.

```sql
SELECT Id, CreatedDate, CreatedById, ParentId, Type
FROM FeedItem
WHERE Type = 'ContentPost'
ORDER BY CreatedDate ASC
```

1. Экспортируйте возможные ID через Data Loader или Workbench, затем сузьте выборку по дате, автору, родительской записи или другим утвержденным критериям.
2. Проверьте план резервного копирования и восстановления организации и испытайте процедуру в Sandbox. Попросите администратора и владельца данных проверить ID и количество записей к удалению.
3. После утверждения удаляйте только выбранные ID с помощью Data Loader. В официальной массовой процедуре Salesforce также сначала экспортируются ID FeedItem с `Type = ContentPost`.

Удаление FeedItem может быть окончательным, миновать корзину и не подлежать восстановлению. При удалении публикации вложение удаляется из ленты; останется ли файл в исходном месте или других общих ресурсах, зависит от его состояния. Не удаляйте без фильтра все `ContentDocument` и не очищайте всю корзину. Для очистки файлового хранилища проверьте Storage Usage, владельца каждого файла, общие ресурсы и последствия перед удалением.

## Источники

- [Work with Chatter Posts — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_posts_parent.htm&language=en_US&type=5)
- [Data and Storage Resources — Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.admin_monitorresources.htm&language=en_US&type=5)
- [Mass Delete Chatter Feed Item records that contain an attachment — Salesforce Help](https://help.salesforce.com/s/articleView?id=000198685&language=en_US&type=1)
- [FeedItem — Salesforce Developers](https://developer.salesforce.com/docs/platform/object-reference/references/standard-objects/object-feeditem.html)
- [Delete Files and Links from Chatter Feeds — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_attachments_del.htm&language=en_US&type=5)
