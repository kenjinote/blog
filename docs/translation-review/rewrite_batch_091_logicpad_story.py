"""Correct the LogicPad origin story's links, dating, and temporal framing."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/LogicPad 開発秘話"
TODAY = "2026-11-24"
LANGS = ("ja", "ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")

TITLES = {
    "en": "The Story Behind LogicPad: Why I Built This Low-Code Tool",
    "de": "Die Geschichte hinter LogicPad: Warum ich das Low-Code-Tool entwickelt habe",
    "es": "La historia detrás de LogicPad: por qué creé esta herramienta low-code",
    "pt": "A história por trás do LogicPad: por que criei esta ferramenta low-code",
    "ru": "История создания LogicPad: почему я разработал этот low-code-инструмент",
}

CONCLUSION = {
    "ja": "この記事を公開した2025年7月の時点では、LogicPadはまだベータ版で、開発を続けていました。\n改善したい点や、これから追加したい機能もたくさんありました。\n現在の機能や提供状況は[公式サイト](https://logicpad.org)で確認できます。",
    "en": "When this article was published in July 2025, LogicPad was still in beta and development was ongoing.\nThere were many things I wanted to improve and features I hoped to add.\nFor current features and availability, see the [official site](https://logicpad.org).",
    "es": "Cuando se publicó este artículo, en julio de 2025, LogicPad todavía estaba en fase beta y su desarrollo continuaba.\nHabía muchas cosas que quería mejorar y funciones que esperaba añadir.\nPara conocer las funciones y la disponibilidad actuales, consulta el [sitio oficial](https://logicpad.org).",
    "fr": "À la publication de cet article, en juillet 2025, LogicPad était encore en version bêta et son développement se poursuivait.\nIl restait beaucoup de choses que je voulais améliorer et de fonctions que j’espérais ajouter.\nPour connaître les fonctions et la disponibilité actuelles, consultez le [site officiel](https://logicpad.org).",
    "de": "Als dieser Artikel im Juli 2025 veröffentlicht wurde, befand sich LogicPad noch in der Beta-Phase und die Entwicklung lief weiter.\nEs gab vieles, das ich verbessern und künftig ergänzen wollte.\nAktuelle Funktionen und Informationen zur Verfügbarkeit finden Sie auf der [offiziellen Website](https://logicpad.org).",
    "pt": "Quando este artigo foi publicado, em julho de 2025, o LogicPad ainda estava em versão beta e seu desenvolvimento continuava.\nHavia muitas coisas que eu queria melhorar e recursos que esperava acrescentar.\nPara ver os recursos e a disponibilidade atuais, consulte o [site oficial](https://logicpad.org).",
    "id": "Saat artikel ini diterbitkan pada Juli 2025, LogicPad masih dalam versi beta dan pengembangannya terus berjalan.\nMasih banyak hal yang ingin saya perbaiki dan fitur yang ingin saya tambahkan.\nUntuk melihat fitur dan ketersediaan terkini, kunjungi [situs resmi](https://logicpad.org).",
    "ko": "이 글을 2025년 7월에 공개했을 당시 LogicPad는 아직 베타 버전이었고 개발이 계속 진행 중이었습니다.\n개선하고 싶은 점과 앞으로 추가하고 싶은 기능이 많이 남아 있었습니다.\n현재 기능과 제공 여부는 [공식 사이트](https://logicpad.org)에서 확인할 수 있습니다.",
    "hi": "जुलाई 2025 में जब यह लेख प्रकाशित हुआ था, तब LogicPad बीटा संस्करण में था और उसका विकास जारी था।\nकई सुधार बाकी थे और कई सुविधाएँ थीं जिन्हें मैं आगे जोड़ना चाहता था।\nवर्तमान सुविधाओं और उपलब्धता के लिए [आधिकारिक साइट](https://logicpad.org) देखें।",
    "ru": "Когда эта статья вышла в июле 2025 года, LogicPad еще находился в бета-версии, и разработка продолжалась.\nОставалось многое улучшить и добавить.\nАктуальные функции и сведения о доступности смотрите на [официальном сайте](https://logicpad.org).",
    "zh-cn": "本文于 2025 年 7 月发布时，LogicPad 仍处于测试阶段，开发工作还在继续。\n当时还有许多需要改进的地方，也有不少我想添加的功能。\n当前功能和提供情况请查看[官方网站](https://logicpad.org)。",
    "zh-tw": "本文於 2025 年 7 月發布時，LogicPad 仍處於 Beta 階段，開發工作還在持續。\n當時還有許多需要改善的地方，也有不少我想新增的功能。\n目前的功能與提供情況請參閱[官方網站](https://logicpad.org)。",
    "ar": "عند نشر هذا المقال في يوليو 2025، كان LogicPad لا يزال في المرحلة التجريبية، وكان تطويره مستمرًا.\nكان هناك الكثير مما أردت تحسينه والميزات التي رغبت في إضافتها.\nللاطلاع على الميزات والتوافر الحاليين، راجع [الموقع الرسمي](https://logicpad.org).",
}

BONUS = {
    "ja": "### 👇おまけ：記事公開当時のLogicPadでできたこと",
    "en": "### 👇 Bonus: What LogicPad Could Do at the Time of Publication",
    "es": "### 👇 Extra: Lo que LogicPad podía hacer cuando se publicó este artículo",
    "fr": "### 👇 Bonus : Ce que LogicPad pouvait faire à la publication de cet article",
    "de": "### 👇 Bonus: Was LogicPad zum Zeitpunkt der Veröffentlichung konnte",
    "pt": "### 👇 Bônus: O que o LogicPad fazia quando este artigo foi publicado",
    "id": "### 👇 Bonus: Kemampuan LogicPad saat artikel ini diterbitkan",
    "ko": "### 👇 보너스: 이 글을 공개할 당시 LogicPad로 할 수 있던 일",
    "hi": "### 👇 बोनस: लेख प्रकाशित होने के समय LogicPad से क्या किया जा सकता था",
    "ru": "### 👇 Бонус: возможности LogicPad на момент публикации статьи",
    "zh-cn": "### 👇 补充：本文发布时 LogicPad 可以实现的功能",
    "zh-tw": "### 👇補充：本文發布時 LogicPad 可以做到的事",
    "ar": "### 👇 إضافة: ما كان LogicPad يتيحه عند نشر هذا المقال",
}

def update(language):
    path = BUNDLE / ("index.md" if language == "ja" else f"index.{language}.md")
    text = path.read_text(encoding="utf-8-sig")
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise ValueError(f"Missing front matter: {path}")
    front, body = match.group(1), text[match.end():]
    front = re.sub(r'(?m)^date: "2026-09-24T19:44:38\+09:00"\n', "", front)
    front = re.sub(r"(?m)^lastmod:.*\n?", "", front)
    dates = re.findall(r"(?m)^date:\s*(.*?)\s*$", front)
    if len(dates) != 1 or "2025-07-30T23:51:35+09:00" not in dates[0]:
        raise ValueError(f"Unexpected publication date in {path}: {dates}")
    if language in TITLES:
        front = re.sub(r"(?m)^title:.*$", "title: " + json.dumps(TITLES[language], ensure_ascii=False), front, count=1)
    lines = body.splitlines()
    bonus_index = next((i for i, line in enumerate(lines) if line.startswith("###") and "👇" in line), None)
    if bonus_index is None:
        raise ValueError(f"Missing bonus section: {path}")
    conclusion_index = next((i for i in range(bonus_index - 1, -1, -1) if lines[i].startswith("## ")), None)
    if conclusion_index is None:
        raise ValueError(f"Missing conclusion section: {path}")
    first = conclusion_index + 1
    while first < bonus_index and not lines[first].strip():
        first += 1
    end = first
    while end < bonus_index and lines[end].strip():
        end += 1
    lines[first:end] = CONCLUSION[language].splitlines()
    bonus_index = next(i for i, line in enumerate(lines) if line.startswith("###") and "👇" in line)
    lines[bonus_index] = BONUS[language]
    body = "\n".join(lines)
    if language == "es":
        body = body.replace("[Pod](https://kenji.blog/es/p/kubernetes-k8s-architecture-pod-service-ingress/)ían", "Podían")
    if language == "hi":
        body = body.replace("[LogicPad](/hi/p/logicpad-windows-app-development-journey/)", "[LogicPad](https://logicpad.org)")
    front += f"\nlastmod: {TODAY}T00:00:00+09:00"
    path.write_text("---\n" + front + "\n---\n\n" + body.rstrip() + "\n", encoding="utf-8")

for lang in LANGS:
    update(lang)
print("Updated LogicPad origin story in thirteen editions")
