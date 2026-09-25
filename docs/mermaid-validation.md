# Mermaid図の一括検査と修正

サイトで利用する **Mermaid 11.12.2** を実ブラウザーで動かし、構文解析に加えてSVGの生成・表示サイズ・エラー表示の有無を検査します。HugoのビルドだけではMermaidの構文エラーを検出できません。

## 今回の対応

- 全言語のMermaidコードフェンスとMermaidショートコードを検査。
- エラーが出た図に限定して、グループ名・ラベルの引用符、ノードID、矢印、図の種類に対応した記法などを修正。
- 状態図の表示名・遷移時の説明、チャートの数値、ガントチャートの期間を保持。
- Mermaidの旧版と現行版を重複して読み込む経路を統一。ショートコードも同じローダーを使い、図のソースをHTMLとして解釈しないようエスケープ。
- 記事の保存時はMermaidの内側のみを置換し、本文・数式・その他のコード・フロントマター・改行形式を保持。並行編集を検知した場合は書き込み前に停止。

修正件数と検証結果は `mermaid-repair-report.json` に記録します。

## 再検査

Python 3、Node.js、Playwright、Microsoft Edgeが必要です。作業用ディレクトリに、サイトと同じバージョンのMermaidライブラリを用意してください。

```powershell
$auditDir = Join-Path $env:TEMP 'kenji-mermaid-audit'
New-Item -ItemType Directory -Force $auditDir
Invoke-WebRequest 'https://cdn.jsdelivr.net/npm/mermaid@11.12.2/dist/mermaid.min.js' -OutFile "$auditDir/mermaid.min.js"

# PLAYWRIGHT_MODULEには、利用するplaywrightパッケージの絶対パスを指定する。
python -B scripts/mermaid_sources.py "$auditDir/inventory.json"
node scripts/check_mermaid.mjs "$auditDir/inventory.json" "$auditDir/results.json" "$auditDir/mermaid.min.js" PLAYWRIGHT_MODULE --render

python -B -m unittest discover -s scripts -p test_mermaid_repairs.py -v
hugo --renderToMemory
```

`--render` を付けると構文解析だけでなくSVG描画まで確認します。エラーが残る場合は終了コード1となり、JSONに記事・図の番号・エラー理由を記録します。検査途中の結果も保存します。中断後は `--resume` を追加すると、ソースのSHA-256が一致する検査結果だけを再利用します。

`mermaid_sources.py` は他言語のコードフェンス内にあるMermaidの記述例を実際の図として扱いません。既存記事の構造に対応した抽出器で、任意のMarkdown方言に対応する汎用パーサーではありません。

## 修正候補の作成と適用

```powershell
python -B scripts/repair_mermaid.py "$auditDir/inventory.json" "$auditDir/results.json" "$auditDir/proposals.json"
node scripts/check_mermaid.mjs "$auditDir/proposals.json" "$auditDir/verified.json" "$auditDir/mermaid.min.js" PLAYWRIGHT_MODULE --render

# 差分を確認した修正案を適用する。
python -B scripts/repair_mermaid.py "$auditDir/inventory.json" "$auditDir/results.json" "$auditDir/proposals.json" --apply "$auditDir/verified.json"
```

修正器は今回確認したエラーパターン向けです。未知の構文を無条件で正しく修復するものではありません。適用には、修正案のソースSHA-256と一致するSVG描画成功結果が必要です。構文検査だけの結果や古い結果では適用できません。

実サイトとの統合確認には `check_mermaid_pages.mjs` を使えます。Hugoで生成したHTMLをローカルHTTPサーバーで配信し、図を含む各ページを開いて、期待した図数のSVGとMermaidローダーが1つだけ存在することを検証します。

```powershell
node scripts/check_mermaid_pages.mjs SITE_DIRECTORY http://127.0.0.1:8767/ REPORT_PATH PLAYWRIGHT_MODULE
```

参照：[Mermaid公式のフローチャート記法](https://mermaid.js.org/syntax/flowchart.html)、[状態図](https://mermaid.js.org/syntax/stateDiagram.html)、[XYチャート](https://mermaid.js.org/syntax/xyChart.html)。最新のドキュメントとサイトの固定バージョンに差がある可能性があるため、判定には固定バージョンの実描画結果を使います。
