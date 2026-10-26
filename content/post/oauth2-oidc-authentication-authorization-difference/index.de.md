---
title: "OAuth 2.0 und OIDC: Authentifizierung, Autorisierung und Token-Prüfung"
description: "Authentifizierung und Autorisierung, die Rollen von OAuth 2.0 und OIDC, Autorisierungscode mit PKCE und die Prüfung von ID-Token anhand von Formeln sowie JavaScript- und Python-Beispielen."
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

OAuth 2.0 ist ein Autorisierungsframework, das Anwendungen begrenzten Zugriff gewährt. OpenID Connect (OIDC) ergänzt einen Mechanismus, mit dem das Ergebnis der Authentifizierung des Endbenutzers an den Client übermittelt wird.

Dieser Artikel unterscheidet Authentifizierung und Autorisierung, die Zwecke der Token, Autorisierungscode mit PKCE und die Prüfung von ID-Token. Der Code zeigt einzelne Verarbeitungsschritte und implementiert keine vollständige Anmeldung. Verwenden Sie im Produktivbetrieb eine OIDC-Bibliothek und eine Anbieterkonfiguration, die Ihren Anforderungen entsprechen.

## 1. Authentifizierung und Autorisierung

### Authentifizierung / AuthN

Die Authentifizierung prüft die Identität eines Benutzers oder Systems anhand vorgelegter Nachweise. Ein Vergleich ist die Kontrolle eines Mitarbeiterausweises am Empfang eines Unternehmens.

### Autorisierung / AuthZ

Die Autorisierung bestimmt, welche Aktionen ein Akteur ausführen und auf welche Ressourcen er zugreifen darf. Die Bestätigung, dass jemand Mitarbeiter ist, erlaubt noch keinen Zutritt zu allen Serverräumen.

| Merkmal | Authentifizierung | Autorisierung |
| --- | --- | --- |
| Frage | Wer ist es? | Was ist erlaubt? |
| Abkürzung | AuthN | AuthZ |
| Hier behandelter Mechanismus | OIDC übermittelt ein Authentifizierungsergebnis | OAuth 2.0 gewährt begrenzten Zugriff |
| Token-Beispiel | ID-Token von OIDC | Access-Token von OAuth 2.0 |

Nicht jedes Authentifizierungsverfahren stellt ein ID-Token aus. OAuth 2.0 definiert auch nicht die gesamte Zugriffskontrolle innerhalb einer Anwendung. Nach dem Empfang eines Tokens muss die API weiterhin die für die konkrete Ressource und Aktion erforderlichen Berechtigungen prüfen.

OAuth 2.0 allein standardisiert nicht, wie der Client das Authentifizierungsergebnis des Endbenutzers überprüft. Der bloße Empfang eines Access-Tokens begründet keine Anmeldung. Verwenden Sie ein Protokoll wie OIDC, mit dem sich dieses Ergebnis validieren lässt.

## 2. Rollen und Grant-Typen von OAuth 2.0

### 2.1 Begrenzter Zugriff

OAuth 2.0 ermöglicht es einem Client, ein Access-Token im Namen des Ressourcenbesitzers oder im eigenen Namen zu erhalten. Zugriff zu delegieren, ohne das Benutzerpasswort an den Client weiterzugeben, ist ein wichtiges Merkmal des Autorisierungscode-Ablaufs.

### 2.2 Vier Rollen

1. **Ressourcenbesitzer (Resource Owner)**: Akteur, der den Zugriff auf eine geschützte Ressource erlauben kann. Dies muss keine natürliche Person sein.
2. **Client**: Anwendung, die geschützte Ressourcen nutzt.
3. **Autorisierungsserver (Authorization Server)**: Server, der Autorisierung, Client-Authentifizierung und weitere Bedingungen des jeweiligen Ablaufs prüft und Token ausstellt.
4. **Ressourcenserver (Resource Server)**: Server, der Token und Berechtigungen validiert und geschützte Ressourcen bereitstellt.

### 2.3 Wichtige Grant-Typen

#### Autorisierungscode-Grant (Authorization Code Grant)

Die Autorisierungsantwort liefert einen kurzlebigen Code, der am Token-Endpunkt gegen ein Access-Token ausgetauscht wird. Sowohl **vertrauliche Clients**, die ihre Zugangsdaten auf einem Server schützen können, als auch **öffentliche Clients**, etwa SPAs und native Apps, können diesen Ablauf mit PKCE verwenden. Ein Client-Secret in ausgeliefertem Anwendungscode oder im Browser bleibt dadurch nicht geheim.

#### Impliziter Grant (Implicit Grant)

Dieser Grant liefert ein Access-Token direkt in der Autorisierungsantwort. Es bestehen Risiken durch Token-Offenlegung, Einschleusen und Wiederverwendung. RFC 9700 besagt, dass Clients diesen Grant NICHT verwenden SOLLTEN (SHOULD NOT), sofern die genannten Risiken nicht gemindert werden. Wählen Sie für neue Konfigurationen Autorisierungscode mit PKCE. Diese Empfehlung ist kein gleichlautendes Verbot sämtlicher OIDC-Antworttypen.

#### Passwort des Ressourcenbesitzers (ROPC)

Bei diesem Grant erhält der Client das Benutzerpasswort direkt. RFC 6749 beschreibt ihn zwar, die aktualisierten Sicherheitsvorgaben in RFC 9700 bestimmen jedoch, dass er **NICHT verwendet werden DARF (MUST NOT)**. Die Migration älterer Systeme darf nicht als empfohlene Ausnahme dargestellt werden.

#### Client-Zugangsdaten (Client Credentials Grant)

Ein vertraulicher Client authentifiziert sich, um ein Token zu erhalten. Er kann auf Ressourcen unter seiner Kontrolle oder nach vorheriger Vereinbarung mit dem Autorisierungsserver auf Ressourcen eines anderen Besitzers zugreifen. Dieser Grant dient häufig der Kommunikation zwischen Systemen ohne Interaktion des Endbenutzers. Der Client wird dabei nicht zwangsläufig zum Ressourcenbesitzer.

### 2.4 Autorisierungscode und PKCE

PKCE (Proof Key for Code Exchange) verknüpft den Client, der die Autorisierungsanfrage startet, mit dem Client, der den Code gegen Token austauscht. Das schützt gegen das Abfangen und Einschleusen von Codes. Öffentliche Clients müssen PKCE verwenden; für vertrauliche Clients wird es ebenfalls empfohlen. Es ersetzt nicht die für einen vertraulichen Client erforderliche Client-Authentifizierung.

Der Client erzeugt für jeden Autorisierungsvorgang einen neuen geheimen `code_verifier`. RFC 7636 legt 43 bis 128 Zeichen aus Buchstaben, Ziffern und `-._~` fest und empfiehlt mindestens 256 Bit Entropie. Werden 32 Byte aus einem kryptografisch sicheren Zufallszahlengenerator ohne Padding als Base64url codiert, entstehen 43 Zeichen.

Bei `S256` wird die Challenge wie folgt berechnet. Das abschließende `=`-Padding von Base64url entfällt.

$$
\text{code\_challenge}=\operatorname{BASE64URL}\!\left(\operatorname{SHA256}\!\left(\operatorname{ASCII}(\text{code\_verifier})\right)\right)
$$

Die Autorisierungsanfrage enthält `code_challenge` und `code_challenge_method=S256`. Die Token-Anfrage enthält den für denselben Vorgang aufbewahrten `code_verifier`. Der Server prüft ihn mit der zum Code gespeicherten Methode und Challenge. Wechseln Sie nicht zu `plain`, weil `S256` fehlgeschlagen ist.

#### Überblick über den Ablauf

```mermaid
sequenceDiagram
    autonumber
    participant U as "Benutzer / Browser"
    participant C as "Client"
    participant AS as "Autorisierungsserver / OIDC-OP"
    participant RS as "Ressourcenserver"
    Note over C: "verifier und state pro Vorgang speichern; bei OIDC auch nonce"
    C->>U: "Zum Autorisierungsendpunkt weiterleiten"
    U->>AS: "Anfrage: challenge und S256; bei OIDC openid und nonce"
    AS-->>U: "Bei Bedarf Authentifizierung und Zustimmung anfordern"
    U->>AS: "Authentifizierung und Autorisierung durchführen"
    AS-->>U: "Mit code und state an registrierte redirect_uri weiterleiten"
    U->>C: "Callback: code und state"
    Note over C: "Vorgang, state und erwarteten Aussteller prüfen"
    C->>AS: "code mit verifier und erforderlicher Client-Authentifizierung austauschen"
    Note over AS: "Code, Bindungen und PKCE prüfen"
    AS-->>C: "Access-Token; bei OIDC auch ID-Token"
    Note over C: "Bei OIDC ID-Token und nonce validieren"
    C->>RS: "API mit Access-Token aufrufen"
    RS-->>C: "Token und Berechtigungen prüfen, dann Ressource zurückgeben"
```

Dies ist der Überblick über einen erfolgreichen Ablauf. Schützen Sie die Kommunikation mit TLS. Implementierungen müssen außerdem Weiterleitungsziele, die einmalige Nutzung von Codes, Fehlerantworten, das Ablaufen eines Vorgangs und bei mehreren Autorisierungsservern den Schutz vor Mix-up-Angriffen behandeln.

#### PKCE-Parameter erzeugen (JavaScript / Web Crypto API)

Diese Browserfunktionen benötigen einen sicheren Kontext, etwa HTTPS. Die Funktion `generatePkce()` gibt nur Parameter zurück; sie sendet keine Autorisierungsanfrage und speichert den Vorgang nicht. Geben Sie den Verifier nicht in Protokollen oder URLs aus. Binden Sie ihn an den im Browser gestarteten Vorgang und verwerfen Sie ihn nach dem Austausch oder Ablauf.

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

Der Code codiert sämtliche Bits der 32 zufälligen Byte. Das frühere Beispiel verknüpfte nur die letzten beiden Hexadezimalstellen von jeweils 28 zufälligen 32-Bit-Ganzzahlen. Es bezog 896 Bit, behielt aber nur 224 Bit bei. Diese Verkürzung wurde korrigiert.

## 3. OIDC und ID-Token

### 3.1 Eine Authentifizierungsschicht über OAuth

Bei OIDC fordert der Client (Relying Party) die Authentifizierung mit dem Scope `openid` an. Der OpenID Provider (OP) liefert das Ergebnis in einem ID-Token. Benutzer müssen nicht jedes Mal ein Passwort eingeben: Der OP kann eine bestehende Sitzung oder ein anderes Authentifizierungsverfahren verwenden.

### 3.2 Token-Zwecke trennen

- **Access-Token**: Zugangsnachweis für einen Ressourcenserver. Es kann ein JWT oder eine undurchsichtige Zeichenfolge sein; OAuth 2.0 legt kein einheitliches Format fest. Der Client muss die API-Vorgaben beachten, statt eine interne Struktur vorauszusetzen.
- **ID-Token**: JWT, das ein für den Client bestimmtes Authentifizierungsergebnis darstellt. Prüfen Sie vor der Nutzung die Signatur, die Claims und die Bindung an die Authentifizierungsanfrage. Decodieren allein reicht nicht aus. Es darf auch nicht anstelle eines Access-Tokens an eine API gesendet werden.

### 3.3 JWT-Struktur und Signaturen

Dieser Abschnitt beschreibt die **JWS Compact Serialization** eines signierten, unverschlüsselten JWT mit drei durch Punkte getrennten Teilen. JWTs können auch als JWE verschlüsselt oder verschachtelt sein und bestehen daher nicht immer aus drei Teilen.

1. **Header**: Felder wie Signaturalgorithmus `alg` und Schlüsselkennung `kid`.
2. **Payload**: Claims zu Aussteller, Empfängern, Ablaufzeit, Subjekt und weiteren Angaben.
3. **Signature**: Signatur oder MAC, erzeugt mit dem angegebenen Algorithmus. Das hier verwendete RS256 nutzt eine digitale RSA-Signatur.

Header und Payload sind lediglich Base64url-codiert. Die Signatur verbirgt ihren Inhalt nicht. Siehe auch [die Unterschiede zwischen Verschlüsselung, Hashing und Signaturen]({{< relref "post/modern-cryptography-public-key-hash-signature/index.de.md" >}}).

#### Wichtige verpflichtende Claims eines ID-Tokens

- `iss`: Ausstellerkennung des OP. Sie muss exakt mit dem erwarteten Aussteller übereinstimmen.
- `sub`: Innerhalb dieses Ausstellers eindeutige und niemals neu zugewiesene Benutzerkennung. Bei mehreren OPs identifizieren Sie Benutzer mit der Kombination aus `iss` und `sub`.
- `aud`: Vorgesehene Empfänger. Prüfen Sie, ob die `client_id` des Clients enthalten ist, und akzeptieren Sie keine zusätzlichen Empfänger, denen der Client nicht vertraut.
- `exp`: Ablaufzeitpunkt. Der aktuelle Zeitpunkt muss davor liegen.
- `iat`: Ausstellungszeitpunkt. Die Client-Richtlinie legt fest, wie alt ein Token sein darf und welche weiteren Einschränkungen gelten.

Wurde ein `nonce` in der Authentifizierungsanfrage gesendet, muss dieser Claim vorhanden sein und sein Wert geprüft werden. Werden zusätzliche Claims oder `max_age` angefordert, sind auch die entsprechenden Prüfungen erforderlich.

#### Eingabe für RS256-Signaturen

Seien `H` der geschützte Header in UTF-8, `P` die Payload in UTF-8 und `B64u` Base64url ohne Padding. Signiert wird die folgende Bytefolge; `||` steht für Verkettung.

$$
M=\operatorname{ASCII}\!\left(\operatorname{B64u}(H)\,||\,\texttt{.}\,||\,\operatorname{B64u}(P)\right),\qquad S=\operatorname{Sign}_{\mathrm{RS256}}(sk,M)
$$

RS256 verwendet RSASSA-PKCS1-v1_5 mit SHA-256. Das Hashing ist Bestandteil dieses Signaturalgorithmus; die Gleichung fügt keinen zusätzlichen äußeren Hash hinzu. Der dritte Teil des Tokens ist `B64u(S)`. Prüfen Sie die Signatur mit einem öffentlichen Schlüssel des vertrauenswürdigen OP und dem festgelegten Algorithmus. Signaturprüfung lässt sich nicht allgemein als Entschlüsselung mit dem öffentlichen Schlüssel beschreiben.

Ein ungeprüftes Token darf weder erlaubte Algorithmen noch die Bezugsquelle für Schlüssel festlegen. Verwenden Sie vertrauenswürdige JWKS aus einer überprüften OP-Konfiguration oder einem überprüften Discovery-Verfahren und berücksichtigen Sie Schlüsselrotation und Caching. `kid` dient der Auswahl innerhalb dieses vertrauenswürdigen Schlüsselsatzes. Laden Sie keine Schlüssel von einer beliebigen, im Token angegebenen URL.

#### Teilbeispiel für die Validierung in Python

Die folgende PyJWT-Funktion behandelt eine eingeschränkte Konfiguration: **RS256, keine Verschlüsselung, ein einzelner als Zeichenfolge dargestellter Empfänger und ein bereits in der Anfrage gesendeter Nonce**. Der Aufrufer übergibt als `signing_key` einen öffentlichen Schlüssel aus den JWKS des vertrauenswürdigen OP. Verpflichtende Claims müssen vorhanden sein und gültige Werte besitzen. Ist `azp` vorhanden, muss es in dieser Konfiguration mit `client_id` übereinstimmen.

Diese Funktion schließt keine Anmeldung ab. Der Aufrufer muss die Zuordnung des Callbacks zum gestarteten Vorgang, state, den Code-Austausch, den erwarteten Aussteller und die einmalige Nutzung des Nonce prüfen und verwalten. Mehrere Empfänger, Verschlüsselung, zusätzliche Authentifizierungsanforderungen, `max_age` und `acr` liegen außerhalb dieses Beispiels.

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

Die Funktion liefert die in diesem Umfang geprüften Claims zurück. Melden Sie nicht allein aufgrund einer gültigen Signatur eine erfolgreiche Authentifizierung. Verknüpfen Sie auch keine Konten anhand eines ungeprüften Namens oder einer ungeprüften E-Mail-Adresse.

## 4. Sicherheitsaspekte

### 4.1 state, nonce, PKCE und CSRF

Wenn Sie `state` verwenden, binden Sie einen unvorhersehbaren Wert sicher an den im Browser gestarteten Vorgang. Prüfen Sie beim Callback Wert, Ablauf und bisherige Nichtverwendung und markieren Sie ihn anschließend als verbraucht. Gleiche Zeichenfolgen allein verhindern nicht sämtliche Formen von [CSRF]({{< relref "post/cross-site-scripting-xss-csrf-security/index.de.md" >}}).

RFC 9700 beschreibt auch, unter welchen Voraussetzungen nach bestätigter PKCE-Unterstützung des Servers dessen CSRF-Schutz genutzt werden kann, sowie die Verwendung eines OIDC-Nonce. Diese Schutzmaßnahmen benötigen weiterhin eine Bindung an den einzelnen Vorgang und eine korrekte Prüfung. `state`, `nonce` und PKCE haben unterschiedliche Aufgaben. Konstante Werte oder ausgelassene Vergleiche bieten nicht den beabsichtigten Schutz. Bei mehreren Autorisierungsservern ist zusätzlich eine Abwehr von Mix-up-Angriffen erforderlich.

### 4.2 Ablauf und Refresh-Token

Eine kurze Lebensdauer des Access-Tokens begrenzt den Zeitraum, in dem ein gestohlenes Token nutzbar ist. Ein Wert wie 15 Minuten ist ein Entwurfsbeispiel und keine allgemeine Pflicht. Für die Prüfung von `exp` in einem signierten JWT lautet die Ablaufbedingung:

$$
T_{\mathrm{now}}<T_{\mathrm{exp}},\qquad T_{\mathrm{exp}}=T_{\mathrm{iat}}+D_{\mathrm{lifetime}}\ \text{nur bei dieser Festlegung}\ T_{\mathrm{now}}<T_{\mathrm{iat}}+D_{\mathrm{lifetime}}
$$

Diese Bedingung prüft nur den Ablauf, nicht die vollständige Gültigkeit des Tokens oder eine Zugriffsberechtigung. Prüfen Sie auch Algorithmus, Schlüssel, Aussteller, Empfänger und gegebenenfalls `nbf`, Widerrufsstatus und die Bindung an die Authentifizierungsanfrage. Verwalten Sie eine etwaige Toleranz für abweichende Uhren ausdrücklich.

Refresh-Token werden optional ausgestellt. Ohne sie muss der Client gegebenenfalls einen neuen Autorisierungsvorgang starten. Für Refresh-Token öffentlicher Clients verlangt RFC 9700 eine Bindung an den sendenden Client (sender constraints) oder Rotation. Die Bindung betrifft kryptografisch den Client, der das Token vorlegt. Der Widerruf eines Refresh-Tokens macht bereits ausgestellte Access-Token nicht zwangsläufig sofort ungültig.

### 4.3 Ablauf und Implementierung auswählen

Nutzen Sie bei Webanwendungen, SPAs und nativen Apps mit Benutzerinteraktion Autorisierungscode mit PKCE als Ausgangspunkt. Wählen Sie eine Konfiguration, die zu Client-Typ, Token-Speicherung, Anbieterunterstützung und Bedrohungsmodell passt. Erzwingen Sie diesen Ablauf nicht für andere Zwecke wie M2M mit Client-Zugangsdaten.

## Fazit

Verwenden Sie OAuth-2.0-Access-Token für Ressourcenzugriffe und prüfen Sie OIDC-ID-Token als für den Client bestimmte Authentifizierungsergebnisse. Kontrollieren Sie die Bindung des Codes an PKCE, die Signatur, verpflichtende Claims, den Nonce und die Zuordnung des Callbacks zum gestarteten Vorgang.

## Referenzen

- [RFC 6749: OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749.html) (Rollen, Token und Client-Zugangsdaten; aktualisierte Sicherheitsvorgaben siehe RFC 9700)
- [RFC 7636: PKCE](https://www.rfc-editor.org/rfc/rfc7636.html) (Abschnitt 4, Abschnitt 7.1 und Anhang B)
- [RFC 9700: Sicherheitspraktiken für OAuth 2.0](https://www.rfc-editor.org/rfc/rfc9700.html) (Abschnitte 2.1, 2.2.2 und 2.4)
- [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html) (Abschnitte 2, 3.1.3.7 und 5.7)
- [RFC 7515: JWS](https://www.rfc-editor.org/rfc/rfc7515.html) (Abschnitte 3.1 und 5.1)
- [PyJWT-API](https://pyjwt.readthedocs.io/en/stable/api.html) (erlaubte Algorithmen, verpflichtende Claims und Empfängerprüfung)
