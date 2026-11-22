# AI画像生成ツールのローカル環境構築マニュアル：Batch 042

確認日: 2026-11-23（JST）
対象: 日本語原文＋英語、中国語（簡体字・繁体字）、スペイン語、韓国語、ポルトガル語、フランス語、ドイツ語、ヒンディー語、インドネシア語、アラビア語、ロシア語の12翻訳

## 主な一次資料

- [ComfyUI Portable for Windows](https://docs.comfy.org/installation/comfyui_portable_windows): Python同梱、NVIDIA・AMD・Intel GPU別の配布と起動手順を確認。
- [Comfy Desktop for Windows](https://docs.comfy.org/installation/desktop/windows): Windows 10以降、x64/ARM64、専用GPU推奨だが必須ではないことを確認。
- [Comfy Registry](https://docs.comfy.org/registry/claim-my-node): legacy ManagerからRegistryへの移行状況を確認。
- [AUTOMATIC1111公式リポジトリ](https://github.com/AUTOMATIC1111/stable-diffusion-webui): Windows手動導入にPython 3.10.6を指定していることを確認。これは同アプリ固有。
- [PyTorch公式ローカル導入手順](https://pytorch.org/get-started/locally/): PyTorchの対応Python・OS・compute backendを選択する方式を確認。アプリ固有のバージョン固定は別扱いとした。
- [Fooocus公式リポジトリ](https://github.com/lllyasviel/Fooocus): プロジェクトの状態がバグ修正のみの限定的LTSであることを確認。
- [NVIDIA Stable Diffusion TensorRT拡張](https://github.com/NVIDIA/Stable-Diffusion-WebUI-TensorRT): TensorRTは任意の最適化で、特定GPU・モデル・設定の測定値を全環境へ一般化できないと判断。

## 変更

- 日本語原文の冒頭に各プロジェクトの現行状況と適用範囲の注意を追加し、英語を含む12翻訳にも対応する現地語注記と公式リンクを追加。
- 日本語原文の固定VRAM/RAM/SSD基準、NVIDIA一択、Python 3.10.6/CUDAの汎用化、A1111の複数起動フラグ同時指定、ComfyUI Manager必須、Fooocusの自動モデル取得、safetensorsの出所保証、TensorRTの1.5〜2倍断定、ControlNetの完全一致保証、診断検査を無効化する助言、将来VRAMの断定を修正。
- 公開日は維持し、最終更新日を設定。壊れていた日本語GPU見出しアンカーも修正。

## 制約・残課題

- 校閲はAIによる。人間・ネイティブ話者による認証ではない。
- 翻訳版の既存の詳細な旧手順は全面再翻訳していない。各言語の注記で、矛盾する旧版依存の記述は現行公式資料に従うよう明示した。将来、翻訳本文自体を段落単位で改稿し、ネイティブ話者が校閲する余地がある。
- GPU実機でインストール・速度比較を行っていない。既存の全リンクも一件ずつ再検査していない。
- 全サイトHugo本番/minifyビルドと対象13ページの静的検査は成功（canonical、lang、hreflang、RTL、更新日、公式リンク）。公開CI・デプロイ後の13 URL確認は後続。全記事goalは継続。
