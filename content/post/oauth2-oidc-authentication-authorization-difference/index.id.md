---
title: "OAuth 2.0 dan OIDC: autentikasi, otorisasi, dan validasi token"
description: "Autentikasi dan otorisasi, peran OAuth 2.0 dan OIDC, kode otorisasi dengan PKCE, serta validasi token ID melalui rumus dan contoh JavaScript serta Python."
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

OAuth 2.0 adalah kerangka kerja otorisasi untuk memberikan akses terbatas kepada aplikasi. OpenID Connect (OIDC) menambahkan mekanisme untuk menyampaikan hasil autentikasi pengguna akhir kepada klien.

Artikel ini membedakan autentikasi dan otorisasi, tujuan penggunaan token, kode otorisasi dengan PKCE, serta validasi token ID. Kode hanya mencontohkan operasi tertentu, bukan implementasi login lengkap. Untuk layanan produksi, gunakan pustaka OIDC dan konfigurasi penyedia yang sesuai dengan kebutuhan Anda.

## 1. Autentikasi dan otorisasi

### Autentikasi / AuthN

Autentikasi memeriksa identitas pengguna atau sistem berdasarkan bukti yang diberikan. Analoginya adalah pemeriksaan kartu identitas karyawan di resepsionis perusahaan.

### Otorisasi / AuthZ

Otorisasi menentukan operasi yang boleh dilakukan suatu pihak dan sumber daya yang boleh diaksesnya. Memastikan seseorang adalah karyawan tidak berarti mengizinkannya masuk ke semua ruang server.

| Aspek | Autentikasi | Otorisasi |
| --- | --- | --- |
| Pertanyaan | Siapa pihak tersebut? | Apa yang diizinkan? |
| Singkatan | AuthN | AuthZ |
| Mekanisme yang dibahas | OIDC menyampaikan hasil autentikasi | OAuth 2.0 memberikan akses terbatas |
| Contoh token | Token ID OIDC | Token akses OAuth 2.0 |

Tidak semua mekanisme autentikasi menerbitkan token ID. OAuth 2.0 juga tidak mendefinisikan seluruh kontrol akses dalam aplikasi. Setelah menerima token, API masih harus memeriksa izin yang diperlukan untuk sumber daya dan operasi tertentu.

OAuth 2.0 sendiri tidak menstandarkan cara klien memverifikasi hasil autentikasi pengguna akhir. Menerima token akses saja tidak cukup untuk menyatakan pengguna sudah login. Gunakan protokol seperti OIDC yang memungkinkan hasil tersebut divalidasi.

## 2. Peran dan tipe grant OAuth 2.0

### 2.1 Akses terbatas

OAuth 2.0 memungkinkan klien memperoleh token akses atas nama pemilik sumber daya atau atas namanya sendiri. Pendelegasian akses tanpa memberikan kata sandi pengguna kepada klien merupakan salah satu ciri penting alur kode otorisasi.

### 2.2 Empat peran

1. **Pemilik sumber daya (Resource Owner)**: pihak yang dapat mengizinkan akses ke sumber daya yang dilindungi. Pihak ini tidak harus berupa manusia.
2. **Klien (Client)**: aplikasi yang menggunakan sumber daya yang dilindungi.
3. **Server otorisasi (Authorization Server)**: server yang memeriksa otorisasi, autentikasi klien, dan persyaratan lain sesuai alur yang digunakan, lalu menerbitkan token.
4. **Server sumber daya (Resource Server)**: server yang memvalidasi token dan izin, lalu menyediakan sumber daya yang dilindungi.

### 2.3 Tipe grant utama

#### Kode otorisasi (Authorization Code Grant)

Respons otorisasi mengembalikan kode berumur pendek yang ditukar dengan token akses di endpoint token. **Klien konfidensial (confidential client)**, yang dapat melindungi kredensial di server, maupun **klien publik (public client)**, seperti SPA dan aplikasi native, dapat menggunakan alur ini dengan PKCE. Menanamkan rahasia klien dalam kode aplikasi yang didistribusikan atau dalam peramban tidak membuatnya tetap rahasia.

#### Grant implisit (Implicit Grant)

Grant ini mengembalikan token akses langsung dalam respons otorisasi. Ada risiko kebocoran, penyisipan, dan penggunaan ulang token. RFC 9700 menyatakan klien SEBAIKNYA TIDAK menggunakannya (SHOULD NOT), kecuali risiko yang disebutkan telah dimitigasi. Untuk konfigurasi baru, pilih kode otorisasi dengan PKCE. Jangan menafsirkan rekomendasi ini sebagai larangan yang sama terhadap semua tipe respons OIDC.

#### Kredensial kata sandi pemilik sumber daya (ROPC)

Dalam grant ini, klien menerima kata sandi pengguna secara langsung. Walaupun RFC 6749 menjelaskannya, pedoman keamanan yang diperbarui dalam RFC 9700 menetapkan bahwa grant ini **TIDAK BOLEH digunakan (MUST NOT)**. Migrasi sistem lama tidak boleh disajikan sebagai pengecualian yang direkomendasikan.

#### Kredensial klien (Client Credentials Grant)

Klien konfidensial mengautentikasi dirinya untuk memperoleh token. Klien dapat mengakses sumber daya yang dikendalikannya atau sumber daya milik pihak lain berdasarkan kesepakatan sebelumnya dengan server otorisasi. Grant ini biasanya digunakan untuk komunikasi antarsistem tanpa interaksi pengguna akhir; klien tidak selalu menjadi pemilik sumber daya.

### 2.4 Kode otorisasi dan PKCE

PKCE (Proof Key for Code Exchange) mengikat klien yang memulai permintaan otorisasi dengan klien yang menukar kode menjadi token, sehingga membantu melindungi dari intersepsi dan penyisipan kode. PKCE wajib digunakan oleh klien publik dan juga direkomendasikan untuk klien konfidensial. PKCE tidak menggantikan autentikasi yang diwajibkan bagi klien konfidensial.

Untuk setiap transaksi otorisasi, klien menghasilkan `code_verifier` rahasia yang baru. RFC 7636 menetapkan panjang 43–128 karakter dari huruf, angka, dan `-._~`, serta merekomendasikan entropi setidaknya 256 bit. Mengodekan 32 byte dari generator acak yang aman secara kriptografis sebagai Base64url tanpa padding menghasilkan 43 karakter.

Untuk `S256`, challenge dihitung sebagai berikut. Padding `=` di akhir Base64url dihilangkan.

$$
\text{code\_challenge}=\operatorname{BASE64URL}\!\left(\operatorname{SHA256}\!\left(\operatorname{ASCII}(\text{code\_verifier})\right)\right)
$$

Permintaan otorisasi mengirimkan `code_challenge` dan `code_challenge_method=S256`. Permintaan token mengirimkan `code_verifier` yang disimpan untuk transaksi yang sama. Server memeriksanya menggunakan metode dan challenge yang dicatat bersama kode. Jangan beralih ke `plain` hanya karena `S256` gagal.

#### Gambaran alur

```mermaid
sequenceDiagram
    autonumber
    participant U as "Pengguna / peramban"
    participant C as "Klien"
    participant AS as "Server otorisasi / OP OIDC"
    participant RS as "Server sumber daya"
    Note over C: "Simpan verifier dan state per transaksi; juga nonce untuk OIDC"
    C->>U: "Alihkan ke endpoint otorisasi"
    U->>AS: "Permintaan: challenge dan S256; openid dan nonce untuk OIDC"
    AS-->>U: "Minta autentikasi dan persetujuan bila diperlukan"
    U->>AS: "Lakukan autentikasi dan otorisasi"
    AS-->>U: "Alihkan ke redirect_uri terdaftar dengan code dan state"
    U->>C: "Callback: code dan state"
    Note over C: "Periksa transaksi, state, dan penerbit yang diharapkan"
    C->>AS: "Tukar code dengan verifier dan autentikasi klien yang diwajibkan"
    Note over AS: "Validasi kode, pengikatan, dan PKCE"
    AS-->>C: "Token akses; juga token ID untuk OIDC"
    Note over C: "Untuk OIDC, validasi token ID dan nonce"
    C->>RS: "Panggil API dengan token akses"
    RS-->>C: "Validasi token dan izin, lalu kembalikan sumber daya"
```

Diagram ini merangkum alur yang berhasil. Lindungi komunikasi dengan TLS. Implementasi juga perlu menangani validasi tujuan pengalihan, penggunaan kode hanya sekali, respons kesalahan, kedaluwarsa transaksi, serta perlindungan terhadap serangan mix-up ketika menggunakan beberapa server otorisasi.

#### Menghasilkan parameter PKCE (JavaScript / Web Crypto API)

Fungsi untuk peramban ini memerlukan konteks aman, seperti HTTPS. `generatePkce()` hanya mengembalikan parameter: fungsi ini tidak mengirim permintaan otorisasi atau menyimpan transaksi. Jangan menampilkan verifier dalam log atau URL. Ikat verifier ke transaksi yang dimulai di peramban tersebut dan buang setelah pertukaran selesai atau transaksi kedaluwarsa.

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

Kode ini mengodekan seluruh bit dari 32 byte acak. Contoh sebelumnya hanya menggabungkan dua digit heksadesimal terakhir dari masing-masing 28 bilangan bulat acak 32 bit: 896 bit diambil, tetapi hanya 224 bit dipertahankan. Pemotongan tersebut telah diperbaiki.

## 3. OIDC dan token ID

### 3.1 Menambahkan lapisan autentikasi pada OAuth

Dalam OIDC, klien (Relying Party) meminta autentikasi dengan scope `openid`, lalu OpenID Provider (OP) mengembalikan hasilnya melalui token ID. Pengguna tidak harus mengetik kata sandi setiap kali: OP dapat menggunakan sesi yang sudah ada atau metode autentikasi lain.

### 3.2 Memisahkan tujuan token

- **Token akses**: kredensial untuk mengakses server sumber daya. Formatnya bisa berupa JWT atau string opak (opaque); OAuth 2.0 tidak mewajibkan satu format. Klien harus mengikuti persyaratan API tanpa mengasumsikan struktur internal token.
- **Token ID**: JWT yang menyatakan hasil autentikasi untuk klien. Sebelum menggunakannya, validasi tanda tangan, klaim, serta keterikatannya dengan permintaan autentikasi. Dekode saja tidak cukup. Token ini juga tidak boleh dikirim sebagai pengganti token akses API.

### 3.3 Struktur JWT dan tanda tangan

Bagian ini menjelaskan **JWS Compact Serialization** untuk JWT bertanda tangan yang tidak dienkripsi, dengan tiga bagian yang dipisahkan titik. JWT juga dapat dienkripsi sebagai JWE atau disusun secara bersarang; jadi, tidak selalu terdiri dari tiga bagian.

1. **Header**: bidang seperti algoritma tanda tangan `alg` dan pengidentifikasi kunci `kid`.
2. **Payload**: klaim tentang penerbit, penerima, waktu kedaluwarsa, subjek, dan informasi lain.
3. **Signature (tanda tangan)**: tanda tangan atau MAC yang dihasilkan dengan algoritma yang ditetapkan. RS256 yang dibahas di sini menggunakan tanda tangan digital RSA.

Header dan payload hanya dikodekan sebagai Base64url. Tanda tangan tidak menyembunyikan isinya. Lihat juga [perbedaan enkripsi, hash, dan tanda tangan]({{< relref "post/modern-cryptography-public-key-hash-signature/index.id.md" >}}).

#### Klaim wajib utama pada token ID

- `iss`: pengidentifikasi penerbit OP. Nilainya harus sama persis dengan penerbit yang diharapkan.
- `sub`: pengidentifikasi pengguna yang unik dan tidak pernah dialokasikan ulang dalam lingkup penerbit tersebut. Jika menggunakan beberapa OP, gabungkan dengan `iss` untuk mengidentifikasi pengguna.
- `aud`: penerima yang dituju. Pastikan `client_id` klien tercakup dan jangan menerima penerima tambahan yang tidak dipercaya.
- `exp`: waktu kedaluwarsa. Waktu saat ini harus lebih awal.
- `iat`: waktu penerbitan. Kebijakan klien menentukan usia token yang dapat diterima dan pembatasan lainnya.

Jika permintaan autentikasi mengirimkan `nonce`, wajibkan keberadaan klaim itu dan periksa nilainya. Permintaan klaim tambahan atau `max_age` juga membutuhkan validasi yang sesuai.

#### Masukan tanda tangan RS256

Misalkan `H` adalah header terlindungi dalam UTF-8, `P` adalah payload dalam UTF-8, dan `B64u` adalah pengodean Base64url tanpa padding. Masukan tanda tangan adalah urutan byte berikut; `||` berarti penggabungan.

$$
M=\operatorname{ASCII}\!\left(\operatorname{B64u}(H)\,||\,\texttt{.}\,||\,\operatorname{B64u}(P)\right),\qquad S=\operatorname{Sign}_{\mathrm{RS256}}(sk,M)
$$

RS256 menggunakan RSASSA-PKCS1-v1_5 dengan SHA-256. Penghitungan hash merupakan bagian dari algoritma tanda tangan tersebut; persamaan ini tidak menambahkan hash luar lagi. Bagian ketiga token adalah `B64u(S)`. Verifikasi tanda tangan dengan kunci publik OP yang dipercaya dan algoritma yang ditetapkan. Jangan menjelaskan verifikasi tanda tangan secara umum sebagai dekripsi dengan kunci publik.

Jangan biarkan token yang belum diverifikasi menentukan algoritma yang diizinkan atau sumber kunci. Gunakan JWKS tepercaya dari konfigurasi atau proses Discovery OP yang telah diverifikasi, serta tangani rotasi dan cache kunci. `kid` digunakan untuk memilih kunci dalam kumpulan tepercaya itu; jangan mengambil kunci dari sembarang URL yang disediakan token.

#### Contoh sebagian proses validasi dalam Python

Fungsi PyJWT berikut mendukung konfigurasi terbatas: **RS256, tanpa enkripsi, satu penerima dalam bentuk string, dan nonce yang sudah dikirim dalam permintaan**. Pemanggil menyediakan `signing_key`, yaitu kunci publik dari JWKS OP yang dipercaya. Klaim wajib harus ada dan nilainya harus valid. Jika ada `azp`, konfigurasi ini mewajibkan nilainya sama dengan `client_id`.

Fungsi ini tidak menyelesaikan proses login. Pemanggil harus memvalidasi dan mengelola hubungan callback dengan transaksi awal, state, pertukaran kode, penerbit yang diharapkan, serta penggunaan nonce hanya sekali. Beberapa penerima, enkripsi, persyaratan autentikasi tambahan, `max_age`, dan `acr` berada di luar cakupan contoh ini.

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

Fungsi mengembalikan klaim yang telah divalidasi dalam cakupan tersebut. Jangan menyatakan autentikasi berhasil hanya karena tanda tangan valid, atau menautkan akun berdasarkan nama maupun alamat email yang belum diverifikasi.

## 4. Pertimbangan keamanan

### 4.1 state, nonce, PKCE, dan CSRF

Jika memakai `state`, ikat nilai yang sulit ditebak secara aman ke transaksi yang dimulai di peramban. Saat callback, periksa kecocokan nilai, batas waktu, dan status belum digunakan, lalu tandai sebagai sudah digunakan. Kesamaan string saja tidak mencegah semua bentuk [CSRF]({{< relref "post/cross-site-scripting-xss-csrf-security/index.id.md" >}}).

RFC 9700 juga membahas penggunaan perlindungan CSRF dari PKCE setelah dukungan server dipastikan, serta penggunaan nonce OIDC. Perlindungan tersebut tetap memerlukan pengikatan khusus untuk setiap transaksi dan validasi yang benar. `state`, `nonce`, dan PKCE memiliki peran berbeda; nilai konstan atau perbandingan yang dilewati tidak memberi perlindungan yang dimaksud. Jika menggunakan beberapa server otorisasi, diperlukan pula pertahanan terhadap serangan mix-up.

### 4.2 Kedaluwarsa dan token pembaruan

Masa berlaku token akses yang pendek membantu membatasi waktu penggunaan token yang dicuri. Nilai seperti 15 menit merupakan contoh desain, bukan persyaratan universal. Saat memeriksa `exp` dalam JWT bertanda tangan, syarat kedaluwarsanya adalah:

$$
T_{\mathrm{now}}<T_{\mathrm{exp}},\qquad T_{\mathrm{exp}}=T_{\mathrm{iat}}+D_{\mathrm{lifetime}}\ \text{hanya jika ditetapkan demikian}\ T_{\mathrm{now}}<T_{\mathrm{iat}}+D_{\mathrm{lifetime}}
$$

Syarat ini hanya memeriksa kedaluwarsa, bukan membuktikan validitas keseluruhan token atau izin akses. Periksa juga algoritma, kunci, penerbit, penerima, serta bila berlaku, `nbf`, status pencabutan, dan keterikatan dengan permintaan autentikasi. Kelola secara eksplisit toleransi perbedaan jam jika digunakan.

Penerbitan token pembaruan (refresh token) bersifat opsional. Tanpanya, klien mungkin perlu melakukan transaksi otorisasi baru. RFC 9700 mewajibkan pembatasan pengirim (sender constraints) atau rotasi untuk token pembaruan yang diterbitkan kepada klien publik. Pembatasan ini mengikat token secara kriptografis ke klien yang menyajikannya. Mencabut token pembaruan tidak selalu langsung membatalkan token akses yang sudah diterbitkan.

### 4.3 Memilih alur dan implementasi

Untuk aplikasi web, SPA, dan aplikasi native yang melibatkan interaksi pengguna, gunakan kode otorisasi dengan PKCE sebagai titik awal. Pilih konfigurasi yang sesuai dengan jenis klien, penyimpanan token, dukungan penyedia, dan model ancaman. Jangan menerapkan alur yang sama secara seragam untuk tujuan lain, seperti kredensial klien untuk M2M.

## Kesimpulan

Gunakan token akses OAuth 2.0 untuk mengakses sumber daya, dan validasi token ID OIDC sebagai hasil autentikasi yang ditujukan kepada klien. Periksa pengikatan kode dengan PKCE, tanda tangan, klaim wajib, nonce, serta hubungan callback dengan transaksi awal.

## Referensi

- [RFC 6749: OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749.html) (peran, token, dan kredensial klien; lihat RFC 9700 untuk pedoman keamanan yang diperbarui)
- [RFC 7636: PKCE](https://www.rfc-editor.org/rfc/rfc7636.html) (bagian 4, bagian 7.1, dan lampiran B)
- [RFC 9700: praktik keamanan OAuth 2.0](https://www.rfc-editor.org/rfc/rfc9700.html) (bagian 2.1, 2.2.2, dan 2.4)
- [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html) (bagian 2, 3.1.3.7, dan 5.7)
- [RFC 7515: JWS](https://www.rfc-editor.org/rfc/rfc7515.html) (bagian 3.1 dan 5.1)
- [API PyJWT](https://pyjwt.readthedocs.io/en/stable/api.html) (algoritma yang diizinkan, klaim wajib, dan validasi penerima)
