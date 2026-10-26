---
title: "OAuth 2.0 and OIDC: Authentication, Authorization, and Token Validation"
description: "Understand authentication and authorization, OAuth 2.0 and OIDC roles, authorization code with PKCE, and ID token validation through equations and JavaScript and Python examples."
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

OAuth 2.0 is an authorization framework for granting applications limited access. OpenID Connect (OIDC) adds a way to communicate the result of end-user authentication to the client.

This article distinguishes authentication from authorization, token purposes, authorization codes and PKCE, and ID token validation. The code illustrates individual operations; it is not a complete login implementation. For a production service, use an OIDC library and provider configuration appropriate to your requirements.

## 1. Authentication and authorization

### Authentication / AuthN

Authentication checks the identity of a user or system using presented evidence. Checking an employee's identity card at a company reception desk is an analogy.

### Authorization / AuthZ

Authorization determines which operations or resources a principal may access. Confirming that someone is an employee does not mean they may enter every server room.

| Item | Authentication | Authorization |
| --- | --- | --- |
| Question | Who is it? | What is permitted? |
| Abbreviation | AuthN | AuthZ |
| Mechanism discussed here | OIDC communicates an authentication result | OAuth 2.0 grants limited access |
| Example token | An OIDC ID token | An OAuth 2.0 access token |

Not every authentication mechanism issues an ID token. OAuth 2.0 also does not define all access control within an application. After receiving a token, an API must still check the permissions required for the particular resource and operation.

OAuth 2.0 alone does not standardize how a client verifies the result of end-user authentication. Do not establish a login merely because an OAuth access token was received: use a protocol, such as OIDC, that lets the client validate the authentication result.

## 2. OAuth 2.0 roles and grants

### 2.1 Limited access

OAuth 2.0 lets a client obtain an access token on behalf of a resource owner or on its own behalf. Delegating access without giving the user's password to the client is an important feature of the authorization code flow.

### 2.2 Four roles

1. **Resource Owner**: a principal capable of granting access to a protected resource. It need not be a human user.
2. **Client**: an application that uses protected resources.
3. **Authorization Server**: a server that checks authorization, client authentication, and other conditions required by the applicable flow and issues tokens.
4. **Resource Server**: a server that validates tokens and permissions and provides protected resources.

### 2.3 Main grant types

#### Authorization Code Grant

The authorization response returns a short-lived code, which is exchanged for an access token at the token endpoint. Both **confidential clients**, which can protect credentials on a server, and **public clients**, such as SPAs and native apps, can use this flow with PKCE. Embedding a client secret in distributed application code or a browser does not make it confidential.

#### Implicit Grant

This grant returns an access token directly in the authorization response. It carries risks of token leakage, injection, and replay. RFC 9700 says clients SHOULD NOT use it unless the specified risks are mitigated. For a new configuration, choose authorization code with PKCE. Do not interpret this recommendation as an identical prohibition on every OIDC response type.

#### Resource Owner Password Credentials Grant (ROPC)

In this grant the client receives the user's password directly. Although RFC 6749 describes it, the updated security guidance in RFC 9700 says it MUST NOT be used. Do not present legacy system migration as a recommended exception.

#### Client Credentials Grant

A confidential client authenticates itself to obtain a token. It can access resources under its control, or another resource owner's resources under an arrangement with the authorization server. This commonly supports machine-to-machine communication without end-user interaction; the client does not necessarily become the resource owner.

### 2.4 Authorization code and PKCE

PKCE (Proof Key for Code Exchange) binds the client starting an authorization request to the client exchanging the code for tokens, helping protect against code interception and injection. Public clients must use it, and it is recommended for confidential clients too. It does not replace the client authentication required of a confidential client.

For each authorization transaction, the client generates a new, secret `code_verifier`. RFC 7636 specifies 43–128 characters drawn from letters, digits, and `-._~`, and recommends at least 256 bits of entropy. Encoding 32 cryptographically random bytes as unpadded Base64url produces 43 characters.

For `S256`, the challenge is calculated as follows. Omit trailing `=` padding from Base64url.

$$
\text{code\_challenge}=\operatorname{BASE64URL}\!\left(\operatorname{SHA256}\!\left(\operatorname{ASCII}(\text{code\_verifier})\right)\right)
$$

Send `code_challenge` and `code_challenge_method=S256` in the authorization request, and send the `code_verifier` retained for that transaction in the token request. The server checks it using the method and challenge recorded with the code. Do not fall back to `plain` because `S256` failed.

#### Flow overview

```mermaid
sequenceDiagram
    autonumber
    participant U as "User / browser"
    participant C as "Client"
    participant AS as "Authorization server / OIDC OP"
    participant RS as "Resource server"
    Note over C: "Retain a verifier and state per transaction; also a nonce for OIDC"
    C->>U: "Redirect to authorization endpoint"
    U->>AS: "Authorization request: challenge and S256; openid and nonce for OIDC"
    AS-->>U: "Request authentication and consent as needed"
    U->>AS: "Authenticate and authorize"
    AS-->>U: "Redirect to registered redirect_uri with code and state"
    U->>C: "Callback: code and state"
    Note over C: "Check transaction, state, and expected issuer"
    C->>AS: "Exchange code with verifier and required client authentication"
    Note over AS: "Validate code, bindings, and PKCE"
    AS-->>C: "Access token; also an ID token for OIDC"
    Note over C: "For OIDC, validate ID token and nonce"
    C->>RS: "Call API using access token"
    RS-->>C: "Validate token and permissions, then return resource"
```

This is a successful-flow overview. Protect communication with TLS. Implementations must also handle redirect validation, single-use codes, error responses, transaction expiration, and mix-up defenses when using multiple authorization servers.

#### Generating PKCE parameters (JavaScript / Web Crypto API)

These browser functions require a secure context such as HTTPS. `generatePkce()` only returns parameters: it does not send an authorization request or store the transaction. Keep the verifier out of logs and URLs, bind it to the initiating browser transaction, and discard it after exchange or expiration.

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

This encodes every bit of the 32 random bytes. The former example concatenated only the last two hexadecimal digits of each of 28 random 32-bit integers, retaining 224 bits despite drawing 896 bits; it has been corrected.

## 3. OIDC and ID tokens

### 3.1 Adding an authentication layer

With OIDC, the client (Relying Party) requests authentication using the `openid` scope, and the OpenID Provider (OP) returns the result in an ID token. Users need not enter a password every time: the OP may use an existing session or another authentication method.

### 3.2 Keep token purposes separate

- **Access token**: a credential for accessing a resource server. It may be a JWT or an opaque string; OAuth 2.0 does not prescribe a single format. Clients should follow the API's requirements rather than assume an internal structure.
- **ID token**: a JWT representing an authentication result for the client. Validate its signature, claims, and binding to the authentication request before using it. Decoding alone is insufficient, and it must not be sent as a substitute for an API access token.

### 3.3 JWT structure and signatures

This section describes **JWS Compact Serialization** for a signed, unencrypted JWT, consisting of three dot-separated parts. JWTs can also be encrypted as JWE or nested; they do not always have three parts.

1. **Header**: fields such as the signature algorithm `alg` and key identifier `kid`.
2. **Payload**: claims such as issuer, audience, expiration, and subject.
3. **Signature**: a signature or MAC generated by the specified algorithm. RS256, discussed here, uses an RSA digital signature.

The header and payload are only Base64url-encoded. Signing does not hide their contents. See also [the differences between encryption, hashing, and signatures]({{< relref "post/modern-cryptography-public-key-hash-signature/index.en.md" >}}).

#### Main required ID token claims

- `iss`: the OP's issuer identifier, which must exactly match the expected issuer.
- `sub`: a subject identifier that is unique and never reassigned within that issuer. Combine it with `iss` when identifying users across multiple OPs.
- `aud`: the intended recipient or recipients. Check that it includes the client's `client_id`, and do not accept additional untrusted audiences.
- `exp`: expiration time. The current time must be before it.
- `iat`: issuance time. Client policy determines acceptable age and related restrictions.

If a `nonce` was sent in the authentication request, require that claim and check its value. Requesting additional claims or `max_age` also requires corresponding validation.

#### What RS256 signs

Let `H` be the UTF-8 protected header, `P` the UTF-8 payload, and `B64u` unpadded Base64url. The bytes to be signed are defined below; `||` denotes concatenation.

$$
M=\operatorname{ASCII}\!\left(\operatorname{B64u}(H)\,||\,\texttt{.}\,||\,\operatorname{B64u}(P)\right),\qquad S=\operatorname{Sign}_{\mathrm{RS256}}(sk,M)
$$

RS256 uses RSASSA-PKCS1-v1_5 with SHA-256. Hashing is part of that signature algorithm; the equation does not add an extra outer hash. The token's third part is `B64u(S)`. Verify it using a trusted OP key and the specified algorithm, rather than describing signature verification generally as public-key decryption.

Do not let an unverified token choose allowed algorithms or where keys are fetched. Use trusted JWKS obtained from verified OP configuration or Discovery, and handle key rotation and caching. Use `kid` to select within that trusted key set; do not fetch keys from an arbitrary URL supplied by the token.

#### A partial validation example in Python

The following PyJWT function supports a deliberately limited configuration: **RS256, no encryption, a single string audience, and a nonce already sent in the request**. The caller supplies `signing_key`, a public key from the trusted OP's JWKS. Required claims must be present as well as valid. If `azp` is present, this configuration requires it to equal `client_id`.

This function does not complete a login. The caller must validate and manage the callback's relationship to the initiating transaction, state, code exchange, expected issuer, and single use of the nonce. Multiple audiences, encryption, additional authentication requirements, `max_age`, and `acr` are outside this example's scope.

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

The return value contains claims validated within that scope. Do not announce successful authentication based only on a valid signature, or link accounts using an unverified name or email address.

## 4. Security considerations

### 4.1 state, nonce, PKCE, and CSRF

When using `state`, securely bind an unpredictable value to the initiating browser transaction. At the callback, check its value, expiration, and unused status, then consume it. String equality alone does not prevent every kind of [CSRF]({{< relref "post/cross-site-scripting-xss-csrf-security/index.en.md" >}}).

RFC 9700 also describes relying on PKCE's CSRF protection after establishing server support, and using an OIDC nonce. These protections still require transaction-specific binding and proper validation. `state`, `nonce`, and PKCE have different roles; constant values or omitted comparisons do not provide the intended protection. Multiple authorization servers additionally require a mix-up defense.

### 4.2 Expiration and refresh tokens

A short access-token lifetime is one way to limit the useful lifetime of a stolen token. A value such as 15 minutes is a design example, not a universal requirement. When checking a signed JWT's `exp`, the expiration condition is:

$$
T_{\mathrm{now}}<T_{\mathrm{exp}},\qquad T_{\mathrm{now}}<T_{\mathrm{iat}}+D_{\mathrm{lifetime}}\ \text{only if}\ T_{\mathrm{exp}}=T_{\mathrm{iat}}+D_{\mathrm{lifetime}}
$$

This checks expiration only; it does not establish overall token validity or access permission. Also validate the algorithm, key, issuer, audience, and, where applicable, `nbf`, revocation status, and binding to the authentication request. Manage any allowed clock skew explicitly.

Issuing refresh tokens is optional. Without one, a client may need a new authorization transaction. RFC 9700 requires sender constraints or rotation for refresh tokens issued to public clients. Revoking a refresh token does not necessarily invalidate previously issued access tokens immediately.

### 4.3 Choosing a flow and implementation

For user-interactive web, SPA, and native applications, start with authorization code and PKCE, then choose a configuration appropriate to the client type, token storage, provider support, and threat model. Do not impose that flow on every use case, such as machine-to-machine client credentials.

## Conclusion

Use OAuth 2.0 access tokens for resource access and validate OIDC ID tokens as authentication results intended for the client. Check the code's binding to PKCE, the signature, required claims, nonce, and the callback's relationship to the initiating transaction.

## References

- [RFC 6749: OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749.html) (roles, tokens, and client credentials; see RFC 9700 for updated security guidance)
- [RFC 7636: PKCE](https://www.rfc-editor.org/rfc/rfc7636.html) (Section 4, Section 7.1, and Appendix B)
- [RFC 9700: OAuth 2.0 Security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) (Sections 2.1, 2.2.2, and 2.4)
- [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html) (Sections 2, 3.1.3.7, and 5.7)
- [RFC 7515: JWS](https://www.rfc-editor.org/rfc/rfc7515.html) (Sections 3.1 and 5.1)
- [PyJWT API](https://pyjwt.readthedocs.io/en/stable/api.html) (allowed algorithms, required claims, and audience validation)
