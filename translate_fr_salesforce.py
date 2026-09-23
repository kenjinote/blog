import codecs

with codecs.open(r'c:\work\kenji.blog\content\post\history-of-salesforce\index.md', 'r', 'utf-8') as f:
    text = f.read()

text = text.replace('title: "企業史: Salesforceの歴史 - SaaS（クラウドソフトウェア）の開拓者"', 'title: "Histoire de l\'entreprise : L\'histoire de Salesforce - Pionnier du SaaS (Logiciel Cloud)"')
text = text.replace('# 企業史: Salesforceの歴史 - SaaS（クラウドソフトウェア）の開拓者', '# Histoire de l\'entreprise : L\'histoire de Salesforce - Pionnier du SaaS (Logiciel Cloud)')
text = text.replace('SalesforceはSaaSのパイオニアです。', 'Salesforce est un pionnier du SaaS.')
text = text.replace('## クラウドコンピューティングの進化', '## L\'évolution du Cloud Computing')
text = text.replace('## 数学モデル', '## Modèle mathématique')
text = text.replace('SaaSの成長モデルは以下のようになります：', 'Le modèle de croissance du SaaS est le suivant :')
text = text.replace('## 追加技術検証パート', '## Partie de vérification technique supplémentaire')
text = text.replace('このセクションでは、さらなる技術的な詳細とケーススタディについて深く掘り下げます。様々な条件下でのパフォーマンスの評価や、他のシステムとの統合に関する課題と解決策を検討します。今後の展望や限界についても考察を行います。', "Dans cette section, nous approfondissons les détails techniques et les études de cas. Nous évaluons les performances dans diverses conditions et examinons les défis et les solutions pour l'intégration avec d'autres systèmes. Nous discutons également des perspectives futures et des limites.")

with codecs.open(r'c:\work\kenji.blog\content\post\history-of-salesforce\index.fr.md', 'w', 'utf-8') as f:
    f.write(text)
