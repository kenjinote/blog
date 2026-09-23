import os
import glob
import json

targets = [
    "biography-steve-jobs", "biography-bill-gates", "biography-linus-torvalds",
    "biography-dennis-ritchie", "biography-alan-kay", "biography-edsger-dijkstra",
    "biography-donald-knuth", "biography-guido-van-rossum", "biography-mark-zuckerberg",
    "biography-marc-andreessen", "biography-frederick-brooks", "biography-martin-fowler",
    "biography-steve-mcconnell", "biography-car-hoare", "biography-harold-abelson"
]

langs = ["en", "zh-cn", "zh-tw", "es", "hi", "ar", "fr", "ru", "pt", "id", "de", "ko"]
post_dir = "C:/work/kenji.blog/content/post"

subagents = []

for target in targets:
    for lang in langs:
        base_file = f"{post_dir}/{target}/index.md"
        out_file = f"{post_dir}/{target}/index.{lang}.md"
        if not os.path.exists(out_file):
            prompt = f"""
あなたはプロの翻訳者です。
{base_file} の内容を読み込み、言語コード '{lang}' に翻訳して {out_file} に write_to_file してください。
【必須ルール】
1. フロントマターの categories と tags は絶対に翻訳せず、元の英語（小文字ハイフン区切り）のまま維持すること！
2. Mermaid図解の翻訳時、ノード内のテキストは必ずダブルクォートで囲むこと。二重ネストは禁止（例: A["Translated Text"]）。
3. 数式がある場合は Block math は $$ ... $$、改行は \\\\ とすること。
"""
            subagents.append({
                "Model": "flash",
                "Role": f"Translator {lang} for {target}",
                "TypeName": "self",
                "Prompt": prompt
            })

with open("translation_batch.json", "w", encoding="utf-8") as f:
    json.dump(subagents, f, indent=2, ensure_ascii=False)

print(f"Prepared {len(subagents)} translation tasks.")
