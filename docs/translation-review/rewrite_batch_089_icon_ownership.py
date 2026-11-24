"""Clarify icon-handle ownership guidance and localize it across all editions."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/LoadIconはDestroyIconを呼び出す必要はない"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")

DESCRIPTIONS = {
"ja": "Windows APIのアイコンハンドルは、共有リソースか呼び出し側所有かでDestroyIconの要否が変わります。LoadIcon、LoadImage、CopyIconの解放条件と、Microsoft公式資料で仕様の説明が食い違うAPIを整理します。",
"en": "Whether an icon handle needs DestroyIcon depends on whether the resource is shared or caller-owned. This guide explains LoadIcon, LoadImage, and CopyIcon ownership, and notes conflicting Microsoft documentation for resource-creation APIs.",
"es": "La necesidad de llamar a DestroyIcon depende de si el recurso del identificador es compartido o pertenece al llamador. Esta guía explica la propiedad de LoadIcon, LoadImage y CopyIcon, y señala discrepancias en la documentación de Microsoft sobre algunas API.",
"fr": "La nécessité d’appeler DestroyIcon dépend du caractère partagé de la ressource ou de son appartenance à l’appelant. Ce guide explique la propriété des handles de LoadIcon, LoadImage et CopyIcon et signale une divergence dans la documentation Microsoft de certaines API.",
"de": "Ob DestroyIcon erforderlich ist, hängt davon ab, ob das Handle auf eine gemeinsam genutzte oder vom Aufrufer verwaltete Ressource verweist. Diese Anleitung erläutert LoadIcon, LoadImage und CopyIcon sowie widersprüchliche Microsoft-Dokumentation zu einigen Erstellungs-APIs.",
"ar": "يعتمد استدعاء DestroyIcon على ما إذا كان مقبض الأيقونة يشير إلى مورد مشترك أم مورد يملكه المستدعي. يشرح هذا الدليل ملكية الموارد في LoadIcon وLoadImage وCopyIcon، وينبه إلى تعارض في وثائق Microsoft لبعض واجهات إنشاء الموارد.",
"hi": "DestroyIcon की आवश्यकता इस पर निर्भर करती है कि आइकन हैंडल साझा संसाधन का है या कॉलर के स्वामित्व वाला है। यह गाइड LoadIcon, LoadImage और CopyIcon के स्वामित्व नियम समझाती है और कुछ API पर Microsoft दस्तावेज़ों के विरोधाभास को बताती है।",
"id": "Perlu tidaknya memanggil DestroyIcon bergantung pada apakah handle ikon menunjuk ke sumber daya bersama atau milik pemanggil. Panduan ini menjelaskan kepemilikan pada LoadIcon, LoadImage, dan CopyIcon, serta mencatat pertentangan dalam dokumentasi Microsoft untuk beberapa API pembuatan ikon.",
"ko": "DestroyIcon 호출 여부는 아이콘 핸들이 공유 리소스인지 호출자 소유 리소스인지에 따라 달라집니다. 이 문서에서는 LoadIcon, LoadImage, CopyIcon의 소유권 규칙과 일부 생성 API에 관한 Microsoft 문서의 상충 내용을 설명합니다.",
"pt": "A necessidade de chamar DestroyIcon depende de o identificador apontar para um recurso compartilhado ou pertencente ao chamador. Este guia explica a propriedade em LoadIcon, LoadImage e CopyIcon e aponta divergências na documentação da Microsoft sobre algumas APIs de criação.",
"ru": "Необходимость вызова DestroyIcon зависит от того, является ли ресурс общим или принадлежит вызывающему коду. В руководстве описано владение для LoadIcon, LoadImage и CopyIcon, а также отмечено противоречие в документации Microsoft для некоторых API создания значков.",
"zh-cn": "是否需要调用 DestroyIcon，取决于图标句柄指向的是共享资源还是由调用方拥有的资源。本指南说明 LoadIcon、LoadImage 和 CopyIcon 的所有权规则，并指出 Microsoft 对部分创建 API 的文档存在矛盾。",
"zh-tw": "是否需要呼叫 DestroyIcon，取決於圖示控制代碼指向的是共用資源，還是由呼叫端擁有的資源。本指南說明 LoadIcon、LoadImage 與 CopyIcon 的所有權規則，並指出 Microsoft 對部分建立 API 的文件存在矛盾。",
}

BODIES = {
"ja": """# アイコンハンドルの所有権

`DestroyIcon`を呼び出すかどうかは、アイコンが共有リソースか、呼び出し側が解放責任を持つリソースかで決まります。共有アイコンを破棄すると、同じリソースを使う別の処理に影響します。

## DestroyIconを呼ばないケース

- `LoadIcon`が返すアイコンは共有リソースです。`DestroyIcon`で破棄してはいけません。`LoadIcon`は現在のサイズの標準メトリックに合うアイコンを読み込み、サイズを指定したい場合は`LoadImage`が推奨されています。
- `LoadImage`に`LR_SHARED`を指定すると、ハンドルは共有されます。`DestroyIcon`を呼ばないでください。`LR_SHARED`は、ファイルから読み込む画像や標準外サイズの画像には使えません。
- `CopyImage`に`LR_COPYRETURNORG`を指定し、元の`hImage`が共有アイコンの場合、元のハンドルが返ることがあります。その場合も破棄してはいけません。

## DestroyIconを呼ぶケース

呼び出し側が所有するアイコンは、使用を終えたら`DestroyIcon`で解放します。Microsoftは次の例を挙げています。

- `CreateIconFromResourceEx`（`LR_SHARED`なし）
- `CreateIconIndirect`
- `CopyIcon`（複製アイコンのハンドルを返します）
- `LoadImage`でアイコンを読み込み、`LR_SHARED`を指定しない場合

## CreateIconFromResourceの注意点

Microsoftの一般的な`DestroyIcon`資料は`CreateIconFromResource`を共有アイコンの取得元として記載していますが、各関数の個別資料は`DestroyIcon`を呼ぶよう説明しています。`CreateIconFromResource`と`CreateIconFromResourceEx`の資料内にも、`LR_SHARED`の説明と解放指示の食い違いがあります。これらのAPIでは一般論だけで判断せず、対象関数の最新資料を確認してください。この矛盾は`LoadIcon`の共有ハンドルの説明とは分けて考えます。

`DestroyIcon`に渡すアイコンは使用中であってはなりません。共有ハンドルかどうか、またモジュールの有効期間も確認してください。

## 参考資料

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
""",
"en": """# Icon-handle ownership

Whether to call `DestroyIcon` depends on whether the icon is a shared resource or a resource that the caller owns and must release. Destroying a shared icon can affect other code that uses the same resource.

## When not to call DestroyIcon

- An icon returned by `LoadIcon` is shared. Do not destroy it with `DestroyIcon`. `LoadIcon` loads an icon at the standard system metric size; use `LoadImage` when you need to specify a size.
- When you pass `LR_SHARED` to `LoadImage`, the handle is shared. Do not call `DestroyIcon`. Do not use `LR_SHARED` for images loaded from files or for nonstandard sizes.
- `CopyImage` can return the original handle when you pass `LR_COPYRETURNORG` and the input `hImage` is a shared icon. Do not destroy that shared handle.

## When to call DestroyIcon

Release caller-owned icons with `DestroyIcon` when you are finished using them. Microsoft gives these examples:

- `CreateIconFromResourceEx` without `LR_SHARED`
- `CreateIconIndirect`
- `CopyIcon`, which returns a duplicate icon handle
- An icon loaded with `LoadImage` without `LR_SHARED`

## A note about CreateIconFromResource

Microsoft's general `DestroyIcon` page lists `CreateIconFromResource` as a source of shared icons, while the individual function pages say to call `DestroyIcon`. The `CreateIconFromResource` and `CreateIconFromResourceEx` pages also conflict internally about `LR_SHARED` and releasing the returned handle. Do not infer ownership for these APIs from the general rule alone; consult the current page for the specific function. This documentation conflict is separate from the shared-handle behavior of `LoadIcon`.

An icon passed to `DestroyIcon` must not be in use. Check whether a handle is shared and whether its source module is still loaded.

## References

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
""",
"es": """# Propiedad del identificador de icono

La decisión de llamar a `DestroyIcon` depende de si el icono es un recurso compartido o uno que pertenece al programa y debe liberarse. Destruir un icono compartido puede afectar a otro código que utilice el mismo recurso.

## Cuándo no llamar a DestroyIcon

- El icono devuelto por `LoadIcon` es compartido. No lo destruyas con `DestroyIcon`. `LoadIcon` carga el icono con el tamaño métrico estándar; usa `LoadImage` si necesitas especificar otro tamaño.
- Si pasas `LR_SHARED` a `LoadImage`, el identificador es compartido. No llames a `DestroyIcon`. No uses `LR_SHARED` para imágenes cargadas desde archivos ni para tamaños no estándar.
- `CopyImage` puede devolver el identificador original si pasas `LR_COPYRETURNORG` y el `hImage` de entrada es un icono compartido. No destruyas ese identificador.

## Cuándo llamar a DestroyIcon

Libera con `DestroyIcon` los iconos que pertenecen al programa cuando termines de usarlos. Microsoft ofrece estos ejemplos:

- `CreateIconFromResourceEx` sin `LR_SHARED`
- `CreateIconIndirect`
- `CopyIcon`, que devuelve un identificador de icono duplicado
- Un icono cargado con `LoadImage` sin `LR_SHARED`

## Nota sobre CreateIconFromResource

La página general de `DestroyIcon` de Microsoft incluye `CreateIconFromResource` entre las fuentes de iconos compartidos, pero las páginas específicas de esas funciones indican que se debe llamar a `DestroyIcon`. Además, las páginas de `CreateIconFromResource` y `CreateIconFromResourceEx` se contradicen internamente sobre `LR_SHARED` y la liberación del identificador devuelto. No deduzcas la propiedad de estas API solo a partir de la regla general: consulta la documentación actual de cada función. Esta discrepancia es distinta del comportamiento de los identificadores compartidos de `LoadIcon`.

El icono que se pasa a `DestroyIcon` no debe estar en uso. Comprueba si el identificador es compartido y si el módulo de origen sigue cargado.

## Referencias

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
""",
"fr": """# Propriété du handle d’icône

L’appel à `DestroyIcon` dépend du fait que l’icône soit une ressource partagée ou une ressource appartenant à l’appelant, qui doit la libérer. Détruire une icône partagée peut affecter d’autres parties du programme qui utilisent la même ressource.

## Quand ne pas appeler DestroyIcon

- L’icône renvoyée par `LoadIcon` est partagée. Ne la détruisez pas avec `DestroyIcon`. `LoadIcon` charge une icône à la taille métrique standard ; utilisez `LoadImage` si vous devez préciser une taille.
- Si vous transmettez `LR_SHARED` à `LoadImage`, le handle est partagé. N’appelez pas `DestroyIcon`. N’utilisez pas `LR_SHARED` pour les images chargées depuis un fichier ou de taille non standard.
- `CopyImage` peut renvoyer le handle d’origine si vous transmettez `LR_COPYRETURNORG` et que le `hImage` fourni est une icône partagée. Ne détruisez pas ce handle.

## Quand appeler DestroyIcon

Libérez avec `DestroyIcon` les icônes appartenant à l’appelant lorsque vous avez fini de les utiliser. Microsoft donne les exemples suivants :

- `CreateIconFromResourceEx` sans `LR_SHARED`
- `CreateIconIndirect`
- `CopyIcon`, qui renvoie un handle d’icône dupliqué
- Une icône chargée avec `LoadImage` sans `LR_SHARED`

## Remarque sur CreateIconFromResource

La page générale Microsoft de `DestroyIcon` cite `CreateIconFromResource` parmi les fonctions qui obtiennent une icône partagée, alors que les pages individuelles indiquent qu’il faut appeler `DestroyIcon`. Les pages de `CreateIconFromResource` et `CreateIconFromResourceEx` se contredisent aussi sur `LR_SHARED` et la libération du handle renvoyé. Pour ces API, ne déduisez pas la propriété de la seule règle générale : consultez la documentation actuelle de chaque fonction. Cette divergence est distincte du comportement des handles partagés de `LoadIcon`.

L’icône transmise à `DestroyIcon` ne doit pas être utilisée. Vérifiez si le handle est partagé et si le module source est toujours chargé.

## Références

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
""",
"de": """# Besitz von Icon-Handles

Ob `DestroyIcon` aufgerufen werden muss, hängt davon ab, ob das Icon gemeinsam genutzt wird oder dem Aufrufer gehört und von ihm freigegeben werden muss. Das Zerstören eines gemeinsam genutzten Icons kann andere Codeabschnitte beeinträchtigen, die dieselbe Ressource verwenden.

## Wann DestroyIcon nicht aufgerufen wird

- Ein von `LoadIcon` zurückgegebenes Icon wird gemeinsam genutzt. Rufen Sie dafür nicht `DestroyIcon` auf. `LoadIcon` lädt ein Icon in der Standardgröße der Systemmetriken; für eine bestimmte Größe verwenden Sie `LoadImage`.
- Wird `LR_SHARED` an `LoadImage` übergeben, ist das Handle gemeinsam genutzt. Rufen Sie `DestroyIcon` nicht auf. Verwenden Sie `LR_SHARED` nicht für Bilder aus Dateien oder für nicht standardmäßige Größen.
- `CopyImage` kann das ursprüngliche Handle zurückgeben, wenn `LR_COPYRETURNORG` gesetzt und das Eingabe-`hImage` ein gemeinsam genutztes Icon ist. Zerstören Sie dieses Handle nicht.

## Wann DestroyIcon aufgerufen wird

Geben Sie Icons, die dem Aufrufer gehören, nach der Verwendung mit `DestroyIcon` frei. Microsoft nennt folgende Beispiele:

- `CreateIconFromResourceEx` ohne `LR_SHARED`
- `CreateIconIndirect`
- `CopyIcon`, das ein dupliziertes Icon-Handle zurückgibt
- Ein mit `LoadImage` ohne `LR_SHARED` geladenes Icon

## Hinweis zu CreateIconFromResource

Die allgemeine Microsoft-Dokumentation zu `DestroyIcon` führt `CreateIconFromResource` als Quelle gemeinsam genutzter Icons auf; die einzelnen Funktionsseiten sagen dagegen, dass `DestroyIcon` aufgerufen werden soll. Auch die Seiten zu `CreateIconFromResource` und `CreateIconFromResourceEx` widersprechen sich intern bezüglich `LR_SHARED` und der Freigabe des zurückgegebenen Handles. Leiten Sie die Besitzverhältnisse bei diesen APIs nicht allein aus der allgemeinen Regel ab, sondern prüfen Sie die aktuelle Dokumentation der jeweiligen Funktion. Dieser Widerspruch ist unabhängig vom Verhalten gemeinsam genutzter `LoadIcon`-Handles.

Ein an `DestroyIcon` übergebenes Icon darf nicht verwendet werden. Prüfen Sie, ob das Handle gemeinsam genutzt wird und ob sein Quellmodul noch geladen ist.

## Quellen

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
""",
"id": """# Kepemilikan handle ikon

Perlu tidaknya memanggil `DestroyIcon` bergantung pada apakah ikon merupakan sumber daya bersama atau dimiliki pemanggil dan harus dilepaskan olehnya. Menghancurkan ikon bersama dapat memengaruhi bagian program lain yang memakai sumber daya yang sama.

## Kapan tidak memanggil DestroyIcon

- Ikon yang dikembalikan oleh `LoadIcon` adalah sumber daya bersama. Jangan menghancurkannya dengan `DestroyIcon`. `LoadIcon` memuat ikon pada ukuran metrik sistem standar; gunakan `LoadImage` jika perlu menentukan ukuran.
- Jika `LR_SHARED` diberikan ke `LoadImage`, handle-nya digunakan bersama. Jangan panggil `DestroyIcon`. Jangan gunakan `LR_SHARED` untuk gambar dari file atau ukuran nonstandar.
- `CopyImage` dapat mengembalikan handle asli jika `LR_COPYRETURNORG` digunakan dan `hImage` masukan adalah ikon bersama. Jangan hancurkan handle tersebut.

## Kapan memanggil DestroyIcon

Lepaskan ikon milik pemanggil dengan `DestroyIcon` setelah selesai digunakan. Microsoft memberikan contoh berikut:

- `CreateIconFromResourceEx` tanpa `LR_SHARED`
- `CreateIconIndirect`
- `CopyIcon`, yang mengembalikan handle ikon duplikat
- Ikon yang dimuat dengan `LoadImage` tanpa `LR_SHARED`

## Catatan tentang CreateIconFromResource

Halaman umum Microsoft untuk `DestroyIcon` mencantumkan `CreateIconFromResource` sebagai sumber ikon bersama, tetapi halaman fungsi tersebut menyarankan untuk memanggil `DestroyIcon`. Halaman `CreateIconFromResource` dan `CreateIconFromResourceEx` juga memiliki penjelasan internal yang bertentangan tentang `LR_SHARED` dan pelepasan handle hasil. Jangan menyimpulkan kepemilikan API ini hanya dari aturan umum; periksa dokumentasi terbaru untuk fungsi tertentu. Pertentangan dokumentasi ini berbeda dari perilaku handle bersama `LoadIcon`.

Ikon yang diberikan ke `DestroyIcon` tidak boleh sedang digunakan. Pastikan apakah handle digunakan bersama dan apakah modul sumbernya masih dimuat.

## Referensi

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
""",
"ko": """# 아이콘 핸들의 소유권

`DestroyIcon` 호출 여부는 아이콘이 공유 리소스인지 호출자가 소유하고 직접 해제해야 하는 리소스인지에 따라 달라집니다. 공유 아이콘을 파괴하면 같은 리소스를 사용하는 다른 코드에 영향을 줄 수 있습니다.

## DestroyIcon을 호출하지 않는 경우

- `LoadIcon`이 반환하는 아이콘은 공유됩니다. `DestroyIcon`으로 파괴하지 마세요. `LoadIcon`은 시스템 메트릭의 표준 크기를 사용하며, 크기를 지정하려면 `LoadImage`를 사용합니다.
- `LoadImage`에 `LR_SHARED`를 지정하면 핸들이 공유됩니다. `DestroyIcon`을 호출하지 마세요. 파일에서 읽은 이미지나 표준 크기가 아닌 이미지에는 `LR_SHARED`를 사용하지 마세요.
- `LR_COPYRETURNORG`를 지정하고 입력 `hImage`가 공유 아이콘이면 `CopyImage`가 원래 핸들을 반환할 수 있습니다. 이 핸들도 파괴하면 안 됩니다.

## DestroyIcon을 호출하는 경우

호출자가 소유한 아이콘은 사용이 끝난 뒤 `DestroyIcon`으로 해제합니다. Microsoft는 다음을 예로 듭니다.

- `LR_SHARED` 없이 호출한 `CreateIconFromResourceEx`
- `CreateIconIndirect`
- 복제 아이콘 핸들을 반환하는 `CopyIcon`
- `LR_SHARED` 없이 아이콘을 읽은 `LoadImage`

## CreateIconFromResource 관련 참고

Microsoft의 일반 `DestroyIcon` 문서에는 `CreateIconFromResource`가 공유 아이콘을 얻는 함수로 나와 있지만, 각 함수의 개별 문서는 `DestroyIcon`을 호출하라고 설명합니다. `CreateIconFromResource`와 `CreateIconFromResourceEx` 문서 안에서도 `LR_SHARED`와 반환 핸들 해제에 대한 설명이 서로 충돌합니다. 이 API의 소유권을 일반 규칙만으로 추측하지 말고 각 함수의 최신 문서를 확인하세요. 이 문서 간 충돌은 `LoadIcon` 공유 핸들의 동작과는 별개입니다.

`DestroyIcon`에 전달하는 아이콘은 사용 중이면 안 됩니다. 핸들이 공유인지, 원본 모듈이 아직 로드되어 있는지 확인하세요.

## 참고 자료

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
""",
"pt": """# Propriedade do identificador do ícone

A necessidade de chamar `DestroyIcon` depende de o ícone ser um recurso compartilhado ou pertencer ao chamador, que é responsável por liberá-lo. Destruir um ícone compartilhado pode afetar outro código que usa o mesmo recurso.

## Quando não chamar DestroyIcon

- O ícone retornado por `LoadIcon` é compartilhado. Não o destrua com `DestroyIcon`. `LoadIcon` carrega o ícone no tamanho padrão das métricas do sistema; use `LoadImage` quando precisar especificar um tamanho.
- Ao passar `LR_SHARED` para `LoadImage`, o identificador é compartilhado. Não chame `DestroyIcon`. Não use `LR_SHARED` para imagens carregadas de arquivos ou com tamanhos não padrão.
- `CopyImage` pode retornar o identificador original quando `LR_COPYRETURNORG` é usado e o `hImage` de entrada é um ícone compartilhado. Não destrua esse identificador.

## Quando chamar DestroyIcon

Libere com `DestroyIcon` os ícones que pertencem ao chamador quando terminar de usá-los. A Microsoft cita estes exemplos:

- `CreateIconFromResourceEx` sem `LR_SHARED`
- `CreateIconIndirect`
- `CopyIcon`, que retorna um identificador de ícone duplicado
- Um ícone carregado por `LoadImage` sem `LR_SHARED`

## Observação sobre CreateIconFromResource

A página geral da Microsoft para `DestroyIcon` lista `CreateIconFromResource` como origem de ícones compartilhados, mas as páginas específicas dessas funções dizem para chamar `DestroyIcon`. As páginas de `CreateIconFromResource` e `CreateIconFromResourceEx` também se contradizem internamente sobre `LR_SHARED` e a liberação do identificador retornado. Não deduza a propriedade dessas APIs apenas pela regra geral; consulte a página atual de cada função. Essa divergência documental é diferente do comportamento dos identificadores compartilhados de `LoadIcon`.

O ícone passado para `DestroyIcon` não pode estar em uso. Verifique se o identificador é compartilhado e se o módulo de origem ainda está carregado.

## Referências

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
""",
"ru": """# Владение дескриптором значка

Нужно ли вызывать `DestroyIcon`, зависит от того, является ли значок общим ресурсом или принадлежит вызывающему коду и должен быть освобожден им. Уничтожение общего значка может повлиять на другой код, использующий тот же ресурс.

## Когда не следует вызывать DestroyIcon

- Значок, возвращенный `LoadIcon`, является общим. Не уничтожайте его с помощью `DestroyIcon`. `LoadIcon` загружает значок стандартного системного размера; если нужно задать размер, используйте `LoadImage`.
- Если передать `LR_SHARED` в `LoadImage`, дескриптор будет общим. Не вызывайте `DestroyIcon`. Не используйте `LR_SHARED` для изображений из файлов или нестандартного размера.
- `CopyImage` может вернуть исходный дескриптор, если указан `LR_COPYRETURNORG`, а входной `hImage` — общий значок. Такой дескриптор также нельзя уничтожать.

## Когда нужно вызывать DestroyIcon

После использования освободите принадлежащие вызывающему коду значки с помощью `DestroyIcon`. Microsoft приводит такие примеры:

- `CreateIconFromResourceEx` без `LR_SHARED`
- `CreateIconIndirect`
- `CopyIcon`, возвращающий дескриптор копии значка
- Значок, загруженный через `LoadImage` без `LR_SHARED`

## Примечание о CreateIconFromResource

В общей документации Microsoft для `DestroyIcon` функция `CreateIconFromResource` указана как источник общих значков, но страницы отдельных функций советуют вызывать `DestroyIcon`. Страницы `CreateIconFromResource` и `CreateIconFromResourceEx` также содержат внутренние противоречия об использовании `LR_SHARED` и освобождении возвращенного дескриптора. Для этих API не определяйте владение только по общему правилу; проверяйте актуальную документацию конкретной функции. Это противоречие не относится к поведению общих дескрипторов `LoadIcon`.

Значок, передаваемый в `DestroyIcon`, не должен использоваться. Проверьте, является ли дескриптор общим и загружен ли еще исходный модуль.

## Ссылки

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
""",
"zh-cn": """# 图标句柄的所有权

是否调用 `DestroyIcon`，取决于图标属于共享资源，还是由调用方拥有并负责释放。销毁共享图标可能影响使用同一资源的其他代码。

## 不要调用 DestroyIcon 的情况

- `LoadIcon` 返回的图标是共享资源。不要用 `DestroyIcon` 销毁它。`LoadIcon` 加载系统标准指标尺寸的图标；需要指定尺寸时请使用 `LoadImage`。
- 向 `LoadImage` 传入 `LR_SHARED` 时，句柄是共享的。不要调用 `DestroyIcon`。文件加载的图像或非标准尺寸图像不要使用 `LR_SHARED`。
- 如果指定 `LR_COPYRETURNORG`，且输入的 `hImage` 是共享图标，`CopyImage` 可能返回原始句柄。不要销毁该句柄。

## 需要调用 DestroyIcon 的情况

调用方拥有的图标在使用完毕后应通过 `DestroyIcon` 释放。Microsoft 给出的示例包括：

- 未指定 `LR_SHARED` 的 `CreateIconFromResourceEx`
- `CreateIconIndirect`
- 返回图标副本句柄的 `CopyIcon`
- 未指定 `LR_SHARED` 时由 `LoadImage` 加载的图标

## 关于 CreateIconFromResource 的说明

Microsoft 的 `DestroyIcon` 通用文档将 `CreateIconFromResource` 列为获取共享图标的来源，但各函数的单独文档又建议调用 `DestroyIcon`。`CreateIconFromResource` 和 `CreateIconFromResourceEx` 的页面对 `LR_SHARED` 与返回句柄释放方式也有内部矛盾。不要仅凭通用规则推断这些 API 的所有权，应查看具体函数的最新文档。此处的文档冲突与 `LoadIcon` 共享句柄的行为不同。

传给 `DestroyIcon` 的图标不能处于使用状态。还要确认句柄是否共享，以及来源模块是否仍处于加载状态。

## 参考资料

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
""",
"zh-tw": """# 圖示控制代碼的所有權

是否呼叫 `DestroyIcon`，取決於圖示屬於共用資源，還是由呼叫端擁有並負責釋放。銷毀共用圖示可能影響使用相同資源的其他程式碼。

## 不要呼叫 DestroyIcon 的情況

- `LoadIcon` 回傳的圖示是共用資源。不要用 `DestroyIcon` 銷毀它。`LoadIcon` 會載入系統標準度量尺寸的圖示；需要指定尺寸時請使用 `LoadImage`。
- 向 `LoadImage` 傳入 `LR_SHARED` 時，控制代碼是共用的。不要呼叫 `DestroyIcon`。從檔案載入的影像或非標準尺寸影像不要使用 `LR_SHARED`。
- 若指定 `LR_COPYRETURNORG`，且輸入的 `hImage` 是共用圖示，`CopyImage` 可能回傳原始控制代碼。不要銷毀該控制代碼。

## 需要呼叫 DestroyIcon 的情況

呼叫端擁有的圖示在使用完畢後應透過 `DestroyIcon` 釋放。Microsoft 提供的例子包括：

- 未指定 `LR_SHARED` 的 `CreateIconFromResourceEx`
- `CreateIconIndirect`
- 回傳圖示副本控制代碼的 `CopyIcon`
- 未指定 `LR_SHARED` 時由 `LoadImage` 載入的圖示

## 關於 CreateIconFromResource 的說明

Microsoft 的 `DestroyIcon` 一般文件將 `CreateIconFromResource` 列為取得共用圖示的來源，但各函式的個別文件又建議呼叫 `DestroyIcon`。`CreateIconFromResource` 與 `CreateIconFromResourceEx` 的頁面對 `LR_SHARED` 和回傳控制代碼的釋放方式也有內部矛盾。請勿只依一般規則推斷這些 API 的所有權，應查閱各函式的最新文件。此處的文件衝突與 `LoadIcon` 共用控制代碼的行為不同。

傳給 `DestroyIcon` 的圖示不可處於使用中。也請確認控制代碼是否共用，以及來源模組是否仍在載入中。

## 參考資料

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
""",
"hi": """# आइकन हैंडल का स्वामित्व

`DestroyIcon` कॉल करना है या नहीं, यह इस पर निर्भर करता है कि आइकन साझा संसाधन है या कॉलर के स्वामित्व में है और उसे कॉलर को मुक्त करना है। साझा आइकन को नष्ट करने से उसी संसाधन का उपयोग करने वाला अन्य कोड प्रभावित हो सकता है।

## DestroyIcon कब न करें

- `LoadIcon` से मिला आइकन साझा होता है। उसे `DestroyIcon` से नष्ट न करें। `LoadIcon` सिस्टम के मानक आकार वाला आइकन लोड करता है; आकार निर्दिष्ट करना हो तो `LoadImage` उपयोग करें।
- `LoadImage` को `LR_SHARED` देने पर हैंडल साझा होता है। `DestroyIcon` न बुलाएँ। फ़ाइल से लोड की गई या गैर-मानक आकार की छवियों के लिए `LR_SHARED` न इस्तेमाल करें।
- यदि `LR_COPYRETURNORG` दिया गया है और इनपुट `hImage` साझा आइकन है, तो `CopyImage` मूल हैंडल लौटा सकता है। उस हैंडल को नष्ट न करें।

## DestroyIcon कब करें

कॉलर के स्वामित्व वाले आइकन का उपयोग पूरा होने पर `DestroyIcon` से उसे मुक्त करें। Microsoft ये उदाहरण देता है:

- `LR_SHARED` के बिना `CreateIconFromResourceEx`
- `CreateIconIndirect`
- `CopyIcon`, जो डुप्लिकेट आइकन हैंडल लौटाता है
- `LR_SHARED` के बिना `LoadImage` से लोड किया गया आइकन

## CreateIconFromResource के बारे में सावधानी

Microsoft का सामान्य `DestroyIcon` पृष्ठ `CreateIconFromResource` को साझा आइकन पाने वाले फ़ंक्शन में गिनता है, जबकि अलग-अलग फ़ंक्शन पृष्ठ `DestroyIcon` कॉल करने को कहते हैं। `CreateIconFromResource` और `CreateIconFromResourceEx` पृष्ठों में भी `LR_SHARED` और लौटाए गए हैंडल को मुक्त करने की बात पर आपसी विरोध है। इन API के स्वामित्व का अनुमान केवल सामान्य नियम से न लगाएँ; संबंधित फ़ंक्शन का वर्तमान दस्तावेज़ देखें। यह दस्तावेज़ी विरोध `LoadIcon` के साझा हैंडल से अलग है।

`DestroyIcon` को दिया गया आइकन उपयोग में नहीं होना चाहिए। यह भी जाँचें कि हैंडल साझा है या नहीं और स्रोत मॉड्यूल अभी लोड है या नहीं।

## संदर्भ

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
""",
"ar": """# ملكية مقبض الأيقونة

يعتمد استدعاء `DestroyIcon` على ما إذا كانت الأيقونة مورداً مشتركاً أم مورداً يملكه المستدعي ويتعين عليه تحريره. قد يؤثر تدمير أيقونة مشتركة في أجزاء أخرى من البرنامج تستخدم المورد نفسه.

## متى لا تستدعي DestroyIcon

- الأيقونة التي يعيدها `LoadIcon` مشتركة. لا تدمرها باستخدام `DestroyIcon`. يحمّل `LoadIcon` الأيقونة بحجم مقاييس النظام القياسي؛ استخدم `LoadImage` إذا أردت تحديد الحجم.
- عند تمرير `LR_SHARED` إلى `LoadImage` يكون المقبض مشتركاً. لا تستدعِ `DestroyIcon`. لا تستخدم `LR_SHARED` للصور المحمّلة من الملفات أو ذات الأحجام غير القياسية.
- قد يعيد `CopyImage` المقبض الأصلي عند تمرير `LR_COPYRETURNORG` إذا كانت قيمة `hImage` المدخلة أيقونة مشتركة. لا تدمر ذلك المقبض.

## متى تستدعي DestroyIcon

حرّر الأيقونات التي يملكها المستدعي باستخدام `DestroyIcon` بعد الانتهاء من استخدامها. تذكر Microsoft الأمثلة التالية:

- `CreateIconFromResourceEx` من دون `LR_SHARED`
- `CreateIconIndirect`
- `CopyIcon` الذي يعيد مقبض نسخة من الأيقونة
- أيقونة حمّلها `LoadImage` من دون `LR_SHARED`

## تنبيه بشأن CreateIconFromResource

تدرج صفحة Microsoft العامة لـ `DestroyIcon` الدالة `CreateIconFromResource` ضمن مصادر الأيقونات المشتركة، لكن صفحات الدوال الفردية توصي باستدعاء `DestroyIcon`. كما تتضمن صفحات `CreateIconFromResource` و`CreateIconFromResourceEx` تعارضاً داخلياً حول `LR_SHARED` وتحرير المقبض الناتج. لا تستنتج الملكية لهذه الواجهات من القاعدة العامة وحدها؛ راجع أحدث وثائق الدالة المحددة. يختلف هذا التعارض عن سلوك المقابض المشتركة لـ `LoadIcon`.

يجب ألا تكون الأيقونة التي تمررها إلى `DestroyIcon` قيد الاستخدام. تحقق مما إذا كان المقبض مشتركاً وما إذا كانت الوحدة المصدر لا تزال محمّلة.

## المراجع

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
""",
}

for language in LANGS:
    suffix = "" if language == "ja" else f".{language}"
    path = BUNDLE / f"index{suffix}.md"
    text = path.read_text(encoding="utf-8-sig")
    text = re.sub(r'(?m)^date: "2026-09-24T19:44:38\+09:00"\n', "", text)
    text = re.sub(r"(?m)^(date: 2024-04-19T01:55:17\+09:00)$", r"\1\nlastmod: 2026-11-24T00:00:00+09:00", text)
    text, count = re.subn(r"(?m)^description:.*$", f"description: '{DESCRIPTIONS[language]}'", text, count=1)
    if count != 1:
        raise SystemExit(f"{language}: description missing")
    text = re.sub(r"\A---\n(?:[ \t]*\n)+", "---\n", text)
    front = text.split("\n---\n", 1)[0]
    text = front + "\n---\n\n" + BODIES[language].rstrip() + "\n"
    path.write_text(text, encoding="utf-8")

print("Clarified icon ownership guidance in thirteen editions")
