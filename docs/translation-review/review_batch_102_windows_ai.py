"""Refresh and audit the Windows AI API article in all published locales."""
from pathlib import Path
import hashlib, json, re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/Microsoft.Windows.AIの最新API活用事例とサンプルコード"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = f"post/{BUNDLE.name}/index.md"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
URLS = {
    "apis":"https://learn.microsoft.com/en-us/windows/ai/apis",
    "start":"https://learn.microsoft.com/en-us/windows/ai/apis/get-started",
    "phi":"https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica",
    "npu":"https://learn.microsoft.com/en-us/windows/ai/npu-devices",
    "dml":"https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started",
}

META = {
"ja":("Windows AI APIの現在地：Phi Silica、Windows ML、DirectMLの選び方","2026年11月時点のMicrosoft公式資料に基づき、Windows AI API、Phi Silicaの利用条件、Windows MLとDirectML、NPU性能値を整理します。"),
"en":("Windows AI APIs today: choosing Phi Silica, Windows ML, and DirectML","A November 2026 guide to Windows AI APIs, Phi Silica availability, Windows ML and DirectML, and how to interpret NPU performance figures, based on Microsoft documentation."),
"de":("Windows-AI-APIs heute: Phi Silica, Windows ML und DirectML auswählen","Leitfaden mit Stand November 2026 zu Windows AI APIs, Phi-Silica-Verfügbarkeit, Windows ML, DirectML und NPU-Leistungswerten auf Grundlage offizieller Microsoft-Dokumentation."),
"es":("Windows AI APIs hoy: elegir Phi Silica, Windows ML y DirectML","Guía de noviembre de 2026 sobre Windows AI APIs, disponibilidad de Phi Silica, Windows ML, DirectML y métricas de rendimiento de NPU basada en documentación oficial de Microsoft."),
"fr":("Windows AI APIs aujourd'hui : choisir Phi Silica, Windows ML et DirectML","Guide de novembre 2026 sur les Windows AI APIs, la disponibilité de Phi Silica, Windows ML, DirectML et les performances des NPU, d'après la documentation Microsoft."),
"hi":("आज के Windows AI APIs: Phi Silica, Windows ML और DirectML का चयन","Microsoft के आधिकारिक दस्तावेज़ों पर आधारित नवंबर 2026 की मार्गदर्शिका: Windows AI APIs, Phi Silica की उपलब्धता, Windows ML, DirectML और NPU प्रदर्शन।"),
"id":("Windows AI API saat ini: memilih Phi Silica, Windows ML, dan DirectML","Panduan November 2026 tentang Windows AI API, ketersediaan Phi Silica, Windows ML, DirectML, dan metrik kinerja NPU berdasarkan dokumentasi resmi Microsoft."),
"ko":("현재 Windows AI API: Phi Silica, Windows ML, DirectML 선택하기","Microsoft 공식 문서를 바탕으로 2026년 11월 기준 Windows AI API, Phi Silica 지원 조건, Windows ML, DirectML, NPU 성능 지표를 정리합니다."),
"pt":("Windows AI APIs hoje: escolher Phi Silica, Windows ML e DirectML","Guia de novembro de 2026 sobre Windows AI APIs, disponibilidade do Phi Silica, Windows ML, DirectML e métricas de NPU com base na documentação da Microsoft."),
"ru":("Windows AI API сегодня: выбор Phi Silica, Windows ML и DirectML","Руководство за ноябрь 2026 года по Windows AI API, доступности Phi Silica, Windows ML, DirectML и показателям NPU на основе документации Microsoft."),
"zh-cn":("Windows AI API 现状：如何选择 Phi Silica、Windows ML 和 DirectML","依据 Microsoft 官方文档，介绍截至 2026 年 11 月的 Windows AI API、Phi Silica 可用条件、Windows ML、DirectML 和 NPU 性能指标。"),
"zh-tw":("Windows AI API 現況：如何選擇 Phi Silica、Windows ML 與 DirectML","依據 Microsoft 官方文件，介紹截至 2026 年 11 月的 Windows AI API、Phi Silica 可用條件、Windows ML、DirectML 與 NPU 效能指標。"),
"ar":("واجهات Windows AI اليوم: اختيار Phi Silica وWindows ML وDirectML","دليل نوفمبر 2026 حول واجهات Windows AI وتوافر Phi Silica وWindows ML وDirectML ومقاييس أداء NPU استناداً إلى وثائق Microsoft الرسمية."),
}

# Intro explains date, scope, availability, user consent, and model transition.
INTRO = {
"ja":"""# Windows AI APIの現在地：Phi Silica、Windows ML、DirectMLの選び方

> **更新日：2026年11月24日。** Windows AI APIは更新が速いため、同日時点のMicrosoft公式資料を基準にします。以前の会話コンテキスト／ストリーミングAPI例、固定NuGetバージョン、DirectMLがNPUを選択するという説明は現行仕様を正しく示していなかったため削除しました。

## Windows AI APIとPhi Silica

APIごとにハードウェア、OS、Windows App SDKの要件が異なります。Phi SilicaはWindows向けのローカル言語モデルですが、すべてのPCで使えるわけではありません。Copilot+ PCや一部の対応GPUなど、実行先により条件が異なります。また、Limited Access Featureと地域の制限があります。実装前に[対応状況](https://learn.microsoft.com/en-us/windows/ai/apis)と[セットアップ](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)を確認してください。

モデルが未準備なら、ダウンロード容量と通信量を説明し、利用者の同意を得てから準備を始めます。非対応デバイスや利用者が無効にした機能も判別し、代替手段を用意してください。MicrosoftはPhi SilicaからAion Instructへの移行予定も公表しています。モデル名や提供時期を固定前提にしないでください。""",
"en":"""# Windows AI APIs today: choosing Phi Silica, Windows ML, and DirectML

> **Updated November 24, 2026.** Windows AI APIs change quickly; this guide reflects Microsoft documentation checked on this date. The earlier conversation-context and streaming API examples, pinned NuGet versions, and claim that DirectML selects an NPU did not accurately describe the current APIs, so they have been removed.

## Windows AI APIs and Phi Silica

Hardware, OS, and Windows App SDK requirements vary by API. Phi Silica is a local language model for Windows, but it is not available on every PC. Requirements differ for Copilot+ PCs and other supported GPUs. It is also a Limited Access Feature with regional restrictions. Check Microsoft's [supported API and hardware matrix](https://learn.microsoft.com/en-us/windows/ai/apis) and [setup guide](https://learn.microsoft.com/en-us/windows/ai/apis/get-started) before choosing it.

If a model is not ready, explain download size and network use and obtain the user's consent before starting setup. Handle unsupported devices and features disabled by the user separately, and provide a fallback. Microsoft has announced a planned transition from Phi Silica to Aion Instruct. Do not treat a model name or availability date as permanent.""",
"de":"""# Windows-AI-APIs heute: Phi Silica, Windows ML und DirectML auswählen

> **Stand: 24. November 2026.** Windows AI APIs ändern sich schnell; dieser Leitfaden folgt der an diesem Tag geprüften Microsoft-Dokumentation. Die früheren Gesprächskontext- und Streamingbeispiele, festgelegten NuGet-Versionen und die Behauptung, DirectML wähle eine NPU, beschrieben die aktuellen APIs nicht korrekt und wurden entfernt.

## Windows AI APIs und Phi Silica

Hardware-, Betriebssystem- und Windows-App-SDK-Anforderungen unterscheiden sich je API. Phi Silica ist ein lokales Sprachmodell für Windows, aber nicht auf jedem PC verfügbar. Für Copilot+ PCs und andere unterstützte GPUs gelten unterschiedliche Voraussetzungen. Phi Silica ist außerdem ein Limited Access Feature und regional eingeschränkt. Prüfen Sie vor der Planung die [unterstützten APIs und Geräte](https://learn.microsoft.com/en-us/windows/ai/apis) sowie die [Einrichtung](https://learn.microsoft.com/en-us/windows/ai/apis/get-started).

Ist ein Modell noch nicht bereit, erläutern Sie Downloadgröße und Datenverbrauch und holen Sie die Zustimmung ein, bevor Sie die Einrichtung starten. Behandeln Sie nicht unterstützte Geräte und deaktivierte Funktionen getrennt und bieten Sie eine Alternative an. Microsoft hat einen geplanten Wechsel von Phi Silica zu Aion Instruct angekündigt. Modellnamen und Termine sind keine dauerhaften Zusagen.""",
"es":"""# Windows AI APIs hoy: elegir Phi Silica, Windows ML y DirectML

> **Actualizado el 24 de noviembre de 2026.** Las Windows AI APIs cambian con rapidez; esta guía refleja la documentación de Microsoft consultada en esa fecha. Se eliminaron los antiguos ejemplos de contexto conversacional y streaming, las versiones fijas de NuGet y la afirmación de que DirectML selecciona una NPU, porque no describían correctamente las API actuales.

## Windows AI APIs y Phi Silica

Los requisitos de hardware, sistema operativo y Windows App SDK varían según la API. Phi Silica es un modelo de lenguaje local para Windows, pero no está disponible en todos los PC. Las condiciones difieren entre Copilot+ PC y otras GPU compatibles. También es una función de acceso limitado (Limited Access Feature) y tiene restricciones regionales. Antes de elegirla, consulta la [compatibilidad de API y hardware](https://learn.microsoft.com/en-us/windows/ai/apis) y la [guía de configuración](https://learn.microsoft.com/en-us/windows/ai/apis/get-started).

Si el modelo aún no está listo, explica el tamaño de la descarga y el uso de red y solicita consentimiento antes de preparar el modelo. Trata por separado los dispositivos incompatibles y las funciones desactivadas por el usuario, y ofrece una alternativa. Microsoft anunció una transición prevista de Phi Silica a Aion Instruct; no des por permanentes el nombre ni la fecha de disponibilidad.""",
"fr":"""# Windows AI APIs aujourd'hui : choisir Phi Silica, Windows ML et DirectML

> **Mise à jour : 24 novembre 2026.** Les Windows AI APIs évoluent rapidement ; ce guide reflète la documentation Microsoft consultée à cette date. Les anciens exemples de contexte conversationnel et de streaming, les versions NuGet figées et l'affirmation selon laquelle DirectML sélectionne un NPU ne décrivaient pas correctement les API actuelles et ont été supprimés.

## Windows AI APIs et Phi Silica

Les exigences matérielles, système et Windows App SDK varient selon l'API. Phi Silica est un modèle de langage local pour Windows, mais il n'est pas disponible sur tous les PC. Les conditions diffèrent entre les Copilot+ PC et les autres GPU pris en charge. Phi Silica est aussi une fonctionnalité à accès limité (Limited Access Feature) et fait l'objet de restrictions régionales. Consultez la [matrice de compatibilité](https://learn.microsoft.com/en-us/windows/ai/apis) et le [guide de configuration](https://learn.microsoft.com/en-us/windows/ai/apis/get-started).

Si le modèle n'est pas prêt, expliquez la taille du téléchargement et l'utilisation du réseau, puis obtenez le consentement avant sa préparation. Gérez séparément les appareils incompatibles et les fonctionnalités désactivées, et prévoyez une solution de repli. Microsoft a annoncé une transition prévue de Phi Silica vers Aion Instruct : le nom du modèle et sa disponibilité ne sont pas définitifs.""",
"hi":"""# Windows AI APIs आज: Phi Silica, Windows ML और DirectML चुनना

> **अपडेट: 24 नवंबर 2026।** Windows AI APIs तेज़ी से बदलते हैं; यह लेख इस तारीख़ को देखे गए Microsoft दस्तावेज़ों पर आधारित है। पुराने conversation-context और streaming उदाहरण, तय NuGet संस्करण और DirectML द्वारा NPU चुनने का दावा वर्तमान API को सही ढंग से नहीं दिखाते थे, इसलिए हटा दिए गए हैं।

## Windows AI APIs और Phi Silica

हर API के लिए हार्डवेयर, OS और Windows App SDK की आवश्यकताएँ अलग हैं। Phi Silica Windows का स्थानीय भाषा मॉडल है, लेकिन हर PC पर उपलब्ध नहीं है। Copilot+ PC और अन्य समर्थित GPU के लिए शर्तें अलग हैं। यह Limited Access Feature भी है और क्षेत्रीय प्रतिबंध लागू हैं। पहले [समर्थित API और हार्डवेयर](https://learn.microsoft.com/en-us/windows/ai/apis) तथा [सेटअप मार्गदर्शिका](https://learn.microsoft.com/en-us/windows/ai/apis/get-started) देखें।

मॉडल तैयार न हो तो डाउनलोड आकार और नेटवर्क उपयोग समझाकर उपयोगकर्ता की सहमति के बाद ही तैयारी शुरू करें। असमर्थित डिवाइस और उपयोगकर्ता द्वारा बंद सुविधा को अलग संभालें और विकल्प दें। Microsoft ने Phi Silica से Aion Instruct पर नियोजित बदलाव घोषित किया है; मॉडल का नाम या उपलब्धता तारीख स्थायी न मानें।""",
"id":"""# Windows AI API saat ini: memilih Phi Silica, Windows ML, dan DirectML

> **Diperbarui 24 November 2026.** Windows AI API berubah cepat; panduan ini mengikuti dokumentasi Microsoft yang diperiksa pada tanggal tersebut. Contoh konteks percakapan dan streaming lama, versi NuGet yang dipatok, serta klaim bahwa DirectML memilih NPU tidak menggambarkan API saat ini dengan benar, sehingga dihapus.

## Windows AI API dan Phi Silica

Persyaratan perangkat keras, OS, dan Windows App SDK berbeda untuk setiap API. Phi Silica adalah model bahasa lokal untuk Windows, tetapi tidak tersedia di semua PC. Persyaratannya berbeda untuk Copilot+ PC dan GPU lain yang didukung. Phi Silica juga merupakan Limited Access Feature dan memiliki batasan wilayah. Periksa [dukungan API dan perangkat keras](https://learn.microsoft.com/en-us/windows/ai/apis) serta [panduan penyiapan](https://learn.microsoft.com/en-us/windows/ai/apis/get-started) sebelum memilihnya.

Jika model belum siap, jelaskan ukuran unduhan dan penggunaan jaringan, lalu minta persetujuan pengguna sebelum memulai penyiapan. Tangani perangkat yang tidak didukung dan fitur yang dinonaktifkan pengguna secara terpisah, serta sediakan alternatif. Microsoft mengumumkan rencana peralihan dari Phi Silica ke Aion Instruct; nama model dan tanggal ketersediaan dapat berubah.""",
"ko":"""# 현재 Windows AI API: Phi Silica, Windows ML, DirectML 선택하기

> **업데이트: 2026년 11월 24일.** Windows AI API는 빠르게 바뀌므로 이 글은 해당 날짜에 확인한 Microsoft 문서를 기준으로 합니다. 기존 대화 컨텍스트·스트리밍 예제, 고정 NuGet 버전, DirectML이 NPU를 선택한다는 설명은 현재 API를 정확히 반영하지 않아 삭제했습니다.

## Windows AI API와 Phi Silica

API마다 하드웨어, OS, Windows App SDK 요구 사항이 다릅니다. Phi Silica는 Windows용 로컬 언어 모델이지만 모든 PC에서 사용할 수 있는 것은 아닙니다. Copilot+ PC와 기타 지원 GPU의 조건도 서로 다릅니다. Limited Access Feature이며 지역 제한도 있습니다. 도입 전 [지원 API와 하드웨어](https://learn.microsoft.com/en-us/windows/ai/apis) 및 [설정 안내](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)를 확인하세요.

모델이 준비되지 않았다면 다운로드 크기와 네트워크 사용량을 안내하고 동의를 받은 뒤 준비를 시작하세요. 미지원 기기와 사용자가 비활성화한 기능을 구분하고 대안을 제공하세요. Microsoft는 Phi Silica에서 Aion Instruct로 전환할 계획도 발표했습니다. 모델명이나 제공 시점은 바뀔 수 있습니다.""",
"pt":"""# Windows AI APIs hoje: escolher Phi Silica, Windows ML e DirectML

> **Atualizado em 24 de novembro de 2026.** As Windows AI APIs mudam rapidamente; este guia segue a documentação Microsoft consultada nessa data. Os exemplos antigos de contexto de conversa e streaming, as versões fixas do NuGet e a afirmação de que o DirectML seleciona uma NPU não descreviam corretamente as APIs atuais e foram removidos.

## Windows AI APIs e Phi Silica

Os requisitos de hardware, sistema e Windows App SDK variam por API. Phi Silica é um modelo de linguagem local para Windows, mas não está disponível em todos os PCs. As condições diferem entre Copilot+ PCs e outras GPUs compatíveis. Também é um Limited Access Feature e tem restrições regionais. Consulte a [compatibilidade de APIs e hardware](https://learn.microsoft.com/en-us/windows/ai/apis) e o [guia de configuração](https://learn.microsoft.com/en-us/windows/ai/apis/get-started).

Se o modelo ainda não estiver pronto, explique o tamanho do download e o uso da rede e obtenha consentimento antes da preparação. Trate separadamente dispositivos incompatíveis e recursos desativados, e ofereça uma alternativa. A Microsoft anunciou a transição planejada de Phi Silica para Aion Instruct; o nome e a disponibilidade do modelo podem mudar.""",
"ru":"""# Windows AI API сегодня: выбор Phi Silica, Windows ML и DirectML

> **Обновлено 24 ноября 2026 года.** Windows AI API быстро меняются; руководство основано на документации Microsoft, проверенной на эту дату. Старые примеры контекста диалога и потоковой генерации, фиксированные версии NuGet и утверждение, что DirectML выбирает NPU, неточно описывали текущие API и удалены.

## Windows AI API и Phi Silica

Требования к оборудованию, ОС и Windows App SDK различаются для разных API. Phi Silica — локальная языковая модель для Windows, но она доступна не на каждом ПК. Для Copilot+ PC и других поддерживаемых GPU условия отличаются. Это Limited Access Feature с региональными ограничениями. Перед выбором проверьте [поддерживаемые API и оборудование](https://learn.microsoft.com/en-us/windows/ai/apis) и [руководство по настройке](https://learn.microsoft.com/en-us/windows/ai/apis/get-started).

Если модель не готова, объясните размер загрузки и расход трафика и получите согласие пользователя до начала настройки. Отдельно обрабатывайте неподдерживаемые устройства и отключённые функции, предусмотрите альтернативу. Microsoft объявила о планируемом переходе с Phi Silica на Aion Instruct; название и доступность модели могут измениться.""",
"zh-cn":"""# Windows AI API 现状：如何选择 Phi Silica、Windows ML 和 DirectML

> **更新日期：2026 年 11 月 24 日。** Windows AI API 更新很快；本文依据 Microsoft 在该日期查阅的官方文档。旧版的对话上下文和流式 API 示例、固定 NuGet 版本，以及“DirectML 会选择 NPU”的说法不能准确描述当前 API，因此已删除。

## Windows AI API 与 Phi Silica

各 API 对硬件、操作系统和 Windows App SDK 的要求不同。Phi Silica 是 Windows 本地语言模型，但并非所有 PC 都支持。Copilot+ PC 与其他受支持 GPU 的条件也不同。Phi Silica 还属于 Limited Access Feature，并有地区限制。选型前请查看[支持的 API 与硬件](https://learn.microsoft.com/en-us/windows/ai/apis)和[配置指南](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)。

模型尚未就绪时，应先说明下载大小和网络用量，取得用户同意后再开始准备。分别处理不支持的设备和被用户关闭的功能，并提供备用方案。Microsoft 已公布从 Phi Silica 迁移到 Aion Instruct 的计划；模型名称和可用日期可能变化。""",
"zh-tw":"""# Windows AI API 現況：如何選擇 Phi Silica、Windows ML 與 DirectML

> **更新日期：2026 年 11 月 24 日。** Windows AI API 更新快速；本文依據 Microsoft 在該日期查閱的官方文件。舊版的對話內容與串流 API 範例、固定 NuGet 版本，以及「DirectML 會選擇 NPU」的說法無法正確描述目前 API，因此已移除。

## Windows AI API 與 Phi Silica

各 API 對硬體、作業系統及 Windows App SDK 的要求不同。Phi Silica 是 Windows 本機語言模型，但並非所有電腦都支援。Copilot+ PC 與其他受支援 GPU 的條件也不同。Phi Silica 屬於 Limited Access Feature，並有地區限制。選用前請查閱[支援的 API 與硬體](https://learn.microsoft.com/en-us/windows/ai/apis)及[設定指南](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)。

模型尚未就緒時，先說明下載大小與網路用量，取得使用者同意後再開始準備。分別處理不支援的裝置和遭使用者停用的功能，並提供替代方案。Microsoft 已公布從 Phi Silica 移轉至 Aion Instruct 的計畫；模型名稱與供應日期可能變動。""",
"ar":"""# واجهات Windows AI اليوم: اختيار Phi Silica وWindows ML وDirectML

> **آخر تحديث: 24 نوفمبر 2026.** تتغير واجهات Windows AI بسرعة؛ ويعكس هذا الدليل وثائق Microsoft التي روجعت في ذلك التاريخ. حُذفت أمثلة السياق الحواري والبث القديمة وإصدارات NuGet المثبتة والقول إن DirectML يختار NPU، لأنها لا تصف الواجهات الحالية بدقة.

## واجهات Windows AI وPhi Silica

تختلف متطلبات الأجهزة ونظام التشغيل وWindows App SDK حسب الواجهة. Phi Silica نموذج لغوي محلي لـ Windows، لكنه غير متاح على كل حاسوب. وتختلف الشروط بين أجهزة Copilot+ PC ووحدات GPU الأخرى المدعومة. كما أنه ميزة وصول محدود (Limited Access Feature) مع قيود إقليمية. راجع [الواجهات والأجهزة المدعومة](https://learn.microsoft.com/en-us/windows/ai/apis) و[دليل الإعداد](https://learn.microsoft.com/en-us/windows/ai/apis/get-started) قبل الاختيار.

إذا لم يكن النموذج جاهزاً، فاشرح حجم التنزيل واستخدام الشبكة واحصل على موافقة المستخدم قبل الإعداد. عالج الأجهزة غير المدعومة والميزات التي عطّلها المستخدم كلّاً على حدة ووفر بديلاً. أعلنت Microsoft خطة انتقال من Phi Silica إلى Aion Instruct؛ وقد يتغير اسم النموذج وموعد توفره.""",
}

CODE = '''## C# example

```csharp
using System;
using Microsoft.Windows.AI;
using Microsoft.Windows.AI.Text;

var state = LanguageModel.GetReadyState();
if (state == AIFeatureReadyState.NotReady)
{
    // Explain the download and obtain user consent before this call.
    var result = await LanguageModel.EnsureReadyAsync();
    if (result.Status != AIFeatureReadyResultState.Success)
        throw result.ExtendedError;
    state = LanguageModel.GetReadyState();
}
if (state != AIFeatureReadyState.Ready)
    throw new InvalidOperationException($"LanguageModel unavailable: {state}");

using LanguageModel model = await LanguageModel.CreateAsync();
var response = await model.GenerateResponseAsync("Explain what an NPU does.");
Console.WriteLine(response.Text);
```
'''
CODE_HEAD = {"ja":"## C#の最小例", "en":"## Minimal C# example", "de":"## Minimales C#-Beispiel", "es":"## Ejemplo mínimo en C#", "fr":"## Exemple C# minimal", "hi":"## C# का न्यूनतम उदाहरण", "id":"## Contoh C# minimal", "ko":"## C# 최소 예제", "pt":"## Exemplo mínimo em C#", "ru":"## Минимальный пример на C#", "zh-cn":"## C# 最小示例", "zh-tw":"## C# 最小範例", "ar":"## مثال C# مختصر"}

SUFFIX = {
"ja":"""## カスタムONNXモデルと実行先

独自のONNXモデルには、MicrosoftはWindows MLをWindows向けの推奨経路として案内しています。Windows MLは対応ハードウェアに応じたExecution Providerの選択や配布を支援します。DirectMLは引き続きサポートされていますが、新機能開発はWindows MLに移っています。DirectMLはDirect3D 12ベースのGPU実行経路です。`device_id = 0` としてもNPUが選ばれるわけではありません。NPUを使う場合はWindows MLと対応ベンダーのExecution Providerの案内に従ってください。

## 性能値の読み方

Copilot+ PCの「40 TOPS以上」はNPU要件の目安であり、TOPSだけではアプリの速度を比較できません。演算精度、対応命令、電力条件も異なります。メモリ転送速度がMT/sで示される場合、DDRの両エッジ分を再度2倍しません。合計バス幅128 bit、8,533 MT/sなら理論値は `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s`（十進単位）です。実効値は構成と負荷で下がります。

ローカル推論がネットワーク送信を避けるのは、対象処理を実際に端末内で実行する場合です。アプリ全体のオフライン動作やデータ送信がないことは保証しません。モデル出力も検証してください。

## 公式資料

- [Windows AI APIs：対応機能とハードウェア](https://learn.microsoft.com/en-us/windows/ai/apis)
- [Windows AI APIアプリのセットアップ](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Phi Silicaの利用手順](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [Copilot+ PCのNPU開発ガイド](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [DirectMLの現状と利用方法](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

コードは公式資料に沿っていますが、このリポジトリではWindows SDKを使ったビルドをしていません。対象SDK、OS、Limited Access Featureの状態を公式資料で確認してください。""",
"en":"""## Custom ONNX models and hardware

For custom ONNX models, Microsoft recommends Windows ML as the Windows path. It helps select an Execution Provider for available hardware and manage its delivery. DirectML remains supported, but new feature development has moved to Windows ML. DirectML is a Direct3D 12 based GPU path; `device_id = 0` does not mean an NPU will be selected. For NPU execution, follow Windows ML and the supported vendor Execution Provider guidance.

## Reading performance figures

“40+ TOPS” is an NPU requirement associated with the Copilot+ PC category; TOPS alone cannot compare application speed. Precision, supported operations, and power conditions also matter. When a memory data rate is already in MT/s, do not multiply by two again for DDR edges. A total 128-bit bus at 8,533 MT/s has a theoretical rate of `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s` in decimal units. Real bandwidth is lower and depends on configuration and workload.

Local inference avoids network transfer for an operation only when the app actually runs it on-device. It does not guarantee that the whole app works offline or sends no data. Validate model output as well.

## Official references

- [Windows AI APIs: supported features and hardware](https://learn.microsoft.com/en-us/windows/ai/apis)
- [Set up a Windows AI API app](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Get started with Phi Silica](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [NPU development guide for Copilot+ PCs](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [DirectML status and getting started](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

The code follows Microsoft's documentation, but has not been built here with a Windows SDK. Recheck the target SDK, OS, and Limited Access Feature status in the official docs.""",
"de":"""## Eigene ONNX-Modelle und Hardware

Für eigene ONNX-Modelle empfiehlt Microsoft Windows ML als Weg für Windows. Es unterstützt die Auswahl eines passenden Execution Providers und dessen Bereitstellung. DirectML wird weiter unterstützt, doch die Entwicklung neuer Funktionen ist zu Windows ML gewechselt. DirectML ist ein GPU-Pfad auf Basis von Direct3D 12; `device_id = 0` wählt keine NPU aus. Für NPU-Ausführung gelten Windows ML und die Hinweise des unterstützten Anbieter-Execution-Providers.

## Leistungswerte einordnen

„40+ TOPS“ ist eine NPU-Anforderung der Kategorie Copilot+ PC. TOPS allein vergleicht keine Anwendungsgeschwindigkeit; Genauigkeit, unterstützte Operationen und Leistungsbedingungen zählen ebenfalls. Ist die Datenrate bereits in MT/s angegeben, darf sie für DDR nicht nochmals mit zwei multipliziert werden. Ein 128-Bit-Gesamtbus mit 8.533 MT/s erreicht theoretisch `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s` (Dezimaleinheiten). Real ist der Wert geringer.

Lokale Inferenz vermeidet Netzwerkverkehr nur für tatsächlich auf dem Gerät ausgeführte Vorgänge. Sie garantiert weder Offlinebetrieb der gesamten App noch ausbleibende Datenübertragung. Prüfen Sie außerdem die Modellausgaben.

## Offizielle Quellen

- [Windows AI APIs: Funktionen und Hardware](https://learn.microsoft.com/en-us/windows/ai/apis)
- [Einrichtung einer Windows-AI-App](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Phi Silica: Einstieg](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [NPU-Entwicklungsleitfaden](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [DirectML: Status und Einstieg](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

Der Code folgt Microsoft-Dokumenten, wurde hier aber nicht mit einem Windows SDK kompiliert. Prüfen Sie Ziel-SDK, Betriebssystem und Limited-Access-Feature-Status erneut.""",
"es":"""## Modelos ONNX propios y hardware

Para modelos ONNX propios, Microsoft recomienda Windows ML en Windows. Ayuda a elegir un Execution Provider adecuado y administrar su distribución. DirectML sigue teniendo soporte, pero el desarrollo de funciones nuevas pasó a Windows ML. DirectML es una vía de GPU basada en Direct3D 12; `device_id = 0` no selecciona una NPU. Para ejecutar en NPU, sigue las indicaciones de Windows ML y del Execution Provider compatible del fabricante.

## Interpretar cifras de rendimiento

«40+ TOPS» es un requisito de NPU asociado a la categoría Copilot+ PC. TOPS por sí solo no permite comparar la velocidad de aplicaciones; también influyen la precisión, las operaciones compatibles y la energía. Si la tasa de memoria ya está en MT/s, no la multipliques por dos otra vez por los flancos DDR. Un bus total de 128 bits a 8.533 MT/s alcanza teóricamente `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s` en unidades decimales. El ancho real es inferior.

La inferencia local evita el tráfico de red de una operación solo si la aplicación la ejecuta realmente en el dispositivo. No garantiza que toda la aplicación funcione sin conexión ni que no envíe datos. Valida también las salidas del modelo.

## Referencias oficiales

- [Windows AI APIs: funciones y hardware](https://learn.microsoft.com/en-us/windows/ai/apis)
- [Configuración de una aplicación Windows AI](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Introducción a Phi Silica](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [Guía de desarrollo NPU](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [Estado e inicio rápido de DirectML](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

El código sigue la documentación Microsoft, pero no se compiló aquí con un SDK de Windows. Comprueba de nuevo el SDK, el sistema operativo y el estado de Limited Access Feature.""",
"fr":"""## Modèles ONNX personnalisés et matériel

Pour les modèles ONNX personnalisés, Microsoft recommande Windows ML pour Windows. Il aide à choisir l'Execution Provider adapté et à gérer sa distribution. DirectML reste pris en charge, mais le développement des nouvelles fonctionnalités est passé à Windows ML. DirectML est une voie GPU fondée sur Direct3D 12 ; `device_id = 0` ne sélectionne pas un NPU. Pour le NPU, suivez Windows ML et les recommandations de l'Execution Provider pris en charge par le fabricant.

## Interpréter les performances

« 40+ TOPS » est une exigence NPU associée à la catégorie Copilot+ PC. Les TOPS seuls ne comparent pas la vitesse des applications : précision, opérations prises en charge et alimentation comptent aussi. Si le débit mémoire est déjà exprimé en MT/s, ne le multipliez pas une seconde fois par deux pour les fronts DDR. Un bus total de 128 bits à 8 533 MT/s atteint théoriquement `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s` en unités décimales. Le débit réel est inférieur.

L'inférence locale évite le trafic réseau d'une opération seulement si l'application l'exécute sur l'appareil. Elle ne garantit ni le mode hors ligne de toute l'application ni l'absence d'envoi de données. Vérifiez également les sorties du modèle.

## Références officielles

- [Windows AI APIs : fonctions et matériel](https://learn.microsoft.com/en-us/windows/ai/apis)
- [Configurer une application Windows AI](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Bien démarrer avec Phi Silica](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [Guide NPU pour Copilot+ PC](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [État et prise en main de DirectML](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

Le code suit la documentation Microsoft, mais n'a pas été compilé ici avec un SDK Windows. Vérifiez de nouveau le SDK, le système et le statut Limited Access Feature.""",
"hi":"""## कस्टम ONNX मॉडल और हार्डवेयर

अपने ONNX मॉडल के लिए Microsoft Windows ML की अनुशंसा करता है। यह उपलब्ध हार्डवेयर के लिए Execution Provider चुनने और उसके वितरण में मदद करता है। DirectML समर्थित है, लेकिन नई सुविधाओं का विकास Windows ML में चला गया है। DirectML, Direct3D 12 आधारित GPU मार्ग है; `device_id = 0` का अर्थ NPU चुनना नहीं है। NPU के लिए Windows ML और समर्थित विक्रेता Execution Provider की मार्गदर्शिका अपनाएँ।

## प्रदर्शन आँकड़ों को समझें

«40+ TOPS» Copilot+ PC श्रेणी से जुड़ी NPU आवश्यकता है; अकेले TOPS से ऐप की गति की तुलना नहीं होती। सटीकता, समर्थित ऑपरेशन और बिजली की स्थिति भी मायने रखते हैं। मेमोरी दर पहले से MT/s में हो तो DDR के दोनों किनारों के कारण उसे फिर से 2 से गुणा न करें। 128-bit कुल बस और 8,533 MT/s की सैद्धांतिक दर `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s` है। वास्तविक दर कम होगी। स्थानीय अनुमान नेटवर्क ट्रैफ़िक तभी रोकता है जब ऐप वह काम डिवाइस पर चलाए; इससे पूरे ऐप के ऑफलाइन होने या डेटा न भेजने की गारंटी नहीं मिलती।

## आधिकारिक संदर्भ

- [Windows AI APIs: सुविधाएँ और हार्डवेयर](https://learn.microsoft.com/en-us/windows/ai/apis)
- [ऐप सेटअप](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Phi Silica मार्गदर्शिका](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [NPU विकास मार्गदर्शिका](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [DirectML की स्थिति](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

कोड Microsoft दस्तावेज़ों के अनुरूप है, लेकिन यहाँ Windows SDK से बिल्ड नहीं किया गया। लागू SDK, OS और Limited Access Feature की स्थिति फिर जाँचें।""",
"id":"""## Model ONNX kustom dan perangkat keras

Untuk model ONNX kustom, Microsoft merekomendasikan Windows ML di Windows. Ini membantu memilih Execution Provider yang sesuai serta mengelola distribusinya. DirectML tetap didukung, tetapi pengembangan fitur baru telah beralih ke Windows ML. DirectML adalah jalur GPU berbasis Direct3D 12; `device_id = 0` tidak berarti NPU dipilih. Untuk NPU, ikuti panduan Windows ML dan Execution Provider vendor yang didukung.

## Memahami metrik kinerja

“40+ TOPS” adalah persyaratan NPU terkait kategori Copilot+ PC. TOPS saja tidak membandingkan kecepatan aplikasi; presisi, operasi yang didukung, dan kondisi daya juga berpengaruh. Jika laju memori sudah dalam MT/s, jangan kalikan dua lagi untuk kedua sisi DDR. Bus total 128-bit pada 8.533 MT/s memiliki laju teoretis `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s`. Nilai nyata lebih rendah. Inferensi lokal hanya menghindari lalu lintas jaringan untuk operasi yang benar-benar dijalankan di perangkat; ini tidak menjamin seluruh aplikasi offline atau tidak mengirim data.

## Referensi resmi

- [Windows AI APIs: fitur dan perangkat keras](https://learn.microsoft.com/en-us/windows/ai/apis)
- [Penyiapan aplikasi Windows AI](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Panduan Phi Silica](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [Panduan pengembangan NPU](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [Status DirectML](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

Kode mengikuti dokumentasi Microsoft, tetapi belum dibangun di sini dengan Windows SDK. Periksa kembali SDK, OS, dan status Limited Access Feature.""",
"ko":"""## 사용자 지정 ONNX 모델과 하드웨어

사용자 지정 ONNX 모델에는 Microsoft가 Windows ML을 권장합니다. 사용 가능한 하드웨어에 맞는 Execution Provider 선택과 배포 관리를 돕습니다. DirectML은 계속 지원되지만 신규 기능 개발은 Windows ML로 이동했습니다. DirectML은 Direct3D 12 기반 GPU 실행 경로이며 `device_id = 0`이라고 해서 NPU가 선택되지는 않습니다. NPU에는 Windows ML과 지원되는 제조사 Execution Provider 지침을 따르세요.

## 성능 수치 해석

“40+ TOPS”는 Copilot+ PC 범주와 관련된 NPU 요구 사항입니다. TOPS만으로 앱 속도를 비교할 수 없으며 정밀도, 지원 연산, 전력 조건도 영향을 줍니다. 메모리 전송률이 MT/s라면 DDR 양쪽 에지를 이유로 다시 2를 곱하지 않습니다. 총 128-bit 버스가 8,533 MT/s일 때 이론값은 `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s`입니다. 실제 대역폭은 더 낮습니다. 로컬 추론은 해당 작업이 기기에서 실행될 때 네트워크 전송을 피할 뿐, 앱 전체의 오프라인 동작이나 데이터 미전송을 보장하지 않습니다.

## 공식 자료

- [Windows AI API 지원 기능과 하드웨어](https://learn.microsoft.com/en-us/windows/ai/apis)
- [앱 설정 안내](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Phi Silica 시작하기](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [Copilot+ PC NPU 개발 가이드](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [DirectML 현황](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

코드는 Microsoft 문서에 따랐지만 여기서 Windows SDK로 빌드하지 않았습니다. SDK, OS, Limited Access Feature 상태를 다시 확인하세요.""",
"pt":"""## Modelos ONNX personalizados e hardware

Para modelos ONNX personalizados, a Microsoft recomenda Windows ML no Windows. Ele ajuda a escolher um Execution Provider adequado e gerenciar sua distribuição. O DirectML continua com suporte, mas o desenvolvimento de novos recursos passou para Windows ML. DirectML é uma via de GPU baseada em Direct3D 12; `device_id = 0` não seleciona uma NPU. Para NPU, siga as orientações do Windows ML e do Execution Provider compatível do fabricante.

## Interpretar métricas de desempenho

“40+ TOPS” é um requisito de NPU associado à categoria Copilot+ PC. TOPS sozinho não compara a velocidade dos aplicativos; precisão, operações compatíveis e energia também contam. Se a taxa de memória já estiver em MT/s, não a multiplique por dois novamente por causa das bordas DDR. Um barramento total de 128 bits a 8.533 MT/s tem taxa teórica de `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s`. A taxa real é menor. A inferência local evita tráfego de rede apenas quando a operação é executada no dispositivo; isso não garante que o app inteiro funcione offline ou não envie dados.

## Referências oficiais

- [Windows AI APIs: recursos e hardware](https://learn.microsoft.com/en-us/windows/ai/apis)
- [Configuração de aplicativos](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Introdução ao Phi Silica](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [Guia NPU para Copilot+ PCs](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [Situação do DirectML](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

O código segue a documentação Microsoft, mas não foi compilado aqui com um Windows SDK. Confira o SDK, o sistema operacional e o status de Limited Access Feature.""",
"ru":"""## Собственные модели ONNX и оборудование

Для собственных моделей ONNX Microsoft рекомендует Windows ML. Он помогает выбирать Execution Provider для доступного оборудования и управлять его распространением. DirectML по-прежнему поддерживается, но разработка новых функций перенесена в Windows ML. DirectML — GPU-путь на основе Direct3D 12; `device_id = 0` не означает выбор NPU. Для NPU следуйте рекомендациям Windows ML и поддерживаемого Execution Provider производителя.

## Как понимать показатели производительности

«40+ TOPS» — требование к NPU, связанное с категорией Copilot+ PC. Одних TOPS недостаточно для сравнения скорости приложений: важны точность, поддерживаемые операции и энергопотребление. Если скорость памяти уже указана в MT/s, не умножайте её повторно на два из-за фронтов DDR. Для общей шины 128 бит и 8 533 MT/s теоретическое значение — `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s`; фактическая пропускная способность ниже. Локальный вывод избегает сетевой передачи лишь для операций, реально выполняемых на устройстве; это не гарантирует офлайн-работу всего приложения или отсутствие отправки данных.

## Официальные источники

- [Windows AI API: функции и оборудование](https://learn.microsoft.com/en-us/windows/ai/apis)
- [Настройка приложения](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Начало работы с Phi Silica](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [Руководство по NPU Copilot+ PC](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [Статус DirectML](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

Код соответствует документации Microsoft, но здесь не собирался с Windows SDK. Проверьте целевые SDK, ОС и статус Limited Access Feature.""",
"zh-cn":"""## 自定义 ONNX 模型与硬件

对于自定义 ONNX 模型，Microsoft 推荐在 Windows 上使用 Windows ML。它会帮助根据可用硬件选择 Execution Provider，并管理其交付。DirectML 仍受支持，但新功能开发已转向 Windows ML。DirectML 是基于 Direct3D 12 的 GPU 执行路径；`device_id = 0` 并不表示会选择 NPU。使用 NPU 时，请遵循 Windows ML 和受支持厂商 Execution Provider 的指南。

## 如何理解性能指标

“40+ TOPS”是与 Copilot+ PC 类别相关的 NPU 要求。TOPS 本身不足以比较应用速度；精度、支持的运算和功耗条件也很重要。如果内存速率已用 MT/s 表示，就不要因 DDR 的两个边沿再次乘以 2。总线宽 128 bit、速率 8,533 MT/s 时，理论值为 `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s`，实际带宽更低。本地推理只在应用确实于设备上执行操作时避免该操作的网络传输；这不保证整个应用离线运行或完全不发送数据。

## 官方资料

- [Windows AI API：支持功能与硬件](https://learn.microsoft.com/en-us/windows/ai/apis)
- [应用配置指南](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Phi Silica 入门](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [Copilot+ PC NPU 开发指南](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [DirectML 状态与入门](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

代码依据 Microsoft 文档编写，但未在此使用 Windows SDK 构建。请重新确认目标 SDK、OS 和 Limited Access Feature 状态。""",
"zh-tw":"""## 自訂 ONNX 模型與硬體

對於自訂 ONNX 模型，Microsoft 建議在 Windows 上使用 Windows ML。它會協助依可用硬體選擇 Execution Provider，並管理其交付。DirectML 仍受支援，但新功能開發已轉往 Windows ML。DirectML 是以 Direct3D 12 為基礎的 GPU 執行路徑；`device_id = 0` 不代表會選擇 NPU。使用 NPU 時，請遵循 Windows ML 與受支援廠商 Execution Provider 的指引。

## 如何解讀效能數據

「40+ TOPS」是與 Copilot+ PC 類別相關的 NPU 要求。TOPS 本身不足以比較應用程式速度；精度、支援的運算與功耗條件也很重要。若記憶體速率已用 MT/s 表示，就不要因 DDR 的兩個邊緣再次乘以 2。總線寬 128 bit、速率 8,533 MT/s 時，理論值為 `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s`，實際頻寬較低。本機推論只有在應用程式確實於裝置上執行操作時，才會避免該操作的網路傳輸；這不保證整個應用程式可離線運作或完全不傳送資料。

## 官方參考資料

- [Windows AI API：支援功能與硬體](https://learn.microsoft.com/en-us/windows/ai/apis)
- [應用程式設定指南](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [Phi Silica 入門](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [Copilot+ PC NPU 開發指南](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [DirectML 狀態與入門](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

程式碼依據 Microsoft 文件編寫，但未在此使用 Windows SDK 建置。請重新確認目標 SDK、OS 與 Limited Access Feature 狀態。""",
"ar":"""## نماذج ONNX مخصصة والأجهزة

توصي Microsoft باستخدام Windows ML لنماذج ONNX المخصصة على Windows. فهو يساعد في اختيار Execution Provider للأجهزة المتاحة وإدارة توزيعه. لا يزال DirectML مدعوماً، لكن تطوير الميزات الجديدة انتقل إلى Windows ML. DirectML مسار GPU قائم على Direct3D 12؛ ولا يعني `device_id = 0` اختيار NPU. لاستهداف NPU، اتبع إرشادات Windows ML وExecution Provider المدعوم من الشركة المصنّعة.

## فهم أرقام الأداء

«40+ TOPS» متطلب NPU مرتبط بفئة Copilot+ PC. ولا تكفي TOPS وحدها لمقارنة سرعة التطبيقات؛ فالدقة والعمليات المدعومة والطاقة مهمة أيضاً. إذا كان معدل نقل الذاكرة محدداً بوحدة MT/s، فلا تضربه مرة أخرى في 2 بسبب حافتي DDR. يبلغ المعدل النظري لناقل إجمالي بعرض 128 bit وسرعة 8,533 MT/s مقدار `8533 × 10^6 × 128 ÷ 8 ≈ 136.5 GB/s`، بينما يكون المعدل الفعلي أقل. لا تتجنب الاستدلالات المحلية نقل الشبكة إلا للعملية التي ينفذها التطبيق فعلياً على الجهاز؛ ولا يضمن ذلك عمل التطبيق كله دون اتصال أو عدم إرسال البيانات.

## مراجع رسمية

- [واجهات Windows AI: الميزات والأجهزة المدعومة](https://learn.microsoft.com/en-us/windows/ai/apis)
- [إعداد تطبيق Windows AI](https://learn.microsoft.com/en-us/windows/ai/apis/get-started)
- [البدء باستخدام Phi Silica](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica)
- [دليل تطوير NPU لأجهزة Copilot+ PC](https://learn.microsoft.com/en-us/windows/ai/npu-devices)
- [حالة DirectML والبدء به](https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started)

يتبع الكود وثائق Microsoft، لكنه لم يُبنَ هنا باستخدام Windows SDK. تحقّق مجدداً من SDK ونظام التشغيل وحالة Limited Access Feature.""",
}

CODE = '''```csharp
using System;
using Microsoft.Windows.AI;
using Microsoft.Windows.AI.Text;

var state = LanguageModel.GetReadyState();
if (state == AIFeatureReadyState.NotReady)
{
    // Explain the download and obtain user consent before this call.
    var result = await LanguageModel.EnsureReadyAsync();
    if (result.Status != AIFeatureReadyResultState.Success)
        throw result.ExtendedError;
    state = LanguageModel.GetReadyState();
}
if (state != AIFeatureReadyState.Ready)
    throw new InvalidOperationException($"LanguageModel unavailable: {state}");

using LanguageModel model = await LanguageModel.CreateAsync();
var response = await model.GenerateResponseAsync("Explain what an NPU does.");
Console.WriteLine(response.Text);
```'''
CODE_HEAD = {"ja":"## C#の最小例", "en":"## Minimal C# example", "de":"## Minimales C#-Beispiel", "es":"## Ejemplo mínimo en C#", "fr":"## Exemple C# minimal", "hi":"## C# का न्यूनतम उदाहरण", "id":"## Contoh C# minimal", "ko":"## C# 최소 예제", "pt":"## Exemplo mínimo em C#", "ru":"## Минимальный пример на C#", "zh-cn":"## C# 最小示例", "zh-tw":"## C# 最小範例", "ar":"## مثال C# مختصر"}

def digest(text):
    return hashlib.sha256(text.replace("\r\n", "\n").encode("utf-8")).hexdigest()

for lang in LANGS:
    path = BUNDLE / ("index.md" if lang == "ja" else f"index.{lang}.md")
    raw = path.read_text(encoding="utf-8-sig")
    if not raw.startswith("---\n"):
        raise ValueError(f"{lang}: invalid front matter")
    front, _ = raw.split("---", 1)[1].split("\n---\n", 1)
    title, description = META[lang]
    front = re.sub(r"(?m)^title:.*$", "title: " + json.dumps(title, ensure_ascii=False), front)
    front = re.sub(r"(?m)^description:.*$", "description: " + json.dumps(description, ensure_ascii=False), front)
    front = re.sub(r"(?m)^(?:date|lastmod|math|mermaid):[^\r\n]*(?:\r?\n|$)", "", front)
    front = front.rstrip() + f'\ndate: "2026-09-11T18:00:00+09:00"\nlastmod: "{TODAY}T00:00:00+09:00"\n'
    body = INTRO[lang] + "\n\n" + CODE_HEAD[lang] + "\n\n" + CODE + "\n\n" + SUFFIX[lang]
    content = "---\n" + front.strip("\r\n") + "\n---\n" + body.strip() + "\n"
    content = "\n".join(line.rstrip() for line in content.splitlines()) + "\n"
    path.write_text(content, encoding="utf-8")

def sha_file(path):
    return digest(path.read_text(encoding="utf-8-sig"))

source_hash = sha_file(BUNDLE / "index.md")
reviews = {}
for lang in LANGS:
    if lang == "ja":
        continue
    path = BUNDLE / f"index.{lang}.md"
    rel = f"post/{BUNDLE.name}/{path.name}"
    summary = "Compared the complete edition with the Japanese source; checked API availability, consent flow, hardware distinction, corrected arithmetic, code shape, and official links."
    terms = "Checked Phi Silica, Aion Instruct, Windows App SDK, Windows ML, DirectML, Execution Provider, TOPS, and MT/s in the localized edition."
    reviews[rel] = {
        "reviewKind":"ai", "reviewedAt":TODAY, "reviewer":"Codex (AI)",
        "source":SOURCE, "sourceHash":source_hash, "translationHash":sha_file(path), "summary":summary,
        "checks":{
            "meaning":{"status":"checked","note":summary},
            "terminology":{"status":"checked","note":terms},
            "mathematics":{"status":"checked","note":"Corrected memory bandwidth to 8,533 MT/s × 128 bit ÷ 8 ≈ 136.5 GB/s and removed unsupported generic peak-TOPS calculations."},
            "code":{"status":"checked","note":"Replaced unsupported API sample with the documented readiness, consent, model creation, and generation flow; not compiled in this repository."},
            "links":{"status":"checked","note":"Added five checked Microsoft Learn references for Windows AI APIs, setup, Phi Silica, NPU guidance, and DirectML."},
        },
        "limitations":["AI-assisted translation review; no human or native-speaker certification.","The C# sample follows Microsoft documentation but was not compiled with a Windows SDK in this repository.","Windows AI API and model availability are time-sensitive; documentation was checked on 2026-11-24."],
    }

entry = {
    "version":1, "batch":102, "article":BUNDLE.name, "reviewedAt":TODAY,
    "sourceHash":source_hash, "sources":list(URLS.values()),
    "scope":"Rewrote the full Japanese article and all twelve translations. Checked Windows AI/Phi Silica hardware and access requirements, replaced unsupported API examples, corrected DirectML/NPU claims and memory-bandwidth arithmetic, qualified offline/privacy claims, and aligned the current C# sample and source links across locales.",
    "findings":[
        "Removed obsolete conversation and streaming code, unsupported option properties, and device-selection claims; added the current documented C# readiness and generation flow.",
        "Clarified Phi Silica hardware, regional, and Limited Access Feature restrictions and recorded Microsoft's announced Aion Instruct transition as time-sensitive.",
        "Clarified Windows ML as the recommended Windows path for custom ONNX models; DirectML remains supported, with new development moved to Windows ML, and is a GPU path.",
        "Corrected the memory-bandwidth example to 8,533 MT/s × 128 bit ÷ 8 ≈ 136.5 GB/s and removed the duplicate DDR factor and unsupported generic peak-TOPS derivation.",
        "Qualified local/offline privacy claims, added five Microsoft Learn references, and disclosed that the sample was not compiled in this repository.",
    ],
    "publicationPending":True, "reviews":reviews,
}
evidence = DOCS / "batch-102.json"
evidence.write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
for rel, review in reviews.items():
    record = {k:review[k] for k in ("source","reviewedAt","reviewer","sourceHash","translationHash","reviewKind")}
    record["evidence"] = "docs/translation-review/batch-102.json"
    record["evidenceHash"] = digest(json.dumps(review, ensure_ascii=False, sort_keys=True))
    ledger["reviews"][rel] = record
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"batch":102,"translations":len(reviews),"sourceHash":source_hash}, ensure_ascii=False))
