---







title: 'Solución al error ''Temporary failure resolving'' al hacer apt update en WSL'
slug: "wsl で「Temporary failure resolving～」と表示される場合の対処方法"
date: 2024-03-31T16:57:33+09:00
tags: ["wsl", "solución"]
draft: false
image: "img.webp"
categories: ["Herramientas y Entornos de Desarrollo"]
description: 'Explicamos cómo solucionar el error ''Temporary failure resolving'' que aparece al ejecutar ''sudo apt update'' en el entorno WSL. Presentamos el procedimiento para cambiar la configuración del servidor DNS y restablecer correctamente la comunicación del administrador de paquetes.'
---








# Qué hacer cuando aparece "Temporary failure resolving~" en WSL

```
kenji@MyComputer:~$ sudo apt update
[sudo] password for kenji:
Err:1 http://archive.ubuntu.com/ubuntu focal InRelease
  Temporary failure resolving 'archive.ubuntu.com'
```

Cuando aparece el error anterior en WSL, es posible que la configuración del servidor DNS sea incorrecta.
En mi entorno, se solucionó con los siguientes pasos.

1. Inicie WSL.
2. Ejecute `sudo nano /etc/resolv.conf`.
3. Cambie la línea de `nameserver` de la siguiente manera.
```
nameserver 8.8.8.8
```
4. Guarde con `Ctrl` + `S` y salga con `Ctrl` + `X`.
5. Ejecute `sudo apt update`.
6. Si no se muestra el error, el problema está resuelto.

## Si los pasos anteriores no lo solucionan

Parece que hay casos donde los pasos anteriores no lo solucionan. Consulte el siguiente artículo.

- [Cómo solucionar 'Temporary failure resolving ~' al ejecutar apt update en WSL](https://qiita.com/ryosukeYamazaki/items/c04ec3ff78aac6eb8d26)
