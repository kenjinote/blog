---
title: "Windows 11: comprobar el inicio rápido si cambia la escala de pantalla"

slug: "Monitor múltipleで毎回起動時にDPIの設定がリセットされてしまうときの対処法"
date: 2024-04-29T19:42:20+09:00
lastmod: "2026-11-24T00:00:00+09:00"

tags: ["Monitores múltiples", "DPI", "Panel de control"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Paso de diagnóstico prudente para Windows 11: desactivar temporalmente el inicio rápido, probar un apagado y encendido y volver a activarlo si no ayuda."
---
El inicio rápido guarda la sesión del kernel y el estado de los controladores en un archivo de hibernación durante el apagado para acelerar el siguiente arranque. Desactivarlo puede ralentizar el inicio. La documentación de Microsoft no lo señala como causa del restablecimiento de escala en varios monitores; considera estos pasos una prueba temporal, no una solución confirmada.

## Cambiar temporalmente la opción

1. Abre el Panel de control y selecciona **Opciones de energía**.
2. Abre **Elegir el comportamiento de los botones de inicio/apagado**.
3. Pulsa **Cambiar la configuración actualmente no disponible** (puede requerir permisos de administrador).
4. Desmarca **Activar inicio rápido (recomendado)** y pulsa **Guardar cambios**.
5. Elige **Apagar**, vuelve a encender el PC y comprueba si se conserva la escala. Prueba apagando y encendiendo; **Reiniciar** no utiliza el inicio rápido.

Si no ayuda, vuelve a la misma pantalla y activa de nuevo el inicio rápido. Los nombres de los menús pueden variar según el idioma y las actualizaciones de Windows.

## Referencias de Microsoft

- [Shut down, sleep, or hibernate your PC — Microsoft Support](https://support.microsoft.com/en-us/windows/experience/power-battery/shut-down-sleep-or-hibernate-your-pc)
- [System power states — Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/power/system-power-states)
- [Distinguishing Fast Startup from Wake-from-Hibernation — Microsoft Learn](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/distinguishing-fast-startup-from-wake-from-hibernation)
