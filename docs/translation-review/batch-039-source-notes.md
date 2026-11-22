# AG03ノイズ対策記事の原文確認

確認日: 2026-11-23（JST）

## 確認した一次資料

- [Yamaha AG03 製品仕様](https://jp.yamaha.com/audio/streaming-gaming/products/mixers/ag/ag03/specs.html): WindowsではYamaha Steinberg USB Driverが必要、MacではOS標準ドライバーを使用。
- [Yamaha AG03 サポート／ダウンロード](https://jp.yamaha.com/audio/streaming-gaming/products/mixers/ag/ag03/support.html): Windows版ドライバーV2.1.3以降では、初代AG03/AG06のAG DSP Controllerを使用できず、AG Controllerを使用するよう案内。
- [Yamaha Steinberg USB Driver for Windows](https://jp.yamaha.com/support/updates/yamaha_steinberg_usb_driver_for_win.html): 2026-11-23時点でV2.1.12。Windows 10/11 (64-bit) および限定機種のWindows on Armを記載。Arm対応モデル一覧にAG03は含まれない。
- [Yamaha AG/ZG series troubleshooting](https://jp.yamaha.com/business/audio/news/2022/defect.html): Windows環境に依存する音切れや認識切断について、ドライバーの再インストール、Windows Update、電源／USB省電力、グラフィックス、接続機器などの対処を提示。BIOS/UEFI項目は上級者向けと注意。

## 原文の修正

- 「即解決」「一発で解消」「具体的な手順」といった一般保証に読めるタイトルと説明を、筆者自身の環境で改善した事例と明示する表現に変更。
- 古いYamaha FAQアーカイブだけに依存する構成をやめ、現在の公式サポート・ドライバー・仕様・トラブルシューティングを引用。
- 日付が重複していたfront matterを整理。公開日2023-03-18を保持し、`lastmod`を2026-11-23に設定。
- 具体的なWindowsの確認・再インストール手順と、Windows on Armの対応機種確認、AG DSP Controllerとの非互換、Mac標準ドライバーを追記。
- AG03とは無関係な日本向けMercari中古出品の埋め込み広告を削除。

## 制約

ドライバーを実機にインストールしたり、ノイズ再現試験をしたりしていない。筆者の体験は独立に再現していない。V2.1.12および対応OS情報は確認日のスナップショットであり、後日変わる可能性がある。全言語の校閲はAIによるもので、ネイティブ校閲・ハードウェア認証ではない。
