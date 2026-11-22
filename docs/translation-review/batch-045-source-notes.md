# Pixelソフトウェア復元記事：Batch 045

確認日: 2026-11-23（JST）
対象: 日本語原文＋12翻訳

## 確認した一次資料

- [Google Pixel Update and Software Repair](https://pixelrepair.withgoogle.com/): 現行ツールの3段階の流れとFastboot接続案内を確認。
- [Google Pixelの初期化ヘルプ](https://support.google.com/pixelphone/answer/4596836): Pixel 4a以降（Foldを含む）を対象としていること、Updateは初期化なしで適用できる場合があること、Reinstallはデータを消去すること、初期化時の70%充電推奨を確認。
- [Pixelの再起動/クラッシュ対処](https://support.google.com/pixelphone/answer/4582729): 初期化前に試せるトラブルシューティングを確認。
- [Google USB Driver](https://developer.android.com/studio/run/win-usb): WindowsのGoogle USB driverがadbデバッグ向けであり、必要時のみ参照するよう表現を限定。

## 変更

- 「初期化される場合がある」という曖昧な警告を修正。UpdateとReinstallのデータへの影響を明確に分離。
- キャリア選択を含む旧画面手順、旧「Rescue Mode」表記、すべての端末に通用するような復元保証、純正ケーブル必須・50%充電の断定を削除。
- 対象機種、データバックアップ、Googleアカウント認証、現在のFastboot接続手順、画面上の操作選択、初期化前の代替対処を13言語で改稿。
- 原公開日2025-02-28をGit履歴で確認し、全13版の重複日付を解消。

## 制約

AI校閲であり、ネイティブ話者認証ではない。実機のUSB接続・ファームウェア更新・初期化は未実施。ツールの対応機種と画面は更新されるため、公式画面に従う注意を記載。Hugo本番ビルド成功。対象13ページのcanonical/lang/RTL/公開日/更新日/Update-Reinstall/ Fastboot/公式リンク/hreflang検査を通過。公開後確認と全記事goalは継続。
