---
title: "OAuth 2.0 et OIDC : authentification, autorisation et validation des jetons"
description: "Authentification et autorisation, rôles d'OAuth 2.0 et d'OIDC, code d'autorisation avec PKCE et validation du jeton d'identité à l'aide de formules et d'exemples JavaScript et Python."
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

OAuth 2.0 est un cadre d'autorisation qui accorde aux applications un accès limité. OpenID Connect (OIDC) y ajoute un mécanisme permettant de transmettre au client le résultat de l'authentification de l'utilisateur final.

Cet article distingue l'authentification de l'autorisation, les usages des jetons, le code d'autorisation avec PKCE et la validation du jeton d'identité. Le code illustre des opérations précises ; il ne constitue pas une implémentation complète de connexion. En production, utilisez une bibliothèque OIDC et une configuration du fournisseur adaptées à vos exigences.

## 1. Authentification et autorisation

### Authentification / AuthN

L'authentification vérifie l'identité d'un utilisateur ou d'un système à partir des éléments présentés. On peut la comparer au contrôle du badge d'un employé à l'accueil d'une entreprise.

### Autorisation / AuthZ

L'autorisation détermine les opérations qu'une entité peut effectuer et les ressources auxquelles elle peut accéder. Confirmer qu'une personne est employée ne lui donne pas accès à toutes les salles de serveurs.

| Élément | Authentification | Autorisation |
| --- | --- | --- |
| Question | Qui est-ce ? | Qu'est-ce qui est permis ? |
| Abréviation | AuthN | AuthZ |
| Mécanisme étudié ici | OIDC transmet un résultat d'authentification | OAuth 2.0 accorde un accès limité |
| Exemple de jeton | Jeton d'identité OIDC | Jeton d'accès OAuth 2.0 |

Tous les mécanismes d'authentification n'émettent pas de jeton d'identité. OAuth 2.0 ne définit pas non plus l'ensemble du contrôle d'accès d'une application. Après réception d'un jeton, l'API doit encore vérifier les permissions nécessaires pour la ressource et l'opération concernées.

OAuth 2.0 seul ne normalise pas la manière dont le client vérifie le résultat de l'authentification de l'utilisateur final. Recevoir un jeton d'accès ne suffit pas à établir une connexion : utilisez un protocole, tel qu'OIDC, qui permet de valider ce résultat.

## 2. Rôles et types d'octroi d'OAuth 2.0

### 2.1 Un accès limité

OAuth 2.0 permet au client d'obtenir un jeton d'accès au nom du propriétaire de la ressource ou pour son propre compte. Déléguer un accès sans transmettre le mot de passe de l'utilisateur au client est une caractéristique importante du flux de code d'autorisation.

### 2.2 Quatre rôles

1. **Propriétaire de la ressource (Resource Owner)** : entité capable d'autoriser l'accès à une ressource protégée. Il ne s'agit pas nécessairement d'une personne.
2. **Client** : application qui utilise des ressources protégées.
3. **Serveur d'autorisation (Authorization Server)** : serveur qui vérifie l'autorisation, l'authentification du client et les autres conditions du flux applicable, puis émet les jetons.
4. **Serveur de ressources (Resource Server)** : serveur qui valide les jetons et les permissions, puis fournit les ressources protégées.

### 2.3 Principaux types d'octroi

#### Code d'autorisation (Authorization Code Grant)

La réponse d'autorisation renvoie un code de courte durée, échangé contre un jeton d'accès au point de terminaison de jetons. Les **clients confidentiels**, capables de protéger leurs éléments d'authentification sur un serveur, ainsi que les **clients publics**, notamment les SPA et les applications natives, peuvent utiliser ce flux avec PKCE. Intégrer un secret client dans du code distribué ou dans un navigateur ne permet pas de le garder secret.

#### Octroi implicite (Implicit Grant)

Ce mécanisme renvoie directement un jeton d'accès dans la réponse d'autorisation. Il présente des risques de fuite, d'injection et de réutilisation des jetons. La RFC 9700 indique que les clients NE DEVRAIENT PAS l'utiliser (SHOULD NOT), sauf si les risques précisés sont atténués. Pour une nouvelle configuration, choisissez le code d'autorisation avec PKCE. N'interprétez pas cette recommandation comme une interdiction identique de tous les types de réponse OIDC.

#### Mot de passe du propriétaire de la ressource (ROPC)

Dans ce mécanisme, le client reçoit directement le mot de passe de l'utilisateur. Bien que la RFC 6749 le décrive, les recommandations de sécurité actualisées de la RFC 9700 imposent de **NE PAS l'utiliser (MUST NOT)**. La migration de systèmes anciens ne doit pas être présentée comme une exception recommandée.

#### Informations d'authentification du client (Client Credentials Grant)

Un client confidentiel s'authentifie pour obtenir un jeton. Il peut accéder à des ressources qu'il contrôle ou à celles d'un autre propriétaire selon un accord préalable avec le serveur d'autorisation. Ce flux sert généralement aux communications entre systèmes sans interaction de l'utilisateur final ; le client ne devient pas nécessairement le propriétaire de la ressource.

### 2.4 Code d'autorisation et PKCE

PKCE (Proof Key for Code Exchange) lie le client qui lance une requête d'autorisation à celui qui échange le code contre des jetons, ce qui contribue à protéger contre l'interception et l'injection de codes. Il est obligatoire pour les clients publics et également recommandé pour les clients confidentiels. Il ne remplace pas l'authentification exigée d'un client confidentiel.

Pour chaque transaction d'autorisation, le client génère un nouveau `code_verifier` secret. La RFC 7636 impose entre 43 et 128 caractères choisis parmi les lettres, les chiffres et `-._~`, et recommande au moins 256 bits d'entropie. Encoder 32 octets issus d'un générateur cryptographiquement sûr en Base64url sans remplissage produit 43 caractères.

Avec `S256`, le défi est calculé comme suit. Les caractères de remplissage `=` en fin de Base64url sont omis.

$$
\text{code\_challenge}=\operatorname{BASE64URL}\!\left(\operatorname{SHA256}\!\left(\operatorname{ASCII}(\text{code\_verifier})\right)\right)
$$

La requête d'autorisation envoie `code_challenge` et `code_challenge_method=S256`. La requête de jeton envoie le `code_verifier` conservé pour cette même transaction. Le serveur le vérifie avec la méthode et le défi enregistrés avec le code. Ne revenez pas à `plain` parce que `S256` a échoué.

#### Vue d'ensemble du flux

```mermaid
sequenceDiagram
    autonumber
    participant U as "Utilisateur / navigateur"
    participant C as "Client"
    participant AS as "Serveur d'autorisation / OP OIDC"
    participant RS as "Serveur de ressources"
    Note over C: "Conserver verifier et state par transaction ; aussi nonce pour OIDC"
    C->>U: "Rediriger vers le point de terminaison d'autorisation"
    U->>AS: "Requête : challenge et S256 ; openid et nonce pour OIDC"
    AS-->>U: "Demander authentification et consentement si nécessaire"
    U->>AS: "Effectuer l'authentification et l'autorisation"
    AS-->>U: "Rediriger vers le redirect_uri enregistré avec code et state"
    U->>C: "Retour : code et state"
    Note over C: "Vérifier transaction, state et émetteur attendu"
    C->>AS: "Échanger code avec verifier et l'authentification du client requise"
    Note over AS: "Valider code, liaisons et PKCE"
    AS-->>C: "Jeton d'accès ; aussi jeton d'identité pour OIDC"
    Note over C: "Pour OIDC, valider jeton d'identité et nonce"
    C->>RS: "Appeler l'API avec le jeton d'accès"
    RS-->>C: "Valider jeton et permissions, puis renvoyer la ressource"
```

Ce diagramme résume un déroulement réussi. Protégez les communications avec TLS. L'implémentation doit également traiter la validation des redirections, l'usage unique des codes, les réponses d'erreur, l'expiration de la transaction et la protection contre les attaques de confusion de serveurs (mix-up) lorsqu'elle utilise plusieurs serveurs d'autorisation.

#### Génération des paramètres PKCE (JavaScript / Web Crypto API)

Ces fonctions destinées au navigateur nécessitent un contexte sécurisé, tel que HTTPS. `generatePkce()` renvoie uniquement les paramètres : elle n'envoie pas la requête d'autorisation et ne stocke pas la transaction. N'exposez pas le verifier dans les journaux ou les URL ; liez-le à la transaction commencée dans ce navigateur, puis supprimez-le après l'échange ou l'expiration.

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

Ce code encode tous les bits des 32 octets aléatoires. L'ancien exemple concaténait seulement les deux derniers chiffres hexadécimaux de chacun de 28 entiers aléatoires de 32 bits : il obtenait 896 bits, mais n'en conservait que 224. Cette troncature a été corrigée.

## 3. OIDC et jetons d'identité

### 3.1 Ajouter une couche d'authentification à OAuth

Avec OIDC, le client (Relying Party) demande l'authentification avec la portée `openid`, et l'OpenID Provider (OP) renvoie le résultat dans un jeton d'identité. L'utilisateur ne saisit pas nécessairement son mot de passe à chaque fois : l'OP peut utiliser une session existante ou un autre moyen d'authentification.

### 3.2 Séparer les usages des jetons

- **Jeton d'accès** : justificatif d'accès à un serveur de ressources. Il peut s'agir d'un JWT ou d'une chaîne opaque ; OAuth 2.0 n'impose pas un format unique. Le client doit suivre les exigences de l'API, sans supposer une structure interne.
- **Jeton d'identité** : JWT représentant un résultat d'authentification destiné au client. Avant de l'utiliser, validez sa signature, ses déclarations et sa liaison avec la requête d'authentification. Le décodage seul ne suffit pas ; il ne doit pas non plus être envoyé à la place d'un jeton d'accès à l'API.

### 3.3 Structure des JWT et signatures

Cette section décrit la **JWS Compact Serialization** d'un JWT signé et non chiffré, composé de trois parties séparées par des points. Un JWT peut aussi être chiffré sous forme de JWE ou imbriqué : il ne comporte pas toujours trois parties.

1. **Header (en-tête)** : champs tels que l'algorithme de signature `alg` et l'identifiant de clé `kid`.
2. **Payload (charge utile)** : déclarations sur l'émetteur, les destinataires, l'expiration, le sujet, etc.
3. **Signature** : signature ou MAC produit par l'algorithme indiqué. RS256, utilisé ici, emploie une signature numérique RSA.

L'en-tête et la charge utile sont seulement encodés en Base64url. La signature ne masque pas leur contenu. Consultez aussi [les différences entre chiffrement, hachage et signature]({{< relref "post/modern-cryptography-public-key-hash-signature/index.fr.md" >}}).

#### Principales déclarations obligatoires du jeton d'identité

- `iss` : identifiant d'émetteur de l'OP, qui doit correspondre exactement à l'émetteur attendu.
- `sub` : identifiant unique de l'utilisateur, jamais réattribué au sein de cet émetteur. Si vous utilisez plusieurs OP, associez-le à `iss` pour identifier l'utilisateur.
- `aud` : destinataire ou destinataires prévus. Vérifiez la présence du `client_id` du client et n'acceptez pas de destinataires supplémentaires non fiables.
- `exp` : instant d'expiration. L'instant courant doit lui être antérieur.
- `iat` : instant d'émission. La politique du client définit l'ancienneté acceptable et les autres restrictions.

Si la requête d'authentification a envoyé un `nonce`, exigez cette déclaration et vérifiez sa valeur. Toute demande de déclarations supplémentaires ou de `max_age` nécessite également les validations correspondantes.

#### Entrée de la signature RS256

Soient `H` l'en-tête protégé en UTF-8, `P` la charge utile en UTF-8 et `B64u` l'encodage Base64url sans remplissage. L'entrée de la signature est la séquence d'octets suivante ; `||` désigne la concaténation.

$$
M=\operatorname{ASCII}\!\left(\operatorname{B64u}(H)\,||\,\texttt{.}\,||\,\operatorname{B64u}(P)\right),\qquad S=\operatorname{Sign}_{\mathrm{RS256}}(sk,M)
$$

RS256 utilise RSASSA-PKCS1-v1_5 avec SHA-256. Le hachage fait partie de cet algorithme de signature ; l'équation n'ajoute pas de hachage externe supplémentaire. La troisième partie du jeton est `B64u(S)`. Vérifiez la signature avec une clé publique de l'OP de confiance et l'algorithme indiqué, sans présenter la vérification des signatures en général comme un déchiffrement avec la clé publique.

Ne laissez pas un jeton non vérifié choisir les algorithmes permis ou l'origine des clés. Utilisez un JWKS de confiance issu d'une configuration ou d'une procédure Discovery de l'OP dûment vérifiées, et gérez la rotation ainsi que le cache des clés. `kid` sert à sélectionner une clé dans cet ensemble de confiance ; ne récupérez pas de clé à une URL arbitraire fournie par le jeton.

#### Exemple partiel de validation en Python

La fonction PyJWT ci-dessous vise une configuration limitée : **RS256, sans chiffrement, un seul destinataire représenté par une chaîne et un nonce déjà envoyé dans la requête**. L'appelant fournit `signing_key`, une clé publique provenant du JWKS de l'OP de confiance. Les déclarations obligatoires doivent être présentes, en plus d'avoir des valeurs valides. Si `azp` est présent, cette configuration exige qu'il corresponde à `client_id`.

Cette fonction ne suffit pas à terminer une connexion. L'appelant doit vérifier et gérer la correspondance entre le retour et la transaction initiale, state, l'échange du code, l'émetteur attendu et l'usage unique du nonce. Les destinataires multiples, le chiffrement, les exigences d'authentification supplémentaires, `max_age` et `acr` sortent du périmètre de cet exemple.

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

La fonction renvoie les déclarations validées dans ce périmètre. N'annoncez pas une authentification réussie sur la seule base d'une signature valide, et ne liez pas de comptes à partir d'un nom ou d'une adresse électronique non vérifiés.

## 4. Considérations de sécurité

### 4.1 state, nonce, PKCE et CSRF

Si vous utilisez `state`, liez de manière sûre une valeur imprévisible à la transaction commencée dans le navigateur. Au retour, vérifiez sa valeur, son expiration et le fait qu'elle n'a pas encore été utilisée, puis marquez-la comme utilisée. L'égalité des chaînes ne suffit pas à empêcher toutes les formes de [CSRF]({{< relref "post/cross-site-scripting-xss-csrf-security/index.fr.md" >}}).

La RFC 9700 traite aussi de la possibilité de s'appuyer sur la protection CSRF de PKCE après avoir confirmé sa prise en charge par le serveur, ainsi que de l'utilisation du nonce OIDC. Ces protections nécessitent toujours une liaison propre à chaque transaction et une validation correcte. `state`, `nonce` et PKCE ont des rôles distincts ; des valeurs constantes ou des comparaisons omises ne fournissent pas la protection attendue. Plusieurs serveurs d'autorisation nécessitent également une défense contre les attaques mix-up.

### 4.2 Expiration et jetons de renouvellement

Une courte durée de vie du jeton d'accès permet de limiter la période d'utilisation d'un jeton volé. Une valeur de 15 minutes, par exemple, est un choix de conception, pas une obligation universelle. Lors de la vérification de `exp` dans un JWT signé, la condition d'expiration est :

$$
T_{\mathrm{now}}<T_{\mathrm{exp}},\qquad T_{\mathrm{exp}}=T_{\mathrm{iat}}+D_{\mathrm{lifetime}}\ \text{uniquement si défini ainsi}\ T_{\mathrm{now}}<T_{\mathrm{iat}}+D_{\mathrm{lifetime}}
$$

Cette condition vérifie uniquement l'expiration ; elle ne démontre ni la validité complète du jeton ni les droits d'accès. Vérifiez aussi l'algorithme, la clé, l'émetteur, les destinataires et, selon le cas, `nbf`, l'état de révocation et la liaison avec la requête d'authentification. Gérez explicitement toute tolérance aux écarts d'horloge.

L'émission de jetons de renouvellement est facultative. Sans eux, le client peut avoir besoin d'une nouvelle transaction d'autorisation. Pour ceux émis aux clients publics, la RFC 9700 exige une liaison cryptographique au client qui présente le jeton (sender constraints) ou une rotation. Révoquer un jeton de renouvellement n'invalide pas nécessairement immédiatement les jetons d'accès déjà émis.

### 4.3 Choisir un flux et une implémentation

Pour les applications Web, SPA et natives avec interaction de l'utilisateur, partez du code d'autorisation avec PKCE. Choisissez une configuration adaptée au type de client, au stockage des jetons, à la prise en charge du fournisseur et au modèle de menace. N'imposez pas le même flux à tous les usages, comme le flux Client Credentials pour les échanges M2M.

## Conclusion

Utilisez les jetons d'accès OAuth 2.0 pour accéder aux ressources et validez les jetons d'identité OIDC comme résultats d'authentification destinés au client. Vérifiez la liaison du code avec PKCE, la signature, les déclarations obligatoires, le nonce et la correspondance entre le retour et la transaction initiale.

## Références

- [RFC 6749 : OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749.html) (rôles, jetons et informations d'authentification du client ; voir la RFC 9700 pour les recommandations de sécurité actualisées)
- [RFC 7636 : PKCE](https://www.rfc-editor.org/rfc/rfc7636.html) (section 4, section 7.1 et annexe B)
- [RFC 9700 : bonnes pratiques de sécurité OAuth 2.0](https://www.rfc-editor.org/rfc/rfc9700.html) (sections 2.1, 2.2.2 et 2.4)
- [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html) (sections 2, 3.1.3.7 et 5.7)
- [RFC 7515 : JWS](https://www.rfc-editor.org/rfc/rfc7515.html) (sections 3.1 et 5.1)
- [API PyJWT](https://pyjwt.readthedocs.io/en/stable/api.html) (algorithmes permis, déclarations obligatoires et validation du destinataire)
