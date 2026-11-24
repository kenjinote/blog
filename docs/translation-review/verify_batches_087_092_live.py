"""Verify publication of reviewed article translation batches 87 onward."""
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse
from xml.etree import ElementTree as ET
import argparse
import json
import re
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs/translation-review"
LANGS = ("ja", "en", "zh-cn", "es", "ko", "pt", "zh-tw", "hi", "fr", "de", "ar", "ru", "id")
NS = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
ARTICLES = {
    87: {
        "bundle": ROOT / "content/post/IntelliJ IDEAでGitHub Copilotを使う",
        "slug": "IntelliJ IDEAでGitHub Copilotを使う",
        "links": [
            "https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension",
            "https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions",
            "https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer",
        ],
        "markers": ["CopyandOpen", "LogintoGitHub", "AuthorizeGitHubCopilotPlugin", "CopilotFree", "CopilotChat"],
        "date": "2022-09-10",
    },
    88: {
        "bundle": ROOT / "content/post/IntelliJ IDEAで日付を貼り付けるコマンドを追加する",
        "slug": "IntelliJ IDEAで日付を貼り付けるコマンドを追加する",
        "links": [
            "https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html",
            "https://www.jetbrains.com/help/idea/template-variables.html",
            "https://www.jetbrains.com/help/idea/settings-live-templates.html",
        ],
        "markers": ["yyyy-MM-dd'T'HH:mm:ssXXX", "Skipifdefined", "Tab", "Everywhere", "+09:00"],
        "date": "2022-09-04",
    },
    89: {
        "bundle": ROOT / "content/post/LoadIconはDestroyIconを呼び出す必要はない",
        "slug": "LoadIconはDestroyIconを呼び出す必要はない",
        "links": [
            "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon",
            "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw",
            "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew",
            "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon",
            "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage",
            "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource",
            "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex",
        ],
        "markers": ["LoadIcon", "LoadImage", "LR_SHARED", "LR_COPYRETURNORG", "CopyIcon", "CreateIconFromResourceEx", "DestroyIcon"],
        "date": "2024-04-19",
    },
    90: {
        "bundle": ROOT / "content/post/かっこいい Web ページテンプレート（html5up）",
        "slug": "かっこいい Web ページテンプレート（html5up）",
        "links": ["https://html5up.net/", "https://html5up.net/license"],
        "markers": ["HTML5", "CSS3", "CCBY3.0", "FreeDownload"],
        "date": "2023-04-17",
    },
    91: {
        "bundle": ROOT / "content/post/LogicPad 開発秘話",
        "slug": "LogicPad 開発秘話",
        "links": ["https://logicpad.org"],
        "markers": ["2025", "👇"],
        "date": "2025-07-30",
    },
    92: {
        "bundle": ROOT / "content/post/MS-DOS 4.0 のオープンソース化",
        "slug": "MS-DOS 4.0 のオープンソース化",
        "links": [
            "https://opensource.microsoft.com/blog/2024/04/25/open-sourcing-ms-dos-4-0/",
            "https://github.com/microsoft/MS-DOS",
            "https://github.com/microsoft/MS-DOS/blob/main/v4.0/LICENSE",
        ],
        "markers": ["2024", "8086", "MIT"],
        "date": "2024-05-05",
    },
    93: {
        "bundle": ROOT / "content/post/日本の災害",
        "slug": "日本の災害",
        "links": [
            "https://www.jma.go.jp/jma/menu/20240101_noto_jishin.html",
            "https://www.fdma.go.jp/disaster/info/items/b055402cefac7721623c30034b25489118dbec38.pdf",
        ],
        "markers": ["2024", "720", "492", "165", "813"],
        "date": "2024-01-07",
    },
    94: {
        "bundle": ROOT / "content/post/Mathematicaで巡回セールスマン問題を解く",
        "slug": "Mathematicaで巡回セールスマン問題を解く",
        "links": [
            "https://reference.wolfram.com/language/ref/FindShortestTour.html",
            "https://reference.wolfram.com/language/ref/SparseArray.html",
        ],
        "markers": ["SparseArray", "Infinity", "FindShortestTour", "137"],
        "date": "2022-10-12",
    },
    95: {
        "bundle": ROOT / "content/post/Mathematica入門",
        "slug": "Mathematica入門",
        "links": [
            "https://reference.wolfram.com/language/ref/Solve.html",
            "https://reference.wolfram.com/language/ref/Reduce.html",
            "https://reference.wolfram.com/language/ref/D.html",
            "https://reference.wolfram.com/language/ref/Integrate.html",
            "https://reference.wolfram.com/language/ref/Limit.html",
            "https://reference.wolfram.com/language/ref/Sum.html",
            "https://reference.wolfram.com/language/ref/Inverse.html",
            "https://reference.wolfram.com/language/ref/Eigensystem.html",
            "https://reference.wolfram.com/language/ref/Projection.html",
            "https://reference.wolfram.com/language/ref/RotationMatrix.html",
            "https://reference.wolfram.com/language/ref/ReflectionTransform.html",
            "https://reference.wolfram.com/language/ref/RandomReal.html",
            "https://reference.wolfram.com/language/ref/RandomInteger.html",
            "https://reference.wolfram.com/language/ref/RandomVariate.html",
        ],
        "markers": ["Sqrt[33]", "Projection", "ReflectionTransform", "RandomInteger[]"],
        "date": "2024-07-25",
    },
    96: {
        "bundle": ROOT / "content/post/Microsoft MVP受賞について(2023-2024)",
        "slug": "Microsoft MVP受賞について(2023-2024)",
        "links": [
            "https://learn.microsoft.com/en-us/teamblog/msdn-technet-migration",
            "https://mvp.microsoft.com/mvpintro/",
        ],
        "markers": ["2017", "2023-2024", "MSDN"],
        "date": "2023-07-31",
    },
    97: {
        "bundle": ROOT / "content/post/Microsoft MVP（2024-2025）を再受賞しました",
        "slug": "Microsoft MVP（2024-2025）を再受賞しました",
        "links": ["https://mvp.microsoft.com/mvpintro/"],
        "markers": ["2024", "2025"],
        "date": "2024-09-03",
    },
    98: {
        "bundle": ROOT / "content/post/Microsoft MVP（2025-2026）を再受賞しました",
        "slug": "Microsoft MVP（2025-2026）を再受賞しました",
        "links": ["https://mvp.microsoft.com/mvpintro/"],
        "markers": ["2025-2026", "2025", "2026"],
        "date": "2025-07-13",
    },
    99: {
        "bundle": ROOT / "content/post/Microsoft Wordのショートカット一覧",
        "slug": "Microsoft Wordのショートカット一覧",
        "linkFragment": "95ef89dd-7142-4b50-afb2-f762f663ceb2",
        "markers": ["F12", "Ctrl"],
        "scopeMarkers": {
            "ja": "米国キーボード配列",
            "en": "U.S. keyboard layout",
            "zh-cn": "美国键盘布局",
            "zh-tw": "美國鍵盤配置",
            "es": "EE. UU.",
            "fr": "disposition de clavier américaine",
            "de": "US-Tastaturbelegung",
            "pt": "layout de teclado dos EUA",
            "ko": "미국 키보드 배열",
            "hi": "अमेरिकी कीबोर्ड लेआउट",
            "ar": "تخطيط لوحة مفاتيح أمريكي",
            "ru": "американской раскладкой клавиатуры",
            "id": "tata letak papan ketik AS",
        },
        "date": "2024-04-07",
    },
    100: {
        "bundle": ROOT / "content/post/「日本人ファースト」について思うこと",
        "slug": "「日本人ファースト」について思うこと",
        "links": [
            "https://www.mhlw.go.jp/stf/newpage_68794.html",
            "https://www.mhlw.go.jp/content/001684938.pdf",
            "https://www.npa.go.jp/publications/statistics/kikakubunseki/R6jyousei.pdf",
            "https://www.chusho.meti.go.jp/koukai/shingikai/syoukibokihon/2018/download/181012syoukiboKihon04.pdf",
            "https://www.stat.go.jp/data/jinsui/2.html",
        ],
        "markers": ["2,571,037", "47,332", "12,170"],
        "date": "2026-01-23",
    },
    101: {
        "bundle": ROOT / "content/post/『君死にたまふことなかれ』",
        "slug": "『君死にたまふことなかれ』",
        "links": [
            "https://www.ndl.go.jp/portrait/datas/347",
            "https://www.aozora.gr.jp/cards/000885/files/3629_48834.html",
        ],
        "markers": ["1904"],
        "date": "2024-07-25",
    },
    102: {
        "bundle": ROOT / "content/post/Microsoft.Windows.AIの最新API活用事例とサンプルコード",
        "slug": "microsoft-windows-ai-api-guide",
        "links": [
            "https://learn.microsoft.com/en-us/windows/ai/apis",
            "https://learn.microsoft.com/en-us/windows/ai/apis/get-started",
            "https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica",
            "https://learn.microsoft.com/en-us/windows/ai/npu-devices",
            "https://learn.microsoft.com/en-us/windows/ai/directml/dml-get-started",
        ],
        "markers": ["136.5 GB/s", "EnsureReadyAsync", "Direct3D 12", "Aion Instruct"],
        "date": "2026-09-11",
    },
    103: {
        "bundle": ROOT / "content/post/【HUGO】ローカルで環境で表示プレビュー",
        "slug": "【HUGO】ローカルで環境で表示プレビュー",
        "links": [
            "https://gohugo.io/installation/windows/",
            "https://gohugo.io/getting-started/usage/",
            "https://gohugo.io/commands/hugo_server/",
        ],
        "markers": ["winget install", "hugo server", "--buildDrafts"],
        "date": "2022-09-05",
    },
    104: {
        "bundle": ROOT / "content/post/abel",
        "slug": "abel",
        "links": [
            "https://abelprize.no/page/about-niels-henrik-abel",
            "https://abelprize.no/page/biography-niels-henrik-abelupbringing-and-schooling",
            "https://abelprize.no/page/biography-niels-henrik-abel-great-journey-abroad",
            "https://abelprize.no/page/biography-niels-henrik-abel-his-last-years",
            "https://snl.no/Niels_Henrik_Abel",
            "https://mathshistory.st-andrews.ac.uk/Biographies/Abel/",
        ],
        "markers": ["1829"],
        "date": "2026-09-20",
    },
    105: {
        "bundle": ROOT / "content/post/Ollamaを使ったローカルLLMの簡単構築とAPI連携",
        "slug": "ollama-local-llm-api-guide",
        "links": [
            "https://docs.ollama.com/quickstart",
            "https://docs.ollama.com/api/chat",
            "https://docs.ollama.com/api/generate",
            "https://docs.ollama.com/api/embed",
            "https://docs.ollama.com/faq",
            "https://github.com/ollama/ollama-python",
            "https://github.com/ollama/ollama-js",
            "https://ollama.com/library",
        ],
        "markers": ["gemma4:e2b", "/api/chat", "/api/embed", "embeddinggemma", "eval_duration", "ollama.chat"],
        "date": "2026-09-11",
    },
    106: {
        "bundle": ROOT / "content/post/PMP勉強",
        "slug": "PMP勉強",
        "links": [
            "https://www.pmi.org/-/media/pmi/documents/public/pdf/certifications/new-pmp-examination-content-outline-2026.pdf",
            "https://www.pmi.org/certifications/project-management-pmp/new-exam",
            "https://www.pmi.org/certifications/project-management-pmp",
            "https://www.pmi.org/-/media/pmi/documents/public/pdf/certifications/generic-certification-handbook.pdf",
            "https://agilemanifesto.org/",
        ],
        "markers": ["180", "170", "240", "33%", "41%", "26%", "2026"],
        "date": "2024-02-04",
    },
    107: {
        "bundle": ROOT / "content/post/PaperModでTwitter Cardを設定する方法",
        "slug": "PaperModでTwitter Cardを設定する方法",
        "links": [
            "https://github.com/adityatelange/hugo-PaperMod/wiki/Features",
            "https://github.com/adityatelange/hugo-PaperMod/wiki/Variables",
            "https://gohugo.io/content-management/page-bundles/",
            "https://devcommunity.x.com/t/card-validator-preview-removal/175006",
        ],
        "markers": ["twitter:card", "twitter:image", "og:image", "1200x630", "hidden: true", "production"],
        "date": "2022-09-10",
    },
    108: {
        "bundle": ROOT / "content/post/PaperModの画像の配置変更",
        "slug": "PaperModの画像の配置変更",
        "links": [
            "https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs",
            "https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/common/post-entry.css",
            "https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844",
        ],
        "markers": ["assets/css/extended/custom.css", "grid-template-areas", "grid-template-columns", "@media (max-width: 600px)", "width: 100%;", "height: auto;"],
        "date": "2022-09-11",
    },
    109: {
        "bundle": ROOT / "content/post/PaperModの配色変更",
        "slug": "PaperModの配色変更",
        "links": [
            "https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs",
            "https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/core/theme-vars.css",
            "https://github.com/adityatelange/hugo-PaperMod/discussions/645",
            "https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum",
        ],
        "markers": ["assets/css/extended/theme-colors.css", "data-theme", "--code-block-bg", "color-scheme: light", "color-scheme: dark", "4.5:1", "10.4:1", "13.4:1"],
        "date": "2022-09-07",
    },
    110: {
        "bundle": ROOT / "content/post/PowerShell で Excel のメタデータ（個人情報）を削除する方法",
        "slug": "PowerShell で Excel のメタデータ（個人情報）を削除する方法",
        "links": [
            "https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removedocumentinformation",
            "https://learn.microsoft.com/en-us/office/vba/api/excel.xlremovedocinfotype",
            "https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removepersonalinformation",
            "https://learn.microsoft.com/en-us/office/vba/api/excel.workbooks.open",
            "https://learn.microsoft.com/en-us/office/vba/api/excel.application.automationsecurity",
            "https://learn.microsoft.com/en-us/office/vba/library-reference/concepts/using-the-document-inspector",
            "https://learn.microsoft.com/en-us/office/client-developer/integration/considerations-unattended-automation-office-microsoft-365-for-unattended-rpa",
            "https://learn.microsoft.com/en-us/office/vba/api/word.document.removedocumentinformation",
            "https://learn.microsoft.com/en-us/office/vba/api/powerpoint.presentation.removedocumentinformation",
        ],
        "markers": ["RemoveDocumentInformation(4)", "xlRDIRemovePersonalInformation", "AutomationSecurity", "*.xlsx", "Document Inspector"],
        "date": "2025-07-30",
    },
    111: {
        "bundle": ROOT / "content/post/PowerShellで.DS_Storeを一括削除する",
        "slug": "PowerShellで.DS_Storeを一括削除する",
        "links": [
            "https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem",
            "https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/remove-item",
            "https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_commonparameters",
        ],
        "markers": ["Get-ChildItem", "-LiteralPath", "'.DS_Store'", "-File", "-Recurse", "-Force", "-WhatIf"],
        "date": "2022-09-12",
    },
    112: {
        "bundle": ROOT / "content/post/PowerToysのインストール",
        "slug": "PowerToysのインストール",
        "links": [
            "https://learn.microsoft.com/en-us/windows/powertoys/install",
            "https://learn.microsoft.com/en-us/windows/package-manager/winget/install",
            "https://learn.microsoft.com/en-us/windows/package-manager/winget/uninstall",
        ],
        "markers": ["winget install --id Microsoft.PowerToys --exact --source winget", "winget uninstall --id Microsoft.PowerToys --exact --source winget", "ARM64", "WebView2 Runtime"],
        "date": "2023-09-30",
    },
    113: {
        "bundle": ROOT / "content/post/Python(matplotlib.pyplot)を使ってグラフを描画する方法",
        "slug": "Python(matplotlib.pyplot)を使ってグラフを描画する方法",
        "links": [
            "https://matplotlib.org/stable/api/pyplot_summary.html",
            "https://numpy.org/doc/stable/reference/generated/numpy.linspace.html",
            "https://research.google.com/colaboratory/faq.html?hl=en",
            "https://colab.research.google.com/",
        ],
        "markers": ["np.linspace(0, 2 * np.pi, 500)", "np.sin(x)", "np.cos(x)", "plt.legend()", "plt.show()", "2π"],
        "date": "2023-04-09",
    },
    114: {
        "bundle": ROOT / "content/post/Pythonコード片",
        "slug": "Pythonコード片",
        "links": [
            "https://docs.python.org/3/library/urllib.request.html",
            "https://docs.python.org/3/library/tempfile.html",
            "https://docs.python.org/3/library/webbrowser.html",
            "https://www.python.org/community/logos/",
        ],
        "markers": ["urlopen(request,timeout=15)", "response.headers.get_content_type()", "2*1024*1024", "webbrowser.open(temp_path.as_uri(),new=2)", "temp_path.unlink()", "PNG signature"],
        "date": "2025-02-24",
    },
    130: {
        "bundle": ROOT / "content/post/モチベーションを上げてくれる動画",
        "slug": "モチベーションを上げてくれる動画",
        "links": ["https://x.com/eleven_s_s/status/1567256455836737544", "https://www.youtube.com/watch?v=5WTldFIQ7E4", "https://www.youtube.com/watch?v=8ewxptSV66M", "https://www.youtube.com/watch?v=9-2YFldnWzg"],
        "markers": [],
        "scopeMarkers": {"ja":"行き詰まった時に見返したい言葉","en":"Words to revisit when I feel stuck","zh-cn":"感到受挫时可以重看的话","es":"Palabras que vuelvo a leer cuando me atasco","ko":"막막할 때 다시 보는 말","pt":"Palavras que revejo quando me sinto travado","zh-tw":"感到受挫時可以重看的話","hi":"जब मन अटक जाए तो फिर से पढ़ने योग्य शब्द","fr":"Des mots à relire quand je me sens bloqué","de":"Worte, die ich bei Stillstand erneut lese","ar":"كلمات أعود إليها عندما أشعر بالتعثر","ru":"Слова, к которым я возвращаюсь в трудный момент","id":"Kata-kata yang saya baca kembali saat merasa buntu"},
        "date": "2022-09-08",
    },
    176: {"bundle": ROOT / "content/post/TinyLLaMA を C++ から呼び出せるようにする手順（llama.cpp使用）", "slug": "TinyLLaMA を C++ から呼び出せるようにする手順（llama.cpp使用）", "links": ["https://github.com/ggml-org/llama.cpp", "https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/simple.cpp", "https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/CMakeLists.txt", "https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/README.md", "https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0", "https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF", "https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"], "markers": ["llamacli", "Q4_K_M", "llama-simple", "C++17", "GGUF"], "date": "2025-07-19"},
    175: {
        "bundle": ROOT / "content/post/ThinkPad（中古）を買った",
        "slug": "ThinkPad（中古）を買った",
        "links": ["https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025", "https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-11-supported-intel-processors", "https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T470s/ThinkPad_T470s_Spec.PDF"],
        "markers": ["Corei7-7600U", "Windows10", "Windows11", "Shift+F10", "2026"],
        "date": "2023-01-13",
    },
    174: {
        "bundle": ROOT / "content/post/Snipping Toolの使い方",
        "slug": "Snipping Toolの使い方",
        "linksByLanguage": {"ja": ["https://support.microsoft.com/ja-jp/windows/snipping-tool-%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3-%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%E3%82%92%E3%82%AD%E3%83%A3%E3%83%97%E3%83%81%E3%83%A3%E3%81%99%E3%82%8B-00246869-1843-655f-f220-97299b865f6b", "https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows"], "en": ["https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots", "https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows"], "zh-cn": ["https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots", "https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows"], "es": ["https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots", "https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows"], "ko": ["https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots", "https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows"], "pt": ["https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots", "https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows"], "zh-tw": ["https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots", "https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows"], "hi": ["https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots", "https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows"], "fr": ["https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots", "https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows"], "de": ["https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots", "https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows"], "ar": ["https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots", "https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows"], "ru": ["https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots", "https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows"], "id": ["https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots", "https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows"]},
        "markers": ["Win + Shift + S", "Win + Shift + R", "Snipping Tool"],
        "date": "2024-04-01",
    },
    173: {
        "bundle": ROOT / "content/post/Slack App + OAuth2 を使って Slack にメッセージを投稿する方法",
        "slug": "Slack App + OAuth2 を使って Slack にメッセージを投稿する方法",
        "links": ["https://docs.slack.dev/reference/methods/chat.postMessage/", "https://docs.slack.dev/authentication/tokens/", "https://api.slack.com/apps", "https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpsendrequest", "https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpreaddata", "https://learn.microsoft.com/en-us/windows/win32/api/winhttp/nf-winhttp-winhttpclosehandle"],
        "markers": ["SLACK_BOT_TOKEN", "chat:write", "escapeJson", "WinHttpQueryDataAvailable", "slackOk", "chat.postMessage"],
        "date": "2025-07-16",
    },
    172: {
        "bundle": ROOT / "content/post/Rustのはじめかた",
        "slug": "Rustのはじめかた",
        "links": ["https://www.rust-lang.org/tools/install", "https://doc.rust-lang.org/book/", "https://doc.rust-lang.org/cargo/getting-started/installation.html", "https://doc.rust-lang.org/rust-by-example/", "https://play.rust-lang.org/", "https://blog.rust-lang.org/2015/05/15/Rust-1.0/"],
        "markers": ["cargo new hello_world", "cargo run", "println!", "rustup", "Rust 1.0"],
        "date": "2022-09-06",
    },
    171: {
        "bundle": ROOT / "content/post/Rustでテストを書く",
        "slug": "Rustでテストを書く",
        "links": ["https://doc.rust-lang.org/book/ch11-01-writing-tests.html", "https://doc.rust-lang.org/cargo/commands/cargo-test.html", "https://doc.rust-lang.org/reference/attributes/testing.html"],
        "markers": ["#[test]", "#[cfg(test)]", "cargo test", "assert_eq!", "test result: ok"],
        "date": "2022-10-01",
    },
    170: {
        "bundle": ROOT / "content/post/Rustでシンプルなウィンドウを表示する",
        "slug": "Rustでシンプルなウィンドウを表示する",
        "links": ["https://docs.rs/windows-sys/latest/windows_sys/Win32/Graphics/Gdi/fn.GetStockObject.html", "https://docs.rs/windows-sys/latest/windows_sys/Win32/UI/WindowsAndMessaging/", "https://docs.rs/windows-sys/latest/windows_sys/Win32/UI/WindowsAndMessaging/struct.WNDCLASSW.html", "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-registerclassw", "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createwindowexw", "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getmessagew", "https://learn.microsoft.com/en-us/windows/win32/winmsg/about-window-classes"],
        "markers": ["windows-sys", "GetModuleHandleW", "RegisterClassW", "CreateWindowExW", "GetMessageW", "WNDCLASSW::default()"],
        "date": "2022-10-01",
    },
    169: {
        "bundle": ROOT / "content/post/RustでMessageBoxを表示する",
        "slug": "RustでMessageBoxを表示する",
        "links": ["https://docs.rs/windows-sys/latest/windows_sys/Win32/UI/WindowsAndMessaging/", "https://docs.rs/crate/windows-sys/latest", "https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxw", "https://github.com/microsoft/windows-rs"],
        "markers": ["windows-sys", "MessageBoxW", "Win32_UI_WindowsAndMessaging", "encode_utf16", "MB_ICONINFORMATION"],
        "date": "2022-09-30",
    },
    168: {
        "bundle": ROOT / "content/post/RAG実装入門ローカルAIに自分のドキュメントを読み込ませる方法",
        "slug": "rag-local-ai-implementation-guide",
        "links": ["https://huggingface.co/intfloat/multilingual-e5-large", "https://www.sbert.net/docs/sentence_transformer/usage/usage.html", "https://docs.trychroma.com/docs/run-chroma/clients", "https://docs.trychroma.com/docs/collections/add-data", "https://docs.trychroma.com/docs/collections/update-data", "https://docs.trychroma.com/docs/collections/delete-data", "https://docs.trychroma.com/docs/collections/configure", "https://github.com/ollama/ollama-python", "https://ollama.com/library/qwen3", "https://pypdf.readthedocs.io/en/stable/"],
        "markers": ["passage: ", "query: ", "PersistentClient(path=", "collection.upsert(", "collection.delete(where=", "ollama.chat(", "qwen3:8b", "untrusted"],
        "date": "2026-09-11",
    },
    167: {
        "bundle": ROOT / "content/post/central-limit-theorem",
        "slug": "central-limit-theorem",
        "links": ["https://math.mit.edu/~dav/05.dir/class6-prep.pdf"],
        "markers": ["Z_n", "num_simulations=10000", "plt.show()"],
        "scopeMarkers": {"ja":"サイズ n の標本を何度も抽出","en":"Repeatedly draw samples of size n","zh-cn":"反复抽取容量为 n 的样本","es":"Extraer repetidamente muestras de tamaño n","ko":"크기 n인 표본을 반복해서 추출","pt":"Extrair repetidamente amostras de tamanho n","zh-tw":"反覆抽取樣本數為 n 的樣本","hi":"आकार n के नमूने बार-बार लें","fr":"Prélever plusieurs fois un échantillon de taille n","de":"Wiederholt Stichproben mit Umfang n ziehen","ar":"سحب عينات حجم كل منها n بصورة متكررة","ru":"Многократно брать выборки объёма n","id":"Ambil sampel berukuran n berulang kali"},
        "date": "2026-09-14",
    },
    166: {
        "bundle": ROOT / "content/post/Webページ内のすべてのチェックボックスを全チェックする",
        "slug": "Webページ内のすべてのチェックボックスを全チェックする",
        "links": ["https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click", "https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/checked", "https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event"],
        "markers": ["input[type=", ".click()", "javascript:(()=>", "not(:disabled)"],
        "date": "2022-10-05",
    },
    165: {
        "bundle": ROOT / "content/post/yt-dlp.exe による YouTube 動画のダウンロード方法",
        "slug": "yt-dlp.exe による YouTube 動画のダウンロード方法",
        "links": ["https://github.com/yt-dlp/yt-dlp/releases/latest", "https://github.com/yt-dlp/yt-dlp#readme", "https://www.youtube.com/t/terms", "https://support.google.com/youtube/answer/56100"],
        "markers": ["yt-dlp.exe -U", "--audio-format mp3", "ffmpeg", "YouTube Terms of Service"],
        "date": "2024-09-03",
    },
    164: {
        "bundle": ROOT / "content/post/wsl で「Temporary failure resolving～」と表示される場合の対処方法",
        "slug": "wsl で「Temporary failure resolving～」と表示される場合の対処方法",
        "links": ["https://learn.microsoft.com/en-us/windows/wsl/troubleshooting", "https://learn.microsoft.com/en-us/windows/wsl/networking", "https://learn.microsoft.com/en-us/windows/wsl/wsl-config"],
        "markers": ["Resolve-DnsName", "getent hosts", "dnsTunneling=true", "wsl --shutdown"],
        "date": "2024-03-31",
    },
    163: {
        "bundle": ROOT / "content/post/Webページの自動更新ブラウザ拡張(Edgeアドオン)",
        "slug": "Webページの自動更新ブラウザ拡張(Edgeアドオン)",
        "links": ["https://microsoftedge.microsoft.com/addons/detail/%E3%82%BF%E3%83%96%E3%81%AE%E8%87%AA%E5%8B%95%E6%9B%B4%E6%96%B0/bicjibdndeejemialpbohjpiimehbapb", "https://support.microsoft.com/en-us/edge/microsoft-edge-extensions-frequently-asked-questions", "https://support.microsoft.com/en-us/edge/change-site-access-permissions-for-extensions-in-microsoft-edge"],
        "markers": ["Tab Auto Refresh", "Get"],
        "date": "2024-04-06",
    },
    162: {
        "bundle": ROOT / "content/post/paint.netで画像の特定個所にモザイクをかける方法",
        "slug": "paint.netで画像の特定個所にモザイクをかける方法",
        "links": ["https://paint.net/doc/latest/EffectsDistortMenu.html", "https://paint.net/roadmap.html", "https://ico.org.uk/media2/pbwchh24/disclosing-documents-to-the-public-securely-all-1-0-0.pdf"],
        "markers": ["Pixelate", "Scale Down", "Scale Up", "Nearest Neighbor"],
        "date": "2023-04-11",
    },
    161: {
        "bundle": ROOT / "content/post/経営者メモ",
        "slug": "経営者メモ",
        "links": ["https://www.youtube.com/watch?v=2TALYTLAke0", "https://www.hotpepper.jp/", "https://beauty.hotpepper.jp/top/", "https://www.bunka.go.jp/seisaku/chosakuken/seidokaisetsu/chosakukensha_fumei/"],
        "markers": ["lastmod", "Hot Pepper", "References", "参考資料"],
        "date": "2022-09-07",
    },
    160: {
        "bundle": ROOT / "content/post/i18nとは？",
        "slug": "i18nとは？",
        "links": ["https://www.w3.org/International/questions/qa-i18n", "https://www.w3.org/TR/i18n-glossary/", "https://www.unicode.org/reports/tr35/"],
        "markers": ["Internationalization", "l10n", "Unicode", "CLDR"],
        "date": "2023-04-07",
    },
    159: {
        "bundle": ROOT / "content/post/paint.netを使って画像に枠線をつける方法",
        "slug": "paint.netを使って画像に枠線をつける方法",
        "links": ["https://paint.net/doc/latest/ImageMenu.html", "https://paint.net/doc/latest/ColorsWindow.html", "https://paint.net/roadmap.html"],
        "markers": ["paint.net5.1.1", "SecondaryColor"],
        "assets": ["img.webp", "img_1.webp"],
        "date": "2023-04-11",
    },
    158: {
        "bundle": ROOT / "content/post/証明書エラーでGitHub Copilotが使えなくなった場合の対処方法",
        "slug": "証明書エラーでGitHub Copilotが使えなくなった場合の対処方法",
        "links": ["https://docs.github.com/en/copilot/how-tos/troubleshoot-copilot/troubleshoot-network-errors", "https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/network-settings", "https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/configure-network-settings?tool=jetbrains", "https://support.eset.com/en/kb3126-disable-ssl-filtering-in-eset-windows-products"],
        "markers": ["UNABLE_TO_VERIFY_LEAF_SIGNATURE", "curl.exe", "SSL/TLS", "2024-04-21"],
        "date": "2024-04-21",
    },
    157: {
        "bundle": ROOT / "content/post/Windows 11の右クリックメニューを従来版に戻す方法",
        "slug": "Windows 11の右クリックメニューを従来版に戻す方法",
        "links": ["https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows", "https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows"],
        "markers": ["InprocServer32", "Shift", "F10", "Microsoft"],
        "assets": ["img_1.webp", "img_2.webp"],
        "date": "2024-03-30",
    },
    156: {
        "bundle": ROOT / "content/post/グラフエディタ",
        "slug": "グラフエディタ",
        "links": ["https://csacademy.com/app/graph_editor/", "https://codeforces.com/blog/entry/45758"],
        "markers": ["CS Academy Graph Editor", "Directed", "DownloadasPNG", "2026年11月24日"],
        "assets": ["img_1.webp"],
        "date": "2022-10-13",
    },
    155: {
        "bundle": ROOT / "content/post/eguiで日本語を表示する方法",
        "slug": "eguiで日本語を表示する方法",
        "links": ['https://github.com/emilk/eframe_template', 'https://docs.rs/egui/latest/egui/text/struct.FontDefinitions.html', 'https://docs.rs/egui/latest/egui/struct.FontData.html', 'https://github.com/google/fonts/tree/main/ofl/notosansjp', 'https://github.com/google/fonts/blob/main/ofl/notosansjp/OFL.txt'],
        "markers": ["Noto Sans JP", "Arc::new", "NotoSansJP[wght].ttf"],
        "date": "2023-04-01",
    },
    154: {
        "bundle": ROOT / "content/post/ボタンついて",
        "slug": "ボタンついて",
        "links": ['https://learn.microsoft.com/en-us/windows/win32/controls/button-styles', 'https://learn.microsoft.com/en-us/windows/win32/controls/bn-clicked', 'https://learn.microsoft.com/en-us/windows/win32/menurc/wm-command', 'https://learn.microsoft.com/en-us/windows/win32/learnwin32/creating-a-window', 'https://github.com/kenjinote/button/blob/main/main.cpp'],
        "markers": ["BN_CLICKED", "ID_BUTTON1"],
        "date": "2023-01-14",
    },
    153: {
        "bundle": ROOT / "content/post/シンプルなアイコン集サイト",
        "slug": "シンプルなアイコン集サイト",
        "links": ['https://developers.google.com/fonts/docs/material_symbols', 'https://github.com/primer/octicons/blob/main/LICENSE', 'https://github.com/planetabhi/sargam-icons/blob/main/LICENSE.txt', 'https://icon-icons.com/id/license', 'https://www.flaticon.com/pricing', 'https://legacy-api-docs.iconfinder.com/', 'https://github.com/iconic/open-iconic', 'https://fonts.google.com/icons', 'https://primer.style/octicons/', 'https://sargamicons.com/', 'https://www.iconfinder.com/', 'https://www.iconfont.cn/'],
        "markers": ["MIT License", "2026"],
        "date": "2022-09-07",
    },
    152: {
        "bundle": ROOT / "content/post/TeamViewerで簡単リモート接続",
        "slug": "TeamViewerで簡単リモート接続",
        "links": ["https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/for-developers/command-line-parameters/", "https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-classic/security/best-practices/best-practices-for-secure-unattended-access/", "https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/security/security-statement/"],
        "markers": ["-p", "Easy Access"],
        "date": "2023-01-13",
    },
    151: {
        "bundle": ROOT / "content/post/mac mini(2018)を購入",
        "slug": "mac mini(2018)を購入",
        "links": ['https://support.apple.com/111912', 'https://support.apple.com/122867', 'https://developer.apple.com/xcode/system-requirements/', 'https://developer.apple.com/documentation/Apple-Silicon/porting-your-macOS-apps-to-Apple-silicon'],
        "markers": ["IntelliJ IDEA", "2026"],
        "date": "2023-04-02",
    },
    150: {
        "bundle": ROOT / "content/post/Windows でパスの通った実行ファイルの場所を見つける方法",
        "slug": "Windows でパスの通った実行ファイルの場所を見つける方法",
        "links": ["https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/where", "https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-command?view=powershell-7.5", "https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-7.5"],
        "markers": ["where.exe", "Get-Command"],
        "date": "2023-04-03",
    },
    149: {
        "bundle": ROOT / "content/post/コミュニティに必要なこと",
        "slug": "コミュニティに必要なこと",
        "links": ["https://scratch.mit.edu/community_guidelines/"],
        "markers": ["Scratch Community Guidelines"],
        "date": "2022-09-23",
    },
    148: {
        "bundle": ROOT / "content/post/macでWindowsライク（Alt+Tab）にアプリケーション切り替えする方法",
        "slug": "macでWindowsライク（Alt+Tab）にアプリケーション切り替えする方法",
        "links": ["https://alt-tab.app/", "https://alt-tab.app/faq", "https://alt-tab.app/privacy", "https://alt-tab.app/terms", "https://support.apple.com/en-us/102650"],
        "markers": ["Command-Tab", "Option-Tab"],
        "date": "2023-04-05",
    },
    147: {
        "bundle": ROOT / "content/post/エクスプローラーの右クリックメニューに秀丸エディタgrepを追加する",
        "slug": "エクスプローラーの右クリックメニューに秀丸エディタgrepを追加する",
        "links": ["https://help.maruo.co.jp/hidemaru/html/230_Option.html", "https://support.microsoft.com/en-us/windows/experience/backup-recovery/how-to-back-up-and-restore-the-registry-in-windows", "https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows", "https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025", "https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-import"],
        "markers": ["Microsoft"],
        "assets": ["秀丸レジストリ登録.reg", "秀丸レジストリ解除.reg"],
        "scopeMarkers": {"en": "Show more options", "ja": "その他のオプションを表示", "zh-cn": "显示更多选项", "es": "Mostrar más opciones", "ko": "더 많은 옵션 표시", "pt": "Mostrar mais opções", "zh-tw": "顯示更多選項", "hi": "Show more options", "fr": "Afficher plus d’options", "de": "Weitere Optionen anzeigen", "ar": "إظهار المزيد من الخيارات", "ru": "Показать дополнительные параметры", "id": "Show more options"},
        "date": "2024-04-03",
    },
    146: {
        "bundle": ROOT / "content/post/ブログで使える写真素材サイト「Unsplash」について",
        "slug": "ブログで使える写真素材サイト「Unsplash」について",
        "links": ["https://unsplash.com/license", "https://unsplash.com/terms", "https://help.unsplash.com/en/articles/2612315-can-i-use-unsplash-images-for-personal-or-commercial-projects", "https://help.unsplash.com/en/articles/2646379-what-if-there-s-a-brand-or-identifiable-person-depicted-in-an-image-that-i-download", "https://help.unsplash.com/en/articles/6604652-what-is-the-unsplash-license"],
        "markers": ["Unsplash+", "third-party", "commercial", "significant", "attribution"],
        "scopeMarkers": {"ja": "Unsplash+", "zh-cn": "Unsplash+", "es": "Unsplash+", "ko": "Unsplash+", "pt": "Unsplash+", "zh-tw": "Unsplash+", "hi": "Unsplash+", "fr": "Unsplash+", "de": "Unsplash+", "ar": "Unsplash+", "ru": "Unsplash+", "id": "Unsplash+"},
        "date": "2023-04-02",
    },
    145: {
        "bundle": ROOT / "content/post/高配当株まとめ",
        "slug": "高配当株まとめ",
        "links": ["https://www2.jpx.co.jp/tseHpFront/JJK020010Action.do", "https://www.fsa.go.jp/sesc/support/advice.html", "https://www.jsda.or.jp/en/about/major-activities/content/Sales_Representatives_Manual_Volume1_EnglishEdition.pdf"],
        "markers": ["8306", "3003"],
        "scopeMarkers": {"ja":"2024-12-22", "en":"2024-12-22", "zh-cn":"2024-12-22", "es":"2024-12-22", "ko":"2024-12-22", "pt":"2024-12-22", "zh-tw":"2024-12-22", "hi":"2024-12-22", "fr":"2024-12-22", "de":"2024-12-22", "ar":"2024-12-22", "ru":"2024-12-22", "id":"2024-12-22"},
        "date": "2024-12-22",
    },
    144: {
        "bundle": ROOT / "content/post/Salesforceチャッター全消しコマンド",
        "slug": "Salesforceチャッター全消しコマンド",
        "links": ["https://help.salesforce.com/s/articleView?id=experience.collab_posts_parent.htm&language=en_US&type=5", "https://help.salesforce.com/s/articleView?id=xcloud.admin_monitorresources.htm&language=en_US&type=5", "https://help.salesforce.com/s/articleView?id=000198685&language=en_US&type=1", "https://developer.salesforce.com/docs/platform/object-reference/references/standard-objects/object-feeditem.html", "https://help.salesforce.com/s/articleView?id=experience.collab_attachments_del.htm&language=en_US&type=5"],
        "markers": ["Type='ContentPost'", "Data Loader"],
        "scopeMarkers": {"ja":"Storage Usage", "en":"Storage Usage", "zh-cn":"Storage Usage", "es":"Storage Usage", "ko":"Storage Usage", "pt":"Storage Usage", "zh-tw":"Storage Usage", "hi":"Storage Usage", "fr":"Storage Usage", "de":"Storage Usage", "ar":"Storage Usage", "ru":"Storage Usage", "id":"Storage Usage"},
        "date": "2022-09-19",
    },
    143: {
        "bundle": ROOT / "content/post/マルチモニタで毎回起動時にDPIの設定がリセットされてしまうときの対処法",
        "slug": "マルチモニタで毎回起動時にDPIの設定がリセットされてしまうときの対処法",
        "links": ["https://support.microsoft.com/en-us/windows/experience/power-battery/shut-down-sleep-or-hibernate-your-pc", "https://learn.microsoft.com/en-us/windows/win32/power/system-power-states", "https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/distinguishing-fast-startup-from-wake-from-hibernation"],
        "markers": ["Fast Startup"],
        "scopeMarkers": {"ja":"Shut down, sleep, or hibernate your PC", "en":"Shut down, sleep, or hibernate your PC", "zh-cn":"Shut down, sleep, or hibernate your PC", "es":"Shut down, sleep, or hibernate your PC", "ko":"Shut down, sleep, or hibernate your PC", "pt":"Shut down, sleep, or hibernate your PC", "zh-tw":"Shut down, sleep, or hibernate your PC", "hi":"Shut down, sleep, or hibernate your PC", "fr":"Shut down, sleep, or hibernate your PC", "de":"Shut down, sleep, or hibernate your PC", "ar":"Shut down, sleep, or hibernate your PC", "ru":"Shut down, sleep, or hibernate your PC", "id":"Shut down, sleep, or hibernate your PC"},
        "date": "2024-04-29",
    },
    142: {
        "bundle": ROOT / "content/post/SalesforceのSOQLを利用して日別のレコード作成数を取得する方法",
        "slug": "SalesforceのSOQLを利用して日別のレコード作成数を取得する方法",
        "links": ["https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-date-functions.html", "https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-convert-time-zone.html", "https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-agg_functions.html", "https://help.salesforce.com/s/articleView?id=code_dev_console_tab_query_editor_soql_sosl.htm&language=en_US&type=0"],
        "markers": ["DAY_ONLY(convertTimezone(CreatedDate))", "COUNT(Id)"],
        "scopeMarkers": {"ja":"ORDER BY COUNT(Id) DESC", "en":"ORDER BY COUNT(Id) DESC", "zh-cn":"ORDER BY COUNT(Id) DESC", "es":"ORDER BY COUNT(Id) DESC", "ko":"ORDER BY COUNT(Id) DESC", "pt":"ORDER BY COUNT(Id) DESC", "zh-tw":"ORDER BY COUNT(Id) DESC", "hi":"ORDER BY COUNT(Id) DESC", "fr":"ORDER BY COUNT(Id) DESC", "de":"ORDER BY COUNT(Id) DESC", "ar":"ORDER BY COUNT(Id) DESC", "ru":"ORDER BY COUNT(Id) DESC", "id":"ORDER BY COUNT(Id) DESC"},
        "date": "2023-04-09",
    },
    141: {
        "bundle": ROOT / "content/post/大きなフォルダーを高速一括削除",
        "slug": "大きなフォルダーを高速一括削除",
        "links": ["https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/del", "https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rmdir"],
        "markers": ["DEL/F/Q/S", "RMDIR/S/Q"],
        "scopeMarkers": {"ja":"dir /a \"Large Folder\"", "en":"dir /a \"Large Folder\"", "zh-cn":"dir /a \"Large Folder\"", "es":"dir /a \"Large Folder\"", "ko":"dir /a \"Large Folder\"", "pt":"dir /a \"Large Folder\"", "zh-tw":"dir /a \"Large Folder\"", "hi":"dir /a \"Large Folder\"", "fr":"dir /a \"Large Folder\"", "de":"dir /a \"Large Folder\"", "ar":"dir /a \"Large Folder\"", "ru":"dir /a \"Large Folder\"", "id":"dir /a \"Large Folder\""},
        "date": "2022-09-20",
    },
    140: {
        "bundle": ROOT / "content/post/好きな数式",
        "slug": "好きな数式",
        "links": ["https://mathworld.wolfram.com/WilsonsTheorem.html", "https://euler.euclid.int/about-eulers-identity/", "https://www.maths.cam.ac.uk/features/node/153", "https://clp.math.uky.edu/clp2/chap_seq_ser-5.html", "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1F76183BF30CECE688E31E8F10F37AC8/S0025557224000111a.pdf/eulers_primeproducing_polynomial_revisited.pdf"],
        "markers": ["1681"],
        "scopeMarkers": {"ja":"n=40", "en":"n=40", "zh-cn":"n=40", "es":"n=40", "ko":"n=40", "pt":"n=40", "zh-tw":"n=40", "hi":"n=40", "fr":"n=40", "de":"n=40", "ar":"n=40", "ru":"n=40", "id":"n=40"},
        "date": "2022-10-05",
    },
    139: {
        "bundle": ROOT / "content/post/SalesforceおすすめChrome拡張",
        "slug": "SalesforceおすすめChrome拡張",
        "links": ["https://chromewebstore.google.com/detail/salesforce-devtools/ehgmhinnhggigkogkbhnbodhbfjgncjf", "https://chromewebstore.google.com/detail/salesforce-advanced-code/lnkgcmpjkkkeffambkllliefdpjdklmi", "https://sf-advanced-code-searcher.web.app/"],
        "markers": ["Salesforce DevTools", "Salesforce advanced Code searcher", "Salesforce REST API"],
        "scopeMarkers": {"ja":"業務用組織に接続する前に", "en":"Before connecting either extension to a work org", "zh-cn":"连接工作组织前请查看最新权限与隐私说明", "es":"Antes de conectar una organización de trabajo revisa los permisos", "ko":"업무용 조직에 연결하기 전에 최신 권한", "pt":"Antes de conectar uma organização de trabalho confira as permissões", "zh-tw":"連接工作組織前請先查看最新權限", "hi":"काम के संगठन से जोड़ने से पहले मौजूदा अनुमतियाँ", "fr":"Avant de connecter une organisation professionnelle vérifiez les autorisations", "de":"Prüfen Sie vor einer Verbindung mit einer Arbeitsorganisation die aktuellen Berechtigungs", "ar":"قبل ربط أي منهما بمؤسسة العمل راجع الأذونات", "ru":"Перед подключением к рабочей организации проверьте актуальные разрешения", "id":"Sebelum menghubungkannya ke organisasi kerja periksa izin"},
        "date": "2022-05-02",
    },
    138: {
        "bundle": ROOT / "content/post/macでコピー＆ペーストのショートカットキーをWindowsと合わせる方法",
        "slug": "macでコピー＆ペーストのショートカットキーをWindowsと合わせる方法",
        "links": ["https://support.apple.com/en-ie/guide/mac-help/mchlp1011/27/mac/27"],
        "markers": ["Control", "Command"],
        "scopeMarkers": {"ja":"すべてのショートカットに影響します", "en":"affects every shortcut using Control or Command", "zh-cn":"所有使用 Control 或 Command 的快捷键", "es":"todos los atajos que usan Control o Command", "ko":"모든 단축키에 적용됩니다", "pt":"todos os atalhos que usam Control ou Command", "zh-tw":"所有使用 Control 或 Command 的快速鍵", "hi":"सभी शॉर्टकट को प्रभावित करता है", "fr":"tous les raccourcis utilisant Control ou Command", "de":"alle Kurzbefehle mit Control oder Command", "ar":"كل الاختصارات التي تستخدم Control أو Command", "ru":"все сочетания с Control или Command", "id":"semua pintasan yang menggunakan Control atau Command"},
        "date": "2023-04-05",
    },
    137: {
        "bundle": ROOT / "content/post/macOSで.DS_Storeを自動生成しないようにするコマンド",
        "slug": "macOSで.DS_Storeを自動生成しないようにするコマンド",
        "links": ["https://support.apple.com/en-us/102064"],
        "markers": [
            "defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE",
            "defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool FALSE",
        ],
        "scopeMarkers": {"ja":"SMB共有上の.DS_Store", "en":".DS_Store files on SMB shares", "zh-cn":"SMB 共享上的 .DS_Store 文件", "es":"archivos `.DS_Store` en recursos compartidos SMB", "ko":"SMB 공유의 `.DS_Store` 파일", "pt":"arquivos `.DS_Store` em compartilhamentos SMB", "zh-tw":"SMB 分享上的 `.DS_Store` 檔案", "hi":"SMB शेयरों पर `.DS_Store` फ़ाइलें", "fr":"fichiers `.DS_Store` sur les partages SMB", "de":"`.DS_Store`-Dateien auf SMB-Freigaben", "ar":"ملفات `.DS_Store` على مشاركات SMB", "ru":"файлы `.DS_Store` на SMB-ресурсах", "id":"file `.DS_Store` pada berbagi SMB"},
        "date": "2022-09-12",
    },
    136: {
        "bundle": ROOT / "content/post/Rustの特徴",
        "slug": "Rustの特徴",
        "links": [
            "https://www.rust-lang.org/",
            "https://blog.rust-lang.org/2020/08/18/laying-the-foundation-for-rusts-future.html",
            "https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html",
            "https://doc.rust-lang.org/cargo/",
            "https://doc.rust-lang.org/rustc/platform-support.html",
            "https://doc.rust-lang.org/book/ch20-01-unsafe-rust.html",
        ],
        "markers": ["Cargo", "2015", "unsafe"],
        "date": "2022-10-03",
    },
    135: {
        "bundle": ROOT / "content/post/今のメインPCスペック",
        "slug": "今のメインPCスペック",
        "links": [
            "https://www.intel.com/content/www/us/en/products/sku/126684/intel-core-i78700k-processor-12m-cache-up-to-4-70-ghz/specifications.html",
            "https://learn.microsoft.com/en-us/windows/release-health/windows11-release-information",
        ],
        "markers": ["Corei7-8700K", "32.0GB", "Windows11Enterprise", "22000.856", "3.70GHz"],
        "scopeMarkers": {"ja":"2022年9月8日時点の記録", "en":"snapshot recorded on September 8, 2022", "zh-cn":"截至 2022 年 9 月 8 日的记录", "es":"registro del 8 de septiembre de 2022", "ko":"2022년 9월 8일 당시의 기록", "pt":"registro de 8 de setembro de 2022", "zh-tw":"截至 2022 年 9 月 8 日的記錄", "hi":"8 सितंबर 2022 का रिकॉर्ड", "fr":"relevé du 8 septembre 2022", "de":"Momentaufnahme vom 8. September 2022", "ar":"سجل مؤرخ في 8 سبتمبر 2022", "ru":"запись от 8 сентября 2022 года", "id":"catatan per 8 September 2022"},
        "date": "2022-09-08",
    },
    134: {
        "bundle": ROOT / "content/post/なぜ数学や計算機が好きなんだろう",
        "slug": "なぜ数学や計算機が好きなんだろう",
        "links": [
            "https://plato.stanford.edu/entries/logic-propositional/",
            "https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/e4fe97d2a250b57bb1e330fba8cf5992_MIT6_172F18_lec16.pdf",
        ],
        "markers": [],
        "scopeMarkers": {"ja":"私自身が感じる魅力", "en":"qualities I personally appreciate", "zh-cn":"这些是我个人感受到的魅力", "es":"Estas son cualidades que yo aprecio personalmente", "ko":"제가 개인적으로 느끼는 매력", "pt":"Estas são qualidades que eu aprecio pessoalmente", "zh-tw":"這些是我個人感受到的魅力", "hi":"ये वे गुण हैं जिन्हें मैं व्यक्तिगत रूप से पसंद करता हूँ", "fr":"Ce sont des qualités que j’apprécie personnellement", "de":"Das sind Eigenschaften, die ich persönlich schätze", "ar":"هذه جوانب أقدّرها شخصيًا", "ru":"Это качества, которые ценю лично я", "id":"Ini adalah hal-hal yang saya hargai secara pribadi"},
        "date": "2022-09-23",
    },
    133: {
        "bundle": ROOT / "content/post/gitでタグを消す",
        "slug": "gitでタグを消す",
        "links": [
            "https://git-scm.com/docs/git-tag",
            "https://git-scm.com/docs/git-ls-remote",
            "https://git-scm.com/docs/git-push",
        ],
        "markers": ["git tag -d v0.1.0", "git ls-remote --tags --refs origin", "git push origin --delete v0.1.0"],
        "date": "2022-10-02",
    },
    132: {
        "bundle": ROOT / "content/post/子供のそんたく",
        "slug": "子供のそんたく",
        "links": [],
        "markers": [],
        "scopeMarkers": {"ja":"子供なりにお母さんを気遣っている", "en":"looking out for her mom in her own little way", "zh-cn":"用孩子自己的方式体贴妈妈", "es":"a su manera de niña, estaba cuidando de su madre", "ko":"아이 나름대로 엄마를 배려하는구나", "pt":"à sua maneira de criança, ela estava cuidando da mãe", "zh-tw":"用孩子自己的方式體貼媽媽", "hi":"अपने बचपन के तरीके से माँ का खयाल रख रही थी", "fr":"elle veillait sur sa mère à sa façon d’enfant", "de":"auf ihre kindliche Weise Rücksicht auf ihre Mutter nahm", "ar":"تراعي أمها بطريقتها الطفولية", "ru":"по-детски она заботится о маме", "id":"memperhatikan ibunya dengan caranya sendiri sebagai anak kecil"},
        "date": "2022-09-07",
    },
    131: {
        "bundle": ROOT / "content/post/ウィンドウタイトルの列挙",
        "slug": "ウィンドウタイトルの列挙",
        "links": [
            "https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-process",
            "https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.mainwindowtitle",
        ],
        "markers": ["Get-Process", "MainWindowTitle", "ProcessName,Id,MainWindowTitle"],
        "scopeMarkers": {"ja":"プロセスごとのメインウィンドウのタイトル", "en":"main-window title for each process", "zh-cn":"每个进程的主窗口标题", "es":"título de la ventana principal de cada proceso", "ko":"프로세스별 기본 창 제목", "pt":"título da janela principal de cada processo", "zh-tw":"每個處理程序的主視窗標題", "hi":"हर प्रक्रिया की मुख्य विंडो का शीर्षक", "fr":"titre de la fenêtre principale de chaque processus", "de":"Titel des Hauptfensters jedes Prozesses", "ar":"عنوان النافذة الرئيسية لكل عملية", "ru":"заголовок главного окна каждого процесса", "id":"judul jendela utama untuk setiap proses"},
        "date": "2022-09-20",
    },
    129: {
        "bundle": ROOT / "content/post/おすすめのビジネス書",
        "slug": "おすすめのビジネス書",
        "links": ["https://amzn.to/3YTv0Dr", "https://amzn.to/3n3SVCQ", "https://amzn.to/3TtKUDf", "https://amzn.to/3TqfjSO"],
        "markers": ["Amazon.co.jp"],
        "date": "2023-03-19",
    },
    128: {
        "bundle": ROOT / "content/post/git resetを取り消す方法",
        "slug": "git resetを取り消す方法",
        "links": ["https://git-scm.com/docs/git-reset", "https://git-scm.com/docs/git-reflog"],
        "markers": ["git reflog --date=local", "git reset --hard rescue-before-reset"],
        "date": "2024-05-15",
    },
    127: {
        "bundle": ROOT / "content/post/カフェ音楽",
        "slug": "カフェ音楽",
        "links": ["https://www.youtube.com/watch?v=1hY8f20tqlI", "https://www.youtube.com/watch?v=jfKfPfyJRdk", "https://www.youtube.com/watch?v=bz5q5gl2uZA", "https://www.youtube.com/watch?v=fWX8zsaTeTc"],
        "markers": [],
        "scopeMarkers": {"ja":"Café Swing | Electro Swing Mix 2019","en":"Café Swing | Electro Swing Mix 2019","zh-cn":"Café Swing | Electro Swing Mix 2019","es":"Café Swing | Electro Swing Mix 2019","ko":"Café Swing | Electro Swing Mix 2019","pt":"Café Swing | Electro Swing Mix 2019","zh-tw":"Café Swing | Electro Swing Mix 2019","hi":"Café Swing | Electro Swing Mix 2019","fr":"Café Swing | Electro Swing Mix 2019","de":"Café Swing | Electro Swing Mix 2019","ar":"Café Swing | Electro Swing Mix 2019","ru":"Café Swing | Electro Swing Mix 2019","id":"Café Swing | Electro Swing Mix 2019"},
        "date": "2022-09-08",
    },
    126: {
        "bundle": ROOT / "content/post/eguiを使ってみる",
        "slug": "eguiを使ってみる",
        "links": ["https://github.com/emilk/egui", "https://github.com/emilk/eframe_template", "https://docs.rs/egui/latest/egui/"],
        "markers": ["eframe_template.git", "cargo run --release"],
        "date": "2023-03-18",
    },
    125: {
        "bundle": ROOT / "content/post/自分にできないことができる人に敬意を払おう",
        "slug": "自分にできないことができる人に敬意を払おう",
        "links": [],
        "markers": [],
        "scopeMarkers": {"ja": "敬意を払おう", "en": "Respect", "zh-cn": "尊重", "es": "Respet", "ko": "존중", "pt": "Respeit", "zh-tw": "尊重", "hi": "सम्मान", "fr": "Respect", "de": "RespektierenwirMenschen", "ar": "لنحترم", "ru": "Уважать", "id": "Hormati"},
        "date": "2023-08-01",
    },
    124: {
        "bundle": ROOT / "content/post/生成AIについて",
        "slug": "生成AIについて",
        "links": ["https://www.jnpc.or.jp/archive/conferences/36601/report", "https://www.jnpc.or.jp/archive/conferences/36631/report", "https://www.jnpc.or.jp/archive/conferences/36714/report"],
        "markers": [],
        "scopeMarkers": {"ja": "日本記者クラブの会見記録", "en": "Japan National Press Club event record", "zh-cn": "日本记者俱乐部会见记录", "es": "Registro del Japan National Press Club", "ko": "일본기자클럽 행사 기록", "pt": "Registro do Japan National Press Club", "zh-tw": "日本記者俱樂部會見紀錄", "hi": "Japan National Press Club का कार्यक्रम विवरण", "fr": "Compte rendu du Japan National Press Club", "de": "Veranstaltungsbericht des Japan National Press Club", "ar": "سجل الفعالية لدى نادي الصحافة الوطني الياباني", "ru": "Запись мероприятия Японского национального пресс-клуба", "id": "Catatan acara Japan National Press Club"},
        "date": "2024-04-16",
    },
    123: {
        "bundle": ROOT / "content/post/何年かぶりの神座（かむくら）（ラーメン）",
        "slug": "何年かぶりの神座（かむくら）（ラーメン）",
        "links": [],
        "markers": [],
        "scopeMarkers": {"ja": "ネギキムチラーメン", "en": "Green Onion Kimchi Ramen", "zh-cn": "葱花泡菜拉面", "es": "Ramen de cebolla verde y kimchi", "ko": "파김치 라멘", "pt": "Ramen de Kimchi e Cebolinha", "zh-tw": "蔥泡菜拉麵", "hi": "हरी प्याज किमची रामेन", "fr": "Ramen au Kimchi et à la Ciboule", "de": "Frühlingszwiebel-Kimchi-Ramen", "ar": "رامن كيمتشي البصل الأخضر", "ru": "Рамэн с зеленым луком и кимчи", "id": "Ramen Daun Bawang Kimchi"},
        "date": "2022-09-09",
    },
    122: {
        "bundle": ROOT / "content/post/今日の作業環境",
        "slug": "今日の作業環境",
        "links": [],
        "markers": [],
        "scopeMarkers": {"ja": "子供の机", "en": "Children's Desk", "zh-cn": "孩子的书桌", "es": "El escritorio del niño", "ko": "아이의 책상", "pt": "Mesa das crianças", "zh-tw": "孩子的書桌", "hi": "बच्चों की मेज", "fr": "Le bureau des enfants", "de": "Kinderschreibtisch", "ar": "مكتب الطفل", "ru": "Детский стол", "id": "Meja Anak"},
        "date": "2022-09-04",
    },
    121: {
        "bundle": ROOT / "content/post/gitリポジトリの最新だけ取得する",
        "slug": "gitリポジトリの最新だけ取得する",
        "links": ["https://git-scm.com/docs/git-clone", "https://git-scm.com/docs/git-fetch"],
        "markers": ["--depth 1", "--single-branch", "--deepen=50", "--unshallow"],
        "date": "2024-04-27",
    },
    120: {
        "bundle": ROOT / "content/post/iPhoneにSIMロックがかかっているか確認する方法",
        "slug": "iPhoneにSIMロックがかかっているか確認する方法",
        "links": [
            "https://support.apple.com/en-us/109316",
            "https://support.apple.com/ja-jp/109316",
            "https://support.apple.com/ja-jp/104999",
        ],
        "markers": ["iPhone", "eSIM"],
        "date": "2024-09-12",
    },
    119: {
        "bundle": ROOT / "content/post/なぜ青色LEDを作ることがほぼ不可能だったのか",
        "slug": "なぜ青色LEDを作ることがほぼ不可能だったのか",
        "links": [
            "https://www.nobelprize.org/prizes/physics/2014/press-release/",
            "https://www.youtube.com/watch?v=AF8d72mA41M",
        ],
        "markers": ["GaN", "2014"],
        "date": "2024-09-15",
    },
    118: {
        "bundle": ROOT / "content/post/fontplus.jp",
        "slug": "fontplus.jp",
        "links": ["https://fontplus.jp/service/pricing", "https://fontplus.jp/"],
        "markers": ["FONTPLUS"],
        "date": "2023-02-07",
    },
    117: {
        "bundle": ROOT / "content/post/Qiskit入門",
        "slug": "qiskit-quantum-programming-intro",
        "links": [
            "https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit",
            "https://quantum.cloud.ibm.com/docs/en/guides/local-simulators",
            "https://quantum.cloud.ibm.com/docs/en/guides/qiskit-1.0-features",
            "https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.QuantumCircuit",
            "https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html",
        ],
        "markers": ["AerSimulator", "measure_all()", "qiskit-aer", "|00", "|11"],
        "date": "2026-09-11",
    },
    116: {
        "bundle": ROOT / "content/post/P≠NP予想",
        "slug": "P≠NP予想",
        "links": [
            "https://www.claymath.org/millennium/p-vs-np/",
            "https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf",
            "https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/f2829e57caade7e7f21d765b8e7b9058_MIT6_046JS15_lec16.pdf",
        ],
        "markers": ["P = NP", "P ⊆ NP", "P ≠ NP", "SAT"],
        "date": "2024-09-11",
    },
    115: {
        "bundle": ROOT / "content/post/Python不要C++だけでAI推論エンジンを構築してみた",
        "slug": "building-ai-inference-engine-cpp-only",
        "links": [
            "https://github.com/ggml-org/ggml",
            "https://github.com/ggml-org/llama.cpp",
            "https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md",
            "https://docs.nvidia.com/cuda/cublas/index.html",
            "https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixmultiplication",
            "https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/n5014.pdf",
        ],
        "markers": ["MemoryArena", "std::align_val_t", "std::bad_alloc()", "28,000,000,000", "cuBLAS", "Metal Performance Shaders"],
        "date": "2026-09-11",
    },
}


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = self.direction = ""
        self.canonical = []
        self.hreflang = {}
        self.links = []
        self.text = []
        self.title = []
        self.description = []
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "html":
            self.lang, self.direction = values.get("lang", ""), values.get("dir", "")
        elif tag == "link" and "canonical" in values.get("rel", "").split():
            self.canonical.append(values.get("href", ""))
        elif tag == "link" and values.get("hreflang"):
            self.hreflang[values["hreflang"]] = values.get("href", "")
        elif tag == "a" and values.get("href"):
            self.links.append(values["href"])
        elif tag == "meta" and values.get("name", "").lower() == "description":
            self.description.append(values.get("content", ""))
        elif tag == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        self.text.append(data)
        if self.in_title:
            self.title.append(data)


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "kenji.blog-translation-review/1.0", "Cache-Control": "no-cache"})
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.status, response.read()


def yaml_value(path, key):
    match = re.search(rf"^{key}:\s*(.*?)\s*$", path.read_text(encoding="utf-8-sig"), re.M)
    if not match:
        raise ValueError(f"Missing {key}: {path}")
    value = match.group(1)
    if value.startswith('"'):
        return json.loads(value)
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    return value


def slug_key(value):
    return re.sub(r"[^0-9a-z\u3040-\u30ff\u3400-\u9fff\uac00-\ud7af]", "", value.casefold())


parser = argparse.ArgumentParser()
parser.add_argument("--ci-run", type=int, required=True)
parser.add_argument("--commit", required=True)
parser.add_argument("--max-batch", type=int, choices=(90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176), default=176)
args = parser.parse_args()
ARTICLES = {number: article for number, article in ARTICLES.items() if number <= args.max_batch}
with urllib.request.urlopen(f"https://github.com/kenjinote/blog/actions/runs/{args.ci_run}", timeout=45) as response:
    run = response.read().decode("utf-8", "replace")
if '<span class="h4 color-fg-default">Success</span>' not in run or args.commit[:7] not in run:
    raise SystemExit("Specified GitHub run does not confirm success for this commit")

with urllib.request.urlopen("https://kenji.blog/sitemap.xml", timeout=45) as response:
    sitemap = ET.fromstring(response.read())
japanese_map = next((item.find("s:loc", NS).text for item in sitemap.findall("s:sitemap", NS) if "/ja/sitemap.xml" in item.find("s:loc", NS).text), None)
if not japanese_map:
    raise SystemExit("Japanese sitemap is missing")
with urllib.request.urlopen(japanese_map, timeout=45) as response:
    sitemap = ET.fromstring(response.read())
all_urls = [item.find("s:loc", NS).text for item in sitemap.findall("s:url", NS)]

results = {}
for batch_number, article in ARTICLES.items():
    bundle = article["bundle"]
    slug = slug_key(article["slug"])
    japanese_url = next((url for url in all_urls if urlparse(unquote(url)).path.startswith("/p/") and slug_key(urlparse(unquote(url)).path.rstrip("/").split("/")[-1]) == slug), None)
    if not japanese_url:
        raise SystemExit(f"Batch {batch_number}: Japanese article missing from sitemap")
    _, raw = fetch(japanese_url)
    root_page = Page()
    root_page.feed(raw.decode("utf-8", "replace"))
    targets = set(root_page.hreflang.values())
    if len(targets) != 13 or len(root_page.hreflang) != 14:
        raise SystemExit(f"Batch {batch_number}: unexpected hreflang targets")
    pages = []
    for language in LANGS:
        url = next((value for value in targets if (language == "ja" and re.search(r"https://kenji\.blog/p/", value)) or (language != "ja" and f"/{language}/p/" in value)), None)
        if not url:
            pages.append({"language": language, "passed": False, "failure": "hreflang target missing"})
            continue
        status, raw = fetch(url)
        page = Page()
        html = raw.decode("utf-8", "replace")
        page.feed(html)
        path = bundle / ("index.md" if language == "ja" else f"index.{language}.md")
        title = yaml_value(path, "title")
        description = yaml_value(path, "description")
        compact = re.sub(r"\s+", "", "".join(page.text))
        checks = {
            "http200": status == 200,
            "canonical": page.canonical == [url],
            "language": page.lang.lower() == language,
            "arabicRtl": language != "ar" or page.direction == "rtl",
            "title": title in "".join(page.title),
            "description": len(page.description) == 1 and page.description[0].strip() == description,
            "hreflangCount": len(page.hreflang) == 14,
            "hreflangTargets": set(page.hreflang.values()) == targets,
            "officialReferences": (
                all(link in page.links for link in article.get("linksByLanguage", {}).get(language, article.get("links", [])))
                if "links" in article or "linksByLanguage" in article
                else any(article["linkFragment"] in link for link in page.links)
            ),
            "localAssets": all(any(unquote(urlparse(link).path).endswith(asset) for link in page.links) for asset in article.get("assets", [])),
            "articleInstructions": all(marker in compact for marker in article["markers"])
            and re.sub(r"\s+", "", article.get("scopeMarkers", {}).get(language, "")) in compact,
            "noKnownBadLinks": not any(link in page.links for link in ("https://kenji.blog/es/p/kubernetes-k8s-architecture-pod-service-ingress/", "/hi/p/logicpad-windows-app-development-journey/")),
            "dates": yaml_value(path, "date").startswith(article["date"]) and yaml_value(path, "lastmod").startswith("2026-11-24"),
        }
        pages.append({"language": language, "url": url, "status": status, "checks": checks, "passed": all(checks.values())})
    results[batch_number] = {"pages": pages, "allPassed": len(pages) == 13 and all(page["passed"] for page in pages)}

passed = len(results) == len(ARTICLES) and all(result["allPassed"] for result in results.values())
receipt = {
    "version": 1,
    "batches": list(ARTICLES),
    "verifiedAt": datetime.now().astimezone().isoformat(timespec="seconds"),
    "ciRun": args.ci_run,
    "ciUrl": f"https://github.com/kenjinote/blog/actions/runs/{args.ci_run}",
    "sourceCommit": args.commit,
    "deployment": "success" if passed else "verification_failed",
    "pagesVerified": sum(sum(page["passed"] for page in result["pages"]) for result in results.values()),
    "allPassed": passed,
    "results": results,
    "limitations": ["AI-assisted translation reviews only; no human or native-speaker certification.", "IDE menus and account plan details can change; each article links to current official references."],
}
(DOCS / f"publication-087-{args.max_batch:03}.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
if passed:
    for batch_number in ARTICLES:
        path = DOCS / f"batch-{batch_number:03}.json"
        entry = json.loads(path.read_text(encoding="utf-8"))
        entry["publicationPending"] = False
        entry["publication"] = {"record": f"docs/translation-review/publication-087-{args.max_batch:03}.json", "ciRun": args.ci_run, "sourceCommit": args.commit, "allPassed": True}
        path.write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"allPassed": passed, "pages": receipt["pagesVerified"], "failures": {batch: [page for page in value["pages"] if not page["passed"]] for batch, value in results.items()}}, ensure_ascii=False, indent=2))
if not passed:
    raise SystemExit(1)
