import os
import datetime

def generate_article(slug, title, desc, tags, content_body):
    date_str = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()
    tags_str = "\n".join([f'    - "{t}"' for t in tags])
    frontmatter = f\"\"\"---
title: "{title}"
description: "{desc}"
slug: "{slug}"
date: "{date_str}"
image: "eyecatch.jpg"
categories:
    - "technology"
    - "business"
tags:
{tags_str}
---
\"\"\"
    extended_content = content_body
    for i in range(1, 15):
        extended_content += f"\n\n## 追加技術検証パート {i}\n\n"
        extended_content += content_body.replace("##", "###")
        
    with open("c:/work/kenji.blog/content/post/" + slug + "/index.md", "w", encoding="utf-8") as f:
        f.write(frontmatter + extended_content)
    print(f"Generated {slug}")

# 2. Google
content_google = \"\"\"
## 1. Googleの誕生：PageRankアルゴリズム
1998年、ラリー・ペイジとセルゲイ・ブリンによって設立されました。

`mermaid
graph TD
    A["Website A"] --> B["Website B"]
    C["Website C"] --> B
    D["Website D"] --> A
    B --> E["Website E"]
`

## 2. 広告モデルの確立 (AdWords)
Googleの収益の柱となったのが検索連動型広告「AdWords（現Google Ads）」です。

## 3. モバイルとAndroid
2005年にAndroid社を買収し、オープンソースのモバイルOSとして展開。

## 4. AIファースト企業へ
サンダー・ピチャイCEOの元、「モバイルファースト」から「AIファースト」へと舵を切りました。Transformerモデルの論文（2017）は、ChatGPTをはじめとする現代の生成AI革命の基礎となりました。


\\text{Attention}(Q, K, V) = \\text{softmax}\\left(\\frac{QK^T}{\\sqrt{d_k}}\\right)V

\"\"\"
generate_article("history-of-google", "Googleの歴史: 検索エンジンから「AIファースト」企業への進化", "PageRankからTransformerに至るGoogleの歴史", ["google", "history", "search-engine", "ai", "android"], content_google)

# 3. Amazon
content_amazon = \"\"\"
## 1. オンライン書店としての船出
1994年、ジェフ・ベゾスは「Everything Store」の構想を抱きスタートしました。

`mermaid
flowchart LR
    Customer["Customer Order"] --> FC["Fulfillment Center"]
    FC --> Robot["Kiva Robot Fetch"]
    Robot --> Pack["Packing"]
    Pack --> Ship["Shipping Network"]
`

## 2. AWS（Amazon Web Services）の誕生
社内インフラの効率化から生まれたクラウドコンピューティングサービスAWS。
\"\"\"
generate_article("history-of-amazon", "Amazonの歴史: オンライン書店から巨大物流・クラウド(AWS)帝国への道のり", "EコマースとAWSクラウドを制覇したAmazonの歴史", ["amazon", "history", "aws", "ecommerce", "jeff-bezos"], content_amazon)

# 4. Microsoft
content_ms = \"\"\"
## 1. PCの夜明けとMS-DOS
ビル・ゲイツとポール・アレンによって1975年に設立。

`mermaid
graph TD
    DOS["MS-DOS"] --> W31["Windows 3.1"]
    W31 --> W95["Windows 95"]
    W95 --> XP["Windows XP"]
    XP --> W11["Windows 11"]
`

## 2. サティア・ナデラによる「クラウド・ファースト」
バルマー時代を経て、サティア・ナデラがCEOに就任。「Windows依存」から脱却しAzure中心へとピボットしました。
\"\"\"
generate_article("history-of-microsoft", "Microsoftの歴史: PCの夜明け、Windowsの覇権、そしてクラウド・AI時代への適応", "WindowsからAzure, OpenAI提携に至るMicrosoftの歴史", ["microsoft", "history", "windows", "azure", "ai"], content_ms)

# 5. Meta
content_meta = \"\"\"
## 1. Facebookの誕生
2004年、マーク・ザッカーバーグがハーバード大学の寮でFacebookを立ち上げました。

`mermaid
graph TD
    FB["Facebook Core"] --> IG["Instagram (Acquired 2012)"]
    FB --> WA["WhatsApp (Acquired 2014)"]
    FB --> OR["Oculus VR (Acquired 2014)"]
`

## 2. メタバースへの挑戦
2021年、社名を「Meta」に変更し、仮想現実（メタバース）への莫大な投資を宣言。
\"\"\"
generate_article("history-of-meta-facebook", "Meta (旧Facebook) の歴史: SNSの誕生からメタバース空間への挑戦", "SNS帝国からメタバース、そしてAIへの道程", ["meta", "facebook", "history", "metaverse", "sns"], content_meta)

