---
title: "OAuth 2.0 y OIDC: autenticación, autorización y validación de tokens"
description: "Autenticación y autorización, roles de OAuth 2.0 y OIDC, código de autorización con PKCE y validación del token de ID mediante fórmulas y ejemplos de JavaScript y Python."
slug: "oauth2-oidc-authentication-authorization-difference"
date: "2026-09-22T08:00:00+09:00"
lastmod: "2026-10-27"
image: "eyecatch.jpg"
categories:
    - "security"
tags:
    - "oauth2"
    - "oidc"
    - "authentication"
    - "authorization"
    - "iam"

---

OAuth 2.0 es un marco de autorización que concede acceso limitado a las aplicaciones. OpenID Connect (OIDC) añade un mecanismo para comunicar al cliente el resultado de la autenticación del usuario final.

Este artículo distingue la autenticación de la autorización, los usos de los tokens, el código de autorización con PKCE y la validación del token de ID. El código ilustra operaciones concretas; no implementa un inicio de sesión completo. En producción, utilice una biblioteca OIDC y una configuración del proveedor adecuadas a sus requisitos.

## 1. Autenticación y autorización

### Autenticación / AuthN

La autenticación comprueba la identidad de un usuario o sistema a partir de las pruebas presentadas. Una analogía es revisar la tarjeta de un empleado en la recepción de una empresa.

### Autorización / AuthZ

La autorización determina qué operaciones puede realizar una entidad y a qué recursos puede acceder. Confirmar que alguien es empleado no significa que pueda entrar en todas las salas de servidores.

| Elemento | Autenticación | Autorización |
| --- | --- | --- |
| Pregunta | ¿Quién es? | ¿Qué se permite? |
| Abreviatura | AuthN | AuthZ |
| Mecanismo tratado aquí | OIDC comunica el resultado de la autenticación | OAuth 2.0 concede acceso limitado |
| Ejemplo de token | Token de ID de OIDC | Token de acceso de OAuth 2.0 |

No todos los mecanismos de autenticación emiten un token de ID. OAuth 2.0 tampoco define todo el control de acceso de una aplicación. Tras recibir un token, la API debe comprobar los permisos necesarios para el recurso y la operación concretos.

OAuth 2.0 por sí solo no estandariza cómo verifica el cliente el resultado de la autenticación del usuario final. Recibir un token de acceso no basta para dar por iniciada una sesión: utilice un protocolo, como OIDC, que permita validar ese resultado.

## 2. Roles y concesiones de OAuth 2.0

### 2.1 Acceso limitado

OAuth 2.0 permite que un cliente obtenga un token de acceso en nombre del propietario del recurso o en nombre propio. Delegar el acceso sin entregar la contraseña del usuario al cliente es una característica importante del flujo de código de autorización.

### 2.2 Cuatro roles

1. **Propietario del recurso (Resource Owner)**: entidad capaz de autorizar el acceso a un recurso protegido. No tiene que ser una persona.
2. **Cliente (Client)**: aplicación que utiliza recursos protegidos.
3. **Servidor de autorización (Authorization Server)**: servidor que comprueba la autorización, la autenticación del cliente y las demás condiciones del flujo correspondiente, y emite tokens.
4. **Servidor de recursos (Resource Server)**: servidor que valida los tokens y los permisos y proporciona los recursos protegidos.

### 2.3 Principales tipos de concesión

#### Código de autorización (Authorization Code Grant)

La respuesta de autorización devuelve un código de corta duración, que se intercambia por un token de acceso en el punto de conexión de tokens. Pueden usar este flujo con PKCE tanto los **clientes confidenciales**, capaces de proteger sus credenciales en un servidor, como los **clientes públicos**, incluidas las SPA y las aplicaciones nativas. Incrustar un secreto del cliente en código distribuido o en el navegador no permite mantenerlo en secreto.

#### Concesión implícita (Implicit Grant)

Esta concesión devuelve directamente un token de acceso en la respuesta de autorización. Presenta riesgos de filtración, inyección y reutilización de tokens. RFC 9700 indica que los clientes NO DEBERÍAN utilizarla (SHOULD NOT) salvo que se mitiguen los riesgos especificados. Para una configuración nueva, elija código de autorización con PKCE. No interprete esta recomendación como una prohibición idéntica para todos los tipos de respuesta de OIDC.

#### Credenciales de contraseña del propietario del recurso (ROPC)

En esta concesión, el cliente recibe directamente la contraseña del usuario. Aunque RFC 6749 la describe, las directrices de seguridad actualizadas de RFC 9700 establecen que **NO DEBE utilizarse (MUST NOT)**. La migración de sistemas heredados no debe presentarse como una excepción recomendada.

#### Credenciales del cliente (Client Credentials Grant)

Un cliente confidencial se autentica para obtener un token. Puede acceder a recursos bajo su control o a los de otro propietario según un acuerdo previo con el servidor de autorización. Suele utilizarse en comunicaciones entre sistemas sin interacción del usuario final; el cliente no se convierte necesariamente en propietario del recurso.

### 2.4 Código de autorización y PKCE

PKCE (Proof Key for Code Exchange) vincula al cliente que inicia una solicitud de autorización con el que intercambia el código por tokens, y ayuda a proteger frente a la intercepción y la inyección de códigos. Es obligatorio para los clientes públicos y también se recomienda para los confidenciales. No sustituye la autenticación del cliente exigida a un cliente confidencial.

En cada transacción de autorización, el cliente genera un nuevo `code_verifier` secreto. RFC 7636 especifica entre 43 y 128 caracteres tomados de las letras, los dígitos y `-._~`, y recomienda al menos 256 bits de entropía. Codificar 32 bytes generados con un generador criptográficamente seguro en Base64url sin relleno produce 43 caracteres.

Con `S256`, el desafío se calcula así. Se omiten los caracteres de relleno `=` al final de Base64url.

$$
\text{code\_challenge}=\operatorname{BASE64URL}\!\left(\operatorname{SHA256}\!\left(\operatorname{ASCII}(\text{code\_verifier})\right)\right)
$$

La solicitud de autorización envía `code_challenge` y `code_challenge_method=S256`; la solicitud de token envía el `code_verifier` conservado para esa misma transacción. El servidor lo comprueba utilizando el método y el desafío registrados junto al código. No vuelva a `plain` porque haya fallado `S256`.

#### Resumen del flujo

```mermaid
sequenceDiagram
    autonumber
    participant U as "Usuario / navegador"
    participant C as "Cliente"
    participant AS as "Servidor de autorización / OP de OIDC"
    participant RS as "Servidor de recursos"
    Note over C: "Conservar verifier y state por transacción; también nonce para OIDC"
    C->>U: "Redirigir al punto de conexión de autorización"
    U->>AS: "Solicitud: challenge y S256; openid y nonce para OIDC"
    AS-->>U: "Solicitar autenticación y consentimiento cuando corresponda"
    U->>AS: "Autenticarse y autorizar"
    AS-->>U: "Redirigir a redirect_uri registrado con code y state"
    U->>C: "Retorno: code y state"
    Note over C: "Comprobar transacción, state y emisor esperado"
    C->>AS: "Intercambiar code con verifier y autenticación del cliente requerida"
    Note over AS: "Validar código, vinculaciones y PKCE"
    AS-->>C: "Token de acceso; también token de ID para OIDC"
    Note over C: "En OIDC, validar token de ID y nonce"
    C->>RS: "Llamar a la API con el token de acceso"
    RS-->>C: "Validar token y permisos, y devolver el recurso"
```

El diagrama resume un flujo exitoso. Proteja las comunicaciones con TLS. La implementación también debe gestionar la validación de las redirecciones, el uso único de los códigos, las respuestas de error, la caducidad de la transacción y la defensa contra ataques de confusión de servidores (mix-up) cuando intervengan varios servidores de autorización.

#### Generación de parámetros PKCE (JavaScript / Web Crypto API)

Estas funciones para el navegador requieren un contexto seguro, como HTTPS. `generatePkce()` solo devuelve parámetros: no envía la solicitud de autorización ni almacena la transacción. Mantenga el verifier fuera de registros y URL, vincúlelo con la transacción iniciada en ese navegador y descártelo después del intercambio o al caducar.

```javascript
function base64url(bytes) {
    return btoa(String.fromCharCode(...bytes))
        .replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

function generateCodeVerifier() {
    const bytes = new Uint8Array(32);
    crypto.getRandomValues(bytes);
    return base64url(bytes);
}

async function generateCodeChallenge(codeVerifier) {
    if (typeof codeVerifier !== 'string' ||
        codeVerifier.length < 43 || codeVerifier.length > 128 ||
        /[^A-Za-z0-9._~-]/.test(codeVerifier)) {
        throw new TypeError('Invalid PKCE verifier');
    }
    const data = new TextEncoder().encode(codeVerifier);
    const digest = await crypto.subtle.digest('SHA-256', data);
    return base64url(new Uint8Array(digest));
}

async function generatePkce() {
    const code_verifier = generateCodeVerifier();
    return {
        code_verifier,
        code_challenge: await generateCodeChallenge(code_verifier),
        code_challenge_method: 'S256'
    };
}
```

El código utiliza todos los bits de los 32 bytes aleatorios. El ejemplo anterior concatenaba únicamente los dos últimos dígitos hexadecimales de cada uno de 28 enteros aleatorios de 32 bits: obtenía 896 bits, pero solo conservaba 224. Se ha corregido ese truncamiento.

## 3. OIDC y tokens de ID

### 3.1 Una capa de autenticación sobre OAuth

En OIDC, el cliente (Relying Party) solicita autenticación con el ámbito `openid`, y el OpenID Provider (OP) devuelve el resultado en un token de ID. El usuario no tiene que introducir su contraseña cada vez: el OP puede utilizar una sesión existente u otro método de autenticación.

### 3.2 Separar los usos de los tokens

- **Token de acceso**: credencial para acceder al servidor de recursos. Puede ser un JWT o una cadena opaca; OAuth 2.0 no impone un único formato. El cliente debe seguir los requisitos de la API, sin suponer una estructura interna.
- **Token de ID**: JWT que representa el resultado de la autenticación destinado al cliente. Antes de utilizarlo, valide su firma, sus declaraciones y su vinculación con la solicitud de autenticación. Decodificarlo no basta; tampoco debe enviarse como sustituto de un token de acceso a una API.

### 3.3 Estructura de JWT y firmas

Esta sección explica **JWS Compact Serialization** para un JWT firmado y sin cifrar, con tres partes separadas por puntos. Un JWT también puede estar cifrado como JWE o tener una estructura anidada: no siempre consta de tres partes.

1. **Header (encabezado)**: campos como el algoritmo de firma `alg` y el identificador de clave `kid`.
2. **Payload (carga útil)**: declaraciones como el emisor, los destinatarios, la caducidad y el sujeto.
3. **Signature (firma)**: firma o MAC generado por el algoritmo especificado. RS256, utilizado aquí, emplea una firma digital RSA.

El encabezado y la carga útil solo están codificados en Base64url. La firma no oculta su contenido. Consulte también [las diferencias entre cifrado, hash y firma]({{< relref "post/modern-cryptography-public-key-hash-signature/index.es.md" >}}).

#### Principales declaraciones obligatorias del token de ID

- `iss`: identificador del emisor del OP. Debe coincidir exactamente con el emisor esperado.
- `sub`: identificador del usuario único y nunca reasignado dentro de ese emisor. Si se utilizan varios OP, combínelo con `iss` para identificar al usuario.
- `aud`: destinatario o destinatarios previstos. Compruebe que incluye el `client_id` del cliente y no acepte destinatarios adicionales que no sean de confianza.
- `exp`: fecha y hora de caducidad. El instante actual debe ser anterior.
- `iat`: instante de emisión. La política del cliente determina la antigüedad aceptable y otras restricciones.

Si se envió `nonce` en la solicitud de autenticación, exija esa declaración y compruebe su valor. Si se solicitaron declaraciones adicionales o `max_age`, también se necesitan las validaciones correspondientes.

#### Entrada de la firma RS256

Sean `H` el encabezado protegido en UTF-8, `P` la carga útil en UTF-8 y `B64u` la codificación Base64url sin relleno. La entrada de la firma es la siguiente secuencia de bytes; `||` indica concatenación.

$$
M=\operatorname{ASCII}\!\left(\operatorname{B64u}(H)\,||\,\texttt{.}\,||\,\operatorname{B64u}(P)\right),\qquad S=\operatorname{Sign}_{\mathrm{RS256}}(sk,M)
$$

RS256 utiliza RSASSA-PKCS1-v1_5 con SHA-256. El cálculo del hash forma parte del algoritmo de firma: la ecuación no añade un hash externo adicional. La tercera parte del token es `B64u(S)`. Verifique la firma con una clave pública del OP de confianza y el algoritmo especificado, sin describir la verificación de firmas en general como un descifrado con clave pública.

No deje que un token sin verificar decida los algoritmos permitidos o el origen de las claves. Utilice un JWKS de confianza obtenido de una configuración o de un proceso Discovery del OP debidamente verificados, y gestione la rotación y la caché de claves. `kid` permite elegir dentro de ese conjunto de confianza; no obtenga claves desde una URL arbitraria indicada por el token.

#### Ejemplo parcial de validación en Python

La siguiente función de PyJWT admite una configuración limitada: **RS256, sin cifrado, un único destinatario representado como cadena y un nonce ya enviado en la solicitud**. Quien llama proporciona `signing_key`, una clave pública procedente del JWKS del OP de confianza. Las declaraciones obligatorias deben existir, además de tener valores válidos. Si aparece `azp`, esta configuración exige que coincida con `client_id`.

Esta función no completa un inicio de sesión. Quien llama debe validar y gestionar la relación entre el retorno y la transacción inicial, state, el intercambio de código, el emisor esperado y el uso único del nonce. Quedan fuera de este ejemplo los destinatarios múltiples, el cifrado, los requisitos adicionales de autenticación, `max_age` y `acr`.

```python
import hmac
import math
import jwt


def verify_id_token(id_token, signing_key, *, issuer, client_id, expected_nonce):
    if not isinstance(expected_nonce, str) or not expected_nonce:
        raise ValueError('A nonce from the stored transaction is required')
    claims = jwt.decode(
        id_token,
        signing_key,
        algorithms=['RS256'],
        audience=client_id,
        issuer=issuer,
        options={
            'require': ['iss', 'sub', 'aud', 'exp', 'iat', 'nonce'],
            'strict_aud': True,
        },
    )
    for name in ('exp', 'iat'):
        value = claims[name]
        if (isinstance(value, bool) or not isinstance(value, (int, float))
                or (isinstance(value, float) and not math.isfinite(value))):
            raise jwt.InvalidTokenError('Invalid NumericDate')
    subject = claims['sub']
    if (not isinstance(subject, str) or not subject or not subject.isascii()
            or len(subject) > 255):
        raise jwt.InvalidTokenError('Invalid subject')
    nonce = claims['nonce']
    if (not isinstance(nonce, str) or not hmac.compare_digest(
            nonce.encode('utf-8'), expected_nonce.encode('utf-8'))):
        raise jwt.InvalidTokenError('Nonce mismatch')
    if 'azp' in claims and claims['azp'] != client_id:
        raise jwt.InvalidTokenError('Authorized party mismatch')
    return claims
```

La función devuelve las declaraciones validadas dentro de ese alcance. No anuncie una autenticación correcta basándose solo en una firma válida, ni vincule cuentas utilizando un nombre o una dirección de correo sin verificar.

## 4. Consideraciones de seguridad

### 4.1 state, nonce, PKCE y CSRF

Si utiliza `state`, vincule de forma segura un valor impredecible a la transacción iniciada en el navegador. Al recibir el retorno, compruebe el valor, su caducidad y que no se haya utilizado; después, márquelo como utilizado. La igualdad entre cadenas no evita por sí sola todas las formas de [CSRF]({{< relref "post/cross-site-scripting-xss-csrf-security/index.es.md" >}}).

RFC 9700 también contempla confiar en la protección CSRF de PKCE tras confirmar que el servidor lo admite, así como utilizar un nonce de OIDC. Estas protecciones requieren una vinculación por transacción y una validación correcta. `state`, `nonce` y PKCE tienen funciones distintas; usar valores constantes u omitir las comparaciones no proporciona la protección prevista. Si se utilizan varios servidores de autorización, también se necesita una defensa contra ataques mix-up.

### 4.2 Caducidad y tokens de actualización

Una duración corta del token de acceso ayuda a limitar el tiempo durante el cual puede utilizarse un token robado. Un valor como 15 minutos es un ejemplo de diseño, no un requisito universal. Al comprobar `exp` en un JWT firmado, la condición de caducidad es:

$$
T_{\mathrm{now}}<T_{\mathrm{exp}},\qquad T_{\mathrm{exp}}=T_{\mathrm{iat}}+D_{\mathrm{lifetime}}\ \text{solo si se define así}\ T_{\mathrm{now}}<T_{\mathrm{iat}}+D_{\mathrm{lifetime}}
$$

Esta condición solo comprueba la caducidad; no demuestra la validez completa del token ni los permisos de acceso. También deben verificarse el algoritmo, la clave, el emisor, los destinatarios y, cuando corresponda, `nbf`, el estado de revocación y la relación con la solicitud de autenticación. Gestione explícitamente cualquier tolerancia al desfase de relojes.

La emisión de tokens de actualización es opcional. Si no se emiten, el cliente puede necesitar una nueva transacción de autorización. RFC 9700 exige vinculación criptográfica al cliente que presenta el token (sender constraints) o rotación para los tokens de actualización emitidos a clientes públicos. Revocar un token de actualización no invalida necesariamente de inmediato los tokens de acceso ya emitidos.

### 4.3 Elección del flujo y de la implementación

Para aplicaciones web, SPA y aplicaciones nativas con interacción del usuario, parta del código de autorización con PKCE y elija una configuración acorde con el tipo de cliente, el almacenamiento de tokens, el soporte del proveedor y el modelo de amenazas. No imponga ese flujo a todos los casos, como las credenciales del cliente para M2M.

## Conclusión

Utilice los tokens de acceso de OAuth 2.0 para acceder a recursos y valide los tokens de ID de OIDC como resultados de autenticación destinados al cliente. Compruebe la vinculación del código con PKCE, la firma, las declaraciones obligatorias, el nonce y la relación entre el retorno y la transacción inicial.

## Referencias

- [RFC 6749: OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749.html) (roles, tokens y credenciales del cliente; consulte RFC 9700 para las directrices de seguridad actualizadas)
- [RFC 7636: PKCE](https://www.rfc-editor.org/rfc/rfc7636.html) (sección 4, sección 7.1 y apéndice B)
- [RFC 9700: buenas prácticas de seguridad para OAuth 2.0](https://www.rfc-editor.org/rfc/rfc9700.html) (secciones 2.1, 2.2.2 y 2.4)
- [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html) (secciones 2, 3.1.3.7 y 5.7)
- [RFC 7515: JWS](https://www.rfc-editor.org/rfc/rfc7515.html) (secciones 3.1 y 5.1)
- [API de PyJWT](https://pyjwt.readthedocs.io/en/stable/api.html) (algoritmos permitidos, declaraciones obligatorias y validación del destinatario)
