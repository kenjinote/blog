---
title: "Я попробовал установить Qt Extension Pack в Visual Studio Code"
slug: "Visual Studio Code に Qt Extension Pack を入れてみた"
date: 2024-09-13T00:53:53+09:00
tags: ["Visual Studio Code", "Qt Extension Pack"]
draft: false
image: "img_1.png"
categories: ["Инструменты и среда разработки"]
---

# Начинаем разработку на Qt в VSCode: Как установить Qt Extension Pack

Привет, я Kenji.
В этот раз я расскажу «Как настроить среду разработки Qt в Visual Studio Code (далее VSCode)».

В последнее время, в дополнение к официальному Qt Creator, всё больше людей хотят разрабатывать приложения Qt с использованием легковесного и расширяемого VSCode.
Тем, кто ищет такую возможность, я рекомендую ** «Qt Extension Pack» **.
Просто установив этот пакет расширений, вы получите все основные расширения, связанные с Qt, одновременно.

---

## Целевая аудитория

* Те, кто хочет начать разработку GUI-приложений с использованием Qt
* Те, кто хочет разрабатывать в VSCode, а не в Qt Creator
* Те, кому лень искать расширения по одному

---

## Предварительные требования

* VSCode уже установлен
  ([Вы можете бесплатно скачать его с официального сайта](https://code.visualstudio.com/))
* Сама библиотека Qt установлена ([Официальный сайт Qt](https://www.qt.io/))

---

## Что такое Qt Extension Pack?

Qt Extension Pack — это пакет расширений для VSCode.
Установив его, автоматически добавятся следующие функции:

* Поддержка файлов `.ui` (Qt Designer)
* Подсветка синтаксиса для файлов `.pro` и `.qrc`
* Автодополнение кода C++ для Qt, поддержка сборки и отладки
* Qt Resource Browser (просмотр ресурсов)

---

## Инструкция по установке

### 1. Откройте VSCode

Сначала запустите VSCode.

### 2. Откройте панель расширений

Нажмите на панель активности слева (иконка с квадратиками), чтобы открыть «Расширения».

Или вы можете нажать сочетание клавиш
`Ctrl + Shift + X`.

### 3. Найдите «Qt Extension Pack»

Введите следующее ключевое слово в строку поиска:

```
Qt Extension Pack
```

![img.png](img.png)

### 4. Нажмите кнопку установки

Когда появится нужный пакет, нажмите кнопку «Установить».
Это установит сразу несколько следующих расширений:

* Qt Language Support
* QML Support
* Qt Designer Integration
* CMake Tools (необходимо для разработки Qt с поддержкой CMake)

---

## Дополнение к настройкам проекта (пример CMake + Qt)

Если вы используете Qt на базе CMake, рекомендуется комбинация со следующими расширениями:

* [CMake Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)
* [CMake Language Support](https://marketplace.visualstudio.com/items?itemName=twxs.cmake)

Кроме того, если вы добавите следующий код в CMakeLists.txt, интеграция с Qt будет проходить более гладко:

```cmake
find_package(Qt6 REQUIRED COMPONENTS Widgets)
target_link_libraries(MyApp PRIVATE Qt6::Widgets)
```

---

## Бонус: Как открывать файлы .ui?

Файлы `.ui` можно редактировать в Qt Designer.
В VSCode вы сможете нажать правой кнопкой мыши на файл `.ui` → выбрать `Open with Qt Designer` (необходимо, чтобы Qt Designer был включен в переменную среды `PATH`).

---

## Заключение

| Шаг | Описание |
| -- | --------------------------- |
| 1 | Запуск VSCode |
| 2 | Открытие панели расширений |
| 3 | Поиск «Qt Extension Pack» |
| 4 | Нажатие кнопки установки |

Создание среды Qt в VSCode стало намного проще, чем раньше.
Она имеет достаточно функций, чтобы служить альтернативой Qt Creator, и мы рекомендуем её тем, кто хочет работать легко и быстро.

---

## Рекомендуемые ссылки

* [Официальный сайт Qt](https://www.qt.io/)
* [Qt Extension Pack - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=TheQtCompany.qt)
* [Официальный сайт VSCode](https://code.visualstudio.com/)
* [Расширение CMake Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)

---

## В заключение

В будущем я планирую продолжить разработку, используя UI-инструменты Qt и QML в этой среде.
В следующий раз я планирую объяснить, ** как собрать и запустить приложение Hello World на Qt из VSCode **.

До скорого!
