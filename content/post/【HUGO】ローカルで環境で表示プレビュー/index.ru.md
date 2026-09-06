---
title: "【HUGO】Предварительный просмотр в локальной среде"
slug: "【HUGO】ローカルで環境で表示プレビュー"
date: 2022-09-05T12:28:01+09:00
tags: ["HUGO"]
draft: false
image: "img.png"
categories: ["ブログ運営"]
---
# Установка HUGO

## Скачивание
[Скачать HUGO](https://github.com/gohugoio/hugo/releases)

С указанного выше сайта скачайте и распакуйте модуль для Windows, соответствующий вашей среде.
В моем случае я скачал "hugo_0.102.3_Windows-64bit.zip".

## Распаковка
Распакуйте скачанный zip-архив и скопируйте находящийся в нем hugo.exe в созданную вами папку, например C:\bin.

## Регистрация в переменных среды
Зарегистрируйте в переменных среды, чтобы запускать hugo.exe из любого места.
Это действия для Windows 11, но я думаю, что вы можете зарегистрировать его, выполнив следующие шаги.

1. Нажмите кнопку Win+Pause, чтобы открыть сведения о системе.
2. Нажмите Дополнительные параметры системы.
3. Нажмите Переменные среды.
4. Выберите Path и нажмите Изменить.
5. Нажмите Создать, введите "C:\bin" в новой строке и нажмите ОК, чтобы закрыть диалоговое окно.
 
# Предварительный просмотр блога
Перейдите в папку блога HUGO в командной строке и выполните следующую команду.

`hugo server -D`

Результат выполнения ниже. (-D — это параметр для отображения черновых статей.)

```
C:\Users\win11\IdeaProjects\kenji.blog>hugo server -D
Start building sites …
hugo v0.102.3-b76146b129d7caa52417f8e914fc5b9271bf56fc windows/amd64 BuildDate=2022-09-01T10:16:19Z VendorInfo=gohugoio

                   | JA
-------------------+-----
  Pages            | 39
  Paginator pages  |  0
  Non-page files   |  7
  Static files     |  0
  Processed images |  0
  Aliases          | 13
  Sitemaps         |  1
  Cleaned          |  0

Built in 161 ms
Watching for changes in C:\Users\win11\IdeaProjects\kenji.blog\{archetypes,content,themes}
Watching for config changes in C:\Users\win11\IdeaProjects\kenji.blog\config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

Адрес выводится во время выполнения (в примере выше `http://localhost:1313/`), поэтому скопируйте адрес в свой браузер.
Предварительный просмотр автоматически обновляется при каждом сохранении файла.
Чтобы завершить предварительный просмотр, введите Ctrl+C в командной строке.
