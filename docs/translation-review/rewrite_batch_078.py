from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
ARTICLE = ROOT / "content/post/Google One （Gemini）が解約できない時の対処方法"
EDITION = {
"en": {
"title": "How to Cancel a Google One Plan with Google AI or Gemini",
"description": "Learn how to cancel a Google One plan that includes Google AI or Gemini, based on where you subscribed. Find the right billing account, troubleshoot missing cancellation options, and understand what happens to storage afterward.",
"body": r'''# How to Cancel a Google One Plan with Google AI or Gemini

Paid Gemini features may be included with a Google One membership such as a Google AI plan. Whether a free trial is offered, its length, the price, and the renewal date depend on the offer and region. Check your Google Account subscription details instead of relying on old prices or trial terms.

Where to cancel depends on how you subscribed: Google One, Google Play, the Apple App Store, a carrier, or another provider. Check these in order to rule out using the wrong account or billing service.

## 1. Find the account and billing provider

Check your signup email or receipt for the Google Account used to purchase the plan and the billing provider. If you use multiple Google Accounts, switch accounts in Google One or Google Play. If a family manager bought the plan, other members may not see its management controls.

## 2. Cancel where you subscribed

* **Google One:** Open [Google One](https://one.google.com/) with the purchasing account, go to Settings, and choose **Cancel membership**. In Gemini, open Settings, choose **Manage subscriptions**, then continue to Google One settings.
* **Google Play:** Open [Google Play subscriptions](https://play.google.com/store/account/subscriptions), select the plan, and choose **Cancel subscription**. Uninstalling an app does not cancel a subscription.
* **Apple App Store:** On an iPhone or iPad, open Settings, tap your name, then **Subscriptions**, and cancel the Google One plan.
* **A carrier or other provider:** Cancel through that provider's account page or support team. For a family plan, contact the person who manages the subscription.

See Google's [Google One cancellation instructions](https://support.google.com/googleone/answer/9056360) and [Google Play cancellation instructions](https://support.google.com/googleplay/answer/7018481). Labels and screen layouts may vary by device, region, and billing arrangement.

## If you cannot find the cancellation option

Sign in with the account shown on the receipt and check which store or provider manages the plan. A status such as **Already canceled** or an end date may mean renewal has stopped. If unsure, check the confirmation email and subscription status, or contact the billing provider.

The [Google Account service deletion page](https://myaccount.google.com/deleteservices) is not the first page to use as a substitute for ordinary cancellation. Google documents deleting the Google One service for specific situations, such as when switching services and a direct subscription transfer is unavailable. Read the on-screen explanation; do not confuse canceling a membership with deleting a service.

## After you cancel

Usually, benefits remain available until the end of the billing period you paid for. Check the confirmation email and subscription page for a stopped renewal and the end date.

When extra Google One storage ends, accounts above the free allowance (usually 15 GB) may be restricted from sending or receiving Gmail, uploading or syncing Drive files, or backing up photos in Google Photos. Check your storage use before canceling and remove files if needed.

## Official references

* [Cancel a Google One membership](https://support.google.com/googleone/answer/9056360)
* [Cancel a Google Play subscription](https://support.google.com/googleplay/answer/7018481)
* [Manage a Google AI plan in Gemini](https://support.google.com/gemini/answer/14517446?hl=en)'''
},
"de": {
"title": "Google One mit Google AI oder Gemini kündigen",
"description": "So kündigen Sie einen Google-One-Tarif mit Google AI oder Gemini beim richtigen Anbieter. Finden Sie das Abrechnungskonto, prüfen Sie fehlende Kündigungsoptionen und erfahren Sie, was danach mit dem Speicher passiert.",
"body": r'''# Google One mit Google AI oder Gemini kündigen

Kostenpflichtige Gemini-Funktionen können in einer Google-One-Mitgliedschaft wie einem Google-AI-Tarif enthalten sein. Ob es einen kostenlosen Testzeitraum gibt, wie lange er dauert, welcher Preis gilt und wann verlängert wird, hängt vom Angebot und der Region ab. Prüfen Sie die Angaben in Ihrem Google-Konto, statt sich auf ältere Preise oder Testbedingungen zu verlassen.

Wo Sie kündigen, hängt davon ab, wo Sie das Abo abgeschlossen haben: Google One, Google Play, Apple App Store, Mobilfunkanbieter oder ein anderer Anbieter. Prüfen Sie der Reihe nach Konto und Abrechnungsstelle.

## 1. Konto und Abrechnungsstelle ermitteln

Prüfen Sie die Bestätigungs-E-Mail oder Rechnung auf das verwendete Google-Konto und den Rechnungsaussteller. Bei mehreren Google-Konten wechseln Sie das Konto in Google One oder Google Play. Hat die Familiengruppenverwaltung den Tarif abgeschlossen, sehen andere Mitglieder möglicherweise keine Verwaltungsoptionen.

## 2. Beim Abschlussanbieter kündigen

* **Google One:** Öffnen Sie [Google One](https://one.google.com/) mit dem kaufenden Konto, gehen Sie zu den Einstellungen und wählen Sie **Mitgliedschaft kündigen**. In Gemini öffnen Sie die Einstellungen, wählen **Abos verwalten** und wechseln zu den Google-One-Einstellungen.
* **Google Play:** Öffnen Sie [Google Play-Abos](https://play.google.com/store/account/subscriptions), wählen Sie den Tarif und dann **Abo kündigen**. Das Deinstallieren einer App kündigt kein Abo.
* **Apple App Store:** Öffnen Sie auf iPhone oder iPad die Einstellungen, tippen Sie auf Ihren Namen und dann auf **Abonnements**. Kündigen Sie dort Google One.
* **Mobilfunkanbieter oder anderer Anbieter:** Kündigen Sie im Kundenkonto oder beim Support dieses Anbieters. Bei einem Familientarif wenden Sie sich an die verwaltende Person.

Details finden Sie in Googles [Anleitung zur Kündigung von Google One](https://support.google.com/googleone/answer/9056360) und [Anleitung zu Google-Play-Abos](https://support.google.com/googleplay/answer/7018481). Bezeichnungen und Menüs unterscheiden sich je nach Gerät, Region und Abrechnung.

## Wenn die Kündigungsoption fehlt

Melden Sie sich mit dem Konto aus der Kaufbestätigung an und prüfen Sie, welcher Store oder Anbieter das Abo verwaltet. Ein Status wie **Bereits gekündigt** oder ein Enddatum kann bedeuten, dass die Verlängerung schon gestoppt ist. Prüfen Sie im Zweifel die Bestätigungsmail und den Abo-Status oder wenden Sie sich an den Rechnungsaussteller.

Die [Seite zum Löschen eines Google-Dienstes](https://myaccount.google.com/deleteservices) ist kein erster Ersatz für die normale Kündigung. Google beschreibt das Löschen des Google-One-Dienstes für besondere Fälle, etwa wenn Sie den Anbieter wechseln und das Abo nicht direkt übertragen werden kann. Lesen Sie den angezeigten Hinweis und verwechseln Sie die Kündigung der Mitgliedschaft nicht mit dem Löschen eines Dienstes.

## Nach der Kündigung

In der Regel bleiben Vorteile bis zum Ende des bereits bezahlten Abrechnungszeitraums verfügbar. Prüfen Sie in der Bestätigungsmail und auf der Abo-Seite, dass die Verlängerung gestoppt wurde und welches Enddatum gilt.

Fällt zusätzlicher Google-One-Speicher weg, können Konten oberhalb des kostenlosen Speicherplatzes (meist 15 GB) Gmail-Nachrichten nicht mehr senden oder empfangen, Drive-Dateien nicht hochladen oder synchronisieren und Google-Fotos nicht sichern. Prüfen Sie vorher die Speicherbelegung und löschen Sie bei Bedarf Dateien.

## Offizielle Quellen

* [Google-One-Mitgliedschaft kündigen](https://support.google.com/googleone/answer/9056360)
* [Google-Play-Abo kündigen](https://support.google.com/googleplay/answer/7018481)
* [Google-AI-Tarif in Gemini verwalten](https://support.google.com/gemini/answer/14517446?hl=de)'''
},
"es": {
"title": "Cómo cancelar un plan de Google One con Google AI o Gemini",
"description": "Aprende a cancelar un plan de Google One con Google AI o Gemini según dónde te suscribiste. Identifica la cuenta y el proveedor de cobro, encuentra opciones de cancelación y conoce el efecto en el almacenamiento.",
"body": r'''# Cómo cancelar un plan de Google One con Google AI o Gemini

Algunas funciones de pago de Gemini pueden estar incluidas en una suscripción de Google One, como un plan de Google AI. La disponibilidad y duración de las pruebas, el precio y la fecha de renovación dependen de la oferta y la región. Consulta los datos de la suscripción en tu cuenta de Google y no des por válidos los precios o condiciones de artículos antiguos.

El lugar para cancelar depende de dónde te suscribiste: Google One, Google Play, App Store de Apple, una operadora u otro proveedor. Comprueba lo siguiente en orden para descartar que estés usando otra cuenta o servicio de cobro.

## 1. Identifica la cuenta y quién te cobra

Revisa el correo de confirmación o el recibo para identificar la cuenta de Google y el proveedor de facturación. Si usas varias cuentas, cambia de cuenta en Google One o Google Play. Si el administrador de un grupo familiar contrató el plan, quizá los demás miembros no puedan gestionarlo.

## 2. Cancela desde el servicio donde te suscribiste

* **Google One:** Abre [Google One](https://one.google.com/) con la cuenta de compra, ve a Configuración y elige **Cancelar membresía**. En Gemini, abre Configuración, selecciona **Administrar suscripciones** y continúa en la configuración de Google One.
* **Google Play:** Abre [suscripciones de Google Play](https://play.google.com/store/account/subscriptions), selecciona el plan y pulsa **Cancelar suscripción**. Desinstalar una aplicación no cancela la suscripción.
* **App Store de Apple:** En un iPhone o iPad, abre Configuración, toca tu nombre y luego **Suscripciones**; cancela allí el plan de Google One.
* **Operadora u otro proveedor:** Cancela desde la cuenta o el soporte de ese proveedor. Si el plan lo administra un familiar, consúltalo con esa persona.

Consulta las instrucciones oficiales para [cancelar Google One](https://support.google.com/googleone/answer/9056360) y [cancelar suscripciones de Google Play](https://support.google.com/googleplay/answer/7018481). Los nombres de los menús pueden variar según el dispositivo, la región y el método de cobro.

## Si no encuentras la opción para cancelar

Inicia sesión con la cuenta que figura en el recibo y comprueba qué tienda o proveedor administra el plan. Un estado como **Ya cancelada** o una fecha de finalización puede significar que ya se detuvo la renovación. Si no está claro, revisa el correo de confirmación y el estado de la suscripción, o contacta con quien te cobra.

La [página para eliminar un servicio de Google](https://myaccount.google.com/deleteservices) no es la primera opción para sustituir la cancelación habitual. Google la indica para situaciones concretas, por ejemplo, al cambiar de servicio cuando no es posible transferir directamente la suscripción. Lee lo que muestra la página y no confundas cancelar la membresía con eliminar un servicio.

## Después de cancelar

Normalmente, los beneficios siguen activos hasta que termine el período de facturación ya pagado. Comprueba en el correo y la página de suscripciones que se haya detenido la renovación y cuál es la fecha de finalización.

Al terminar el almacenamiento adicional de Google One, las cuentas que superen el espacio gratuito (normalmente 15 GB) pueden tener restricciones para enviar o recibir Gmail, subir o sincronizar archivos en Drive y guardar copias de seguridad en Google Fotos. Comprueba el espacio usado antes de cancelar y libera archivos si hace falta.

## Fuentes oficiales

* [Cancelar una membresía de Google One](https://support.google.com/googleone/answer/9056360)
* [Cancelar una suscripción de Google Play](https://support.google.com/googleplay/answer/7018481)
* [Administrar un plan de Google AI en Gemini](https://support.google.com/gemini/answer/14517446?hl=es)'''
},
"fr": {
"title": "Résilier un forfait Google One avec Google AI ou Gemini",
"description": "Découvrez comment résilier un forfait Google One incluant Google AI ou Gemini selon le service auquel vous vous êtes abonné. Identifiez le compte et le fournisseur de facturation, puis vérifiez les effets sur votre espace de stockage.",
"body": r'''# Résilier un forfait Google One avec Google AI ou Gemini

Certaines fonctionnalités payantes de Gemini peuvent être incluses dans un abonnement Google One, comme un forfait Google AI. L'existence et la durée d'un essai gratuit, le prix et la date de renouvellement dépendent de l'offre et de la région. Consultez les informations de votre compte Google au lieu de vous fier aux anciens prix ou conditions d'essai.

La résiliation dépend du service utilisé pour souscrire : Google One, Google Play, l'App Store d'Apple, un opérateur ou un autre fournisseur. Vérifiez ces éléments dans l'ordre pour écarter une erreur de compte ou de facturation.

## 1. Identifier le compte et le fournisseur de facturation

Consultez l'e-mail de confirmation ou le reçu pour retrouver le compte Google utilisé et le fournisseur qui vous facture. Si vous avez plusieurs comptes, changez de compte dans Google One ou Google Play. Si le responsable d'un groupe familial a souscrit le forfait, les autres membres ne disposent pas toujours des commandes de gestion.

## 2. Résilier auprès du service utilisé lors de la souscription

* **Google One :** Ouvrez [Google One](https://one.google.com/) avec le compte acheteur, accédez aux paramètres et choisissez **Résilier l'abonnement**. Dans Gemini, ouvrez les paramètres, sélectionnez **Gérer les abonnements**, puis accédez aux paramètres Google One.
* **Google Play :** Ouvrez [les abonnements Google Play](https://play.google.com/store/account/subscriptions), sélectionnez le forfait et choisissez **Résilier l'abonnement**. Désinstaller une application ne résilie pas un abonnement.
* **App Store d'Apple :** Sur iPhone ou iPad, ouvrez Réglages, touchez votre nom, puis **Abonnements** et résiliez le forfait Google One.
* **Opérateur ou autre fournisseur :** Résiliez depuis l'espace client ou auprès du service d'assistance de ce fournisseur. Pour un forfait familial, contactez la personne qui le gère.

Consultez les consignes officielles pour [résilier Google One](https://support.google.com/googleone/answer/9056360) et [résilier un abonnement Google Play](https://support.google.com/googleplay/answer/7018481). Les intitulés et menus peuvent varier selon l'appareil, la région et la facturation.

## Si l'option de résiliation est introuvable

Connectez-vous au compte indiqué sur le reçu et vérifiez quelle boutique ou quel fournisseur gère le forfait. Un état **Déjà résilié** ou une date de fin peut indiquer que le renouvellement est déjà arrêté. En cas de doute, consultez l'e-mail de confirmation et l'état de l'abonnement, ou contactez le fournisseur de facturation.

La [page de suppression d'un service Google](https://myaccount.google.com/deleteservices) ne doit pas remplacer en premier lieu la résiliation habituelle. Google décrit la suppression du service Google One dans des cas particuliers, par exemple lors d'un changement de service si le transfert direct de l'abonnement est impossible. Lisez les informations affichées et ne confondez pas résiliation de l'abonnement et suppression d'un service.

## Après la résiliation

En général, les avantages restent disponibles jusqu'à la fin de la période déjà payée. Vérifiez dans l'e-mail de confirmation et sur la page des abonnements que le renouvellement est arrêté et relevez la date de fin.

À la fin du stockage Google One supplémentaire, les comptes dépassant l'espace gratuit (généralement 15 Go) peuvent ne plus pouvoir envoyer ou recevoir des messages Gmail, importer ou synchroniser des fichiers Drive ni sauvegarder des photos dans Google Photos. Vérifiez l'espace utilisé avant la résiliation et libérez des fichiers si nécessaire.

## Sources officielles

* [Résilier un abonnement Google One](https://support.google.com/googleone/answer/9056360)
* [Résilier un abonnement Google Play](https://support.google.com/googleplay/answer/7018481)
* [Gérer un forfait Google AI dans Gemini](https://support.google.com/gemini/answer/14517446?hl=fr)'''
},
"pt": {
"title": "Como cancelar um plano do Google One com Google AI ou Gemini",
"description": "Saiba como cancelar um plano do Google One com Google AI ou Gemini conforme o local da assinatura. Identifique a conta e o provedor de cobrança e entenda o que acontece com o armazenamento após o cancelamento.",
"body": r'''# Como cancelar um plano do Google One com Google AI ou Gemini

Alguns recursos pagos do Gemini podem fazer parte de uma assinatura do Google One, como um plano Google AI. A disponibilidade e duração de uma avaliação gratuita, o preço e a data de renovação dependem da oferta e da região. Confira os dados na sua Conta do Google em vez de confiar em preços ou condições antigos.

O local do cancelamento depende de onde você assinou: Google One, Google Play, App Store da Apple, operadora ou outro provedor. Verifique os itens abaixo para descartar o uso da conta ou do serviço de cobrança errado.

## 1. Identifique a conta e quem faz a cobrança

Confira o e-mail de confirmação ou recibo para identificar a Conta do Google usada na compra e o provedor de cobrança. Se você usa várias contas, alterne entre elas no Google One ou Google Play. Se o administrador de um grupo familiar assinou o plano, os outros integrantes talvez não tenham acesso aos controles de gerenciamento.

## 2. Cancele no serviço usado para assinar

* **Google One:** Abra o [Google One](https://one.google.com/) com a conta da compra, acesse Configurações e escolha **Cancelar assinatura**. No Gemini, abra Configurações, selecione **Gerenciar assinaturas** e continue nas configurações do Google One.
* **Google Play:** Acesse [assinaturas do Google Play](https://play.google.com/store/account/subscriptions), selecione o plano e toque em **Cancelar assinatura**. Desinstalar um app não cancela a assinatura.
* **App Store da Apple:** No iPhone ou iPad, abra Ajustes, toque no seu nome e em **Assinaturas**; cancele o plano do Google One.
* **Operadora ou outro provedor:** Cancele na conta ou no suporte desse provedor. Em um plano familiar, fale com a pessoa que o administra.

Consulte as instruções oficiais para [cancelar o Google One](https://support.google.com/googleone/answer/9056360) e [cancelar assinaturas do Google Play](https://support.google.com/googleplay/answer/7018481). Os nomes dos menus variam conforme o dispositivo, a região e a forma de cobrança.

## Se a opção de cancelamento não aparecer

Faça login com a conta que aparece no recibo e confira qual loja ou provedor gerencia o plano. Um status como **Já cancelada** ou uma data de término pode indicar que a renovação já foi interrompida. Se não tiver certeza, confira o e-mail de confirmação e o status da assinatura ou fale com o provedor de cobrança.

A [página para excluir um serviço da Conta do Google](https://myaccount.google.com/deleteservices) não deve ser a primeira opção no lugar do cancelamento normal. O Google indica a exclusão do serviço Google One em situações específicas, como ao mudar de serviço quando não é possível transferir a assinatura diretamente. Leia a explicação exibida e não confunda o cancelamento da assinatura com a exclusão de um serviço.

## Depois do cancelamento

Em geral, os benefícios continuam disponíveis até o fim do período já pago. Confira no e-mail de confirmação e na página de assinaturas se a renovação foi interrompida e qual é a data de término.

Quando o armazenamento adicional do Google One terminar, contas acima do espaço gratuito (normalmente 15 GB) poderão ter restrições para enviar ou receber mensagens no Gmail, enviar ou sincronizar arquivos no Drive e fazer backup no Google Fotos. Confira o uso do armazenamento antes de cancelar e libere arquivos se necessário.

## Referências oficiais

* [Cancelar uma assinatura do Google One](https://support.google.com/googleone/answer/9056360)
* [Cancelar uma assinatura do Google Play](https://support.google.com/googleplay/answer/7018481)
* [Gerenciar um plano Google AI no Gemini](https://support.google.com/gemini/answer/14517446?hl=pt)'''
},
"ru": {
"title": "Как отменить план Google One с Google AI или Gemini",
"description": "Узнайте, как отменить план Google One с Google AI или Gemini в зависимости от места оформления подписки. Найдите нужный аккаунт и платёжного провайдера, а также проверьте, как отмена повлияет на хранилище.",
"body": r'''# Как отменить план Google One с Google AI или Gemini

Платные функции Gemini могут входить в подписку Google One, например в план Google AI. Наличие и длительность бесплатного пробного периода, цена и дата продления зависят от предложения и региона. Проверяйте сведения о подписке в аккаунте Google, а не ориентируйтесь на старые цены и условия.

Способ отмены зависит от места оформления: Google One, Google Play, App Store, оператор связи или другой поставщик. Проверьте пункты ниже по порядку, чтобы исключить вход не в тот аккаунт или поиск не в том сервисе оплаты.

## 1. Найдите аккаунт и платёжного провайдера

Проверьте письмо о покупке или квитанцию: там указаны аккаунт Google и поставщик, который списывает деньги. Если аккаунтов несколько, переключитесь между ними в Google One или Google Play. Если план оформил менеджер семейной группы, другие участники могут не видеть настройки подписки.

## 2. Отмените подписку там, где её оформили

* **Google One:** Откройте [Google One](https://one.google.com/) в аккаунте, с которого оформлена покупка, перейдите в настройки и выберите **Отменить подписку**. В Gemini откройте настройки, нажмите **Управление подпиской** и перейдите к настройкам Google One.
* **Google Play:** Откройте [подписки Google Play](https://play.google.com/store/account/subscriptions), выберите план и нажмите **Отменить подписку**. Удаление приложения не отменяет подписку.
* **Apple App Store:** На iPhone или iPad откройте «Настройки», нажмите на своё имя, затем **Подписки** и отмените план Google One.
* **Оператор или другой поставщик:** Отмените подписку в личном кабинете или через поддержку поставщика. По семейному плану обратитесь к его менеджеру.

Подробности есть в официальных инструкциях: [отмена Google One](https://support.google.com/googleone/answer/9056360) и [отмена подписки Google Play](https://support.google.com/googleplay/answer/7018481). Названия пунктов меню могут отличаться в зависимости от устройства, региона и способа оплаты.

## Если кнопки отмены нет

Войдите в аккаунт из квитанции и проверьте, какой магазин или поставщик управляет планом. Статус **Уже отменена** или указанная дата окончания могут означать, что продление уже остановлено. Если это неясно, проверьте письмо-подтверждение и статус подписки либо свяжитесь с поставщиком, который выставляет счёт.

[Страница удаления сервиса Google](https://myaccount.google.com/deleteservices) не предназначена для обычной отмены как первый шаг. Google описывает удаление сервиса Google One для отдельных случаев, например при переходе на другой сервис, если прямой перенос подписки невозможен. Прочитайте пояснения на странице и не путайте отмену подписки с удалением сервиса.

## После отмены

Обычно функции доступны до конца уже оплаченного расчётного периода. Проверьте письмо и страницу подписки: продление должно быть остановлено, а дата окончания указана.

После окончания дополнительного места Google One аккаунты, превышающие бесплатный лимит (обычно 15 ГБ), могут столкнуться с ограничениями: нельзя будет отправлять и получать письма Gmail, загружать и синхронизировать файлы Drive или создавать резервные копии в Google Фото. До отмены проверьте объём данных и при необходимости освободите место.

## Официальные источники

* [Отменить подписку Google One](https://support.google.com/googleone/answer/9056360)
* [Отменить подписку Google Play](https://support.google.com/googleplay/answer/7018481)
* [Управление планом Google AI в Gemini](https://support.google.com/gemini/answer/14517446?hl=ru)'''
},
"id": {
"title": "Cara Membatalkan Paket Google One dengan Google AI atau Gemini",
"description": "Pelajari cara membatalkan paket Google One yang mencakup Google AI atau Gemini sesuai tempat Anda berlangganan. Temukan akun dan penyedia tagihan yang tepat serta pahami dampaknya pada penyimpanan.",
"body": r'''# Cara Membatalkan Paket Google One dengan Google AI atau Gemini

Fitur Gemini berbayar mungkin disertakan dalam keanggotaan Google One, seperti paket Google AI. Ketersediaan dan durasi uji coba gratis, harga, serta tanggal perpanjangan bergantung pada penawaran dan wilayah. Periksa detail langganan di Akun Google Anda, bukan harga atau ketentuan uji coba dari artikel lama.

Tempat membatalkan bergantung pada tempat Anda berlangganan: Google One, Google Play, Apple App Store, operator seluler, atau penyedia lain. Periksa langkah berikut secara berurutan untuk memastikan Anda tidak memakai akun atau layanan tagihan yang keliru.

## 1. Temukan akun dan penyedia tagihan

Periksa email konfirmasi atau tanda terima untuk mengetahui Akun Google yang dipakai dan penyedia yang menagih. Jika memiliki beberapa akun, ganti akun di Google One atau Google Play. Jika pengelola grup keluarga membeli paket, anggota lain mungkin tidak melihat kontrol pengelolaan langganan.

## 2. Batalkan melalui layanan tempat Anda berlangganan

* **Google One:** Buka [Google One](https://one.google.com/) dengan akun pembelian, buka Setelan, lalu pilih **Batalkan keanggotaan**. Di Gemini, buka Setelan, pilih **Kelola langganan**, lalu lanjutkan ke setelan Google One.
* **Google Play:** Buka [langganan Google Play](https://play.google.com/store/account/subscriptions), pilih paket, lalu pilih **Batalkan langganan**. Menghapus aplikasi tidak membatalkan langganan.
* **Apple App Store:** Di iPhone atau iPad, buka Pengaturan, ketuk nama Anda, lalu **Langganan** dan batalkan paket Google One.
* **Operator atau penyedia lain:** Batalkan melalui akun atau dukungan penyedia tersebut. Untuk paket keluarga, hubungi pengelolanya.

Lihat petunjuk resmi untuk [membatalkan Google One](https://support.google.com/googleone/answer/9056360) dan [membatalkan langganan Google Play](https://support.google.com/googleplay/answer/7018481). Nama menu dapat berbeda menurut perangkat, wilayah, dan cara penagihan.

## Jika opsi pembatalan tidak ditemukan

Masuk dengan akun pada tanda terima dan periksa toko atau penyedia yang mengelola paket. Status seperti **Sudah dibatalkan** atau tanggal berakhir dapat berarti perpanjangan telah dihentikan. Jika belum jelas, periksa email konfirmasi dan status langganan, atau hubungi penyedia tagihan.

[Halaman penghapusan layanan Akun Google](https://myaccount.google.com/deleteservices) bukan pilihan pertama sebagai pengganti pembatalan biasa. Google menjelaskan penghapusan layanan Google One untuk situasi tertentu, misalnya ketika beralih layanan dan langganan tidak dapat dipindahkan secara langsung. Baca penjelasan yang tampil dan jangan samakan pembatalan keanggotaan dengan penghapusan layanan.

## Setelah membatalkan

Biasanya, manfaat tetap tersedia sampai akhir periode tagihan yang telah dibayar. Periksa email konfirmasi dan halaman langganan untuk memastikan perpanjangan berhenti dan tanggal berakhirnya.

Setelah penyimpanan tambahan Google One berakhir, akun yang melebihi penyimpanan gratis (biasanya 15 GB) mungkin tidak dapat mengirim atau menerima Gmail, mengunggah atau menyinkronkan file Drive, serta mencadangkan foto di Google Foto. Periksa penggunaan penyimpanan sebelum membatalkan dan hapus file jika perlu.

## Referensi resmi

* [Membatalkan keanggotaan Google One](https://support.google.com/googleone/answer/9056360)
* [Membatalkan langganan Google Play](https://support.google.com/googleplay/answer/7018481)
* [Mengelola paket Google AI di Gemini](https://support.google.com/gemini/answer/14517446?hl=id)'''
},
"ko": {
"title": "Google AI 또는 Gemini가 포함된 Google One 요금제 해지 방법",
"description": "가입한 경로에 따라 Google AI 또는 Gemini가 포함된 Google One 요금제를 해지하는 방법을 설명합니다. 결제 계정과 제공업체를 확인하고, 해지 메뉴가 보이지 않을 때와 저장용량 영향을 알아보세요.",
"body": r'''# Google AI 또는 Gemini가 포함된 Google One 요금제 해지 방법

유료 Gemini 기능은 Google AI 요금제와 같은 Google One 멤버십에 포함될 수 있습니다. 무료 체험 제공 여부와 기간, 가격, 갱신일은 가입한 혜택과 지역에 따라 다릅니다. 오래된 글의 가격이나 체험 조건을 기준으로 삼지 말고 Google 계정에서 구독 정보를 확인하세요.

해지 위치는 Google One, Google Play, Apple App Store, 이동통신사 등 가입 경로에 따라 다릅니다. 잘못된 계정이나 결제 서비스를 확인하는 일이 없도록 다음 순서로 살펴보세요.

## 1. 계정과 결제 제공업체 확인

가입 확인 이메일이나 영수증에서 구매에 사용한 Google 계정과 결제 업체를 확인합니다. Google 계정이 여러 개라면 Google One 또는 Google Play에서 계정을 전환하세요. 가족 그룹 관리자가 요금제를 가입했다면 다른 구성원에게 관리 메뉴가 표시되지 않을 수 있습니다.

## 2. 가입한 서비스에서 해지

* **Google One:** 구매 계정으로 [Google One](https://one.google.com/)을 열고 설정에서 **멤버십 취소**를 선택합니다. Gemini에서는 설정의 **구독 관리**를 누른 다음 Google One 설정으로 이동합니다.
* **Google Play:** [Google Play 정기 결제](https://play.google.com/store/account/subscriptions)를 열고 요금제를 선택한 뒤 **구독 취소**를 누릅니다. 앱을 삭제해도 구독은 취소되지 않습니다.
* **Apple App Store:** iPhone 또는 iPad에서 설정을 열고 이름을 탭한 다음 **구독**에서 Google One 요금제를 해지합니다.
* **통신사 또는 다른 제공업체:** 해당 업체의 계정 페이지나 고객 지원에서 해지합니다. 가족 요금제라면 관리 담당자에게 문의하세요.

자세한 내용은 Google의 [Google One 해지 안내](https://support.google.com/googleone/answer/9056360)와 [Google Play 구독 해지 안내](https://support.google.com/googleplay/answer/7018481)를 참고하세요. 메뉴 이름과 위치는 기기, 지역, 결제 방식에 따라 다를 수 있습니다.

## 해지 메뉴가 보이지 않는 경우

영수증에 표시된 계정으로 로그인했는지, 어떤 스토어나 제공업체가 요금제를 관리하는지 확인합니다. **이미 취소됨** 상태나 종료 날짜가 표시되면 갱신이 이미 중지되었을 수 있습니다. 확실하지 않으면 확인 이메일과 구독 상태를 확인하거나 결제 업체에 문의하세요.

[Google 계정 서비스 삭제 페이지](https://myaccount.google.com/deleteservices)는 일반 해지의 첫 번째 대체 경로가 아닙니다. Google은 다른 서비스로 전환할 때 정기 결제를 직접 이전할 수 없는 경우 등 특정 상황에서 Google One 서비스를 삭제하는 방법을 안내합니다. 표시되는 설명을 읽고 멤버십 해지와 서비스 삭제를 혼동하지 마세요.

## 해지한 뒤 확인할 내용

일반적으로 이미 결제한 기간이 끝날 때까지 혜택을 이용할 수 있습니다. 확인 이메일과 구독 화면에서 갱신이 중지되었는지, 종료 날짜가 언제인지 확인하세요.

Google One 추가 저장용량이 종료된 뒤 무료 저장용량(보통 15GB)을 초과해 사용 중이면 Gmail 송수신, Drive 파일 업로드·동기화, Google 포토 백업이 제한될 수 있습니다. 해지 전에 사용량을 확인하고 필요하면 파일을 정리하세요.

## 공식 자료

* [Google One 멤버십 해지](https://support.google.com/googleone/answer/9056360)
* [Google Play 구독 해지](https://support.google.com/googleplay/answer/7018481)
* [Gemini 앱에서 Google AI 요금제 관리](https://support.google.com/gemini/answer/14517446?hl=ko)'''
},
"zh-cn": {
"title": "如何取消包含 Google AI 或 Gemini 的 Google One 套餐",
"description": "根据订阅渠道，了解如何取消包含 Google AI 或 Gemini 的 Google One 套餐。确认正确的账号和扣费方，排查找不到取消选项的原因，并了解取消后存储空间的变化。",
"body": r'''# 如何取消包含 Google AI 或 Gemini 的 Google One 套餐

Gemini 付费功能可能包含在 Google One 会员中，例如 Google AI 套餐。是否提供免费试用、试用时长、价格和续订日期取决于具体优惠和地区。请在 Google 账号的订阅页面核对信息，不要依赖旧文章中的价格或试用条件。

取消入口取决于订阅渠道：Google One、Google Play、Apple App Store、移动运营商或其他服务商。请按以下顺序检查，排除账号或扣费平台不正确的情况。

## 1. 确认账号和扣费方

查看订阅确认邮件或收据，确认购买套餐所用的 Google 账号和扣费服务商。如果有多个 Google 账号，请在 Google One 或 Google Play 中切换账号。如果套餐由家庭群组管理员购买，其他成员可能看不到管理选项。

## 2. 在订阅渠道取消

* **Google One：** 使用购买套餐的账号打开 [Google One](https://one.google.com/)，进入设置并选择**取消会员资格**。在 Gemini 中可打开设置，选择**管理订阅**，再转到 Google One 设置。
* **Google Play：** 打开[Google Play 订阅](https://play.google.com/store/account/subscriptions)，选择套餐并点按**取消订阅**。卸载应用不会取消订阅。
* **Apple App Store：** 在 iPhone 或 iPad 上打开“设置”，点按姓名，再进入**订阅**取消 Google One 套餐。
* **运营商或其他服务商：** 在该服务商的账号页面或通过客服取消。家庭套餐请联系管理该套餐的人。

详细步骤请参阅 Google 的[取消 Google One 会员资格说明](https://support.google.com/googleone/answer/9056360)和[取消 Google Play 订阅说明](https://support.google.com/googleplay/answer/7018481)。菜单名称和位置可能因设备、地区和付款方式而异。

## 找不到取消选项时

请使用收据上显示的账号登录，并确认套餐由哪个商店或服务商管理。若显示**已取消**或到期日期，续订可能已经停止。如不确定，请检查确认邮件和订阅状态，或联系扣费方。

[Google 账号服务删除页面](https://myaccount.google.com/deleteservices)不是常规取消订阅的首选替代入口。Google 将删除 Google One 服务的步骤用于特定情况，例如更换服务且无法直接转移订阅。请阅读页面提示，不要将取消会员资格与删除服务混为一谈。

## 取消后

通常，已付费的会员权益会保留到当前结算周期结束。请在确认邮件和订阅页面中确认续订已停止，并查看到期日期。

Google One 额外存储空间到期后，如果账号使用量超过免费额度（通常为 15 GB），Gmail 收发邮件、Drive 上传或同步文件、Google 相册备份等功能可能受到限制。取消前请检查存储用量，必要时清理文件。

## 官方资料

* [取消 Google One 会员资格](https://support.google.com/googleone/answer/9056360)
* [取消 Google Play 订阅](https://support.google.com/googleplay/answer/7018481)
* [在 Gemini 中管理 Google AI 套餐](https://support.google.com/gemini/answer/14517446?hl=zh-CN)'''
},
"zh-tw": {
"title": "如何取消包含 Google AI 或 Gemini 的 Google One 方案",
"description": "依照訂閱管道，了解如何取消包含 Google AI 或 Gemini 的 Google One 方案。確認正確的帳戶與扣款方、排查找不到取消選項的原因，並了解取消後儲存空間的影響。",
"body": r'''# 如何取消包含 Google AI 或 Gemini 的 Google One 方案

Gemini 付費功能可能包含在 Google One 會員資格中，例如 Google AI 方案。是否提供免費試用、試用期間、價格與續訂日期，會因優惠和地區而異。請在 Google 帳戶的訂閱資料中確認，不要依賴舊文章中的價格或試用條件。

取消方式取決於訂閱管道：Google One、Google Play、Apple App Store、電信業者或其他服務供應商。請依序檢查以下項目，確認登入帳戶及扣款服務是否正確。

## 1. 確認帳戶與扣款方

查看訂閱確認電子郵件或收據，確認購買方案使用的 Google 帳戶與扣款供應商。如果有多個帳戶，請在 Google One 或 Google Play 切換帳戶。若方案由家庭群組管理員購買，其他成員可能看不到管理選項。

## 2. 從訂閱管道取消

* **Google One：** 使用購買方案的帳戶開啟 [Google One](https://one.google.com/)，前往設定並選擇**取消會員資格**。在 Gemini 中開啟設定、選擇**管理訂閱**，再前往 Google One 設定。
* **Google Play：** 開啟 [Google Play 訂閱](https://play.google.com/store/account/subscriptions)，選取方案並選擇**取消訂閱**。解除安裝應用程式不會取消訂閱。
* **Apple App Store：** 在 iPhone 或 iPad 上開啟「設定」，點選姓名，再進入**訂閱項目**取消 Google One 方案。
* **電信業者或其他供應商：** 請在該供應商的帳戶頁面或透過客服取消。家庭方案請洽詢管理方案的人。

請參閱 Google 官方的[取消 Google One 會員資格說明](https://support.google.com/googleone/answer/9056360)與[取消 Google Play 訂閱說明](https://support.google.com/googleplay/answer/7018481)。選單名稱與位置可能因裝置、地區和付款方式而異。

## 找不到取消選項時

請使用收據所列的帳戶登入，並確認方案由哪個商店或供應商管理。若狀態顯示**已取消**或有結束日期，可能已停止續訂。如有疑問，請檢查確認信與訂閱狀態，或聯絡扣款方。

[Google 帳戶服務刪除頁面](https://myaccount.google.com/deleteservices)不是一般取消訂閱的首選替代方案。Google 將刪除 Google One 服務的步驟用於特定情況，例如轉換服務且無法直接轉移訂閱。請閱讀頁面說明，不要混淆取消會員資格與刪除服務。

## 取消後

通常已付款的會員權益會保留至目前帳單週期結束。請在確認電子郵件與訂閱頁面確認續訂已停止並查看結束日期。

Google One 額外儲存空間到期後，若帳戶用量超過免費空間（通常為 15 GB），Gmail 收發郵件、Drive 上傳或同步檔案、Google 相簿備份等功能可能受限。取消前先檢查用量，必要時整理檔案。

## 官方參考資料

* [取消 Google One 會員資格](https://support.google.com/googleone/answer/9056360)
* [取消 Google Play 訂閱](https://support.google.com/googleplay/answer/7018481)
* [在 Gemini 中管理 Google AI 方案](https://support.google.com/gemini/answer/14517446?hl=zh-TW)'''
},
"hi": {
"title": "Google AI या Gemini वाले Google One प्लान को कैसे रद्द करें",
"description": "जहाँ आपने सदस्यता ली थी, उसके अनुसार Google AI या Gemini वाले Google One प्लान को रद्द करने का तरीका जानें। सही खाते और बिलिंग सेवा की पहचान करें और रद्द करने के बाद स्टोरेज पर पड़ने वाला असर समझें।",
"body": r'''# Google AI या Gemini वाले Google One प्लान को कैसे रद्द करें

Gemini की कुछ सशुल्क सुविधाएँ Google AI प्लान जैसे Google One सदस्यता में शामिल हो सकती हैं। मुफ़्त ट्रायल उपलब्ध होना, उसकी अवधि, कीमत और नवीनीकरण की तारीख ऑफ़र और क्षेत्र पर निर्भर करती है। पुराने लेखों की कीमत या ट्रायल शर्तों के बजाय अपने Google खाते में सदस्यता की जानकारी देखें।

रद्द करने की जगह इस बात पर निर्भर करती है कि आपने कहाँ से सदस्यता ली थी: Google One, Google Play, Apple App Store, मोबाइल ऑपरेटर या कोई अन्य सेवा। गलत खाता या बिलिंग सेवा देखने की संभावना जाँचने के लिए नीचे दिए चरण अपनाएँ।

## 1. खाता और बिलिंग सेवा पहचानें

पुष्टि ईमेल या रसीद देखकर पता करें कि खरीदारी में कौन-सा Google खाता इस्तेमाल हुआ और बिल कौन भेज रहा है। अगर आपके कई खाते हैं, तो Google One या Google Play में खाता बदलें। अगर परिवार समूह के मैनेजर ने प्लान लिया है, तो दूसरे सदस्यों को उसे मैनेज करने के विकल्प नहीं दिख सकते।

## 2. उसी सेवा से रद्द करें जहाँ सदस्यता ली थी

* **Google One:** खरीदारी वाले खाते से [Google One](https://one.google.com/) खोलें, सेटिंग में जाएँ और **सदस्यता रद्द करें** चुनें। Gemini में सेटिंग खोलकर **सदस्यताएँ मैनेज करें** चुनें और Google One सेटिंग पर जाएँ।
* **Google Play:** [Google Play सदस्यताएँ](https://play.google.com/store/account/subscriptions) खोलें, प्लान चुनें और **सदस्यता रद्द करें** चुनें। ऐप हटाने से सदस्यता रद्द नहीं होती।
* **Apple App Store:** iPhone या iPad पर सेटिंग खोलें, अपना नाम टैप करें, फिर **सदस्यताएँ** में Google One प्लान रद्द करें।
* **मोबाइल ऑपरेटर या अन्य सेवा:** उस सेवा की खाता साइट या सहायता टीम के ज़रिए रद्द करें। परिवार वाले प्लान के लिए उसे मैनेज करने वाले व्यक्ति से संपर्क करें।

विस्तार के लिए Google के [Google One रद्द करने के निर्देश](https://support.google.com/googleone/answer/9056360) और [Google Play सदस्यता रद्द करने के निर्देश](https://support.google.com/googleplay/answer/7018481) देखें। मेनू के नाम और जगह डिवाइस, क्षेत्र और बिलिंग तरीके के अनुसार अलग हो सकते हैं।

## रद्द करने का विकल्प न मिले तो

रसीद में दिए खाते से साइन इन करें और जाँचें कि प्लान किस स्टोर या सेवा के ज़रिए मैनेज होता है। **पहले ही रद्द** स्थिति या समाप्ति की तारीख दिखने का मतलब हो सकता है कि नवीनीकरण रुक चुका है। संदेह हो तो पुष्टि ईमेल और सदस्यता स्थिति देखें या बिल भेजने वाली सेवा से संपर्क करें।

[Google खाता सेवा हटाने वाला पेज](https://myaccount.google.com/deleteservices) सामान्य रद्दीकरण के बदले पहला विकल्प नहीं है। Google इस प्रक्रिया को खास स्थितियों के लिए बताता है, जैसे सेवा बदलते समय सदस्यता सीधे ट्रांसफ़र न हो सके। स्क्रीन पर दिए निर्देश पढ़ें और सदस्यता रद्द करने को सेवा हटाने के साथ न मिलाएँ।

## रद्द करने के बाद

आमतौर पर पहले से चुकाई गई बिलिंग अवधि के अंत तक सुविधाएँ उपलब्ध रहती हैं। पुष्टि ईमेल और सदस्यता पेज पर नवीनीकरण रुकने और समाप्ति तारीख की जाँच करें।

Google One का अतिरिक्त स्टोरेज खत्म होने पर, मुफ़्त सीमा (आमतौर पर 15 GB) से अधिक उपयोग करने वाले खातों में Gmail भेजने या पाने, Drive फ़ाइलें अपलोड या सिंक करने और Google Photos बैकअप की पाबंदियाँ लग सकती हैं। रद्द करने से पहले स्टोरेज उपयोग देखें और ज़रूरत हो तो फ़ाइलें हटाएँ।

## आधिकारिक संदर्भ

* [Google One सदस्यता रद्द करें](https://support.google.com/googleone/answer/9056360)
* [Google Play सदस्यता रद्द करें](https://support.google.com/googleplay/answer/7018481)
* [Gemini में Google AI प्लान मैनेज करें](https://support.google.com/gemini/answer/14517446?hl=hi)'''
},
"ar": {
"title": "كيفية إلغاء خطة Google One التي تتضمن Google AI أو Gemini",
"description": "تعرّف على طريقة إلغاء خطة Google One التي تتضمن Google AI أو Gemini حسب جهة الاشتراك. حدّد الحساب ومزوّد الفوترة الصحيح، وتعرّف على أثر الإلغاء في مساحة التخزين.",
"body": r'''# كيفية إلغاء خطة Google One التي تتضمن Google AI أو Gemini

قد تكون بعض ميزات Gemini المدفوعة ضمن عضوية Google One مثل خطة Google AI. يختلف توفر الفترة التجريبية المجانية ومدتها والسعر وموعد التجديد حسب العرض والمنطقة. تحقّق من تفاصيل الاشتراك في حساب Google بدلاً من الاعتماد على الأسعار أو شروط التجربة الواردة في مقالات قديمة.

تختلف جهة الإلغاء بحسب مكان الاشتراك: Google One أو Google Play أو App Store من Apple أو شركة الاتصالات أو مزوّد آخر. تحقّق من الخطوات التالية بالترتيب لاستبعاد استخدام حساب أو جهة فوترة غير صحيحة.

## 1. تحقّق من الحساب وجهة الفوترة

راجع رسالة التأكيد أو الإيصال لمعرفة حساب Google المستخدم ومزوّد الفوترة. إذا كنت تستخدم عدة حسابات، فبدّل الحساب في Google One أو Google Play. إذا اشترى مدير مجموعة العائلة الخطة، فقد لا تظهر خيارات الإدارة لبقية الأعضاء.

## 2. ألغِ الاشتراك من الخدمة التي اشتركت عبرها

* **Google One:** افتح [Google One](https://one.google.com/) بالحساب الذي أجرى الشراء، وانتقل إلى الإعدادات واختر **إلغاء العضوية**. في Gemini افتح الإعدادات، واختر **إدارة الاشتراكات**، ثم انتقل إلى إعدادات Google One.
* **Google Play:** افتح [اشتراكات Google Play](https://play.google.com/store/account/subscriptions)، واختر الخطة ثم **إلغاء الاشتراك**. لا يؤدي حذف التطبيق إلى إلغاء الاشتراك.
* **Apple App Store:** على iPhone أو iPad، افتح «الإعدادات»، واضغط على اسمك ثم **الاشتراكات**، وألغِ خطة Google One.
* **شركة اتصالات أو مزوّد آخر:** ألغِ الاشتراك من صفحة الحساب أو عبر دعم المزوّد. في الخطة العائلية، تواصل مع الشخص الذي يديرها.

للتفاصيل، راجع تعليمات Google الرسمية حول [إلغاء عضوية Google One](https://support.google.com/googleone/answer/9056360) و[إلغاء اشتراك Google Play](https://support.google.com/googleplay/answer/7018481). قد تختلف أسماء القوائم ومواقعها حسب الجهاز والمنطقة وطريقة الفوترة.

## إذا لم يظهر خيار الإلغاء

سجّل الدخول بالحساب المذكور في الإيصال، وتحقّق من المتجر أو المزوّد الذي يدير الخطة. قد تعني حالة **تم الإلغاء بالفعل** أو ظهور تاريخ انتهاء أن التجديد قد توقف. إذا لم يتضح الأمر، فراجع رسالة التأكيد وحالة الاشتراك أو تواصل مع جهة الفوترة.

صفحة [حذف خدمة من حساب Google](https://myaccount.google.com/deleteservices) ليست الخيار الأول بديلاً عن الإلغاء المعتاد. تشرح Google حذف خدمة Google One في حالات محددة، مثل الانتقال إلى خدمة أخرى عندما يتعذر نقل الاشتراك مباشرة. اقرأ المعلومات المعروضة ولا تخلط بين إلغاء العضوية وحذف الخدمة.

## بعد الإلغاء

عادةً تظل المزايا متاحة حتى نهاية فترة الفوترة المدفوعة. تحقّق من رسالة التأكيد وصفحة الاشتراك للتأكد من إيقاف التجديد ومعرفة تاريخ الانتهاء.

عند انتهاء مساحة Google One الإضافية، قد تُفرض قيود على الحسابات التي تتجاوز مساحة التخزين المجانية (عادةً 15 غيغابايت)، مثل إرسال رسائل Gmail أو استقبالها، أو تحميل الملفات ومزامنتها في Drive، أو الاحتفاظ بنسخة احتياطية في Google Photos. تحقّق من استخدام المساحة قبل الإلغاء ونظّف الملفات عند الحاجة.

## مراجع رسمية

* [إلغاء عضوية Google One](https://support.google.com/googleone/answer/9056360)
* [إلغاء اشتراك Google Play](https://support.google.com/googleplay/answer/7018481)
* [إدارة خطة Google AI في Gemini](https://support.google.com/gemini/answer/14517446?hl=ar)'''
},
}

for language, data in EDITION.items():
    path = ARTICLE / f"index.{language}.md"
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    assert len(parts) == 3, path
    old = parts[1].splitlines()
    metadata = [line for line in old if not re.match(r"^(title|date|lastmod|description):", line)]
    quote = lambda value: "'" + value.replace("'", "''") + "'"
    front = "\n".join([
        f"title: {quote(data['title'])}",
        "date: 2025-09-27T10:02:59+09:00",
        "lastmod: 2026-11-23",
        *metadata,
        f"description: {quote(data['description'])}",
    ])
    path.write_text("---\n" + front + "\n---\n\n" + data["body"].strip() + "\n", encoding="utf-8")
    print(f"Updated {path.relative_to(ROOT)}")

import hashlib
import json

def digest(path):
    return hashlib.sha256(path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").encode("utf-8")).hexdigest()

source_path = ARTICLE / "index.md"
source_key = source_path.relative_to(ROOT / "content").as_posix()
checks = {
    "meaning": {"status": "checked", "note": "Read the complete Japanese source and localized article. Compared eligibility and variability caveats, account and billing-provider selection, cancellation paths, the limited service-deletion scenario, cancellation status, billing period, and storage consequences."},
    "terminology": {"status": "checked", "note": "Reviewed localized terminology for Google One membership, Google AI plan, Gemini, free trial, renewal, billing provider, family group manager, service deletion, storage allowance, and cancellation."},
    "mathematics": {"status": "not_applicable", "note": "No mathematical claims or calculations are included. The 15 GB free storage reference is a product allowance, not a calculation."},
    "code": {"status": "not_applicable", "note": "The article contains no code or executable commands."},
    "links": {"status": "checked", "note": "Compared Google One cancellation, Google Play cancellation, Gemini subscription management, and Google One service-deletion guidance with Google's official help pages. The linked routes and limits are explained in context."},
}
reviews = {}
for language in EDITION:
    translation_path = ARTICLE / f"index.{language}.md"
    translation_key = translation_path.relative_to(ROOT / "content").as_posix()
    reviews[translation_key] = {
        "reviewKind": "ai",
        "reviewedAt": "2026-11-23",
        "reviewer": "Codex (AI)",
        "source": source_key,
        "sourceHash": digest(source_path),
        "translationHash": digest(translation_path),
        "checks": checks,
        "summary": "Replaced outdated trial and fixed-price assertions with current account-specific guidance, routed cancellation by signup and billing provider, limited the Google service-deletion route to documented cases, and explained post-cancellation storage effects.",
        "limitations": [
            "AI review only; no human or native-speaker confirmation.",
            "No account-specific subscription, payment, cancellation, or refund status was accessed.",
            "Plan names, prices, trial eligibility, menus, and storage rules may vary by region and account; check the current account and official help pages.",
        ],
    }

batch = {
    "version": 1,
    "article": ARTICLE.name,
    "frozenSourceHash": digest(source_path),
    "reviewedAt": "2026-11-23",
    "sources": [
        "https://support.google.com/googleone/answer/9056360",
        "https://support.google.com/googleplay/answer/7018481",
        "https://support.google.com/gemini/answer/14517446?hl=ja",
        "https://myaccount.google.com/deleteservices",
        "https://gemini.google/jp/subscriptions/?hl=ja",
    ],
    "findings": [
        "Removed the blanket one-month trial and JPY 2,900 price claim; Google's current Japanese plan display and help center show that offers and terms must be checked for the subscriber's account and region.",
        "Explained cancellation by original signup and billing provider: Google One, Google Play, Apple App Store, carrier/other provider, or family plan manager.",
        "Corrected the claim that the official cancellation page may fail; limited service deletion to Google's documented special cases such as a non-transferable subscription during a service switch.",
        "Added confirmation-status and billing-period checks plus the storage and service restrictions that may follow loss of paid storage.",
        "Preserved the original publication date 2025-09-27, removed duplicate injected dates, and set lastmod 2026-11-23 in all 13 editions.",
    ],
    "validation": "docs/translation-review/validation-078.json",
    "scope": "Read the full Japanese source and each of twelve complete translations. Checked current Google One/Google Play/Gemini cancellation routes, the narrowly scoped service-deletion path, billing period, and storage effects against official Google documentation.",
    "publicationPending": True,
    "reviews": reviews,
}
(ROOT / "docs/translation-review/batch-078.json").write_text(json.dumps(batch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

static = {
    "version": 1,
    "article": ARTICLE.name,
    "checkedAt": "2026-11-23",
    "editions": {},
    "criteria": [
        "13 language editions retain one original date and include lastmod 2026-11-23.",
        "Each translation follows the same cancellation workflow and includes three official Google help links, no fixed trial duration or price claim, and localized guidance for signup channel, missing controls, service deletion, and post-cancellation storage.",
        "All twelve translation hashes match the review evidence.",
    ],
    "limitations": ["Static content review; no account-specific billing flow was exercised.", "No human or native-speaker review has been recorded."],
}
for edition in ["index.md", *(f"index.{language}.md" for language in EDITION)]:
    path = ARTICLE / edition
    text = path.read_text(encoding="utf-8")
    assert text.count("date:") == 1 and "lastmod: 2026-11-23" in text, edition
    assert text.count("support.google.com/googleone/answer/9056360") >= 2, edition
    assert text.count("support.google.com/googleplay/answer/7018481") >= 2, edition
    assert text.count("support.google.com/gemini/answer/14517446") >= 1, edition
    assert "2,900" not in text and "2.900" not in text and "2900" not in text, edition
    assert "1-month free trial" not in text and "1か月間の無償体験" not in text, edition
    static["editions"][edition] = {"sha256": digest(path), "bytes": path.stat().st_size}
(ROOT / "docs/translation-review/validation-078.json").write_text(json.dumps(static, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("Wrote B078 review evidence and static validation.")
