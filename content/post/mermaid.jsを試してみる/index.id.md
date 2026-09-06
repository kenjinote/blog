---
title: "Mencoba mermaid.js"
slug: "mermaid.jsを試してみる"
date: 2024-05-25T02:18:09+09:00
tags: ["mermaid.js"]
draft: false
mermaid: true
image: "img_2.png"
categories: ["AI dan Teknologi"]
---

## Apa itu mermaid.js

mermaid.js adalah pustaka JavaScript yang memungkinkan Anda menulis sintaks khusus berbasis teks (Sintaks Mermaid) untuk menampilkan diagram kompleks secara grafis, seperti diagram alur, grafik, dan diagram Gantt.
Ini juga digunakan di berbagai layanan seperti GitHub, Qiita, dan Notion. Kali ini, kita akan mencoba mengaktifkan penggunaan mermaid.js di hugo.

## Mengaktifkan mermaid.js di hugo

Langkah-langkahnya adalah sebagai berikut:

1. Tambahkan yang berikut ini ke layouts/partials/extend_footer.html.

```html
{{ if or .Params.mermaid .Site.Params.mermaid }}
<script src="https://cdn.jsdelivr.net/npm/mermaid@10.3.0/dist/mermaid.min.js"></script>
{{- $loadmermaid := resources.Get "js/load-mermaid.js" }}
<script src="{{ $loadmermaid.RelPermalink }}"></script>
<script>
    window.initMermaid();
    if (isDarkTheme()) {
        setPrefTheme('dark');
    } else {
        setPrefTheme('light');
    }
</script>
{{ end }}
```
※ `mermaid.min.js` hanya dimuat jika `mermaid: true` pada pernyataan if. Pustaka ini cukup besar, sekitar 3MB.

3. Buat assets/js/load-mermaid.js. Proses ini digunakan untuk inisialisasi dan menggambar ulang saat tema dialihkan secara dinamis.

```javascript
(function(window){
'use strict'

  const elementCode = '.mermaid'
  const loadMermaid = function(theme) {
    window.mermaid.initialize({theme})
    window.mermaid.init({theme}, document.querySelectorAll(elementCode))
  }
  const saveOriginalData = function(){
    return new Promise((resolve, reject) => {
      try {
        var els = document.querySelectorAll(elementCode),
            count = els.length;
        els.forEach(element => {
          element.setAttribute('data-original-code', element.innerHTML)
          count--
          if(count == 0){
            resolve()
          }
        });
      } catch (error) {
       reject(error) 
      }
    })
  }
  const resetProcessed = function(){
    return new Promise((resolve, reject) => {
      try {
        var els = document.querySelectorAll(elementCode),
            count = els.length;
        els.forEach(element => {
          if(element.getAttribute('data-original-code') != null){
            element.removeAttribute('data-processed')
            element.innerHTML = element.getAttribute('data-original-code')
          }
          count--
          if(count == 0){
            resolve()
          }
        });
      } catch (error) {
       reject(error) 
      }
    })
  } 

  const init = ()=>{
    saveOriginalData()
    .catch( console.error )
    document.body.addEventListener('dark-theme-set', ()=>{
      resetProcessed()
      .then(loadMermaid('dark'))
      .catch(console.error)
    })
    document.body.addEventListener('light-theme-set', ()=>{
      resetProcessed()
      .then(loadMermaid('default'))
      .catch(console.error)
    })
  }
  window.initMermaid = init
})(window);
```
Kode asli didasarkan pada yang berikut ini:
- [Reinitialize with new theme #1945](https://github.com/mermaid-js/mermaid/issues/1945)

3. Ubah proses pengalihan tema di header.html

```javascript
function switchTheme(theme) {
  switch (theme) {
    case 'light':
{{ if or .Params.mermaid .Site.Params.mermaid }}
      document.body.dispatchEvent(new CustomEvent('light-theme-set'));
{{ end }}
      document.body.classList.remove('dark');
      break;
    case 'dark':
{{ if or .Params.mermaid .Site.Params.mermaid }}
      document.body.dispatchEvent(new CustomEvent('dark-theme-set'));
{{ end }}
      document.body.classList.add('dark');
      break;
    // auto
    default:
      if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
{{ if or .Params.mermaid .Site.Params.mermaid }}
        document.body.dispatchEvent(new CustomEvent('dark-theme-set'));
{{ end }}
        document.body.classList.add('dark');
      }
  }
}
```

4. Buat layouts/shortcodes/mermaid.html

```html
<div class="mermaid" align="{{ if .Get "align" }}{{ .Get "align" }}{{ else }}center{{ end }}">
  {{ safeHTML .Inner }}
</div>
```

Sekarang mermaid.js siap digunakan.

## Menggunakan mermaid.js

1. Tambahkan yang berikut ini ke definisi artikel

```dtd
marmaid: true
```

2. Tambahkan yang berikut ini ke isi artikel

 **Diagram Alur** 

```markdown
{{</*mermaid align="center"*/>}}
graph TD
    A[Mulai] -->|Kondisi 1| B(Kondisi 2)
    B --> C{Kondisi 3}
    C -->|Kondisi 4| D[Selesai]
{{</*/mermaid*/>}}
```

 **Hasil** 

{{<mermaid align="center">}}
graph TD
    A[Mulai] -->|Kondisi 1| B(Kondisi 2)
    B --> C{Kondisi 3}
    C -->|Kondisi 4| D[Selesai]
{{</mermaid>}}

 **Diagram Gantt** 

```markdown
{{</*mermaid align="center"*/>}}
gantt
    section Project
    Definisi Persyaratan :done,      a, 2024-05-25, 5d
    Desain Dasar :done,      b, after a,    5d
    Desain Detail :done,      c, after b,    5d
    Pembuatan    :active,    d, after c,    10d
    Pengujian Unit :crit,      e, after d,    5d
    Pengujian Integrasi :           f, after e,    5d
    Pengujian Sistem :           g, after f,    5d
    Rilis :milestone, h, after g,    1d
{{</*/mermaid*/>}}
```

 **Hasil** 

{{<mermaid align="center">}}
gantt
    section Project
    Definisi Persyaratan :done,      a, 2024-05-25, 5d
    Desain Dasar :done,      b, after a,    5d
    Desain Detail :done,      c, after b,    5d
    Pembuatan    :active,    d, after c,    10d
    Pengujian Unit :crit,      e, after d,    5d
    Pengujian Integrasi :           f, after e,    5d
    Pengujian Sistem :           g, after f,    5d
    Rilis :milestone, h, after g,    1d
{{</mermaid>}}


 **Diagram Urutan** 

```markdown
{{</*mermaid align="center"*/>}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: Masukkan ID/PW
    view->>controller: Permintaan Autentikasi
    controller->>model: Permintaan Autentikasi
    model->>database: Permintaan Autentikasi
    database-->>model: Kembalikan Hasil
    model-->>controller: Kembalikan Hasil
    controller-->>view: Kembalikan Hasil
    view-->>user: Tampilkan Hasil
{{</*/mermaid*/>}}
``` 

 **Hasil** 

{{<mermaid align="center">}}
sequenceDiagram
    participant user
    participant view
    participant controller
    participant model
    participant database
    user->>view: Masukkan ID/PW
    view->>controller: Kueri ajax
    controller->>model: Permintaan Autentikasi
    model->>database: Terbitkan SQL
    database-->>model: Kembalikan Hasil SQL
    model-->>controller: Kembalikan Hasil Permintaan Autentikasi
    controller-->>view: Kembalikan Hasil Kueri ajax
    view-->>user: Tampilkan Hasil Autentikasi
{{</mermaid>}}

Itu saja.

### Referensi
- [Situs resmi mermaid.js](https://mermaid.js.org/#/)
- [Situs demo untuk pratinjau sintaks mermaid](https://mermaid.live/)
