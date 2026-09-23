
$articles = @("history-of-nvidia", "history-of-alibaba", "history-of-nec", "history-of-panasonic", "history-of-ibm")
$langs = @("en", "es", "fr", "hi", "id", "ko", "pt", "ru", "zh-cn", "zh-tw", "de", "ar")

$json = "{ `"Subagents`": ["
foreach ($article in $articles) {
    foreach ($lang in $langs) {
        $json += "{`"TypeName`":`"translator`", `"Role`":`"Translate $article to $lang`", `"Prompt`":`"Translate c:\\work\\kenji.blog\\content\\post\\$article\\index.md to $lang. Save as index.$lang.md in the same dir. Rules: 1. DO NOT translate categories and tags. 2. Enclose Mermaid nodes in double quotes.`"},"
    }
}
$json = $json.Substring(0, $json.Length - 1)
$json += "] }"
$json | Out-File -Encoding utf8 subagents2.json

