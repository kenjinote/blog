---

title: "'Colección de Atajos y Trucos de Windows'"
date: 2022-09-18T23:49:29+09:00
tags: ["Windows", "Trucos", "Atajos"]
draft: false
image: "img.png"
categories: ["PC・Gadgets"]
---

Aquí hay una pequeña colección de trucos que uso habitualmente en Windows. Espero que aquellos que acaban de empezar a usar Windows lo encuentren útil.
Se asume el uso de Windows 11, pero creo que la mayoría también funcionan en Windows 10.

## Cerrar ventana
- `Alt + F4` con la ventana activa
- `Ctrl + W` con la ventana activa. Cierra la pestaña o ventana (solo en aplicaciones compatibles)
- Haz doble clic en el icono a la izquierda de la barra de título de la ventana
- Haz clic en la `×` en la barra de título de la ventana

## Mostrar el escritorio
- `Win + D`. Si lo presionas dos veces, vuelve al estado de ventana original. Es útil cuando quieres mostrar el escritorio por un instante.
- `Win + M`. Minimiza todas las aplicaciones. No se restaura presionando dos veces.

## Entrada de voz
- `Win + H`. Inicia la entrada de voz. Para detenerla, presiona `Esc` o `Win + H` nuevamente.

## Mostrar el menú contextual clásico en el Explorador
- Presiona `Shift + F10` o la tecla de aplicación. La tecla de aplicación está en la parte inferior derecha del teclado.

## Capturar una parte de la pantalla
- Con `Win + Shift + S` puedes seleccionar un área para capturar la pantalla.
- Con `Win + Print Screen` o simplemente `Print Screen` puedes capturar la pantalla completa.
(Si agregas `Win`, la imagen capturada se guardará en `C:\Users\nombre_de_usuario\Pictures\Screenshots`.)
- Con `Alt + Print Screen` puedes capturar la ventana actual.

## Iniciar aplicaciones ancladas a la barra de tareas
- Puedes iniciar aplicaciones ancladas a la barra de tareas con `Win + número`.
  Por ejemplo, al presionar `Win + 1` se inicia la primera aplicación a la izquierda en la barra de tareas.
- Con `Win + T` puedes enfocar los iconos de la barra de tareas, y si presionas `Win + T` varias veces,
  o `←` o `→`, puedes mover la selección y presionar la tecla `Enter` para iniciar la aplicación seleccionada.

## Acercar/Alejar
- `Win + +` abre la Lupa de Windows. Luego, puedes acercar o alejar la pantalla con `Win + + o -`.
- Puedes acercar o alejar con `Ctrl + + o -` en el bloc de notas, navegador, etc. (solo en aplicaciones compatibles).

## Bloquear Windows
- `Win + L`
- `Ctrl + Alt + Del` → `Space` o `Enter`

## Apagar Windows
- Si presionas `Alt + F4` estando en el escritorio (usando `Win + M` o `Win + D`) o con la barra de tareas activa (usando `Win + T` o `Win + B`), aparecerá un cuadro de diálogo como el siguiente. Asegúrate de que "Apagar" esté seleccionado y presiona `Enter`.
  También puedes usar `Win + R` → `Alt + F4` → `Alt + F4`.
  ![img_20.png](img_20.png)
- Puedes apagar con `Win + X` → `U` → `U`.
- En el símbolo del sistema o en "Ejecutar" (`Win + R`), escribe `shutdown /s /t 0` para apagar. Si agregas `/f`, se forzará el apagado.

## Reiniciar Windows
- Si presionas `Alt + F4` estando en el escritorio (usando `Win + M` o `Win + D`) o con la barra de tareas activa (usando `Win + T` o `Win + B`), aparecerá un cuadro de diálogo como el siguiente. Presiona `↓` una vez para seleccionar "Reiniciar" y luego `Enter`.
  También puedes usar `Win + R` → `Alt + F4` → `Alt + F4`.
  ![img_21.png](img_21.png)
- Puedes reiniciar con `Win + X` → `U` → `R`.
- Puedes reiniciar con `shutdown /r /t 0`. Si agregas `/f`, se forzará el reinicio.

## Suspender Windows
- Si presionas `Alt + F4` estando en el escritorio (usando `Win + M` o `Win + D`) o con la barra de tareas activa (usando `Win + T` o `Win + B`), aparecerá un cuadro de diálogo como el siguiente. Presiona `↑` una vez para seleccionar "Suspender" y luego `Enter`.
  También puedes usar `Win + R` → `Alt + F4` → `Alt + F4`.
  ![img_23.png](img_23.png)
- Puedes hibernar escribiendo `rundll32.exe powrprof.dll,SetSuspendState` en `Win + R` o en el símbolo del sistema.

## Cerrar sesión de Windows
- Si presionas `Alt + F4` estando en el escritorio (usando `Win + M` o `Win + D`) o con la barra de tareas activa (usando `Win + T` o `Win + B`), aparecerá un cuadro de diálogo como el siguiente. Presiona `↑` dos veces para seleccionar "Cerrar sesión" y luego `Enter`.
  También puedes usar `Win + R` → `Alt + F4` → `Alt + F4`.
  ![img_22.png](img_22.png)
- `Win + X` → `U` → `I`
- `Ctrl + Alt + Del` → `Tab` dos veces o `↓` dos veces → `Enter` o `Space`
- Puedes cerrar sesión con `logoff`.

## Mover ventanas con el teclado
- `Win + ←` : Mover a la izquierda
- `Win + →` : Mover a la derecha
- `Win + ↑` : Mover hacia arriba / Maximizar
- `Win + ↓` : Mover hacia abajo / Minimizar
- `Win + Shift + ← o →` : Mover entre monitores múltiples
- `Win + Alt + ← o → o ↑ o ↓` : Mover la ventana sin maximizar/minimizar
- Cuando no está minimizada, presiona `Alt + Espacio`, luego `M` y usa las teclas de flecha para mover.
※ Como la ventana sigue al cursor del ratón, puedes recuperarla incluso si está fuera de la pantalla.

## Finalizar un proceso en el Administrador de tareas
![img_24.png](img_24.png)
1. Puedes abrir el Administrador de tareas con `Ctrl + Shift + Esc`.
2. Puedes cambiar de pestaña con `Ctrl + Tab`.
3. Después de presionar `Tab` en la pestaña `Detalles`, puedes buscar un proceso por prefijo usando el teclado alfanumérico.
4. Con el nombre del proceso seleccionado, presiona la tecla `Delete` y luego `Enter` para finalizar el proceso.

## Finalizar un proceso especificando su nombre con un comando
- Puedes finalizar un proceso con `taskkill /f /im nombre_del_proceso`.
Por ejemplo, `taskkill /f /im explorer.exe` finalizará el explorador.

## Iniciar múltiples instancias del mismo programa desde el icono de la barra de tareas
- Al hacer clic izquierdo mientras mantienes presionada la tecla `Shift` en la barra de tareas, puedes iniciar múltiples instancias del mismo programa. (Solo aplicaciones que admiten instancias múltiples).

## Iniciar un programa con privilegios de administrador
- Al iniciar un programa mientras mantienes presionado `Ctrl + Shift`, puedes iniciarlo con privilegios de administrador.

## Iniciar el Explorador
- Puedes iniciar el Explorador con `Win + E`.
- Presiona `Win + R` para abrir "Ejecutar", escribe `explorer` y presiona `Enter`.
- Puedes crear una nueva carpeta con `Ctrl + Shift + N`.

## Abrir el símbolo del sistema en la ubicación abierta del Explorador
- En Windows 11, puedes iniciar el símbolo del sistema desde "Terminal" en el menú contextual.
- Además, puedes iniciar el símbolo del sistema escribiendo `cmd` en la barra de direcciones y presionando la tecla `Enter`.

## Mostrar el historial del portapapeles
- Puedes mostrar el historial del portapapeles con `Win + V`.
Si seleccionas texto o imágenes que copiaste anteriormente, puedes copiarlos nuevamente.

## Ejecutar
![img_28.png](img_28.png)
- Puedes abrir "Ejecutar" con `Win + R`.

A continuación, se presentan algunos comandos que puedes ejecutar en "Ejecutar" o en el símbolo del sistema.

## Abrir Edge
![img_18.png](img_18.png)
- Escribe `msedge` y presiona `Enter`

## Abrir Internet Explorer 11 (IE11)
![img_25.png](img_25.png)
- Escribe `powershell.exe -Command "(New-Object -ComObject InternetExplorer.Application).Visible = $true"` y presiona `Enter`

## Abrir Terminal
![img_19.png](img_19.png)
- Escribe `wt` y presiona `Enter`

## Abrir el Panel de control
![img_15.png](img_15.png)
- Escribe `control` y presiona `Enter`
- También puedes abrirlo con `explorer.exe shell:::{26EE0668-A00A-44D7-9371-BEB064C98683}`.

## Iniciar el Bloc de notas
![img_4.png](img_4.png)
- Escribe `notepad` y presiona `Enter`

## Iniciar la Calculadora
![img_5.png](img_5.png)
- Escribe `calc` y presiona `Enter`

## Iniciar Paint
![img_6.png](img_6.png)
- Escribe `mspaint` y presiona `Enter`

## Iniciar PowerShell
![img_7.png](img_7.png)
- Escribe `powershell` y presiona `Enter`

## Iniciar Visual Studio Code
![img_8.png](img_8.png)
- Escribe `code` y presiona `Enter`

## Iniciar Excel
![img_9.png](img_9.png)
- Escribe `excel` y presiona `Enter`
※ Solo si Excel está instalado.

## Abrir Word
![img_10.png](img_10.png)
- Escribe `winword` y presiona `Enter`
※ Solo si Word está instalado.

## Abrir PowerPoint
![img_11.png](img_11.png)
- Escribe `powerpnt` y presiona `Enter`
  ※ Solo si PowerPoint está instalado.

## Abrir Configuración del sistema
![img_1.png](img_1.png)
- Escribe `msconfig` y presiona `Enter`

## Abrir Propiedades del sistema
![img_2.png](img_2.png)
- Escribe `sysdm.cpl` y presiona `Enter`

## Abrir Información de la versión de Windows
![img_27.png](img_27.png)
- Escribe `winver` y presiona `Enter`

## Abrir el Teclado en pantalla
![img_14.png](img_14.png)
- Escribe `osk` y presiona `Enter`

## Abrir WordPad
![img_12.png](img_12.png)
- Escribe `wordpad` o `write` y presiona `Enter`

## Abrir el Editor del Registro
![img_13.png](img_13.png)
- Escribe `regedit` y presiona `Enter`

## Abrir Programas y características
- Escribe `explorer.exe shell:::{7b81be6a-ce2b-4676-a29e-eb907a5126c5}` y presiona `Enter`

## Abrir Propiedades del teclado
- Escribe `explorer.exe shell:::{725BE8F7-668E-4C7B-8F90-46BDB0936430}` y presiona `Enter`

## Abrir Propiedades del mouse
![img_16.png](img_16.png)
- Escribe `explorer.exe shell:::{6C8EEC18-8D75-41B2-A177-8831D59D2D50}` y presiona `Enter`

## Abrir Sonido
![img_3.png](img_3.png)
- Escribe `explorer.exe shell:::{F2DDFC82-8F12-4CDD-B7DC-D4FE1425AA4D}` y presiona `Enter`

## Abrir Cuentas de usuario
- Escribe `explorer.exe shell:::{60632754-c523-4b62-b45c-4172da012619}` y presiona `Enter`

## Copiar texto del cuadro de mensaje estándar
![img_26.png](img_26.png)
- Puedes copiar el texto de un cuadro de mensaje estándar con `Ctrl + C`.
Al copiar el cuadro de mensaje anterior, se copiará lo siguiente en el portapapeles.
```
[Window Title]
WordPad

[Main Instruction]
¿Desea guardar los cambios en Documento?

[Guardar(S)] [No guardar(N)] [Cancelar]
```

## Guardar la salida del símbolo del sistema en el portapapeles
Si agregas ` | clip` (tubería + clip) después de un comando, como `echo "hello" | clip`, puedes copiar la salida estándar al portapapeles.

## Exportar la jerarquía de carpetas como texto
Puedes usar el comando `tree` en el símbolo del sistema para generar la jerarquía de carpetas en formato de árbol.

Ejemplo de salida
```
C:.
├─.idea
│  └─libraries
├─binaryeditorbz
├─blog
│  ├─archetypes
│  ├─content
│  ├─data
│  ├─layouts
│  ├─static
│  └─themes
│      └─PaperMod
│          ├─.git
│          │  ├─branches
│          │  ├─hooks
│          │  ├─info
│          │  ├─logs
│          │  │  └─refs
│          │  │      ├─heads
│          │  │      └─remotes
│          │  │          └─origin
│          │  ├─objects
│          │  │  ├─info
│          │  │  └─pack
│          │  └─refs
│          │      ├─heads
│          │      ├─remotes
│          │      │  └─origin
│          │      └─tags
│          ├─.github
│          │  ├─ISSUE_TEMPLATE
│          │  └─workflows
│          ├─assets
│          │  ├─css
│          │  │  ├─common
│          │  │  ├─core
│          │  │  ├─extended
│          │  │  ├─hljs
│          │  │  └─includes
│          │  └─js
│          ├─i18n
│          ├─images
│          └─layouts
│              ├─partials
│              │  └─templates
│              ├─shortcodes
│              └─_default
│                  └─_markup
(omitido)
```

## Referencias
- [Métodos abreviados de teclado de Windows](https://support.microsoft.com/es-es/windows/m%C3%A9todos-abreviados-de-teclado-de-windows-dcc61a57-8ff0-cffe-9796-cb9706c75eec)
