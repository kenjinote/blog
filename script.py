import os
import re

source_file = r'c:\work\kenji.blog\content\post\プログラミング言語一覧\index.md'
base_dir = os.path.dirname(source_file)

with open(source_file, 'r', encoding='utf-8') as f:
    text = f.read()

translations = {
    'pt': {
        'title': 'Lista de Linguagens de Programação',
        'C言語': 'C',
        'プログラミング言語一覧': 'Lista de Linguagens de Programação',
        'INRIA（フランス国立情報学自動制御研究所）で開発されている関数型言語の一種。': 'Um tipo de linguagem funcional desenvolvida no INRIA (Instituto Nacional de Pesquisa em Informática e Automação da França).',
        'プログラミング言語であり、LISP系の言語の方言の一つ': 'Uma linguagem de programação e um dos dialetos da família de linguagens LISP.',
        'シンプルなプログラミング言語': 'Uma linguagem de programação simples.',
        'コンピュータにおいて汎用的な用途に使うことができる並行処理指向のオープンソースソフトウェア（英：Open Source Software、略：OSS）プログラミング言語および実行環境。': 'Uma linguagem de programação de software de código aberto (OSS) voltada para concorrência e ambiente de execução que pode ser usada para propósitos gerais em computadores.',
        'スタック指向のプログラミング言語': 'Linguagem de programação orientada a pilhas.',
        'D言語は強い静的型付け言語': 'A linguagem D é uma linguagem fortemente tipada estaticamente.',
        'Eiffelはオブジェクト指向プログラミング言語のひとつ': 'Eiffel é uma linguagem de programação orientada a objetos.',
        'Adaはオブジェクト指向プログラミング言語のひとつ': 'Ada é uma linguagem de programação orientada a objetos.',
        'Pascalは手続き型プログラミング言語のひとつ': 'Pascal é uma linguagem de programação procedural.',
        '昔からある。汎用のプログラミング言語である。': 'Existe há muito tempo. É uma linguagem de programação de uso geral.',
        '数値計算に特化したプログラミング言語': 'Linguagem de programação especializada em cálculos numéricos.',
        '機械語と1対1に対応するプログラミング言語': 'Linguagem de programação com correspondência de 1 para 1 com a linguagem de máquina.',
        '手続き型プログラミング言語のひとつ。 名前は「beginners\' all-purpose symbolic instruction code」のバクロニムである。': 'Uma linguagem de programação procedural. O nome é um acrônimo para "beginners\' all-purpose symbolic instruction code".',
        'オブジェクト指向プログラミング言語': 'Linguagem de programação orientada a objetos.',
        '前置記法で記述するプログラミング言語': 'Linguagem de programação escrita com notação de prefixo.',
        'MLは関数型プログラミング言語の一つ': 'ML é uma linguagem de programação funcional.',
        '関係を定義し問題を解くために使われるプログラミング言語': 'Linguagem de programação usada para definir relacionamentos e resolver problemas.',
        'OpenGLのシェーダー言語': 'Linguagem de shader do OpenGL.',
        'リレーショナルデータを操作するための言語': 'Linguagem para manipulação de dados relacionais.',
        'Adobeが開発した印刷用のスクリプト言語': 'Linguagem de script para impressão desenvolvida pela Adobe.',
        'Windows標準でインストールされている。オブジェクトが扱える。': 'Instalado por padrão no Windows. Pode manipular objetos.',
        'Javaによく似た言語': 'Uma linguagem muito semelhante ao Java.'
    },
    'zh-tw': {
        'title': '程式語言列表',
        'C言語': 'C',
        'プログラミング言語一覧': '程式語言列表',
        'INRIA（フランス国立情報学自動制御研究所）で開発されている関数型言語の一種。': '在 INRIA（法國國家資訊與自動化研究所）開發的一種函數式語言。',
        'プログラミング言語であり、LISP系の言語の方言の一つ': '一種程式語言，也是 LISP 語言家族的方言之一。',
        'シンプルなプログラミング言語': '簡單的程式語言。',
        'コンピュータにおいて汎用的な用途に使うことができる並行処理指向のオープンソースソフトウェア（英：Open Source Software、略：OSS）プログラミング言語および実行環境。': '一種可用於電腦通用目的之並行處理導向開源軟體 (OSS) 程式語言及執行環境。',
        'スタック指向のプログラミング言語': '堆疊導向的程式語言。',
        'D言語は強い静的型付け言語': 'D 語言是一種強靜態型別語言。',
        'Eiffelはオブジェクト指向プログラミング言語のひとつ': 'Eiffel 是一種物件導向程式語言。',
        'Adaはオブジェクト指向プログラミング言語のひとつ': 'Ada 是一種物件導向程式語言。',
        'Pascalは手続き型プログラミング言語のひとつ': 'Pascal 是一種程序式程式語言。',
        '昔からある。汎用のプログラミング言語である。': '歷史悠久。是一種通用程式語言。',
        '数値計算に特化したプログラミング言語': '專門用於數值計算的程式語言。',
        '機械語と1対1に対応するプログラミング言語': '與機器語言一對一對應的程式語言。',
        '手続き型プログラミング言語のひとつ。 名前は「beginners\' all-purpose symbolic instruction code」のバクロニムである。': '程序式程式語言之一。其名稱是「beginners\' all-purpose symbolic instruction code」的首字母縮略詞。',
        'オブジェクト指向プログラミング言語': '物件導向程式語言。',
        '前置記法で記述するプログラミング言語': '使用前綴表示法撰寫的程式語言。',
        'MLは関数型プログラミング言語の一つ': 'ML 是一種函數式程式語言。',
        '関係を定義し問題を解くために使われるプログラミング言語': '用於定義關係並解決問題的程式語言。',
        'OpenGLのシェーダー言語': 'OpenGL 的著色器語言。',
        'リレーショナルデータを操作するための言語': '用於操作關聯式資料的語言。',
        'Adobeが開発した印刷用のスクリプト言語': 'Adobe 開發的列印用指令碼語言。',
        'Windows標準でインストールされている。オブジェクトが扱える。': 'Windows 標準內建安裝。可以處理物件。',
        'Javaによく似た言語': '與 Java 非常相似的語言。'
    },
    'hi': {
        'title': 'प्रोग्रामिंग भाषाओं की सूची',
        'C言語': 'C',
        'プログラミング言語一覧': 'प्रोग्रामिंग भाषाओं की सूची',
        'INRIA（フランス国立情報学自動制御研究所）で開発されている関数型言語の一種。': 'INRIA (फ्रांसीसी राष्ट्रीय कंप्यूटर विज्ञान और स्वचालन अनुसंधान संस्थान) में विकसित एक प्रकार की कार्यात्मक भाषा।',
        'プログラミング言語であり、LISP系の言語の方言の一つ': 'एक प्रोग्रामिंग भाषा और LISP भाषा परिवार की एक बोली।',
        'シンプルなプログラミング言語': 'एक सरल प्रोग्रामिंग भाषा।',
        'コンピュータにおいて汎用的な用途に使うことができる並行処理指向のオープンソースソフトウェア（英：Open Source Software、略：OSS）プログラミング言語および実行環境。': 'कंप्यूटर में सामान्य उद्देश्य के अनुप्रयोगों के लिए उपयोग की जा सकने वाली समवर्ती प्रसंस्करण-उन्मुख ओपन-सोर्स सॉफ्टवेयर (OSS) प्रोग्रामिंग भाषा और रनटाइम वातावरण।',
        'スタック指向のプログラミング言語': 'स्टैक-उन्मुख प्रोग्रामिंग भाषा।',
        'D言語は強い静的型付け言語': 'D भाषा एक मजबूत स्थिर रूप से टाइप की गई भाषा है।',
        'Eiffelはオブジェクト指向プログラミング言語のひとつ': 'Eiffel एक ऑब्जेक्ट-ओरिएंटेड प्रोग्रामिंग भाषा है।',
        'Adaはオブジェクト指向プログラミング言語のひとつ': 'Ada एक ऑब्जेक्ट-ओरिएंटेड प्रोग्रामिंग भाषा है।',
        'Pascalは手続き型プログラミング言語のひとつ': 'Pascal एक प्रक्रियात्मक प्रोग्रामिंग भाषा है।',
        '昔からある。汎用のプログラミング言語である。': 'यह बहुत पहले से मौजूद है। यह एक सामान्य-उद्देश्य वाली प्रोग्रामिंग भाषा है।',
        '数値計算に特化したプログラミング言語': 'संख्यात्मक गणना के लिए विशेष प्रोग्रामिंग भाषा।',
        '機械語と1対1に対応するプログラミング言語': 'मशीन भाषा के साथ 1-से-1 पत्राचार वाली प्रोग्रामिंग भाषा।',
        '手続き型プログラミング言語のひとつ。 名前は「beginners\' all-purpose symbolic instruction code」のバクロニムである。': 'एक प्रक्रियात्मक प्रोग्रामिंग भाषा। नाम "beginners\' all-purpose symbolic instruction code" का एक एक्रोनिम है।',
        'オブジェクト指向プログラミング言語': 'ऑब्जेक्ट-ओरिएंटेड प्रोग्रामिंग भाषा।',
        '前置記法で記述するプログラミング言語': 'उपसर्ग संकेतन (prefix notation) के साथ लिखी गई प्रोग्रामिंग भाषा।',
        'MLは関数型プログラミング言語の一つ': 'ML एक कार्यात्मक प्रोग्रामिंग भाषा है।',
        '関係を定義し問題を解くために使われるプログラミング言語': 'संबंधों को परिभाषित करने और समस्याओं को हल करने के लिए उपयोग की जाने वाली प्रोग्रामिंग भाषा।',
        'OpenGLのシェーダー言語': 'OpenGL की शेडर भाषा।',
        'リレーショナルデータを操作するための言語': 'रिलेशनल डेटा में हेरफेर करने के लिए एक भाषा।',
        'Adobeが開発した印刷用のスクリプト言語': 'Adobe द्वारा विकसित मुद्रण के लिए एक स्क्रिप्ट भाषा।',
        'Windows標準でインストールされている。オブジェクトが扱える。': 'विंडोज़ पर मानक रूप में स्थापित। ऑब्जेक्ट्स को संभाल सकता है।',
        'Javaによく似た言語': 'Java के समान एक भाषा।'
    },
    'fr': {
        'title': 'Liste des langages de programmation',
        'C言語': 'C',
        'プログラミング言語一覧': 'Liste des langages de programmation',
        'INRIA（フランス国立情報学自動制御研究所）で開発されている関数型言語の一種。': 'Un type de langage fonctionnel développé à l\'INRIA (Institut national de recherche en informatique et en automatique).',
        'プログラミング言語であり、LISP系の言語の方言の一つ': 'Un langage de programmation et l\'un des dialectes de la famille des langages LISP.',
        'シンプルなプログラミング言語': 'Un langage de programmation simple.',
        'コンピュータにおいて汎用的な用途に使うことができる並行処理指向のオープンソースソフトウェア（英：Open Source Software、略：OSS）プログラミング言語および実行環境。': 'Un langage de programmation et un environnement d\'exécution de logiciels open source (OSS) orientés traitement simultané qui peuvent être utilisés à des fins générales sur les ordinateurs.',
        'スタック指向のプログラミング言語': 'Langage de programmation orienté pile.',
        'D言語は強い静的型付け言語': 'Le langage D est un langage fortement typé statiquement.',
        'Eiffelはオブジェクト指向プログラミング言語のひとつ': 'Eiffel est un langage de programmation orienté objet.',
        'Adaはオブジェクト指向プログラミング言語のひとつ': 'Ada est un langage de programmation orienté objet.',
        'Pascalは手続き型プログラミング言語のひとつ': 'Pascal est un langage de programmation procédural.',
        '昔からある。汎用のプログラミング言語である。': 'Existe depuis longtemps. C\'est un langage de programmation à usage général.',
        '数値計算に特化したプログラミング言語': 'Langage de programmation spécialisé dans le calcul numérique.',
        '機械語と1対1に対応するプログラミング言語': 'Un langage de programmation avec une correspondance un à un avec le langage machine.',
        '手続き型プログラミング言語のひとつ。 名前は「beginners\' all-purpose symbolic instruction code」のバクロニムである。': 'Un langage de programmation procédural. Le nom est un acronyme de "beginners\' all-purpose symbolic instruction code".',
        'オブジェクト指向プログラミング言語': 'Langage de programmation orienté objet.',
        '前置記法で記述するプログラミング言語': 'Langage de programmation écrit en notation préfixée.',
        'MLは関数型プログラミング言語の一つ': 'ML est un langage de programmation fonctionnel.',
        '関係を定義し問題を解くために使われるプログラミング言語': 'Langage de programmation utilisé pour définir des relations et résoudre des problèmes.',
        'OpenGLのシェーダー言語': 'Le langage de shader d\'OpenGL.',
        'リレーショナルデータを操作するための言語': 'Un langage pour manipuler des données relationnelles.',
        'Adobeが開発した印刷用のスクリプト言語': 'Un langage de script pour l\'impression développé par Adobe.',
        'Windows標準でインストールされている。オブジェクトが扱える。': 'Installé en standard sur Windows. Peut manipuler des objets.',
        'Javaによく似た言語': 'Un langage très similaire à Java.'
    },
    'de': {
        'title': 'Liste der Programmiersprachen',
        'C言語': 'C',
        'プログラミング言語一覧': 'Liste der Programmiersprachen',
        'INRIA（フランス国立情報学自動制御研究所）で開発されている関数型言語の一種。': 'Eine Art funktionale Programmiersprache, die am INRIA (Nationales französisches Forschungsinstitut für Informatik und Automatisierung) entwickelt wurde.',
        'プログラミング言語であり、LISP系の言語の方言の一つ': 'Eine Programmiersprache und ein Dialekt der LISP-Sprachfamilie.',
        'シンプルなプログラミング言語': 'Eine einfache Programmiersprache.',
        'コンピュータにおいて汎用的な用途に使うことができる並行処理指向のオープンソースソフトウェア（英：Open Source Software、略：OSS）プログラミング言語および実行環境。': 'Eine nebenläufige, Open-Source-Software (OSS) Programmiersprache und Laufzeitumgebung, die für allgemeine Zwecke auf Computern verwendet werden kann.',
        'スタック指向のプログラミング言語': 'Stack-orientierte Programmiersprache.',
        'D言語は強い静的型付け言語': 'Die D-Sprache ist eine stark statisch typisierte Sprache.',
        'Eiffelはオブジェクト指向プログラミング言語のひとつ': 'Eiffel ist eine objektorientierte Programmiersprache.',
        'Adaはオブジェクト指向プログラミング言語のひとつ': 'Ada ist eine objektorientierte Programmiersprache.',
        'Pascalは手続き型プログラミング言語のひとつ': 'Pascal ist eine prozedurale Programmiersprache.',
        '昔からある。汎用のプログラミング言語である。': 'Gibt es schon lange. Es ist eine universelle Programmiersprache.',
        '数値計算に特化したプログラミング言語': 'Auf numerische Berechnungen spezialisierte Programmiersprache.',
        '機械語と1対1に対応するプログラミング言語': 'Programmiersprache mit Eins-zu-Eins-Entsprechung zur Maschinensprache.',
        '手続き型プログラミング言語のひとつ。 名前は「beginners\' all-purpose symbolic instruction code」のバクロニムである。': 'Eine prozedurale Programmiersprache. Der Name ist ein Akronym für "beginners\' all-purpose symbolic instruction code".',
        'オブジェクト指向プログラミング言語': 'Objektorientierte Programmiersprache.',
        '前置記法で記述するプログラミング言語': 'Programmiersprache, die in Präfixnotation geschrieben wird.',
        'MLは関数型プログラミング言語の一つ': 'ML ist eine funktionale Programmiersprache.',
        '関係を定義し問題を解くために使われるプログラミング言語': 'Programmiersprache, die zur Definition von Beziehungen und zur Lösung von Problemen verwendet wird.',
        'OpenGLのシェーダー言語': 'Die Shader-Sprache von OpenGL.',
        'リレーショナルデータを操作するための言語': 'Eine Sprache zur Manipulation relationaler Daten.',
        'Adobeが開発した印刷用のスクリプト言語': 'Eine von Adobe entwickelte Skriptsprache für den Druck.',
        'Windows標準でインストールされている。オブジェクトが扱える。': 'Standardmäßig unter Windows installiert. Kann Objekte manipulieren.',
        'Javaによく似た言語': 'Eine Sprache, die Java sehr ähnlich ist.'
    }
}

for lang, trans_dict in translations.items():
    lang_text = text
    # Double quotes in title
    lang_text = re.sub(r"title:\s*['\"].*?['\"]", f'title: "{trans_dict["title"]}"', lang_text)
    
    # Translate each exact string match
    for jp, trans in trans_dict.items():
        if jp == 'title': continue
        lang_text = lang_text.replace(jp, trans)
        
    # Ensure markdown bold ** has spaces outside if touching word chars
    lang_text = re.sub(r'(?<=\w)\*\*', r' **', lang_text)
    lang_text = re.sub(r'\*\*(?=\w)', r'** ', lang_text)
    
    dest_path = os.path.join(base_dir, f'index.{lang}.md')
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(lang_text)

print('Success')