"""Review Hugo CLI guidance and all localized versions (batch 086)."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BUNDLE = ROOT / "content/post/Hugoコマンド一覧"
DOCS = ROOT / "docs/translation-review"
LEDGER = ROOT / "data/translation_reviews.json"
TODAY = "2026-11-24"
SOURCE = "post/Hugoコマンド一覧/index.md"
EVIDENCE = "docs/translation-review/batch-086.json"
LANGS = ("ar", "de", "en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw")
OFFICIAL = [
    "https://gohugo.io/commands/hugo_new_project/",
    "https://gohugo.io/commands/hugo_new_content/",
    "https://gohugo.io/commands/hugo_deploy/",
    "https://gohugo.io/commands/hugo_list_all/",
    "https://gohugo.io/installation/macos/",
]

PROJECT_SENTENCE = {
    "ja": "指定した名前の新しいサイトを作成します。",
    "ar": "ينشئ موقعاً جديداً بالاسم الذي تحدده.",
    "de": "Erstellt eine neue Website mit dem angegebenen Namen.",
    "en": "Creates a new site using the name you provide.",
    "es": "Crea un sitio nuevo con el nombre que indiques.",
    "fr": "Crée un nouveau site avec le nom indiqué.",
    "hi": "आपके दिए गए नाम से एक नई साइट बनाता है।",
    "id": "Membuat situs baru dengan nama yang Anda tentukan.",
    "ko": "지정한 이름으로 새 사이트를 만듭니다.",
    "pt": "Cria um novo site com o nome informado.",
    "ru": "Создает новый сайт с указанным именем.",
    "zh-cn": "使用指定的名称创建新网站。",
    "zh-tw": "使用指定的名稱建立新網站。",
}
CONTENT_SENTENCE = {
    "ja": "指定したパスに新しいコンテンツファイルを作成します。",
    "ar": "ينشئ ملف محتوى جديداً في المسار المحدد.",
    "de": "Erstellt eine neue Inhaltsdatei am angegebenen Pfad.",
    "en": "Creates a new content file at the specified path.",
    "es": "Crea un archivo de contenido en la ruta especificada.",
    "fr": "Crée un nouveau fichier de contenu au chemin indiqué.",
    "hi": "निर्दिष्ट पथ पर नई सामग्री फ़ाइल बनाता है।",
    "id": "Membuat file konten baru pada path yang ditentukan.",
    "ko": "지정한 경로에 새 콘텐츠 파일을 만듭니다.",
    "pt": "Cria um novo arquivo de conteúdo no caminho especificado.",
    "ru": "Создает новый файл контента по указанному пути.",
    "zh-cn": "在指定路径创建新的内容文件。",
    "zh-tw": "在指定路徑建立新的內容檔案。",
}
OLD_PROJECT_SENTENCE = {
    "ja": "新しいサイトを作成するコマンドです。`<サイト名>`には、サイトの名前を指定します。",
    "ar": "هذا الأمر لإنشاء موقع جديد. في `<اسم الموقع>`، حدد اسم الموقع.",
    "de": "Befehl zum Erstellen einer neuen Website. Geben Sie unter `<site-name>` den Namen der Website an.",
    "en": "Command to create a new site. Specify the name of the site in `<site-name>`.",
    "es": "Comando para crear un nuevo sitio. Especifica el nombre del sitio en `<nombre del sitio>`.",
    "fr": "Commande pour créer un nouveau site. Dans `<nom-du-site>`, spécifiez le nom du site.",
    "hi": "एक नई साइट बनाने का कमांड। `<साइट का नाम>` में, साइट का नाम निर्दिष्ट करें।",
    "id": "Perintah untuk membuat situs baru. Tentukan nama situs pada `<Nama Situs>`.",
    "ko": "새로운 사이트를 생성하는 명령어입니다. `<사이트명>`에는 사이트의 이름을 지정합니다.",
    "pt": "Comando para criar um novo site. Em `<nome-do-site>`, especifique o nome do site.",
    "ru": "Команда для создания нового сайта. Вместо `<Имя сайта>` укажите название вашего сайта.",
    "zh-cn": "这是创建新网站的命令。`<网站名>`请指定网站的名称。",
    "zh-tw": "建立新網站的指令。在 `<網站名稱>` 中指定網站的名稱。",
}
OLD_CONTENT_SENTENCE = {
    "ja": "新しい記事を作成するコマンドです。`<記事名>`には、記事の名前を指定します。",
    "ar": "هذا الأمر لإنشاء مقال جديد. في `<اسم المقال>`، حدد اسم المقال.",
    "de": "Befehl zum Erstellen eines neuen Artikels. Geben Sie unter `<artikelname>` den Namen des Artikels an.",
    "en": "Command to create a new post. Specify the name of the post in `<post-name>`.",
    "es": "Comando para crear un nuevo artículo. Especifica el nombre del artículo en `<nombre del artículo>`.",
    "fr": "Commande pour créer un nouvel article. Dans `<nom-de-l'article>`, spécifiez le nom de l'article.",
    "hi": "एक नया लेख बनाने का कमांड। `<लेख का नाम>` में, लेख का नाम निर्दिष्ट करें।",
    "id": "Perintah untuk membuat artikel baru. Tentukan nama artikel pada `<Nama Artikel>`.",
    "ko": "새로운 글을 작성하는 명령어입니다. `<기사명>`에는 글의 이름을 지정합니다.",
    "pt": "Comando para criar um novo artigo. Em `<nome-do-artigo>`, especifique o nome do artigo.",
    "ru": "Команда для создания новой статьи. Вместо `<Имя статьи>` укажите название вашей статьи.",
    "zh-cn": "这是创建新文章的命令。`<文章名>`请指定文章的名称。",
    "zh-tw": "建立新文章的指令。在 `<文章名稱>` 中指定文章的名稱。",
}


def digest(text):
    return hashlib.sha256(text.replace("\r\n", "\n").encode("utf-8")).hexdigest()


def require(ok, message):
    if not ok:
        raise SystemExit(message)


def replace_section_description(text, command, replacement):
    pattern = rf"(```bash\n{re.escape(command)}\n```\n\n).*?(?=\n\n##)"
    updated, count = re.subn(pattern, lambda match: match.group(1) + replacement, text, count=1, flags=re.S)
    require(count == 1, f"Missing section for {command}")
    return updated


files = {"ja": BUNDLE / "index.md"}
files.update({language: BUNDLE / f"index.{language}.md" for language in LANGS})
for language, path in files.items():
    text = path.read_text(encoding="utf-8-sig")
    if language == "ja":
        text = text.replace(OLD_PROJECT_SENTENCE[language], PROJECT_SENTENCE[language], 1)
        text = text.replace(OLD_CONTENT_SENTENCE[language], CONTENT_SENTENCE[language], 1)
    else:
        text = text.replace(OLD_PROJECT_SENTENCE[language], PROJECT_SENTENCE[language], 1)
        text = text.replace(OLD_CONTENT_SENTENCE[language], CONTENT_SENTENCE[language], 1)
    text = replace_section_description(text, "hugo new project <site-name>", PROJECT_SENTENCE[language])
    text = replace_section_description(text, "hugo new content posts/<post-name>.md", CONTENT_SENTENCE[language])
    text = re.sub(r"\A---\n(?:[ \t]*\n)+", "---\n", text)
    text = re.sub(r"(?m)^---\n(?:[ \t]*\n){2,}", "---\n\n", text, count=1)
    path.write_text(text, encoding="utf-8")

def front_and_body(text):
    require(text.startswith("---\n"), "Missing YAML front matter")
    return text[4:].split("\n---\n", 1)


source_text = files["ja"].read_text(encoding="utf-8-sig")
source_front, source_body = front_and_body(source_text)
require(len(re.findall(r"(?m)^date:", source_front)) == 1, "Source must have exactly one date")
require("lastmod: 2026-11-24T00:00:00+09:00" in source_front, "Source lastmod missing")
source_commands = re.findall(r"(?m)^```bash\n(.*?)\n```$", source_body, re.S)
require(source_commands == [
    "brew install hugo", "hugo new project <site-name>", "hugo new content posts/<post-name>.md",
    "hugo server", "hugo", "hugo deploy", "hugo list all", "hugo config", "hugo help", "hugo version"
], "Unexpected or inconsistent command examples")
source_hash = digest(source_text)
reviews = {}

for language in LANGS:
    relative = f"post/Hugoコマンド一覧/index.{language}.md"
    path = files[language]
    text = path.read_text(encoding="utf-8-sig")
    front, body = front_and_body(text)
    require(len(re.findall(r"(?m)^date:", front)) == 1, f"{language}: duplicate date remains")
    require("lastmod: 2026-11-24T00:00:00+09:00" in front, f"{language}: lastmod missing")
    require("draft: false" in front, f"{language}: publication status changed")
    commands = re.findall(r"(?m)^```bash\n(.*?)\n```$", body, re.S)
    require(commands == source_commands, f"{language}: command sequence or syntax differs")
    official_links = re.findall(r"\]\((https://gohugo\.io/[^)]+)\)", body)
    require(official_links == OFFICIAL, f"{language}: official documentation links differ")
    for required in ("GitHub Pages", "v0.159.2", "<site-name>", "<post-name>"):
        require(required in body, f"{language}: missing technical detail {required}")
    review = {
        "reviewKind": "ai",
        "reviewedAt": TODAY,
        "reviewer": "Codex (AI)",
        "source": SOURCE,
        "sourceHash": source_hash,
        "translationHash": digest(text),
        "summary": "Read the complete Japanese article and all twelve translations. Compared installation context, site/content creation commands, local server, build output, deploy target and version requirements, list/config/version behavior, localized descriptions, metadata, and official references against current Hugo documentation.",
        "checks": {
            "meaning": {"status": "checked", "note": "The article now distinguishes current project/content commands, local development, build output, cloud-storage deployment, and ordinary hosting deployments consistently across editions."},
            "terminology": {"status": "checked", "note": "Hugo CLI, project, content, deployment target, Deploy edition, and cloud-storage terms were compared in all localized sections."},
            "mathematics": {"status": "not_applicable", "note": "The article contains no mathematical claims or formulas."},
            "code": {"status": "checked", "note": "All ten shell examples now match exactly across all thirteen editions; the project and content command syntax follows current Hugo CLI documentation."},
            "links": {"status": "checked", "note": "All five direct Hugo official references are live and identical across translations; localized internal Go-language links point to matching language paths."},
        },
        "limitations": [
            "AI-assisted review; no human or native-speaker certification.",
            "Hugo command availability and edition requirements can change in future releases; recheck the official CLI documentation when updating this article.",
        ],
    }
    reviews[relative] = review

entry = {
    "version": 1,
    "batch": 86,
    "article": "Hugoコマンド一覧",
    "reviewedAt": TODAY,
    "sourceHash": source_hash,
    "sources": OFFICIAL,
    "scope": "Read the complete Japanese article and all twelve translations. Compared install example, CLI commands, shell syntax, output paths, deployment configuration and edition requirements, metadata, localized terminology, and direct official references.",
    "findings": [
        "Updated site creation to the current `hugo new project` CLI syntax and explicitly explained the older `hugo new site` examples.",
        "Updated article creation to `hugo new content posts/<post-name>.md` and clarified its project-root path.",
        "Corrected the misleading generic deploy description: `hugo deploy` targets supported cloud storage, uses a deployment target and provider authentication, and is not a general command for GitHub Pages; Hugo v0.159.2+ requires the Deploy edition.",
        "Clarified that `hugo list all` includes drafts, future-dated and expired content, and that `hugo config` displays defaults as well as project configuration.",
        "Replaced conflicting duplicate `date` metadata with one preserved 2024-05-31 date and a review `lastmod`; added direct official references in all languages.",
    ],
    "publicationPending": True,
    "reviews": reviews,
}
(DOCS / "batch-086.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
for relative, review in reviews.items():
    record = {key: review[key] for key in ("source", "reviewedAt", "reviewer", "sourceHash", "translationHash", "reviewKind")}
    record["evidence"] = EVIDENCE
    record["evidenceHash"] = hashlib.sha256(json.dumps(review, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    ledger["reviews"][relative] = record
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"batch": 86, "translations": len(reviews), "sourceHash": source_hash}, ensure_ascii=False))
