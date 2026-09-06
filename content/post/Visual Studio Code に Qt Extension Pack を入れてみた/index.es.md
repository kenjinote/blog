---





title: "Instalación de Qt Extension Pack en Visual Studio Code"
date: 2024-09-13T00:53:53+09:00
tags: ["Visual Studio Code", "Qt Extension Pack"]
draft: false
image: "img_1.png"
categories: ["Herramientas y Entorno de Desarrollo"]
---






# Comenzando el desarrollo de Qt en VSCode: Cómo instalar el Qt Extension Pack

Hola, soy Kenji.
Esta vez presentaré "Cómo configurar el entorno de desarrollo de Qt en Visual Studio Code (en adelante VSCode)".

Recientemente, además del Qt Creator oficial, ha aumentado el número de personas que desean desarrollar aplicaciones de Qt utilizando el ligero y altamente extensible VSCode.
Para estas personas, recomiendo el "**Qt Extension Pack**".
Con solo instalar este paquete de extensiones, tendrás a tu disposición las principales extensiones relacionadas con Qt.

---

## Audiencia Objetivo

* Personas que desean comenzar a desarrollar aplicaciones GUI usando Qt
* Personas que prefieren desarrollar en VSCode en lugar de Qt Creator
* Personas a las que les resulta tedioso buscar las extensiones una por una

---

## Requisitos Previos

* VSCode debe estar instalado
  ([Puedes descargarlo gratis desde el sitio web oficial](https://code.visualstudio.com/))
* La biblioteca base de Qt debe estar instalada ([Sitio web oficial de Qt](https://www.qt.io/))

---

## ¿Qué es el Qt Extension Pack?

Qt Extension Pack es un paquete de extensiones para VSCode.
Al instalarlo, las siguientes características se agregan automáticamente:

* Soporte para archivos `.ui` (Qt Designer)
* Resaltado de sintaxis para archivos `.pro` y `.qrc`
* Soporte para autocompletado de código C++, compilación y depuración para Qt
* Qt Resource Browser (referencia de recursos)

---

## Pasos de Instalación

### 1. Abre VSCode

Primero, inicia VSCode.

### 2. Abre la vista de Extensiones

Haz clic en el panel de Actividad a la izquierda (el icono de bloques cuadrados) para mostrar "Extensiones".

Opcionalmente, puedes presionar el atajo
`Ctrl + Shift + X`.

### 3. Busca "Qt Extension Pack"

Ingresa las siguientes palabras clave en la barra de búsqueda:

```
Qt Extension Pack
```

![img.png](img.png)

### 4. Haz clic en el botón Instalar

Una vez que se muestre el paquete correspondiente, haz clic en el botón "Instalar".
Esto instalará múltiples extensiones a la vez, como:

* Qt Language Support
* QML Support
* Qt Designer Integration
* CMake Tools (esencial para el desarrollo de Qt basado en CMake)

---

## Notas sobre la configuración del proyecto (Ejemplo CMake + Qt)

Si utilizas Qt con CMake, se recomienda la siguiente combinación de extensiones:

* [CMake Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)
* [CMake Language Support](https://marketplace.visualstudio.com/items?itemName=twxs.cmake)

Además, agregar las siguientes líneas en tu CMakeLists.txt facilita la integración con Qt:

```cmake
find_package(Qt6 REQUIRED COMPONENTS Widgets)
target_link_libraries(MyApp PRIVATE Qt6::Widgets)
```

---

## Extra: ¿Cómo abrir los archivos .ui?

Los archivos `.ui` se pueden editar en Qt Designer.
En VSCode, puedes hacer clic derecho en el archivo `.ui` → seleccionar `Open with Qt Designer` (requiere que Qt Designer esté incluido en la variable de entorno `PATH`).

---

## Resumen

| Paso | Contenido                     |
| -- | --------------------------- |
| 1  | Iniciar VSCode              |
| 2  | Abrir panel de Extensiones  |
| 3  | Buscar "Qt Extension Pack"  |
| 4  | Clic en botón Instalar      |

Configurar el entorno de Qt en VSCode se ha vuelto mucho más fácil que antes.
Ofrece suficientes funciones para ser una alternativa a Qt Creator, y es recomendable para quienes desean trabajar de forma ágil.

---

## Colección de Enlaces Recomendados

* [Sitio Oficial de Qt](https://www.qt.io/)
* [Qt Extension Pack - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=TheQtCompany.qt)
* [Sitio Oficial de VSCode](https://code.visualstudio.com/)
* [Extensión CMake Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)

---

## Finalmente

De ahora en adelante, planeo avanzar en el desarrollo utilizando las herramientas de interfaz de usuario de Qt y QML en este entorno.
La próxima vez, explicaré **cómo compilar y ejecutar una aplicación de Hello World en Qt desde VSCode**.

¡Hasta luego!
