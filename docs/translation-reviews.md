# 翻訳の校閲と更新追随

記事の言語切り替えと hreflang は Hugo の `AllTranslations` を共通の対応元とする。翻訳のない言語を選んでも現在の記事から移動せず、その言語のホームへのリンクを案内する。見出しは言語により構成・ID が異なるため、切り替え先は対応記事の先頭とする。

タグ・カテゴリでは、異なる用語が同じ公開 URL に正規化される場合がある。いずれかの言語でこの衝突があるグループは対応が曖昧なため、全言語で自分自身だけを指定し、他言語への切り替えは未翻訳時と同じ案内にする。衝突しないグループと記事は通常どおり翻訳先へ移動できる。用語の表記統一または明示的な別 URL で衝突を解消すると、翻訳の対応も自動的に戻る。

## 校閲台帳

`data/translation_reviews.json` で最終確認日、担当者、原文パス、確認した原文と翻訳の SHA-256 を記録する。改行コードだけの差は無視し、本文・タイトル・説明・日付などファイルの変更を検出する。台帳の初期状態は未確認であり、既存の自動翻訳や作成日を人による校閲日として扱わない。

`reviewKind` は `ai`（AI校閲）または `human`（人による校閲）。CSV の `humanConfirmed` でも区別する。`current` は確認したファイルの版と一致するという意味であり、人による確認済みを意味しない。AI校閲の後に対象言語に堪能な人が確認した際は、新しい人の校閲記録として保存する。

AI校閲では、本文を全体まで原文と照合したうえで、`docs/translation-review/` に翻訳ごとの根拠を保存する。意味、用語、数式、コード、リンクの全項目について、確認内容または該当なしの理由、修正点、残る制限を記述する。構文チェックや数式の文字列一致だけで意味照合を完了扱いにしない。記録時に根拠と台帳の原文・翻訳の版を照合し、不完全な根拠や古い版では記録を拒否する。

```powershell
python scripts/translation_reviews.py check
python scripts/translation_reviews.py report --language en --output translation-review-en.csv
```

CSV の `status` は次のいずれかになる。

| 状態 | 意味と次の対応 |
| --- | --- |
| `unreviewed` | 校閲記録なし。原文と照合して校閲する |
| `missing` | 翻訳ファイルなし。翻訳を追加してから校閲する |
| `source_changed` | 校閲後に原文または対応する原文パスが変更された。差分を翻訳へ反映して再校閲する |
| `translation_changed` | 校閲後に翻訳が変更された。変更部分を再校閲する |
| `current` | 校閲した原文・翻訳の内容と一致。翻訳の正確さそのものを自動判定するものではない |

このリポジトリの `content/post/<記事>/index.ja.md`（なければ `index.md`）を日本語原文、`index.<言語>.md` を翻訳として集計する。別の原文を記録する場合は `record --source` で明示できる。下書き・未来記事も編集用キューには含める。公開ページの対応関係は別途、Hugo が実際に出力した HTML とサイトマップで検査する。

## 重要記事から、言語ごとに進める

`priorities` は記事ディレクトリをキーとする。1 が最優先、2 が次点、未指定は 3。初期キューでは内容の誤りの影響を考え、セキュリティ、文字コード、統計の代表記事を 1 に指定した。アクセス解析に基づく順位ではない。今後は閲覧数・読者の指摘・原文の変更規模に応じて見直す。

1. 対象言語の CSV を生成し、優先度 1 の `source_changed`、`translation_changed`、`unreviewed`、`missing` を確認する。
2. 対象言語に堪能な校閲者が原文と照合し、意味の欠落、用語、自然な表現、数式・コード、リンクと画像、言語固有の表記を確認する。
3. 必要な修正を保存した後にだけ、次のコマンドで最終確認を記録する。担当者名は実際の校閲者に置き換える。

```powershell
python scripts/translation_reviews.py record post/central-limit-theorem/index.en.md --source post/central-limit-theorem/index.md --kind human --reviewer "校閲担当者名"
```

4. 翻訳と台帳を同じ変更としてコミットする。原文を変更した際は再度キューを生成し、`source_changed` の翻訳を言語別に確認する。

AI校閲の記録では `--kind ai --reviewer "Codex (AI)" --evidence docs/translation-review/<根拠ファイル>.json` を指定する。全記事を対象とする目標と順序は [translation-review-goal.md](translation-review-goal.md) に記録する。

CI は台帳の形式・参照ファイル・AI校閲の根拠を検査し、毎回 `translation-review-queue` の CSV 成果物を保存する。未確認や原文更新ありは校閲待ちとして可視化し、公開を一律に止めない。実際の人による校閲は今後このキューに従って実施する。

## 公開前の翻訳対応検査

```powershell
python scripts/test_multilingual.py
python scripts/check_multilingual.py public
```

CI では全サイトマップ掲載ページについて hreflang の重複、自分自身への指定、HTTPS、言語の一致、リンク先の存在、相互参照、サイドバーとの一致、未翻訳時の案内を検査する。失敗した場合はデプロイしない。日本語版がある対応グループだけ、その記事の日本語版を `x-default` にする。

hreflang の出力箇所は `layouts/partials/head/hreflang.html` に一本化した。[Google の多言語ページ向け指針](https://developers.google.com/search/docs/specialty/international/localized-versions) に沿って、存在する対応ページのみを指定する。重複をなくすこと自体に検索順位改善を保証する意味はない。
